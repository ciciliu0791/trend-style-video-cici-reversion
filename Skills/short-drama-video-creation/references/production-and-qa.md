# Draft-to-final production and QA

参考图和关键帧按主技能规则优先使用当前可调用且满足输入/输出要求的 ChatGPT image gen，不可用或能力不足时说明后回退 Seedream；用户指定模型和已批准方案优先。Seedance 负责动态草稿与正式视频。Seedream / Seedance 优先独立 MCP，不可用时才回退独立 arkcli，不使用 ve arkcli。具体调用遵循所选工具的技能，不重复安装或接入流程；记录实际服务、模型和参考图传输方式。

音频保留 SeedAudio；复杂音色、编曲或音乐发展优先建议 Suno。按 [音频策划](audio-planning.md) 由用户写好最终 prompt、单独生成，再下载接入，未收到可用输出前保持 `awaiting-user-generation`，不自动提交或用其他服务替换。

## Shot planning

Plan sound alongside the first script and storyboard using [audio planning](audio-planning.md); use a distinct sound column with cue IDs, then expand it into the initial audio prompt package.

Each shot needs an ID, timeline position, source type (generated/reused/editor-made), cast, entry state → main action → visible result, camera, duration, reference versions, exact prompt, audio plan, draft settings, final source settings, and acceptance criteria. Separate generated duration from the selected source range.

Use the scene timing and transitions reference linked from `SKILL.md` for per-scene lengths, model-specific action density and exact timed prompt cards. Cover every scene boundary in the transition matrix. A continuous bridge is a separately budgeted shot with actual first/last-frame inputs, not merely a request to "transition smoothly." Neighbor outputs may be generated first under their own approval; dependent bridge submissions wait for endpoint review.

Use manageable action chains and explicit contact points for interactions. Split complex actions when needed rather than assuming one universal shot-duration limit. Choose whole-sequence generation or independent plates based on current model support, continuity needs, and repair scope. Editor-made graphics and stills are appropriate when intended; they do not replace required physical performance.

## Review packages

Gate 0 confirms the proposed workflow and model settings before production, including default SD2.5 480p drafts and SD2.5 native 1080p final sources, model-aware scene lengths and bridge allowances. It does not replace exact-input review or spend authorization.

Gate 1 includes numbered keyframes/contact sheet plus full-resolution assets, timed storyboard, exact timed prompts, ordered reference roles, resource/model/settings, job count, and authorization limits, plus a dedicated audio section (sound beats, cue sheet, exact prompts/reuse sources, sample/full production order, listening criteria and allowance). Include each bridge's start/end images, neighboring source hashes/ranges, duration and causal camera/state handoff. Gate 2 includes the latest playable draft with all transitions, change log, defect dispositions, final source/output settings, final job/dependency plan, and remaining budget. Gate 3 includes the actual export, QA evidence, and any explicitly accepted limitations.

Bind each approval to a package version and the artifacts it covers. Record user confirmation text or a conversation reference, date, shot/job scope, and file hashes where available. Agent QA and human approval are separate fields. Final review approval covers the exported file hash, not merely its filename.

Revision handling:

- Story, reference, keyframe, prompt, model, duration, generation-audio settings, or other generation-setting changes require updated gate-1 approval for affected video jobs before submission.
- Gate 1 can authorize a bounded draft repair allowance, but revised creative inputs still need review; do not confuse spending authorization with creative approval.
- Gate 2 approves the planned change from draft to final settings; that agreed resolution change needs no redundant gate-1 request.
- Final neighbor outputs produce new bridge endpoint images. Gate 2 can authorize the final job/dependency plan, but unseen endpoint bytes still need targeted gate-1 input review before bridge submission; do not restart review of unchanged scenes.
- A new creative change after gate 2 returns affected material to draft review and renewed gate 2. Keep unaffected approvals; recheck adjacent cuts and shared identity/audio dependencies.
- Postproduction-only fixes need QA and renewed gate-3 acceptance of the changed export, without video regeneration unless necessary.

## Targeted repair and performance preservation

Localize the defect and affected time window first. Inspect alternative ranges in the existing source, then assess an editorial repair, a local postproduction repair, and only then a new generation where needed. This is a diagnostic order, not permission to hide missing story action or force a damaging cut. Preserve successful unrelated material and its approval.

A cut must retain readable action, emotional cause and spatial continuity. After any duration change, update affected captions, graphics, sound cues, music ranges, joins and documented timecodes together. For a style-only revision, preserve approved media, timing and sound unless the requested result requires a specific change; protect the current edit from stale build scripts.

At gate 2, where relevant, compare native-spec regeneration against preserving a valued performance with high-resolution text/graphics and disclosed source upscaling. Weigh performance, continuity, visible detail, task allowance and regeneration uncertainty together. Preservation below the original source specification requires explicit acceptance and final disclosure; it is not the default for every project, and upscaling is never native generation. This comparison uses the existing gates, not an additional approval cycle.

## Separate draft and final states

Keep per-shot draft and final records; do not overload a single `approved` flag.

Draft: `planned → submitted → downloaded → qa-reviewed → human-approved`.
Final: `planned → submitted → downloaded → qa-approved → frozen → mounted`.
Final cut: `exported → qa-reviewed → human-accepted`.

Track failures explicitly: `rejected`, `failed`, `submission-unknown`, or `download-pending`. Draft shot approvals do not replace approval of the assembled draft. Reused assets can enter final QA without a new task, with provenance and checks against the current brief. Editor-made shots record their project source instead of fabricated task IDs.

Store drafts, final source plates, original outputs, edited derivatives, and exports separately. Record task ID, prompt/settings/reference version, local path/hash, source range, review result, and any approved exception. A frozen file is a locally preserved approved version; changing it requires a new version and review.

## Same-model drafts and final generation

Default to Seedance 2.5 at 480p for drafts and the same model at native 1080p for final source plates, confirmed at gate 0 and checked against the selected service's reference/audio/action controls. The final export canvas is a separate specification. Do not substitute a cheaper model and describe it as equivalent. If unsupported, show the supported alternative and its quality implications, revised prompts/durations and required task count before generation. A production draft is not the unsupported SD2.5 API draft flag.

A supported draft-to-final API may use a prior task or asset: check its actual parameter contract, compatibility and lifetime before planning around it. Otherwise final production is a new generation using approved creative inputs at final settings. Same model, seed, or prompt does not guarantee the same performance. Preserve the draft as a comparison target and inspect final outputs anew.

Reserve final-generation spend before exhausting the budget on drafts. Default allowance is one initial request plus one targeted repair per shot per stage; final generation is its own planned stage, not a draft repair. The authorized cap always takes precedence. Do not automatically promote, upscale, or re-label low-resolution draft files as final. A qualifying existing final-spec asset may be reused after QA; an intentional quality exception needs explicit acceptance.

## QA checkpoints

**Before video:** use [performance and continuity](performance-and-continuity.md) to check emotional triggers, visible cues, reference roles and contradictory constraints. Check reference identity, anatomy, orientation, costume/prop details, composition, continuity anchors, and safe text placement in keyframes.

**Draft playback:** check story clarity, action preparation/contact/result, emotional beats, dialogue, timing, entrances/exits, spatial continuity, anatomy, occlusion, lip sync, and transitions. Inspect action peaks as well as shot boundaries. A contact sheet cannot establish movement or audio quality.

**Bridge playback:** inspect the entire transition plus both neighboring joins at normal speed and frame-by-frame near the boundaries. Check endpoint correspondence, motion speed/direction, posture/contact, identity/props/geography, exposure/palette, audio continuity, duplicated holds and skipped/repeated action. Recheck after trims or neighbor replacements; successful two-frame submission is not continuity evidence.

**Final plates:** compare with the approved draft and acceptance criteria. Check detail at final viewing size, identity, performance, continuity, unintended changes, decode success, and source dimensions. A higher-resolution output may still fail semantically. Fix the cause: reference/keyframe for identity, simpler staging for action, postproduction for exact text, affected audio cue for sound. Avoid regenerating successful unrelated shots.

**Text and graphics:** follow [text, localization and hierarchy](text-localization-and-hierarchy.md) for complete language coverage, glossary consistency, information priority, platform-safe full bounds and obstruction across motion. For technical demonstrations, also check input/result logic and scoped factual claims.

**Actual export:** verify duration, dimensions, frame rate, audio tracks, decode integrity, mounted asset versions, source ranges, and absence of accidental placeholders. Play the full file for black/frozen frames, abrupt cuts, subtitle errors/overflow, audio sync/levels, and clipped endings. Record file hash, checks performed, timestamped defects, repairs, and recheck results.

If playback/listening or another required check cannot be performed, mark it `not checked`, explain the limit, and request human review of that specific gap. Never convert technical success or sampled frames into a semantic PASS. Explicit human verification can supply missing evidence; without it, keep the result a review cut.

## Completion audit

Every shot and bridge must map to its intended final media or editor source, and every boundary to a checked transition or intentional cut. Reconcile scene/bridge source ranges and edit overlaps with the approved runtime. No superseded draft, accidental placeholder, missing dynamic performance, unresolved blocking defect, or unapproved source-quality exception may remain. Confirm the assembled timeline uses the current approved files, QA refers to the actual export, and gate 3 accepts that version before declaring completion.

## Continue to a complete reviewable cut

A continuation after a pilot can authorize expansion within the presented package; it is not evidence that the user inspected motion or accepted every defect. Record the actual decision separately from QA. A pilot does not introduce another human gate beyond gates 0-3. If an unperformed playback check is the only gap and the user directs continuation, preserve it as `not checked` and keep the assembled draft visibly under review. Do not treat a known blocking defect as passed.

A complete-video request includes assembly and a playable review export within its approved scope. Do not re-ask for the same export permission at optional tool preview steps. Before a genuinely necessary gate-2 decision, finish the complete draft, defect dispositions, exact final plan and remaining authorization. An exported draft still cannot be labeled accepted final.

## Camera and reference instructions that survive submission

Specify opening framing and camera side, screen positions and eyelines, one main action, motivated camera movement (or a locked camera), focus, ending framing/state, and any hold. Check adjacent shots for posture, geography, prop state and a meaningful change of shot size. Avoid demanding an offscreen action and its visibility in a close-up at the same time.

Each submitted prompt must stand alone: replace references to other shot IDs with visible states. Describe ordered inputs by their local reference number and authority. A scene reference does not automatically control identity or body proportions, and a normal reference image is not a guaranteed first frame. Only use hard first/last-frame language when the selected mode supports and actually uses it. Keep intended camera results separate from observations of the returned clip.

## Audio and export evidence

On audio timeout, preserve an unknown outcome and reconcile available task/output evidence before retrying. A missing response does not prove no charge. Temporary local audio or silence may support draft timing if compatible with the brief; label it and keep the requested audio unresolved. Do not silently replace a specified voice/provider, or attribute synthesized placeholders to the model. Log source, version, hash, selected interval and mix role for each cue.

Check what the validator actually ran: skipped browser checks, disabled motion assertions and sparse snapshots are not passes for those scopes. Inspect actual exported frames covering every scene, not just a tool's default sample set. Record decode, source/canvas/export dimensions, native/output fps, duration, audio streams, black-frame intervals and peak levels separately from full-speed viewing/listening. Neither absence of black frames nor a non-clipping peak proves good motion or audible mix quality.

After remux, gain or other post-export changes, preserve provenance, update the delivered hash and recheck that file. Keep the editor source consistent with the deliverable. Deliver a stable local video and a working playback entry point, with the correct production-stage label.
