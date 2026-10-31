# From Shared Analysis to a Remake or New Story

## Use the Shared Analysis and Selected Mode

Read the [shared source-analysis contract](../../../../Skills/viral-remake-skill/prompts/analysis.md) and [adaptation choice](adaptation-modes.md), also linked from the entry skill. They govern evidence, Hook, audience experience, style, main attraction points and the 复刻 / 改写故事 interaction. Do not maintain a separate Trend analysis or infer the choice from the entry name.

Reuse the source findings in the existing review. Resolve the mode before committing the adapted story; analysis-only work does not require a choice. Retain timestamps, evidence limitations and the distinction between source observation and invented adaptation.

Carry a compact preservation map into the treatment:

| Source evidence/time | Selected Hook, experience, style or attraction | Actual carrier | KEPT/CHANGED in this mode | New action/view/sound and output check |
|---|---|---|---|---|

For 复刻, additionally map the main source progression and shot functions to new beats, explaining changes to actions or rhythm. Do not promise identical cut points unless explicitly selected and measured. For 改写故事, build a new premise, action sequence and ending; preserve selected appeal without defaulting to the old plot or shot order.

Both modes must preserve the selected Hook carriers and visual/sound relationships, not just props or a color list. Keep intentional stillness, reactions and repetition when these are the attraction. A changed mode reuses valid source evidence, not approvals of now-changed generated inputs.

## Develop the storyline as viewer discoveries

Write the audience promise and final feeling in one sentence each. Then write a compact treatment at the requested scale within the selected mode. A remake retains its chosen source progression; a rewrite may create a new one.

For each beat answer:

1. What does the viewer know entering it?
2. What new action, image or sound changes that understanding?
3. What visible consequence carries us forward?
4. What would be lost if this beat were removed?

Remove a beat with no distinct contribution, or give it a purposeful pause/reaction function. Do not force a twist, obstacle or escalation on every genre. Do not stretch a short reference into a longer procedural film without checking whether new discoveries justify the extra time.

Distinguish event density from cut density. More cuts, locations or camera moves do not automatically create interest. A sustained shot can work when its information evolves; several beautiful views can still repeat the same information.

For performance, specify trigger, initial state, visible response and resulting state. Keep actions natural for the actual cast. No automatic human gestures for animals or animal restrictions for human actors.

An emotional turn, shared look or deliberate pause can be a shot's primary story contribution, not a fallback after generation fails. Describe its trigger, readable change and consequence. Do not force extra walking, handling or exaggerated motion to meet a generic action quota; reject meaningless filler rather than quiet acting.

Use `entry state -> subject action -> object response -> exit state -> viewer meaning`. Distinguish adjacent stages by their states and function, not only by increasing motion amplitude. One continuous causal action can include anticipation, change, completion and inspection; these do not automatically require four shots or four generation jobs.

Before removing an impossible gesture, record its function and choose a plausible equivalent for the selected realistic or anthropomorphic treatment. If equivalence is unresolved, recommend a concrete alternative and disclose the fidelity tradeoff. Do not remove agency by default. Mark invented gestures, automatic prop behavior and new causes as adaptations, not source observations. Do not impose active performance, escalation or a punchline on intentionally quiet, repetitive or open-ended work.

## Translate direction into camera language

For each shot, write the camera's editorial purpose before lens or movement terms:

- Discover: limit context so the viewer notices a meaningful detail.
- Explain: reveal enough geography to read action, contact and consequence.
- Align: share a character's attention or distance from the event.
- Reframe: change interpretation by revealing scale or offscreen information.
- Conclude: show the result and allow the chosen ending to register.

These are options, not a mandatory sequence. Specify shot size, height/angle, camera side, visible subject/contact points, start/end composition, movement direction and approximate pace. Do not label a steep oblique view "top-down" or substitute a zoom for a physical move without acknowledging the difference.

Stage the action and camera together. If a mechanism must be understood, keep cause and result readable in the chosen view. If the shot must keep several characters visible during a move, explicitly check that the path and final framing permit it. Split an overloaded farewell/orbit/aerial reveal/cloud-entry shot when those goals cannot all register in the allotted time.

Create a small geography sketch only when connected action needs it. Fix screen direction, object state, eyelines, scale and meaningful identity details. Camera movement changes the view, not the world layout. Mark newly invented offscreen environments as creative design, not previously verified geography.

## Design the joins before generating

For each boundary declare a direct cut, match/action cut, sound bridge, motivated continuous move, or intentional discontinuity. Explain what carries attention across it.

Record outgoing and incoming state: subject position, gaze, contact/prop state, action phase, object shape, lighting and camera motion. A color match alone cannot repair a causal contradiction.

Use a generated bridge only when required intervening action must be visible. Budget its seconds and dependencies. First/last-frame conditioning requires actual tool support for those roles; generic reference images are not equivalent.

For dependent bridges, extract endpoints from selected source ranges, not blindly from the untrimmed files. Review the paired endpoints with their neighbors before the bridge call. New endpoint images require affected-job approval; do not claim earlier approval covered unseen bytes. Check returned endpoints and movement rather than assuming the model obeyed.

## Compile prompts from the selected treatment

The prompt must express the chosen directing decisions, not redesign the story during submission. Separate technical settings from creative prose. Write a standalone prompt for each job; avoid "continue the previous shot."

Use the actual supported input roles and a compact structure:

```text
Job and technical contract: model/mode, requested seconds, aspect, resolution,
audio setting, ordered reference IDs and authority. Keep these outside prose.

Opening: visible location, subject positions, initial physical state,
framing, light and shot-specific identity/prop invariants.

Performance intention: the selected behavior/contrast or deliberate stillness
the viewer must read; put its observable carrier early, not just "funny".

Timed beats: contiguous approximate intervals over the requested duration;
one readable causal progression with anticipation, contact/action and result.

Camera: why this view, start/end composition, path, direction and speed.
Ending: resulting state, intended landing hold or continuing motion.
Sound: native audio intent or separate cue IDs, including intentional silence.
Exclusions: only relevant failure constraints.
```

Do not bury the action under repetitive identity descriptions or generic quality adjectives. Assign identity, design and composition references distinct authority. Check contradictions such as locked camera plus orbit, fixed gaze plus looking away, and a last-frame state inconsistent with the requested action.

Keep only necessary identity invariants and exclusions; do not enforce a universal word limit. Distinguish anatomical disappearance from natural occlusion during a turn. If a result requires a visible cause, include it; do not request motionless hair under unchanged airflow without a feasible selected explanation. Deliberate ellipses remain valid when part of the chosen treatment.

## Trace analysis into the final prompt

Before image commissioning, then again against the exact rendered video prompt, trace:

`source evidence -> selected mechanism -> adapted action/view -> actual prompt clause -> reference authority -> output check`

Use the existing beat/shot table or a short linked note. Check that essential behavior survives templates and rendering; a rationale in a planning field that never reaches the model is insufficient. Review the compiled prompt, not only the storyboard or its template.

- Detect active subject action replaced by wind, camera movement or a still pose.
- Detect distinct stages collapsed into repeated motion with larger amplitude.
- Recheck cropping, prop fixation and movement restrictions against their creative cost.
- Verify the chosen view can show both required action and resulting state.
- State which changes are intentional and selected, rather than calling them faithful reproduction.
- Ask whether a materially flatter version lacking the chosen mechanism could also satisfy every instruction. If yes, specify the missing behavior instead of adding adjectives.

WorkBuddy example: `sitting calmly` and `two very small head turns` in V1 weakened the selected serious, exaggerated grooming performance. V2 restored lifted-chin poses, broader hair sweeps, formal clothing and a deadpan finish; the user reported substantial improvement. Retain these as useful practices for that premise, not a universal formula or proof that one model alone caused the gain. A quiet observation reference may correctly require the same calm language that failed this example.

Example, not a fixed preset:

> One continuous five-second shot. Begin tightly on droplets falling from the underside of the same suspended cloud. From 0-2 seconds, the camera moves backward to reveal the approved operator and the pedal mechanism, maintaining the established camera side. From 2-4 seconds, the operator presses once; after contact, the linked plates close and a stronger stream falls into the basin. From 4-5 seconds, the pedal and plates return while the cloud remains attached. Finish with the operator, pedal and cloud visible. No internal cut, reverse water flow or second cloud.

Use that example only if the selected cast, geometry and service make the action feasible. Timings are model instructions, not guaranteed output events. Measure the result before choosing source ranges or syncing sound.

## Self-review before asking the user

Before image commissioning, publish the full treatment/timed storyboard with a compact whole-film review in the existing project entry. Check these decisions internally, then expose the concrete findings rather than just a checked list:

- The adapted premise stands on its own and the selected source mechanisms remain perceptible.
- Every required beat has a view that can show it; actions are not described outside the frame.
- Similar adjacent framings are intentional, not an accidental default.
- The runtime allows necessary discoveries and reactions without duplicate preparation.
- Camera and action density fit the chosen model/mode.
- Each join has compatible states or a meaningful deliberate discontinuity.
- Music has a planned function, and the important visual payoff has a sound/timing intention.

For each material issue record `beat/time -> audience consequence -> revision or reason to retain -> unresolved image/motion/sound test`. Include competing demands from text, faces, action and music, even when each shot looks acceptable alone. Trace the selected source mechanism across the whole sequence and ending, not just its first shot. State what remains unverified; a sound or performance written in the storyboard has not been observed in output.

If the direction is weak, revise the package before commissioning images. Reuse already settled choices; this visible review is a creative deliverable, not a mandatory extra approval. Ask only for unresolved consequential direction. Do not make the user supply missing camera language after generation.

## Prompt disclosure in review

Show the complete image prompt before each planned image batch, and the complete video prompt before its submission approval. Use per-image/per-job cards linking story function, selected images, ordered reference authority/exclusions, technical parameters and acceptance criteria. Do not replace exact prose with the structured outline above, a summary or a request.json path.

Expand shared constraints and appended repair clauses in the rendered review, even if the authoring system stores them separately. Check the compiled text and settings against the actual outgoing request. After generation pair the same card with the original result, inspected defects and disposition; do not rewrite submitted text to match what the model happened to do. Historical missing disclosure is labeled retrospective, not backdated approval.
