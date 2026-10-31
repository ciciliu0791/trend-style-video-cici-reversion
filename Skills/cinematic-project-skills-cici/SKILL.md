---
name: cinematic-project-skills-cici
description: Develop and manage a film, short drama, or episodic AI video as a coherent production project, from story development through coverage, continuity, editing, sound, and delivery. Use for project-level quality improvement or ongoing production management, not isolated prompt writing or a single image request.
---

# Cinematic_Project_Skills_Cici

Make every production choice serve the intended audience experience. Manage story, performance, design, coverage, continuity, resources, and editing as connected work. Attractive shots alone are insufficient evidence that a film works.

This is a project and creative-development layer. Use available specialist skills for generation, prompting, editing, and export when needed, without loading all of them at project start. Current user instructions override older skill defaults. Never silently change the chosen model, provider, editor, appearance, or approved workflow.

## Standard production contract

Read [stage standards](references/stage-standards.md) when starting or resuming a full project. Every active stage has an input version, responsible role, required output, exit evidence, and a next handoff. Record `not-started`, `in-progress`, `ready-for-review`, `passed`, `blocked`, or `needs-recheck`; an exception needs a reason and impact, not an empty checkbox. Responsibility is a review function, not a claim that a separate person or agent exists.

For full projects, retain six essential outcomes: brief/script, director's treatment, executable coverage/assets, traceable production, reviewed assembly, verified delivery. Combine paperwork for small projects, but do not silently omit the decisions. Local revisions visit only affected stages. Existing accepted artifacts satisfy a stage after checking version and relevance.

Use [the director's workbook](references/directing-workbook.md) for new directing decisions and [the directing template](assets/director-treatment.template.md) to record selected ones. Keep unselected alternatives separate from the production baseline. Standardize decision completeness and handoff, not shot counts, styles, clip lengths, or emotional formulas.

## Check the shared project state

For ongoing production, revision or delivery, read [project control](references/project-control.md). Use [the state template](assets/project-state.template.json) for a new project; map old records explicitly rather than migrating or inventing missing approvals. Keep one workflow owner and a current deliverable scope. Character references do not automatically activate another series workflow.

Run [the read-only checker](scripts/check_project.py) on resume, relevant changes, keyframe review, before paid submission, task creation/terminal events, edits, export and user feedback. Use its documented command and interpret `can_continue`, `blocked`, `questions` and `warnings` together. Reconcile actual records and update the state/PROJECT summary; the checker performs no writes, network calls or generation.

Only continue affected tasks after required evidence is satisfied; continue independent covered work. Existing IDs must be queried or downloaded, never recreated because a download is missing. A `submit_candidate` result is not permission: verify real user scope, tool requirements and exact outgoing inputs.

Ask only consequential unresolved direction, authorization or experience questions, with a recommendation, alternatives, impact and independent next work. Reuse stable question IDs and recorded decisions; do not ask a mandatory question at every stage. Missing machine-verifiable facts are the Agent's work.

Keep planned attempts separate from authorized creations and consumed attempts, including repairs. Keep draft satisfaction separate from formal work, technical QA and publishing. This shared control does not reduce any applicable specialist approval gates. For maintenance run [offline tests](tests/test_project_control.py); never use paid generation as a framework test.

## Recover the project

Read project instructions, latest script/cut, selected assets, decisions, budget, and unfinished work. Establish whether the request is research, development, planning, production, revision, or delivery. Research and skill construction do not authorize media generation.

Recover decisions before asking questions. Ask only for missing information that materially changes the work; continue independent parts while waiting. Distinguish recorded decisions, proposed choices, and unknowns.

Use the smallest useful record. A short scene may use one document; a series needs shared canon and episode records. Copy [the project template](assets/project.template.md) for new work, deleting irrelevant fields. For existing work, map existing files to these responsibilities instead of creating competing sources of truth. Read [records and changes](references/project-records.md) for multi-shot production, revisions, or paid jobs.

## Develop the film before commissioning footage

Write a concise brief: intended viewer, format/runtime, emotional promise, premise, point of view, distinctive specificity, delivery destination, and constraints. For drama, develop desire, obstacle, choices, consequences, and ending. Preserve intentional ambiguity; do not force conflict or three-act structure onto observational, lyrical, or experimental work.

Move from treatment/beat outline to scenes and dialogue at the level needed. For each dramatic scene identify what the viewer knows before and learns afterward; what the character wants and what resists them; how their tactic changes; which visible behavior or sound carries the turn; and what the next scene inherits.

Read dialogue aloud or use a timed scratch read when possible. Account for action, pauses, reactions, and silence. Label unperformed timings as estimates. Revise redundant exposition and intended changes that cannot be seen or heard.

For a series, add a repeatable story engine, character relationships/trajectories, world rules, episode promises, unresolved setups, and canon at episode boundaries. Give each episode its own movement; do not mandate cliffhangers.

## Design around the edit

Read [creative review](references/creative-review.md) when developing scenes, planning coverage, or reviewing a cut.

Establish a concise direction/design bible: identity and performance behavior; geography; important props/costumes; framing/camera logic; light/color; sound perspective; and permitted changes. Translate mood words into visible/audible choices. Preserve selected looks rather than regenerating them for novelty.

Break the script into practical requirements. Choose coverage by editorial purpose: geography, action, reaction, reveal, transition, or subjective viewpoint. A long take may serve several purposes; do not mandate master/close-up coverage. Include reactions/inserts when the story would otherwise be uneditable. Budget source handles around edits where the service permits them.

Separate scene, shot, generation job, take, and edit event. A job may contain multiple shots; a shot may require multiple jobs. Record editorial duration independently of generated duration. Map required beats to planned shots and later to selected source ranges.

Choose cuts, sound bridges, dissolves, or continuous transitions for a reason. Do not commission a generated bridge at every boundary. For continuous-action joins, specify matching endpoints and dependencies. Track emotional continuity as well as wardrobe and eyeline: knowledge, allegiance, and recovery from a shock affect subsequent behavior.

## Make production feasible

Schedule dependencies and milestones from the breakdown. For AI work, prioritize uncertain story-critical interactions, identity/performance tests, and sound intelligibility before large dependent batches. A test must answer a named uncertainty and remain within authorized scope. An animatic can test timing but cannot establish motion or acting quality.

Allocate references, generation, repairs, editing, sound, and delivery separately. Track estimated, committed, and settled cost without double-counting; preserve repair allowance and enough capacity to finish. Verify current pricing when a quote is needed. Unknown cost is not zero. Do not hard-code model capabilities, prices, resolutions, or draft-to-final support.

Before paid video work, make scope, inputs, settings, estimated cost, and limits reviewable and obtain required authorization. Reuse authorization for unchanged covered work. Follow existing image permission separately; do not impose per-image approval. Creative reference selection and spending permission are different decisions.

For live-action/hybrid work, add actual cast/crew availability, locations, equipment, rehearsal, call sheets, backup, and relevant permissions. Do not fabricate bookings, agreements, or compliance evidence. Omit irrelevant human-production logistics from entirely generated projects.

## Produce and assemble together

Use these responsibilities as separate review passes, not a requirement to spawn agents or hire crew:

| Responsibility | Decision |
|---|---|
| Writer/director | Does behavior and perspective convey the intended story? |
| Producer | Is the next work feasible within scope, time, and resources? |
| Design/cinematography | Do world, framing, light, and movement serve the scene? |
| Script supervisor | Are coverage and physical/emotional continuity editable? |
| Editor/sound | Do selected footage and sound make the scene intelligible and affecting? |

Persist task IDs and recover uncertain submissions before retrying. Keep originals and selected takes distinct. Inspect actual motion/audio when tools support it; disclose uninspected dimensions. Contact sheets cannot establish performance, temporal stability, lip sync, or sound quality.

Assemble footage early. Review neighboring shots and the whole film at normal speed. Record timestamped observations and their effect on the story. Prioritize broken causality/performance, continuity/intelligibility, distracting artifacts, then polish. Choose the smallest effective repair: edit, alternate take, sound adjustment, pickup, or regeneration. Reassess the assembled scene afterward.

## Finish with evidence

These are readiness checks, not automatic permission requests. Advance when evidence and existing authorization suffice. Involve the user for required creative selection, scope/spend changes, and acceptance under the agreed review plan.

| Milestone | Required evidence |
|---|---|
| Story ready | Coherent scene progression, intended experience, plausible timing |
| Production ready | Coverage/dependencies, selected necessary references, feasible schedule/budget |
| Assembly ready | Playable complete story with missing/temporary elements identified |
| Picture lock | Cut version and timing frozen under the agreed decision process |
| Delivery ready | Actual export checked for story, joins, sound, titles/subtitles, destination specifications |

Plan sound early and use temporary sound in editorial. After picture lock, complete detailed dialogue, ambience, effects/Foley, music, mix, color, and finishing as appropriate. Later timing changes reopen affected sound, subtitle, VFX, and export checks.

Deliver the actual file with version, source provenance, QA evidence, limitations, and acceptance status. Verify destination requirements instead of inventing universal loudness, codec, frame-rate, or resolution rules. Label plan, animatic, assembly, rough cut, picture-locked cut, delivery review, and accepted final honestly. Never invent user acceptance.

After a pilot or delivery, compare outcomes with the brief and record rework causes, usable footage, cost, and review findings. Following this skill does not prove improvement. See [research basis](references/research.md) for sourced practices and proposed AI adaptations.
