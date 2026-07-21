# MellyCore Operations Data Contract Spec

**Task ID:** MELLYCORE-OPERATIONS-DATA-CONTRACT-001
**Version:** 1.0
**Status:** Documentation/fixture/schema contract only. No runtime, backend, adapter, UI, scheduler, provider integration, hardware telemetry, or execution is authorized or created by this document.
**Scope:** Translates the logical contracts approved in `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` (integrated into canonical `main` via PR #7) into eleven concrete, dashboard-facing fixture-level entities — `operation_run`, `task_record`, `agent_identity`, `model_provider_usage`, `token_cost_record`, `validation_result`, `artifact_record`, `environment_capability_snapshot`, `approval_gate`, `safety_status`, `recommendation_ledger_entry` — with their required/optional fields, allowed status values, forbidden claims, example fixtures, and dashboard display semantics.

---

## 1. Status, Purpose, and Non-Goals

### 1.1 Documentation/fixture/schema scope only

This document and its companion machine-readable files under `shared_context/operations/` are a **fixture-level data contract**, not an implementation. They define the *shape* dashboard-facing operational data would take, and the *rules* that shape must obey to stay truthful. No backend, database, runtime adapter, UI, scheduler, provider integration, or hardware-telemetry agent exists or is created by this document. Every field, enum, and example below is a **fixture contract**, not evidence that any corresponding running system exists.

### 1.2 Relationship to the AI Operations Intelligence spec (source of truth)

This document does **not** redefine the logical records in `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §4–§9 (AI Estate Inventory, Unified Run Ledger, Skill Gap Detector, Memory Freshness Monitor, Recommendation Ledger, Approval Contract). It decomposes and cross-references them into eleven concrete, narrower entities suited to dashboard rendering and deterministic fixture testing. Where a field, enum, or rule already exists in that spec or in `[[../../shared_context/loops/RUN_LEDGER_SCHEMA]]`, this document reuses it by reference and MUST NOT restate it incompatibly. This satisfies `MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001` §16 item 1 ("exact next task").

### 1.3 Relationship to prior unpushed work

A separate local branch, `docs/mellycore-operations-data-contract-001` (dated 2026-07-19, never pushed to `clean-origin`, not referenced as canonical by any shared-context file — see `shared_context/PROJECT_STATE.md`, `ROADMAP.md`, `RUN_QUEUE.md`, `AGENT_HANDOFF.md`, all of which explicitly state its content is not claimed canonical), contains an earlier, differently-scoped attempt at an operations data contract (AI Estate Inventory, Unified Run Ledger, Skill Gap Candidate, Memory Freshness, Recommendation Ledger, Approval Record, and a ten-value Truthful-State Labels reference). That branch is based on a `main` commit roughly ten merged pull requests behind current canonical `main` and was not rebased or reconciled as part of this task — doing so would require conflict resolution in `shared_context/*`, which this task's authorization does not permit. This document is a fresh authoring pass against current canonical `main` and the operator's current eleven-entity specification; reconciling or superseding the older branch is explicitly deferred to a future, separately authorized task (Section 6).

### 1.4 Non-goals (explicit)

- No backend ingestion, database, runtime adapter, or scheduler.
- No provider API calls, provider keys, tokens, credentials, or `.env` values.
- No frontend scaffold, Source Arena implementation, or Three.js vendoring.
- No NASA runtime retirement.
- No deployment or release of any kind.
- No trading, broker, order-execution, buy/sell UX, or MellyTrade runtime direction.
- No claim that any entity below is live, measured, or connected to a real running system unless a separately authorized implementation task says so with file-backed evidence.
- No hardware polling, telemetry collection, or automatic environment detection (Section 2.8).

### 1.5 Truthfulness rules (normative)

1. Every fixture under `shared_context/operations/*.example.json` is illustrative only — never live telemetry, never evidence of a real run, never provider-account data. Each carries an explicit `example_notice` string saying so.
2. Any datum labeled `simulated` MUST carry that label wherever rendered; it MUST NOT be presented as live.
3. `token_cost_record.estimated_cost` MUST NOT be populated without `calculation_method` and `pricing_source`; a cost with no source is `null`, never invented (preserves `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §5.3).
4. `validation_result.verdict` of `ACCEPT` requires the validator actually ran; a validator that did not run records `NOT_RUN`, never a defaulted pass (preserves §5.6). This task's own report (Section 6) obeys this rule.
5. A `dashboard_status` of `implemented` requires file-backed evidence (a path, commit SHA, or test/validator result) cited in `evidence_refs`. Without such evidence the correct status is `planned`, `simulated`, or `fixture/example`.
6. Zero MUST NOT stand in for unknown/unmeasured (preserves §5.2's measured/unmeasured distinction exactly).
7. `environment_capability_snapshot` records are always `source: operator_provided` and `dashboard_status: fixture/example` under this contract version; this document creates no hardware-polling, telemetry-agent, or runtime-detection capability (Section 2.8).
8. No safety gate in `safety_status.gates` may be reported as passed without the corresponding check having actually run in the same task/run; an unrun check reports `not_evaluated`, never a defaulted pass.

### 1.6 Dashboard status vocabulary (normative)

Every entity below carries a `dashboard_status` field limited to exactly these seven values:

| Value | Meaning | Relation to `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §1.9 |
|---|---|---|
| `implemented` | Backed by file/commit/test evidence cited in `evidence_refs`. | Maps to `IMPLEMENTED`. |
| `planned` | Named on the roadmap; no fixture or implementation exists yet. | Maps to `PLANNED`. |
| `simulated` | Deterministic placeholder standing in for a real running system; always labeled as such wherever shown. | Maps to `SIMULATED`. |
| `fixture/example` | A documentation illustration of shape only, never intended to represent any run — real or simulated. Narrower than `simulated`, and the value used by every `*.example.json` file in this contract. | Subtype of `SIMULATED`, specific to this contract's own fixtures. |
| `not present` | The record or source that should exist could not be found at authoring/observation time. | Maps to `UNAVAILABLE`. |
| `blocked` | The underlying operation, run, or task is blocked and cannot proceed. | Reuses the existing `outcome` enum value `blocked` already defined in `[[../../shared_context/loops/RUN_LEDGER_SCHEMA]]`. |
| `requires operator approval` | The record's next lifecycle step needs an exact, scoped, digest-bound operator approval (§9 of the AI Operations Intelligence spec) before it can proceed. | A lifecycle-gate status, not a `truthful_state` label — applies chiefly to `approval_gate` and `recommendation_ledger_entry`. |

This seven-value vocabulary is the **UI-facing projection** this contract uses. It does not replace or redefine the ten-value `truthful_state` glossary in `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §1.9 (`IMPLEMENTED`, `LEGACY_PROTOTYPE`, `SPECIFIED`, `PLANNED`, `SIMULATED`, `UNAVAILABLE`, `DEGRADED`, `STALE`, `UNKNOWN`, `ERROR`), which remains the authoritative per-datum label. Every fixture in this contract also carries a `truthful_state` field using that glossary's exact values, so both vocabularies are always present together and never contradict each other.

---

## 2. Entity Catalogue

Every entity's JSON Schema definition lives in `shared_context/operations/OPERATIONS_DATA_CONTRACT_SCHEMA.json` under `$defs.<entity_name>`, and its example fixture lives at the matching key in `shared_context/operations/OPERATIONS_DATA_CONTRACT.example.json`. The tables below are the authoritative field lists; the JSON Schema file MUST NOT diverge from them.

### 2.1 `operation_run`

**Purpose.** Fixture-level, dashboard-facing view of a single execution of an agent operation (a task, loop run, or CLI invocation). Generalizes, and MUST NOT contradict, the Unified Run Ledger logical record (`[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §5.1) and `[[../../shared_context/loops/RUN_LEDGER_SCHEMA]]`.

| Field | Type | Required | Notes |
|---|---|---|---|
| `schema_version` | string | yes | Contract version. |
| `operation_run_id` | string | yes | Stable unique identity; compatible with the existing `run_id` form. |
| `task_id` | string | yes | The `task_record` this run served. |
| `agent_id` | string | yes | The `agent_identity` that performed the run. |
| `started_at` | timestamp | yes | UTC/RFC3339. |
| `outcome` | enum | yes | `success` \| `failure` \| `escalated` \| `paused` \| `blocked` — reuses the existing enum exactly, not extended. |
| `dashboard_status` | enum | yes | Section 1.6 vocabulary. |
| `truthful_state` | enum | yes | §1.9 ten-value glossary. |
| `evidence_refs` | array | yes | Immutable evidence references; empty array only if `dashboard_status` is not `implemented`. |
| `completed_at` | timestamp \| null | no | `null` for an incomplete run. |
| `commit_sha` | string \| null | no | `null` when no commit resulted; never a placeholder SHA. |
| `approval_ref` | string \| null | no | Reference to an `approval_gate` record. |

**Forbidden claims.** MUST NOT report `outcome: success` while `completed_at` is `null`. MUST NOT render a `null` `commit_sha` as an empty or placeholder value. This enum MUST NOT be extended with deploy/release-adjacent values (no `deployed`, `released`, `live`).

**Dashboard display semantics.** Render the `outcome` badge and `dashboard_status` badge together, never one without the other. `blocked`/`failure`/`escalated` runs are visually distinct from `success`. A run with `completed_at: null` is never rendered as complete.

### 2.2 `task_record`

**Purpose.** The discrete unit of work an `operation_run` serves — a roadmap task, run-queue entry, or loop stage. Cross-references the Controlled Loop State Machine stages (`[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §3) for compatible naming; does not redefine loop-stage semantics.

| Field | Type | Required | Notes |
|---|---|---|---|
| `schema_version` | string | yes | |
| `task_id` | string | yes | |
| `title` | string | yes | |
| `status` | enum | yes | `pending` \| `in_progress` \| `blocked` \| `completed` \| `cancelled`. |
| `created_at` | timestamp | yes | |
| `dashboard_status` | enum | yes | Section 1.6 vocabulary. |
| `truthful_state` | enum | yes | §1.9 glossary. |
| `parent_task_id` | string \| null | no | |
| `owner_agent_id` | string \| null | no | Reference to `agent_identity`. |
| `related_operation_run_ids` | array | no | |
| `blocked_reason` | string \| null | no | Required in practice whenever `status: blocked`. |
| `evidence_refs` | array | no | |

**Forbidden claims.** MUST NOT be marked `completed` without at least one `evidence_ref` when `dashboard_status` is `implemented`; a task with no work performed stays `pending` or carries `dashboard_status: planned`.

**Dashboard display semantics.** Drives a checklist-style view; `blocked_reason` is mandatory display text whenever `status: blocked`.

### 2.3 `agent_identity`

**Purpose.** Which actor — human operator, named agent persona, or automated script — performed or owns an `operation_run`/`task_record`. Cross-references AI Estate Inventory identifier/normalization rules (`[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §4.2) without duplicating the full estate record.

| Field | Type | Required | Notes |
|---|---|---|---|
| `schema_version` | string | yes | |
| `agent_id` | string | yes | |
| `display_name` | string | yes | |
| `agent_class` | enum | yes | `human_operator` \| `ai_agent_session` \| `automated_script`. |
| `dashboard_status` | enum | yes | Section 1.6 vocabulary. |
| `truthful_state` | enum | yes | §1.9 glossary. |
| `model_ref` | string \| null | no | Link to a `model_provider_usage` record. |
| `estate_ref` | string \| null | no | Link to an AI Estate Inventory entry, only when that record is itself file-backed. |
| `notes` | string \| null | no | |

**Forbidden claims.** MUST NOT imply an `ai_agent_session` acted outside operator-visible task scope. MUST NOT set `estate_ref` unless the referenced AI Estate Inventory record actually exists and is file-backed.

**Dashboard display semantics.** Identity chip on every run/task row; `agent_class` drives icon/badge choice, never authority.

### 2.4 `model_provider_usage`

**Purpose.** Which model/provider combination was invoked for a given `operation_run`, normalized per `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §4.3.

| Field | Type | Required | Notes |
|---|---|---|---|
| `schema_version` | string | yes | |
| `operation_run_id` | string | yes | |
| `provider` | string | yes | Normalized per §4.3. |
| `model` | string | yes | Normalized per §4.3. |
| `capability_used` | string | yes | From the capability vocabulary in §4.4; this document does not extend that vocabulary. |
| `dashboard_status` | enum | yes | Section 1.6 vocabulary. |
| `truthful_state` | enum | yes | §1.9 glossary. |
| `authentication_mode` | string \| null | no | **Mode only** (e.g. `operator_local_cli`, `not_configured`) — never a credential, key, or token (hard rule, preserves §4.6). |
| `request_count` | integer \| null | no | Measured only; `null` if unmeasured. |
| `region` | string \| null | no | |

**Forbidden claims.** MUST NOT contain any provider API key, token, secret, or account identifier under any field name. `authentication_mode` is mode-only.

**Dashboard display semantics.** Shown as a small provider/model tag on the owning `operation_run`; `authentication_mode` shown only as a mode label, never as a value resembling a credential.

### 2.5 `token_cost_record`

**Purpose.** Fixture-level view of token and cost measurement for one `operation_run`. Preserves, and MUST NOT contradict, `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §5.2–§5.3 and the measured/total distinction in `[[../../shared_context/loops/RUN_LEDGER_SCHEMA]]`.

| Field | Type | Required | Notes |
|---|---|---|---|
| `schema_version` | string | yes | |
| `operation_run_id` | string | yes | |
| `measured` | boolean | yes | Keys the measured/unmeasured distinction — never inferred from whether a number is present. |
| `input_tokens` | integer \| null | yes | `null` unless `measured: true`. |
| `output_tokens` | integer \| null | yes | `null` unless `measured: true`. |
| `dashboard_status` | enum | yes | Section 1.6 vocabulary. |
| `truthful_state` | enum | yes | §1.9 glossary. |
| `cache_read_tokens` | integer \| null | no | |
| `estimated_cost` | object \| null | no | `{ amount, currency, calculation_method, measured_or_estimated, pricing_source, pricing_timestamp }`; `null` when not measurable. |
| `budget_enforcement` | enum \| null | no | `pass` \| `fail` \| `unenforceable`. MUST be `unenforceable` (never `pass`) when `measured: false`. |

**Forbidden claims.** Zero MUST NOT mean unknown. Totals MUST NOT be invented — a total exists only when measured. `estimated_cost` MUST carry an explicit `measured_or_estimated` basis and MUST NOT be shown with false precision or as a measured charge. An estimate can neither trip nor satisfy `budget_enforcement`.

**Dashboard display semantics.** Unmeasured runs show `—` (an explicit "not measured" glyph), never `0`. Estimated cost is always rendered with an "estimated" qualifier.

### 2.6 `validation_result`

**Purpose.** Fixture-level record of one validator's verdict against an `operation_run` or `artifact_record`. Preserves `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §5.6.

| Field | Type | Required | Notes |
|---|---|---|---|
| `schema_version` | string | yes | |
| `validation_id` | string | yes | |
| `target_ref` | string | yes | An `operation_run_id` or `artifact_id`. |
| `validator_identity` | string | yes | Must be independent of the actor whose work it checks. |
| `verdict` | enum | yes | `ACCEPT` \| `REJECT` \| `NOT_RUN`. |
| `dashboard_status` | enum | yes | Section 1.6 vocabulary. |
| `truthful_state` | enum | yes | §1.9 glossary. |
| `evidence_ref` | string \| null | no | Required (non-null) whenever `verdict: ACCEPT` or `REJECT`. |
| `ran_at` | timestamp \| null | no | `null` when `verdict: NOT_RUN`. |
| `notes` | string \| null | no | |

**Forbidden claims.** `ACCEPT` MUST NOT be recorded unless the validator actually executed. `NOT_RUN` is distinct from `ACCEPT` and MUST NOT be collapsed into it. The validator identity MUST differ from the actor that produced the work being validated.

**Dashboard display semantics.** Three-state badge (accept/reject/not-run); a `NOT_RUN` badge is visually distinct from a passing badge, never hidden.

### 2.7 `artifact_record`

**Purpose.** A file, doc, schema, fixture, or report produced by an `operation_run`. Generalizes `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §5.5 file-change normalization beyond diffs to any produced artifact.

| Field | Type | Required | Notes |
|---|---|---|---|
| `schema_version` | string | yes | |
| `artifact_id` | string | yes | |
| `operation_run_id` | string | yes | |
| `path` | string \| null | yes | Repo-relative path; `null` only for a not-yet-created `planned` artifact. |
| `change_kind` | enum | yes | `added` \| `modified` \| `deleted` \| `unchanged`. |
| `dashboard_status` | enum | yes | Section 1.6 vocabulary. |
| `truthful_state` | enum | yes | §1.9 glossary. |
| `artifact_class` | enum \| null | no | `doc` \| `spec` \| `schema` \| `fixture` \| `report` \| `other`. |
| `content_digest` | string \| null | no | A hash reference, never file contents. |

**Forbidden claims.** MUST NOT include file contents, secrets, or credential-bearing paths (reuses §5.5 exactly). `path` MUST be a real repo-relative path whenever `change_kind` is not planned-only.

**Dashboard display semantics.** Rendered as a compact changed-files list per run, grouped by `change_kind`; never shows file content, only path and digest.

### 2.8 `environment_capability_snapshot`

**Purpose.** An **operator-provided**, point-in-time, non-authoritative description of a local machine's capability, used only for capacity-planning dashboard display. This entity exists nowhere else in canonical `main`; it is new to this contract.

| Field | Type | Required | Notes |
|---|---|---|---|
| `schema_version` | string | yes | |
| `snapshot_id` | string | yes | |
| `recorded_at` | timestamp | yes | When the operator recorded this snapshot — not a live poll timestamp. |
| `source` | enum | yes | Fixed to the single allowed value `operator_provided` in this contract version. |
| `os` | string | yes | e.g. `"Windows 11 Pro 10.0.26200"`. |
| `dashboard_status` | enum | yes | Section 1.6 vocabulary — **always `fixture/example` under this contract version** (hard rule). |
| `truthful_state` | enum | yes | §1.9 glossary — always `SIMULATED` under this contract version. |
| `cpu` | string \| null | no | e.g. `"Ryzen 7 5700X"`. |
| `ram_gb` | number \| null | no | |
| `gpu` | string \| null | no | e.g. `"RTX 4060 8GB VRAM / 3072 CUDA cores"`. |
| `storage` | string \| null | no | e.g. `"953.9 GB SSD"`. |

**Forbidden claims (hard rule).** This entity MUST NEVER be populated by runtime hardware polling, a telemetry agent, or automatic environment detection code. `source` is fixed to `operator_provided` specifically to foreclose that. `dashboard_status` MUST always be `fixture/example` for every record created under this contract version; a future, separately authorized task would be required before any `implemented` or live value becomes possible for this entity.

**Dashboard display semantics.** Rendered, if at all, behind an explicit "example environment — operator-provided, not detected" label; never used to gate or vary any runtime behavior.

### 2.9 `approval_gate`

**Purpose.** Fixture-level view of one operator approval decision gating a recommendation or implementation step. Preserves `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §9 exactly (digest binding, scope, expiry, revocation, action-scope ladder, no self-approval, no blanket approval).

| Field | Type | Required | Notes |
|---|---|---|---|
| `schema_version` | string | yes | |
| `approval_id` | string | yes | |
| `recommendation_id` | string | yes | |
| `operator_identity` | string | yes | |
| `decision` | enum | yes | `pending` \| `approved` \| `rejected` \| `revoked` \| `expired`. |
| `target_digest` | string | yes | Binds to the exact content approved. |
| `authorized_actions` | array | yes | Explicit; anything not listed is prohibited. |
| `issued_at` | timestamp | yes | |
| `dashboard_status` | enum | yes | Section 1.6 vocabulary. |
| `truthful_state` | enum | yes | §1.9 glossary. |
| `expires_at` | timestamp \| null | no | |
| `revoked_at` | timestamp \| null | no | |
| `reason` | string \| null | no | |
| `evidence_refs` | array | no | |

**Forbidden claims.** No blanket or inferred approval. A changed `target_digest` invalidates the approval. The action-scope ladder MUST NOT be collapsed — approval to commit ≠ push ≠ open a PR ≠ mark ready ≠ merge ≠ deploy (reused exactly from §9.2). No approval may authorize an action prohibited by `[[../../shared_context/SAFETY_CONTRACT]]`. No component may approve its own action; only the operator approves.

**Dashboard display semantics.** Human-readable summary required for every record (what is approved, against what digest, which actions, until when) so the operator can decide without reading raw fields (§9.3).

### 2.10 `safety_status`

**Purpose.** A dashboard-facing rollup of the project's standing safety posture (from `[[../../shared_context/SAFETY_CONTRACT]]` and this repository's operating rules) at the time of an `operation_run`, for audit display. Reflects `SAFETY_CONTRACT.md`; does not redefine it.

| Field | Type | Required | Notes |
|---|---|---|---|
| `schema_version` | string | yes | |
| `safety_status_id` | string | yes | |
| `operation_run_id` | string | yes | |
| `evaluated_at` | timestamp | yes | |
| `gates` | object | yes | Maps each standing gate name (e.g. `no_secrets_detected`, `no_destructive_git`, `no_deploy_without_approval`, `no_push_without_approval`, `no_trading_mutation`) to one of `pass` \| `fail` \| `not_evaluated`. |
| `dashboard_status` | enum | yes | Section 1.6 vocabulary. |
| `truthful_state` | enum | yes | §1.9 glossary. |
| `violations` | array | no | Empty by default. |
| `notes` | string \| null | no | |

**Forbidden claims.** No gate in `gates` may be `pass` without the corresponding check having actually run in the same task/run; an unrun check is `not_evaluated`, never a defaulted `pass`. A non-empty `violations` array MUST NOT be paired with an overall `dashboard_status` of `implemented`-clean without disclosing the violation.

**Dashboard display semantics.** Rendered as a compact gate checklist; any `fail` or `not_evaluated` gate is shown, never hidden or summarized away as "OK".

### 2.11 `recommendation_ledger_entry`

**Purpose.** Fixture-level view of one entry in the Recommendation Ledger (`[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §8). Preserves the exact thirteen lifecycle states and the append-only rule.

| Field | Type | Required | Notes |
|---|---|---|---|
| `schema_version` | string | yes | |
| `recommendation_id` | string | yes | |
| `source_run_ids` | array | yes | |
| `observation_summary` | string | yes | |
| `proposed_action` | string | yes | |
| `risk_class` | enum | yes | `low` \| `medium` \| `high` \| `safety_relevant`. |
| `status` | enum | yes | `OBSERVED` \| `ANALYZED` \| `RECOMMENDED` \| `APPROVED` \| `REJECTED` \| `EXPIRED` \| `IMPLEMENTING` \| `IMPLEMENTED` \| `VALIDATING` \| `VALIDATED` \| `FAILED` \| `CANCELLED` \| `SUPERSEDED` — reuses §8.2 exactly. |
| `created_at` | timestamp | yes | |
| `dashboard_status` | enum | yes | Section 1.6 vocabulary. |
| `truthful_state` | enum | yes | §1.9 glossary. |
| `approval_ref` | string \| null | no | Required (non-null) once `status: APPROVED` or later. |
| `implementation_refs` | array | no | Required (non-empty) once `status: IMPLEMENTED`. |
| `validation_refs` | array | no | Required (non-empty) once `status: VALIDATED`. |
| `expires_at` | timestamp \| null | no | |
| `supersedes` / `superseded_by` | string \| null | no | |

**Forbidden claims.** `IMPLEMENTED` requires `implementation_refs`; `VALIDATED` requires `validation_refs`. No silent deletion — corrections append a new record referencing the prior one. Duplicates from the same evidence MUST NOT create a second active recommendation. `safety_relevant` entries require operator approval and MUST NOT be auto-actioned.

**Dashboard display semantics.** Rendered as a lifecycle timeline; `dashboard_status: requires operator approval` is shown prominently whenever `status` is `RECOMMENDED` and no valid `approval_ref` exists yet.

---

## 3. Companion Machine-Readable Files

- `shared_context/operations/OPERATIONS_DATA_CONTRACT_SCHEMA.json` — one JSON Schema (draft-07) document with a `$defs` entry per entity above. Its top-level `description` states it is a documentation contract only, not runtime config, not live data ingestion, not execution authority, and names this document as the field-list authority it must not diverge from.
- `shared_context/operations/OPERATIONS_DATA_CONTRACT.example.json` — one example fixture object per entity, each carrying `dashboard_status: "fixture/example"`, `truthful_state: "SIMULATED"`, and an `example_notice` string.
- `shared_context/operations/README.md` — directory index and truthfulness summary for both files above.

No validator script reads, imports, or enforces these files in this task; `scripts/validate_project_state.py` and any other existing validator are run only to confirm they still pass with these additions present (Section 6).

---

## 4. Acceptance Notes

This document satisfies `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §16 item 1 (the "exact next task"). It remains documentation/fixture scope: no runtime execution, no backend, no provider integration, no frontend scaffold, no NASA runtime retirement, no Three.js vendoring, and no deployment are authorized or performed by this document or its companion files. The next stage in that spec's sequencing (3D Scene Foundation) is a separately specified and separately authorized task, not entered by this document's existence.

---

## 5. Cross-References

- `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` — source-of-truth logical contracts (§4–§9), truthful-state glossary (§1.9), acceptance requirements (§17).
- `[[../../shared_context/loops/RUN_LEDGER_SCHEMA]]` — authoritative loop-level run/token contract; not redefined here.
- `[[../../shared_context/SAFETY_CONTRACT]]` — authoritative safety posture; reflected, not redefined, by `safety_status`.
- `[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]` — authoritative provenance/trust/sensitivity model; `evidence_refs` fields across this contract reuse its vocabulary and do not redefine it.

---

## 6. Prior-Branch Reconciliation (deferred, not performed by this task)

The unpushed local branch `docs/mellycore-operations-data-contract-001` (Section 1.3) remains unreconciled with this document and with current canonical `main`. A future, separately authorized task should decide, with explicit operator direction, whether to: (a) discard that branch's content in favor of this document, (b) fold compatible pieces (e.g. its `TRUTHFUL_STATE_LABELS.md`, `AI_ESTATE`, `SKILL_GAP_CANDIDATE`, and `MEMORY_FRESHNESS` fixture pairs, which address AI Operations Intelligence entities outside this document's eleven-entity scope) into a later revision, or (c) archive it as superseded history. This task does not decide that question and does not delete, rebase, or push that branch.
