# MellyCore AI Operations Intelligence Spec

**Task ID:** MELLYCORE-AI-OPERATIONS-INTELLIGENCE-001
**Version:** 1.0
**Status:** Draft specification (documentation-only). No runtime, backend, adapter, UI, scheduler, provider integration, or production schema is authorized or created by this document.
**Scope:** The logical contracts for MellyCore AIOS *AI Operations Intelligence* — the AI Estate Inventory, Unified Run Ledger, Skill Gap Detector, Memory Freshness Monitor, Recommendation Ledger, operator-approval contract, and the controlled improvement loop that connects them — expressed as specification only.

---

## 1. Status, Purpose, and Truthfulness

### 1.1 Specification status

This document is a **specification**, not an implementation. It defines logical records, states, transitions, and requirements that a *future, separately approved* implementation task MUST satisfy. It creates no backend, database, runtime adapter, UI, scheduler, provider integration, autonomous agent, execution engine, production JSON Schema, or runtime-consumed configuration. Every enum, record, and payload below is a **logical contract**, not a declared runtime type, and MUST NOT be read as evidence that any corresponding code exists.

### 1.2 Documentation-only scope

Following this project's established spec-before-code pattern (Loop Operations Foundation → persistence review → persistence implementation; Context provenance/sensitivity spec → future gate; Knowledge Graph spec package → static UI), this task produces documentation and shared-context updates only. The exact next task, `MELLYCORE-OPERATIONS-DATA-CONTRACT-001` (Section 16), translates these logical contracts into fixture/schema artifacts and validation requirements — still without runtime execution.

### 1.3 Product purpose

MellyCore AIOS is a **local-first, operator-controlled AI Operations Observatory**. Its purpose is to make models, agents, runs, context, memory, recommendations, approvals, and validation results **visible, inspectable, provenance-aware, truthful about freshness and completeness, approval-gated, and auditable**. AI Operations Intelligence is the layer that turns raw operational evidence into inventory, ledgers, gap analysis, freshness signals, and recommendations — without ever acting on them itself.

### 1.4 Intended operator

The intended user is a single technical **operator** (the repository owner) running MellyCore locally. The operator is the sole authority for consequential action. Every consequential transition in this specification terminates at an explicit operator decision. There is no second privileged role that can substitute for the operator, and no system component may act as the operator.

### 1.5 Current implemented foundations

The following exist in the repository today and MAY be referenced as `IMPLEMENTED` (see Section 1.9):

- **Loop Operations Foundation** — report-only, nine registered loops, deterministic circuit breaker, immutable per-run ledgers, no scheduler, no write path (`[[../architecture/MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001]]`).
- **Context Gate through I4** — guarded admission, canonical write-once provenance records, content-free index, computed audit, and a read-only dashboard Context surface (`[[MELLYCORE_CONTEXT_GATE_IMPLEMENTATION_SPEC_001]]`, `[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]`).
- **Run/token/persistence contract** — `[[../../shared_context/loops/RUN_LEDGER_SCHEMA]]` and `[[../../shared_context/loops/LOOP_STATE_SCHEMA]]`, with measured-token honesty already enforced in Python.
- **Static local surfaces** — homepage and the legacy Live Cockpit V2 prototype.
- **Human-invoked evidence** — two persisted `project-health` runs; no loop is `production_enabled`.

### 1.6 Planned capabilities

The AI Estate Inventory, Unified Run Ledger (cross-domain), Skill Gap Detector, Memory Freshness Monitor, Recommendation Ledger, Approval Queue execution surface, and Observatory UI modules described here are **`SPECIFIED` or `PLANNED`**. None is implemented. Naming a capability in this document does not authorize or claim its implementation.

### 1.7 Explicit non-claim of runtime implementation

This specification explicitly does **not** claim that any of the following exist: an inventory backend, a cross-domain run-ledger store, an automatic analyzer, a recommendation engine, an approval executor, a skill installer, a memory refresher, a provider adapter, a scheduler, or any UI beyond the existing static/legacy surfaces. Where this document uses present-tense normative verbs ("the record contains", "the monitor distinguishes"), those describe the **contract a future implementation must meet**, not a running system.

### 1.8 Authoritative source hierarchy

When this document and another source appear to conflict, precedence is, strongest first:

1. Explicit operator instruction in the current task.
2. `[[../../shared_context/SAFETY_CONTRACT]]` and `[[../safety/MELLYCORE_LOOP_SAFETY_CONTRACT_001]]`.
3. The enforced Python contracts: `[[../../shared_context/loops/RUN_LEDGER_SCHEMA]]`, `[[../../shared_context/loops/LOOP_STATE_SCHEMA]]`, and the Loop Operations validators/guard/readiness modules.
4. `[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]` and the Context Gate specs.
5. `[[../architecture/MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001]]`.
6. Canonical positioning in `[[../../shared_context/PROJECT_STATE]]`, `[[../../shared_context/ROADMAP]]`, `[[../../README]]`.
7. This specification.

This document **defers** to items 2–5 and MUST NOT redefine them incompatibly. Where it needs their concepts, it references them.

### 1.9 Truthful-state labels (glossary)

Every record and every Observatory surface MUST classify each datum with exactly one of the following truthful-state labels. These labels are the semantic layer beneath the Holographic UI spec's visible `Real source` / `Simulated model output` / `Planned` labels (`[[MELLYCORE_HOLOGRAPHIC_UI_SPEC_001]]`) and do not replace them.

| Label | Meaning |
|---|---|
| `IMPLEMENTED` | Exists in the repository and is exercised or directly readable today. |
| `LEGACY_PROTOTYPE` | Historical prototype/demo code retained as evidence; not current product direction (e.g. the NASA Images browser demo). |
| `SPECIFIED` | Defined by an accepted specification; not implemented. |
| `PLANNED` | Named on the roadmap; not yet specified in full or implemented. |
| `SIMULATED` | Deterministic local placeholder/demo content; carries its label and is never presented as live. |
| `UNAVAILABLE` | A source that should exist could not be reached or read at observation time. |
| `DEGRADED` | Partially available; some fields present, others missing or unverified. |
| `STALE` | Was valid but has passed its freshness/review boundary and has not been re-verified. |
| `UNKNOWN` | No value is known; explicitly distinct from zero, empty, or false. |
| `ERROR` | Processing failed; the datum could not be produced or parsed. |

**Truthfulness rule (normative):** The UI and records MUST NOT silently present `PLANNED`, `SIMULATED`, `STALE`, or `UNKNOWN` data as live verified state. Any surface that renders such data MUST show its label.

### 1.10 Additional glossary

- **Observation** — a recorded fact derived from evidence. Carries no proposed action.
- **Analysis** — an interpretation of one or more observations. Carries no proposed action.
- **Recommendation** — a proposed consequential action, with evidence, awaiting an operator decision.
- **Approval** — an operator's scoped, digest-bound, time-limited authorization for a specific recommendation.
- **Implementation** — the act, performed only under a valid approval, that changes something.
- **Validation** — independent confirmation that an implementation did what was approved.
- **Record** — the append-oriented, provenance-bearing evidence of any of the above.
- **Estate asset** — a model, agent, skill, tool, or governed surface available to MellyCore.

An observation is not a recommendation. A recommendation is not an approval. An approval is not proof of implementation. Implementation is not proof of validation. Validation is not permission to merge or deploy.

---

## 2. System Principles and Invariants

The following invariants are normative and apply to every contract in this document.

1. **Local-first.** All records live in the local repository as reviewable artifacts. No external service is required to read operational truth.
2. **Operator control.** Every consequential transition terminates at an explicit operator decision (Section 9).
3. **Least privilege.** A component receives only the access its stated purpose requires. Read scope is the default; write authority is never implied.
4. **Read-only first.** Observation, analysis, inventory, freshness, and gap detection MUST be read-only. They MUST NOT mutate the repository, the estate, memory, or any external system.
5. **Append-only evidence.** Ledgers (run, recommendation) and provenance records are append-oriented; history is corrected by supersession, never by silent in-place rewrite (Section 13).
6. **Explicit provenance.** Every record carries where it came from and how trustworthy it is (Section 10). A record with no provenance is `UNKNOWN`, not trusted.
7. **Explicit null/unknown semantics.** `UNKNOWN`, absent, zero, empty, and false are distinct and MUST NOT be collapsed. "Not measured" is never rendered as "zero".
8. **Deterministic validation.** Validation and guard decisions MUST be reproducible from the same inputs, without calling a model or a network (mirrors `[[../architecture/MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001]]` §4.9).
9. **No silent fallback.** A missing or failed input yields an explicit `UNAVAILABLE`/`DEGRADED`/`ERROR` state, never a fabricated success.
10. **No implicit approval.** Absence of a "no" is not a "yes". Approval exists only as an explicit, valid approval record (Section 9).
11. **No self-elevation.** No component may grant itself permission, widen its own scope, or raise its own trust level.
12. **No autonomous safety-policy changes.** Safety rules (`[[../../shared_context/SAFETY_CONTRACT]]`, `[[../safety/MELLYCORE_LOOP_SAFETY_CONTRACT_001]]`) may be changed only by the operator through a separately approved task, never by this system.
13. **No autonomous push, merge, deployment, or branch deletion.** These require explicit, separate, per-action operator authorization.
14. **No repository-stored provider secrets.** Authentication metadata records only mode/availability, never a key, token, cookie, password, or private key (Sections 4, 14).
15. **No trading operations.** MellyCore AIOS is separate from MellyTrade; no broker, order, trade, or `regulated_high_risk` financial runtime behavior is in scope (mirrors the `**/MellyTrade/**` boundary in the loop registry and provenance spec §5.1).
16. **Recommendation is not execution.** Producing, storing, or displaying a recommendation never causes it to be carried out.

---

## 3. Controlled Loop State Machine

The controlled improvement loop is the backbone that connects observation to record. Its canonical lifecycle is:

```
observe → analyze → recommend → (approve | reject) → implement → validate → record
```

### 3.1 Stages

| Stage | Responsible actor | Required input | Required output/evidence | Permitted next |
|---|---|---|---|---|
| `OBSERVED` | System (read-only) | Evidence refs (runs, context, estate) | Observation record + provenance | `ANALYZED`, `CANCELLED`, `EXPIRED` |
| `ANALYZED` | System (read-only) | ≥1 observation | Analysis summary + evidence linkage | `RECOMMENDED`, `CANCELLED`, `EXPIRED` |
| `RECOMMENDED` | System (read-only) | Analysis | Recommendation record (Section 8) | `APPROVED`, `REJECTED`, `EXPIRED`, `SUPERSEDED`, `CANCELLED` |
| `APPROVED` | **Operator** | Recommendation + approval record (Section 9) | Approval record bound to digest | `IMPLEMENTING`, `EXPIRED`, `CANCELLED` |
| `REJECTED` | **Operator** | Recommendation | Rejection reason | *(terminal; re-observation may create a new recommendation)* |
| `IMPLEMENTING` | Operator or separately authorized executor | Valid, non-expired approval | Implementation refs | `IMPLEMENTED`, `FAILED`, `CANCELLED` |
| `IMPLEMENTED` | as above | Implementation refs | Evidence of the change | `VALIDATING` |
| `VALIDATING` | **Independent** validator | Implementation evidence | Validation attempt record | `VALIDATED`, `FAILED` |
| `VALIDATED` | Independent validator | Passing validation | Validation refs | `RECORDED` |
| `FAILED` | any | Failure evidence | Failure record + `error_signature` | `RECOMMENDED` (new attempt) or terminal |
| `RECORDED` | System | Full evidence chain | Immutable, append-only closure | *(terminal)* |

### 3.2 Terminal and failure states

Terminal states are `REJECTED`, `EXPIRED`, `CANCELLED`, `SUPERSEDED`, and `RECORDED`. `FAILED` is a recoverable failure state: it may lead to a *new* recommendation/attempt but MUST NOT be relabeled as success.

### 3.3 Semantics

- **Retry** — a failed attempt does not silently resume; it produces a new attempt with a strictly increasing index and its own evidence (mirrors run-ledger `iterations` append-only rule).
- **Cancellation** — the operator may cancel any non-terminal item; cancellation is recorded, not deleted.
- **Expiry** — a recommendation or approval past its `expires_at` transitions to `EXPIRED`; expiry is evaluated deterministically against a stated clock (Section 10.10).
- **Idempotency** — the same observed evidence MUST NOT create duplicate active recommendations (Section 8 deduplication); replaying an event MUST NOT advance state twice.
- **Correlation** — every item carries a stable `correlation_id` linking observation → analysis → recommendation → approval → implementation → validation → record.
- **Operator gates** — the `RECOMMENDED → APPROVED` and any deploy/merge transition are operator gates; a system component MUST NOT perform them.

### 3.4 Prohibited transitions (normative)

The following transitions MUST be refused:

- `OBSERVED → IMPLEMENTING`
- `ANALYZED → IMPLEMENTING`
- `RECOMMENDED → IMPLEMENTING` without an exact, valid, non-expired approval (Section 9)
- `APPROVED → COMPLETED/RECORDED` without both implementation evidence and validation evidence
- `FAILED → VALIDATED/RECORDED` without a new validated attempt
- `REJECTED → IMPLEMENTING`
- `EXPIRED` (recommendation or approval) `→ IMPLEMENTING`
- any `* → APPROVED` performed by a non-operator actor
- any transition that widens the approved scope beyond the approval's `authorized_actions`/`target_digest`

A future implementation MUST express this map as an explicit allowed-transition table enforced deterministically, in the spirit of `ALLOWED_TRANSITIONS` in the loop validators.

---

## 4. AI Estate Inventory

A single, read-only inventory of the AI assets and tools available to MellyCore: models, agents, skills, tools, and governed surfaces.

### 4.1 Logical record

**ILLUSTRATIVE — logical fields, not a runtime type.** Required fields (minimum):

| Field | Type | Notes |
|---|---|---|
| `asset_id` | string | Stable unique identifier (Section 4.2). |
| `schema_version` | string | Contract version of this record. |
| `provider` | string | Normalized provider identity (Section 4.3). |
| `model` | string \| null | Normalized model identity; `null`/`UNKNOWN` if not a model asset. |
| `plan` | string \| null | Plan/tier label if known; else `UNKNOWN`. |
| `authentication_mode` | enum | Mode only; never a credential value (Section 4.6). |
| `purpose` | string | What role this asset serves (routing role, tool function). |
| `cost_class` | enum | Section 4.7. |
| `capabilities` | array | Controlled capability vocabulary (Section 4.4). |
| `status` | enum | Section 4.8. |
| `last_validated_at` | date \| null | When availability/capability was last confirmed; `null` = never. |
| `allowed_projects` | array | Projects this asset may serve (Section 4.5). |
| `provenance` | object | Where this record came from (Section 10). |
| `evidence_refs` | array | Immutable references to supporting evidence. |
| `freshness_state` | enum | `FRESH` / `EXPIRING` / `STALE` / `UNKNOWN` (Section 7). |
| `created_at` | date | Record creation. |
| `updated_at` | date | Last metadata update (supersession-aware). |

### 4.2 Stable identifier rules

`asset_id` MUST be stable across re-observation and MUST NOT encode volatile data (status, timestamps). A change of provider or model identity produces a **new** `asset_id`; the prior record is retired (Section 4.9), not mutated.

### 4.3 Provider/model normalization

Provider and model strings MUST be normalized to a documented canonical form (e.g. casing, vendor aliases) so the same asset is not double-counted. Normalization rules are data, defined in the next task's contract; unresolved forms are `UNKNOWN`, never guessed.

### 4.4 Capability vocabulary

`capabilities` MUST draw from a controlled vocabulary (e.g. `text_generation`, `code`, `reasoning`, `review`, `vision`, `tool_use`, `embedding`). An unrecognized capability is recorded as `UNKNOWN` rather than invented. Capability claims MUST be evidence-backed or marked `UNVALIDATED`.

### 4.5 Allowed-project semantics

`allowed_projects` enumerates the projects an asset may serve. It MUST honor the MellyTrade boundary: no estate asset is `allowed` for trading/broker runtime use. An empty `allowed_projects` means the asset is inventoried but not authorized for any project — not "authorized for all".

### 4.6 Authentication metadata (hard rule)

`authentication_mode` describes **only** the authentication mode or credential-availability state. It MUST NOT contain API keys, access tokens, refresh tokens, cookies, private keys, passwords, or any raw secret value. Suggested logical enum: `NONE`, `ENV_REFERENCE`, `OS_CREDENTIAL_STORE`, `CLI_SESSION`, `MANAGED_IDENTITY`, `EXTERNAL_OPERATOR_SESSION`, `UNKNOWN`. These are logical labels, not implemented runtime types.

### 4.7 Cost class

Suggested logical enum: `FREE`, `TRIAL`, `METERED`, `SUBSCRIPTION`, `LOCAL_COMPUTE`, `UNKNOWN`. `cost_class` is a coarse classification and is distinct from measured run cost (Section 5).

### 4.8 Status and transitions

Suggested logical enum: `AVAILABLE`, `DEGRADED`, `UNAVAILABLE`, `UNVALIDATED`, `RETIRED`, `UNKNOWN`. A newly inventoried asset is `UNVALIDATED` until confirmed. Status MUST NOT be inferred from a weaker signal (presence of a record does not imply `AVAILABLE`). Every non-`AVAILABLE` status SHOULD carry a stated reason.

### 4.9 Retirement, replacement, duplicates, provenance priority

- **Retirement/replacement** — a retired asset's record is preserved with `status: RETIRED` and, when applicable, a pointer to its replacement.
- **Duplicate handling** — two records normalizing to the same asset identity are a duplication finding; the inventory MUST deduplicate to a single active record, retaining the others as history.
- **Provenance priority** — when sources disagree, precedence follows Section 10.4 (higher `trust_level`, `repo_derived` over `generated`); ties are not auto-resolved but flagged.
- **Unknown values** — any unknown field is `UNKNOWN`/`null`, never a placeholder that reads as real.

---

## 5. Unified Run Ledger

A normalized, append-oriented record for every agent/model task execution across domains. It **generalizes** the existing loop run ledger; it MUST preserve, and MUST NOT contradict, `[[../../shared_context/loops/RUN_LEDGER_SCHEMA]]` and `[[../../shared_context/loops/LOOP_STATE_SCHEMA]]`.

### 5.1 Logical record

**ILLUSTRATIVE — logical fields, not a runtime type.** Required fields (minimum):

| Field | Type | Notes |
|---|---|---|
| `schema_version` | string | Contract version. |
| `run_id` | string | Stable unique run identity (compatible with the existing run-ledger `run_id` form). |
| `task_id` | string | The task/loop this run served. |
| `agent` | string | Actor that performed the run. |
| `model` | string \| null | Model used, normalized (Section 4.3); `null`/`UNKNOWN` if not applicable. |
| `provider` | string \| null | Provider, normalized. |
| `started_at` | timestamp | UTC/RFC3339 (Section 5.4). |
| `completed_at` | timestamp \| null | `null` for an incomplete run. |
| `input_tokens` | integer \| null | Measured only (Section 5.2). |
| `output_tokens` | integer \| null | Measured only. |
| `cache_read_tokens` | integer \| null | Measured only. |
| `estimated_cost` | object \| null | Section 5.3. |
| `files_changed` | array | Normalized change list (Section 5.5). |
| `validator_results` | array | Section 5.6. |
| `outcome` | enum | `success` / `failure` / `escalated` / `paused` / `blocked` (preserves the existing enum). |
| `commit_sha` | string \| null | `null` when no commit resulted (Section 5.7). |
| `operator_approved` | boolean | Section 5.8 — never sufficient alone. |
| `approval_ref` | string \| null | Reference to the approval record (Section 9). |
| `evidence_refs` | array | Immutable evidence references. |
| `provenance` | object | Section 10. |
| `created_at` | timestamp | Record creation. |

### 5.2 Token semantics (preserves the existing contract)

- Measured token counts MUST be non-negative integers.
- Unmeasured token values MUST be `null` or absent per the canonical existing contract; the measured/unmeasured distinction is keyed off an explicit `measured` flag, exactly as `[[../../shared_context/loops/RUN_LEDGER_SCHEMA]]` requires — never off whether a number happens to be present.
- **Zero MUST NOT be used to mean unknown.** "Measured, and it was zero" and "not measured" are different facts and MUST stay distinguishable.
- Totals MUST NOT be invented; a total is present only when measured.
- Per-run or daily **budget enforcement MUST NOT be claimed when the required measurements are unavailable** — the correct report is `unenforceable`, never `pass` (mirrors the guard's behavior).

### 5.3 Cost semantics

`estimated_cost`, when present, MUST define: `amount`, `currency`, `calculation_method`, a `measured` vs `estimated` flag, `pricing_source`, and `pricing_timestamp`. It MUST be `null` when not measurable. Estimates MUST carry an explicit basis marker (in the spirit of the existing `basis: ESTIMATE_NOT_MEASURED`) and MUST NOT be presented with false precision or as a measured charge. An estimate can neither trip nor satisfy a budget check.

### 5.4 Lifecycle, timestamps, partial/failed runs

Timestamps MUST be UTC/RFC3339. `completed_at` MUST NOT precede `started_at`. An incomplete run has `completed_at: null` and an honest `outcome` (`failure`/`paused`/`blocked`), never a fabricated `success`. Partial runs are recorded as partial; missing fields are `UNKNOWN`.

### 5.5 File-change normalization

`files_changed` entries MUST be normalized (path + change kind) and MUST NOT include file contents, secrets, or credential-bearing paths.

### 5.6 Validator results

Each `validator_results` entry records the validator identity, verdict (`ACCEPT`/`REJECT`/`NOT_RUN`), and evidence reference. The validator MUST be independent of the actor that produced the work (preserves the run-ledger verifier-independence rule). `NOT_RUN` is distinct from `ACCEPT`.

### 5.7 Commit SHA nullability

`commit_sha` is `null` for any run that produced no commit. A `null` here MUST NOT be rendered as an empty or placeholder SHA.

### 5.8 `operator_approved` is not authority (hard rule)

`operator_approved: true` MUST NOT independently authorize implementation. When execution authority is relevant, it MUST be paired with an exact, valid, non-expired approval record (Section 9) referenced by `approval_ref`. A boolean alone is never sufficient.

### 5.9 Deduplication, correction, supersession

Duplicate run events (same `run_id`) are deduplicated to one record. Corrections are made by appending a superseding record referencing the prior one; the history is never silently rewritten (Section 13).

---

## 6. Skill Gap Detector

A **recommendation-only** detector that surfaces candidate skills from repeated operator/agent effort. It never creates, modifies, installs, activates, or grants anything.

### 6.1 Candidate threshold

A repeated process observed **at least three times** MAY become a skill-gap candidate. Below three, it is an observation, not a candidate.

### 6.2 Prohibited automatic actions (hard rule)

The detector MUST NOT automatically: create a skill, modify a skill, install a skill, activate a skill, change instructions, grant permissions, or commit/push code. Its only output is a candidate record for operator review.

### 6.3 Logical record

**ILLUSTRATIVE — logical fields, not a runtime type.** Required fields (minimum): `candidate_id`, `pattern_key`, `observation_window`, `occurrence_count`, `evidence_refs`, `affected_tasks`, `proposed_skill_purpose`, `expected_benefit`, `estimated_maintenance_cost`, `risk_class`, `confidence`, `status`, `operator_decision`, `created_at`, `expires_at`.

### 6.4 Detection and handling

- **Repeat detection** — occurrences are matched on `pattern_key`; both **exact** repetition and **semantic** near-repetition MAY be counted, but semantic matches MUST be marked lower `confidence` and remain evidence-linked.
- **Deduplication** — the same pattern MUST NOT spawn multiple active candidates.
- **Minimum evidence** — a candidate MUST cite the specific `evidence_refs` that establish its `occurrence_count`.
- **False positives** — a candidate the operator rejects is recorded as rejected; the detector MUST NOT immediately re-raise it. Re-observation after rejection is permitted only with materially new evidence and a fresh candidate id.
- **Expiry** — a candidate past `expires_at` transitions to expired and is not silently deleted.
- **Sensitivity boundary** — `pattern_key`, evidence, and purpose fields MUST NOT contain secrets or `regulated_high_risk`/MellyTrade content (Section 10).

---

## 7. Memory Freshness Monitor

Read-only monitoring of the freshness, trust, and sensitivity of knowledge, memory, context, and recommendation inputs. It **integrates with** the existing Context Gate provenance/sensitivity model (`[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]`) and MUST NOT replace or redefine it.

### 7.1 Freshness policy

Each monitored item MUST carry: `last_validated_at`, `validation_source`, `trust_level` (`high`/`medium`/`low`), `sensitivity_level` (`public`/`internal`/`private`/`secret`/`regulated_high_risk`), and a `staleness_policy` with `review_after` where applicable — reusing the provenance spec's `immutable_historical` / `volatile` / `periodic_review` semantics. Immutable historical facts never go stale; volatile and periodic-review facts have a `review_after`.

### 7.2 Freshness states

An item is `FRESH`, `EXPIRING` (approaching `review_after`), `STALE` (past `review_after`, unre-verified), `UNKNOWN` (no freshness data), or `INVALID` (provenance broken/contradicted). A `STALE` item is flagged for human review, never auto-deleted, hidden, or silently refreshed.

### 7.3 Dependency propagation

When a fact that other records depend on goes `STALE`/`INVALID`, dependents MUST be flagged as potentially affected (propagated staleness), not silently trusted.

### 7.4 Manual review and refusal behavior

- Re-validation of a `STALE` item requires a human/operator action; the monitor proposes, it does not refresh.
- **Sensitive information (`secret`, `regulated_high_risk`) MUST NOT be silently refreshed or re-fetched.** The correct behavior is refusal plus a content-free refusal note (mirrors provenance spec §5.1 and the existing refusal-log pattern).
- Trust MUST NOT be automatically elevated; raising `trust_level` requires a stated human rationale (mirrors provenance spec §4.3).

### 7.5 Five distinct states (normative)

The monitor MUST distinguish, and MUST NOT conflate, these five properties of a record:

1. the record **exists**;
2. the record is **trusted**;
3. the record is **fresh**;
4. the record is **relevant** to the current task;
5. the record is **authorized** for the current task.

A record can exist without being trusted, be trusted but stale, be fresh but irrelevant, or be relevant but unauthorized. These are not interchangeable.

---

## 8. Recommendation Ledger

An append-oriented ledger of every recommendation and its full disposition.

### 8.1 Logical record

**ILLUSTRATIVE — logical fields, not a runtime type.** Required fields (minimum): `recommendation_id`, `schema_version`, `source_run_ids`, `source_evidence_refs`, `observation_summary`, `analysis_summary`, `proposed_action`, `expected_benefit`, `risk_class`, `confidence`, `affected_projects`, `affected_files_or_systems`, `required_approvals`, `status`, `approval_ref`, `implementation_refs`, `validation_refs`, `created_at`, `expires_at`, `supersedes`, `superseded_by`.

### 8.2 Lifecycle states

`OBSERVED`, `ANALYZED`, `RECOMMENDED`, `APPROVED`, `REJECTED`, `EXPIRED`, `IMPLEMENTING`, `IMPLEMENTED`, `VALIDATING`, `VALIDATED`, `FAILED`, `CANCELLED`, `SUPERSEDED`. These names are consistent with the controlled-loop contract (Section 3).

### 8.3 Rules

- **Append-only audit history** — every state change is appended with actor, timestamp, and evidence; nothing is edited in place except to set `superseded_by`.
- **Exact evidence linkage** — every recommendation MUST cite the `source_run_ids`/`source_evidence_refs` it rests on.
- **Confidence** — a bounded, defined score with a stated basis; confidence is not certainty and never substitutes for approval.
- **Risk classification** — `risk_class` (e.g. `low`/`medium`/`high`/`safety_relevant`) sets the required approval scope; `safety_relevant` recommendations require operator approval and MUST NOT be auto-actioned.
- **Expiry** — a recommendation past `expires_at` becomes `EXPIRED` and cannot be approved.
- **Duplicates** — the same proposed action from the same evidence MUST NOT create a second active recommendation (deduplication).
- **Supersession** — a revised recommendation references `supersedes`; the prior is marked `SUPERSEDED`. Rejection and cancellation are recorded with reasons.
- **Implementation/validation evidence** — `IMPLEMENTED` requires `implementation_refs`; `VALIDATED` requires `validation_refs`. `FAILED` records the failure with an `error_signature`.
- **No silent deletion** — records are never deleted for presentation cleanliness (Section 13).
- **No execution by this specification** — this document defines the ledger; it executes no recommendation.

---

## 9. Approval Contract

An exact, scoped, time-bound authorization from the operator for a specific recommendation.

### 9.1 Logical record

**ILLUSTRATIVE — logical fields, not a runtime type.** Required fields (minimum): `approval_id`, `schema_version`, `recommendation_id`, `operator_identity`, `decision`, `target_digest`, `scope`, `constraints`, `authorized_actions`, `prohibited_actions`, `issued_at`, `expires_at`, `revoked_at`, `reason`, `evidence_refs`.

### 9.2 Requirements (normative)

- **Digest binding** — an approval binds to the exact content or `target_digest` it approved. If the content changes, the digest no longer matches and the approval is **invalid** (Section 14 digest-mismatch).
- **Scoped** — an approval authorizes only the explicit `authorized_actions` against the explicit targets; anything not listed is prohibited.
- **Expiry** — an approval past `expires_at` is invalid and MUST NOT authorize a new implementation.
- **Revocation** — an approval MAY be revoked (`revoked_at`) before execution begins; a revoked approval authorizes nothing.
- **Change invalidation** — changed content invalidates the approval; re-approval of the new digest is required.
- **No blanket/inferred approval** — a general or inferred approval is invalid; absence of approval means no authority.
- **Action-scope ladder (each step is a separate approval):**
  - approval to **commit** is not approval to **push**;
  - approval to **push** is not approval to **create a PR**;
  - approval to **create a PR** is not approval to move it to **ready**;
  - approval to **ready** is not approval to **merge**;
  - approval to **merge** is not approval to **deploy**.
- **Policy ceiling** — an approval cannot authorize an action prohibited by a higher-level safety policy (`[[../../shared_context/SAFETY_CONTRACT]]`); such an approval is void.
- **No self-approval** — a system component MUST NOT approve its own (or any) consequential action; only the operator approves (Section 14).
- **Absence = no authority** — where no valid approval exists, the authority does not exist.

### 9.3 Human-readable summary

Each approval MUST be expressible as a concise, human-readable summary suitable for UI display (what is being approved, against what digest, which actions, until when), so the operator can decide without reading raw fields.

---

## 10. Provenance, Trust, Sensitivity, and Audit

This section **reuses** the authoritative Context Gate model (`[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]`) and MUST NOT redefine it incompatibly.

1. **Provenance references** — every record carries a provenance object identifying `source_identity`, `source_type` (`user_provided`/`repo_derived`/`generated`/`externally_sourced`), and `verification_state` (`verified`/`unverified`).
2. **Source classification** — as above; a record with no source is `UNKNOWN`, not trusted.
3. **Trust levels** — `high`/`medium`/`low`, defaulted from `source_type` × `verification_state` per the provenance spec's lookup, human-overridable only with a stated rationale. `generated` content is capped at `medium` by default.
4. **Sensitivity levels** — `public`/`internal`/`private`/`secret`/`regulated_high_risk`, with the `allowed_use` matrix. `secret` is refused at admission; `regulated_high_risk` defaults to refused/deferred.
5. **Freshness interaction** — trust and freshness are independent axes (Section 7); a trusted record can be stale.
6. **Immutable evidence** — evidence references are write-once; corrections use supersession (`superseded_by`), never in-place edits.
7. **Refusal records** — refusals (e.g. a blocked secret) are logged content-free — the fact and category, never the value (mirrors the existing refusal log).
8. **Access boundaries and redaction** — private/secret/`regulated_high_risk` content MUST NOT be displayed, summarized, or exported; redaction is by classification, not by best effort.
9. **Audit retention** — audit and evidence records are retained per Section 13; safety/refusal evidence is never deleted for cleanliness.
10. **Schema versioning and clock** — every record carries `schema_version`; timestamps are UTC/RFC3339; expiry/freshness are evaluated against a stated clock. Deterministic rebuild from committed evidence MUST be possible (mirrors the content-free index/audit).

---

## 11. Observatory Module Map

Logical contracts map to intended **read-only** Observatory surfaces. This section specifies *what* each surface shows; it creates no UI and MUST NOT contradict the accepted `[[MELLYCORE_HOLOGRAPHIC_UI_SPEC_001]]`. Source Arena remains the leading visual metaphor; this task does not implement it.

For every surface: it is read-only; it MUST label each datum with a Section 1.9 truthful-state label; and it MUST render `empty`, `loading`, `partial`, `stale`, `unavailable`, and `error` states explicitly rather than as blanks or fabricated completeness.

| Surface | Purpose | Source records | Key operator question | Prohibited implication |
|---|---|---|---|---|
| **Mission Control** | Objectives, gates, blockers, operator choices | Recommendation ledger, approvals, loop states | "What needs my decision?" | That anything acted without me. |
| **Agent Activity** | Visible work state and evidence | Unified Run Ledger, loop states | "What are agents doing, with what evidence?" | That agents used uncontrolled tools. |
| **Context Pulse** | Provenance, sensitivity, freshness, contradiction signals | Context Gate records, Memory Freshness Monitor | "Is my context trustworthy and fresh?" | That stale/unknown data is live. |
| **Model Router** | Model roles and (future) evidence-backed routing | `[[../../shared_context/MODEL_ROUTING]]`, AI Estate Inventory | "Which model/role, and why?" | That routing is automated/live today. |
| **Unified Run Ledger** | One inspectable history of runs and outcomes | Unified Run Ledger | "What ran, what did it cost, what was the outcome?" | That unmeasured cost is zero. |
| **Approval Queue** | Consequential recommendations awaiting decision | Recommendation ledger, approvals | "What am I being asked to authorize?" | That a queued item is already approved. |
| **Memory & Recommendation Ledger** | Durable recommendations and disposition | Recommendation ledger, memory records | "What was recommended and what happened?" | That a recommendation was executed. |
| **AI Estate Inventory** | Models, agents, skills, tools, governed surfaces | AI Estate Inventory | "What assets do I have and their status?" | That an `UNVALIDATED` asset is available. |

Foundation status is truthful per current positioning: Context Pulse and the Unified Run Ledger have **partially implemented foundations** (Context Gate records; loop ledgers); the remaining surfaces are `PLANNED`. Permitted read-only interactions are inspection, filtering, and drill-down to evidence — never a state-changing control.

---

## 12. Failure, Partial-Data, and Recovery Semantics

For each condition, the system MUST prefer an explicit `UNKNOWN`/`PARTIAL`/`STALE`/`UNAVAILABLE`/`ERROR` state over fabricated completeness.

| Condition | Required behavior |
|---|---|
| Missing token counts | Fields `null`; budget reported `unenforceable`; never zero. |
| Unknown price | `estimated_cost: null`; no false precision. |
| Provider unavailable | Asset `status: UNAVAILABLE` with reason; dependent runs marked accordingly. |
| Incomplete run | `completed_at: null`; honest non-success `outcome`. |
| Stale memory | `STALE`; flagged for review; not auto-refreshed. |
| Invalid provenance | Record `INVALID`/`UNKNOWN`; not trusted. |
| Revoked approval | Authorizes nothing; execution refused. |
| Expired approval | Invalid; `IMPLEMENTING` refused. |
| Validator unavailable | Validation `NOT_RUN`; not `ACCEPT`. |
| Partial validation | `DEGRADED`/`PARTIAL`; not `VALIDATED`. |
| Conflicting records | Contradiction flagged to the ledger; not auto-resolved. |
| Duplicate event | Deduplicated; state not advanced twice. |
| Clock skew | Recorded; expiry evaluated against a stated clock; skew surfaced. |
| Interrupted implementation | `FAILED` with evidence; no silent `success`. |
| Failed recommendation | `FAILED` with `error_signature`; recoverable via new attempt. |
| Missing commit | `commit_sha: null`; not a placeholder. |
| Evidence corruption | `ERROR`; record quarantined for review, not silently dropped. |

---

## 13. Retention, Immutability, and Corrections

- **Append-only records:** Unified Run Ledger entries, Recommendation Ledger entries, approval records, provenance/evidence records, and refusal records.
- **Updatable metadata:** derived/annotative fields (e.g. `updated_at`, `freshness_state`, a `superseded_by` pointer) MAY be updated; core evidence MUST NOT.
- **Correction records:** a correction is a new record referencing the corrected one, with rationale.
- **Supersession:** the prior record is marked superseded; both remain readable.
- **Tombstones:** where an item must be withdrawn, a tombstone marks it withdrawn with reason; the underlying evidence is not erased.
- **Retention:** evidence is retained to allow deterministic rebuild; safety/refusal evidence is retained indefinitely.
- **No silent history rewrite** and **no deletion of safety or refusal evidence for presentation cleanliness.**
- This section authorizes **no** new runtime persistence behavior; it constrains a future implementation.

---

## 14. Security and Threat Model

For each threat, the specification-level required behavior:

| Threat | Required preventive/refusal behavior |
|---|---|
| Prompt injection in observations/memory | Observed content is data, not instruction; never acted on; injected "approvals"/commands are ignored and flagged. |
| Poisoned provenance | Unverifiable provenance → `UNKNOWN`/low trust; not admitted as trusted. |
| Stale approvals | Expiry enforced; expired approval authorizes nothing. |
| Approval replay | Approvals are single-scope, digest-bound, and consumed; replay against different content fails digest check. |
| Digest mismatch | Any content change invalidates the approval; execution refused. |
| Confused-deputy actions | A component acts only within its own least-privilege scope; it cannot borrow the operator's authority. |
| Privilege escalation | No self-elevation; scope is fixed by the approval. |
| Secret leakage | No secrets in any record; authentication metadata is mode-only; refusals are content-free. |
| Misleading simulated data | `SIMULATED` data always labeled; never presented as live. |
| Fabricated validation | Validation requires independent evidence; `NOT_RUN` ≠ `ACCEPT`. |
| Provider impersonation | Provider identity is evidence-backed and normalized; unverified providers are `UNKNOWN`. |
| Cost manipulation | Cost is measured-or-null with a stated basis; estimates cannot satisfy budgets. |
| Token-count fabrication | Only measured tokens count; unmeasured is `null`, never zero. |
| Malicious recommendation chaining | Each recommendation requires its own evidence and its own approval; approval of one is not approval of a chain. |
| Self-approval | A component MUST NOT approve its own consequential action; only the operator approves. |
| Autonomous safety-rule modification | Refused; safety policy changes only via a separate operator-approved task. |

---

## 15. Non-Goals

This specification explicitly excludes: backend implementation; database implementation; runtime adapters; provider authentication; provider keys; autonomous task execution; autonomous skill creation; autonomous code modification; autonomous commit, push, PR, merge, deploy, rollback, or release; autonomous safety-rule changes; trading operations; a production scheduler; claims of real-time completeness; Source Arena implementation; and any replacement of the existing Context Gate or Loop Operations contracts.

---

## 16. Implementation Sequencing

Future stages are defined here but not implemented:

1. **Exact next task — `MELLYCORE-OPERATIONS-DATA-CONTRACT-001`.** Translate the approved logical contracts in this document into fixture/schema artifacts and validation requirements (still documentation/fixture scope; no runtime execution).
2. 3D Scene Foundation (Source Arena groundwork) — separately specified and authorized.
3. Cockpit Shell.
4. Static Observatory modules (read-only, mock-labeled).
5. Read-only adapters.
6. Guarded approvals.
7. End-to-end safety validation.

Guarded execution MUST remain gated behind later explicit specifications and per-stage operator authorization. No stage is entered merely because the previous one produced files.

---

## 17. Acceptance Requirements (O1–O18)

Each requirement has a normative assertion, a verification method, and a blocking failure condition.

| ID | Normative assertion | Verification method | Blocking failure |
|---|---|---|---|
| **O1** | Product identity and truthful implementation status are stated; foundations vs planned are separated. | Read §1; cross-check `[[../../shared_context/PROJECT_STATE]]`. | Any planned capability described as implemented. |
| **O2** | The controlled-loop state machine is fully specified with prohibited transitions. | Read §3; check §3.4 list. | A prohibited transition is permitted. |
| **O3** | AI Estate Inventory record is complete with identifier/normalization/status rules. | Read §4; field checklist. | A required field or rule missing. |
| **O4** | Unified Run Ledger record is complete and preserves the existing contract. | Read §5 vs `RUN_LEDGER_SCHEMA.json`. | Contradiction with the existing contract. |
| **O5** | Token measurement honesty (measured/null/zero distinct; budgets unenforceable when unmeasured). | Read §5.2, §12. | Zero used for unknown, or budget claimed on unmeasured. |
| **O6** | Cost-estimation honesty (measured-or-null, stated basis, no false precision). | Read §5.3, §12. | Estimate presented as measured, or false precision. |
| **O7** | Skill Gap Detector is recommendation-only. | Read §6.2. | Any automatic skill create/modify/install/activate. |
| **O8** | Memory freshness separates trust/freshness/sensitivity and the five states. | Read §7.5, §7.4. | States conflated, or sensitive silent refresh allowed. |
| **O9** | Recommendation Ledger lifecycle is append-only with evidence linkage. | Read §8. | Silent deletion or missing evidence linkage. |
| **O10** | Exact approval binding and expiry (digest-bound, scoped, revocable, expiring). | Read §9. | Blanket/inferred approval permitted. |
| **O11** | No inferred or blanket authority; boolean is never sufficient. | Read §5.8, §9.2. | A boolean alone authorizes execution. |
| **O12** | Provenance and audit compatible with Context Gate. | Read §10 vs provenance spec. | Incompatible redefinition. |
| **O13** | Truthful-state UX semantics (labels, empty/partial/stale/error). | Read §1.9, §11. | Planned/simulated/stale rendered as live. |
| **O14** | Failure and partial-data behavior prefers explicit unknown states. | Read §12. | Fabricated completeness for any listed condition. |
| **O15** | Security/threat-model coverage with required behavior per threat. | Read §14. | A listed threat lacks required behavior. |
| **O16** | No provider secrets or runtime implementation. | Secret scan + scope review (Phase 7). | Any secret or runtime artifact present. |
| **O17** | Existing Context Gate and Loop Operations remain authoritative. | Read §1.8, §5, §7, §10. | This spec overrides them. |
| **O18** | Exact next-task boundary is `MELLYCORE-OPERATIONS-DATA-CONTRACT-001`. | Read §16. | A different or missing next task. |

---

## 18. Illustrative Examples

Every example below is **ILLUSTRATIVE — NOT A RUNTIME SCHEMA OR LIVE RECORD.** They contain no real secrets, credentials, private paths, or live data. Field values are placeholders.

### 18.1 AI Estate Inventory entry

```
ILLUSTRATIVE — NOT A RUNTIME SCHEMA OR LIVE RECORD
{
  "asset_id": "asset-model-example-001",
  "schema_version": "aoi-estate-1",
  "provider": "example-provider",
  "model": "example-model-a",
  "plan": "UNKNOWN",
  "authentication_mode": "ENV_REFERENCE",
  "purpose": "architecture-and-review",
  "cost_class": "SUBSCRIPTION",
  "capabilities": ["reasoning", "code", "review"],
  "status": "UNVALIDATED",
  "last_validated_at": null,
  "allowed_projects": ["mellycore-aios"],
  "freshness_state": "UNKNOWN",
  "provenance": {"source_type": "repo_derived", "verification_state": "unverified"},
  "evidence_refs": ["shared_context/MODEL_ROUTING.md"]
}
```

### 18.2 Measured run

```
ILLUSTRATIVE — NOT A RUNTIME SCHEMA OR LIVE RECORD
{
  "run_id": "example-run--20260101T000000Z--0123456789ab",
  "task_id": "example-task",
  "agent": "example-agent",
  "model": "example-model-a",
  "started_at": "2026-01-01T00:00:00Z",
  "completed_at": "2026-01-01T00:02:10Z",
  "input_tokens": 4210, "output_tokens": 880, "cache_read_tokens": 0,
  "tokens_measured": true,
  "estimated_cost": null,
  "outcome": "success",
  "commit_sha": null,
  "operator_approved": false,
  "approval_ref": null
}
```

### 18.3 Unmeasured run

```
ILLUSTRATIVE — NOT A RUNTIME SCHEMA OR LIVE RECORD
{
  "run_id": "example-run--20260101T010000Z--fedcba987654",
  "task_id": "example-task",
  "agent": "example-agent",
  "model": "example-model-a",
  "started_at": "2026-01-01T01:00:00Z",
  "completed_at": null,
  "input_tokens": null, "output_tokens": null, "cache_read_tokens": null,
  "tokens_measured": false,
  "estimated_cost": null,
  "outcome": "paused",
  "commit_sha": null
}
```
Note: unmeasured tokens are `null`, never `0`; budget for this run is `unenforceable`.

### 18.4 Skill-gap candidate

```
ILLUSTRATIVE — NOT A RUNTIME SCHEMA OR LIVE RECORD
{
  "candidate_id": "gap-example-001",
  "pattern_key": "repeated-local-validation-sequence",
  "observation_window": "2026-01-01..2026-01-14",
  "occurrence_count": 4,
  "evidence_refs": ["example-run-1", "example-run-2", "example-run-3", "example-run-4"],
  "proposed_skill_purpose": "codify a repeated read-only validation sequence",
  "risk_class": "low",
  "confidence": "medium",
  "status": "candidate",
  "operator_decision": null,
  "created_at": "2026-01-14",
  "expires_at": "2026-02-14"
}
```

### 18.5 Stale memory record

```
ILLUSTRATIVE — NOT A RUNTIME SCHEMA OR LIVE RECORD
{
  "record_id": "mem-example-001",
  "summary": "example current-state fact",
  "last_validated_at": "2026-01-01",
  "validation_source": "repo_derived",
  "trust_level": "medium",
  "sensitivity_level": "internal",
  "staleness_policy": "volatile",
  "review_after": "2026-01-15",
  "freshness_state": "STALE"
}
```

### 18.6 Recommendation

```
ILLUSTRATIVE — NOT A RUNTIME SCHEMA OR LIVE RECORD
{
  "recommendation_id": "rec-example-001",
  "schema_version": "aoi-rec-1",
  "source_run_ids": ["example-run-1"],
  "proposed_action": "example documentation cleanup",
  "expected_benefit": "reduced drift",
  "risk_class": "low",
  "confidence": "medium",
  "required_approvals": ["operator"],
  "status": "RECOMMENDED",
  "approval_ref": null,
  "created_at": "2026-01-14",
  "expires_at": "2026-01-28"
}
```

### 18.7 Exact approval

```
ILLUSTRATIVE — NOT A RUNTIME SCHEMA OR LIVE RECORD
{
  "approval_id": "apr-example-001",
  "schema_version": "aoi-approval-1",
  "recommendation_id": "rec-example-001",
  "operator_identity": "operator",
  "decision": "approved",
  "target_digest": "sha256:EXAMPLE_DIGEST_PLACEHOLDER",
  "scope": "single-recommendation",
  "authorized_actions": ["commit"],
  "prohibited_actions": ["push", "merge", "deploy"],
  "issued_at": "2026-01-14T12:00:00Z",
  "expires_at": "2026-01-15T12:00:00Z",
  "revoked_at": null,
  "reason": "reviewed and scoped to a local commit only"
}
```
Note: this approves `commit` only; it is not approval to push, PR, merge, or deploy.

### 18.8 Rejected recommendation

```
ILLUSTRATIVE — NOT A RUNTIME SCHEMA OR LIVE RECORD
{
  "recommendation_id": "rec-example-002",
  "status": "REJECTED",
  "approval_ref": null,
  "reason": "operator judged the change out of scope",
  "created_at": "2026-01-14"
}
```

### 18.9 Failed validation

```
ILLUSTRATIVE — NOT A RUNTIME SCHEMA OR LIVE RECORD
{
  "recommendation_id": "rec-example-003",
  "status": "FAILED",
  "implementation_refs": ["example-impl-1"],
  "validation_refs": ["example-validation-1"],
  "error_signature": "validator-reject:example",
  "note": "independent validation returned REJECT; a new attempt is required"
}
```

### 18.10 Superseded recommendation

```
ILLUSTRATIVE — NOT A RUNTIME SCHEMA OR LIVE RECORD
{
  "recommendation_id": "rec-example-001",
  "status": "SUPERSEDED",
  "superseded_by": "rec-example-004",
  "note": "revised after new evidence; prior record retained as history"
}
```

---

*This specification is a documentation-only artifact of `MELLYCORE-AI-OPERATIONS-INTELLIGENCE-001`. It authorizes no backend, runtime, adapter, UI, scheduler, provider integration, autonomous agent, execution engine, production schema, or runtime-consumed configuration. Every logical record, enum, and example is a contract or illustration, not a running system. The exact next task is `MELLYCORE-OPERATIONS-DATA-CONTRACT-001`.*
