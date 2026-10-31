# Shared Analysis and Adaptation Choice

Use one source analysis for both modes. Read the shared analysis contract linked directly from the entry skill. Do not run a second analysis just because the user changes modes. Keep the evidence, selected attraction mechanisms and mode decision in the existing review entry.

## Analyze First, Then Resolve the Direction

Show a compact source-informed summary before developing the adapted storyline:

- Hook: first attention cue, sustained interest and payoff, with the actual action/image/sound carrying each.
- Audience experience: intended or inferred feeling, sensory appeal, performance and relationship to the viewer.
- Style: camera, rhythm, palette, light, materials, costume and sound, explaining their function.
- Main attraction points: a few defining mechanisms, supported by timestamps and separated from popularity hypotheses.
- Preservation proposal: what should survive in either mode, what may change, what must not be copied, and evidence gaps.

Do not claim that every style dimension must remain identical. Preserve the selected relationships and audience effect; explain material departures. A prop, color or character substitution alone is not a mechanism transfer.

If the user has not already chosen, ask one concrete question using the available interactive question tool, or the same choices in chat:

> 这次希望采用哪种改编方式？
>
> - **复刻**：保留原片主要段落、镜头功能、动作调度和节奏，替换主体与具体内容，同时保留已选的 Hook、观感和风格。
> - **改写故事**：保留已选的 Hook、观感、风格和主要吸引点，重新设计故事、动作、镜头顺序与结尾。

Recommend one option only when the brief supports it, with a brief reason. Do not silently choose based on the invoked skill name. An explicit request such as "拍同款，保留原来的展开" or "换一个故事但保留这种感觉" already answers this question: restate the choice and proceed without a redundant approval. "Use Viral/Trend" alone does not settle it.

For analysis-only requests, deliver the analysis without forcing a production choice. For an ambiguous production request, keep shared analysis and asset inventory moving, but wait for the answer before committing a mode-specific story or commissioning dependent media. Choosing a mode does not authorize production, uploads, extra calls or spending.

## Mode Contract

| Decision | 复刻 / structure-remake | 改写故事 / story-rewrite |
|---|---|---|
| Common invariants | Selected Hook, audience experience, style relationships and attraction mechanisms | The same selected invariants |
| Story and shots | Preserve the main source progression, shot functions, staging and approximate rhythm; map source beats to new beats | Write a new premise and causal/discovery sequence; source plot, shot order/count, runtime and ending may change |
| Changes | Explain changed actions, necessary omissions and timing departures in KEPT/CHANGED | Explain how new actions/views carry each retained mechanism; do not grade against discarded source cuts |
| Timing | Default to functional/rhythmic fidelity, not identical timestamps | Time the new story according to its selected audience experience |
| Output check | Does the source progression still work with the new subject, and do its selected mechanisms register? | Does the new story stand on its own while preserving the selected appeal, rather than only a similar palette? |

Neither mode licenses copying source identity, logos, dialogue, music or footage. Use original or authorized replacements. Neither requires a product, CTA, twist, exaggerated action or a fixed runtime.

If the user explicitly requires matching cut points, treat measured close timing as a sub-option of 复刻, not a third compulsory question. Require reviewed source cuts; if they cannot be measured, explain the limit and obtain a choice between supplying evidence and functional/rhythmic fidelity. Never promise exact timing from samples.

If required reference coverage is missing, name the missing asset and affected beat and ask for it. Do not silently remove required content or treat no response as inability to supply it.

## One Entry, One Record

For new projects use `trend-style-video` as the workflow owner for either mode and its existing production/review path. The workspace Viral skill is a compatibility entry and a source of optional structure-remake methods, not a second end-to-end pipeline. Do not invoke the global Viral skill or inherit its ad-only defaults.

On existing projects preserve their owner, current cut, run paths, hashes, selected assets, pending IDs and approvals. Add the shared analysis and choice to the current review/decision record; do not migrate project history merely to adopt this entry.

Record `adaptation-choice` in the existing decision notes with the user's words, chosen mode, selected invariants, allowed changes and timing intent. This is a stable decision label, not a new required machine-schema field. Keep pending choices pending. On a user-requested mode change, retain valid source evidence and invalidate only affected proposed story/prompt work; do not transfer old approval to changed requests.

Legacy adapter compatibility:

- `mode: ad|creative` describes content, not the user's remake/rewrite choice.
- `fidelity: adaptation|close-timing` describes timing constraints. Do not put `structure-remake` or `story-rewrite` into those enums.
- Keep the choice in the review/decision notes and existing storyboard `concept` / `change_summary` / shot `reason` fields when using that schema.
- Use the legacy structure-storyboard method for 复刻 only when needed and compatible. For 改写故事 use the Trend creative-development path; do not pass it through a prompt that defaults to preserving source shot functions.
- This instruction merge does not upgrade the legacy Volcengine-only execution adapter or authorize it for BytePlus.

Follow current workspace budget and authorization rules for production. Preserve exact prompt disclosure, selected-image dependencies, scope confirmation and task recovery. The mode question is a creative direction decision, not an additional routine spending gate.
