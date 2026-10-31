---
name: trend-style-video
description: Analyze reference hooks, appeal and style, then remake the structure or rewrite the story. Use for 拍同款, 复刻, 改写故事 and trend-inspired videos. Not for isolated image edits.
---

# Trend-Style Video

Use one shared analysis of Hook, audience experience, style and main attraction mechanisms, then resolve whether the user wants a structure remake (复刻) or a story rewrite (改写故事). Preserve the selected appeal in either mode. Design the story and edit before commissioning footage.

This is the unified workspace entry for Trend and workspace Viral analysis and mode selection. Keep workspace Viral as a compatibility entry and optional structure-remake method; do not run both complete workflows. Do not modify or invoke the global Viral skill as part of this merge. Use one production package and decision record, preserving existing project owners and history.

Organize user review around five deliverables: source-informed story/camera review, images and their full prompts, exact video inputs, the complete motion cut, and the inspected export. Technical checks and permission records support these deliverables; they are not additional user gates. Keep trend adaptation, evidence coverage and originality visible throughout.

## Load by task

- Read the [shared source-analysis contract](../../../Skills/viral-remake-skill/prompts/analysis.md) and [adaptation choice](references/adaptation-modes.md) for reference analysis and mode selection. The former is also the workspace Viral analyzer's actual prompt, not a second copy.
- Read [creative development](references/creative-development.md) for source analysis, storyline, camera design, prompts or creative revisions.
- For a structure remake needing the legacy structured storyboard, read its [storyboard contract](../../../Skills/viral-remake-skill/prompts/storyboard.md) and [interfaces](../../../Skills/viral-remake-skill/references/interfaces.md). Reuse the shared analysis; do not start another pipeline. Story rewrite stays on the creative-development path.
- Read [production and review](references/production-and-review.md) before planning image review, paid work, assembly, revisions or delivery.
- For ongoing production, revision or delivery, read [shared project control](../../../Skills/cinematic-project-skills-cici/references/project-control.md). Use its [state template](../../../Skills/cinematic-project-skills-cici/assets/project-state.template.json) and [read-only checker](../../../Skills/cinematic-project-skills-cici/scripts/check_project.py), without running another complete creative workflow.
- Copy [the project template](assets/PROJECT.template.md) once for a new production. Fill progressively; remove irrelevant fields. For existing productions, map the current records instead of creating a competing source of truth.
- Use [acceptance scenarios](references/acceptance-scenarios.md) when evaluating or modifying this skill, not as paperwork for every film.

## Recover first

Identify whether the request is analysis, planning, production, revision or export. Read the latest cut, brief, selected references, approvals, pending task IDs and remaining budget. Do not restart completed stages or ask for assets already provided.

Record the brief's audience, intended feeling, runtime range, aspect ratio, cast, visual treatment, text/dialogue choice, music route, deadline and delivery specification. Ask only about missing choices that materially change the result; recommend a concrete option rather than returning an open-ended questionnaire.

Skill creation, analysis and planning do not authorize media generation. For an explicit production request, continue through the authorized playable cut and export rather than stopping at plans or isolated clips.

## 1. Review the source, story and camera treatment

### Extract the transferable style

Inspect the actual reference with an appropriate available tool. Record inspected intervals and whether motion and audio were assessed. If inaccessible, use supplied media or mark a description-led proposal as unverified; do not invent observed shots.

Write a compact style map covering hook, information reveals, rhythm, framing/movement, design/light/materials and sound. Label observations separately from hypotheses about why it works. A supplied "trending" label does not establish current popularity or prove retention.

Identify the visible/audible carrier of each selected mechanism, not just its props or adjectives. Prefer complete playback, event-centered inspection and listening; separate `observed`, `user-reported`, `inferred` and `unknown`. Only decision-critical missing evidence blocks the affected direction; keep feasible, authorized visual tests explicitly limited.

Present the shared analysis and proposed preservation set, then resolve 复刻 or 改写故事 using the adaptation-choice instructions before committing a mode-specific story. If the user already explicitly chose, record and restate it without asking again. Analysis-only work does not require a mode choice. Do not automatically reuse source footage, music, logos, dialogue or identifying likenesses.

For 复刻, map source beats to adapted beats and explain KEPT/CHANGED actions, framing and rhythm. Exact source timing is an explicitly requested sub-option requiring measured cuts, not the default meaning of 复刻. For 改写故事, develop a new premise and sequence while preserving the selected Hook, audience experience, style and main attractions. Do not switch workflow owner merely because the mode changes.

### Write the story and camera treatment together

Develop one recommended concept within the selected mode around an audience promise and ending effect. For a remake, retain the selected source progression; for a rewrite, allow a new story and ending. Offer alternatives only for a consequential unresolved direction. Do not force conflict or a three-act formula onto lyrical, observational or playful work.

Map each beat to what viewers discover, the visible action/change, its consequence, the necessary view and its approximate time. Make camera choices explain, conceal or reveal information. Compare the proposed rhythm with the reference; do not preserve its palette while accidentally discarding the pace that motivated the request.

Map source behavior to its function and the adapted behavior that carries it. Check `entry state -> subject action -> object response -> exit state`. Do not silently turn active performance into passive environmental motion to simplify generation. Deliberate stillness, repetition and low action may themselves be the selected mechanism.

Create a compact camera progression and continuity map before generating keyframes. Give every shot a reason to exist and every join a declared treatment. Remove redundant approach, preparation or reaction beats. Use an animatic only if it answers a named timing or composition uncertainty; it is not motion evidence.

Plan music, ambience, action sound, speech and silence now, not after footage is finished.

Before commissioning images, deliver the full treatment/timed storyboard and a compact whole-film review: cause or discovery, performance/emotion, spatial continuity, feasible camera coverage, attention/readability, sound rhythm and ending effect. Name affected beats, revisions or reasons to retain them, and uncertainties requiring image or motion tests. Do not substitute a completed matrix or an action-count threshold for this review. Preserve selected quietness, reactions or repetition without adding physical business to pass a checklist.

## 2. Review image prompts and the minimum useful reference set

Reuse adopted identity, appearance and palette. List only new uncertainties: essential identity coverage, staging/contact geometry, or a critical transition state. Do not require a fresh image for every shot or multi-angle character sheets by default.

Within applicable image authorization, prepare independent candidates as a batch. Default to one candidate per needed composition, no automatic retry. If a selected image must become the next image's reference, wait for that selection; do not manufacture a dependency-free batch.

Record identity, hair silhouette and color, ears, costume, body proportions, screen-space height/position and allowed movement before new keyframes. Separate permitted viewpoint occlusion from missing anatomy. A targeted repair is another counted request, not an exemption from a zero-additional-call limit.

Before image calls, expose each exact image prompt, ordered references/roles and settings in a readable review card. After generation, pair that card with the actual full-resolution result, version, single-image and cross-image QC, and disposition. Present the numbered set together; repair only covered material defects and preserve adopted images. Treat missing coverage as blocking, useful improvement or optional. Only blocking dependencies stop work.

Do not convert image spending permission into visual selection approval. Conversely, do not repeatedly request image-generation permission already granted. Never silently change models, increase counts or exceed budgets.

## 3. Review the exact video inputs and authorize the package

Bundle the following into the same review:

- Style map, selected premise, timed story and camera progression.
- Necessary keyframes with full image prompts, reference roles, continuity and sound plan.
- Per-job cards pairing selected frames, story purpose, entry/action/exit, camera, exact standalone video prompt, ordered inputs and output criteria.
- Verified model/provider/region, duration, aspect/resolution, audio settings and mode constraints.
- Job dependencies, generated versus edited seconds, costs, bounded retries and delivery/reuse plan.

Before presenting the package, trace each selected mechanism into the actual final prompt and its review criterion. Check whether cropping, fixed props, smaller movements or identity constraints weakened it. A simpler version missing the mechanism must not satisfy the same prompt unchanged. This is internal self-review, not another user approval gate.

Keep the chat summary short and link one current review entry. The review body must expose full image and video prompts, not only descriptions, version IDs or request.json links. Shared constraints and appended repair instructions may be collapsed but must remain expandable in full. Verify exact text, ordered inputs and settings against the outgoing request; preserve submitted wording and distinguish proposed revisions from actual submissions. Historical omissions are disclosed retrospectively, never marked as reviewed before submission.

Obtain one explicit confirmation covering the shown version, selected frames, exact jobs and video spending. Existing matching approval satisfies this checkpoint. Unresolved image selections must be settled before dependent video submissions; image-prompt disclosure adds no per-image spending checkpoint.

This is the first planned production-package checkpoint; the earlier mode choice resolves creative direction, not spending. New dependent frames or revised paid inputs require a small affected-job package. Do not repeat unchanged approvals or conceal changes behind a package summary. Current workspace budget rules govern covered spending and override legacy per-call quotation stops; retain exact-input disclosure, selection and consequential creative-change confirmation.

## 4. Generate, assemble and review the complete motion cut

If a story-critical uncertainty needs a pilot, identify the question and its effect on downstream jobs. Run it within the approved package. Continue approved independent shots while waiting; do not regenerate dependent images before the pilot proves their necessary geometry.

Inspect actual results and assemble promptly. Once the pilot meets the agreed criteria, continue covered work without another routine permission request unless the user reserved pilot selection. Do not perfect a collection of stills while the film remains untested.

Persist each request/task ID; recover existing tasks after uncertain submissions or download failures. No blind retries. Use the editor for timing, precise text, deliberate holds, sound and appropriate finishing, not to disguise absent required physical action.

Show a playable complete cut with available sound, identifying temporary or missing elements. Review experience, continuity/action, then delivery. Inspect both sides of joins and normal-speed motion; listen when possible. Label sampled-frame, playback, listening and technical evidence separately.

This is the second planned review checkpoint. Request specific decisions about timestamped issues, not separate approvals for every otherwise usable clip. Prefer trims, alternate ranges, sound changes or permitted postproduction repairs before regeneration.

Separate assembly status, QC and user selection. A defective take may appear in a clearly labeled review cut without being approved final footage. An unchecked critical pilot is not evidence that its dependent geometry works. For missing playback/listening, provide the exact clip/time, question and person needed to complete review, not a generic unchecked flag or invented pass.

## 5. Finish the selected cut and inspect the actual export

Confirm the finishing plan per affected shot: retain, trim, postproduction repair or regenerate. Preserve satisfactory performances. Record native source and output specifications and obtain explicit acceptance of any source-quality exception; upscaling is not native high-resolution generation.

If repairs require changed generated inputs or new spending, return only affected jobs to the production-package checkpoint. A draft-to-final upgrade is optional and separately authorized; never silently change model or regenerate an approved performance solely to satisfy a default resolution.

After agreed edits, export the actual file, verify it, and provide a direct link. User acceptance belongs to the exact inspected version: changes after review produce a new review cut until accepted. Do not demand a fresh export authorization when already covered, or call technical success human acceptance.

## Project management without extra gates

For new projects use `project-state.json` as the shared index and this skill as `workflow_owner` in both modes. Preserve an existing project's owner and use an explicit mapping rather than migrating its history. Keep `adaptation-choice` in existing decision notes, not a new required schema key. On resume, change, keyframes, pre-submit, task creation/terminal update, edit, pre/post-export and feedback, reconcile records and run the shared checker. Refresh only the marked PROJECT summary; do not overwrite user prose or approved snapshots.

Read `can_continue`, `blocked`, `questions` and `warnings`. Fix technical facts yourself, retain existing-ID recovery, and stop only affected new work. Before each paid call verify its real approval, remaining allowance and exact outgoing package even if the checker offers `submit_candidate`. A check result never grants permission or proves quality.

Present only consequential unresolved direction, scope/spend, access or experience decisions. Each Q-ID carries why now, a recommendation, alternatives, affected tasks and independent work. Reuse resolved decisions; do not re-ask adopted colors or turn every stage into a question. Record unchecked playback/listening without inventing a pass.

Track the five user-facing deliverables against existing shared stages: story/source review to P1/P2, images and video-input review to P3, complete motion cut to P4/P5, and finishing/export to P5/P6. Keep the P1-P6 schema unchanged. These are internal handoffs, not five user approval gates. Use writer/director, producer, continuity and editor/sound as review responsibilities, not a requirement to spawn agents.

Keep one project index, immutable package snapshots when approved, machine-readable task records and versioned exports. The live editor project and current manifest must point to the same selected assets and timing. Preserve old outputs without duplicating the entire project for each minor edit.

After delivery, synchronize the current file/hash, task terminal status, user feedback, open checks and next action. If the editor still represents an older cut, label that version explicitly. Praise is valid experience evidence, not automatic final QA, extra spending or publishing permission.

On a revision, inspect current user edits and update only the affected dependency chain. On resume, read the current index and pending jobs, not every historical document. Do not ask the user to repeat settled decisions.

## Tool and specialization boundaries

- Load current generation/editing tool skills only when needed; obey their mandatory confirmations and safety requirements. Shared evidence may satisfy overlapping gates, but this workflow cannot waive a tool's required confirmation.
- For this workspace, prefer independent Seedance/Seedream MCP. If unavailable or insufficient, explain the limitation and use standalone BytePlus `arkcli`; never `ve arkcli` or the uninstalled Creative Kit. Verify current capabilities, region, endpoint, authentication and price. Reuse valid evidence rather than repeating checks gratuitously.
- Keep the user's chosen model and consult the current [workspace rules](../../../AGENTS.md) for stage defaults. Manyue dynamic drafts currently use Seedance 2.5 / 480p; formal production follows the approved episode specification, retaining the earlier 2.0 Fast preference when unspecified. A production draft is not API `draft=true`; verify actual capabilities and explain any proposed change before applicable approval. Other casts do not inherit Manyue's model, anatomy, dialogue or duration conventions.
- For Manyue, load its skill and relevant identity/canon references, retaining the current episode's explicit creative choices. A character cameo does not switch `workflow_owner` or import the full diary episode's runtime, captions or formal-production gates. If the request is actually a diary episode, select that owner and preserve its applicable gates. Reuse valid shared evidence rather than creating duplicate approvals.
- Use HyperFrames by default when a new editor is needed; retain an existing editor and user changes. Read its current skill before editing or rendering.
- Keep audio generation/reuse and licensing explicit. When the user chooses Suno, supply a prompt and await the user-provided track; do not assume an API. An unavailable track may leave a clearly labeled review mix, not fabricated finished audio.
- Keep credentials and expiring signed URLs out of shared records. Do not upload or publish without authorization. In this workspace, authorized uploads default to the user's Drive Seedance folder, preserving permissions; folder/preview links are not model-readable media URLs.

## Design references

This workflow shares analysis with workspace Viral and draws on these methods without requiring every source workflow to run:

- [Workspace Viral compatibility entry](../../../Skills/viral-remake-skill/SKILL.md): shared analysis and optional structure-remake methods; historical execution adapters remain separate.
- [Short-drama creation](../../../Skills/short-drama-video-creation/SKILL.md): playable action, timed prompts and connected shots.
- [Cinematic project skills Cici](../../../Skills/cinematic-project-skills-cici/SKILL.md): directing intention, stage evidence, dependencies and proportionate records.

The Cloud Laundry process motivated fewer serial image checkpoints and earlier camera design. Treat faster review and better creative quality as hypotheses to measure in the next production, not proven benefits of this new skill.
