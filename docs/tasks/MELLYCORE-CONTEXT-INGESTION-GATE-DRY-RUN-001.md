# MELLYCORE-CONTEXT-INGESTION-GATE-DRY-RUN-001

## Task ID

`MELLYCORE-CONTEXT-INGESTION-GATE-DRY-RUN-001`

## Outcome

`PASS_GATE_DRY_RUN_PREVIEW_NO_ADMISSION` — the ingestion gate was hand-exercised in preview semantics on an 8-item candidate batch; 6 draft `ContextSource` records were produced pending human Step 7 review; **nothing was admitted**; no gate implementation exists or was created.

## Scope

Hand-exercise the gate specified in `docs/specs/MELLYCORE_CONTEXT_INGESTION_GATE_SPEC_001.md` against the provenance/sensitivity model in `docs/specs/MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001.md`, using only committed repo facts. Docs/static artifacts only — no backend, no CLI implementation, no provider calls, no secrets, no private-file ingestion, no dashboard change, no push.

## 1. Preflight

- Repo root: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios` (canonical, confirmed)
- Branch: `publish/mellycore-main-001`
- Starting HEAD: `c4f9b6f` (`docs(aios): specify context ingestion gate`)
- Working tree: clean before any edit
- Every fact claimed by a `repo_derived` candidate below was verified by direct read at this HEAD (directory listings / file existence checks), which is what qualifies those items as `verified` under the provenance spec's Section 4.2 rule for `repo_derived` content.

## 2. How this dry run maps to the gate spec

- **Mode:** preview (gate spec Section 13) — every check evaluated, full report emitted, and the gate itself wrote nothing. The draft records and this report are an ordinary human-reviewed docs commit, exactly the path Section 13 allows for keeping a preview report.
- **Hand-exercised:** no code ran. Each check (R1–R9, warning conditions, parking conditions, staleness, contradiction scan) was applied manually in spec order. The gate audit blocks in the draft records carry `"mode": "preview_hand_exercised"` so no future reader mistakes this for tool output.
- **Preview directory:** drafts live in `shared_context/context_provenance_preview/` — deliberately **not** the canonical future home `shared_context/context_provenance/records/`, which gate spec Section 12 reserves for a future, separately approved implementation task. See that directory's README for its rules.
- **No admission claimed:** every draft has `reviewed_by: null`, `decision: null`, `record_status: DRAFT_PENDING_HUMAN_REVIEW`. Per both specs, only a human Step 7 decision can produce `decision: admitted`.

## 3. Candidate batch and per-item evaluation

Eight candidates, all from committed repo facts. Trust levels are computed from the provenance spec Section 4.3 lookup (`repo_derived` × `verified` → `high`; `generated` × `unverified` → `low`).

| # | Candidate claim (abbreviated) | `source_type` | `verification_state` | Proposed sensitivity | Computed trust | `staleness_policy` (`review_after`) | `allowed_use` | Outcome | Reason/warning codes | Human review? |
|---|---|---|---|---|---|---|---|---|---|---|
| C1 | Milestone A closed by `MELLYCORE-OPERATIONAL-TRUST-REVIEW-001` (commit `befaee5`) | `repo_derived` | `verified` | `internal` | `high` | `immutable_historical` (—) | `internal_summary_display` | **ACCEPT** | — | Step 7 (always) |
| C2 | Live dashboard preview committed at `site/dashboard.html` (commit `4272e1b`), mock data labeled, no provider calls | `repo_derived` | `verified` | `internal` | `high` | `immutable_historical` (—) | `internal_summary_display` | **ACCEPT** | — | Step 7 (always) |
| C3 | `project-health` has exactly two persisted run-evidence files; `audit` reports `exercised: 1` because the tier counts loops, not runs | `repo_derived` | `verified` | `internal` | `high` | `volatile` (`2026-07-24`) | `internal_summary_display` | **ACCEPT** | — | Step 7 (always) |
| C4 | Provenance/sensitivity spec exists (commit `e7767d9`), docs-only | `repo_derived` | `verified` | `internal` | `high` | `immutable_historical` (—) | `internal_summary_display` | **ACCEPT** | — | Step 7 (always) |
| C5 | Ingestion gate spec exists (commit `c4f9b6f`), docs-only | `repo_derived` | `verified` | `internal` | `high` | `immutable_historical` (—) | `internal_summary_display` | **ACCEPT** | — | Step 7 (always) |
| C6 | Generated one-sentence summary of the current safety posture (static-first, report-only, no secrets/MCP/scheduler/trading, 127.0.0.1-only previews) | `generated` | `unverified` | `internal` | `low` | `periodic_review` (`2026-10-17`) | `internal_reasoning_only` (stricter than default, rationale stated) | **ACCEPT_WITH_WARNINGS** | `allowed_use_stricter_than_default` (Section 6.1) | Step 7 (always), warning attached |
| C7 | Generated summary of the model routing strategy (from `MODEL_ROUTING.md`), **deliberately proposing `trust_level: high`** as a negative-path exercise | `generated` | `unverified` | `internal` | computed `low`; proposed `high` | `volatile` (`2026-08-17`) | `internal_summary_display` | **REFUSE** | `trust_cap_violation` (R6) | N/A — refused before review |
| C8 | The canonical local repo path is `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios` (machine-specific configuration, from `PROJECT_STATE.md`) | `repo_derived` | `verified` | `private` | `high` | `periodic_review` (`2026-10-17`) | `internal_reasoning_only` (private default) | **NEEDS_HUMAN_REVIEW** | parking condition 1 (`private` sensitivity never rides through on a default) | Yes — parked with a specific question (below) |

**Counts:** 8 candidates → 5 `ACCEPT`, 1 `ACCEPT_WITH_WARNINGS`, 1 `REFUSE`, 1 `NEEDS_HUMAN_REVIEW`, 0 `CONTRADICTION_FOUND`.

Precedence order was applied per item as specified (`REFUSE` > `CONTRADICTION_FOUND` > `NEEDS_HUMAN_REVIEW` > `ACCEPT_WITH_WARNINGS` > `ACCEPT`); no item triggered more than one outcome class, so no precedence tiebreak was actually needed this pass.

### C7 refusal detail (aggregate-safe)

Recorded per gate spec Section 7: reason code `trust_cap_violation`, date `2026-07-17`, proposer `MELLYCORE-CONTEXT-INGESTION-GATE-DRY-RUN-001`. The item was constructed **deliberately** to exercise R6: a `generated` item proposing `trust_level: high` must be refused mechanically, because only a human at Step 7 may raise trust above the computed default. The refusal worked as specified. No draft record file was created for C7 (refused items get no draft). The content itself was not secret, so identity may be shown: an agent summary of `shared_context/MODEL_ROUTING.md`. A corrected resubmission (proposing no trust above `low`, or leaving trust to the gate) would be a new candidate and would plausibly reach `ACCEPT` — that resubmission was intentionally *not* done in this pass, to keep the negative path visible in the record.

### C8 parked question for the human reviewer

Specific question, per gate spec Section 8's "parked items state a specific question" rule: *the canonical repo path is machine-specific (`private` per the provenance spec's own example of machine-specific configuration) and is already committed in `PROJECT_STATE.md`. Should it be admitted as a `private`/`internal_reasoning_only` record (useful for agent reasoning about the canonical workspace), or is admission unnecessary because the committed file itself already serves this purpose?* No draft file was created; the item waits for that decision.

### Contradiction scan (Step 6)

Each candidate claim was compared against the other seven and against current `shared_context/*.md` state. **No contradiction found.** One deliberate near-miss is worth recording: C3's "two persisted runs" vs. `audit --json`'s `exercised: 1` looks like a numeric conflict but is not one — the exercised tier counts loops, not runs. The claim text of C3 embeds that clarification precisely so a future ingest pass does not file a false contradiction. No `CONTRADICTION_LEDGER.md` entry was drafted or written; the ledger still has no live entries.

### Staleness scan

No admitted records exist yet, so the against-the-store direction (stale-implication) had nothing to check — noted as exercised-but-vacuous rather than skipped. Inbound checks ran for all 8: every `volatile`/`periodic_review` item carries `review_after`; none was past-dated; no staleness warnings fired.

## 4. Artifacts produced

- `shared_context/context_provenance_preview/README.md` — preview-directory rules (not the canonical store; drafts only; refused/parked items get no files).
- Six draft records (`preview: true`, `record_status: DRAFT_PENDING_HUMAN_REVIEW`, `reviewed_by`/`decision` null), one per `ACCEPT`/`ACCEPT_WITH_WARNINGS` item:
  - `ctx-2026-07-17-milestone-a-closed.json`
  - `ctx-2026-07-17-dashboard-preview-committed.json`
  - `ctx-2026-07-17-project-health-two-runs.json`
  - `ctx-2026-07-17-provenance-spec-exists.json`
  - `ctx-2026-07-17-gate-spec-exists.json`
  - `ctx-2026-07-17-safety-posture-summary.json`
- This report (the preview report of record, including the aggregate-safe refusal entry for C7 and the parked question for C8).

## 5. Key lessons from the dry run

1. **The spec vocabulary held.** All 8 items classified cleanly with the existing labels, outcomes, reason codes, and parking conditions — no missing enum value, no ambiguous rule, no case where two rules gave conflicting instructions.
2. **Claim phrasing determines staleness class, and it matters.** "The dashboard preview was committed as `4272e1b`" is `immutable_historical`; "the dashboard currently reads these files" would be `volatile`. Rewording candidates as dated events wherever honest made most of the batch durable. Future proposers should be pointed at this pattern explicitly.
3. **Contradiction detection needs subject semantics, not string/number matching.** The `two runs` vs. `exercised: 1` near-miss would be a false positive for any naive numeric comparison. The mitigation used here — embedding the loops-not-runs clarification inside the claim text — works, but a future implementation must treat "same subject" carefully.
4. **The trust cap refusal is exercisable and unambiguous** (C7): R6 fired exactly as written, and the aggregate-safe refusal-logging rule was easy to follow because the spec states precisely what may be recorded.
5. **The preview/canonical directory split resolved a real tension.** The gate spec reserves `shared_context/context_provenance/` for the implementation task; without a designated preview location, this dry run would have had to either violate that boundary or produce no durable drafts. The `context_provenance_preview/` convention (with README rules) is worth carrying forward; the future Step 7 review task should decide whether decided records migrate to the canonical home or the drafts are decided in place.
6. **Step 7 is the bottleneck by design.** Even a fully clean batch produces zero admitted records without an operator review — the dry run confirms the workflow cannot silently self-admit, which is exactly the property the gate exists to guarantee.

## 6. Validation

Docs-safe validators re-run (no code touched; none expected to change):

| Command | Result |
| --- | --- |
| `py -3.9 -m scripts.loop_ops validate` | PASS, 9 loops, 0 findings |
| `py -3.9 -m unittest discover -s tests -p "test_loop_ops*.py"` | 150 tests, OK |
| `py -3.9 scripts/validate_project_state.py` | PASS |

All six draft JSON files parse as valid JSON (checked with the standard-library `json` module via a one-off read — no script was added to the repository).

## 7. What remains intentionally unimplemented

- No gate code, CLI, script, or test exists — this run was performed by hand against the spec.
- **No `ContextSource` record is admitted.** Six drafts exist, all pending human Step 7 review; `reviewed_by` and `decision` are null in every one.
- The canonical `shared_context/context_provenance/records/` directory and the append-only refusal log do not exist (the C7 refusal is recorded aggregate-safely in this report only).
- No contradiction ledger entry exists; the ledger has no live entries.
- No apply mode exists in any form; no dashboard change was made; no `regulated_high_risk` approval process exists.

## 8. Files changed

- `shared_context/context_provenance_preview/README.md` (new)
- `shared_context/context_provenance_preview/ctx-2026-07-17-*.json` (6 new draft records)
- `docs/tasks/MELLYCORE-CONTEXT-INGESTION-GATE-DRY-RUN-001.md` (this file)
- `shared_context/ROADMAP.md`, `shared_context/RUN_QUEUE.md`, `shared_context/PROJECT_STATE.md`, `shared_context/AGENT_HANDOFF.md` (state sync)

No code, loop registry, schema, CLI, evidence, state, site, or dashboard file was touched.

## 9. Safety posture confirmed

- Docs/static artifacts only; no provider/network/MCP call; no secrets read or written; no private file ingested (C8's path fact came from the already-committed `PROJECT_STATE.md`, and it was parked, not admitted).
- No gate implementation, database, backend, or scheduler.
- No dashboard change; `site/` untouched.
- No push. No destructive git command. Nothing touched the MellyTrade workspace.

## 10. Recommended next task

`MELLYCORE-CONTEXT-FIRST-ADMISSION-REVIEW-001` — the human Step 7 review of this batch (docs-only): the operator confirms or overrides each draft's classification, decides the C8 parked question, sets `reviewed_by`/`decision`/`decision_at`/`decision_rationale` on each record, decides whether decided records stay in the preview directory or move to the canonical `shared_context/context_provenance/` home (creating it as an explicitly approved act), and commits the result — producing the first genuinely **admitted** `ContextSource` records. Only after that review has proven the full workflow end-to-end should a gate implementation spec/task be considered.
