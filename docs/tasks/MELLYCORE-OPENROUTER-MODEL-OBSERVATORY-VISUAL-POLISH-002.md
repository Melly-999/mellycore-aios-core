# OpenRouter Model Observatory Visual Polish 002

**Task:** `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-VISUAL-POLISH-002`
**Status:** `LOCAL_COMMIT_CREATED_NOT_PUSHED`
**Branch:** `feat/mellycore-openrouter-model-observatory-static-snapshot-slice-001`
**Base:** `f1e177e38a26cfc80e047c8481d7932ad4419487`

## Scope

This task closes the single remaining P2 from
`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-VISUAL-ACCEPTANCE-002`: the Budget
Estimator began below the fixed footer in the first 1440×900 viewport.

## Change

One desktop-only CSS media rule reduces Observatory panel top padding,
section-head spacing, and the gap below the top safety strip. No DOM,
JavaScript, fixture, interaction, mobile-order, or safety-copy change was
needed.

At 1440×900:

- Observatory grid top: approximately y=312 before, y=241 after.
- Route Advisor: y=241–764 after.
- Budget Estimator: approximately y=851 before, y=780 after.
- Budget Estimator header: y=781–839 after.
- Fixed status bar: y=847–900.

The complete Budget Estimator header, including `Static approximate · not
account billing`, is visible above the fixed footer.

## Validation

- `node --check site/js/dashboard.js` — pass.
- `py -3.9 scripts/validate_project_state.py` — pass.
- `git diff --check` — pass.
- 375px: body/document width `360/360`; footer remains 45px.
- 320px: body/document width `305/305`; footer remains 45px.
- Mobile order remains Route Advisor, selected model, Budget Estimator,
  Fallback Chain, Model Constellation, Capability Matrix, Cost Radar.
- Lane filtering, model selection, run-type routing, estimator inputs,
  capability matrix, and fallback chain pass.
- Source Arena: 8 nodes, 8 queue records, 4 simulated lens cards.
- Model Arena: 4 simulated lens cards.
- Browser console: 0 errors, 0 warnings.
- Network capture: all application requests are localhost-only.

## Safety

The Observatory remains a local static snapshot with representative, not-live
pricing; no account usage, API key, model call, backend, provider connection,
deployment, or automatic routing was introduced. All safety labels are
unchanged.

Commit subject:

`fix: expose OpenRouter observatory budget state`

## Exact Next Task

`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-VISUAL-ACCEPTANCE-003`
