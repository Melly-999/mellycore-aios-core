# MELLYCORE-VERCEL-STATIC-SHOWCASE-ROOT-PATH-REMEDIATION-001

## Outcome

`SUCCESS_VERCEL_STATIC_ROOT_PATH_REMEDIATION_COMMIT_CREATED_NOT_PUSHED`

## Baseline

- Repository: `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`
- Canonical base: `59b1408d5966a57ebd8e8636fd815198b7227f8f`
- Branch: `fix/mellycore-vercel-static-root-path-remediation-001`
- Existing Vercel URL: `https://mellycore-aios-core.vercel.app`
- Vercel root: `site/`

## Root Cause

`site/js/dashboard.js` booted all dashboard data panels through one mandatory
`Promise.all`. Repository-only Markdown, loop registry/state, provenance index,
and evidence paths were fetched from `/shared_context/*`. Those files are
deliberately outside the published `site/` root, so the first 404 rejected the
whole boot promise and was logged with `console.error`.

Source Arena, Model Arena, and the OpenRouter Observatory use local static
fixtures and did not require those repository-only files.

## Remediation

- Keep `data/dashboard_snapshot.json` and `data/context_audit_snapshot.json`
  required, using page-relative paths that work for both `/dashboard.html` and
  `/site/dashboard.html`.
- Treat repository-only Markdown, registry, state, provenance, and evidence
  reads as optional on 404.
- Use the full repository-backed rendering path when all repository context is
  available.
- Otherwise render explicit static/degraded copy for Overview, Context, Loops,
  Evidence, and Roadmap without publishing internal context or claiming live
  data.
- Preserve the Source Arena, Model Arena, Observatory, and all existing safety
  labels and local fixtures unchanged.

No internal-labeled `shared_context` file was copied into `site/`.

## Validation

- `node --check site/js/dashboard.js` — PASS
- `py -3.9 scripts/validate_project_state.py` — PASS
- `git diff --check` — PASS
- `py -3.9 -B -m unittest discover` — PASS, 245 tests
- `site/`-root browser smoke — PASS:
  - no console errors or warnings;
  - only `127.0.0.1` requests;
  - Source Arena, Model Arena, and Observatory available;
  - safety labels visible;
  - 320px widths `305/305`;
  - 375px widths `360/360`.
- repository-root browser smoke — PASS; full repository context path remained
  available with no console errors or warnings.

## Forbidden-Search Classification

Diff hits for backend/provider/live-pricing/account-usage/model-call terms are
negative safety statements or task-report search terminology. There are no
executable OpenRouter, NASA, provider, backend, broker, order, or model-call
additions and no credential/environment access.

## Safety and Release State

- Static-only showcase preserved.
- Representative/not-live pricing preserved.
- No account billing, API key, backend, provider connection, or model call.
- No workflow, dependency, Vercel configuration, or GitHub Pages change.
- No push, PR, merge, deploy, or redeploy.
- The existing Vercel deployment remains unaccepted until a later reviewed
  remediation is published and post-deploy smoke passes.

## Exact Next Task

`MELLYCORE-VERCEL-STATIC-SHOWCASE-ROOT-PATH-REMEDIATION-REVIEW-001`
