"""Offline fixtures only. Never call a provider or alter a real production."""

import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


HOME = Path(__file__).resolve().parents[1]
SCRIPT = HOME / "scripts" / "check_project.py"
SPEC = importlib.util.spec_from_file_location("project_control", SCRIPT)
CONTROL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CONTROL)


class ProjectControlTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="video-control-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.state = json.loads((HOME / "assets" / "project-state.template.json").read_text())
        self.state.update(project_id="fixture", scope="draft", tasks=[])
        for stage in self.state["stages"]:
            stage["applicable"] = True
        for aid in ("ref", "package", "permission", "preflight", "video", "editor"):
            self.add_artifact(aid)
        self.state["checks"] = [
            {"id": k, "kind": k, "artifact": "package", "version": "v1",
             "status": "passed", "evidence": "preflight"}
            for k in ("capability", "authentication", "transport", "price")
        ]
        self.task = {
            "id": "video-job", "stage": "P4", "scope": "draft",
            "operation": "generate_video", "status": "pending", "paid": True,
            "depends_on": [], "input_versions": {"ref": "v1"}, "outputs": ["video"],
            "checks": [c["id"] for c in self.state["checks"]],
            "package": "package", "authorization": "approval", "next_cost": 3,
            "executions": [],
        }
        self.state["tasks"] = [self.task]
        self.grant = {
            "id": "approval", "evidence": "permission", "max_creations": 1,
            "currency": "USD", "amount_limit": 4, "exposure": 0,
            "bindings": {"video-job": {
                "operation": "generate_video", "scope": "draft",
                "package_sha256": self.art("package")["sha256"],
                "input_sha256": {"ref": self.art("ref")["sha256"]},
            }},
        }
        self.state["authorizations"] = [self.grant]

    def add_artifact(self, aid, content=None):
        path = self.root / (aid + ".txt")
        path.write_text(content or ("fixture " + aid), encoding="utf-8")
        self.state["artifacts"].append({
            "id": aid, "path": path.name, "version": "v1",
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        })
        return path

    def art(self, aid):
        return next(a for a in self.state["artifacts"] if a["id"] == aid)

    def execution(self, status, task_id="task-1", created=1, kind="initial"):
        aid = "exec-" + str(len(self.task["executions"]))
        self.add_artifact(aid, json.dumps({"phase": status, "task_id": task_id, "created": created}))
        self.task["executions"].append({
            "artifact": aid, "kind": kind, "status_pointer": "/phase",
            "task_id_pointer": "/task_id", "created_pointer": "/created",
            "status_map": {status: status},
        })

    def question(self, status="open"):
        q = {"id": "Q1", "decision_key": "bob-color", "status": status,
             "blocks": ["video-job"], "question": "Keep the selected color?",
             "why_now": "Changes this reference.", "recommendation": "Keep it.",
             "alternatives": ["Change it."], "decision_evidence": None}
        self.state["questions"].append(q)
        return q

    def clone_task(self, tid="other"):
        t = copy.deepcopy(self.task)
        t["id"], t["executions"] = tid, []
        self.state["tasks"].append(t)
        self.grant["bindings"][tid] = copy.deepcopy(self.grant["bindings"]["video-job"])
        return t

    def run_check(self):
        (self.root / "project-state.json").write_text(json.dumps(self.state), encoding="utf-8")
        return CONTROL.check_project(self.root)

    def codes(self, report, section="blocked"):
        return {i["code"] for i in report[section]}

    def actions(self, report):
        return {i["task_id"]: i["action"] for i in report["can_continue"]}

    def test_template_safe_and_cli_success(self):
        (self.root / "project-state.json").write_bytes((HOME / "assets" / "project-state.template.json").read_bytes())
        run = subprocess.run([sys.executable, str(SCRIPT), "--project", str(self.root)],
                             capture_output=True, text=True, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(json.loads(run.stdout)["can_continue"][0]["action"], "execute_local")

    def test_unchanged_authorization_needs_no_new_question(self):
        r = self.run_check()
        self.assertEqual(r["blocked"], [])
        self.assertEqual(r["questions"], [])
        self.assertEqual(self.actions(r)["video-job"], "submit_candidate")

    def test_selection_is_not_spending_authorization(self):
        self.art("ref").update(requires_selection=True, selected=True, selection_evidence="permission")
        self.task["authorization"] = None
        self.assertIn("authorization_missing", self.codes(self.run_check()))

    def test_spending_does_not_select_frame(self):
        self.art("ref").update(requires_selection=True, selected=False)
        self.assertIn("selection_missing", self.codes(self.run_check()))

    def test_generate_marked_free_still_requires_permission(self):
        self.task.update(paid=False, authorization=None)
        self.assertIn("authorization_missing", self.codes(self.run_check()))

    def test_preflight_required(self):
        self.task["checks"].remove("price")
        self.assertIn("preflight_missing", self.codes(self.run_check()))

    def test_file_changed_without_hash_update(self):
        (self.root / "ref.txt").write_text("different bytes")
        self.assertIn("artifact_missing_or_changed", self.codes(self.run_check()))

    def test_package_hash_change_invalidates_binding(self):
        p = self.root / "package.txt"
        p.write_text("different prompt/settings")
        self.art("package")["sha256"] = CONTROL.digest(p)
        self.assertIn("package_changed", self.codes(self.run_check()))

    def test_new_input_hash_even_same_version_invalidates_binding(self):
        p = self.root / "ref.txt"
        p.write_text("repaired ear")
        self.art("ref")["sha256"] = CONTROL.digest(p)
        self.assertIn("input_hash_changed", self.codes(self.run_check()))

    def test_only_changed_reference_dependents_block(self):
        other = self.clone_task()
        self.add_artifact("other-ref")
        other["input_versions"] = {"other-ref": "v1"}
        self.grant["bindings"]["other"]["input_sha256"] = {"other-ref": self.art("other-ref")["sha256"]}
        self.art("ref")["version"] = "v2"
        r = self.run_check()
        self.assertIn("input_version_changed", self.codes(r))
        self.assertIn("other", self.actions(r))
        self.assertNotIn("video-job", self.actions(r))

    def test_stale_required_check_is_local(self):
        other = self.clone_task()
        other["operation"], other["paid"], other["checks"] = "analyze", False, []
        self.state["checks"][0]["version"] = "v0"
        r = self.run_check()
        self.assertIn("check_version_changed", self.codes(r))
        self.assertEqual(self.actions(r)["other"], "execute_local")

    def test_repair_counts_against_authorized_creations(self):
        self.execution("failed")
        self.execution("failed", task_id="task-2", kind="repair")
        self.grant["max_creations"] = 2
        r = self.run_check()
        self.assertIn("creation_limit", self.codes(r))
        self.assertEqual(r["authorization_usage"][0]["recorded_or_reserved_creations"], 2)

    def test_upload_failure_is_not_a_created_video(self):
        self.execution("upload_failed", None, 0)
        r = self.run_check()
        self.assertEqual(r["authorization_usage"][0]["recorded_or_reserved_creations"], 0)
        self.assertEqual(self.actions(r)["video-job"], "submit_candidate")

    def test_unknown_creation_reserves_one_and_never_recreates(self):
        self.execution("unknown", None, 0)
        r = self.run_check()
        self.assertIn("submission_unknown", self.codes(r))
        self.assertNotIn("video-job", self.actions(r))
        self.assertEqual(r["authorization_usage"][0]["recorded_or_reserved_creations"], 1)

    def test_queued_task_is_query_only(self):
        self.execution("queued")
        self.assertEqual(self.actions(self.run_check())["video-job"], "query_existing")

    def test_success_with_missing_download_only_recovers(self):
        self.execution("succeeded")
        (self.root / "video.txt").unlink()
        self.assertEqual(self.actions(self.run_check())["video-job"], "verify_or_download_existing")

    def test_completed_task_does_not_recreate(self):
        self.execution("succeeded")
        self.task["status"] = "completed"
        r = self.run_check()
        self.assertEqual(r["blocked"], [])
        self.assertNotIn("video-job", self.actions(r))

    def test_missing_completed_output_blocks_downstream(self):
        self.execution("succeeded")
        self.task["status"] = "completed"
        other = self.clone_task()
        other.update(status="pending", paid=False, operation="edit", depends_on=["video-job"])
        (self.root / "video.txt").unlink()
        r = self.run_check()
        self.assertIn("dependency_blocked", self.codes(r))
        self.assertNotIn("other", self.actions(r))

    def test_unreadable_execution_prevents_new_paid_work(self):
        self.execution("queued")
        self.task["executions"][0]["status_pointer"] = "/does-not-exist"
        self.clone_task()
        r = self.run_check()
        self.assertIn("execution_invalid", self.codes(r))
        self.assertIn("ledger_unreconciled", self.codes(r))

    def test_duplicate_execution_not_double_counted(self):
        self.execution("failed")
        self.task["executions"].append(copy.deepcopy(self.task["executions"][0]))
        self.assertIn("execution_invalid", self.codes(self.run_check()))

    def test_synchronous_image_result_needs_no_fake_task_id(self):
        self.task.update(operation="generate_image", status="completed")
        self.execution("succeeded", None, 1)
        self.task["executions"][0]["synchronous"] = True
        self.assertEqual(self.run_check()["blocked"], [])

    def test_video_cannot_claim_synchronous_exemption(self):
        self.execution("succeeded", None, 1)
        self.task["executions"][0]["synchronous"] = True
        self.assertIn("state_invalid", self.codes(self.run_check()))

    def test_malformed_ledger_does_not_block_separate_grant(self):
        self.execution("queued")
        self.task["executions"][0]["status_pointer"] = "/missing"
        other = self.clone_task()
        grant = copy.deepcopy(self.grant)
        grant["id"] = "separate"
        other["authorization"] = "separate"
        self.state["authorizations"].append(grant)
        self.assertEqual(self.actions(self.run_check())["other"], "submit_candidate")

    def test_identical_bytes_at_new_local_transport_path_reuse_grant(self):
        p = self.root / "reference-from-drive.txt"
        p.write_bytes((self.root / "ref.txt").read_bytes())
        self.art("ref")["path"] = p.name
        self.assertEqual(self.run_check()["blocked"], [])

    def test_duplicate_provider_id_is_reconciled(self):
        self.execution("failed")
        self.execution("failed")
        self.assertIn("execution_invalid", self.codes(self.run_check()))

    def test_budget_unknown_is_not_zero(self):
        self.grant["exposure"] = None
        self.assertIn("budget_unknown", self.codes(self.run_check()))

    def test_budget_limit(self):
        self.grant["exposure"] = 2
        self.assertIn("budget_limit", self.codes(self.run_check()))

    def test_shared_count_not_offered_twice(self):
        self.clone_task()
        r = self.run_check()
        self.assertEqual(len(self.actions(r)), 1)
        self.assertIn("creation_limit", self.codes(r))

    def test_shared_money_not_offered_twice(self):
        self.clone_task()
        self.grant["max_creations"] = 2
        r = self.run_check()
        self.assertEqual(len(self.actions(r)), 1)
        self.assertIn("budget_limit", self.codes(r))

    def test_question_blocks_only_its_targets(self):
        self.question()
        self.clone_task()
        r = self.run_check()
        self.assertNotIn("video-job", self.actions(r))
        self.assertIn("other", self.actions(r))
        self.assertEqual(len(r["questions"]), 1)

    def test_resolved_question_not_repeated(self):
        self.question("resolved").update(answer="Keep.", decision_evidence="permission")
        self.assertEqual(self.run_check()["questions"], [])

    def test_duplicate_decision_key_rejected(self):
        q = self.question()
        duplicate = copy.deepcopy(q)
        duplicate["id"] = "Q2"
        self.state["questions"].append(duplicate)
        self.assertIn("state_invalid", self.codes(self.run_check()))

    def test_unchecked_listening_not_falsely_passed(self):
        self.state["checks"].append({"id": "listen", "artifact": "video", "version": "v1",
                                    "kind": "listening", "status": "not-checked", "evidence": None})
        r = self.run_check()
        self.assertIn("uninspected", self.codes(r, "warnings"))
        self.assertEqual(r["blocked"], [])
        self.task["checks"].append("listen")
        self.assertIn("check_not_satisfied", self.codes(self.run_check()))

    def test_waiver_requires_evidence_and_reason(self):
        self.state["checks"][0].update(status="waived", reason="", evidence=None)
        self.assertIn("check_evidence_missing", self.codes(self.run_check()))

    def test_praise_does_not_activate_formal_scope(self):
        self.task["scope"] = "formal"
        self.assertEqual(self.actions(self.run_check()), {})

    def test_draft_does_not_need_formal_stage(self):
        self.state["stages"][5].update(applicable=False, reason="No formal delivery requested.")
        self.assertNotIn("stage_evidence_missing", self.codes(self.run_check()))

    def test_stage_completion_requires_evidence(self):
        self.state["stages"][0]["status"] = "passed"
        self.assertIn("stage_evidence_missing", self.codes(self.run_check()))

    def test_editor_version_mismatch_is_reported(self):
        self.state["delivery"] = {"artifact": "video", "cut_version": "v2",
                                  "editor": "editor", "editor_cut_version": "v1"}
        self.assertIn("editor_version_mismatch", self.codes(self.run_check(), "warnings"))

    def test_dependency_cycle_rejected(self):
        other = self.clone_task()
        other["depends_on"] = ["video-job"]
        self.task["depends_on"] = ["other"]
        self.assertIn("state_invalid", self.codes(self.run_check()))

    def test_bad_count_type_fails_closed(self):
        self.grant["max_creations"] = True
        self.assertIn("state_invalid", self.codes(self.run_check()))

    def test_missing_legacy_state_never_invents_approval(self):
        self.assertIn("state_invalid", self.codes(CONTROL.check_project(self.root)))

    def test_explicit_legacy_index_is_external_and_read_only(self):
        mapping = self.root / "mapping.json"
        mapping.write_text(json.dumps(self.state))
        r = CONTROL.check_project(self.root, state_file=mapping)
        self.assertEqual(r["blocked"], [])
        self.assertFalse((self.root / "project-state.json").exists())

    def test_no_project_writes(self):
        self.run_check()
        before = {p.name: p.read_bytes() for p in self.root.iterdir()}
        CONTROL.check_project(self.root, event="feedback")
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.root.iterdir()})

    def test_deleted_artifact_is_not_restored(self):
        (self.root / "ref.txt").unlink()
        self.run_check()
        self.assertFalse((self.root / "ref.txt").exists())


if __name__ == "__main__":
    unittest.main()
