# Context Ingestion Gate Spec

**Task ID:** MELLYCORE-CONTEXT-INGESTION-GATE-SPEC-001
**Version:** 1.0
**Status:** Draft specification (docs-only)
**Scope:** The validation gate every candidate context item must pass before it can become an admitted `ContextSource` record in Milestone B ("One Brain")

---

## 1. Purpose

`MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001.md` (commit `e7767d9`) defines *what* an admitted piece of context must carry: the `ContextSource` record, provenance and sensitivity labels, a trust-level lookup, staleness policy, and contradiction precedence guidance. This document defines the **ingestion gate** — the deterministic set of checks an admission request must pass, the outcomes those checks can produce, and the exact points where a human decision is mandatory.

The gate exists so that the provenance/sensitivity model is *enforced*, not merely documented. Without a gate, the model is a convention an agent could drift from; with a gate, every future context source — repo files, human statements, generated summaries, external references — passes through one auditable choke point before it can enter durable memory.

**This document authorizes no implementation.** No gate code, CLI, script, database, MCP server, backend, or dashboard change is created by this task. No `ContextSource` record exists yet and none is created here. This is a specification for future, separately approved tasks, following the project's established spec-before-code pattern (persistence review → persistence implementation; provenance spec → this gate spec → future gate exercise/implementation).

---

## 2. Relationship to Existing Docs

- `[[../specs/MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]` is the authority on the `ContextSource` record shape, label vocabularies, trust defaults, `allowed_use` matrix, staleness policies, and contradiction precedence. This gate spec **consumes** that model; it redefines none of it. Where this document says "per the provenance spec," the provenance spec wins on any conflict.
- `[[../../shared_context/SOURCE_INGEST_WORKFLOW]]` remains the human-gated process for graph fixtures; the provenance spec's Section 8 generalized it into an eight-step admission workflow. The gate specified here **is the machine-checkable portion of Steps 1–6** of that admission workflow. It does not replace Step 7 (human review) and never will — see Section 8 below.
- `[[../../shared_context/CONTRADICTION_LEDGER]]` remains the only destination for detected contradictions. The gate routes to it; it never resolves anything (Section 11).
- `[[../../shared_context/CONTEXT_PACK_GENERATOR_SPEC]]`'s allowlist/blocklist is a coarse path filter applied when a context pack is generated. The gate applies **after** that, per item, at the admission boundary — a file passing the pack generator's path filter still gets full gate validation before any claim from it is admitted.
- The write-once and dry-run-by-default conventions are deliberately reused from the proven loop-evidence system (`scripts/loop_ops/persist.py`'s `persist-run` contract): dry-run default, explicit apply gated on operator approval, write-once immutable artifacts, identical-bytes idempotent recovery. One immutability convention, not two.

---

## 3. Gate Position in the Admission Workflow

The provenance spec's Section 8 admission workflow, annotated with gate responsibility:

| Step | Action | Owner |
|---|---|---|
| 1. Collect | Identify source; hard refusal of `secret`/`regulated_high_risk`-shaped content | **Gate** (Section 7) |
| 2. Classify provenance | `source_type`, `verification_state` | Proposer supplies; **gate validates** (Section 5) |
| 3. Classify sensitivity | `sensitivity_level`, derived `allowed_use` | Proposer supplies; **gate validates** (Sections 7, 9) |
| 4. Classify staleness | `staleness_policy`, `review_after` | Proposer supplies; **gate validates** (Section 10) |
| 5. Compute default trust | `trust_level` from the lookup table | **Gate computes**; proposer may not exceed it (Section 7) |
| 6. Detect contradictions | Against admitted records and same-batch items | **Gate detects, routes to ledger** (Section 11) |
| 7. Human review | Confirm/override, resolve/defer contradictions, set `decision` | **Human only — never the gate** |
| 8. Publish | Commit write-once record | Human-approved apply only (Sections 12–13) |

The gate is everything mechanical before the human; it is never a substitute for the human.

---

## 4. Admissible Inputs (What May Request Admission)

An **admission request** is a batch of one or more **candidate items**, each proposing exactly one future `ContextSource` record. Only these input classes may request admission, mapping 1:1 to the provenance spec's `source_type` labels:

| Input class | `source_type` | Constraints |
|---|---|---|
| A direct human-operator statement, quoted or paraphrased with the operator's confirmation | `user_provided` | Must cite the conversation/task in `source_identity`. |
| Content read directly from a file or commit in this repository at proposal time | `repo_derived` | `source_identity` is a repo-relative path (plus commit hash where relevant). Never a path matching the refusal rules in Section 7. |
| An agent-produced summary, inference, or synthesis | `generated` | Must identify the producing agent/task in `proposed_by` and cite what it was derived from. |
| A dated summary of an external document/page already captured in this repo's docs (e.g. `docs/research/` inspiration summaries) | `externally_sourced` | Never a live authenticated fetch; never a URL requiring credentials. The external content must already exist as a committed, dated summary — the gate takes no network action. |

Anything not in this table cannot request admission. In particular: raw binary files, database files, screenshots/HAR archives, chat logs containing third-party personal data, and anything sourced from the MellyTrade workspace are not admissible input classes at all.

A batch is the unit of gate execution; each item in it receives its own independent outcome (Section 6). One refused item never blocks the rest of the batch, except when the refusal reason is a batch-level violation (e.g. the batch manifest itself is malformed).

---

## 5. Required Metadata (No Admission Request Without It)

Every candidate item must arrive with all proposer-supplied `ContextSource` fields from the provenance spec Section 3 already filled in:

- `source_id` (proposed; gate verifies uniqueness against existing records and the same batch)
- `source_identity`
- `source_type` and `verification_state`
- `sensitivity_level` and derived `allowed_use`
- `captured_at`
- `staleness_policy`, plus `review_after` when the policy is `volatile` or `periodic_review`
- `proposed_by`
- the claim text itself (what is actually being asserted), and
- `notes` (optional, but if present, subject to the same no-secrets field rule)

The gate computes `trust_level` from the lookup table itself (Step 5); a proposer-supplied `trust_level` is treated as a *suggestion* and ignored where it exceeds the computed default (Section 7, rule R6).

**Missing or malformed required metadata is a validation failure, not a prompt for the gate to guess.** The item is returned as `REFUSE` with reason `incomplete_metadata` and may be resubmitted complete. The gate never infers `sensitivity_level`, never defaults `staleness_policy`, and never backfills `captured_at` — silent defaults are exactly how untracked context would leak in.

---

## 6. Validation Outcomes

Every candidate item receives exactly one of five outcomes, evaluated in this precedence order (first match wins):

| Outcome | Meaning | Terminal? |
|---|---|---|
| `REFUSE` | The item violates a hard rule (Section 7) or is structurally invalid. It cannot proceed to human review in this form. | Yes, for this submission. A corrected resubmission is a new item. |
| `CONTRADICTION_FOUND` | The item's claim conflicts with an admitted record or another same-batch item. A draft `[[../../shared_context/CONTRADICTION_LEDGER]]` entry is produced; the item is blocked until a human resolves or defers that entry. | No — parked pending human ledger action. |
| `NEEDS_HUMAN_REVIEW` | The item passed the hard rules but contains a condition the gate must not decide alone (Section 8). | No — parked pending human decision. |
| `ACCEPT_WITH_WARNINGS` | The item passed all checks but carries non-blocking warnings (Section 6.1) the human reviewer must see. | No — eligible for Step 7 review, warnings attached. |
| `ACCEPT` | The item passed every check cleanly. | No — eligible for Step 7 review. |

**`ACCEPT` never means admitted.** Per the provenance spec, no record reaches `decision: admitted` without a human reviewer (`reviewed_by` non-null). `ACCEPT` and `ACCEPT_WITH_WARNINGS` mean only "eligible to be presented for the human decision" — the gate's outcome is a validation verdict, never an admission. Conversely, `REFUSE` **is** binding on the machine side: an item the gate refuses cannot be hand-waved into memory without either correcting the item or amending this spec through a reviewed docs task.

### 6.1 Warning conditions (`ACCEPT_WITH_WARNINGS`)

- `captured_at` older than 30 days at proposal time for a `volatile` item.
- `review_after` already in the past at proposal time (the item is proposing itself pre-stale — legal, but the reviewer must see it).
- An `allowed_use` proposed *stricter* than the default matrix (legal per the provenance spec, but flagged so the rationale gets reviewed).
- The claim references another `ContextSource` that is itself past its `review_after` date (staleness contagion — see Section 10).
- `verification_state: verified` asserted without a stated verification method in `notes` or the claim body.

---

## 7. Immediate Refusal Rules (`REFUSE`)

These are evaluated first, fail fast, and are not human-overridable at gate level. R1 and R2 restate the provenance spec's Section 5.1 hard rules; the rest are gate-specific enforcement.

| # | Rule | Reason code |
|---|---|---|
| R1 | `sensitivity_level: secret`, or content that is secret-*shaped* regardless of proposed label: credentials, API keys, tokens, `.env` values, account identifiers, private keys, connection strings. The refusal record logs the *category* detected, never the value. | `secret_content` |
| R2 | `sensitivity_level: regulated_high_risk`, or content that is regulated-shaped: brokerage/trading account data, trade history, health/legal/PII-adjacent material. Default `rejected` per the provenance spec; no admission path exists until a separate approval process is specified. | `regulated_high_risk` |
| R3 | `source_identity` or claimed origin inside a forbidden path: `**/MellyTrade/**`, `**/mellytrade/**`, `.env*`, credential/token files, `db/*.db`, or any path on `[[../../shared_context/CONTEXT_PACK_GENERATOR_SPEC]]`'s blocklist or `LOOP_REGISTRY.json`'s `global_forbidden_paths`. | `forbidden_path` |
| R4 | Required metadata missing or malformed (Section 5), including a `volatile`/`periodic_review` item without `review_after`. **A missing staleness policy is a refusal, never a default.** | `incomplete_metadata` |
| R5 | Proposed `allowed_use` looser than the provenance spec's default matrix for the proposed `sensitivity_level`. Loosening is never a gate-level act — it requires re-classifying sensitivity itself under human review. | `allowed_use_loosening` |
| R6 | Proposed `trust_level` exceeding the computed default — most importantly, **any `generated` item proposing `trust_level: high`**. The generated-content trust cap (`generated` defaults to `medium` at best, never `high`) is enforced mechanically here; only a human reviewer at Step 7 may raise trust above the default, with a stated rationale, and the gate never pre-approves that. | `trust_cap_violation` |
| R7 | A `source_id` colliding with an existing record or another item in the same batch (write-once protection at the identifier level). | `id_collision` |
| R8 | An input class outside Section 4's table (e.g. a live URL fetch, a binary, MellyTrade-workspace content). | `inadmissible_input_class` |
| R9 | Secret-shaped or forbidden content detected inside `notes`, `decision_rationale` (if pre-filled), or the claim text itself — the field-level no-secrets rule applied to every free-text field, matching `[[../../shared_context/CONTEXT_GRAPH_SCHEMA]]` Section 6. | `field_level_secret` |

A `REFUSE` outcome is itself recorded (Section 12) as an aggregate-countable event: reason code, date, `proposed_by` — **never** the refused content, and for R1/R9 never the `source_identity` either if the identity itself would leak what was found.

---

## 8. What Requires Human Approval (`NEEDS_HUMAN_REVIEW` and Step 7)

Two distinct layers, deliberately kept separate:

**Layer 1 — everything.** Every item that survives the gate still requires the provenance spec's Step 7 human review before `decision: admitted`. This is unconditional and this spec adds no bypass. The gate has no authority to admit.

**Layer 2 — conditions the gate must park explicitly (`NEEDS_HUMAN_REVIEW`)** rather than passing along as a clean `ACCEPT`:

1. `sensitivity_level: private` — admission of private material is legal but must never ride through on a default; a human confirms both the classification and that `internal_reasoning_only` use is genuinely needed.
2. Any proposed override: trust above default (with rationale), sensitivity classification the proposer marks uncertain, or a re-dating of an existing record's `review_after`.
3. `externally_sourced` items whose underlying dated summary is older than 90 days (freshness of the external world cannot be machine-verified here).
4. An item that would supersede an existing admitted record (`superseded_by` chains are history-changing; a human confirms the succession).
5. Borderline sensitivity: any item where the gate's mechanical checks and the proposer's label disagree in the *stricter* direction (e.g. proposer says `public` but the content matches an `internal`-shaped pattern such as task-internal rationale). The gate never silently upgrades or downgrades sensitivity — it parks the item and states the discrepancy.

For every parked item the gate must state *which* condition triggered parking, so the human reviews a specific question, not a vague flag.

---

## 9. Acceptance by Sensitivity Level

For items that clear Sections 7–8, the gate validates the proposed `sensitivity_level` against these criteria before the item can carry it into review:

| Level | Gate acceptance criteria |
|---|---|
| `public` | Content is already public in substance (README/showcase copy, published docs) or is generic architectural description containing no operator-specific paths, names, or internal task detail. Default `allowed_use: public_display`. |
| `internal` | Project-internal material: task docs, design rationale, run evidence summaries, roadmap state. Safe for the dashboard and shared_context, not for a public artifact. Default `allowed_use: internal_summary_display`. |
| `private` | Operator-specific or machine-specific detail (local paths with usernames, personal configuration). Always parked `NEEDS_HUMAN_REVIEW` (Section 8); if admitted, locked to `allowed_use: internal_reasoning_only`. |
| `secret` | Never accepted — R1. |
| `regulated_high_risk` | Never accepted — R2. |

---

## 10. Stale-Claim Detection

Motivated by the same two real bugs the provenance spec cites (`PROJECT_STATE.md`'s stale HEAD line, twice). The gate checks staleness in both directions:

- **Inbound:** every `volatile`/`periodic_review` item must carry `review_after` (R4). A `review_after` already in the past is a warning (Section 6.1), not a refusal — proposing known-stale history is legal if labeled honestly.
- **Against the existing store:** when a new item's claim concerns the same subject as an admitted record whose `review_after` has passed, the gate flags the existing record as **stale-implicated** in its report. It does not auto-expire, delete, or supersede the old record — stale is not false. The human reviewer decides: re-verify and re-date the old record, supersede it via the new item, or log a contradiction if the two actively conflict.
- **Staleness contagion:** an item whose claim depends on a stale-implicated record gets `ACCEPT_WITH_WARNINGS` at best, so confidence chains stay honest.

The count of stale-implicated records is a first-class dashboard signal (Section 14), so staleness stops being caught only by manual review.

---

## 11. Contradiction Routing

When a candidate item's claim conflicts with an admitted `ContextSource` record or another item in the same batch:

1. The item's outcome is `CONTRADICTION_FOUND`.
2. The gate produces a **draft** `[[../../shared_context/CONTRADICTION_LEDGER]]` entry (claim A, claim B, source refs, proposed severity) in its report. In dry-run/preview mode (Section 13) the draft appears only in the report — the ledger file is not written. The ledger entry is written only on a human-approved apply.
3. The gate **never resolves** the contradiction. Not by trust level, not by recency, not by the provenance spec's Section 7 precedence guidance — that guidance exists to help the *human* decide faster and may be cited inside the human's `resolution_decision`, but `status: resolved` is set only by a human, exactly as the ledger already requires.
4. The item remains blocked until the ledger entry is resolved or explicitly deferred by the reviewer; a deferral leaves the item `deferred`, never silently admitted alongside an open contradiction about its own claim.

---

## 12. Provenance Recording and the Write-Once `ContextSource` Artifact

How an admission (or refusal) is durably recorded, reusing the loop-evidence conventions verbatim rather than inventing new ones:

- **On-disk home (future):** one file per record under a future `shared_context/context_provenance/` directory — e.g. `shared_context/context_provenance/records/ctx-YYYY-MM-DD-<slug>.json` — created only by a future, separately approved implementation task. This spec names the location so future work converges, but creates neither the directory nor any file.
- **Write-once:** once a record carries a `decision`, its file is immutable. A re-submitted identical byte-for-byte write is idempotent recovery (allowed, no-op); any differing write to an existing record file is refused — the same identical-bytes rule `persist-run` already enforces for run evidence. Changes happen only by writing a **new** record with a new `source_id` and setting `superseded_by` on the old one.
- **Record shape:** exactly the provenance spec's Section 3 `ContextSource` fields. The gate adds a small audit block, not new semantics: `gate_spec_version`, `validation_outcome`, `warnings[]` (reason codes only), and `validated_at`.
- **Refusal log:** refusals are recorded as aggregate-safe entries (date, reason code, `proposed_by`) in a separate append-only refusal log in the same future directory — never the refused content, per Section 7. This is what feeds the "sensitive items blocked" dashboard count without leaking what was blocked.
- **Every admitted record's `decision_rationale` is required** — including obvious admissions — per the provenance spec, so the gate's report template must carry a rationale field the human fills at Step 7; the gate never auto-fills it.

---

## 13. Dry-Run / No-Write Preview Mode, Then Apply

Mirroring `persist-run` exactly:

- **Preview (dry-run) is the default and, for now, the only mode.** A gate pass in preview mode reads inputs, evaluates every check, and emits a full report — per-item outcomes, reason codes, warnings, draft ledger entries, draft record contents — and **writes nothing**: no record file, no ledger entry, no refusal-log entry, no state change anywhere in the repository.
- **Apply is a future capability, not authorized here.** When a future task implements it, apply must require, at minimum: an explicit `--apply` flag, a non-empty operator approval identifier, an expected-HEAD check matching the repository's actual current HEAD, and the human Step 7 decisions already recorded for every item being written. Preview-then-apply must be two separate invocations — never one step.
- A preview report is a conversation/report artifact only. If a preview report itself is worth keeping, committing it is an ordinary human-reviewed docs commit, not a gate write.
- No batch may go from raw proposal to committed records in one automated motion, ever. The human review sits between preview and apply by construction.

---

## 14. Dashboard Signals (Specification Only — No Code Written)

Extends the provenance spec's Section 9 future "Context" tab with gate-status fields. Same pattern as the existing dashboard: real data read live from committed files, mock data explicitly labeled, no provider calls. Nothing here is built by this task.

| Signal | Meaning | Data source (once records exist) |
|---|---|---|
| **Gate outcomes to date** | Cumulative counts by outcome (`ACCEPT`, `ACCEPT_WITH_WARNINGS`, `REFUSE`, `NEEDS_HUMAN_REVIEW`, `CONTRADICTION_FOUND`). | Record files' audit blocks + the refusal log. |
| **Pending human review** | Items parked `NEEDS_HUMAN_REVIEW` or `CONTRADICTION_FOUND` not yet decided. | Records with `decision` still unset / open ledger entries. |
| **Refusals by reason code** | Aggregate counts per Section 7 reason code — never content, never identity for R1/R9. | The append-only refusal log. |
| **Stale-implicated records** | Admitted records past `review_after` and flagged by a gate pass, not yet re-verified. | Computed from record files vs. current date. |
| **Last gate pass** | Date and mode (preview/apply) of the most recent gate execution. | Most recent gate report/audit block. |
| **Ledger link-through** | Open vs. resolved contradiction counts, already specified in the provenance spec's Section 9 — displayed adjacent so gate status and ledger status read as one story. | `CONTRADICTION_LEDGER.md`, parsed live. |

---

## 15. Future Implementation Boundaries

What a future, separately approved implementation task may and may not do. These boundaries are part of this spec's contract; an implementation that exceeds them requires a new reviewed spec, not an in-flight decision:

**May:**
- Implement the gate as a standard-library-only, read-only-by-default CLI under `scripts/` (the `loop_ops` pattern), with preview as default and apply gated per Section 13.
- Create `shared_context/context_provenance/` with the record and refusal-log layout from Section 12.
- Add automated tests following the existing `tests/test_loop_ops_*` conventions.
- Add the Section 14 dashboard fields to `site/dashboard.html`'s existing tab pattern in a separate, explicitly scoped task.

**May not (without a new reviewed spec):**
- Run unattended: no scheduler, file watcher, cron, or continuous ingestion trigger.
- Touch the network: no fetches, no authenticated APIs, no MCP server, no provider/model calls from the gate itself.
- Write to any database or add any dependency.
- Auto-resolve contradictions, auto-expire stale records, auto-fill `decision`/`decision_rationale`/`reviewed_by`, or raise any trust level.
- Relax R1/R2 refusal, the generated-content trust cap, or the `allowed_use` no-loosening rule — the provenance spec marks these as hard constraints requiring their own explicitly approved spec to change.
- Read from or write to any forbidden path (R3), including anything in the MellyTrade workspace.

---

## 16. What Remains Intentionally Unimplemented

- No gate code, CLI, script, or test exists. This document is the checks' specification, not their implementation.
- No `ContextSource` record, `shared_context/context_provenance/` directory, or refusal log has been created.
- No contradiction ledger entry has been written — the ledger still has no live entries.
- No dashboard tab, panel, or field from Section 14 has been built; `site/` is untouched.
- No apply mode exists anywhere, in any form.
- No approval process for `regulated_high_risk` content has been defined (unchanged gap from the provenance spec; the safe default remains refusal).

---

## 17. Safety Notes

- Every rule in `[[../../shared_context/SAFETY_CONTRACT]]` applies unchanged; nothing here loosens any existing constraint.
- The R1/R2 refusals and the generated-content trust cap are restatements of the provenance spec's hard constraints — this spec inherits, and may not weaken, them.
- Gate reports, refusal logs, and record fields must never contain secret values, credentials, `.env` contents, or account identifiers — including in "what was refused" messages, which carry category codes only.
- The gate extends the `**/MellyTrade/**` boundary already enforced by `LOOP_REGISTRY.json`'s `global_forbidden_paths` to context admission, keeping one consistent boundary at every layer.

---

*This specification is a docs-only artifact of `MELLYCORE-CONTEXT-INGESTION-GATE-SPEC-001`. It authorizes no gate implementation, database, API, MCP, dashboard, scheduler, or runtime — every future admission remains a human-reviewed, docs-only action until a separate, explicitly approved task changes that.*
