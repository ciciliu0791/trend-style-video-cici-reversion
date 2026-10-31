# Scene timing, prompts and two-frame transitions

## Plan by model and dramatic beat

Distinguish a scene (editorial story unit), a shot (camera unit), and a generation job (model request). One scene can use several shots/jobs; a supported longer generation can cover a coherent sequence. Give every scene an exact proposed editorial length and every job an exact requested duration, timed prompt, selected source range and reason for its length. Never use "as needed" as the only timing plan.

Use these as creative starting ranges, not API guarantees:

| Model | Suggested action unit | Longer sequence policy |
|---|---|---|
| Seedance 2.5 | 4-8 seconds for a reaction/insert; 8-15 seconds for setup, action and response | Consider 15-30 seconds for a causally connected sequence with stable identity/geography and readable dialogue. Use its longer narrative capacity when useful, not a blanket 15-second cap or automatic 30-second target. |
| Seedance 2.0 / 2.0 Fast | 4-8 seconds for one main action; 8-15 seconds for a simple linked beat | Split longer scenes into individually prompted jobs and plan their joins. The project's historical route capped jobs at 15 seconds; verify the selected variant's current limits. |
| Two-frame bridge on either model | Usually 4-6 generated seconds for a small move or state handoff | Choose enough time for physically plausible travel and a settled landing; verify the selected mode's minimum/maximum. Split a complex bridge at an approved intermediate frame. |

SD2.5's longer capacity does not guarantee better acting or continuity in every long take. Retain short shots for punchlines, fragile interactions, caption readability and economical repairs. Account for spoken lines at a natural pace, pauses, anticipation, contact, response, camera travel and edit handles. Validate duration against the actual service/mode/resolution combination; project evidence records SD2.5 durations of 4-30 seconds, but edit/auto modes can have different requirements.

For a model switch, rewrite the action density, timed beats, job count and transition map and obtain approval. Do not truncate a 24-second SD2.5 prompt into a 15-second SD2.0 request or reuse the old timing unchanged.

## Cover every boundary

Give each adjacent scene pair one declared treatment: continuous two-frame bridge, match/action cut, intentional hard cut, or an approved postproduction transition. First decide whether the intervening action must be visible, using [performance and narrative continuity](performance-and-continuity.md). Use a **generated start-frame + end-frame bridge** when continuous movement or a state change must actually be shown between separately generated scenes; an insert or change of camera angle alone does not require one. A deliberate reverse shot or time/location cut need not become a morphing bridge; record why the cut is appropriate. A dissolve cannot repair missing physical action.

For a bridge `T-A-B`, plan this chain:

`scene A selected out-frame -> T-A-B start frame -> motivated motion -> T-A-B end frame -> scene B selected in-frame`

1. Specify the outgoing and incoming poses, prop state, screen positions, eyelines, camera side/height/framing, motion direction/speed, light and palette. Explain the visual cause connecting them. Fix contradictory endpoints first; do not ask a model to hide an unexplained posture change or teleport.
2. Freeze the neighboring selected clips/ranges. Extract the last displayed frame of A and first displayed frame of B, not automatically the last/first frame of their untrimmed model outputs. Record parent clip hashes, source timestamps/frame indices, image paths/hashes and extraction/crop settings.
3. Use A's out-frame as the bridge's actual first-frame input and B's in-frame as its actual last-frame input. Confirm that the current model/CLI mode accepts both roles together, along with any other required references; ordinary reference images or `return_last_frame` output support do not establish two-frame conditioning.
4. Match endpoint dimensions/aspect ratio and final-stage quality. Review any crop or regenerated endpoint with its neighbors. The recorded SD2.5 contract requires `ratio=adaptive` for first/last-frame tasks; verify the live contract and encode the intended composition in the endpoint images, not an incompatible fixed-ratio request. Do not invent flags or reference-role syntax; use the owning CLI instructions.
5. Include both numbered images, exact prompt, duration and settings in gate 1. If boundary frames only become available after neighbor generation, keep bridge approval pending, then review this small package. Approval of an earlier description is not approval of unseen frame bytes.
6. Generate once within authorization, download and check the bridge. Assemble `A -> bridge -> B`, preserving the landing. Remove only verified duplicate seam frames if they create a hitch; inspect again for velocity or pose jumps. Do not arbitrarily trim the middle out of a bridge and claim the endpoint constraints still hold.

When clips do not exist yet, approved designed endpoint keyframes can seed the plan. Mark them provisional until the actual adjacent outputs are checked. Conditioning with the same planned frame does not prove returned frames match it. If two-frame input is unsupported or incompatible with required controls, pause only the bridge, explain the limitation, and seek approval for a supported model/mode, intermediate shot, or deliberate editorial cut. Never silently send two generic reference images and call the result frame-locked.

## Write matching prompts

Create a standalone prompt for each job, including bridges. Use absolute visible descriptions rather than "continue S03." State:

- Selected model/mode, requested seconds, reference order and each input's authority.
- Opening composition, identity/prop invariants, physical state and light.
- Contiguous time-coded beats covering the requested duration, with one readable causal progression.
- Camera path, screen direction, speed/easing and occlusion/contact constraints.
- Closing composition/state, landing hold or continued motion matching the next clip.
- Native audio/dialogue or separate cue IDs and intentional silence; exclusions and acceptance criteria.

For draft and final, preserve approved story beats, durations and reference roles; state the 480p versus native 1080p settings outside the creative prose. Treat changed final endpoint images as new reviewed input versions. Model output timing is approximate: measure the result and reconcile the edit, dialogue, sound cues and runtime rather than assuming timestamp obedience.

### Matched scene examples

These are planning examples, not pre-approved prompts or universal optimal durations. Fill actual identity references and settings before submission.

**SD2.5: one 12-second scene job**

> One continuous office shot, medium-wide at seated eye height. Use the approved identity image for the single courier's face and wardrobe; use the room image only for desk geometry and soft left window light. 0-3s: courier stands at screen left holding one closed envelope in the right hand and looks at the desk to screen right. 3-7s: takes two measured steps rightward and stops beside the desk. 7-10s: places the same envelope flat on the near desk edge, with fingers contacting paper before release. 10-12s: withdraws the hand and looks toward the doorway at screen right, breathing naturally. Locked camera throughout. No cut, duplicate envelope, readable text or unexplained prop change. No generated speech; ambience cue A01 continues in post.

**SD2.0: the same 12-second scene planned as two 6-second jobs**

> Job A, 6s: medium-wide office shot at seated eye height; same approved courier identity, wardrobe, desk and left window light. 0-2s: courier at screen left holds one closed envelope in the right hand, looking toward the desk at screen right. 2-5s: takes two measured steps right and stops beside the desk, still holding the envelope. 5-6s: settles weight with natural breathing. Locked camera; no cut, prop duplication or speech.

> Job B, 6s: medium view from the same camera side of the courier already standing beside the desk, holding one closed envelope in the right hand. Preserve the approved identity, wardrobe and left window light. 0-1s: settles beside the near desk edge. 1-4s: lowers the same envelope onto the desk, fingers contact paper then release. 4-6s: withdraws the hand and looks toward the doorway at screen right. Locked camera; no new envelope, readable text or speech. Ambience A01 continues.

Plan a motivated change of shot size with matched standing/prop state for A -> B; inspect the actual cut. This simple scene may also work as one supported SD2.0 job, but splitting isolates contact-action repair. For a scene exceeding the verified SD2.0 limit, splitting is mandatory. A new bridge adds time unless the approved edit explicitly reallocates it.

### Two-frame bridge example: 6 seconds

> One continuous 6-second transition. Input 1 is the first-frame condition: a closed door at frame right, the courier's right hand already resting on its handle, envelope left on the office desk. Input 2 is the last-frame condition: the same door open inward, same courier just inside the corridor, body facing screen right, hand released, envelope absent from the hand. Match these approved endpoint compositions and preserve identity, wardrobe, door hinges, camera side and window-light direction. 0-1s: continue the starting posture with subtle breathing. 1-3s: rotate the handle, push the door inward and step through the opening with visible contact. 3-5s: camera tracks gently right through the doorway, following the same courier without crossing the action axis. 5-6s: decelerate into Input 2's framing and posture, with natural breathing. No internal cut, dissolve, teleport, door morph, duplicated limbs or new props. No generated dialogue; room tone carries through and corridor ambience enters gently in post.

Use this only if the actual two endpoints make the travel feasible. The chosen boundary states must match the adjacent clips; do not force this example onto unrelated footage.

## Runtime, dependencies and QA

Include scene and bridge jobs in both draft and final counts, generated seconds, repair ceilings and reserve. Compute editorial runtime from the sum of selected clip durations minus explicitly overlapping edit intervals; two-frame bridges normally add duration rather than overlap. Keep generation duration, chosen interval and timeline placement separate. Do not add bridges on top of an approved fixed runtime without reallocating beats or obtaining approval.

Track dependencies as `A asset/range + B asset/range -> endpoint pair -> bridge prompt/job -> assembled joins`. A change to either neighbor, trim, crop, endpoint, model or prompt invalidates the affected bridge inputs/approval and join QA. Reuse the bridge only after revalidation; regenerate only when needed and authorized. Final bridges use final-resolution neighbor frames, not draft extracts. A 1080p bridge between upscaled 480p sources is not an all-native-1080p result.

Inspect each entire bridge and at least the outgoing last second and incoming first second at normal speed, then inspect frame-by-frame around both joins. Check pose, identity, props, geography, exposure/color, camera velocity, duplicate-frame stalls, skipped/repeated action and audio carry-over. Verify continuity of the returned footage, not merely that the API accepted both frames. Record timestamped findings against the actual assembled file; sampled stills alone do not establish smooth motion.

## Project evidence behind these rules

Paths are relative to the Seedance workspace root. These are historical production records, not newly performed media QA or live capability guarantees.

- `EP04_post/records/SEEDANCE25_CAPABILITIES.json`: SD2.5 lists 480p/720p/1080p, 4-30-second generation, no API draft flag, and mode-specific ratio/duration restrictions.
- `ProjectPlan/EP01｜分镜脚本_2.0-15s限制版.md`: the older SD2.0 route split longer scenes around its 15-second limit. Do not carry that limit into SD2.5 planning.
- `EP04_post/planning/SEEDANCE_SKILL_REVIEW.md`: standing-to-seated discontinuity, conflicting eyelines and ambiguous shot-size changes required explicit state/camera planning and standalone prompts.
- `EP04_post/planning/COMPLETE_DRAFT_REVIEW.md`: native 480p sources stayed distinct from the draft canvas and proposed native 1080p final stage; final generation remained separately authorized.
- `videos/manyue-dreamcore-edit/revisions/film-transition-v7/prompt-en.txt` and `qa/review.json`: ordered state references and a motivated subject-to-shadow-to-flower camera handoff helped a difficult join; palette still required correction. This was a full-video edit with ordered references, not evidence of a tested first/last-frame bridge API.
