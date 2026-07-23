# OpenRouter Model Observatory Visual Polish

**Task:** `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-VISUAL-POLISH-001`
**Status:** `LOCAL_COMMIT_CREATED_NOT_PUSHED`
**Branch:** `feat/mellycore-openrouter-model-observatory-static-snapshot-slice-001`
**Base:** `f1e177e38a26cfc80e047c8481d7932ad4419487`

## Scope

This task closes the visual/product findings from
`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-VISUAL-ACCEPTANCE-001` without changing
the existing fixture, routing policy, estimator logic, provider boundary, or
deployment state.

## Changes

- Replaced the equal-weight model-card catalogue composition with a CSS/DOM
  router core, static orbit rings, routing axis, and eight selectable model
  nodes.
- Rebuilt the 1440×900 command hierarchy so Model Constellation, Route
  Advisor, selected-model state, and the beginning of Budget Estimator are
  visible in the first viewport.
- Moved lane controls into Route Advisor and aligned DOM plus visual mobile
  order to: Route Advisor controls/result, selected model, Budget Estimator,
  Fallback Chain, compact model list, Capability Matrix, Cost Radar.
- Reduced the mobile bottom status bar from 66px to 44px and removed two
  lower-value mobile status items.
- Increased Observatory secondary mono-copy size/contrast.

No JavaScript logic or model data changed.

## Validation

- `node --check site/js/dashboard.js` — pass.
- `py -3.9 scripts/validate_project_state.py` — pass.
- `git diff --check` — pass.
- 1440×900: router-core/orbital metaphor visible; Route Advisor begins at
  approximately y=212; Budget Estimator begins at approximately y=751 and is
  partially visible before the fixed status bar.
- 375px: `body.scrollWidth=360`,
  `documentElement.clientWidth=360`.
- 320px: `body.scrollWidth=305`,
  `documentElement.clientWidth=305`.
- Mobile DOM/article order matches the required decision flow; the complete
  model list follows Fallback Chain.
- Lane filter, model selection, run-type routing, estimator inputs, matrix,
  and fallback updates pass.
- Source Arena: 8 visible source nodes and 4 visible simulated lens cards.
- Model Arena: 4 visible model cards.
- Browser console: 0 errors, 0 warnings.
- Network capture: application requests are localhost-only. Two non-local
  `chrome-extension://` assets are browser-control instrumentation, not
  application requests.

## Safety

The Observatory remains a local static snapshot with representative,
not-live pricing; no account usage, model calls, backend, provider connection,
key, deployment, or automatic routing is introduced. The six exact safety
labels remain present at entry and estimator.

Commit subject:

`fix: polish OpenRouter observatory visual hierarchy`

## Exact Next Task

`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-VISUAL-ACCEPTANCE-002`
