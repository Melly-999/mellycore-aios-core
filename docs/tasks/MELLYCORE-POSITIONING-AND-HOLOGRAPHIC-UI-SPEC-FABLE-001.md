# MELLYCORE-POSITIONING-AND-HOLOGRAPHIC-UI-SPEC-FABLE-001

Status: complete (docs-only).
Model: Fable 5. Effort: High.

## Outcome

Produced the product positioning and "Holographic Social Source Cockpit" (HSSC)
visual/UI specification at
`docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md`, covering:

1. Product positioning — canonical public paragraph, the five allowed claims, the
   never-claim list, and the "static and zero-autonomy by design" framing.
2. Visual direction — HSSC-1: three-layer scene model (space / hologram / feed),
   purple-first color tokens (`--holo-*`, cyan demoted), glass/hologram/hull
   materials, the core + provider-orbit + containment-hull signature composition,
   badge system, and an explicit avoid-list (no gamer RGB, no generic dashboard,
   no NASA dominance).
3. Screen concepts — Source Arena mobile, Source Arena desktop, Model Arena,
   Overview hero, Context provenance, Roadmap/status; each with layout,
   real/simulated/planned inventory, required visible labels, dominance and
   reduction rules.
4. CSS-only 3D/holographic spec — perspective scene, orbiting provider ring,
   central core, containment hull, floating/layered cards, shadow/glow tokens,
   frozen `holo-pose` screenshot state, reduced-motion, mobile flatten, forced
   colors, no-JS meaningful fallback, performance guardrails. No Three.js, no
   Canvas, no dependency, no build step.
5. Implementation-ready hand-off task `MELLYCORE-HOLOGRAPHIC-UI-SPEC-001` for
   Sonnet 5: files likely touched, CSS components, additive-only HTML rules,
   near-zero JS budget, accessibility/mobile requirements, browser QA checklist,
   validation commands, safety constraints.
6. README/portfolio guidance — one-liner, README top-section structure,
   screenshot/GIF capture list, what never to claim, and the zero-autonomy
   explanation.
7. Roadmap — next 10 tasks in order with IDs, model routing (Fable 5 vs
   Sonnet 5), effort, type, dependencies, and v0.3.0 membership; v0.3.0 defined
   as the HSSC release (presentational + docs only, no new capability surface).
8. Hard recommendation — do 1–3 (closeout/positioning/honesty) first, review the
   spec before pixels, keep cosmic visuals as stage not star, defer second
   provider and any live-model work past v0.3.0.

## Files

- `docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md` (new)
- `docs/tasks/MELLYCORE-POSITIONING-AND-HOLOGRAPHIC-UI-SPEC-FABLE-001.md` (new)
- `shared_context/AGENT_HANDOFF.md`, `shared_context/RUN_QUEUE.md` (state sync)

## Posture / safety confirmation

Docs-only. No site/dashboard code, CSS, HTML, or JS was changed; no
implementation was performed. No backend, database, API key, secret, provider
runtime, scheduler, workflow YAML, deploy, dependency, canonical `ContextSource`
record, refusal-log, loop-evidence, or MellyTrade change. NASA Images API remains
the only live keyless demo provider; GitHub Repository remains planned/demo; the
spec itself restates and hardens all honesty labels. The spec authorizes nothing;
implementation requires the separately approved `MELLYCORE-HOLOGRAPHIC-UI-SPEC-001`
task after `MELLYCORE-HOLOGRAPHIC-UI-SPEC-REVIEW-001`.

## Next recommended task

`MELLYCORE-PR3-CLOSEOUT-DOCS-001` (record the PR #3 merge at `fff50d2` in shared
state), then `MELLYCORE-POSITIONING-REFRESH-001`, per the spec's Section 7 order.
