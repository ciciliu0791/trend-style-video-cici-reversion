# Viral remake v2

A reviewed structure-adaptation workflow for ads, creative stories and pet/music performances. Analysis can proceed offline; **video generation requires reviewed keyframes and exact prompts plus explicit user confirmation**.

## Setup

Python 3.9+, ffmpeg/ffprobe, and `pip install -r requirements.txt`. Run `python3 scripts/doctor.py` for local diagnostics; it does not call models or upload files. For live work, follow [Ark CLI execution](references/ark-cli.md) and the current official Volcengine/Ark skills. The generator uses an explicitly selected Ark profile; it never loads the old `.env` or assumes BytePlus keys work on Volcengine.

## Offline planning

Run commands from this skill folder, using a **new** project run directory. Replace example paths.

```bash
python3 scripts/probe.py --run /project/run --video /project/source.mp4
# Alternative for evidence actually observed in a browser:
python3 scripts/probe.py --run /project/another-run --observations /project/observations.json
python3 scripts/analyze.py --run /project/run --brief /project/brief.yaml --import-json /project/analysis.json
python3 scripts/storyboard.py --run /project/run --brief /project/brief.yaml --import-json /project/storyboard.json --tag v1
```

The agent can author the analysis/storyboard JSON from inspected evidence. Optional `--generate --analysis-budget-authorization 'actual authorization'` uses the configured text route for one paid analysis/storyboard call. No automated retry on failed JSON; raw response is retained. Budget these calls separately in external_reserve. Imports require no model credentials.

## Keyframes → exact prompts → confirmation

1. Confirm text method, audio approach, storyboard, references and image budget. Set the corresponding brief fields. Discover and review current model capabilities and pricing; populate explicit route snapshots.
2. Generate an **image review package** or select suitable existing frames. For generated keyframes, render once for request hashes, add matching quotes, render again, and record the already-given image authorization before submitting.
3. Inspect the images and select a keyframe for every distinct composition and required transition state.
4. Render the **video review package**; populate matching video quotes and rerender if necessary. Show its HTML/contact sheet, full-resolution frames, exact prompts, reference order, settings and total planned tasks/cost.
5. Wait for the human's explicit video confirmation. Record selected job IDs; then submit only those IDs.

```bash
python3 scripts/review.py --run /project/run --brief /project/brief.yaml --modality image
python3 scripts/review.py --run /project/run --approve /project/run/reviews/IMAGE_VERSION/package.json --jobs KF-1 --evidence 'Actual image-budget/reference authorization'
python3 scripts/gen_images.py --run /project/run --package /project/run/reviews/IMAGE_VERSION/package.json --jobs KF-1 --confirm
python3 scripts/gen_images.py --run /project/run --pick shot1=/project/keyframe1.png shot2=/project/keyframe2.png
python3 scripts/review.py --run /project/run --brief /project/brief.yaml --modality video
# Show review.html and keyframes, then WAIT for the user's answer.
python3 scripts/review.py --run /project/run --approve /project/run/reviews/VIDEO_VERSION/package.json --jobs S-1 S-2 --evidence 'Actual user confirmation of this displayed package'
python3 scripts/gen_video.py --run /project/run --package /project/run/reviews/VIDEO_VERSION/package.json --jobs S-1 S-2 --confirm
python3 scripts/gen_video.py --run /project/run --resume LOCAL_RECORD_ID
```

`--confirm` alone does not authorize a package. Run without it to inspect the package without submission. A changed prompt/keyframe/reference/model/settings/budget requires a new review package. Repeating a submitted package is blocked; resume instead. A targeted repair needs an updated storyboard version describing the defect/repair and renewed review.

## Finish

```bash
python3 scripts/edit.py --run /project/run --selection /project/selections.json --output /project/edit-manifest-v1.json
# Build/review/render the HyperFrames project using the current HyperFrames skill.
python3 scripts/qa.py --video /project/final.mp4 --expected /project/expected.json --output /project/technical-qa-v1.json
# Inspect/listen; record actual evidence for the exact file hash, then:
python3 scripts/qa.py --video /project/final.mp4 --expected /project/expected.json --review /project/semantic-review.json --output /project/final-qa-v2.json
```

See [interfaces](references/interfaces.md) for complete schemas, route/price normalization, recovery and edit selections. [Production lessons](references/production-lessons.md) ties the changes to the local remake records.

## Compatibility and tests

Old runs and videos are unchanged. Legacy brief fields are readable, but model defaults, hard-coded prices, unconditional two-take batches, timestamp-based selection, custom storage signing and credential-dependent local steps are retired. Scripts are orchestrators around Ark CLI and offline artifacts; old generation CLI flags are replaced by explicit `--package` / `--jobs` / `--confirm`. `assets.py` is an inert migration notice. This is not a drop-in rerun of historical scripts.

```bash
python3 -m unittest discover -s tests -v
```

Tests use local synthetic media and mocked CLI responses. They do not establish live account access, model availability or actual prices.
