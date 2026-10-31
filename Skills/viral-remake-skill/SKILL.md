---
name: viral-remake-skill
description: Continue workspace Viral projects or enter shared Hook and style analysis. Use for legacy Viral runs and 拍同款; choose structure remake or story rewrite through the unified Trend entry.
---

# Workspace Viral: Shared Analysis and Legacy Compatibility

Use [Trend](../../.trae/skills/trend-style-video/SKILL.md) as the unified entry for new workspace projects. Both entries use the same source-analysis contract below and resolve 复刻 or 改写故事 before committing a story. Do not default the user's choice merely because they invoked Viral, and do not analyze the source twice.

For 复刻 preserve the selected Hook, audience experience, style, main source progression, shot functions, staging and rhythm. For 改写故事 preserve the selected appeal but develop a new story through Trend's creative-development path. Close timing is an explicit remake sub-option requiring measured cuts. Neither mode requires a product, sales claim or CTA.

This directory retains the old workspace scripts and records; it is not the global Viral skill. Its frontmatter name now matches the directory. Existing `viral-remake` owner labels, run paths, packages and approvals remain historical identifiers and must not be renamed or rewritten. For existing projects keep one current owner and reuse shared analysis without migration; for new projects use `trend-style-video`.

## Read only what is needed

- [Shared source analysis](prompts/analysis.md) and [adaptation choice](../../.trae/skills/trend-style-video/references/adaptation-modes.md): required for either entry's analysis and mode decision. The analysis file is the actual legacy analyzer prompt and the single shared analysis contract.
- [Trend creative development](../../.trae/skills/trend-style-video/references/creative-development.md): story rewrite, and shared story/camera development. Use the unified Trend production path for new projects, not the legacy workflow below as a second pipeline.
- [Production lessons](references/production-lessons.md): when choosing source coverage, cast, continuity, repair or review strategy.
- [Interfaces and commands](references/interfaces.md): before creating a brief, storyboard, route snapshot, review package or edit handoff.
- [Ark CLI execution](references/ark-cli.md): before any model, pricing, discovery or task call. In this workspace use independent Seedance/Seedream MCP first, then supported standalone BytePlus `arkcli`; never silently switch services. The bundled adapter remains Volcengine-only and is not the BytePlus fallback.
- [Analysis](prompts/analysis.md), [storyboard](prompts/storyboard.md) and [QA](prompts/qa.md) prompts: before authoring or revising those artifacts, including local/manual work. Preserve their existing JSON interfaces.
- [README](README.md): executable offline-to-production sequence and migration notes.

## Legacy Structure-Remake Workflow

Use this section only for existing compatible structure-remake projects or explicitly selected legacy methods. New projects stay in the unified Trend workflow. Before step 2, resolve the shared adaptation choice; for story rewrite use Trend creative development instead of this structure-preserving storyboard prompt. Preserve existing run state and task recovery when reusing a legacy project.

1. **Source evidence.** Apply the shared source-analysis contract, including Hook, audience experience, style and main attraction points; reuse an existing analysis when its evidence is still valid. When the user has not supplied a usable video file, first offer the source-download choice below. Probe a local video, or import actual timestamped browser observations with limits. Prefer full playback, event-centered inspection and listening; fixed sample counts prove neither continuous action nor sound. Preserve source text regardless of the later text method. Source speech requires a verified transcript or audio-capable review; caption reading is not transcription. Resolve decision-critical gaps; do not block unrelated authorized visual work.
2. **Adapt and storyboard.** Use `ad` or `creative`; keep a KEPT/CHANGED explanation and source-beat mapping. Each shot specifies cast, camera, entry state → subject action → object response → visible result/exit state. One main causal behavior may contain several stages without extra shots/jobs. Preserve the function of gestures when adapting bodies; do not silently replace active performance with passive motion. Deliberate stillness or repetition may be the selected mechanism. Describe spatial sides and contact points for interactions, and the causal link for transitions. Use original music unless source audio reuse is explicitly authorized.
3. **Confirm production choices.** Resolve storyboard, aspect/duration, audio, reference uploads and budget. **Ask the user whether text should be generated, added in post, or omitted before production unless already specified.** Analysis need not wait for this preference. Existing authorization remains valid; do not repeat settled questions.
4. **Create keyframes for review.** Within the authorized image budget generate, or reuse approved, keyframes covering unresolved composition, contact and critical transition states. Distinguish source evidence frames from generation inputs; neither every shot nor every analytical beat requires a new image. Shared composition can reuse a mapped frame. Batch independent preparation and inspect exact input crops together, including edges, residual props/tags and reflection direction. "Expression only" does not isolate pixels. Keyframe generation is image generation, not permission to generate video; do not repeat an already granted image spending approval.
5. **Show the video review package.** First trace selected mechanisms into the actual rendered prompt and output criteria; catch weakened agency, missing stages and creative losses from cropping/fixed props. Essential behavior must be in rendered action/camera/state fields, not only `function` or `reason`. Present its numbered contact sheet, full-resolution keyframes, timed storyboard, exact rendered prompts, ordered reference roles, actual resource/settings, task count and cost estimate. `review.py` writes HTML/Markdown and immutable `package.json` for the bundled adapter's supported routes; it does not make unsupported BytePlus routes valid. For MCP/standalone BytePlus use the current provider skill and an equivalent frozen package with the same authorization/recovery protections. If prices are unknown, obtain matching evidence before seeking final spending approval.
6. **Wait for explicit user confirmation before submitting video.** For compatible bundled-adapter packages record it using `review.py --approve`; for the supported MCP/BytePlus workflow record the actual user words against its frozen package, exact inputs/settings and selected job IDs. Do not invent evidence or pass unsupported packages through the old adapter. A whole-clip job requires approval of all its included shots. `--confirm` alone cannot bypass package approval.
7. **Generate and review motion.** Only approved, unchanged jobs may submit. Keyframe, prompt, reference, model, duration, resolution, audio or budget changes require a new package and confirmation for affected jobs. Unchanged jobs may retain approval across packages when their full digest is identical. Reference files and selected picks are rechecked.
8. **Assemble and deliver.** Select approved dynamic plates; validate source ranges with `edit.py` when the documented handoff is compatible, otherwise use the current editor's equivalent checks. Use the current HyperFrames skill for timing, text, original audio, overlays and rendering. Run compatible local `qa.py` checks on the actual delivered file, attach semantic review evidence by file hash, and disclose missing checks; no implicit paid model review.

## Missing source video file

When only a video URL, screenshots or a description is available, briefly explain that a playable source with audio improves analysis of actions, timing, transitions and music synchronization, and therefore remake accuracy. Offer one concrete choice, unless the user has already chosen or authorized a download:

> 为了更准确地拆解动作、节奏和镜头衔接，你希望由我尝试下载原视频，还是自行下载后提供文件？Instagram 视频可尝试 [Trendsee 下载工具](https://tools.trendsee.io/instagram-video-downloader)。

- Treat the link as a user-suggested Instagram downloader, not a verified universal downloader or a guarantee of availability. For TikTok or other platforms, check an appropriate supported route instead of claiming this tool supports them.
- If the user chooses Agent downloading, verify available tools and source access, then attempt the authorized download. Do not bypass access controls, request account passwords or cookies, install software, incur new fees, or upload private media to a third party without applicable permission. Download access does not establish reuse rights.
- If the user chooses self-download, provide the link and ask for the resulting original-quality video with audio where available; a screen recording with audio is a fallback. Do not repeatedly ask once the choice is settled.
- If downloading is unavailable or declined, continue feasible browser-based analysis or a clearly labeled limited proposal. Record which intervals were actually played, sampled or heard; do not infer continuous choreography, precise beat timing or a verified transcript from screenshots alone. A local file improves access but does not itself prove full playback/listening review or that the generation model received a video reference.

## Cost and recovery

- Apply the current [workspace rules](../../AGENTS.md) for project-level budgets and covered spending; do not recreate legacy per-call quotation approvals. Preserve exact-input disclosure, actual creative selections and scope confirmations. Choosing a mode alone does not authorize production or spending.
- Balanced default: reuse approved assets, one candidate, up to one targeted repair per job within the authorized budget. No compulsory Pro model, two takes, four-keyframe limit or whole-project quality upgrade.
- Choose whole-clip generation for simple supported sequences; plates for independent repairs, precise edits and ensemble staging. Model capabilities determine limits, not a universal 30-second rule.
- Before each batch, include image/video costs, pending reservations and any separately authorized analysis/audio/render spend. Unknown prices are never zero; normalize currency and billing units from dated evidence. `request_hash` binds each quote to the actual request.
- Every create is single-attempt. Persist task IDs immediately; resume known IDs after polling/download failure. Lost creation responses become `submission-unknown` and block further creates until reconciled. Never guess a task from a recent listing.
- Repair the cause: identity → references/keyframe; missing action → clearer causal staging, simplifying only when the selected function survives; palette/background/text → bounded postproduction when approved; audio → affected cue. Show revised video prompts/keyframes before paid retries.

## Evidence and quality

Keep identity, composition, environment and motion roles separate. References do not replace explicit invariants (for example, asymmetric facial markings or product geometry). Respect the selected realistic/anthropomorphic body rules; distinguish natural occlusion from structural disappearance. Recommend a concrete equivalent and disclose the tradeoff when anatomy cannot carry a required gesture.

Before paid submission, check actual input roles/types/order and supported readable transport; distinguish file access, client declarations, serialized contents and backend evidence. A partial preview proves neither successful media fetching nor omission. Follow tool-specific preview stop rules; do not add paid calls for diagnostics.

QA follows the approved intent and intentional changes. Assess the chosen mechanism, behavior and ending before ordinary polish. Inspect action peaks and transitions, not only evenly spaced frames. Visual samples, motion playback, transcript checks and direct listening are separate evidence. Two model reviews are optional second opinions for disputed/high-risk shots, not proof of correctness or a mandatory expense.

Preserve original outputs, selected edits and their provenance separately. A rendered timeline is not proof that motion, text or audio is correct. Call an unchecked export a review cut, not a verified final. Record user improvement reports without treating praise as passed QA, extra spending or publishing permission. Synchronize current file/hash, terminal task status, actual editor version and open checks; preserve historical snapshots. When several variables change, attribute improvement to the combined package, not one model.
