# MELLYCORE-OPERATIONS-DATA-CONTRACT-BRANCH-RECONCILIATION-001

Status: complete locally (comparison/decision task, documentation-only
follow-up edits, one local commit, not pushed, not merged).

## Task Purpose

Compare the two local Operations Data Contract branches —
`docs/mellycore-operations-data-contract-001` (original, 2026-07-19) and
`docs/mellycore-operations-data-contract-001-v2` (fresh pass, commit
`96394c2cc84ff06ad3499c30098bfe164181335c`) — and decide the safest
integration path before either is pushed or a PR is opened.

## Authorization Boundary

The operator authorized: read-only inspection of both branches without
mutating either; comparison of changed files, specs, schemas, fixtures, and
shared-context edits; running existing validators; and at most one local
reconciliation commit if safe and necessary. No push, merge, rebase of the
stale branch across shared-context conflicts, runtime/backend/frontend/
provider work, or secrets/`.env`/workflow YAML/deploy config/trading UX.

## Preflight

- `git status --short` — clean before and after this task's edits (only the
  intended files changed).
- Branch: `docs/mellycore-operations-data-contract-001-v2`.
- HEAD before this task: `96394c2cc84ff06ad3499c30098bfe164181335c`.
- `clean-origin/main` tip: `edf56ea4cace434c3e4cc52dcfe17984ba9f76ea` — fetched
  fresh; `git merge-base --is-ancestor edf56ea... clean-origin/main` confirmed
  YES (canonical `main` unchanged since the prior task, still includes PR
  #12).

## Branch Comparison

| | `docs/mellycore-operations-data-contract-001` (original) | `docs/mellycore-operations-data-contract-001-v2` (fresh) |
|---|---|---|
| Merge-base with `clean-origin/main` | `06a7a421a06abbe38450d276af94985da8ddeba0` — **~10 merged PRs behind** current `main` | `edf56ea4cace434c3e4cc52dcfe17984ba9f76ea` — **current**, zero drift |
| Pushed to `clean-origin`? | No (confirmed via `git ls-remote`, empty result) | No |
| Own new files | `docs/tasks/MELLYCORE-OPERATIONS-DATA-CONTRACT-001.md`; `shared_context/operations/{AI_ESTATE,APPROVAL_RECORD,MEMORY_FRESHNESS,RECOMMENDATION_LEDGER,SKILL_GAP_CANDIDATE,UNIFIED_RUN_LEDGER}{_SCHEMA.json,.example.json}`; `TRUTHFUL_STATE_LABELS.md`; `README.md` (15 files) | `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md`; `docs/tasks/MELLYCORE-OPERATIONS-DATA-CONTRACT-001.md`; `shared_context/operations/{OPERATIONS_DATA_CONTRACT_SCHEMA.json,OPERATIONS_DATA_CONTRACT.example.json,README.md}` (5 files) |
| Entity coverage | AI Estate Inventory, Unified Run Ledger, Skill Gap Candidate, Memory Freshness, Recommendation Ledger, Approval Record (6, one schema+example pair each) + a standalone 10-value Truthful-State Labels reference doc | 11 entities: `operation_run`, `task_record`, `agent_identity`, `model_provider_usage`, `token_cost_record`, `validation_result`, `artifact_record`, `environment_capability_snapshot`, `approval_gate`, `safety_status`, `recommendation_ledger_entry` — a finer-grained, dashboard-oriented decomposition, consolidated into one schema/one example file |
| Shared-context edits | Edits `PROJECT_STATE.md`, `RUN_QUEUE.md`, `ROADMAP.md`, `AGENT_HANDOFF.md` against the **old** `main` state — would require conflict resolution against ~10 PRs of intervening rewrites (renderer P2 chain) to reconcile with current `main` | Edits the same four files, additively, against **current** `main` — no conflict |
| JSON validity | All 12 JSON files parse cleanly (checked via `git show <branch>:<path>` piped to `json.load`, without checkout) | Both JSON files parse cleanly |
| Quality markers | Each schema's `description` states documentation-contract-only scope, names the authoritative contract it must not redefine, and forbids secret-bearing fields; `authentication_mode` is mode-only; every example carries `example_notice`; schemas cross-reference `TRUTHFUL_STATE_LABELS.md` for the ten-value glossary | Same quality bar: documentation-contract descriptions, mode-only `authentication_mode`, `example_notice` per fixture, `dashboard_status` (7-value) + `truthful_state` (10-value) on every record, `environment_capability_snapshot` schema-locked (`const`) to `operator_provided` / `fixture/example` / `SIMULATED` |
| Overclaim grep (`DEPLOYED\|RELEASED\|LIVE_PROVIDER\|LIVE_ORDERS\|BROKER\|BUY\|SELL\|EXECUTE`) | 0 hits in any of the 15 unique files | 0 hits in new/edited content (one self-referential mention of the grep pattern itself in the task report, not an overclaim) |

## Overlap with the AI Operations Intelligence Spec

Both branches translate the same canonical source
(`docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md`, integrated via
PR #7), at different granularity:

- **Conceptually superseded by `-v2` for dashboard purposes:** the original
  branch's `UNIFIED_RUN_LEDGER`, `APPROVAL_RECORD`, and
  `RECOMMENDATION_LEDGER` schema/example pairs map onto `-v2`'s
  `operation_run` + `token_cost_record` + `model_provider_usage` +
  `validation_result` (a finer decomposition of §5), `approval_gate` (§9),
  and `recommendation_ledger_entry` (§8) respectively. No field-level
  contradiction was found — both correctly preserve the same underlying
  enums (`outcome`, `verdict`, the thirteen recommendation-lifecycle states,
  the action-scope ladder) from the canonical spec; they differ only in
  packaging (one wide entity vs. several narrow ones).
- **Not superseded — unique, still-needed coverage:** the original branch's
  `AI_ESTATE_SCHEMA`/`.example` (§4), `SKILL_GAP_CANDIDATE_SCHEMA`/`.example`
  (§6), and `MEMORY_FRESHNESS_SCHEMA`/`.example` (§7) address domains `-v2`
  does not cover at all — `-v2`'s `agent_identity` is deliberately a
  lightweight per-run reference, not a full AI Estate Inventory record, and
  `-v2` has no Skill Gap or Memory Freshness entities. `TRUTHFUL_STATE_LABELS.md`
  is a standalone reference doc that each of those three schemas points to by
  file reference (`shared_context/operations/TRUTHFUL_STATE_LABELS.md`) — the
  three schema pairs and the labels file are not independently portable;
  folding in the schemas without the labels file would leave a dangling
  cross-reference.

**No unresolved semantic contradiction was found between the two branches.**
Differences are in scope and packaging granularity, not conflicting facts,
enums, or claims.

## Decision

**Keep `docs/mellycore-operations-data-contract-001-v2` as the canonical
integration candidate for `MELLYCORE-OPERATIONS-DATA-CONTRACT-001`.**

Reasoning:

1. `-v2`'s merge-base with `clean-origin/main` is current; the original
   branch's is ~10 merged PRs stale, and its `shared_context/*` edits would
   need conflict resolution to reconcile — explicitly out of scope for this
   task ("do not rebase stale branch if conflicts touch shared_context").
2. The three entities with real semantic overlap (run ledger, approval,
   recommendation) are already covered, compatibly, by `-v2`'s finer
   decomposition.
3. The four non-superseded file pairs (AI Estate, Skill Gap, Memory
   Freshness, Truthful-State Labels) are valuable, reviewer-quality prior art
   but form a cross-referencing set that needs its own content review before
   being folded in — not a same-task blind copy. This is deferred to a
   separate, explicitly authorized follow-up task (Section "Next Task"
   below), consistent with "preserve valuable prior-art content only if it
   does not create conflicts or overclaims" — folding it in *without* that
   review would risk exactly the kind of overclaim this task is meant to
   prevent.

The original branch (`docs/mellycore-operations-data-contract-001`) was
**not** checked out, rebased, merged, deleted, or pushed. It remains
available, unchanged, for the follow-up task to draw from.

## Files Changed (this task)

Documentation-only, recording the decision above — no schema or fixture
content was copied or merged in this task:

- `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md` — Section 6
  rewritten from "deferred, not performed by this task" to record the
  comparison findings and decision.
- `shared_context/PROJECT_STATE.md`, `ROADMAP.md`, `RUN_QUEUE.md`,
  `AGENT_HANDOFF.md` — each gained an additive paragraph recording that this
  reconciliation task ran, selected `-v2` as the candidate, and identified
  the four-file-pair follow-up; no existing sentence was deleted, and none
  now claims integration into canonical `main`.
- `docs/tasks/MELLYCORE-OPERATIONS-DATA-CONTRACT-BRANCH-RECONCILIATION-001.md`
  (this report).

## Validation Evidence

- `python scripts/validate_project_state.py` — `PASS MellyCore project
  scaffold validation passed` (run both before and after this task's edits).
- `python -m scripts.context_gate audit --json` — `finding_count: 0`,
  `index_status: "current"`, `writes_performed: 0`.
- `python -m scripts.loop_ops validate` — `PASS no findings; registry is
  valid for Phase 1` (9 loops).
- JSON parse check: both `-v2` JSON files, and all 12 JSON files unique to
  the original branch (read via `git show <branch>:<path>` without checkout),
  parse successfully — 14 files total, 0 failures.
- Overclaim grep
  (`DEPLOYED|RELEASED|LIVE_PROVIDER|LIVE_ORDERS|BROKER|BUY|SELL|EXECUTE`,
  case-insensitive) across every unique file in both branches: 0 genuine
  hits. (One self-referential mention of the pattern itself, inside this
  report and the prior task's report, documenting the search — not an
  overclaim.)
- No `pytest`/`unittest` suite was run; none is claimed.

## Safety Confirmation

- No secrets, credentials, tokens, or `.env` values in any compared or
  edited file.
- No runtime, backend, frontend, provider-integration, or trading-UX code
  was written, copied, or implied.
- No push, merge, rebase, force operation, branch deletion, tag, release, or
  deploy was performed. Retired `origin` was never contacted.
- Canonical `main` (`edf56ea...`) is unchanged and remains truthful: nothing
  in canonical `main`'s shared-context files claims this contract, in either
  branch, is integrated.

## Remaining Risks

- The original branch (`docs/mellycore-operations-data-contract-001`)
  remains unpushed and undeleted; if the operator later pushes it directly
  without going through the recommended follow-up, its stale
  `shared_context/*` edits would conflict with current canonical `main`.
- The four non-superseded file pairs have not yet been re-validated against
  the *current* `-v2` spec's field-naming conventions (e.g. `-v2` uses
  `dashboard_status` + `truthful_state` on every record; the original
  branch's files use only `truthful_state`) — the follow-up task will need
  to decide whether to adapt them to `-v2`'s two-field convention or keep
  them as a distinct, self-consistent sub-package.
- No JSON Schema validation library is installed in this environment, so
  schema-to-example conformance for both branches was checked manually
  (during authoring and during this comparison), not by an automated tool.

## Next Task

`MELLYCORE-OPERATIONS-DATA-CONTRACT-AI-ESTATE-SKILLGAP-MEMORY-001`
(suggested name) — under separate operator authorization, review and fold
the original branch's `AI_ESTATE`, `SKILL_GAP_CANDIDATE`, `MEMORY_FRESHNESS`
schema/example pairs and `TRUTHFUL_STATE_LABELS.md` into
`docs/mellycore-operations-data-contract-001-v2` (or a new branch cut from
it), deciding along the way whether to adapt them to the `-v2`
`dashboard_status`/`truthful_state` convention. Only after that fold-in is
reviewed and validated should push and PR creation for the combined result be
separately authorized.
