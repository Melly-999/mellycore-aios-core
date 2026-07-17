# MELLYCORE-CONTEXT-INGESTION-GATE-SPEC-001

## Task ID

`MELLYCORE-CONTEXT-INGESTION-GATE-SPEC-001`

## Outcome

`PASS_SPEC_COMMITTED_NO_IMPLEMENTATION`

## Scope

Design the ingestion gate for MellyCore One Brain: the deterministic validation checks, outcomes, refusal rules, human-review boundaries, and write-once recording conventions that enforce the provenance/sensitivity model (`docs/specs/MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001.md`, commit `e7767d9`) before any future context source can enter durable memory. Docs/spec only — no implementation, no database, no MCP, no backend, no dashboard rewrite, no provider calls, no secrets, no ingestion of private files, no push.

## 1. Preflight

- Repo root: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios` (canonical, confirmed)
- Branch: `publish/mellycore-main-001`
- Starting HEAD: `e7767d9` (`docs(aios): specify provenance and sensitivity model`)
- Working tree: clean before any edit

## 2. Research: read before writing

Read in full before drafting: the provenance/sensitivity spec itself, `SOURCE_INGEST_WORKFLOW.md`, `CONTRADICTION_LEDGER.md`, `CONTEXT_GRAPH_SCHEMA.md`, `DECISIONS.md`, `ROADMAP.md`, `RUN_QUEUE.md`, `PROJECT_STATE.md`, and `AGENT_HANDOFF.md`. The gate spec is deliberately positioned as the machine-checkable portion of the provenance spec's Section 8 admission workflow (Steps 1–6), consuming that model without redefining any label, matrix, or default.

## 3. Deliverable: the spec document

`docs/specs/MELLYCORE_CONTEXT_INGESTION_GATE_SPEC_001.md`. It answers the ten design questions:

1. **Admissible inputs** (Section 4): four input classes mapping 1:1 to the provenance `source_type` labels; batches of candidate items with independent per-item outcomes; binaries, db files, live fetches, and MellyTrade-workspace content are not admissible classes at all.
2. **Required metadata** (Section 5): all proposer-supplied `ContextSource` fields must arrive complete; the gate computes `trust_level` itself and never infers, defaults, or backfills missing metadata — incomplete requests are refused, not guessed at.
3. **Immediate refusal** (Section 7): nine mechanical rules R1–R9 with stable reason codes — secret/secret-shaped content, regulated_high_risk content, forbidden paths, incomplete metadata, `allowed_use` loosening, trust-cap violations, id collisions, inadmissible input classes, field-level secrets.
4. **Human approval** (Section 8): two layers — every surviving item still requires Step 7 human review unconditionally, and five conditions additionally park an item as `NEEDS_HUMAN_REVIEW` (private sensitivity, proposed overrides, aged external summaries, supersession, borderline sensitivity).
5. **Acceptance by sensitivity** (Section 9): criteria for `public`/`internal`/`private`; `secret` and `regulated_high_risk` never accepted.
6. **Stale-claim detection** (Section 10): inbound `review_after` enforcement, stale-implication flagging of existing records (never auto-expiry — stale is not false), and staleness contagion via warnings.
7. **Contradiction routing** (Section 11): outcome `CONTRADICTION_FOUND`, a draft ledger entry in the report, human-only resolution, item blocked until resolved or explicitly deferred.
8. **Provenance recording** (Section 12): future `shared_context/context_provenance/` home, aggregate-safe refusal log, human-required `decision_rationale`.
9. **Write-once `ContextSource` shape** (Section 12): the provenance spec's record plus a small gate audit block (`gate_spec_version`, `validation_outcome`, `warnings[]`, `validated_at`); identical-bytes idempotent recovery, differing writes refused — the `persist-run` convention reused verbatim.
10. **Dashboard signals** (Section 14): gate outcomes to date, pending human review, refusals by reason code (never content), stale-implicated records, last gate pass, ledger link-through — specified only, not built.

All task requirements are covered: secret/regulated_high_risk refusal (R1/R2), the generated-content trust cap enforced mechanically (R6), mandatory staleness policy (R4), contradictions routed to the ledger and never auto-resolved (Section 11), dry-run-before-apply and no-write preview mode (Section 13 — preview is the default and currently only mode; apply is future, operator-gated, two-invocation), the five validation outcomes with precedence order (Section 6), and future implementation boundaries (Section 15).

## 4. Key gate decisions

- **`ACCEPT` never means admitted.** Gate outcomes are validation verdicts; the human Step 7 decision remains the only path to `decision: admitted`. Conversely `REFUSE` is machine-binding: a refused item cannot enter memory without correction or a reviewed amendment to the spec itself.
- **Refusals fail fast and are not gate-level overridable.** The nine R-rules run before anything else, in a fixed precedence order (`REFUSE` > `CONTRADICTION_FOUND` > `NEEDS_HUMAN_REVIEW` > `ACCEPT_WITH_WARNINGS` > `ACCEPT`), so an item's outcome is deterministic.
- **The gate never guesses.** No inferred sensitivity, no defaulted staleness policy, no backfilled dates, no auto-filled rationale — silent defaults are how untracked context leaks in.
- **Refusal logging is aggregate-safe.** Reason code, date, proposer — never the refused content, and never even the `source_identity` when that would leak what a secret was (R1/R9).
- **One immutability convention.** Write-once records, identical-bytes idempotent recovery, differing-bytes refusal, expected-HEAD-gated apply — all reused from the tested `persist-run` contract rather than inventing a parallel convention.
- **Preview and apply are separate invocations by construction**, with human review between them; no batch can go raw-proposal → committed-records in one motion.
- **Implementation boundaries are part of the contract** (Section 15): a future implementation may build a standard-library-only CLI, the record directory, tests, and the dashboard fields — and may not add scheduling, network, databases, dependencies, auto-resolution, or any relaxation of R1/R2/trust-cap/no-loosening without a new reviewed spec.

## 5. What remains intentionally unimplemented

- No gate code, CLI, script, or test exists — the checks are specified, not implemented.
- No `ContextSource` record, `shared_context/context_provenance/` directory, or refusal log has been created.
- No contradiction ledger entry was written; the ledger still has no live entries.
- No dashboard tab or field was built; `site/` untouched.
- No apply mode exists in any form.
- No `regulated_high_risk` approval process exists (unchanged gap; safe default remains refusal).

## 6. Validation

Docs-safe validators re-run to confirm no regression (no code touched, none expected):

| Command | Result |
| --- | --- |
| `py -3.9 -m scripts.loop_ops validate` | PASS, 9 loops, 0 findings |
| `py -3.9 -m unittest discover -s tests -p "test_loop_ops*.py"` | 150 tests, OK |
| `py -3.9 scripts/validate_project_state.py` | PASS |

No implementation exists to test — this task added specification and documentation only.

## 7. Files changed

- `docs/specs/MELLYCORE_CONTEXT_INGESTION_GATE_SPEC_001.md` (new — the gate spec)
- `docs/tasks/MELLYCORE-CONTEXT-INGESTION-GATE-SPEC-001.md` (this file)
- `shared_context/ROADMAP.md` (Milestone B ingestion-gate bullet marked completed spec-only)
- `shared_context/RUN_QUEUE.md` (item 48 added)
- `shared_context/PROJECT_STATE.md` (Milestone B section extended; HEAD line updated; next-tasks list updated)
- `shared_context/AGENT_HANDOFF.md` (latest-addition summary and next-recommended-task line updated)
- `shared_context/DECISIONS.md` (one line recording the gate-outcome and preview-before-apply decisions)

No code, loop registry, schema, CLI, evidence, state, site, or dashboard file was touched.

## 8. Safety posture confirmed

- Docs-only change; no provider/network/MCP call; no secrets read or written; no private file ingested.
- No ingestion implementation, database, backend, or MCP.
- No dashboard rewrite — `site/` untouched.
- No scheduler installed or proposed.
- No push. No destructive git command. Nothing touched the MellyTrade workspace.

## 9. Recommended next task

`MELLYCORE-CONTEXT-INGESTION-GATE-DRY-RUN-001` — hand-exercise the gate process (docs-only, human-reviewed, preview semantics: report only, nothing auto-written) on a small first batch of candidate `ContextSource` items drawn from already-committed repo facts, producing the first human-approved admitted records as static committed artifacts. This parallels the proven loop pattern (foundation → dry run → registered run) and validates the spec against reality before any code is written. No gate implementation, database, MCP, or runtime is authorized until this exercise and a subsequent implementation spec/review say so.
