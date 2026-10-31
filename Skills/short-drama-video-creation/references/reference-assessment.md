# Reference assessment

Judge sufficiency against the planned output, not an arbitrary image count. One strong image can be enough for a simple shot; ten inconsistent images may not establish identity.

## Locate the assets

Use the source already supplied by the user. If unknown, ask for the storage location and access method: local folder, shared Drive/cloud folder, conversation attachments, or another source. Ask only for missing access details; do not assume a particular cloud service. If the user has no source assets, follow original reference design below. Record original source IDs/paths separately from local working copies and confirm the delivery destination when needed.

## Inspect and map

For each input record a stable ID/version, source/local path, permission or reuse constraints known from the brief, accessible format/quality, relevant shots, intended role, invariant details, and what must not be copied. Keep identity, costume, props, environment, style, composition, motion, and audio roles separate. Identify conflicts rather than blending incompatible references silently.

Inspect actual contents. A filename, inaccessible link, thumbnail, or description does not prove full reference coverage. For source video record inspected time ranges and evidence limits. Speech needs audio review or a verified transcript; visible captions alone are not transcription. Exact source-cut reproduction needs measured timing.

Compare coverage with the storyboard:

| Dimension | Check when relevant |
|---|---|
| Identity | Clear face/body, distinguishing marks, required angles, multiple-character distinction |
| Wardrobe/props | Colors, geometry, scale, held objects, consistency between shots |
| Environment | Layout, entrances, exits, lighting, geographic relationships |
| Style/composition | Medium, palette, framing, camera perspective, intentional deviations |
| Action | Entry state, contact/operation, visible result, spatial sides, anatomy |
| Transition endpoints | Outgoing selected end frame and incoming selected start frame; matching identity/props/geography, feasible motion, camera/light compatibility and verified first/last-frame input support |
| Audio | Exact dialogue, pronunciation, voice direction, timing, reuse permission |

For a two-frame bridge, preserve each endpoint's parent clip hash, selected boundary timestamp/frame index, local image hash and crop/aspect-ratio settings. Review the pair together and in context with neighboring motion. Designed keyframes remain provisional until checked against actual outputs. A scene/style reference is not a first/last-frame condition; output last-frame retrieval alone does not prove two-frame input support. Reject contradictory endpoints before trying to interpolate between them.

## Report gaps with a remedy

Use `blocking`, `useful improvement`, or `optional`, with the affected shot, likely failure, and smallest useful addition.

- **Blocking:** an identity-critical subject is unidentifiable, a required input is unreadable, references contradict a required invariant, or the requested exact behavior cannot be established. Pause dependent generation until a reference, revised shot, or explicit acceptable limitation resolves the requirement. A technical input requirement cannot be waived by accepting visual uncertainty.
- **Useful improvement:** an additional angle or prop detail would materially reduce drift but the shot is feasible. Recommend it; do not turn the suggestion into an unnecessary stop.
- **Optional:** added richness with little bearing on acceptance. Continue without it unless requested.

Example: “S04 shows the character in left profile, but R01 is front-facing. A clear left-profile image with the same hairstyle and costume would reduce identity drift. Alternatively, change S04 to a three-quarter view or approve a generated profile reference.”

Offer existing approved assets, user-provided additions, reference creation within an authorized image budget, simpler staging, or a documented limitation. Do not silently drop identity references, publicly share private media to bypass transport failures, or request coverage unrelated to planned shots.

## Original work with no references

Ask only for creative constraints that matter. Propose a compact character/environment/style direction, create or select the minimum useful anchors within authorization, and include those anchors in gate 1. Treat invented detail as creative design, not missing evidence. Reassess sufficiency if revisions introduce new angles, interactions, costumes, or locations.

## Resolve competing reference authority

Give each important attribute a primary reference, with secondary inputs limited to named roles. For example, a front identity reference can own facial markings, a side view their projection, a full-body image proportions, and a scene image furniture/light only. State the conflict rule explicitly; do not average incompatible identities or inherit background text and marks. Preserve the exact input order, role descriptions and hashes used in the approved submission.
