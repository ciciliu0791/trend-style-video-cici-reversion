# Ark CLI execution boundary

## Current workspace route

Follow the current [workspace rules](../../../AGENTS.md): prefer independent Seedance/Seedream MCP for generation and task queries. If unavailable or missing the required capability, disclose that limitation and use supported standalone BytePlus `arkcli` (`@byteplus/ark-cli`), not `ve arkcli` or Creative Kit. Read the current tool/installed skill instructions for the operation, including shared/auth/resources/pricing/gen when using BytePlus CLI; this document does not waive their checks or confirmations.

Verify the actual model, service, region, endpoint, credentials, supported inputs/settings and price. BytePlus and Volcengine credentials/endpoints are not interchangeable. Keep the selected stage/model; Manyue stage defaults come from current workspace rules, not this legacy adapter.

The scripts bundled here have NOT been migrated to BytePlus or MCP. Do not send a BytePlus route to their live `--generate`, discovery, submission or recovery paths, rename the service to bypass validation, or feed native MCP responses into a legacy parser by assumption. Use the current provider workflow with equivalent exact-prompt/reference review, immutable approval, budget and task-recovery records. Local import/edit/QA utilities may be used only with their documented compatible inputs.

Before a paid submission, verify media types, roles, ordering and model-readable transport. Separate file readability, declared inputs, inspectable serialized content and backend evidence. Generic references in a partial preview do not prove media fetching or omission. Obey preview stop requirements and do not create an additional paid task for verification.

## Legacy Volcengine adapter contract

The remainder describes the existing adapter, not the active BytePlus route. Use it only in a separately selected and authorized Volcengine context compatible with workspace rules. Read the installed `volcengine-cli` skill and its current dependencies first.

Every ve process must inherit runtime-resolved `VE_CALLER_NAME` and `VE_SKILL_NAME`; the adapter sets `VE_CALLER_TYPE=ai_agent` and omits wrapper-managed Ark caller/notifier variables. Resolve caller values from the active runtime rather than copying a historical Codex example. No keys are logged or passed as arguments; the adapter selects an explicitly reviewed profile.

The adapter verifies ve >=1.1.11 before child calls. Its supported service is Volcengine Ark. BytePlus profiles/endpoints are not interchangeable; unsupported service selection stops before invocation. No profile/default changes, endpoint creation, custom signing or direct HTTP model fallback are performed.

`doctor.py` is local by default. After official read-only auth/resource discovery, its `--discover` mode captures resource, exact-model capability and pricing JSON. Review the returned region, product, bound model/version, invocability, billing lane, input types and parameter descriptions, then normalize a route snapshot using interfaces.md. Empty/ambiguous metadata is not proof of support. The adapter compares current resource evidence before creation and refuses changed context; refresh the snapshot rather than relaxing it.

Only declared supported settings and input roles are submitted. Local image inline transport must be explicitly selected and supported; video/audio references require the authorized CLI upload route. Neither a local image nor possession of storage credentials implies permission to upload. Do not change permissions or publish references to fix transport errors.

Generation uses `+gen` with explicit modality, reference roles, JSON output and no-open. No `--wait`: task IDs are saved immediately. `gen get` resumes known tasks. Response JSON may contain short-lived signed URLs: keep run directories private, share review files rather than raw response logs. Dry review rendering is offline and does not prove online support.

Analysis uses one `+chat` request and saves the original response before parsing. Invalid JSON is a local repair problem, not permission for repeated paid calls. Separate ASR or SeedAudio operations remain explicitly authorized external steps; import their transcripts/cues. This revision does not silently migrate audio to a model whose generation support has not been verified.

Official references consulted 2026-10-21 (recheck at execution):
- [Ark shared](https://github.com/volcengine/ark-cli/blob/main/skills/arkcli-shared/SKILL.md)
- [Generation workflow](https://github.com/volcengine/ark-cli/blob/main/skills/arkcli-gen/SKILL.md)
- [Generation parameters](https://github.com/volcengine/ark-cli/blob/main/skills/arkcli-gen/references/arkcli-gen.md)
- [Chat parameters](https://github.com/volcengine/ark-cli/blob/main/skills/arkcli-chat/references/arkcli-chat.md)
- [Pricing](https://github.com/volcengine/ark-cli/blob/main/skills/arkcli-pricing/SKILL.md)

No live account or paid generation was used to validate this revision. Offline tests validate local behavior and mocked CLI contracts, not actual service availability.
