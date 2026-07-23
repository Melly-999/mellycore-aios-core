# MELLYCORE-OPTION-B-OPENROUTER-DEPLOY-ROADMAP-SYNC-001

**Status:** `DOCS_ONLY_COMMITTED_LOCALLY_NOT_PUSHED`. Documentation and
planning task only. No implementation, no push, no PR, no merge, no deploy.

## Purpose

Update MellyCore AIOS living documentation so the roadmap truthfully reflects
the operator's selected deployment path: **Option B — Static Showcase +
Source Arena + OpenRouter Model/Cost Observatory**. The OpenRouter panel
starts as a static snapshot / no-key / no-backend / no-model-call feature; it
is not implemented as a live OpenRouter integration by this or any prior task.

## Operator decision

`OPTION_B_SELECTED`. First deploy bundles: (1) the cinematic MellyCore
showcase, (2) the Source Arena static renderer slice, (3) an OpenRouter
model/cost observatory as a static snapshot, (4) a model-routing/cost-
awareness story, (5) truthful safety labels. This is not authorization to
call OpenRouter APIs.

## Canonical base

- Repository: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios`.
- Canonical remote: `clean-origin` → `https://github.com/Melly-999/mellycore-aios-core.git`.
- Canonical `main` at task start: `9a5d1bb0bac80b567608f115f10cbd211b327aba`
  (verified via `git fetch clean-origin && git rev-parse clean-origin/main`;
  matched the expected SHA exactly — no drift).
- PR #17: https://github.com/Melly-999/mellycore-aios-core/pull/17, branch
  `feat/mellycore-source-arena-renderer-static-slice-001`, head
  `08642089f9c062928c72d3968fd23843a5e9995d` (verified via
  `git rev-parse HEAD` on that local branch — matched exactly).

## Files inspected

`README.md`, `shared_context/PROJECT_STATE.md`, `shared_context/ROADMAP.md`,
`shared_context/RUN_QUEUE.md`, `shared_context/AGENT_HANDOFF.md`, and (for
context only, via `git show`, no checkout) the task report on the PR #17
branch, `docs/tasks/MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-001.md`.

Inventory result: none of the five living docs contained any prior mention
of "deploy," "showcase," "OpenRouter," or "PR #17" beyond the existing
generic safety-boundary sentences (e.g. "no autonomous ... deployment").
There was no stale "JARVIS showcase only" deploy-target claim to correct —
this is a net-new roadmap addition, not a correction of an existing
overclaim. One genuine staleness was found and reconciled:
`shared_context/AGENT_HANDOFF.md`'s "Next Run (Source Arena Renderer track)"
section still pointed to `MELLYCORE-DOCS-INTEGRATION-REVIEW-001` as the exact
next task, which is superseded now that PR #17 exists; a superseding note was
added above that paragraph (the paragraph itself is preserved as historical
record, consistent with this repository's existing practice).

## Files changed

- `shared_context/ROADMAP.md` — added "Option B Deploy Path — Static AIOS
  Showcase + OpenRouter Observatory" section (PR #17 blocker, 15-task
  sequence, deploy target, OpenRouter Level 1/2/3 gating).
- `shared_context/RUN_QUEUE.md` — added "Immediate Next Task — Option B
  Deploy Path" section naming the XSS triage task as the exact next step,
  with a concise ordered summary of the sequence after it.
- `shared_context/PROJECT_STATE.md` — added "Operator Decision — Option B
  Deploy Path" section recording the decision, OpenRouter not-implemented/
  not-authorized status, and the PR #17 blocker.
- `shared_context/AGENT_HANDOFF.md` — added a new "Latest Task Update"
  section at the top recording this task, the PR #17 blocker, and model
  routing recommendations; added a superseding note to the now-stale "Next
  Run (Source Arena Renderer track)" pointer.
- `docs/tasks/MELLYCORE-OPTION-B-OPENROUTER-DEPLOY-ROADMAP-SYNC-001.md` —
  this report.

`README.md` was inspected and left unchanged — see README decision below.

## README decision

Not edited. `README.md` makes no "first deploy" or near-term deploy-target
claim of any kind — it states only that the current local preview "is not a
public deployment or proof that planned Observatory capabilities exist" and
lists implemented/specified/planned status per area. There was nothing
incomplete or stale in it relative to the Option B decision, so editing it
would have been scope creep beyond Phase 7's trigger condition.

## Option B task sequence (recorded in `ROADMAP.md` and `RUN_QUEUE.md`)

1. `MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-XSS-FINDING-TRIAGE-001`
2. `MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-MERGE-GATE-001`
3. `MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-POST-MERGE-STATE-SYNC-001`
4. `MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-POST-MERGE-STATE-SYNC-PUBLISH-001`
5. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-SPEC-001`
6. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-001`
7. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-VISUAL-ACCEPTANCE-001`
8. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-FINAL-REVIEW-001`
9. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-MERGE-GATE-001`
10. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-POST-MERGE-STATE-SYNC-001`
11. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-POST-MERGE-STATE-SYNC-PUBLISH-001`
12. `MELLYCORE-STATIC-DEPLOYMENT-READINESS-001`
13. `MELLYCORE-STATIC-SHOWCASE-DEPLOYMENT-001`
14. `MELLYCORE-STATIC-SHOWCASE-POST-DEPLOY-VERIFY-001`
15. `MELLYCORE-DEPLOYMENT-STATE-SYNC-001`

None of tasks 2–15 is started, active, or authorized by this documentation
sync alone.

## OpenRouter safety levels

- **Level 1 — Static Snapshot**: allowed for first deploy. Local fixture,
  static prices/capabilities, no API key, no backend, no live fetch, no
  model call.
- **Level 2 — Public Catalog Readiness**: future-gated. Public model catalog
  review, freshness labels, cache strategy, no account usage, no API key in
  frontend, separate approval required.
- **Level 3 — Account Usage / Real Costs**: strictly future-gated. Requires
  backend, secrets management, authentication, usage/cost security review,
  deployment security review, explicit approval.

Levels 2 and 3 are excluded from the first deploy unless separately
authorized.

## Current blocker status

PR #17 remains **open, not merged**, blocked by a failed Sourcery check
flagging a possible XSS/static-analysis finding around `innerHTML` at
`site/js/dashboard.js:509` and `:554-561`. The orbit-clipping defect on that
branch is already fixed. The Source Arena static slice is not canonical
until PR #17 merges. This task did not touch `site/`, did not triage the
finding, and did not merge PR #17.

## Safety boundaries maintained

- PR #17: open, not merged, blocked by the unresolved Sourcery finding.
- Source Arena static slice: not canonical until PR #17 merges.
- OpenRouter Observatory: selected roadmap target, not implemented.
- OpenRouter live API / account usage: not authorized.
- Backend/provider integration: not implemented.
- Deployment / release: not performed.
- Trading execution: prohibited (unrelated to this repository; recorded per
  standing instruction).

## Validators

- `git status --short` — confirmed docs-only change set before commit (see
  Diff Review below).
- `git diff --check` — no whitespace-error findings.
- `python scripts/validate_project_state.py` — attempted; see Final Report
  for the exact result on this machine (Python launcher availability).
- Manual grep scan for overclaim patterns (`OpenRouter.*(live|current|account|usage)`,
  `PR #17.*merged`, `deploy(ed|ment).*(perform|complete)`,
  `backend.*implement`, `api[_ ]?key`) across the five changed files and
  `README.md` — no active overclaim found; all such phrases in the new text
  are framed as explicitly not-yet-true / future-gated.

## No-implementation confirmation

No `site/` file was edited. No JSON fixture, API call, OpenRouter key,
backend/proxy, provider integration, deployment config, or workflow YAML was
added. No dependency was added. No PR was opened or merged. No push occurred.

## Exact next task

`MELLYCORE-OPTION-B-OPENROUTER-DEPLOY-ROADMAP-SYNC-PUBLISH-001` — push this
roadmap-sync commit, open a docs-only PR, review, and merge if clean. After
that, resume `MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-XSS-FINDING-TRIAGE-001`.
