# MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-SPEC-001

**Status:** `SPEC_ONLY_LOCAL_COMMIT_DELIVERY`
**Implementation state:** `STATIC_SNAPSHOT_PLANNED`
**Live/API/account state:** `LIVE_API_NOT_AUTHORIZED` ·
`ACCOUNT_USAGE_NOT_AUTHORIZED` · `NO_API_KEYS` · `NO_BACKEND` ·
`NO_MODEL_CALLS` · `NO_DEPLOY`

## 1. Purpose

Create the implementation-ready product/UX/data/routing specification for the
OpenRouter Model/Cost Observatory selected in Option B:

`MellyCore Static AIOS Showcase + Source Arena + OpenRouter Model/Cost Observatory`

The task is documentation/specification only. It does not create the local
fixture or UI slice.

## 2. Repository and preflight

- Repository: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios`
- Canonical remote: `clean-origin` →
  `https://github.com/Melly-999/mellycore-aios-core.git`
- Canonical `clean-origin/main` after fetch:
  `b72bcbdacb61435f7cbc150fffc50ff87d1f3db9`
- Expected SHA: `b72bcbdacb61435f7cbc150fffc50ff87d1f3db9`
- Result: exact match
- Base meaning: normal merge commit for PR #19, publishing the Source Arena
  static-slice post-merge docs sync
- Branch: `docs/mellycore-openrouter-model-observatory-spec-001`
- Worktree at preflight: clean
- Sequencer at preflight: no merge, rebase, cherry-pick, revert, or sequencer
  state active

## 3. Files inspected

- `AGENTS.md`
- `README.md`
- `shared_context/PROJECT_STATE.md`
- `shared_context/AGENT_HANDOFF.md`
- `shared_context/RUN_QUEUE.md`
- `shared_context/SAFETY_CONTRACT.md`
- `shared_context/MODEL_ROUTING.md`
- `shared_context/DESIGN_SYSTEM.md`
- `shared_context/ROADMAP.md`
- `docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md`
- `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md`
- `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md`
- `docs/tasks/MELLYCORE-OPTION-B-OPENROUTER-DEPLOY-ROADMAP-SYNC-001.md`
- `docs/tasks/MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-001.md`
- `docs/tasks/MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-POST-MERGE-STATE-SYNC-001.md`
- Targeted inventory across `README.md`, `shared_context/`, `docs/specs/`,
  and `docs/tasks/` for OpenRouter, Option B, model routing, cost, and named
  model references
- Recent `clean-origin/main` history confirming PR #19 closed the spec
  prerequisite

## 4. Files changed

- `docs/specs/MELLYCORE_OPENROUTER_MODEL_OBSERVATORY_SPEC.md` — new normative
  implementation-ready spec
- `docs/tasks/MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-SPEC-001.md` — this
  durable task report
- `shared_context/PROJECT_STATE.md` — records specified/not-implemented state,
  PR #19 prerequisite closure, safety posture, and next task
- `shared_context/ROADMAP.md` — marks PR #19 and the spec step complete, inserts
  the spec publication gate, and keeps implementation/deployment later
- `shared_context/RUN_QUEUE.md` — moves the exact next task to spec publication
- `shared_context/AGENT_HANDOFF.md` — adds the spec handoff and current task
  pointer

`README.md` was inspected and left unchanged. No `site/`, fixture, workflow,
dependency, backend, provider, account, or deployment file was changed.

## 5. Spec artifact

`docs/specs/MELLYCORE_OPENROUTER_MODEL_OBSERVATORY_SPEC.md`

Product promise:

> A cockpit for choosing the right model at the right cost before an agent run
> begins.

The spec contains all sixteen required sections: purpose, promise, user stories,
information architecture, visual direction, static schema, model lanes, routing
policy, budget estimator, exact safety labels, local interactions, mobile,
accessibility, non-goals, static-slice acceptance criteria, and future gates.

## 6. Key UX decisions

- Premium command cockpit, not a catalogue or pricing table.
- Seven coordinated panels: Model Constellation, Cost Radar, Route Advisor,
  Budget Estimator, Capability Matrix, Fallback Chain, and Safety Boundary
  Strip.
- The first viewport answers lane, model fit, and approximate cost in that
  order.
- The constellation is navigation only; it does not imply availability,
  connectivity, ranking, or live routing.
- Mobile flattens to stacked cards and a lane-grouped list with no hover-only
  behavior or dense mega-table.
- HTML/CSS/DOM is sufficient for the future static slice; WebGL, Three.js, and
  Canvas are excluded.

## 7. Static data schema

The contract includes the required model fields plus `schema_version`,
`cache_read_cost_per_million`, and `currency`. Cost and context values are
nullable; unknown is `null`, never zero or an invented number. Every entry
carries a snapshot date, source note, safety note, and explicit status. The
fixture-level notice must say static snapshot, representative pricing, not live
pricing, and no account backing.

No fixture is created by this task.

## 8. Model-routing policy

The spec defines nine lanes and policy for:

- Fable 5
- Opus-class / Opus 4.x
- GPT-5.6 Sol
- GPT-5.5
- Claude Sonnet
- Tera
- GLM / cheaper models
- Codex

Each entry defines best use, avoid use, cost caution, and fallback. Fable 5 is
recorded as unavailable in the current task context; GPT-5.6 Sol is its
product-architecture fallback, Opus-class is the escalation for ambiguous
safety/future-live boundaries, Claude Sonnet is the docs-consistency route,
and Codex is reserved for separately authorized implementation/validation.
Aliases do not imply current provider availability.

## 9. Budget estimator

The future local estimator accepts selected model, input/output tokens,
optional cache-read tokens, and run type. It returns an approximate estimated
cost or `null`, cost class, a reviewed cheaper compatible alternative, the
premium-worth signal, assumptions, and snapshot date.

Missing input/output price data produces `INSUFFICIENT PRICING DATA`. Missing
cache pricing uses the regular input rate only as a visible conservative
assumption. Every output says:
`Static approximate estimate — not account billing`.

## 10. Safety boundaries

The six exact labels are normative:

- `STATIC SNAPSHOT`
- `NO API KEY`
- `NO MODEL CALLS`
- `NO ACCOUNT USAGE`
- `NOT LIVE PRICING`
- `FUTURE-GATED LIVE CATALOG`

No live OpenRouter catalog, account usage, key, backend, proxy, database,
authentication, model execution, automatic routing/fallback, billing sync,
deployment, or renderer implementation is authorized.

## 11. Future gates

- `MELLYCORE-OPENROUTER-PUBLIC-CATALOG-LIVE-READINESS-001`
- `MELLYCORE-OPENROUTER-PUBLIC-CATALOG-LIVE-SLICE-001`
- `MELLYCORE-OPENROUTER-ACCOUNT-USAGE-SECURITY-REVIEW-001`

All are future-only and require separate authorization. The account-security
gate must precede any account-backed usage/cost work.

## 12. Validation

- `python scripts/validate_project_state.py` — `NOT_RUN`: the `python`
  executable is not available on this Windows host, so PowerShell rejected the
  command before the validator started. This is not recorded as a pass.
- `py -3.9 scripts/validate_project_state.py` — `PASS`:
  `PASS MellyCore project scaffold validation passed`
- `git diff --check` — clean; no whitespace-error or conflict-marker finding.
  Git emitted only existing working-tree LF→CRLF conversion notices.
- Changed-file scope review — `PASS`: exactly the spec, task report, and four
  allowed living docs changed; no `site/`, fixture, workflow, runtime,
  dependency, backend, or deploy path changed.
- Required-section/label/future-gate search — `PASS`: all sixteen numbered
  sections, all six exact safety labels, and all three exact future-gate IDs
  are present.
- Active-overclaim search — `PASS`: matches for OpenRouter implementation,
  live/current pricing, account usage, API key, backend, model calls, deploy,
  and WebGL/Three.js/Canvas are labels, explicit negations, historical context,
  or future-gated requirements. No active implementation, live/current price,
  account-backed, backend, model-call, deployment, or renderer claim remains.

## 13. No-implementation confirmation

No `site/` edit, fixture, OpenRouter request, general network fetch, key,
credential, `.env`, backend, proxy, account usage, model call, provider
integration, dependency, deploy config, workflow YAML, WebGL, Three.js, Canvas,
release, push, PR, or merge is part of this task.

MellyTrade is untouched.

## 14. Exact next task

`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-SPEC-PUBLISH-001`

Publish the single docs commit, open a docs-only PR, review it, merge if clean,
and verify canonical `main`. The static snapshot implementation does not begin
before that publication gate completes.
