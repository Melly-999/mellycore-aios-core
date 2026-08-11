# MellyCore Agent Runtime Architecture Spec Remediation 001 — Task Report

## 1. Purpose

Remediate all fourteen findings recorded by
`MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-001` (P0 = 0, P1 = 4, P2 = 5,
P3 = 5), which returned `FAIL_REMEDIATION_REQUIRED` against
`docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md`.

Three of the four blocking findings were **seam conflicts** — the Agent Runtime
asserted semantics a different canonical owner already owns and either forbids
or cannot represent. This task therefore created a canonical seam-decision
record **before** editing any owner document, resolved each seam either by
conforming the Agent Runtime or by a minimal, additive owner amendment, and
recorded why every rejected alternative was rejected.

This is a documentation and architecture task only. No Agent Runtime code,
framework bridge, agent execution, provider call, model-provider connection,
tool execution, credential, secret, queue, persistence, frontend component, or
deployment was created.

## 2. Starting repository state

- Root: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios`
- Starting branch: `docs/mellycore-agent-runtime-architecture-spec-review-001`
- Starting HEAD: `ac762f5a9964c5c5111b83e831aee6624651e391`
- Parent: `17da8603fbe8b75082cfea44223745b3c63f14de`
- Subject: `docs: review agent runtime architecture`
- Canonical remote: `clean-origin` →
  `https://github.com/Melly-999/mellycore-aios-core.git`
- Fresh canonical main after the one authorized fetch:
  `947f33d27d5546775186e96bdc61e30db78c0b3d` — matched expected; **no drift**
- Starting worktree/index: clean
- Remediation branch before creation: absent locally; absent on `clean-origin`
  and `origin`
- Branch created from `ac762f5a9964c5c5111b83e831aee6624651e391`:
  `docs/mellycore-agent-runtime-architecture-spec-remediation-001` (not from
  `clean-origin/main`)

Exactly one network operation occurred: `git fetch clean-origin` (exit code
`0`), during the canonical remote gate. No later network access of any kind.

## 3. Review 001 dependency

This task consumes
`docs/research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_001.md` (review
commit `ac762f5a9964c5c5111b83e831aee6624651e391`) as the authoritative owner of
the finding definitions. All fourteen finding IDs were reconstructed directly
from that record's §45, not from any summary. The review record and its task
report were **not** modified and remain byte-identical.

Review 001 recorded that the following areas passed without a blocking finding,
and none was redesigned here: the canonical identifier model, canonical
serialization and digest discipline, nine-state package/runtime separation,
framework bridge prohibitions, memory categories, explicit handoff acceptance,
the single governed provider path, cancellation and timeout honesty, the retry
and reconciliation model, isolation boundaries, operator approvals, the threat
model, the external-content posture, runtime modes, and the inert-v1 boundary.
Only narrow consistency updates required by a recorded finding were applied to
them.

## 4. Finding register

| Finding | Review evidence | Canonical owner | Current contradiction | Required decision | Validation |
| --- | --- | --- | --- | --- | --- |
| `P1-01` | Review §45 P1-01; §11; §16 | Control Plane §8 | Six `run_state` values projected to `lifecycle_status:active`, which §8.2 forbids for a running agent; §9.5/§9.7 Run sets excluded `active`, `queued`, `draft`, `ready` | Conform Runtime **and** minimally amend the owner, which has no member meaning "executing" | 17-row projection table; every value legal and non-forbidden |
| `P1-02` | Review §45 P1-02; §18 | Provider Registry §21 | Runtime facts 5/6 duplicated Registry facts 5/6, whose §21.3 records are provider-scoped and require `provider_id`, while fact 10 already delegates to all eight | Resolve in Runtime only; Registry unchanged | 11-row fact table with owner, subject, evidence, scopes, expiry, denial class |
| `P1-03` | Review §45 P1-03; §30 | AI Operations §5 | Multi-attempt evidence contradicted §5.9 dedup by `run_id` and §5.1's single `outcome`/`model`/`provider` | Minimally amend the owner; dedup by `run_id` cannot preserve two attempts under any reading | Attempts never deduplicated; summaries derived |
| `P1-04` | Review §45 P1-04; §16 | Agent Runtime §12 | §23.6 mandated `waiting_for_operator`; §12.3 did not permit it from `waiting_for_model` | Resolve in Runtime only | Transition listed; reachable in one hop |
| `P2-01` | Review §45 P2-01 | Runtime consumption over Shared Context truth | "`blocked` or re-read per policy" with no defined policy | Deterministic policy in Runtime | Six exact conditions; fail-closed default |
| `P2-02` | Review §45 P2-02 | Agent Runtime §15 | `model_routing_decision_ref` in an envelope frozen before the decision exists | Revision chain in Runtime | 8-step sequence; envelope never mutated |
| `P2-03` | Review §45 P2-03 | AI Operations / Loop Operations | Agent-run identity not reconciled with the loop run-ledger form; loop runs unmentioned | Namespacing at the ledger layer | `run_kind`; forbidden substitution |
| `P2-04` | Review §45 P2-04 | Agent Runtime §20 | Concurrent broadcast acceptance unspecified | Atomic single-winner in Runtime | Seven conditions; no scope gained by racing |
| `P2-05` | Review §45 P2-05 | Agent Runtime §29 | Runtime restart with an attempt in an unknown state unaddressed | Recovery model in Runtime | 16-row matrix; no blind redispatch |
| `P3-01` | Review §45 P3-01 | Agent Runtime §19 | Trace enumerated 16 fields against a 17-field claim | Correct and complete the trace | 17 enumerated fields |
| `P3-02` | Review §45 P3-02 | Agent Runtime §20.2 | Handoff contents are 12, described as 11 | State the true count | "Exactly twelve" |
| `P3-03` | Review §45 P3-03 | Agent Runtime §33 | 38 rows carried 40 class names | Separate and fix both counts | 49 rows / 49 classes; one class per row |
| `P3-04` | Review §45 P3-04 | Agent Runtime §24, §9 | `INSUFFICIENT_PRICING_DATA` unowned; nine-state ↔ eleven-fact mapping unstated | Give it an owner; state the mapping | §33 row; §9.1 mapping table |
| `P3-05` | Review §45 P3-05 | Agent Runtime §8.3 | Type discipline stated in implementation-language terms | Make normative wording language-neutral | Exact-type rule neutral; Python marked non-normative |

No finding in the authoritative review differed materially from the register
above, so no stop condition triggered.

## 5. Canonical ownership matrix

| Concern | Canonical owner | Runtime responsibility | Changed here? |
| --- | --- | --- | --- |
| Status dimensions and vocabulary | Control Plane §8 | Publish a deterministic projection; define no status value | Owner amended additively |
| Entity catalogue | Control Plane §7 | Reuse; redefine nothing | No |
| Provider records, eight facts, credential classes, authorization-record custody | Provider Registry | Read; never register or mutate | **No — byte-identical** |
| Provider access, credentials, policy order, provider error taxonomy | Integration Gateway | Submit bounded proposals | **No** |
| Unified Run Ledger record, deduplication, supersession | AI Operations §5, §13 | Emit append-only evidence as a producer only | Owner amended additively |
| Loop registry, loop run identity, loop guard contracts | Loop Operations + `shared_context/loops/**` | Never present an agent run as a loop run | **No** |
| Canonical Shared Context truth, admission, provenance, sensitivity | Shared Context Layer + Context specs | Read snapshots; propose; never write canonically | **No** |
| Approvals | Control Plane §16 + Gateway §18 | Enforce; never self-approve | **No** |
| Agent runtime coordination, lifecycle, envelopes, bridges, handoffs, events | **This specification** | Owner | Yes |
| Agent packages | Deferred — Agent Package Contract | State required metadata only | No |

## 6. Seam-decision record

`docs/decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001.md` was
written **before** any specification edit and contains complete decisions for
every P1 and P2 finding, an eighteen-section structure, and a per-seam summary
table recording canonical owner, runtime responsibility, selected resolution,
documents changed, and why alternatives were rejected.

Its governing principles: the existing owner wins unless it provably cannot
represent the required semantics; a seam is never hidden inside the Agent
Runtime; owner amendments are additive and minimal; additive is not weakening;
higher-precedence contracts (AI Operations §1.8 items 2–5) are absolute;
runtime-specific semantics belong to the runtime; provider authorization stays
delegated; and no safety property is traded for coherence.

The record authorizes no implementation.

## 7. P1-01 remediation — lifecycle projection

**Decision: conform the Runtime and minimally amend the Control Plane.**

The owner could not represent the semantics: its lifecycle enum contains no
member meaning "currently executing" other than `active`, and §8.2 explicitly
forbids `active` for a running agent. Four conforming alternatives were tested
and rejected in the seam record §6.2 — reusing `active` (weakens a live safety
prohibition), projecting to `queued`/`ready` (misreports in-flight work),
omitting the field (removes runs from every lifecycle surface and from the
module `Statuses` contracts), and a seventh dimension (forbidden).

**Owner amendment (additive, 5 surgical edits):** `running` added to the §8.1
lifecycle enum; a §8.2 clause defining `running` and **reaffirming the `active`
prohibition verbatim**; the Run lifecycle sets in §9.5, §9.7, and §9.10
extended.

**Runtime changes:** §12.1 gained an explicit projection-direction and authority
statement plus a Control Plane dependency clause; §12.2 was rebuilt as a
**complete 17-row table** with columns for dimension, canonical projected value,
and owner evidence, followed by five normative projection notes; §34 gained five
operator-surface projection rules.

**Result:** all 17 states project to a legal, non-forbidden value. Six project
to `running`, two to `blocked`, and **none to `active`**. `run_state` remains
authoritative; the projection is one-directional and lossy; no runtime decision
is taken on a projected value; waiting, running, blocked, reconciliation, and
terminal meanings all remain distinct in `run_state` and are required to remain
separately visible in operator views.

## 8. P1-02 remediation — authorization facts

**Decision: resolve entirely inside the Agent Runtime. Provider Registry is
byte-identical and its eight facts remain exactly eight.**

§14 was rebuilt as three subsections. **§14.1** holds the eight run-admission
facts, **§14.2** the three per-invocation facts, and **§14.3** eight rules. Each
of the eleven facts now states owner, evidence record, subject, action scope,
tenant scope, environment scope, revision binding, expiry, and denial class.

Facts 5 and 6 were renamed and re-scoped:

- Fact 5 → **Tenant runtime authorization**, evidence
  `tenant_agent_runtime_authorization`, owned by this specification, subject
  `tenant_id`, scope "may operate the Agent Runtime in this environment". It
  says nothing about any provider.
- Fact 6 → **Agent capability authorization**, evidence
  `tenant_agent_capability_authorization`, binding tenant + `agent_definition_id`
  + one **agent capability class** from the package's `declared_capabilities`.

Rule 5 states the separation normatively in both directions: a Registry record
never satisfies a runtime fact and a runtime record never satisfies a Registry
fact; provider-side tenant and capability authorization exist **only** inside
fact 10; and an agent run proposing no provider operation requires facts 1–8
only and never a `provider_id`. Rule 6 names the two capability vocabularies and
forbids resolving one against the other (`UNSUPPORTED_CAPABILITY`).

**Consequential correction.** §12.2 previously defined `authorized` as "all
eleven facts hold", which facts 9–11 cannot satisfy for operations not yet
proposed. Rule 3 now fixes evaluation points: facts 1–8 are run-admission facts;
facts 9, 10, and 11 are evaluated at the point of tool use, provider proposal,
and consequential operation. §12.2 row 3 and §12.4 rule 3 were updated to match.
This narrows what run authorization claims and grants nothing new.

Two denial classes were added so the runtime facts are not reported through a
provider class: `RUNTIME_AUTHORIZATION_DENIED` and
`CAPABILITY_AUTHORIZATION_DENIED`.

## 9. P1-03 remediation — Run Ledger

**Decision: minimally amend AI Operations Intelligence §5, additively.**

Deduplication keyed on `run_id` alone cannot preserve two attempts of one run
under any reading, the Agent Runtime is a declared non-owner that cannot amend
§5.9 itself, and a second Runtime-owned ledger is prohibited.

**Owner amendment:** §5.1 gained `ledger_record_id` (the deduplication
identity), optional `attempt_id`, and optional `run_kind`. §5.9 was rewritten to
key deduplication on `ledger_record_id`; to state that records sharing a `run_id`
but differing in `attempt_id` are **distinct and MUST NOT be deduplicated**; to
state that a retry produces a new `attempt_id` and a replay a new `run_id`; and
to define a **derived** logical-run summary that never erases, supersedes,
hides, or stands in for attempt evidence and that reports disagreement between
attempts rather than selecting one as truth.

**Runtime alignment:** new §25.1 lists the exact fields the runtime supplies per
ledger record — `ledger_record_id`, `run_kind: agent_run`, `run_id`,
`attempt_id` (always present for an agent run), `step_id`, `sequence`, and
separate `observed_at`/`recorded_at` — followed by six consequences owned by AI
Operations and reused unchanged, and an explicit statement that the runtime does
not own or operate a second ledger. Prior §25 rules became §25.2 unchanged.

**Backward compatibility:** all three fields are optional with defined absent
semantics — `attempt_id` absent → single-attempt; `run_kind` absent →
`loop_run`; `ledger_record_id` absent → prior `run_id` behavior. Every existing
loop run ledger remains conforming **without modification**, so the
higher-precedence loop schemas (AI Operations §1.8 item 3) are neither edited nor
contradicted. §5.2–§5.8 and §13 are untouched.

**No migration was performed or claimed.** No persistence exists to migrate.

## 10. P1-04 remediation — routing-tie transition

**Decision: resolve entirely inside the Agent Runtime.**

§12.3 now permits `waiting_for_model`, `waiting_for_tool`, and
`waiting_for_agent` to transition to `waiting_for_operator`, and declares the
transition table **closed** — a transition absent from it is forbidden, and no
transition may be reached by an unstated intermediate hop. All three waiting
states were added rather than only the routing case, because tool-approval and
handoff-adjudication escalations reach the same state by the same logic.

New **§12.3.1** names the four allowed predecessors of `waiting_for_operator`,
tabulates each escalation trigger with its recorded reason class, and adds five
rules: mandatory §12.5 evidence; the runtime never resolves the escalated
condition; release requires an unexpired action-, revision-, and time-bound
operator decision; return to `running` resumes at the escalating step; and
`reconciliation_required` deliberately has no such transition.

§12.4 gained rules 10–12 forbidding unlisted transitions, unlisted predecessors
or unevidenced releases, and any resolution of a tie, approval, or conflict by
the runtime, a silent fallback, an arbitrary pick, or a timeout default.

§23.6 gained an explicit reachability statement and six resolution rules,
including that the operator selects only from the recorded tied set and that a
declined or expired decision yields `blocked`, never a default model. Scenario
15 was updated to name the transition it uses.

## 11. P2 remediation

| Finding | Change | Location |
| --- | --- | --- |
| `P2-01` | New **§17.4** — a declared, versioned, digest-bound staleness policy with five fields; materiality determined by **enumeration, never inference**; a six-condition table (current; stale non-material; stale material; policy absent; source unavailable; conflicting revision) each with one resulting state, reason class, and evidence; six rules including refresh-is-replacement-never-mutation, material-change-invalidates-the-envelope-binding, absence-fails-closed, and bounded operator exceptions | §17.4, §17.3 rule 4, Scenario 25 |
| `P2-02` | `model_routing_decision_ref` **removed** and replaced by `bound_routing_decision_ref` (present only when a revision was created to bind an already-issued decision); `envelope_revision_id` and `supersedes_envelope_revision_id` added; §15.3 rewritten as immutability **plus a revision chain**; new **§15.4** fixes the 8-step sequence and six invariants, and makes per-step routing decisions step-scoped artifacts that never enter or re-digest the envelope | §15.1, §15.3, §15.4 |
| `P2-03` | New **§8.4** — `run_kind` namespacing with seven normative rules: identity is the pair `(run_kind, run_id)`; the discriminator is mandatory on every emission; the agent form is opaque and never parsed as the loop form; cross-kind resolution denies with `RUN_KIND_MISMATCH`; collisions are integrity events; linkage uses `triggering_run_ref`, never identity reuse; and the Loop Operations model is neither renamed nor absorbed | §8.4, AI Operations §5.1 |
| `P2-04` | New **§20.4** — single-winner broadcast with an atomic compare-and-set on `acceptance_version`; a seven-condition table covering simultaneous claims, late claims, expiry, withdrawal, budget exhaustion, missing facts, and duplicates; seven rules including "racing grants nothing", reserve-once/draw-by-winner-only, losing is recorded not erased, no partial starts, and no optimistic acceptance pending confirmation | §20.4, §20.2, §29.2 |
| `P2-05` | New **§29.3** — durable evidence expectations, explicit recorded takeover, optional bridge status query whose failure yields `unknown`, a **16-row recovery matrix**, and eight rules including no blind redispatch, same-attempt resumption only on definitive external status, new attempt after reconciliation, duplicate-dispatch prevention via idempotency-key state, operator escalation, permanent block, no revival of terminal runs, and no reconstruction by inference | §29.3, §29.2 |

## 12. P3 remediation

1. **`P3-01`** — §19 rewritten as an enumerated 17-field table. `destination_run_id`
   was added so every transfer is attributable to both runs, which §29.1 run
   isolation and the §34 Context-flow view both require; the authoritative count
   is now **17**.
2. **`P3-02`** — §20.2 states **"exactly twelve"** required contents.
3. **`P3-03`** — the combined `STEP_LIMIT_EXCEEDED / DEPTH_LIMIT_EXCEEDED /
   LOOP_DETECTED` row was split into three rows, and §33 now states **49 rows and
   49 distinct class names** with a normative one-class-per-row invariant that
   any future amendment must preserve, so the two counts can never diverge again.
4. **`P3-04`** — `INSUFFICIENT_PRICING_DATA` is now an enumerated §33 class owned
   by this specification, with §24 rule 2 stating that the underlying cost
   semantics remain owned by AI Operations §5.2–§5.3 and Control Plane §19. New
   **§9.1** states the nine-state ↔ eleven-fact mapping and explains why states
   2, 7, and 9 deliberately have no fact.
5. **`P3-05`** — §8.3 rule 1 now states an **exact-type identity check** in
   language-neutral terms, with the Python form retained as a clearly marked
   *non-normative illustration*.

## 13. Control Plane compatibility

Purely additive. One enum member and one clause added; three module `Statuses`
rows extended. **No existing member changed meaning, and the `active`
prohibition is preserved verbatim.** The six-dimension model is intact; no
seventh dimension was created, consistent with Control Plane §24's recorded
decision. Any consumer that never renders a live run observes no change.

## 14. Registry compatibility

**Byte-identical — not amended.** Registry §21.1's eight facts remain exactly
eight; §21.2's rules and §21.3's two record types are untouched. Provider
authorization remains owned by the Registry and evaluated by the Gateway, and
runtime fact 10 continues to delegate entirely.

## 15. AI Operations compatibility

Additive. Three optional fields in §5.1 and a rewritten §5.9. All new fields
have defined absent-value semantics that reproduce prior behavior exactly, so
existing loop run ledgers remain conforming unmodified. §5.2–§5.8 and §13 are
untouched, and nothing contradicts the higher-precedence contracts in §1.8.

## 16. Loop identity compatibility

Unaffected. Loop run identity, its enforced `run_id` pattern, loop state, and
the guard contracts are preserved exactly, and the loop schemas were **not**
edited. Separation is achieved by namespacing at the ledger layer plus §8.4's
forbidden-substitution rules. The Loop Operations model is neither renamed,
absorbed, extended, nor superseded.

## 17. Shared Context staleness

Deterministic. Six conditions with one outcome each; materiality by enumeration
rather than inference; absence of a policy fails closed to `blocked`; refresh is
replacement with a new snapshot identity and a §19 trace record; a material
change invalidates the envelope's context binding and requires a new envelope
revision and renewed authorization rather than a re-read; conflicting revisions
escalate to `waiting_for_operator`; operator exceptions are per-snapshot,
per-run, time-bound and never convert material into non-material. No silent
substitution or automatic acceptance is possible. Canonical context truth,
admission, and provenance semantics are unchanged.

## 18. Envelope sequencing

Eight explicit steps: run request → initial validation (revision 1) →
pre-authorization routing request (optional) → routing decision → resolved
revision 2 → renewed validation → authorization against the current revision's
exact digest → dispatch eligibility. Steps 3–5 are skipped in the ordinary case,
where routing is per step during execution and a routing decision is a
step-scoped artifact that never enters the envelope.

Invariants: an authorized revision is never mutated; adding or changing a bound
decision creates a new digest-bound revision requiring renewed validation and
authorization; prior revisions and decisions remain auditable with bidirectional
supersession links; an approval bound to revision *N* is void for *N+1*; a
per-step decision crossing a §23.4 boundary requires a new revision, a new
attempt, and renewed authorization; and a broken supersession chain is rejected
with `ENVELOPE_INTEGRITY_FAILED`.

## 19. Broadcast concurrency

Single-winner with an atomic compare-and-set keyed by `handoff_id` on
`acceptance_version`, reusing the optimistic-concurrency mechanism §29.2 already
mandates. Exactly one claim can satisfy the precondition. Losers are denied with
`HANDOFF_ALREADY_ACCEPTED` and create no run at all; late, withdrawn, and
budget-exhausted claims deny with their own classes; duplicate claims from the
winner return the recorded decision. Budget is reserved once at broadcast
creation and drawn only by the winner, with full release on expiry or
non-acceptance. **No recipient gains scope by racing** — the winner's effective
scope is still the intersection of the handoff scope and its own authorizations.
If the atomic decision boundary cannot be established, no acceptance occurs.

## 20. Restart recovery

A new instance never adopts a run implicitly: it appends a takeover record
carrying prior and new `runtime_instance_id`, last durable `run_state`,
`attempt_id`, last confirmed `sequence`, and the recovery decision. The last
durably recorded transition is authoritative; evidence observed but not durably
appended is treated as absent, never inferred. A bridge status query is used
where supported; unsupported, errored, timed-out, or ambiguous answers yield
`unknown`, which is never evidence of absence.

The 16-row matrix resolves every last-durable state. Rows 4, 6, 9, 11, and 14 —
every case where an external effect could be in flight and cannot be positively
excluded — resolve to `reconciliation_required` with dispatch forbidden. Rows 3,
5, 7, and 8 permit same-attempt resumption only on a definitive external status.
Terminal runs are never revived. Unreadable or inconsistent durable evidence
blocks with `evidence_state:unknown` rather than being reconstructed.

## 21. Scenario replay

All 42 scenarios were replayed against the edited model.

- **Original 32 (§38):** Scenario 15 now reaches `waiting_for_operator` through
  the listed `waiting_for_model → waiting_for_operator` transition and records
  the complete tied candidate set. Scenario 25 now resolves through the §17.4
  condition table, naming the exact condition, resulting state, reason class,
  and evidence for each branch. The remaining 30 were re-verified unchanged.
- **Additional 10 (new §38.1, scenarios 33–42):** framework emits an unknown
  event; framework writes native memory outside the bridge; model outside the
  approved provider set; provider operation while registration is unresolved;
  handoff references a superseded revision; approval expires while queued; two
  agents propose conflicting canonical updates; duplicate model responses out of
  order; cancellation and completion race; runtime restart with an attempt in an
  unknown state. Scenario 42 now resolves through the §29.3 matrix.

**Total: 42 deterministic scenarios, none requiring architectural
interpretation.** The count is stated in §38.1 and in §1.4.

## 22. Counts and terminology

Every count was **recalculated from the document's own tables**, not copied, and
recorded in new **§1.4** as normative document metrics with a rule that any
future amendment must recompute and restate them.

| Dimension | Count |
| --- | --- |
| Specification sections | 43 |
| Canonical identifiers | 15 |
| Lifecycle states (terminal / waiting / pending) | 17 (5 / 4 / 2) |
| Lifecycle transition rows | 13 |
| Forbidden-transition rules | 12 |
| Authorization facts (admission / per-invocation) | 11 (8 / 3) |
| Envelope field groups | 14 |
| Authorization sequencing steps | 8 |
| Bridge operations | 9 |
| Shared Context operations | 7 |
| Staleness conditions | 6 |
| Memory categories | 6 |
| **Context-flow trace fields** | **17** |
| Handoff kinds | 6 |
| **Handoff envelope contents** | **12** |
| Broadcast acceptance conditions | 7 |
| Tool-access stages | 7 |
| Isolation boundaries | 8 |
| Race and conflict behaviors | 8 |
| Recovery matrix rows | 16 |
| Security threats | 16 |
| **Error taxonomy rows** | **49** |
| **Error taxonomy distinct class names** | **49** |
| Operator views | 13 |
| Runtime modes | 7 |
| **Deterministic scenarios** | **42** (32 + 10) |

Normative architecture wording is implementation-neutral. The one
language-specific construct that remained is now a clearly marked non-normative
illustration.

## 23. Owner documents changed

1. `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` — additive:
   §8.1 enum member, §8.2 clause, §9.5/§9.7/§9.10 Run lifecycle sets.
2. `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` — additive:
   §5.1 three optional fields, §5.9 deduplication identity and attempt
   preservation.

Both were selected in the pre-edit decision and neither was widened beyond the
sections named in the seam record §11.

## 24. Owner documents unchanged

`MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`;
`MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`;
`MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md`;
`MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001.md`; all
`shared_context/loops/**` schemas; `shared_context/CONTEXT_GRAPH_SCHEMA.md`;
`shared_context/CONTEXT_PACK_GENERATOR_SPEC.md`;
`MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001.md`;
`shared_context/SAFETY_CONTRACT.md`; `shared_context/VALIDATION.md`;
`MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md`; both prior review
records; and both original task reports — all verified byte-identical by Git
blob ID after the commit.

## 25. Files changed

Exactly nine:

1. `docs/decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001.md` (new)
2. `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md` (remediated)
3. `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` (owner amendment)
4. `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` (owner amendment)
5. `docs/tasks/MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REMEDIATION-001.md` (new)
6. `shared_context/PROJECT_STATE.md`
7. `shared_context/ROADMAP.md`
8. `shared_context/RUN_QUEUE.md`
9. `shared_context/AGENT_HANDOFF.md`

No source file and no test file changed.

## 26. Validation

- Validator: `py -3.9 scripts/validate_project_state.py` — output and exit code
  recorded in the final execution report.
- `git diff --check`, `git status --short`, `git diff --name-only`,
  `git diff --stat` — recorded in the final execution report.
- Table counts verified programmatically against the edited document rather than
  asserted; one draft assertion (50 error rows) was corrected to the measured
  value (49) before commit.
- Immutable baselines re-verified by Git blob ID for every unchanged reviewed
  and canonical document.
- Introduced secret-pattern count: 0.
- `pytest: NOT_RUN — no source or test files changed.`
- No dependency was installed. Black, flake8, and mypy were not run and are not
  claimed passing.

## 27. Known limitations

1. **Remediation claims are unverified.** This task remediated its own reviewed
   findings; no independent party has confirmed the closures. That is the sole
   purpose of Review 002.
2. Two canonical owner documents were amended. Although both amendments are
   additive, minimal, and backward compatible, an independent reviewer should
   test that claim directly rather than accept it.
3. The framework compatibility matrix remains an architectural planning
   position. No framework was installed, imported, connected, or executed.
4. The framework-process isolation *mechanism*, run persistence, scheduling, and
   queue architecture remain deferred; §29.3 fixes the required safe states, not
   the mechanism.
5. Cloudflare `P2-04` remains unresolved by design and is not adjudicated here.
6. No runtime, bridge, scaffold, or agent exists, so no claim in the remediated
   specification has been exercised against a running system.

## 28. Exact next task

`MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-002` — an independent,
read-only re-review of the remediated architecture, the seam-decision record,
and both owner amendments. Not started, not authorized by this task, and not an
implementation task.

## 29. Explicit non-authorizations

This task authorizes none of: Agent Runtime implementation; framework bridge
implementation; Agent Package Contract, Framework Bridge Contract, or Shared
Context Bridge drafting; Agent Runtime Scaffold work; agent framework SDK
installation, vendoring, or dependency declaration; execution of any agent,
sub-agent, workflow, graph, crew, or conversation; any model-provider API call;
any tool invocation; any provider connection, authentication, credential
configuration or verification, OAuth flow, or token creation; any MCP connection
or execution; any integration-fabric connection or webhook registration;
persistence, database, or queue implementation; backend or frontend
implementation; dependency installation, workflow YAML, release, or deployment;
any push, pull request, merge, or remote branch; or any MellyTrade interaction.

Live provider work remains blocked and unauthorized. The Agent Package Contract
remains blocked pending Review 002. Migration triggers #1, #4, #5, #6, and #7
remain uncrossed.

## 30. No-push state

One local documentation commit was created on
`docs/mellycore-agent-runtime-architecture-spec-remediation-001`. It was **not**
pushed. No pull request, merge, remote branch, amend, reset, restore, stash,
clean, rebase, squash, cherry-pick, force operation, or deployment occurred.

Commit SHA: reported in the final execution report.

The global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` is unchanged, not
reordered, and not reinterpreted.
