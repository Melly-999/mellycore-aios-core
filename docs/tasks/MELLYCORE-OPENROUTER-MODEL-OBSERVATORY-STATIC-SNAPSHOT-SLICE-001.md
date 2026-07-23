# MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-001

**Status:** Implemented on a feature branch, one local commit, **not pushed,
not merged**.

**Branch:** `feat/mellycore-openrouter-model-observatory-static-snapshot-slice-001`
**Base:** `clean-origin/main` at `f1e177e38a26cfc80e047c8481d7932ad4419487`
(the PR #20 spec-publish merge commit).
**Canonical spec:** `docs/specs/MELLYCORE_OPENROUTER_MODEL_OBSERVATORY_SPEC.md`

## Summary

Implements the first static-snapshot slice of the OpenRouter Model/Cost
Observatory described by the canonical spec: a new "Observatory" tab on the
Live Cockpit V2 dashboard presenting Model Constellation, Cost Radar, Route
Advisor, Budget Estimator, Capability Matrix, Fallback Chain, and a
persistent Safety Boundary Strip — all driven by a local, static JS fixture
with zero network calls, API keys, or provider connections.

## Files changed

- `site/dashboard.html` — added the Observatory nav tab and panel markup.
- `site/js/dashboard.js` — added `OBS_*` constants (safety labels, lanes, run
  types, capability fields, the eight-model fixture, lane→model routing
  table) and the Observatory render/interaction functions; wired into `boot()`.
- `site/css/dashboard.css` — added Observatory-specific styling reusing
  existing tokens and component classes (`.dash-surface`, `.task-button`,
  `.metric-strip`, `.context-rule-list`), plus responsive/reduced-motion/
  forced-colors rules.
- `docs/tasks/MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-001.md`
  (this report).
- `shared_context/PROJECT_STATE.md`, `shared_context/ROADMAP.md`,
  `shared_context/RUN_QUEUE.md`, `shared_context/AGENT_HANDOFF.md` — living
  docs updated to record this slice as branch-only, not merged.

No other file was touched. No `.env`, credential, workflow, dependency, or
deploy-config file was created or modified.

## Static data summary

Eight fixture records in `OBS_MODEL_FIXTURE.models` (`site/js/dashboard.js`):
Fable 5, Opus-class, GPT-5.6 Sol, GPT-5.5, Claude Sonnet, Tera, GLM / cheap
model, Codex. Each conforms to spec §6's schema (`model_id`, `display_name`,
`provider`, `routing_lane`, `cost_class`, `input_cost_per_million`,
`output_cost_per_million`, `cache_read_cost_per_million`, `currency`,
`context_window`, `capabilities`, `best_for`, `avoid_for`, `fallbacks`,
`status`, `snapshot_date`, `source_note`, `safety_note`).

**Deliberate design choice:** every `input_cost_per_million`,
`output_cost_per_million`, and `context_window` field is `null`. No 2026
OpenRouter pricing or context-window figure has a reviewed source in this
fixture, so nothing is fabricated — per spec §6 ("Unknown is `null`, never
zero") and the acceptance criterion "Uses `null`/unknown states instead of
invented prices ... or availability." `cost_class` and routing-lane
qualitative assignments are carried over from the already-reviewed routing
table in the canonical spec §8, not invented. Statuses used:
`UNAVAILABLE` (Fable 5, per spec §3/§8), `PLANNED_ALIAS` (Opus-class,
GPT-5.6 Sol, Tera, GLM — all named as aliases in the spec), and `UNKNOWN`
(GPT-5.5, Claude Sonnet, Codex — no reviewed identifier/price on file; the
spec explicitly forbids a "generic Codex price assumption").

Fixture-level `example_notice` states it is a static snapshot of
representative example entries only, not live pricing, not account-backed.

## Safety labels

The exact six labels from spec §10 render at both the Observatory entry and
the Budget Estimator, verified in-browser:
`STATIC SNAPSHOT` · `NO API KEY` · `NO MODEL CALLS` · `NO ACCOUNT USAGE` ·
`NOT LIVE PRICING` · `FUTURE-GATED LIVE CATALOG`.

## Interaction checks (browser-verified)

- Lane filter chips narrow the Model Constellation to one lane (verified:
  "Cheap Worker" → shows only GLM / cheap model).
- Model selection updates Cost Radar, Selected Model detail, Fallback Chain,
  Route Advisor, Budget Estimator, and Capability Matrix together (a real bug
  was found and fixed here — `renderObsMatrix()` was initially missing from
  `selectObsModel()`; confirmed fixed by re-testing).
- Run-type selection updates Route Advisor's recommended lane/model/fallback
  and the estimator's premium signal (verified: selecting
  "Security/Architecture Review" recommends Opus-class with Claude Sonnet as
  fallback).
- Budget Estimator: verified `INSUFFICIENT PRICING DATA` renders for all
  fixture models (expected, since all rates are `null`). The formula itself
  (spec §9.2, including the `CACHE_RATE_UNKNOWN_ASSUMED_INPUT_RATE` branch)
  was independently cross-checked against a synthetic priced model and
  produces the mathematically correct result.
- Model cards carry an explicit `aria-label` stating model, lane, cost
  class, status, and selected state (added during verification once the
  default browser accessible-name rendering in this harness was found to
  need an explicit label for reliable exposure).
- Each model button uses `aria-pressed`; lane and run-type filters are real
  `<button>` elements with keyboard-reachable click handlers (no hover-only
  interaction).

## Mobile check

At the `max-width: 760px` breakpoint, `.obs-layout` switches to
`display: flex; flex-direction: column` and CSS `order` values place: Safety
Boundary Strip (outside the flex container, always first) → lane filter →
Model Constellation → Route Advisor → Selected Model → Budget Estimator →
Fallback Chain → Capability Matrix → Cost Radar. Confirmed via
`getComputedStyle` at the breakpoint (`display: flex`, `flexDirection:
column`, and the expected `order` integers on each card). The Capability
Matrix is a `<details>`/`<table>` (semantic table-equivalent, collapsible).
No horizontal body overflow was observed.

## Source Arena regression check

Re-verified after implementing the Observatory tab: Source Arena still lists
8 local records, the holographic stage renders, and the 4 simulated
model-lens cards populate correctly. No change was made to Source Arena code
paths.

## Validator results

```
node --check site/js/dashboard.js         → PASS
py -3.9 scripts/validate_project_state.py → PASS (MellyCore project scaffold validation passed)
git diff --check                          → clean
```

Browser checks: no console errors; `read_network_requests` showed only the
pre-existing local `shared_context/**` and `site/data/**` GETs — zero
requests to any external host, zero requests containing `openrouter` or
`nasa`.

## Forbidden-search results

Searched all three changed application files for `openrouter.ai`,
`api.openrouter`, `fetch(`, `apiKey`, `.env`, `WebGL`, `THREE.`, `<canvas`,
`images-api.nasa.gov`. Two pre-existing, unrelated hits were found and
classified safe:

- `site/js/dashboard.js` — a pre-existing `ARCHIVE_RECORDS` copy line
  mentioning "WebGL-enhanced renderer" (decision-level text describing an
  already-accepted, not-yet-implemented ADR; not new code from this task).
- `site/js/dashboard.js` — the pre-existing `getText`/`getJSON` helpers'
  `fetch(path, options)` calls, used only for local `shared_context/**` and
  `site/data/**` reads that predate this task; the Observatory code added
  here calls neither.

No new hit was introduced by this slice.

## Commit / worktree state

One local commit on the feature branch:

```
feat: add OpenRouter model observatory snapshot
```

Not pushed. Not merged. No PR opened. Worktree clean after commit.

## Safety confirmation

- OpenRouter Observatory: static snapshot slice implemented, **not merged,
  not deployed**.
- Live API / account usage / backend / provider connection: not implemented,
  not authorized.
- No API key, `.env`, credential, or secret was added anywhere.
- No WebGL, Three.js, or Canvas renderer was used.
- No workflow, dependency, or deploy-config file was touched.
- No MellyTrade file was touched.
- Source Arena regression-checked and confirmed intact.

## Exact next task

`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-REVIEW-001`
