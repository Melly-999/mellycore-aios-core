# MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-REMEDIATION-001

**Status:** One local remediation commit on the existing feature branch,
**not pushed, not merged**.

**Branch:** `feat/mellycore-openrouter-model-observatory-static-snapshot-slice-001`
**Prior HEAD (pre-remediation):** `84faf5b6fafe474684e8320ebe54305a82c9d602`
**Base:** `clean-origin/main` at `f1e177e38a26cfc80e047c8481d7932ad4419487`

## Summary

Fixes the two findings from
`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-REVIEW-001`
(outcome `NEEDS_FIXES_STATIC_SNAPSHOT_SLICE_REVIEW`): a P1 mobile
horizontal-page-scroll defect and a P3 `obs-matrix-body` class/id naming
collision. No new Observatory feature, no API/backend/key work, no
WebGL/Three.js/Canvas, no dependency/workflow edit.

## Files changed

- `site/css/dashboard.css` — mobile-breakpoint width containment fix.
- `site/dashboard.html` — renamed the matrix wrapper `<div>`'s class.
- `docs/tasks/MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-REMEDIATION-001.md`
  (this report).
- `shared_context/PROJECT_STATE.md`, `shared_context/ROADMAP.md`,
  `shared_context/RUN_QUEUE.md`, `shared_context/AGENT_HANDOFF.md` — updated
  to record the remediation commit as branch-only, not pushed.

`site/js/dashboard.js` was **not touched** — the P3 fix only required a class
rename in the HTML; the `<tbody id="obs-matrix-body">` (which JS selects via
`getElementById`) was left unchanged.

## P1 fix summary

**Root cause:** at the `max-width: 760px` mobile breakpoint,
`.obs-main { display: contents }` (added so CSS `order` could reorder cards
directly under the flex `.obs-layout`) removes `.obs-main`'s own box from the
render tree. This breaks the definite-width containing-block chain for every
card beneath it, so *any* descendant with its own intrinsic sizing — the
Model Constellation's `grid-template-columns: repeat(auto-fill, minmax(168px, 1fr))`,
the Route Advisor's nowrap run-type button row, the Capability Matrix's
nowrap `<table>` — could inflate the *card's own rendered width* past the
viewport rather than scrolling within itself. Confirmed by direct
measurement: `.obs-constellation-card` rendered at `1176.9px` and
`.obs-advisor-card` at `936.9px` in a 375px viewport, forcing
`document.body.scrollWidth` up to `1189px`.

**Fix:** in the same `@media (max-width: 760px)` block, every direct
Observatory card (`.obs-constellation-card`, `.obs-advisor-card`,
`.obs-selected-card`, `.obs-estimator-card`, `.obs-fallback-card`,
`.obs-matrix-card`, `.obs-radar-card`) is now pinned to
`width: 100%; max-width: 100%; min-width: 0`, so a card's own box can never
grow past the flex container's width regardless of descendant content —
descendants can only scroll internally (the matrix table already had its own
`overflow-x: auto` wrapper; the lane-filter chip row already had
`overflow-x: auto` from the pre-existing `.task-selector` mobile rule). The
Model Constellation grid was additionally given an explicit column count
(`repeat(2, minmax(0, 1fr))` at ≤760px, `minmax(0, 1fr)` — i.e. one column —
at ≤420px) instead of `auto-fill`, removing the ambiguous intrinsic-sizing
computation at its source as well.

This was applied as one general rule across all seven cards rather than
patched card-by-card, because the first narrow attempt (fixing only
`.obs-constellation-card`/`.obs-model-grid`) left `.obs-advisor-card` and
`.obs-matrix-card` still overflowing — the same `display: contents` root
cause affects any card with wide descendant content, not just the one with a
CSS Grid.

## P3 fix summary

Renamed `<div class="dash-details-body obs-matrix-body">` to
`<div class="dash-details-body obs-matrix-body-wrap">` in
`site/dashboard.html`. The `<tbody id="obs-matrix-body">` is unchanged, and
so is `document.getElementById("obs-matrix-body")` in `dashboard.js` — no
class selector anywhere in the CSS ever referenced `.obs-matrix-body`, so
nothing else needed updating. Confirmed by grepping all three files for
`obs-matrix-body` before and after the change.

## Mobile overflow measurements

Measured live in-browser (note: `window.innerWidth`/`visualViewport.width`
are unreliable in this preview harness — reports ~949px regardless of the
requested viewport — so `document.documentElement.clientWidth`, which does
track the requested width correctly and against which the `max-width`
media queries correctly evaluate, is the ground truth used below):

| Viewport | `clientWidth` | `body.scrollWidth` (before fix) | `body.scrollWidth` (after fix) |
| --- | --- | --- | --- |
| 375px | 375 | 1189 | **375** |
| 320px | 320 | not separately measured pre-fix | **320** |

`document.body.scrollWidth === document.documentElement.clientWidth` at both
widths post-fix — zero horizontal page overflow, satisfying the required
result exactly.

## Interaction checks

Re-verified live in-browser after the fix, at mobile width:

- Lane filter narrows the Model Constellation correctly (e.g., "Cheap
  Worker" → shows only GLM / cheap model).
- Model selection (Codex) updates Selected Model detail and Capability
  Matrix together.
- Run-type selector (Coding / Refactor) updates Route Advisor's recommended
  lane/model/fallback correctly (Codex, fallback GPT-5.6 Sol).
- Budget Estimator updates on input (still correctly shows `INSUFFICIENT
  PRICING DATA`, since fixture pricing remains `null` by design).

At desktop width (1400px): `.obs-layout` remains `display: grid`, the Model
Constellation grid remains multi-column (~194px × 5 columns observed), and no
horizontal overflow — the mobile-only fix does not affect desktop layout.

## Source Arena regression check

Re-verified post-fix: 8 local records, holographic stage renders, 4 simulated
model-lens cards populate — unaffected, as expected (no Source Arena file was
touched).

## Validators

```
node --check site/js/dashboard.js         → PASS
py -3.9 scripts/validate_project_state.py → PASS
git diff --check                          → clean
```

Browser checks: no console errors at any tested viewport; `read_network_requests`
showed only local `localhost:8791` GETs (the pre-existing `shared_context/**`
and `site/data/**` reads) — zero external requests.

## Forbidden-search classification

Searched the full remediation diff (`site/css/dashboard.css`,
`site/dashboard.html`) for `openrouter.ai`, `api.openrouter`, `fetch(`,
`apiKey`, `.env`, `process.env`, `THREE`, `WebGL`, `<canvas`,
`images-api.nasa.gov`, and live/current/account-pricing language: **zero
hits**. The diff is CSS selectors/values and one HTML class-attribute rename
only.

## Commit / worktree state

One new local commit on the existing feature branch:

```
fix: contain OpenRouter observatory mobile layout
```

Not pushed. Not merged. No PR opened. Worktree clean after commit.

## Safety confirmation

- OpenRouter Observatory: static snapshot only, still not merged, not
  deployed.
- No live API, account usage, backend, or provider connection introduced.
- No API key, `.env`, credential, or secret added anywhere.
- No WebGL, Three.js, or Canvas renderer used.
- No workflow, dependency, or deploy-config file touched.
- No MellyTrade file touched.
- Source Arena regression-checked and confirmed intact.
- No new Observatory feature or product-scope expansion — this is a
  layout-containment bug fix only.

## Exact next task

`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-REVIEW-002`
