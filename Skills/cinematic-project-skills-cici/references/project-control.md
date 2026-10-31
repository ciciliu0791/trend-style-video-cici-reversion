# Shared project control

Use this contract for an ongoing production, revision or delivery. It is a control layer, not another creative workflow or permission authority. Keep one `workflow_owner`; importing a character profile does not activate its entire series workflow. Preserve each owner's applicable review gates and current tool/workspace requirements.

## Records and initialization

- `PROJECT.md` is the human entry point. Maintain its marked progress/questions region from the current state, without overwriting user prose.
- `project-state.json` indexes stages, dependencies, evidence and decisions. Start with `assets/project-state.template.json`, replace the ID and scope, and activate only stages in the actual request.
- Approved packages and actual user confirmations remain authoritative for permission. Never edit an old approved snapshot to match a new request.
- Execution files and actual output bytes remain authoritative for task outcomes. The state only maps them; it is not another invented execution history.
- Preserve existing layouts. For legacy work, create an explicit small index or use `--state /absolute/path/to/temporary-index.json` for read-only evaluation. Do not auto-migrate old contracts or manufacture missing approval.
- Planning and skill maintenance do not require a new production index or media generation. The shipped template exposes only a local analysis candidate, no paid authorization.

All indexed paths are local files, relative to the project directory or absolute, including when the index is outside that directory. URLs are not file evidence. Keep secrets, base64 and signed URLs out of shared records and checker output. Temporary scripts/caches are not required permanent evidence.

## When to run

Resolve the script path relative to this reference's skill directory, then run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 "<cici-skill>/scripts/check_project.py" \
  --project "<project-directory>" --event resume --format json
```

Events: `resume`, `change`, `keyframes`, `pre-submit`, `task-update`, `edit`, `pre-export`, `post-export`, `feedback`.

1. Recover current versions and recorded decisions before asking anything.
2. On an event, reconcile affected source records and update their state index. Before submission, register the exact candidate and examine existing executions first.
3. Run the checker. Read all four groups, not only the exit code. Fix machine-verifiable defects yourself.
4. Continue independent covered work. Resolve recorded questions only when they require user choice/action. Do not bypass affected blocks by editing status flags.
5. Update `last_event` and the PROJECT summary after reconciling the result. The checker never writes either file.

Use `task-update` after creation or a meaningful terminal/failure transition, not a full hash sweep on every unchanged poll. Each invocation currently performs a full indexed check; it is not an incremental engine or a daemon. Reuse still-valid preflight evidence; refresh it when its model, input, access or other controlling condition changes.

Exit `0` means no recorded blocks; `2` means one or more blocks (including invalid/missing state). Warnings do not change the exit code. Both exits return JSON unless `--format text` is selected.

`can_continue` actions:

| Action | Meaning |
|---|---|
| `execute_local` | Candidate local task, subject to the user's request |
| `submit_candidate` | Records allow one candidate within the indexed limits; still verify actual intent, tool requirements and actual request bytes |
| `query_existing` | Query the listed existing remote IDs, never create a replacement |
| `verify_or_download_existing` | Verify/download that succeeded output; never regenerate for a missing download |

Read-only recovery may be offered while creative changes block new work. Unknown creation is a block, not permission to retry. A known failure may permit a repair only when the same exact package and explicit remaining grant cover it.

## State contract, version 1

Root fields: `schema_version: 1`, nonempty `project_id`, `workflow_owner`, `scope`; arrays `artifacts`, `stages`, `tasks`, `authorizations`, `checks`, `questions`; optional `delivery`, `character_profiles`, `last_event`.

Scope is a named current deliverable, for example `planning`, `images`, `draft` or `formal`. A task in a different scope is not proposed for execution. Do not silently change scope to consume an old grant. There is no universal percentage complete.

### Artifacts and evidence

An artifact has `id`, `path`, `version`, optional `sha256`. Pin lowercase SHA256 for current paid inputs and packages. Missing future outputs can be listed, but completed tasks and passed stages must have nonempty actual outputs. Hash mismatches block dependent work rather than restoring files.

For an input whose visual selection was reserved, add `requires_selection: true`, `selected: true/false`, and `selection_evidence: <artifact-id>`. Existing valid choices satisfy this; no per-image spending gate is introduced.

A check has `id`, target `artifact`, target `version`, `kind`, `status`, and `evidence` (artifact ID or null). Kinds are `frames`, `playback`, `listening`, `technical`, `semantic`, `user_feedback`, `capability`, `authentication`, `transport`, `price`.

Statuses: `not-checked`, `passed`, `failed`, `waived`. Passed checks require a nonempty evidence file; waived checks also require a `reason`. A waiver must reflect the real allowed exception, not the Agent's convenience. Evidence tied to an old target version needs recheck.

Unperformed checks produce warnings unless listed as requirements of the next task or a passed stage. They are never silently passed. A feedback check does not replace playback, listening or technical checks. The Agent must choose the relevant exit checks for the workflow; the script cannot decide which artistic checks matter.

### Stages and tasks

Keep stages `P1` development, `P2` direction, `P3` preparation, `P4` production, `P5` editorial, `P6` delivery.

Each stage has `id`, `applicable`, `status`, `inputs`, `outputs`, `checks`, `next_action`; an inapplicable stage also has a `reason`. Statuses are `not-started`, `in-progress`, `ready-for-review`, `passed`, `blocked`, `needs-recheck`. Passed stages need outputs, satisfied exit checks and completed scoped tasks.

A task has:

- Stable `id`, `stage`, `scope`, `operation`, `status`, boolean `paid`.
- `depends_on`: task IDs. The graph must be acyclic; dependents need completed, reconciled inputs.
- `input_versions`: artifact ID to selected version; `outputs`: artifact IDs.
- `checks`: required check IDs. All new generation candidates require capability, authentication, transport and price evidence.
- `package`: frozen-package artifact ID or null; `authorization`: grant ID or null.
- `next_cost`: current estimate in the grant's currency, or null (unknown).
- `executions`: explicit maps to all previous attempts, including repairs.

Operations: `analyze`, `generate_image`, `generate_video`, `generate_audio`, `edit`, `export`, `publish`. Task statuses: `pending`, `in-progress`, `completed`, `blocked`, `needs-recheck`.

Generation/publication always needs mapped permission even if marked free; any other `paid: true` operation does too. The index of standing image permission can point to existing user/workspace evidence rather than asking again. Nonpaid edit/export candidates still depend on an actual user request; a JSON label is not authority.

### Authorization and budget

A grant has `id`, `evidence` (real confirmation artifact), `max_creations` (integer), `currency`, `amount_limit` (number or null), `exposure` (number or null), and `bindings`.

`bindings` maps each covered task ID to this object:

```json
{
  "operation": "generate_video",
  "scope": "draft",
  "package_sha256": "<SHA256 of the actual frozen package>",
  "input_sha256": {"K01": "<SHA256 of the actual selected image>"}
}
```

The frozen package must contain exact prompts, ordered input roles, model/provider/region, mode/settings and scope. The Agent must verify that the actual outgoing request matches it. The checker pins package bytes and the input set/hashes; it does not parse every vendor-specific contract or intercept the command.

Separate planned repair allowance from this user-authorized `max_creations`. Count successful, failed and repair creations. Unknown creation reserves at least one slot until reconciled. Verified upload-before-creation failure counts zero creations, but is not proof of zero financial cost.

`exposure` is the reconciled committed-or-settled amount, not the sum of quote + reservation + usage estimate + settlement. Keep those individual accounting facts in their existing records and update exposure from them. The checker does not fetch prices or calculate invoices. With a monetary limit, unknown exposure or next cost blocks new paid candidates.

Candidates sharing a grant consume its remaining count/amount in listed task order for this report, preventing the report from offering the same slot twice. This is advisory allocation, not a persisted reservation or concurrency lock. Before each actual submission, rerun after persisting the latest attempt. Do not allow independent writers to submit against the same uncoordinated ledger.

### Execution maps, including old formats

Each attempt maps an existing local execution artifact without altering it:

```json
{
  "artifact": "execution-v4",
  "kind": "initial",
  "status_pointer": "/status",
  "task_id_pointer": "/task_id",
  "created_pointer": "/created_generation_tasks",
  "status_map": {"draft_exported_pending_user_review": "succeeded"}
}
```

Pointers use RFC6901. `kind` is `initial` or `repair`. Map only observed native status strings to `unknown`, `upload_failed`, `queued`, `running`, `succeeded`, `failed`, `cancelled`, `expired`.

Known remote states require a real task ID and positive created count. Synchronous image/audio responses may explicitly set `synchronous: true`, with a succeeded/failed result, positive creation count and a null task-ID value at an existing pointer. Do not fabricate a remote task ID for synchronous output; video cannot use this exemption.

Record pointers must resolve. An absent counter or ambiguous native state needs reconciliation; do not silently assume zero. If an old record lacks the fields, create an explicit cited normalization outside the old immutable record, label inferred fields and verify them before execution. A summary aggregating multiple attempts must not also be listed alongside those same attempts. Duplicate file paths or provider IDs are rejected.

Unreadable ledgers block new protected work sharing that grant; an unassigned ambiguous ledger blocks new protected work globally until assigned. Separate reconciled grants and local work can continue. Source queries/downloads remain distinct from new creation.

### Questions

Each question has `id`, stable `decision_key`, `status`, `blocks` (task IDs), `question`, `why_now`, `recommendation`, nonempty `alternatives`, and `decision_evidence` (artifact ID or null). A resolved question also has `answer`; a not-applicable one has `reason`.

Lifecycle: `open -> asked -> resolved / deferred / not-applicable`. Deferred blocking questions remain blocking. Do not create a paraphrased duplicate: reuse its decision_key. Reopen only after a material basis change and explain the version change.

Only ask for unresolved consequential direction, permission/scope, actual user-experience tradeoffs, or necessary user-supplied access/material. Check records and tools first. Do not ask the user to compute hashes, find an already recorded task ID, or repeat selected colors.

Present the recommendation, alternatives, why it matters now, affected tasks and independent work that can continue. Combine related questions; do not create mandatory questions at every stage. An empty question queue is normal.

The script validates IDs and evidence presence, not natural-language intent or authenticity. Fix missing documentation from existing evidence yourself; ask the user only if the actual decision is absent.

### Delivery

Optional `delivery` contains `artifact`, `cut_version`, `editor`, `editor_cut_version`. Version disagreement is a warning, never an instruction to overwrite the editor. Agent-check that the recorded editor version really corresponds to the current timeline and selected source ranges.

Store acceptance against the exact export in existing review evidence. Praise does not activate formal scope, spending or publication. Final and draft workflows keep their applicable gates; do not import a series gate just because one character appears.

## Limits and maintenance

This standard-library checker reads files only. It cannot establish truthful user authorization, model input use, visual quality, continuous-motion quality, music sync, legal rights or settled costs. Do not describe a structural pass as any of those.

After changing it, run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover \
  -s "<cici-skill>/tests" -p "test_*.py" -v
```

Use temporary fixtures and explicitly mapped historical files. Do not call generation services, rewrite past approvals or restore user-deleted temporary files to make a test pass.
