# Research: a director-led film project skill

Research date: 2026-10-24. Status: research basis for Cinematic_Project_Skills_Cici. The user subsequently selected DirectorSKILL as a structural reference for directing, with original implementation and standardized essential project steps. No production-quality claim has been established. Repository instructions were inspected as evidence, not activated as skills. No third-party code was executed or installed.

## Initial comparison recommendation (superseded by the user’s structural choice)

Use `62656456/ai-film-skills`'s `director-agent` as the leading candidate for creative reasoning. Evaluate `wuwangzhang1216/DirectorSKILL` for its practical blocking and director-book structure, and `kangarooking/director-skills`'s performance module for specific acting problems. Keep project tracking subordinate to directing decisions. This is a judgment based on source inspection, not an end-to-end quality benchmark.

## GitHub candidates inspected

### 1. Open Film Skills: director-agent

[Entrypoint](https://github.com/62656456/ai-film-skills/blob/main/skills/director-agent/SKILL.md) · [Director thinking](https://github.com/62656456/ai-film-skills/blob/main/skills/director-agent/references/director-thinking-spine.md) · [Project workbench](https://github.com/62656456/ai-film-skills/blob/main/skills/director-agent/references/director-workbench-protocol.md)

Closest fit for the requested director perspective. It addresses audience alignment and knowledge, causal story development, playable behavior, spatial relationships, image concepts, sound, time, and editorial choices. It preserves selected decisions when handing off to storyboards. The workbench adds project continuity without requiring its full machinery for a local rewrite.

Useful distinction: first decide what viewers experience, then select how to stage and photograph it. This is more valuable than adding camera terminology to a generic shot list.

Caution: the larger collection is extensive. Its separate storyboard skill imposes additional style approval and fixed prompt-format conventions; these need reconciliation with current preferences rather than blanket adoption. Detailed records do not establish artistic quality.

Verified GitHub metadata: Apache-2.0; last push 2026-10-18. Inspected director entrypoint blob: `1c17278089500960509f20dc1af3cbc5e30d35c3`.

### 2. Cinematic Director Skill

[Entrypoint](https://github.com/wuwangzhang1216/DirectorSKILL/blob/main/SKILL.md) · [Blocking and staging](https://github.com/wuwangzhang1216/DirectorSKILL/blob/main/references/blocking-and-staging.md)

Strong practical bridge from interpretation to a director's book, blocking, coverage, keyframes, sound, edit plans, and repair notes. Its blocking examples demonstrate how spatial relationships change the meaning of the same event. Useful for making directing decisions executable.

Caution: some heuristics are framed as universal rules: narrow clip-duration defaults, a single style lens, and mandatory environmental motion in its blocking-to-prompt procedure. Adopt these only where justified. Camera and performance complexity must follow the scene and verified model capability.

Verified GitHub metadata: MIT; last push 2026-08-31. Entrypoint declares version 2.1.0. This inspection does not validate its model reliability claims.

### 3. Emotion Performance Director

[Module](https://github.com/kangarooking/director-skills/blob/main/emotion-performance-director/SKILL.md)

A useful narrow specialist: translates subtext into selected gaze, breath, facial, body, and vocal behavior before, during, and after a line. It preserves dialogue and avoids adding gestures merely to fill a checklist.

Caution: its focus is naturalistic human micro-performance, not complete story development or project direction. Apply cautiously to stylized work and animal characters. Model execution of subtle gestures still needs testing.

Verified repository metadata: MIT; last push 2026-10-20.

## Other leads

[StoryMind](https://github.com/LinHao-city/StoryMind) and [OpenDirector](https://github.com/seme-org/open-director) advertise broader generation applications. They may help study execution architecture, but were not source-audited here and are less direct answers to a reusable directing skill. [This curated list](https://github.com/PAMPAS-Lab/awesome-ai-short-drama) is useful for discovery; its claims and star counts are not independent quality evidence.

The generic [film-director-producer persona](https://github.com/theneoai/awesome-skills/blob/main/skills/persona/media/film-director-producer/SKILL.md) is a lower-priority candidate: its entrypoint relies on invented professional credentials and the displayed frontmatter reports a YAML error. Prefer actionable craft guidance over role-play authority.

## Professional practice cross-check

- ScreenSkills describes the editor working with the director from pre-production and assembling footage during shooting. Implication: plan for editing and inspect sequences early. [Editor profile](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/post-production/editor-film-and-tv-drama/)
- Its script-supervisor specification connects timing, story breakdown, coverage, physical/emotional continuity, and editorial handoff. Implication: track the changing story state as well as visual identity. [Role specification](https://www.screenskills.com/media/7610/final-jd-script-supervisor-110523.pdf)
- Sundance's directing course includes scene analysis, beat shifts, rehearsal, blocking, and a production binder. Implication: direct behavior and spatial action before reducing a scene to prompts. [Directing Actors](https://collab.sundance.org/catalog/Directing-Actors-Self-paced/June-2026)
- ScreenSkills places dialogue, effects, Foley, ambience and the final mix within coordinated sound supervision. Implication: sound needs its own creative intent and workstream. [Sound editor profile](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/post-production/supervising-sound-editor/)
- Film Independent's line-producer discussion connects the script breakdown to schedule and budget. Implication: resources should follow the intended film and concrete requirements. [Budgeting discussion](https://www.filmindependent.org/blog/know-crew-line-producer-angela-sostres-tips-building-better-budget/)

These sources support professional responsibilities. They do not validate any particular AI skill or guarantee improved films.

## Proposed next evaluation

Use one identical short dialogue scene, with locked story facts and no generation, to compare the two leading candidates. Inspect audience viewpoint/information order, playable objectives, blocking, image choices, sound, motivated cuts, and preservation of the story. Then build the final skill around the strongest demonstrated decisions, retaining the current project's model and permission rules. A text evaluation is preliminary; final-film improvement requires actual footage and cut review.

If adopting upstream files, pin the source revision and preserve required license/notices. No upstream implementation files have been copied into this draft.

## Adopted design and attribution

The user selected [DirectorSKILL](https://github.com/wuwangzhang1216/DirectorSKILL) as a structural reference on 2026-10-24. Inspected tree revision: `c65ae0d14457053efb1e354c7e7f7e120d97fad1`. Its separation of entrypoint, on-demand directing references, and practical templates informs this package. Its interpretation → beats → treatment → blocking/coverage → production/post structure informs the directing organization.

Cici adds original stage contracts (entry, responsibility, output, exit evidence, handoff), baseline/version propagation, and differentiated readiness/authorization/acceptance. The directing workbook and templates are newly written. Upstream prose, director-style modules, prompt lexicons, scripts, and model adapters are not copied. Fixed shot durations, mandatory environmental movement, and a required named-director lens are not adopted. The research recommendations above record the comparison, not a mandate to install other packages.
