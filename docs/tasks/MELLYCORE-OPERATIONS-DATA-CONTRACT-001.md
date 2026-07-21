# MELLYCORE-OPERATIONS-DATA-CONTRACT-001

Status: complete locally (documentation/spec/fixture-and-schema scope only,
one local commit, not pushed, not merged).

## Task Purpose

Translate the logical contracts approved in
`docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` (integrated
into canonical `main` via PR #7) into a concrete, eleven-entity, dashboard-facing
Operations Data Contract — `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md` —
covering `operation_run`, `task_record`, `agent_identity`,
`model_provider_usage`, `token_cost_record`, `validation_result`,
`artifact_record`, `environment_capability_snapshot`, `approval_gate`,
`safety_status`, and `recommendation_ledger_entry`, plus companion JSON
Schema and example fixture files.

## Authorization Boundary

The operator authorized: read-only local and `clean-origin` inspection;
creation of one dedicated local branch from the pinned canonical-`main` SHA;
creation of documentation/spec/schema/example fixtures and this task report;
minimum-necessary shared-context updates; running existing validators; and at
most one local commit. No backend/runtime, provider integration, frontend
scaffold, NASA runtime retirement, Three.js vendoring, deployment, trading
UX, secrets/`.env`, workflow YAML, push, merge, or retired-`origin` contact.

## Canonical Base

- Canonical remote: `clean-origin` → `Melly-999/mellycore-aios-core`.
- Canonical `main`: `edf56ea4cace434c3e4cc52dcfe17984ba9f76ea` — confirmed to
  include the renderer P2 closeout merge (PR #12,
  `MELLYCORE-P2-CLOSEOUT-MERGE-001`) via
  `git merge-base --is-ancestor edf56ea... clean-origin/main`.
- Working branch: `docs/mellycore-operations-data-contract-001-v2`, created
  directly from `clean-origin/main` at `edf56ea4cace434c3e4cc52dcfe17984ba9f76ea`.
- Retired remote `origin` was never contacted.

## Prior-Branch Discovery and Reconciliation Decision

A local branch named `docs/mellycore-operations-data-contract-001` already
existed, dated 2026-07-19, authored by the operator, never pushed to
`clean-origin`. It contains a differently-scoped, thorough prior attempt
(AI Estate Inventory, Unified Run Ledger, Skill Gap Candidate, Memory
Freshness, Recommendation Ledger, Approval Record, and a ten-value
Truthful-State Labels reference fixture set) based on a `main` commit
(`06a7a42`) roughly ten merged pull requests behind current canonical `main`
— it predates the entire Source Arena renderer P2 remediation/closeout chain.

Rebasing or merging that branch onto current `main` would require conflict
resolution in `shared_context/PROJECT_STATE.md`, `RUN_QUEUE.md`,
`ROADMAP.md`, and `AGENT_HANDOFF.md` (all substantially rewritten since),
which this task's scope does not authorize. Per the task's stop condition
("existing ODC branch contains conflicting work that cannot be safely
reconciled"), that branch was **not** checked out, rebased, merged, or
modified. Instead:

- A **new** branch, `docs/mellycore-operations-data-contract-001-v2`, was
  created directly from current canonical `main`, since the requested branch
  name was already in local use by the operator's own unpushed work.
- The new spec (this task) was authored fresh against current `main` and the
  operator's current eleven-entity specification, cross-referencing the
  already-canonical `MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` rather
  than the older branch's artifact set.
- Reconciliation between the two branches (discard / fold-compatible-parts /
  archive) is explicitly deferred to a future, separately authorized task —
  see the spec document, Section 6. Neither branch was deleted, pushed, or
  merged.

## Sources Inspected

`docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` (full read:
§§1, 5, 6, 7, 8, 9, 16, 17); `shared_context/PROJECT_STATE.md`,
`ROADMAP.md`, `RUN_QUEUE.md`, `AGENT_HANDOFF.md`, `SAFETY_CONTRACT.md`;
`shared_context/loops/RUN_LEDGER_SCHEMA.json` (field/enum reference);
`scripts/` directory listing (`context_gate`, `loop_ops`,
`validate_project_state.py`); the prior branch's
`docs/tasks/MELLYCORE-OPERATIONS-DATA-CONTRACT-001.md` and
`shared_context/operations/*` (read via `git show`, not checked out).

## Source-of-Truth Hierarchy Applied

1. `MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` §4–§9 and its
   ten-value truthful-state glossary (§1.9) remain authoritative; this task's
   spec cross-references them and does not redefine them.
2. `shared_context/loops/RUN_LEDGER_SCHEMA.json`'s `outcome` enum and
   measured/total token semantics remain authoritative; `operation_run` and
   `token_cost_record` reuse them exactly.
3. `shared_context/SAFETY_CONTRACT.md` remains authoritative; `safety_status`
   reflects it and does not redefine it.
4. This task creates fixture-level entity contracts and examples only; no
   existing authoritative contract is redefined incompatibly.

## Exact Changed-File Set

New:

- `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md` (339 lines) —
  the eleven-entity spec.
- `shared_context/operations/README.md` (42 lines).
- `shared_context/operations/OPERATIONS_DATA_CONTRACT_SCHEMA.json` (306
  lines) — one JSON Schema draft-07 document, `$defs` per entity.
- `shared_context/operations/OPERATIONS_DATA_CONTRACT.example.json` (165
  lines) — one example fixture object per entity.
- `docs/tasks/MELLYCORE-OPERATIONS-DATA-CONTRACT-001.md` (this report).

Edited (minimum necessary, additive only — no existing sentence deleted):

- `shared_context/PROJECT_STATE.md`, `ROADMAP.md`, `RUN_QUEUE.md`,
  `AGENT_HANDOFF.md` — each gained a short note that this task's work now
  also exists on a second local branch
  (`docs/mellycore-operations-data-contract-001-v2`), still
  `NOT_PRESENT_PENDING_INTEGRATION` in canonical `main`, without claiming
  either branch is canonical and without deciding their reconciliation.

Intentionally unchanged: the prior branch
`docs/mellycore-operations-data-contract-001`, `README.md`,
`shared_context/loops/*`, `shared_context/context_provenance*`, `site/`,
`scripts/`, `tests/`, `.github/`, dependency manifests, and all historical
task reports.

## Entities Defined

`operation_run`, `task_record`, `agent_identity`, `model_provider_usage`,
`token_cost_record`, `validation_result`, `artifact_record`,
`environment_capability_snapshot`, `approval_gate`, `safety_status`,
`recommendation_ledger_entry` — each with purpose, required/optional fields,
allowed status values, forbidden claims, dashboard display semantics (spec
Section 2), a matching `$defs` entry in `OPERATIONS_DATA_CONTRACT_SCHEMA.json`,
and one example fixture in `OPERATIONS_DATA_CONTRACT.example.json`.

## Dashboard Status Vocabulary

Defined in the spec, Section 1.6: `implemented`, `planned`, `simulated`,
`fixture/example`, `not present`, `blocked`, `requires operator approval` —
mapped explicitly onto (and never contradicting) the existing ten-value
`truthful_state` glossary in `MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md`
§1.9. Every fixture carries both fields.

## Environment Capability Snapshot — Non-Authoritative Example Only

Per the operator's explicit instruction, the operator's own local machine
specification (Windows 11 Pro 10.0.26200, Ryzen 7 5700X, 24 GB RAM, RTX 4060
8 GB VRAM / 3072 CUDA cores, 953.9 GB SSD) was used **only** as the
illustrative value set inside `OPERATIONS_DATA_CONTRACT.example.json`'s
`environment_capability_snapshot` object, with `source: "operator_provided"`
(fixed by schema `const`), `dashboard_status: "fixture/example"` (fixed by
schema `const`), and an explicit `example_notice`. No hardware-detection,
polling, or telemetry code was written or implied; the spec's Section 2.8
states this as a hard rule for the entity itself, not only for this example.

## Validation Evidence

- `python scripts/validate_project_state.py` — `PASS MellyCore project
  scaffold validation passed` (run after all file changes above).
- `python -m scripts.context_gate audit --json` — `finding_count: 0`,
  `index_status: "current"`, `writes_performed: 0` (read-only; unaffected by
  this task's docs/spec/fixture-only files, which are outside its scope).
- `python -m scripts.loop_ops validate` — `PASS no findings; registry is
  valid for Phase 1` (9 loops, unaffected by this task).
- `python -c "json.load(...)"` on both new JSON files — both parse as valid
  JSON.
- Automated JSON-Schema-to-example cross-validation was **not** run: the
  `jsonschema` Python library is not installed in this environment and was
  **not** added as a new dependency (per this repository's own precedent of
  not adding a schema-validation dependency for documentation-contract
  fixtures). The schema and example were instead manually cross-checked
  field-by-field during authoring. This is stated explicitly rather than
  implied as automated.
- No `pytest`/`unittest` suite was run; none was required by this task's
  scope, and this report does not claim any test suite passed.
- Forbidden-overclaim grep across the diff and new files for
  `DEPLOYED|RELEASED|LIVE_PROVIDER|LIVE_ORDERS|BROKER|BUY|SELL|EXECUTE`: one
  hit, `shared_context/AGENT_HANDOFF.md:24`, pre-existing (not introduced by
  this task), reading `` `ACCEPTED_REQUIREMENT_NOT_EXECUTED`; runtime,
  release, deploy, and `` — a prohibition/status-label listing of
  not-yet-done categories, not an overclaim. No hits appear anywhere in the
  new spec, schema, example, or README files.
- `git status --short` before this task's edits: clean. After: exactly the
  five new files and four additive edits listed above; no other file
  touched.

## Safety Confirmation

- No provider key, credential, token, secret, private key, `.env` value, or
  account identifier appears anywhere in the new/edited files.
- No workflow YAML, dependency manifest, backend/runtime code, frontend
  scaffold, Three.js reference, or NASA-runtime-retirement action was
  created or performed.
- No trading, broker, order-execution, or buy/sell UX of any kind.
- `environment_capability_snapshot.source` is schema-fixed to
  `operator_provided`; no runtime hardware detection exists or is implied.
- Retired remote `origin` was never contacted; only `clean-origin` was read.
- No push, PR, merge, rebase, squash, force operation, branch deletion, tag,
  release, or deploy was performed.

## Remaining Risks

- Two unreconciled local branches (`...-001` and `...-001-v2`) now exist for
  the same task ID; a future task must decide how to reconcile them before
  either is pushed, to avoid confusing or duplicate history on
  `clean-origin`.
- The eleven-entity decomposition in this task is narrower in some places
  (no direct `AI Estate Inventory`, `Skill Gap Candidate`, or `Memory
  Freshness` fixture pairs) and broader in others (`environment_capability_snapshot`,
  `artifact_record`, `safety_status` are new) than the prior branch's
  seven-artifact set; a future reconciliation task should decide whether to
  fold the prior branch's AI-Estate/Skill-Gap/Memory-Freshness fixtures into
  a later revision of this contract.
- No automated JSON-Schema validation library is present in this
  environment; the manual cross-check reduces but does not eliminate the
  chance of a small field-name mismatch between the markdown spec and the
  JSON Schema file.

## Commit Evidence

Exactly one local commit was created on
`docs/mellycore-operations-data-contract-001-v2` with message
`docs: add operations data contract`, parent
`edf56ea4cace434c3e4cc52dcfe17984ba9f76ea` (canonical `main`, includes PR
#12). No push, PR, or merge was performed. The exact commit SHA lives in
local Git history and is not fabricated here in advance of the commit.

## Next Task

`MELLYCORE-OPERATIONS-DATA-CONTRACT-BRANCH-RECONCILIATION-001` (suggested
name) — decide, under separate operator authorization, how to reconcile
`docs/mellycore-operations-data-contract-001` and
`docs/mellycore-operations-data-contract-001-v2` before either is pushed,
then push and open a PR for the reconciled result. That task is not
authorized by this one and requires its own separate scope review.
