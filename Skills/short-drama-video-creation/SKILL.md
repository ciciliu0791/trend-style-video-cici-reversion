---
name: short-drama-video-creation
description: Develop original short dramas, standalone videos, and reference-led adaptations from brief and reference assessment through reviewed motion drafts and final-quality production. Use for end-to-end creation or production revisions requiring story, continuity, generation, editing, and human review; not for isolated prompt writing or reference analysis alone.
---

# Short drama and video creation

Make the approved story visible and audible in the actual delivered video. A storyboard, animatic, low-resolution draft, or technically valid export is not evidence of a finished production.

## Working assumptions

未指定生图服务时，先确认当前会话可调用的 ChatGPT image gen 能力；可用且支持本次参考图、编辑和输出要求时优先使用。不可用或缺少必要能力时，说明限制后回退 Seedream。用户明确指定的模型或已批准的生产包优先，不自动改换；不能因当前聊天模型属于 OpenAI 就推断生图可用，也不硬编码未经核实的模型名。

Seedream / Seedance 的创建、查询与恢复优先使用独立 MCP（`seedream`、`seedance`），不可用或能力不足时再使用独立 `arkcli`（`@byteplus/ark-cli`）。不要使用 `ve arkcli` 或恢复已卸载的 Creative Kit。遵守所用工具及技能的必要检查，复用有效能力证据，不额外增加安装、接入教程或查价步骤。BytePlus 国际服务与火山引擎的模型名、地域、凭据和 endpoint 不能混用；更换服务前说明限制，不静默替换。

独立音频保留 SeedAudio 路线；复杂音色、编曲或音乐发展需求优先建议 Suno。Suno 由用户写好最终 prompt 并单独生成，随后下载接入；不自动提交或假定存在 Suno API。详细交接见 [音频策划](references/audio-planning.md)。

## Resources

- Read [performance and narrative continuity](references/performance-and-continuity.md) when designing acting beats, reactions or connected character shots.
- Read [text, localization and visual hierarchy](references/text-localization-and-hierarchy.md) when planning captions, graphics, localized versions or technical demonstrations.
- Read [audio planning](references/audio-planning.md) when writing the first script/storyboard, preparing prompts, or revising sound; keep audio as a separate production workstream.
- Read [reference assessment](references/reference-assessment.md) before locking the production package or revising references.
- Read [production and QA](references/production-and-qa.md) before drafting, reviewing, generating final assets, or assembling a delivery.
- Read [production tracking](references/production-tracking.md) when allocating generation attempts or resuming unfinished production.
- Read [scene timing and transitions](references/scene-timing-and-transitions.md) before planning scene lengths, writing video prompts, or connecting scenes.
- Copy [the production-plan template](assets/PRODUCTION_PLAN.template.md) into the project and fill it progressively. Do not edit the template in place.

## Before production: confirm the plan

After read-only project inspection, present a short proposed plan and obtain **gate 0: workflow and model confirmation** before beginning the production workflow. Default to **Seedance 2.5 (SD2.5), 480p for the complete motion draft**, and **Seedance 2.5 (SD2.5), native 1080p for final source generation**. These are proposed defaults, not automatic approval or guaranteed service availability. Record the exact model/version or endpoint, provider, Region, resolution, aspect-ratio/mode constraints, duration limits, reference controls and audio settings for each stage, with capability evidence or unresolved checks. Do not silently substitute Seedance 2.0, another provider, or an upscale.

Show the story/runtime, initial scene breakdown, model-aware proposed lengths, transition strategy (including start/end-frame bridge jobs), draft/final/repair task counts and generated seconds, audio scope, delivery specification, and review sequence. Ask one bundled confirmation of this concrete plan and any unresolved alternatives. Gate 0 confirms the workflow and model choices; it does not approve unwritten prompts, unreviewed keyframes, paid work outside explicit authorization, or final production. Keep gates 1-3 below. Existing explicit approval of the same plan may satisfy gate 0; record it without re-asking or rewriting history.

Here, `draft` means a low-resolution production stage, not an API `draft=true` flag. The project's recorded SD2.5 contract does not support that flag. Verify the current selected mode before using any draft-to-final operation.

## Workflow

1. **Ground the brief.** Inspect existing scripts, media, project files, and approvals. If not already specified, ask where the assets are stored and how to access them (local folder, Drive/shared folder, attachments, or another source). Record the location and preferred delivery destination; do not ask again when already supplied. If no assets exist, proceed with original reference design within authorization. Resolve audience, story, duration, aspect ratio, visual treatment, audio, final source/output specifications, budget, and quality priority. Do not inherit a source project's cast, genre, runtime, or format. Planning-only requests do not authorize paid generation.
2. **Assess references.** Map each input to its intended role and shots. Identify blocking gaps, useful improvements, and optional additions. Ask for specific missing coverage only where it matters; invented characters and settings can start without supplied references. Continue independent work while essential inputs are pending.
3. **Prepare the picture and audio package.** Define visible emotional changes and inherited scene state for performance beats. For text-heavy scenes, assign the primary visual focus and language coverage using the linked references. Write sound beats alongside the script and a separate cue-ID sound column in the storyboard. Include a dedicated audio section with emotional progression, cue sheet, exact prompts or reuse sources, sample/full-length order, listening criteria and separate authorization limits. Present a script, timed storyboard, reference map, necessary reviewed keyframes, exact video prompts, model/settings, and separate draft/final/repair authorization limits. For every scene, map its editorial duration to generation jobs and write matching timed prompts; distinguish longer SD2.5 sequences from shorter SD2.0 action units using the timing reference. Classify every adjacent scene boundary. For a continuous generated transition, plan a separate bridge with the outgoing scene's selected end frame as its start and the incoming scene's selected start frame as its end, plus its own prompt, duration, dependencies and budget. Generate reference images or keyframes only within existing image authorization. For adaptations, distinguish observed source structure from creative changes; do not claim exact timing or transcription without evidence.
4. **Human gate 1 — production package.** Obtain and record approval of the concrete package before submitting video. Existing explicit approval covers unchanged work; do not ask again. Resolve remaining spend authorization before paid work.
5. **Draft the complete story.** A pilot is an intermediate milestone: continue through authorized generation, assembly, and a playable review export rather than handing back only isolated clips. For high-quality production, default to a complete motion draft with dialogue and audio timing using gate-0-confirmed Seedance 2.5 at 480p when supported. Freeze selected neighboring plates and extract their boundary frames before submitting dependent bridge jobs; review newly extracted inputs under gate 1. Include every planned transition in the playable draft. An animatic may precede motion work but cannot substitute for its review. Confirm a deliberately reduced draft scope with the user rather than silently skipping story coverage.
6. **QA and revise.** Inspect action and performance in playback, identity and continuity across shots, text, sound, and timing. Present timestamped findings and targeted fixes. Evaluate selected source ranges and editorial or postproduction repairs before regenerating successful performances; follow the repair strategy in production and QA. Show changed prompts/keyframes/settings for affected video jobs and obtain revised gate-1 approval before paid submissions; unchanged jobs retain their approval. Refresh the assembled draft after edits.
7. **Human gate 2 — revised draft to final.** Show the current complete draft, resolved/open defects, final specification, final-generation or explicitly accepted reuse plan, and remaining authorization. Where regeneration risks losing an approved performance, compare it with preservation plus disclosed source-quality limits rather than treating resolution alone as quality. Record human approval of that version. Draft approval advances to final production within authorization; it is not task completion.
8. **Produce final assets.** Follow the gate-2-approved generation or reuse route. For new generation, use an explicitly supported draft-to-final operation or generate from approved prompts/references at the confirmed final settings, defaulting to Seedance 2.5 native 1080p. Verify every result again. Rebuild transition endpoints from the approved final-resolution neighboring plates and review those inputs before generating final bridges; do not inherit draft boundary frames or transition QA. Mount only approved, locally frozen final assets or explicitly approved qualifying reuse; preserve draft and original outputs separately.
9. **Human gate 3 — final cut.** Export and QA the actual file, present it as a review cut with disclosed limitations, and obtain final acceptance. Deliver as final only after QA and human approval of that file/version. A finished-video request includes export.

## Review and completion rules

Approvals record the real user decision, scope, version, and artifact identifiers; never infer approval from silence, a tool success, or agent QA. Changes invalidate affected approvals and dependent continuity checks, not the entire unchanged project. Follow explicit user changes to review scope while recording them.

Use HyperFrames for assembly by default, loading its current skill when needed; preserve an existing editor when appropriate. Exact subtitles, logos, UI, and typography belong in postproduction by default. Native generated dialogue or separate audio are both valid according to the brief and actual service support.

Final completion requires every planned shot and transition, correct approved asset versions, final source specifications, clean assembly, actual-file technical and semantic QA of both sides of every join, and gate-3 acceptance. Do not count output upscaling as native final-quality generation or retain a draft plate merely because it passed story review. Any intentional source-quality exception must be explicit in gate 2 and final review.

Stop only the affected work when references, capability, budget, or approval are missing. Continue useful independent work, preserve recovery information, and report the concrete next decision. Label status honestly: `plan`, `animatic`, `motion draft`, `final review cut`, or `accepted final`.
