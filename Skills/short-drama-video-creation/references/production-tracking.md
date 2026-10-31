# Production tracking

## Budget draft and final work together

Do not run price lookups or require pricing snapshots as a production step. Use existing user-provided budgets, known costs, and returned usage/charges when available; missing prices are unknown, not zero. Do not invent monetary estimates or claim verified savings.

Track reference/keyframe work, draft generation and repairs, final generation and repairs, audio, and rendering separately. Preserve the authorized amount or task-count limits and reserve capacity for final production. When costs are already known, reconcile settled spend and pending commitments against the cap without double-counting. If a monetary-only cap cannot be enforced with available information, ask for a bounded task-count authorization rather than reintroducing price discovery. Existing authorization remains valid.

Count scene and transition-bridge jobs separately within each stage, including generated seconds and endpoint-image work. A six-second bridge is an additional request and six generated seconds even if the edit uses less. Allocate final bridges as well as final scene plates before using the reserve. Reconcile selected scene/bridge durations and declared overlaps against the approved runtime; do not silently extend it.

Default to one candidate and at most one targeted repair per shot per stage, within the approved cap. If further work is needed, report the failed criterion, proposed change, and additional task count (plus cost if already known). Do not loop seeds or switch models indefinitely. Continue independent work while a budget decision is pending.

## Submit once; recover existing work

Persist a local job record with exact non-secret inputs and a request fingerprint before submission. Submit each intended job once and save task/request ID immediately. Poll known IDs with bounded backoff and a deadline; preserve pending state for later resumption.

A lost creation response is `submission-unknown`: reconcile with available authoritative request/task evidence before any new create. Do not guess from a recent task list. Polling timeout or download failure does not justify a paid resubmission. Resume the existing task or retrieve its original output.

Download successful media, verify existence and decode, preserve originals, and record local hashes before QA. Track selected source ranges and edited derivatives separately. Mount local frozen assets for final renders, not expiring remote URLs.

Choose native audio or separate cues according to the approved brief. Keep final export and source files organized in the agreed project location. Uploading or sharing outside that location requires the user's existing authorization.

## Immutable approvals and current execution state

Keep approved package bytes/hashes unchanged. Put current task status, draft mounts and QA in a separate execution ledger; a mounted draft is not an approved final asset. Protect newer prompts/captions/packages from historical build scripts. Maintain one current project status and an explicitly historical section instead of stacking contradictory “current” notes.

Record gate-0 model/workflow confirmation separately from gate-1 exact inputs and gate-2 final authorization. For each bridge persist both parent clip hashes, selected boundary timestamps/frame indices, extracted endpoint hashes, input roles, prompt/settings version and stage. Track `waiting-for-neighbors` and `waiting-for-endpoint-approval` before submission. A changed neighbor, crop or source range invalidates dependent endpoint/join checks; do not resubmit or retain an old bridge without reconciling those dependencies.

Count submission attempts, accepted tasks, completed tasks, generated seconds and unknown pending outcomes separately. A rejection without a task is not generated footage and does not establish billing treatment. If the authorized request ceiling does not distinguish attempts from accepted tasks, count attempts conservatively. Keep audio failures and final-generation reserves separate from video usage.

Persist reproducible build/poll helpers with the project, not only in temporary storage. Preserve originals and derivative mappings; never put credentials, signed result URLs or full base64 request bodies into shared records. Record tool/runtime versions used successfully; a failed optional update does not invalidate an installed working renderer. Do not pin future jobs to an episode's historical model availability or tool limitations.
