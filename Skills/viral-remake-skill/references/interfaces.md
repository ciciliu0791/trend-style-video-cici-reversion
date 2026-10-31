# File interfaces and migration

All JSON is UTF-8. Existing run folders are historical inputs: use a new run and explicitly import a chosen storyboard/analysis. Paths in YAML are relative to that YAML; snapshots and manifests use absolute paths plus SHA256. No file modification-time selection remains.

## Brief and source

Copy `config/brief.example.yaml`. Legacy `product`/`person`/`copy` fields remain readable; missing mode infers ad only when product.name exists. New defaults: adaptation, balanced, plates, one take. Missing text/audio/budget is allowed during analysis but blocks production. No keys or endpoint defaults are inherited from `.env`.

`probe.py --observations observations.json` accepts:

```json
{"url":"https://example.com/reference","duration_seconds":188,
 "observations":[{"time":6,"evidence":"Observed central lead and layered ensemble"}],
 "limits":["Sampled views only; exact cuts and source audio unverified"]}
```

For local video, inspect detected cuts before using `--cuts-reviewed` in a new run. Only reviewed measured cuts enable close-timing mode. An imported transcript is `{ "available": true, "lines": [{"start":0,"end":1,"text":"verified speech"}] }`; false means unknown. No implicit ASR calls.

## Storyboard

Import JSON with title, duration and shots. Required shot fields: unique id, start/end, entry_state, action, exit_state and keyframe_brief. Include function, camera, cast IDs, source_evidence, KEPT/CHANGED reason, onscreen_text and dialogue as needed. Shots cover the target duration with no gaps. Close-timing additionally requires orig_shot and measured boundaries within 0.3 seconds.

`keyframe_from` maps shared composition to another shot; do not use it to disguise a distinct shot. `keyframe_states` maps extra transition IDs to entry_state/action/exit_state/keyframe_brief objects. Image packages create these state jobs; select their images with `--pick state-id=/absolute/image.png` before preparing video. `transition_frames` may name already selected additional frames.

For fractional edits use a whole-second `generation_duration` on that plate, sufficient to cover its intended used duration. Native generation limits remain resource-specific. `video_settings` can override supported settings, but cannot undercut the needed duration. Whole-route jobs bundle all shots and require approval as a unit; use plates for partial shot approval.

## Reviewed route snapshots

The adapter deliberately does not guess routing fields from evolving CLI response schemas. `doctor.py --discover` saves raw evidence. Following the current official Ark skills, read it and normalize each route explicitly. Keep evidence files and the route together in a private preflight folder. Unknown support blocks live generation.

```json
{
  "service":"volcengine", "profile":"your-explicit-profile",
  "region":"region-from-resource", "base_url":"https://verified-service-host/api/v3",
  "resource":"ep-actual-id", "model":"actual-bound-model", "model_version":"actual-version",
  "modality":"video", "transport":"inline-local", "checked_at":"ISO-8601 timestamp",
  "constraints_reviewed":true,
  "params":{
    "duration":{"support":true,"min":4,"max":8,"description":"Illustration only: replace with actual returned bounds"},
    "ratio":{"support":true,"enum":["16:9"]},
    "resolution":{"support":true,"enum":["720p"]},
    "generate_audio":{"support":true,"enum":[false,true]}
  },
  "input_roles":["first_frame","reference_image"], "max_references":3,
  "resource_evidence":{"path":"/absolute/resource.json","sha256":"actual-file-sha256"},
  "capability_evidence":{"path":"/absolute/capabilities.json","sha256":"actual-file-sha256"}
}
```

The numbers above are **not supported-model claims**. Normalize only actual supported parameters and read their descriptions/conditional combinations. `constraints_reviewed` attests that the agent inspected those conditions; it is not automatic semantic validation. Service, region, base URL, credential lane and model binding must be checked against authoritative resource metadata before setting it. Image routes use modality image and supported image settings such as size/output_format; text routes use modality text for analysis and declare verified input_modalities (such as ["image", "video"]) when analyzing media. Unresolved or unsupported BytePlus routes are not accepted by this adapter.

Use `common.file_ref(path)` to calculate evidence hashes. The adapter rechecks hashes and compares current resource evidence immediately before submission; changed routing requires a new package. Resource comparison is intentionally conservative, so harmless provider metadata changes can require refreshing the evidence.

## Pricing and budget

Render the first package to obtain exact job request_hash values. Unknown quotes do not permit submission. Query current pricing, select matching charge items, and write a pricing snapshot referenced by `brief.pricing`; render again for the final review. Price changes alter approval digests.

```json
{"checked_at":"ISO-8601 timestamp","source":"saved official price response or official URL","currency":"CNY",
 "jobs":{"S-1":{"request_hash":"exact-hash-from-review",
 "items":[{"charge_item":"actual-charge-item","quantity":10000,"unit_quantity":1000000,"price":46,"unit":"tokens"}]}}}
```

This arithmetic example is **not a real quotation**. Quantities must conservatively account for the actual model, reference inputs, output duration/resolution and applicable charges. Each quote is per request; takes multiplies it. An optional usage_key on each price item maps returned usage fields to usage_estimate after completion; this remains distinct from settled charges. Do not convert units implicitly or subtract a quota as though it were cash. Missing prices remain null. Refresh pricing at production time.

`budget` includes cap, currency, authorization (actual user decision), max_attempts_per_job (default 2), and external_reserve (default 0). Reserve planned analysis/audio/storage/render expenses outside this generator in external_reserve so they are not omitted from the total. Paid analysis commands additionally require their own explicit authorization; they save usage in the raw response and never retry automatically. Do not count the same expense both as external_reserve and a settled generation task.

The ledger is `tasks/*.json`: estimate, reserved, usage, usage_estimate (null until priced), settled (null until billed), currency, task_id, status and local file/hash. Unsettled or failed requests retain a conservative reservation until actual billing evidence resolves it. `recover.py --settled` records the actual amount in the ledger currency.

## Review, approval and recovery

`reviews/<version>/package.json`, review.md, review.html and contact.jpg are generated together. Review HTML links original full-resolution frames. A job digest includes its exact prompt, reference content/roles, relevant storyboard, settings, route, quote and batch/budget context.

Record approval only after the human confirms the displayed package, using its path, selected job IDs and actual confirmation text/reference. The mechanism records conversational authorization; it cannot itself prove that the human saw a screen. Never manufacture that evidence or infer video approval from image approval.

Known tasks resume with `gen_video.py --resume LOCAL_RECORD_ID`. Each invocation queries once; use bounded waits/backoff, save progress and stop on errors. It never creates another task. If the result has no local file, use `recover.py --download-response` against the saved response in that task's private output directory, or `--file` to attach a verified existing result. This is artifact retrieval, not model inference.

For `submission-unknown`, reconcile only with authoritative provider/request evidence. `recover.py --task-id` binds the recovered ID; `--no-task-created` releases the reservation only when evidence proves no task was created. A matching recent model/name alone is insufficient. No automatic resubmission.

## Editing and delivery

`edit.py --selection` accepts shots keyed by storyboard ID. Each selection has task_record (local ledger ID), source_in and qa: approved. Reuse instead requires file, reuse_authorization and provenance. Root fields include text_policy, output specification and optional audio_cues with path/start/end. The edit manifest preserves source/used duration and references; HyperFrames consumes this as a handoff, not as its native project format. Use the HyperFrames skill to build the actual project.

`qa.py --expected` accepts duration, dimensions `[width,height]`, fps, audio_required and speech_required. Optional review JSON has file_sha256 and checks keyed by sampled_visual, motion_playback, transcription, direct_listening, final_frame and black_frame_review. Each value has status (pass/failed/unverified/not-applicable) and evidence. Required checks must pass for reviewed-final; otherwise the report says review-incomplete or needs-repair.

A successful decode is not a visual verdict. Inspect the last frame and black-frame candidates, distinguish intentional fades, and listen when audio is required. Never mark unavailable listening or motion review as passed.

Optional `qa.py --model-review-route /absolute/text-route.json --analysis-budget-authorization "actual decision"` requests one paid second opinion and retains its raw response. Reserve this expense externally. It does not automatically promote visual, playback or listening statuses; those require explicit evidence in the review record.
