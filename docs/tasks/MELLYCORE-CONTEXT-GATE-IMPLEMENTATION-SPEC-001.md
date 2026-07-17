# MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-SPEC-001

## Task ID

`MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-SPEC-001`

## Outcome

`PASS_SPEC_COMMITTED_NO_IMPLEMENTATION`

## Scope

Write the docs-only implementation specification for the Context Ingestion Gate CLI, building on the four completed Milestone B steps (provenance spec `e7767d9`, gate spec `c4f9b6f`, dry run `f7a2d9f`, first admissions `b3597df`). No code, no backend, no provider calls, no dashboard code, no push.

## 1. Preflight

- Repo root: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios` (canonical, confirmed)
- Branch: `publish/mellycore-main-001`
- Starting HEAD: `b3597df` (`docs(aios): admit first context sources`)
- Working tree: clean before any edit

## 2. Deliverable

`docs/specs/MELLYCORE_CONTEXT_GATE_IMPLEMENTATION_SPEC_001.md`, covering every requirement:

1. **Canonical directory** (Section 2): `shared_context/context_provenance/` with `records/<source_id>.json` (write-once), `refusals/REFUSAL_LOG.jsonl` (append-only), derived `INDEX.json`, `MIGRATION_001.md`, and a README. Deterministic serialization (UTF-8, sorted keys) so write-once byte comparisons and git diffs are stable. A canonical record separates immutable `ContextSource` + `gate_audit` content from a mutable-by-definition `envelope` (location/lifecycle metadata) — the distinction that lets migration relocate records without ever touching record content.
2. **Migration plan** (Section 3): relocation-not-re-decision for the six admitted preview records — same `source_id`s, envelope-only transformation, SHA-256 + parsed-field-identity verification recorded in `MIGRATION_001.md`, preview store tombstoned in the same commit, full apply gating, defense-in-depth re-run of R1–R9, one-time and idempotent with staged writes.
3. **Refusal log** (Section 4): JSONL, append-only, structurally whitelisted to five aggregate-safe keys (`refused_at`, `reason_code`, `proposed_by`, `batch_id`, `gate_spec_version`) so content leakage is a type error; written only by `apply`; the dry run's historical C7 refusal backfilled as line one during migration.
4. **CLI** (Section 5): `scripts/context_gate/` mirroring the `loop_ops` module pattern, standard library only, `preview` (default gate operation, writes nothing, reports the exact bytes apply would write), `validate-record` (single-file shape check, used internally by apply), `apply` (the only record-writing command: non-empty `--operator-approval-id`, `--expected-head` match, clean tree, human Step 7 decision fields required per record, all checks re-run at apply time, `--migrate-preview` for the one-time migration), `rebuild-index` (derived, deterministic, content-free index), `audit` (computed-only counts including stale-implicated records, orphaned supersessions, blocked items, refusal counts; `--json` for the dashboard snapshot shape).
5. **Preview default / apply gating / write-once / hard refusals**: preview is default and non-writing; apply is the sole writer and re-refuses `secret`, `regulated_high_risk`, forbidden paths, and generated-high-trust at write time even if a manifest claims a prior clean preview; write-once uses the identical-bytes-idempotent / differing-bytes-refused `persist-run` contract.
6. **Blocked C8 handling** (Section 6): blocked items are first-class manifest citizens (re-reported by `preview`, counted by `audit`, never writable while blocked); the operator's eventual answer resolves via the normal pipeline as either a new admitted candidate or a durable `decision: rejected` record. The spec records a recommendation (decline — `PROJECT_STATE.md` already serves the purpose and a rejection record documents the choice without duplicating private-shaped data) while leaving the decision explicitly with the operator.
7. **Test plan** (Section 9): `unittest`-only suites mirroring `test_loop_ops_*` — per-rule R1–R9 tests with passing twins, outcome-precedence ordering, all 8 trust-lookup cells, every warning and parking condition, staleness both directions, the loops-vs-runs near-miss as a no-contradiction regression test, write-once/path-safety/apply-gating/refusal-log-whitelist/migration-tamper tests, index determinism, and a shipped-records validation test.
8. **Dashboard-read contract** (Section 7): read-only live reads of committed files; `allowed_use` filtering via the content-free index (`internal_reasoning_only` never rendered — count only); refusals as counts only; stale badged not hidden; superseded behind history affordance; `notes` never displayed; `[MOCK]` labeling preserved.
9. **Phasing** (Section 8): I1 checks+preview, I2 apply+migration, I3 index+audit, I4 dashboard tab — each a separate, explicitly approved task, all bound by the gate spec Section 15 boundaries (stdlib only, no network/MCP/DB/scheduler, no auto-resolution, no constraint relaxation, no push).

## 3. Key decisions

- **Envelope vs. content split.** Write-once immutability applies to record *content* (`ContextSource` + `gate_audit`); a small `envelope` block carries location/lifecycle metadata. This resolves the tension between "records never change" and "records must move from the preview store to the canonical home" without weakening either rule — migration is provably content-preserving via parsed-field identity checks, not trust.
- **Apply trusts nothing.** A preview report is advice to the human, not a credential for apply: every check re-runs at write time. This closes the gap where a stale or forged preview could smuggle a violating record past the gate.
- **Aggregate safety by construction.** The refusal-log writer accepts only whitelisted keys, making the "never log refused content" rule structural rather than procedural.
- **The index is disposable.** `INDEX.json` is derived, content-free, and rebuildable — the dashboard filters on it, but apply never reads it, so a corrupted or stale index can never affect admission decisions.
- **Blocked questions must terminate.** The C8 pattern gets a defined lifecycle (blocked → operator answer → admitted candidate or durable rejection record) so operator questions cannot silently evaporate.

## 4. Validation

| Command | Result |
| --- | --- |
| `py -3.9 -m scripts.loop_ops validate` | PASS, 9 loops, 0 findings |
| `py -3.9 -m unittest discover -s tests -p "test_loop_ops*.py"` | 150 tests, OK |
| `py -3.9 scripts/validate_project_state.py` | PASS |

No implementation exists to test — this task added specification and documentation only.

## 5. Files changed

- `docs/specs/MELLYCORE_CONTEXT_GATE_IMPLEMENTATION_SPEC_001.md` (new — the implementation spec)
- `docs/tasks/MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-SPEC-001.md` (this file)
- `shared_context/ROADMAP.md` (Milestone B implementation-spec bullet added)
- `shared_context/RUN_QUEUE.md` (item 51 added)
- `shared_context/PROJECT_STATE.md` (HEAD line updated; Milestone B section extended; next-tasks list updated)
- `shared_context/AGENT_HANDOFF.md` (latest addition and next-recommended-task updated)

`DECISIONS.md` unchanged — no new policy decision was made; the envelope/content split and apply-re-check behaviors are spec design within the already-decided gate framework, and the C8 recommendation is explicitly not a decision.

## 6. What remains unimplemented

- All of it, by design: no `scripts/context_gate/` code, no tests, no canonical directory, no migration, no refusal log, no index, no audit command, no dashboard tab.
- The six admitted records remain in `shared_context/context_provenance_preview/` pending Phase I2 migration.
- The blocked C8 operator decision remains open (recommendation recorded in the spec, Section 6).
- No `regulated_high_risk` approval process exists; refusal remains the only path.

## 7. Safety posture confirmed

- Docs-only; no provider/network/MCP call; no secrets; no backend, CLI, or dashboard code; no push; no destructive git action; nothing touched MellyTrade or any forbidden path.

## 8. Recommended next task

`MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I1-001` — implement Phase I1 exactly as specified: the `scripts/context_gate/` scaffold, `ContextSource` models, `validate-record`, `preview` with the full R1–R9/warning/parking/staleness/contradiction check set, and the Section 9 checks test suite. No write path yet (apply/migration is Phase I2), which keeps the first code task read-only by construction. Before or during I2, the operator should answer the blocked C8 question (spec recommendation: decline with a durable rejection record).
