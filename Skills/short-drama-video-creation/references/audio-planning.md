# Audio planning and production

Treat audio as its own production workstream, designed alongside the script and storyboard from their first version. Do not defer it to a generic postproduction note. Explicit silence, no score or no voiceover are valid choices; blank fields are not a plan. For an existing project, fill gaps without rewriting historical approvals.

## 服务选择与 Suno 人工交接

- 先复用获准且符合项目要求的音频。常规环境声、动作音效、提示音及简单音乐保留 SeedAudio 路线，调用前核实所需能力；明确指定的来源或已批准方案优先。
- 对复杂音色、多乐器编曲、细腻演奏或有明显段落发展的背景音/音乐，优先建议 Suno；不据此承诺精确秒点、分轨或任意音效控制。
- 用户写好最终 prompt，并在 Suno 单独生成。Agent 可整理时长、情绪、乐器、人声要求、段落与禁止项；只有用户要求时才协助起草，不把草案当成最终 prompt，也不自动提交或假定有 Suno API。
- 对应 cue 依实际进度记录 `awaiting-user-prompt`、`awaiting-user-generation` 或 `download-pending`，等待用户返回文件或可下载链接。等待期间可继续独立画面工作，不自动换服务补位。
- 收到输出后下载或导入本地并保留原件。记录 Suno 来源、用户最终 prompt/版本（缺失则标未知）、作品链接/ID（可用时）、文件 hash、使用许可/用途确认和采用区间；不虚构 API 任务 ID、费用或分轨。保留原格式，转码另存派生版。
- 试听音色、编曲、情绪、意外人声、重复感与头尾后再对齐和混音；不能试听时标记 `not checked` 并请用户补验，不以下载成功替代听审。

## Script: narrative purpose

For each dramatic beat identify the intended emotion, music entrance/development/exit or silence, environmental perspective, important action sounds, character vocalization and dialogue delivery. Explain why sound occurs rather than writing “upbeat BGM.” Define thematic continuity and contrast across scenes. Character sounds must fit the cast and brief; do not import pet-specific rules or a previous project's instruments and sound counts.

## Storyboard: sound column and cue sheet

Every shot has a separate sound column linked to stable cue IDs, an explicit carry-over cue, or intentional silence. Continuous music or ambience may span multiple shots. The cue sheet records type, shot/time window, narrative function, timbre/identity/distance, entry and exit, observable sync anchor, priority/ducking, generation or reuse source and acceptance criteria.

Anchor effects to actual events, such as a foot contacting the floor or a result becoming visible. Planned timestamps remain provisional until footage exists. Consider on/offscreen position and mouth state for vocalizations, leave reading space under captions, and avoid sounding every cut. Script and edit revisions update affected cue links and cross-scene audio ranges.

## Initial prompt package: a dedicated audio section

Include audio in gate 1 alongside picture: sound direction, emotional progression, cue sheet, intended source/provider, exact prompts or approved reuse assets, output/stem requirements, sample-to-full production order, acceptance criteria and separate generation/repair allowance. “Add music later” does not satisfy this section.

Music prompts specify motif/instrumentation/performance, phrasing/rests, dramatic development, ending and exclusions. Effect prompts specify event count, subject/material/action, space/distance, duration, clean head/tail and excluded layers. Character sounds specify identity, delivery and emotion. Model timing is guidance; editorial alignment supplies precision. Voice-reference support does not establish musical-theme continuation support.

Mark unneeded layers explicitly and do not invent generation work. For native video audio, identify which layers are embedded and which are added separately to prevent duplicates. Samples require existing generation authorization; a plan alone is not spend permission. Review audio within the existing package/draft gates, without automatically introducing another whole-project approval.

## Produce, audition and mix independently

For a new direction, start with a short representative music sample and a few signature effects; follow the agreed listening checkpoint before expansion. Sample duration/count follow the project, not a previous episode. Evaluate phrasing, timbre, naturalness, emotion and repetition through listening, not file existence or loudness alone.

Keep music, ambience, actions, interface sounds and character voices separately editable where needed. Preserve originals, gain-adjusted audition copies and mixes with source/prompt/hash, task outcome, trims/gain and timeline mapping. Audition gain is not the final mix level. Missing or temporary audio remains unresolved; do not silently substitute coded tones for the planned instrumental performance.

Preserve failure evidence, reconcile timeouts and stop automatic attempts after repeated audit rejection; do not invent a reason or silently change providers. Continue independent picture work while disclosing the audio gap. Full-speed listening assesses sync, balance, transitions, ending and density. See [production and QA](production-and-qa.md) and [tracking](production-tracking.md) for recovery and delivery rules.


## Audible event and music-edit checks

- File start is not necessarily audible event start. Inspect leading silence and audition the cue, then align its perceptible onset with the visual event. Preserve the original and record source trim/offset; a waveform alone does not establish correct perceptual sync.
- For looped or shortened music, audition every join, repeated motif and final cadence in context. Check repetition, phrasing, abrupt timbre changes and clipped tails; a crossfade or successful encode does not prove a natural musical join.
- Use a pause before a reaction or ducking under dialogue/character sounds when it serves the scene. Do not prescribe a pause at every cut, fixed gain values or one universal cue density. Record unperformed listening checks as such within the existing review process.
