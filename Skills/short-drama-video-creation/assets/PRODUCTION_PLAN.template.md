# Production plan — <project title>

Status: plan / animatic / motion draft / final review cut / accepted final

## Gate 0: workflow and model confirmation

Complete after project inspection and confirm before production begins. Defaults are proposals, not spend permission. Existing matching explicit approval can be recorded here.

| Stage | Proposed model | Native source resolution | Exact model/version or endpoint | Provider/Region | Mode, ratio, duration limits, frame/audio controls | Capability evidence / unresolved checks |
|---|---|---|---|---|---|---|
| Complete motion draft | Seedance 2.5 (SD2.5) | 480p | | | | |
| Final source generation | Seedance 2.5 (SD2.5) | 1080p | | | | |

- Initial story/scene breakdown, target runtime and proposed model-aware lengths:
- Continuous transitions requiring start-frame + end-frame bridge jobs; intended cuts:
- Draft/final initial job counts and generated seconds, including bridges:
- Separate keyframe/audio/repair limits and final-production reserve:
- Draft coverage, final export size/fps, delivery path:
- Review sequence: gate 0 plan → gate 1 exact inputs → gate 2 complete draft/final authorization → gate 3 final export acceptance:
- Actual user decision, date/reference, plan version and approved deviations:
- Missing capability/authorization decisions and affected work:

`Draft` is a production stage, not an instruction to set API `draft=true`. Never assume draft-to-final conversion, two-frame conditioning or a model alias is supported.

## Brief

- Goal, audience, story/hook, and intended response:
- Original / reference-led adaptation; preserved versus changed elements:
- Duration, aspect ratio, visual treatment, language:
- Final source specifications and export specifications:
- Dialogue, native/separate audio, music/SFX, exact text treatment:
- Quality priority and draft coverage (high quality defaults to full motion cut):
- Asset storage location and access method (ask if unknown):
- Editor/project path and agreed output/delivery directory:
- Authorized spend/currency, repair limits, final-production reserve:
- Existing approvals and explicit workflow exceptions:

## Reference inventory and gaps

| ID/version | Path/source | Role/invariants | Must not control | Shots | Access/quality/reuse constraints |
|---|---|---|---|---|---|

| Gap | Affected shot | Blocking/useful/optional | Likely defect | Specific addition or alternative | Decision/status |
|---|---|---|---|---|---|

## Script and timed storyboard

Write dialogue, visible beats and sound intent together from the first version. Specify music/emotional progression, ambience, action/character sounds and intentional silence. Include source-evidence limits for adaptations.

| Scene / shot | Timeline/duration | Cast/scene/camera | Entry → action → result / dialogue | Sound: cue IDs / carry-over / silence | Sync anchor / acceptance criteria |
|---|---|---|---|---|---|

### Performance and inherited state

Use for character beats, including purposeful reactions; do not require large physical movement in every shot.

| Shot | Trigger / main action or reaction purpose | Initial → final emotion / visible cues | Framing / reference roles / conflicting constraints checked | Location / positions / gaze / prop and unfinished-action state carried across cut | Landing / reading time |
|---|---|---|---|---|---|

### Text, localization and viewing layout

- Project style/version; primary focus versus dialogue/card roles:
- Target platforms, aspect ratio, viewing size and safe-area basis; real publishing-preview status:
- Required languages and order; coverage of dialogue, names, UI, notifications, messages, statuses and end cards:
- Character display-name / terminology glossary; internal IDs kept separate:
- Shared text source or reconciliation method for graphics, captions and sidecars:
- For technical demonstrations only: input/result consistency, simulation label, capability/platform claim sources and verification dates:

| Beat | Primary visual focus | Dialogue adds | Graphics/card adds or is omitted | Full bounds / motion obstruction / longest translation / reading-time check |
|---|---|---|---|---|

### Scene duration and model fit

Give every scene an exact length and matching prompt/job mapping. SD2.5 can use longer coherent sequences when supported; SD2.0 scenes exceeding its verified limit need multiple jobs. Creative ranges are not capability guarantees.

| Scene | Editorial seconds | Beat timing / dialogue allowance | Model / generation mode | Job IDs and requested seconds | Exact prompt path/version | Why this length / split |
|---|---|---|---|---|---|---|

### Boundary and transition plan

Classify every adjacent scene pair. For continuous generated bridges, outgoing selected end frame = bridge start input; incoming selected start frame = bridge end input. Freeze both neighbors before extracting actual endpoints and reviewing the bridge package.

| Boundary / bridge ID | From / to scene | Continuous bridge / intentional cut / other + reason | Outgoing state → causal motion → incoming state | Generated seconds / selected interval / timeline | Exact prompt version / audio carry-over | Draft/final dependency status |
|---|---|---|---|---|---|---|

| Bridge / stage | Start-frame path/hash | A parent hash + selected out timestamp/frame | End-frame path/hash | B parent hash + selected in timestamp/frame | Dimensions/crop / verified two-frame mode | Gate-1 input approval |
|---|---|---|---|---|---|---|

- Endpoint feasibility: posture, props, geography, camera side/direction/velocity, light:
- Provisional designed endpoints versus extracts verified against actual clips:
- Unsupported two-frame controls and explicitly approved alternatives:
- Scene selected seconds + bridge selected seconds − declared edit overlaps = total runtime:
- Runtime reallocation or user-approved extension for added bridges:

### Exact scene and bridge prompt card (repeat per job)

- Scene/shot/job ID, stage, model/mode and requested duration:
- Ordered input roles/versions; actual first/last-frame roles for bridges:
- Opening framing/state and identity/prop/environment invariants:
- Contiguous timed beats covering the full requested duration:
- Camera path/speed, contact/occlusion, closing state and landing:
- Dialogue/native audio settings or separate cue IDs/silence; exclusions:
- Acceptance criteria, prompt path/version/hash:
- Draft/final settings difference and any newly reviewed endpoint inputs:

## Independent audio plan and initial prompt package

- Sound direction, theme, emotional progression, intentional silence:
- Music instrumentation/performance, phrasing, development, ending and exclusions:
- Character voice/sound identity, emotion, on/offscreen position and density limits:
- Native-video audio versus separate stems; unneeded layers and reasons:
- Exact prompts / approved reuse sources and versions:
- Sample → agreed listening check → full assets → sync/mix → full-cut listening:
- Provider/capability evidence, output/stem requirements, request/repair allowance:
- Acceptance criteria and unresolved decisions:

| Cue ID / type | Shots / time window | Purpose / timbre / distance | Entry/exit / sync anchor | Priority/ducking | Prompt/reuse source | Acceptance criteria |
|---|---|---|---|---|---|---|

### Audio execution (linked to the planned cues)

| Cue ID | Planned/actual placement | Original/audition/mix hashes | Task/outcome/cost status | Trim/gain/stem | Technical/listening QA | Temporary/final/open gap |
|---|---|---|---|---|---|---|

## Shot production matrix

| Shot or bridge | Generated/reused/editor-made | References/keyframes/prompt version | Draft model/settings | Final model/source settings | Generated duration / used range | Draft status | Final status | Final local path/hash |
|---|---|---|---|---|---|---|---|---|

## Generation records

- Selected draft/final models and creative settings:
- Exact prompts and ordered reference versions: <local package paths>

| Job/shot/stage | Request fingerprint | Task/request ID | Status | Original path/hash | Usage/cost basis | Review result | Recovery next step |
|---|---|---|---|---|---|---|---|

## Budget

Use existing authorization and known costs only; monetary fields may remain unknown. Record task counts and usage without price lookup.

| Stage | Estimate/currency/unit | Pending commitment | Usage-derived cost | Settled charge | Authorized ceiling |
|---|---|---|---|---|---|
| References/keyframes | | | | | |
| Draft video and repairs | | | | | |
| Draft transition bridges and repairs | | | | | |
| Final video and repairs | | | | | |
| Final transition bridges and repairs | | | | | |
| Audio/storage/render | | | | | |

Remaining authorization and reserved final budget:

## Review history

| Gate | Package/version and artifact hashes | Covered shots/settings/cost | Actual user decision/reference/date | Accepted limitations | Invalidated by / replacement |
|---|---|---|---|---|---|
| 0: workflow/models | | | | | |
| 1: production package | | | | | |
| 2: revised draft → final | | | | | |
| 3: final cut | | | | | |

## QA and revisions

| Stage/file hash | Shot/timecode | Check and evidence method | Pass/fail/not checked | Defect/fix | Dependent shots | Recheck result |
|---|---|---|---|---|---|---|

## Delivery audit

- All planned shots mapped to approved final assets/editor sources:
- All boundaries accounted for; bridges use reviewed final-stage endpoints:
- Both joins and full bridge motion checked in playback; no repeated/skipped action or color/velocity jump:
- Scene/bridge durations and selected intervals reconcile to the approved runtime:
- Current reference/prompt/asset versions mounted; no accidental draft plates:
- Native source specifications verified; intentional exceptions recorded:
- No placeholders or missing required performances:
- Actual export path/hash; duration/dimensions/fps/audio/decode checks:
- Full playback/listening and semantic checks, or explicit human verification:
- Open limitations and acceptance evidence:
- Gate-3 acceptance for this exact export:
- Final deliverables and provenance/QA record locations:

## Execution and delivery evidence

- Single current status / historical record / next action:
- CLI entry point, target product/Region, capability evidence and runtime version:
- Immutable approved package/hash / separate execution ledger / reproducible scripts:
- Submission attempts / accepted / completed / generated seconds / unknown pending outcomes:
- User continuation and its scope, separate from motion QA:
- Audio source/hash / temporary or final / timeout reconciliation / listening status:
- Original → mounted source → derivative → actual export hash:
- Validator checks actually enabled / browser ran / snapshots cover each scene:
- Full decode / black intervals / peak levels / normal-speed viewing and listening evidence:
- Native source dimensions/fps / draft canvas / final output specification:
- Complete playable review file and entry point / specific remaining human decision:


## Revision and delivery checks

- Affected time window and defect; existing source-range / editorial / local postproduction repair considered before new generation:
- If final-source quality is a tradeoff: regeneration versus preservation comparison, actual user decision, source/output specifications and disclosed limitation:
- [ ] Character reactions have a visible cause; inherited positions, gaze and prop state remain coherent after inserts.
- [ ] Language coverage and glossary are complete for the requested version; text/graphics/sidecar revisions agree.
- [ ] Full text bounds fit the project safe area; animation states and action peaks remain readable at viewing size.
- [ ] Duration edits propagate to captions, graphics, cues, music, joins and documentation.
- [ ] Audible cue onsets, music loop/edit seams, repetition and ending were listened to, or explicitly marked not checked.
- [ ] Technical demonstration claims and input/result logic checked where applicable; unrelated projects mark this not applicable.
