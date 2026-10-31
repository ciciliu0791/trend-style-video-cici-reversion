# Records and change control

Use existing formats and create records only when useful. The project summary indexes records rather than copying all their content.

## Authority and synchronization

Use one `project-state.json` as the structured index, not another approval or execution history. Immutable packages and actual user decisions control authorization; execution records and output bytes control results. `PROJECT.md` presents their current summary and creative context.

After an execution event, update the real record first, then its index, run the read-only check, and refresh only the marked progress/questions summary. Preserve user prose and old snapshots. Do not automatically write an approved state, even after a checker pass.

Map existing records with explicit paths, hashes, status mappings and JSON pointers. Missing or ambiguous history means reconcile, not assume zero cost or invent permission. Never list both an aggregate execution summary and its component attempts as separate charges.

Use stable Q-IDs and decision keys. Each open question records why now, recommendation, alternatives and the task IDs it blocks; each resolved question links its answer and actual evidence. Separate missing documentation that the Agent can recover from a genuinely missing user decision.

Allocate planned attempts, authorized creations and consumed creations separately. Repairs count. Keep estimates, reservations, usage-derived estimates and settled amounts as states of a charge, not additive expenses. Shared-grant candidates need a new check before each actual submission; the checker is not a distributed reservation lock.

## Working records

- **Brief/status:** project ID, outcome, phase, latest script/cut, next action, questions and constraints.
- **Decisions:** date, decision-maker, proposed/accepted status, artifact/version/scope. Separate user permission from internal readiness.
- **Canon/design:** reference control dimensions, geography, props/costumes, character knowledge/relationships, permitted changes. Episodes inherit specific versions.
- **Scene/coverage:** scene ID, story day/time/place, purpose/turn, participants, required beats and covering shots, continuity in/out, estimated or measured timing.
- **Shot/job/take:** shot ID, editorial purpose, screen time, entry/action/exit, reference versions, prompt/settings version, job IDs, takes, inspection, selection reason.
- **Edit:** cut version, timeline position, source take/file, source in/out, speed/crop/transformations, audio cues, adjacent-cut notes. Preserve enough to rebuild in the chosen editor.
- **Resources:** work item, dependency, estimate, authorized cap, pending commitment, settled charge, status, retry limit, remaining reserve. Reconcile commitments against settled charges without double-counting; keep unknowns visible.
- **Review:** version/time, observation, viewer/story impact, severity, repair, owner/status, recheck evidence. Distinguish observed, user-reported, inferred, and unverified claims.

Stable IDs such as `EP01_SC03_SH02_T03` survive edit reordering. Keep credentials and expiring signed URLs out of durable/shared records; use safe IDs and local paths.

## Revision impact

| Change | Recheck |
|---|---|
| Motivation/revealed information | Later behavior/dialogue and canon |
| Identity/costume/location | Dependent shots and neighboring continuity |
| Selected take or source range | Adjacent action/eyeline, sound sync, subtitles, transition endpoints |
| Length/order | Runtime, pace, cues, sound bridges, captions/graphics |
| Model/provider/settings | Capabilities, price, inputs, authorization, actual output QA |
| Export settings | Exported file and destination compatibility |

Example: a selected take moves a letter into the other hand. Check the matching action and related insert, not an unrelated establishing shot. If the contents change, also revisit later dialogue and character knowledge.

Freeze selected inputs before dependent generation and record versions/hashes where useful. Preserve superseded assets and selection history. Do not overwrite a selected take with an unreviewed candidate.

## Resuming

Read status, selected cut, open defects, pending jobs and remaining authorization. Query recorded jobs before retrying uncertain ones. Continue the next unblocked dependency without restarting the workflow.

Do not regenerate to compensate for a deleted temporary script or missing local download. The permanent task/output records must suffice for recovery. A legacy project may be checked using an external temporary state index without writing into its production directory.
