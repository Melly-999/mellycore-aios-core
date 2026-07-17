# Context Gate Implementation Spec

**Task ID:** MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-SPEC-001
**Version:** 1.0
**Status:** Draft implementation specification (docs-only)
**Scope:** The concrete CLI, directory layout, migration plan, test plan, and dashboard-read contract for implementing the Context Ingestion Gate — code to be written only by a future, separately approved task

---

## 1. Purpose and Position

Milestone B has now proven the full One Brain admission workflow **by hand**, end to end:

1. `MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001.md` (`e7767d9`) — the model: `ContextSource` shape, provenance/sensitivity/trust labels, staleness, contradiction guidance.
2. `MELLYCORE_CONTEXT_INGESTION_GATE_SPEC_001.md` (`c4f9b6f`) — the gate: admissible inputs, refusal rules R1–R9, five outcomes, preview-before-apply, implementation boundaries.
3. `MELLYCORE-CONTEXT-INGESTION-GATE-DRY-RUN-001` (`f7a2d9f`) — a hand-exercised preview pass: 8 candidates, all five outcome classes exercised (5/1/1/1/0), six draft records.
4. `MELLYCORE-CONTEXT-FIRST-ADMISSION-REVIEW-001` (`b3597df`) — the operator-delegated Step 7 review: all six drafts admitted, now write-once immutable in `shared_context/context_provenance_preview/`, one item blocked on an operator question.

This document specifies **how to implement** what was just proven by hand: a standard-library-only CLI under `scripts/context_gate/`, the canonical record store, the migration of the six admitted records, the refusal log, and the contract a future dashboard tab must honor. It stays inside the gate spec's Section 15 boundaries in every particular.

**This document authorizes no implementation.** No code, test, directory, or record is created by this task. The gate spec and provenance spec remain the authorities on gate semantics; where this document and they conflict, they win.

---

## 2. Canonical Directory Layout

Created by implementation Phase I2 (Section 8), not before, and never by hand:

```
shared_context/context_provenance/
  README.md                      # rules of the store (write-once, no secrets, migration note)
  records/
    ctx-YYYY-MM-DD-<slug>.json   # one write-once ContextSource record per file
  refusals/
    REFUSAL_LOG.jsonl            # append-only, aggregate-safe (Section 4)
  INDEX.json                     # derived index, rebuildable at any time (Section 5.4)
  MIGRATION_001.md               # manifest of the preview→canonical migration (Section 3)
```

Rules:

- `records/` files are **write-once**: after a file exists, an identical-bytes rewrite is idempotent recovery (allowed, no-op); any differing write is refused — the exact `persist-run` contract. The only permitted in-place mutation ever is setting `superseded_by` on a decided record, and even that is done via `apply` with operator approval, never by hand.
- Filenames are exactly `<source_id>.json`. `source_id` uniqueness is enforced at both preview and apply (gate rule R7).
- `INDEX.json` is **derived data**: deleting it loses nothing; `rebuild-index` regenerates it deterministically from `records/`. It is never the source of truth and `apply` never reads it to make decisions.
- Every JSON file is UTF-8, LF, pretty-printed with sorted keys (deterministic bytes so write-once comparisons and git diffs are stable).

### 2.1 Canonical record shape

A canonical record file contains:

- All `ContextSource` fields from the provenance spec Section 3 (including `reviewed_at`, adopted from the first admission review as a permanent field).
- The `gate_audit` block from the gate spec Section 12 (`gate_spec_version`, `validation_outcome`, `warnings[]`, `validated_at`, `mode`).
- An `envelope` block for location/lifecycle metadata that is **not** part of the record's semantic content: `{"store": "canonical", "migrated_from": <path or null>, "migrated_at": <date or null>}`.

The distinction matters for write-once semantics: the `ContextSource` + `gate_audit` content of a decided record is immutable; the `envelope` exists precisely so relocation (Section 3) never has to touch record content. The preview-era fields `preview` and `record_status` are envelope-era ancestors and do not appear in canonical records.

---

## 3. Migration Plan for the Six Admitted Preview Records

The six records admitted by `MELLYCORE-CONTEXT-FIRST-ADMISSION-REVIEW-001` currently live in `shared_context/context_provenance_preview/` with `record_status: ADMITTED_IN_PREVIEW_LOCATION_PENDING_CANONICAL_MIGRATION`. Migration is Phase I2's first real `apply`-mode act and must satisfy all of the following:

1. **Relocation, not re-decision.** The same `source_id` is kept — this is the same record moving home, not a new claim. No decision field, provenance field, claim, or rationale may change by even one byte.
2. **Mechanical transformation, fully specified:** canonical file = preview file with (a) the `preview` and `record_status` envelope fields removed, (b) the Section 2.1 `envelope` block added (`migrated_from` = the preview path, `migrated_at` = migration date), (c) re-serialized in the canonical deterministic format. Nothing else.
3. **Hash-verified manifest.** `MIGRATION_001.md` records, per record: `source_id`, SHA-256 of the preview file, SHA-256 of the canonical file, and a machine-checkable statement that the `ContextSource` + `gate_audit` fields are value-identical (the implementation must verify this by parsed-field comparison, not trust it).
4. **Same commit retires the preview store.** The six preview JSON files are removed and the preview `README.md` is replaced with a tombstone pointing at the canonical store and the migration commit — git history preserves the originals; write-once is honored because content provably did not change (item 3) and the relocation is an operator-approved, spec-defined act, not a silent mutation.
5. **Full apply gating** (Section 5.3): operator approval id, expected-HEAD match, clean working tree. The migration also re-runs all gate refusal checks against each record as defense in depth — a record that would today violate R1–R9 must fail migration loudly (none should; this is a tripwire, not an expectation).
6. **One-time and idempotent.** Re-running migration after success is a no-op (canonical files already present with identical bytes); a partial failure leaves the preview store untouched (canonical writes are staged to a temp path and only moved into place after all six verify).

---

## 4. Append-Only Refusal Log

`shared_context/context_provenance/refusals/REFUSAL_LOG.jsonl` — one JSON object per line, append-only, never rewritten, never sorted, never compacted:

```json
{"refused_at": "YYYY-MM-DD", "reason_code": "trust_cap_violation", "proposed_by": "<task/agent id>", "batch_id": "<batch manifest id>", "gate_spec_version": "..."}
```

- **Aggregate-safe only:** no claim text, no content, and — for `secret_content` (R1) and `field_level_secret` (R9) — no `source_identity` either. The line records *that* a refusal happened and *why-category*, never *what* was refused. The implementation must enforce this structurally: the refusal-log writer accepts only these five whitelisted keys, so leaking a content field is a type error, not a review catch.
- Written only by `apply` (a preview pass reports would-be refusals but writes nothing, per the gate spec's no-write rule).
- `audit` and the dashboard consume it as counts grouped by `reason_code` only.
- The dry run's one historical refusal (C7, `trust_cap_violation`, 2026-07-17, recorded in the dry-run report) is **backfilled as the first line** during migration, sourced from that report, so the log is complete from the workflow's true beginning.

---

## 5. CLI Specification

Module layout mirrors `scripts/loop_ops/` exactly: `scripts/context_gate/` with `__main__.py`, `cli.py`, `models.py`, `checks.py`, `store.py`, `index.py`, `audit.py`. Standard library only. Invocation: `py -3.9 -m scripts.context_gate <command>`. Every command exits nonzero on any failure. **Preview is the default**: running with no subcommand prints help and performs no action; no command writes anything except `apply` and `rebuild-index`, and `rebuild-index` writes only the derived `INDEX.json`.

### 5.1 `preview --batch <manifest.json> [--json]`

The default gate operation and the only way to evaluate a new batch.

- Input: a batch manifest (a JSON file listing candidate items, each carrying the proposer-supplied `ContextSource` fields per gate spec Section 5). The manifest may live anywhere readable; nothing in the repo is written.
- Runs, in gate-spec order: R1–R9 refusal checks → metadata completeness → trust computation (proposer suggestions above the computed default trigger R6, never silent acceptance) → sensitivity criteria → staleness (both directions, against `records/`) → contradiction scan (against `records/` and same-batch items) → outcome assignment by fixed precedence.
- Output: a full per-item report (human-readable; `--json` for machine parity): outcome, reason/warning codes, computed trust, parked questions verbatim, draft contradiction-ledger entries, and the exact canonical bytes each `ACCEPT`/`ACCEPT_WITH_WARNINGS` item *would* produce — so the human reviews precisely what `apply` would later write.
- **Writes nothing**, including on catastrophic input errors.

### 5.2 `validate-record --file <path> [--json]`

Shape-checks one record file (draft, decided, or canonical) against the `ContextSource` schema: required fields, enum values, date formats, `review_after` presence for `volatile`/`periodic_review`, field-level no-secrets scan (R9 patterns), deterministic-serialization check for canonical files. Read-only. Used by tests, by hand, and by `apply` internally on every record it is about to write.

### 5.3 `apply --batch <manifest> --operator-approval-id <id> --expected-head <sha> [--migrate-preview]`

The only command that writes records. Hard requirements, all `persist-run`-proven patterns:

- Non-empty `--operator-approval-id`; `--expected-head` equal to the repository's actual current HEAD; clean working tree.
- Every record to be written must already carry its **human Step 7 decision**: `reviewed_by`, `reviewed_at`, `decision`, `decision_at`, `decision_rationale` all non-null. `apply` writes decided records; it never decides. A manifest item without a recorded human decision is skipped with a loud report line, never written.
- Re-runs **all** preview checks at apply time (defense in depth — a stale preview report confers nothing). Any R1–R9 hit aborts that item; `secret`/`regulated_high_risk`/forbidden-path/generated-high-trust items can therefore never be written even if a manifest lies about a prior preview.
- Write-once enforcement per Section 2; path/symlink/case-collision safety per `persist.py` precedent; refusal-log appends for refused items (Section 4); contradiction-ledger entries written only when the human decision explicitly includes the reviewed entry text.
- `--migrate-preview` performs Section 3's one-time migration (and is refused with a clear message once `MIGRATION_001.md` exists and all six canonical files verify).
- Never pushes, never touches the network, never calls a provider, never schedules anything.

### 5.4 `rebuild-index`

Regenerates `INDEX.json` deterministically from `records/*.json`: for each record, `source_id`, `source_type`, `sensitivity_level`, `allowed_use`, `trust_level`, `staleness_policy`, `review_after`, `decision`, `superseded_by`, `validation_outcome`, and file name. Sorted by `source_id`; stable bytes. Contains **no claim text and no notes** — it is a routing/filtering index, and keeping content out of it is what makes the dashboard-read contract (Section 7) enforceable at the file level. Safe to run anytime; a git-dirty `INDEX.json` after rebuild simply means the index was stale.

### 5.5 `audit [--json]`

Read-only, computed-only (the `loop_ops audit` philosophy — tiers computed from evidence, never stored claims):

- Record counts by `source_type`, `sensitivity_level`, `trust_level`, `decision`.
- **Stale-implicated count**: records whose `review_after` < today and no superseding record exists — the first machine check for the exact stale-claim bug class that motivated the staleness model.
- Superseded chains (and orphaned `superseded_by` references, which are findings).
- Refusal counts by `reason_code` from the log.
- Blocked/parked items awaiting operator decisions (Section 6).
- Consistency findings: record file whose name ≠ its `source_id`, non-deterministic serialization, index drift vs. a fresh rebuild.
- `--json` output is the shape the dashboard snapshot consumes (Section 7).

---

## 6. Blocked Item Handling (the C8 Repo-Path Decision)

The blocked question from the first admission review — *admit the canonical repo path as a `private`/`internal_reasoning_only` record, or decline because the committed `PROJECT_STATE.md` already serves the purpose?* — is an **operator input this spec cannot answer**. The implementation must represent such items honestly rather than letting them evaporate:

- The batch-manifest format includes a `blocked` item status carrying the verbatim operator question and its origin task. `preview` re-reports open blocked items on every run; `audit` counts them. A blocked item is never writable by `apply` in blocked state.
- When the operator answers (in a task instruction or `DECISIONS.md` entry), the answer resolves the item one of two ways, both through the normal pipeline: **(a)** admit — the item becomes an ordinary candidate in a new batch, goes through `preview`, receives its human decision, and is written by `apply` as a `private`/`internal_reasoning_only` record; or **(b)** decline — a decided record with `decision: rejected` and the operator's rationale is written, so the question is answered durably instead of lingering forever.
- **Recommendation to the operator** (decision still yours): decline (b). The provenance spec already treats machine-specific paths as `private`, the committed `PROJECT_STATE.md` line serves the reasoning need, and a `rejected` record documents the choice without duplicating private-shaped data into a second store.

---

## 7. Dashboard-Read Contract

For the future "Context" tab task (dashboard code remains out of scope here and in the gate spec). The UI may consume `ContextSource` data **only** under these rules:

1. **Read-only, local, live.** The dashboard reads committed files at page load (`INDEX.json`, `records/*.json`, `REFUSAL_LOG.jsonl`, `CONTRADICTION_LEDGER.md`) exactly like the existing tabs read `ROADMAP.md`/state files. No write action, no provider call, no network beyond `127.0.0.1` static file serving.
2. **Filter by `allowed_use` before opening records, using the index.** `INDEX.json` carries `allowed_use` precisely so the UI can decide what it may render without parsing record bodies:
   - `public_display` → may render claim text anywhere the site renders content.
   - `internal_summary_display` → may render claim text in the local dashboard only; never on a public/showcase page.
   - `internal_reasoning_only` → **must not be rendered at all** — not the claim, not the notes, not the `source_identity`. The UI may show only that N such records exist (count, no identity).
3. **Refusals are counts only**, grouped by `reason_code` — the log is already aggregate-safe, and the UI must not attempt to enrich it.
4. **Stale is flagged, not hidden**: records past `review_after` render with an explicit stale badge (mirroring the "stale is not false" rule), never silently dropped.
5. **Superseded records** render only behind an explicit history affordance, with the current record primary.
6. **Honest-data labeling**: anything not read live from committed files carries the existing `[MOCK]` label convention. The audit snapshot, if frozen, is labeled with its capture date like `site/data/dashboard_snapshot.json` today.
7. The dashboard never displays `notes` fields of any record regardless of `allowed_use` (they are reviewer-facing), and never displays any field of a `hidden`-equivalent or refused item.

---

## 8. Implementation Phases (Each a Separate, Explicitly Approved Task)

| Phase | Contents | Ships with |
|---|---|---|
| **I1** | `scripts/context_gate/` scaffold; `models.py` (`ContextSource` parse/validate); `validate-record`; `preview` with all R1–R9/warnings/parking/staleness/contradiction checks | Full unit-test suite for checks and outcomes (Section 9); no writes possible yet |
| **I2** | `apply` (write-once store, refusal log, gating), `--migrate-preview` migration of the six admitted records + refusal-log backfill + preview-store tombstone | Write-path tests; `MIGRATION_001.md`; canonical `README.md` |
| **I3** | `rebuild-index`, `audit` (+ `--json`) | Index determinism and audit-finding tests |
| **I4** | Dashboard "Context" tab per Section 7 | Separate task, per the gate spec's existing boundary |

Boundaries (unchanged from gate spec Section 15, restated as binding on all phases): standard library only; no network/MCP/database/scheduler/watcher; no auto-resolution of contradictions; no auto-expiry of stale records; no relaxation of R1/R2, the generated trust cap, or `allowed_use` no-loosening; no reads/writes under any forbidden path; no push from any phase.

---

## 9. Test Plan (For the Implementation Tasks)

`tests/test_context_gate_checks.py`, `tests/test_context_gate_store.py`, `tests/test_context_gate_tools.py`, plus `tests/context_gate_fixtures.py` — standard-library `unittest`, mirroring the `test_loop_ops_*` conventions (150 existing tests untouched). Minimum coverage:

**Checks (I1):**
- One test per refusal rule R1–R9, each with a passing twin (e.g. `generated`+`high` refused vs. `generated`+`medium` passing R6 — using synthetic fixture content only, never real secrets).
- Outcome precedence: an item triggering multiple classes lands on the highest-precedence outcome; assert exact ordering `REFUSE` > `CONTRADICTION_FOUND` > `NEEDS_HUMAN_REVIEW` > `ACCEPT_WITH_WARNINGS` > `ACCEPT`.
- Trust lookup table: all 8 `source_type` × `verification_state` cells; proposer suggestion above default → R6; at/below default → ignored in favor of computed.
- Each Section 6.1 warning condition fires, and only when its condition holds.
- Staleness both directions: missing `review_after` on `volatile` → R4; past `review_after` inbound → warning not refusal; stale-implicated flagging against a fixture store; staleness contagion.
- Contradiction: same-subject conflict vs. fixture store and within-batch; the loops-vs-runs near-miss encoded as a regression test asserting **no** contradiction; draft ledger entry text produced but nothing written.
- Parking conditions 1–5 each produce `NEEDS_HUMAN_REVIEW` with the specific stated question.

**Store (I2):**
- Write-once: identical-bytes re-apply is a no-op; single-byte difference refused; symlink/path-traversal/case-collision attempts refused (Windows case-insensitivity covered per `persist.py` precedent).
- Apply gating: missing/empty approval id, wrong expected HEAD, dirty tree, and any record missing a human decision field → refused, nothing written (assert directory bytes unchanged).
- Apply re-check: a manifest item that would violate R1 at apply time is refused even when flagged as previously previewed.
- Refusal-log writer: whitelisted keys only — passing a content-bearing key raises; JSONL append preserves prior lines byte-for-byte.
- Migration: field-value identity verification catches a tampered preview fixture; partial-failure leaves preview store untouched; second run is a no-op.

**Tools (I3):**
- `rebuild-index` determinism (two runs, identical bytes) and content policy (no claim/notes text anywhere in `INDEX.json`).
- `audit` counts against a synthetic store: stale-implicated, superseded chains, orphaned `superseded_by` finding, index-drift finding, blocked-item count.
- `validate-record` accepts every shipped canonical record (once migrated) — the "shipped registry" test pattern from `test_loop_ops_tools.py`.

**Global:** no test touches the network, writes outside a temp directory, or embeds a real secret-shaped value (fixtures use obviously fake placeholders that still trip the R1/R9 detectors).

---

## 10. What This Spec Does Not Authorize

- No code, module, test, or CLI exists or is created by this task — Sections 5, 8, and 9 describe future work requiring separate approval per phase.
- `shared_context/context_provenance/` still does not exist; the six admitted records remain in the preview location; the refusal log does not exist; `INDEX.json` does not exist.
- No dashboard code, tab, or field — Section 7 is a contract for a future task, not a change to `site/`.
- No scheduler, watcher, network, MCP, database, provider call, or push.
- No answer to the blocked C8 question — Section 6 gives a recommendation, but the decision remains the operator's.
- No change to the provenance spec, gate spec, ledger, or any admitted record.

---

## 11. Safety Notes

- All `[[../../shared_context/SAFETY_CONTRACT]]` rules apply unchanged. R1/R2 refusals, the generated-content trust cap, and `allowed_use` no-loosening remain hard constraints inherited from the two upstream specs; nothing in this implementation plan may weaken them, and Section 9 requires tests proving the implementation enforces them.
- The refusal log's structural whitelist (Section 4) exists so that aggregate-safety is enforced by the type system of the writer, not by reviewer vigilance.
- The migration is the only operation that ever removes a file from a provenance store, it is hash-verified, one-time, operator-approved, and leaves full git history — nothing else may delete or rewrite any record, log line, or ledger entry.

---

*This implementation specification is a docs-only artifact of `MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-SPEC-001`. It authorizes no code, directory, record, migration, index, dashboard change, or runtime — each implementation phase is a separate, explicitly approved future task.*
