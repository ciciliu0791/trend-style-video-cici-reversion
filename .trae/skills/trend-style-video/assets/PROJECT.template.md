# Reference-Driven Video Project

Copy once for a new production; reuse existing records on revision. Fill progressively and remove irrelevant fields. Link detailed machine records rather than duplicating them. Empty fields are not approvals.

## Current Review Entry

- Current creative version / completed deliverable / next action:
- Full storyboard and whole-film findings:
- Image set and full image-prompt cards:
- Full video-input cards / current playable cut / inspected export:
- Concrete unresolved user decision, or none:

Link this entry in chat and the main review. Keep complete prompts in readable cards, not only request.json. Proposed, submitted and retrospectively disclosed inputs must be distinguished. Technical facts below are supporting records, not the creative review.

## Current State (Shared Machine Summary)

<!-- project-control:start -->
- Structured index: `project-state.json` or explicit legacy mapping:
- Workflow owner: `trend-style-video`; current requested scope / character profiles:
- Last check event / evidence date:
- Completed task count / current artifacts / unperformed checks:
- Checker candidates / affected blocks / existing-ID recovery:
- Planned attempts / authorized creations / consumed or reserved creations:
- Project / request type:
- Current stage / status:
- Current script / package / cut / editor path:
- Next action / blocking dependencies:
- Remaining authorization / pending task IDs:
- User decisions already settled:

| Q-ID / decision key | Question / why now | Recommendation / alternatives | Blocked tasks | Independent next work | Status / answer evidence |
|---|---|---|---|---|---|

Mirror reconciled state here; do not overwrite user prose outside these markers. No open questions is valid. Checker candidates are not spending approval, and a positive viewer reaction does not complete unperformed QA.
<!-- project-control:end -->

## 1. Source, Story and Camera Review

### Brief and Original Direction

- Adaptation choice: pending / 复刻 (structure-remake) / 改写故事 (story-rewrite):
- Choice evidence: user's words / linked decision; reuse explicit prior choice:
- Selected Hook / audience experience / style relationships / main attraction points to preserve:
- Allowed story, action, shot-order, ending and timing changes:
- Audience / intended experience:
- Original premise / point of view / ending effect:
- Target runtime range / aspect / native source and delivery specifications:
- Cast / identity / world rules / adopted palette:
- Text, language and dialogue:
- Music route / ambience / effects / silence:
- Music needed / deliberately absent / unresolved; why:
- Deadline / destination / assets location:
- Must preserve / must not copy:
- Timing intent: functional/rhythmic fidelity for remake / new-story timing for rewrite / explicitly requested measured close timing:

Use the existing decision key `adaptation-choice`; this section adds no required machine-schema fields. Analysis-only work may leave the mode pending. Mode selection is not production authorization. Existing projects keep their current owner and records.

### Source Evidence and Style Map

- Source IDs and URLs/files:
- Inspected intervals; timing measured or estimated:
- Motion inspected / sound heard / transcript verified / unknown:
- Evidence of popularity, if claimed; otherwise unverified:
- Decision-critical unknowns / affected conclusions / feasible limited work:

| Style dimension | Evidence/time and observed/user-reported/inferred/unknown | Mechanism and visible/audible carrier | Original choice / deliberate departure |
|---|---|---|---|
| Hook: first cue, sustained interest and payoff | | | |
| Audience experience and main attraction points | | | |
| Discovery and causal action | | | |
| Rhythm and camera | | | |
| Film style, palette, light, material and costume function | | | |
| Sound and silence | | | |

For each selected attraction, identify its carrier, proposed audience effect and what may change without losing it. In remake mode map the main source progression and shot functions; in rewrite mode show their selected functional equivalents without requiring identical source cuts.

### Story, Camera and Sound

- Directing intention:
- Treatment:
- Full script/dialogue or readable treatment body:
- Camera progression / geography / continuity invariants:
- Musical event intended to support the visual payoff:

| Beat / shot ID | Viewer entry -> discovery / source function | Entry -> subject action -> object response -> exit | Camera purpose, start -> end view/path | Editorial seconds | Kept/changed function and continuity | Sound cue IDs |
|---|---|---|---|---|---|---|

For a short film, use brief notes in this table rather than separate analysis documents. One continuous causal behavior may contain several stages without requiring separate shots/jobs.

| Join | Treatment and motive | Outgoing -> incoming state | Dependency / feasibility / uncertainty |
|---|---|---|---|

### Whole-Film Findings Before Image Commissioning

Review mechanism transfer, causality/discovery, emotion, space, camera feasibility, competing face/action/text attention, sound rhythm and ending. A meaningful reaction or deliberate stillness needs no invented physical action to pass. A completed beat table is not this review.

| Beat/time | Audience consequence or uncertainty | Revision or reason to retain | Image/motion/sound test still needed | Ready or material unresolved direction |
|---|---|---|---|---|

## 2. Image Prompts and Minimal Reference Review

| Character | Identity | Hair shape/length and color | Ears/anatomy | Costume | Body proportions and apparent height/position | Allowed change / selection evidence |
|---|---|---|---|---|---|---|

- Existing approved identities and look:
- Proposed new image count / cost / attempts:
- Contact sheet, full-resolution links and per-image prompt cards:
- Independent image batch vs selected-image dependencies:
- Source evidence frames vs actual conditioning images; why each input is needed:
- Exact input crop QC: edges, residual props/tags, mirror direction and cross-reference conflicts:
- Initial candidates / targeted repairs / approved remaining count (repairs are real calls):

| Reference ID/version/hash | Role and authority | Question resolved | Shots | Blocking/useful/optional | User selection / agent QA |
|---|---|---|---|---|---|

### Image Review Card (Repeat for Each Needed Image)

- Frame ID / shot coverage / mechanism or state it resolves:
- Actual image link or explicitly not generated / selected version:
- Staging, identity, emotional state, camera and continuity intent:
- Tool/model/provider / size / effective settings / scoped attempts and cost:
- Prompt version / proposed, submitted, retrospective disclosure, or reuse:

| Input order | Viewable reference/version | Actual role | Controls | Exclusions |
|---|---|---|---|---|

Complete image prompt, including shared constraints and appended corrections:

```text
Insert the exact full image prompt. Do not substitute an outline, "same as above" or JSON link.
```

- Individual and cross-image QC / defect and disposition / neighboring frames to recheck:
- User selection or pending consequential choice:
- Actual request/hash trace and comparison with reviewed text:

For reuse cite the selected source and original evidence rather than inventing a new prompt. Disclosure precedes image calls but adds no per-image spending approval. Batch independent work; honor actual selection dependencies and repair limits.

## 3. Exact Video Inputs and Production Package

- Package version / immutable snapshot and hash:
- Complete image and video review-card body/entry (raw request files are supplementary):
- Model/provider/endpoint/region / capability and price evidence:
- Actual mode/input roles / resolution/aspect/duration/audio constraints:
- Proposed pilot uncertainty, if any:
- Audio generation/reuse/permission plan:
- Draft/reuse/final route; no automatic quality upgrade:
- Input evidence: file readable / client declaration / serialized request / backend evidence; unknowns:
- Preflight evidence IDs and controlling versions: capability / authentication / transport / price:
- Analysis-to-prompt trace: source mechanism -> adapted action/view -> final prompt clause -> reference -> output check:
- Counterexample check: could a version lacking the selected mechanism satisfy this exact prompt?
- Deliberate tradeoffs from cropping, fixed props or movement/anatomy restrictions:

| Job ID | Shot(s) / dependency | Exact prompt version/hash | Ordered inputs/roles/hashes | Requested seconds/settings | Planned selected seconds | Attempts / estimate |
|---|---|---|---|---|---|---|

### Video Review Card (Repeat per Job)

- Job ID / shot function / viewer discovery:
- Selected images and their stage-2 review cards:
- Technical settings and reference authority:
- Opening composition/state:
- Intended performance/contrast or deliberate stillness and its observable carrier:
- Contiguous timed action:
- Camera purpose/path:
- Closing state/hold:
- Sound cue or native audio intent:
- Shot-specific exclusions and acceptance criteria:

| Input order | Viewable reference/version | Actual supported role | Controls | Exclusions |
|---|---|---|---|---|

Complete video prompt, not just the directing fields above:

```text
Insert the exact standalone compiled prompt with shared constraints and appended revisions.
```

- Proposed/submitted version / request comparison for text, input order and parameters:
- After generation: playable original / technical and performance defects / affected joins:
- Changed input comparison and affected-job decision, if required:

### Sound in the Same Review

- Cue roles / full audio prompts or permitted source files / native versus separate audio:
- Source/license / independent spending scope / sample-listening and full-cut plan:
- Missing or temporary sound / explicitly silent visual-draft scope:
- Music payoff and actual sync anchors; pending human-supplied track:

## 4. Complete Motion Cut and Coherent Review

- Playable complete cut/version/runtime and originals:
- Actual sound / temporary or missing layers / authorized silent-draft status:
- Whole-cut experience, frame/join, normal-speed motion and listening evidence:

| Cut/time | Evidence type and observation | Viewer consequence / severity | Smallest repair | Affected dependencies | Recheck/status |
|---|---|---|---|---|---|

| Unperformed check: file/time | Specific question and required method | Proposed reviewer | Returned evidence or still unchecked |
|---|---|---|---|

Presence in the draft does not mean approved final footage. Pass continues covered work; repair must be assessed for dependency impact; blockers stop only affected work; unchecked critical geometry is not permission to expand dependent jobs.

- Revision before/after comparison and whole-sequence result:
- Current coherent user decision, not per-clip routine approvals:

## 5. Finishing Plan and Actual Export

| Shot | Retain / trim / postproduction / regenerate | Reason and source range | Native source/output specification or explicit exception | Changed paid inputs/cost and approval |
|---|---|---|---|---|

- Picture-lock or selected cut version:
- Actual export path / hash / specification:
- Technical actual-file QA and full-cut playback/listening evidence:
- Source resolution, output resolution, crop/upscale disclosure:
- Known limitations / missing checks:
- User acceptance evidence and exact version, or awaiting review:
- User-reported improvement, separate from technical/semantic QA:
- Current file/hash and task terminal status synchronized; editor's actual version:

Preserve satisfactory performances; a finishing plan does not require another generation round. Do not treat a draft approval as quality-exception approval or spend permission. The two planned production checkpoints are stage 3 inputs and stage 4 complete-cut review, followed by acceptance of the actual export; these five deliverables are not five approval stops. The earlier remake/rewrite choice resolves creative direction once, not an additional spending gate. Current workspace rules govern covered project spending.

## Supporting Records: Decisions and Spending

| Decision ID/date | User words or linked evidence | Artifact version/hash and selected jobs | Creative selection | Authorized operations/cap/attempts | Unresolved scope |
|---|---|---|---|---|---|

| Work item | Estimate/currency/unit | Authorized scope | Pending commitment | Usage-derived amount | Settled charge | Reconciled state |
|---|---|---|---|---|---|---|

Do not add estimate, commitment, usage and settlement for the same job as separate spend.

## Supporting Records: Production and Handoff Index

| Stage | Input version | Status | Output/evidence | Next action |
|---|---|---|---|---|
| Develop/direct | | | | |
| Prepare | | | | |
| Produce | | | | |
| Assemble | | | | |
| Deliver | | | | |

Map this internal view to shared P1/P2, P3, P4, P5 and P6. The five creative deliverables above map respectively to P1/P2, P3, P3, P4/P5 and P5/P6; do not renumber shared stages or add required schema keys. Maintain it from the same index; stages overlap and are not extra user gates. Out-of-scope work needs a reason, not a fictitious completion.

- Task records / original files / selected takes:
- Missing coverage or temporary material:
- Current editor manifest / source ranges / revision history:
- Scene-relative action cues and global music timing:
- Licensing and provenance records:

## Measured Lessons

- Image candidates generated / selected / review rounds:
- Time to first complete motion cut:
- Video generated seconds / used source seconds:
- Rework cause (story, camera, reference, generation, edit or sound):
- Estimated / usage-derived / settled spend:
- User feedback and comparison limits:
- Primary iteration question / other simultaneous changes; no single-factor claim without evidence:
