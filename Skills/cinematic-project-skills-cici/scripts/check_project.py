#!/usr/bin/env python3
"""Read-only project checks. No network, writes, generation, or permission grants."""

import argparse
import hashlib
import json
import math
import re
from pathlib import Path


EVENTS = ("resume", "change", "keyframes", "pre-submit", "task-update",
          "edit", "pre-export", "post-export", "feedback")
STAGE_STATUS = {"not-started", "in-progress", "ready-for-review", "passed",
                "blocked", "needs-recheck"}
TASK_STATUS = {"pending", "in-progress", "completed", "blocked", "needs-recheck"}
REMOTE_STATUS = {"unknown", "upload_failed", "queued", "running", "succeeded",
                 "failed", "cancelled", "expired"}
ACTIVE_QUESTIONS = {"open", "asked", "deferred"}
OPERATIONS = {"analyze", "generate_image", "generate_video", "edit", "export",
              "generate_audio", "publish"}
GATED = {"generate_image", "generate_video", "generate_audio", "publish"}
HASH = re.compile(r"[0-9a-f]{64}")


class Invalid(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise Invalid(message)


def text(value):
    return isinstance(value, str) and bool(value.strip())


def strings(value):
    return isinstance(value, list) and all(text(x) for x in value) and len(set(value)) == len(value)


def count(value):
    return type(value) is int and value >= 0


def money(value):
    return value is None or (type(value) in (int, float) and math.isfinite(value) and value >= 0)


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def pointer(data, selector):
    """Resolve explicit RFC6901 pointers, including null at an existing key."""
    require(isinstance(selector, str) and selector.startswith("/"), "pointer must start with /")
    for token in selector[1:].split("/"):
        key = token.replace("~1", "/").replace("~0", "~")
        try:
            data = data[int(key)] if isinstance(data, list) else data[key]
        except (KeyError, IndexError, TypeError, ValueError):
            raise Invalid("execution pointer does not resolve") from None
    return data


def validate(state):
    require(isinstance(state, dict) and state.get("schema_version") == 1, "schema_version must be 1")
    for key in ("project_id", "workflow_owner", "scope"):
        require(text(state.get(key)), key + " is required")
    tables = {}
    for name in ("artifacts", "stages", "tasks", "authorizations", "checks", "questions"):
        rows = state.get(name)
        require(isinstance(rows, list), name + " must be a list")
        require(all(isinstance(r, dict) and text(r.get("id")) for r in rows), name + " requires IDs")
        require(len({r["id"] for r in rows}) == len(rows), name + " has duplicate IDs")
        tables[name] = {r["id"]: r for r in rows}
    artifacts, stages, tasks, grants, checks, questions = (tables[n] for n in tables)
    require(set(stages) == {"P1", "P2", "P3", "P4", "P5", "P6"}, "stages must contain P1-P6")
    for a in artifacts.values():
        require(text(a.get("path")) and text(a.get("version")), "artifact path/version required")
        require(a.get("sha256") is None or bool(HASH.fullmatch(str(a["sha256"]))), "invalid SHA256")
        require(type(a.get("requires_selection", False)) is bool, "requires_selection must be boolean")
        require(type(a.get("selected", False)) is bool, "selected must be boolean")
    for s in stages.values():
        require(s.get("status") in STAGE_STATUS and type(s.get("applicable")) is bool, "invalid stage")
        for key, catalog in (("inputs", artifacts), ("outputs", artifacts), ("checks", checks)):
            require(strings(s.get(key)) and set(s[key]) <= set(catalog), "invalid stage " + key)
        require(s["applicable"] or text(s.get("reason")), "out-of-scope stage needs reason")
        require(text(s.get("next_action")), "stage needs next_action")
    for c in checks.values():
        require(c.get("artifact") in artifacts, "check target missing")
        require(text(c.get("version")), "check version required")
        require(c.get("kind") in {"frames", "playback", "listening", "technical", "semantic",
                                 "user_feedback", "capability", "transport", "price", "authentication"}, "invalid check kind")
        require(c.get("status") in {"not-checked", "passed", "failed", "waived"}, "invalid check status")
        require(c.get("evidence") is None or c["evidence"] in artifacts, "check evidence missing")
    for t in tasks.values():
        require(t.get("stage") in stages and text(t.get("scope")), "invalid task stage/scope")
        require(t.get("status") in TASK_STATUS and t.get("operation") in OPERATIONS, "invalid task")
        require(type(t.get("paid")) is bool and money(t.get("next_cost")), "invalid task cost")
        for key, catalog in (("depends_on", tasks), ("outputs", artifacts), ("checks", checks)):
            require(strings(t.get(key)) and set(t[key]) <= set(catalog), "invalid task " + key)
        require(t["id"] not in t["depends_on"], "self dependency")
        require(isinstance(t.get("input_versions"), dict), "task input_versions must be an object")
        require(set(t["input_versions"]) <= set(artifacts) and
                all(text(v) for v in t["input_versions"].values()), "invalid task inputs")
        require(t.get("authorization") is None or t["authorization"] in grants, "unknown authorization")
        require(t.get("package") is None or t["package"] in artifacts, "unknown package")
        require(isinstance(t.get("executions"), list), "executions must be a list")
        for e in t["executions"]:
            require(isinstance(e, dict) and e.get("artifact") in artifacts, "execution artifact missing")
            require(e.get("kind") in {"initial", "repair"}, "execution kind must be initial/repair")
            require(type(e.get("synchronous", False)) is bool, "synchronous must be boolean")
            require(not e.get("synchronous") or t["operation"] in {"generate_image", "generate_audio"},
                    "synchronous execution only applies to image/audio results")
            for k in ("status_pointer", "task_id_pointer", "created_pointer"):
                require(text(e.get(k)) and e[k].startswith("/"), "invalid execution pointer")
            require(isinstance(e.get("status_map"), dict) and bool(e["status_map"]) and
                    all(text(k) and v in REMOTE_STATUS for k, v in e["status_map"].items()),
                    "invalid execution status map")
    visiting, done = set(), set()

    def visit(tid):
        require(tid not in visiting, "task dependency cycle")
        if tid in done:
            return
        visiting.add(tid)
        for dep in tasks[tid]["depends_on"]:
            visit(dep)
        visiting.remove(tid)
        done.add(tid)
    for tid in tasks:
        visit(tid)
    for g in grants.values():
        require(g.get("evidence") in artifacts and count(g.get("max_creations")), "invalid grant")
        require(isinstance(g.get("bindings"), dict) and bool(g["bindings"]) and
                set(g["bindings"]) <= set(tasks), "invalid grant bindings")
        for tid, b in g["bindings"].items():
            require(isinstance(b, dict) and b.get("operation") in OPERATIONS and text(b.get("scope")),
                    "invalid grant binding")
            require(bool(HASH.fullmatch(str(b.get("package_sha256", "")))), "grant needs package SHA256")
            require(isinstance(b.get("input_sha256"), dict) and
                    set(b["input_sha256"]) <= set(artifacts) and
                    all(HASH.fullmatch(str(h)) for h in b["input_sha256"].values()), "invalid grant inputs")
        require(money(g.get("amount_limit")) and money(g.get("exposure")), "invalid budget amounts")
        require(text(g.get("currency")), "grant needs currency")
    keys = set()
    for q in questions.values():
        require(text(q.get("decision_key")) and q["decision_key"] not in keys, "duplicate/missing decision_key")
        keys.add(q["decision_key"])
        require(q.get("status") in ACTIVE_QUESTIONS | {"resolved", "not-applicable"}, "invalid question status")
        require(strings(q.get("blocks")) and set(q["blocks"]) <= set(tasks), "invalid question targets")
        for k in ("question", "why_now", "recommendation"):
            require(text(q.get(k)), "question needs " + k)
        require(strings(q.get("alternatives")) and q["alternatives"], "question needs alternatives")
        require(q.get("decision_evidence") is None or q["decision_evidence"] in artifacts, "invalid decision evidence")
    delivery = state.get("delivery")
    require(delivery is None or isinstance(delivery, dict), "invalid delivery")
    if delivery:
        require(delivery.get("artifact") in artifacts and text(delivery.get("cut_version")), "invalid delivery artifact")
        require(delivery.get("editor") in artifacts and text(delivery.get("editor_cut_version")), "invalid editor")
    return tables


def check_project(project, event="resume", state_file=None):
    root = Path(project).resolve()
    result = {"schema_version": 1, "event": event, "read_only": True,
              "can_continue": [], "blocked": [], "questions": [], "warnings": [], "progress": []}

    def issue(section, code, owner, message):
        item = {"code": code, "owner": owner, "message": message}
        if item not in result[section]:
            result[section].append(item)

    try:
        require(event in EVENTS, "unknown event")
        path = Path(state_file) if state_file else root / "project-state.json"
        if not path.is_absolute():
            path = root / path
        state = json.loads(path.read_text(encoding="utf-8"))
        tables = validate(state)
    except Invalid as error:
        issue("blocked", "state_invalid", "project", str(error))
        return result
    except (OSError, ValueError, RecursionError):
        issue("blocked", "state_invalid", "project",
              "Missing/invalid state or references; inspect the local schema contract. Do not infer approval.")
        return result

    arts, stages, tasks, grants, checks, questions = (tables[n] for n in tables)
    cache = {}

    def artifact(aid, owner, need_hash=False):
        a = arts[aid]
        if aid not in cache:
            try:
                p = Path(a["path"])
                require("://" not in a["path"], "local paths only")
                p = p if p.is_absolute() else root / p
                require(p.is_file() and p.stat().st_size > 0, "missing/empty artifact")
                actual = digest(p) if a.get("sha256") or need_hash else None
                require(not a.get("sha256") or actual == a["sha256"], "hash mismatch")
                cache[aid] = (p, actual, None)
            except (OSError, Invalid):
                cache[aid] = (None, None, "artifact_missing_or_changed")
        p, actual, error = cache[aid]
        if error:
            issue("blocked", error, owner, "Required artifact " + aid + " is missing, empty or changed.")
            return None
        if need_hash:
            if not a.get("sha256"):
                issue("blocked", "hash_required", owner, "Pin SHA256 for " + aid + " before protected work.")
                return None
        return p

    def check_evidence(cid, owner):
        c = checks[cid]
        if c["version"] != arts[c["artifact"]]["version"]:
            issue("blocked", "check_version_changed", owner, "Required check " + cid + " describes an older version.")
            return
        if c["status"] not in {"passed", "waived"}:
            issue("blocked", "check_not_satisfied", owner, "Required check " + cid + " is " + c["status"] + ".")
            return
        if not c.get("evidence") or (c["status"] == "waived" and not text(c.get("reason"))):
            issue("blocked", "check_evidence_missing", owner, "Check " + cid + " needs evidence/waiver rationale.")
        else:
            artifact(c["artifact"], owner)
            artifact(c["evidence"], owner)

    for c in checks.values():
        if c["status"] == "not-checked":
            issue("warnings", "uninspected", c["id"], c["kind"] + " has not been checked; this is not a pass.")
    for q in questions.values():
        if q["status"] in ACTIVE_QUESTIONS:
            result["questions"].append(q)
            for tid in q["blocks"]:
                if tasks[tid]["scope"] == state["scope"]:
                    issue("blocked", "question_open", tid, "Decision " + q["id"] + " is unresolved.")
        elif q["status"] == "resolved":
            if not text(q.get("answer")) or not q.get("decision_evidence"):
                issue("blocked", "decision_evidence_missing", "project", "Resolved question " + q["id"] + " lacks evidence.")
            else:
                artifact(q["decision_evidence"], "project")
        elif not text(q.get("reason")):
            issue("blocked", "decision_reason_missing", "project", q["id"] + " needs a not-applicable reason.")

    remote, used = {}, {gid: 0 for gid in grants}
    seen_records, seen_ids = set(), set()
    bad_ledgers = set()
    for tid, t in tasks.items():
        remote[tid] = []
        for e in t["executions"]:
            p = artifact(e["artifact"], tid)
            if not p:
                bad_ledgers.add(t["authorization"] or "*")
                continue
            try:
                require(p.resolve() not in seen_records, "execution record listed twice")
                seen_records.add(p.resolve())
                data = json.loads(p.read_text(encoding="utf-8"))
                raw = pointer(data, e["status_pointer"])
                require(isinstance(raw, str) and raw in e["status_map"], "unmapped execution state")
                status = e["status_map"][raw]
                provider_id = pointer(data, e["task_id_pointer"])
                created = pointer(data, e["created_pointer"])
                require(count(created), "invalid created count")
                require(provider_id is None or text(provider_id), "invalid task ID")
                synchronous = e.get("synchronous") and status in {"succeeded", "failed"}
                require(status == "unknown" or status == "upload_failed" or
                        (created > 0 and (text(provider_id) or synchronous)),
                        "known remote state requires ID and creation count")
                require(status != "upload_failed" or (created == 0 and provider_id is None), "inconsistent upload failure")
                require(not provider_id or provider_id not in seen_ids, "task ID counted twice")
                if provider_id:
                    seen_ids.add(provider_id)
                remote[tid].append((status, provider_id))
                if t["authorization"]:
                    used[t["authorization"]] += max(created, 1 if status == "unknown" else 0)
                elif created or status == "unknown":
                    issue("warnings", "historical_authorization_unmapped", tid, "Existing execution has no mapped grant; do not invent one.")
            except (OSError, ValueError, TypeError):
                bad_ledgers.add(t["authorization"] or "*")
                issue("blocked", "execution_invalid", tid, "Reconcile the explicit execution mapping before any new protected work.")
        if t["status"] == "completed":
            if not t["outputs"]:
                issue("blocked", "output_missing", tid, "Completed task needs an actual output.")
            for aid in t["outputs"]:
                artifact(aid, tid)
            if (t["paid"] or t["operation"] in GATED) and not any(s == "succeeded" for s, _ in remote[tid]):
                issue("blocked", "completion_unproven", tid, "Protected task completion lacks a succeeded execution.")
            if any(s in {"unknown", "queued", "running"} for s, _ in remote[tid]):
                issue("blocked", "execution_unfinished", tid, "Completed task still contains an unfinished execution.")

    def blocked(owner):
        return any(i["owner"] in {owner, "project"} for i in result["blocked"])

    for tid, t in tasks.items():
        if t["scope"] != state["scope"] or not stages[t["stage"]]["applicable"]:
            continue
        if t["status"] in {"blocked", "needs-recheck"}:
            issue("blocked", "task_requires_review", tid, "Resolve the recorded block/recheck; do not resubmit.")
        for aid, version in t["input_versions"].items():
            if version != arts[aid]["version"]:
                issue("blocked", "input_version_changed", tid, "Input " + aid + " changed; recheck only dependent work.")
            artifact(aid, tid)
        for cid in t["checks"]:
            check_evidence(cid, tid)
        for dep in t["depends_on"]:
            if tasks[dep]["status"] != "completed":
                issue("blocked", "dependency_incomplete", tid, "Dependency " + dep + " is not complete.")

    # Propagate failed evidence through the DAG, not to unrelated tasks.
    for _ in tasks:
        for tid, t in tasks.items():
            if t["scope"] == state["scope"]:
                for dep in t["depends_on"]:
                    if blocked(dep):
                        issue("blocked", "dependency_blocked", tid, "Dependency " + dep + " needs reconciliation.")

    remaining = {gid: max(0, g["max_creations"] - used[gid]) for gid, g in grants.items()}
    money_left = {gid: None if g.get("amount_limit") is None or g.get("exposure") is None
                  else g["amount_limit"] - g["exposure"] for gid, g in grants.items()}
    for gid, g in grants.items():
        if used[gid] > g["max_creations"]:
            issue("warnings", "creation_limit_exceeded", gid, "Recorded executions exceed the authorized creation count.")
    for tid, t in tasks.items():
        if t["scope"] != state["scope"] or not stages[t["stage"]]["applicable"] or t["status"] == "completed":
            continue
        statuses = remote[tid]
        recovery = None
        if any(s == "unknown" for s, _ in statuses):
            issue("blocked", "submission_unknown", tid, "Reconcile the existing submission; no new request.")
        elif any(s in {"queued", "running"} for s, _ in statuses):
            recovery = "query_existing"
        elif any(s == "succeeded" for s, _ in statuses):
            recovery = "verify_or_download_existing"
        if recovery:
            # Recovery is read-only and remains useful even while creative work is blocked.
            result["can_continue"].append({"task_id": tid, "action": recovery,
                                          "provider_task_ids": [i for _, i in statuses if i]})
            continue
        if blocked(tid):
            continue
        protected = t["paid"] or t["operation"] in GATED
        if protected:
            gid = t["authorization"]
            if not gid:
                issue("blocked", "authorization_missing", tid, "Record matching existing permission or obtain uncovered scope approval.")
                continue
            if gid in bad_ledgers or "*" in bad_ledgers:
                issue("blocked", "ledger_unreconciled", tid, "Reconcile unreadable executions charged to this grant before new work.")
                continue
            if t["operation"].startswith("generate_"):
                kinds = {checks[cid]["kind"] for cid in t["checks"]}
                if not {"capability", "authentication", "transport", "price"} <= kinds:
                    issue("blocked", "preflight_missing", tid, "Generation needs capability, authentication, transport and price evidence.")
            g = grants[gid]
            artifact(g["evidence"], tid)
            b = g["bindings"].get(tid)
            if not b or b["operation"] != t["operation"] or b["scope"] != t["scope"] or not t["package"]:
                issue("blocked", "authorization_mismatch", tid, "Grant does not cover this operation/scope/package.")
                continue
            p = artifact(t["package"], tid, True)
            if p and arts[t["package"]]["sha256"] != b["package_sha256"]:
                issue("blocked", "package_changed", tid, "Current package differs from the recorded grant.")
            if set(t["input_versions"]) != set(b["input_sha256"]):
                issue("blocked", "input_set_changed", tid, "Actual inputs differ from the recorded grant.")
            for aid in t["input_versions"]:
                artifact(aid, tid, True)
                if arts[aid].get("sha256") != b["input_sha256"].get(aid):
                    issue("blocked", "input_hash_changed", tid, "Input " + aid + " differs from the grant.")
                a = arts[aid]
                if a.get("requires_selection"):
                    if not a.get("selected") or a.get("selection_evidence") not in arts:
                        issue("blocked", "selection_missing", tid, "Required input " + aid + " is not selected with evidence.")
                    else:
                        artifact(a["selection_evidence"], tid)
            if remaining[gid] < 1:
                issue("blocked", "creation_limit", tid, "No unallocated authorized creation remains (repairs count too).")
            if g.get("amount_limit") is not None:
                if money_left[gid] is None or t.get("next_cost") is None:
                    issue("blocked", "budget_unknown", tid, "Budget exposure or next cost is unknown, not zero.")
                elif t["next_cost"] > money_left[gid]:
                    issue("blocked", "budget_limit", tid, "Next operation exceeds the remaining monetary limit.")
            if not blocked(tid):
                remaining[gid] -= 1
                if money_left[gid] is not None and t.get("next_cost") is not None:
                    money_left[gid] -= t["next_cost"]
        if not blocked(tid):
            result["can_continue"].append({"task_id": tid, "action": "submit_candidate" if protected else "execute_local",
                                          "note": "Record checks only; not permission or a quality verdict."})

    for sid, s in stages.items():
        result["progress"].append({"stage": sid, "applicable": s["applicable"],
                                   "recorded_status": s["status"], "next_action": s["next_action"]})
        if not s["applicable"]:
            continue
        if s["status"] == "passed":
            if not s["outputs"] or not s["checks"]:
                issue("blocked", "stage_evidence_missing", sid, "Passed stage needs outputs and explicit exit checks.")
            for aid in s["inputs"] + s["outputs"]:
                artifact(aid, sid)
            for cid in s["checks"]:
                check_evidence(cid, sid)
            for tid, t in tasks.items():
                if t["stage"] == sid and t["scope"] == state["scope"] and (t["status"] != "completed" or blocked(tid)):
                    issue("blocked", "stage_task_unfinished", sid, "Passed stage includes unfinished/recheck task " + tid + ".")
    delivery = state.get("delivery")
    if delivery:
        artifact(delivery["artifact"], "delivery")
        artifact(delivery["editor"], "delivery")
        if delivery["cut_version"] != delivery["editor_cut_version"]:
            issue("warnings", "editor_version_mismatch", "delivery", "Export and editor describe different cuts; label honestly.")
    result["authorization_usage"] = [{"id": gid, "recorded_or_reserved_creations": used[gid],
                                     "authorized_max": g["max_creations"]} for gid, g in grants.items()]
    result["project_id"], result["scope"] = state["project_id"], state["scope"]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True)
    parser.add_argument("--state", help="Explicit state index, including an external temporary legacy mapping")
    parser.add_argument("--event", choices=EVENTS, default="resume")
    parser.add_argument("--format", choices=("json", "text"), default="json")
    args = parser.parse_args()
    report = check_project(args.project, args.event, args.state)
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        for key in ("progress", "can_continue", "blocked", "questions", "warnings"):
            print(key + ":")
            for item in report[key]:
                print("  " + json.dumps(item, ensure_ascii=False))
    return 2 if report["blocked"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
