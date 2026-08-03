# MellyCore Agent Runtime Architecture Spec Review 001 — Task Report

## 1. Purpose

Perform an independent, read-only architecture, security, consistency, and
implementability review of
`docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md`, created by commit
`17da8603fbe8b75082cfea44223745b3c63f14de`, and issue one defensible
architecture-gate decision.

The reviewer did not author the specification. Every architectural claim was
treated as unverified until independently confirmed from the specification
text, the canonical MellyCore contracts, and deterministic scenario replay. The
review did not optimize for producing a PASS and did not repair any finding.

This is a documentation and review task only. No Agent Runtime code, framework
bridge, agent execution, provider call, model-provider connection, tool
execution, credential, secret, queue, persistence, frontend component, or
deployment was created.

## 2. Starting repository state

- Root: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios`
- Starting branch: `docs/mellycore-agent-runtime-architecture-spec-001`
- Starting HEAD: `17da8603fbe8b75082cfea44223745b3c63f14de`
- Parent: `95a31316b0c4871343637a6b414f4aaa79dee76d`
- Subject: `docs: define agent runtime architecture`
- Canonical remote: `clean-origin` →
  `https://github.com/Melly-999/mellycore-aios-core.git`
- Fresh canonical main after the one authorized fetch:
  `947f33d27d5546775186e96bdc61e30db78c0b3d` — matched the expected value; **no
  drift**
- Starting worktree/index: clean
- Review branch before creation: absent locally; absent on `clean-origin` and
  `origin`
- Branch created from `17da8603fbe8b75082cfea44223745b3c63f14de`:
  `docs/mellycore-agent-runtime-architecture-spec-review-001` (not from
  `clean-origin/main`)

Exactly one network operation occurred: `git fetch clean-origin` (exit code
`0`), during the canonical remote gate. No later network access of any kind
occurred.

## 3. Reviewed commit

`17da8603fbe8b75082cfea44223745b3c63f14de` — `docs: define agent runtime
architecture`, parent `95a31316b0c4871343637a6b414f4aaa79dee76d`. Independently
confirmed to contain **exactly six paths**, with no source file, test file,
canonical provider document, or prior review record.

## 4. Reviewed files

1. `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md` (1,502 lines)
2. `docs/tasks/MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001.md` (382 lines)
3. `shared_context/PROJECT_STATE.md`
4. `shared_context/ROADMAP.md`
5. `shared_context/RUN_QUEUE.md`
6. `shared_context/AGENT_HANDOFF.md`

## 5. Canonical cross-check sources

Control Plane spec (§7.1, §7.2, §7.3, §8.1, §8.2, §9.1–§9.7, §19); Provider
Registry contract extension (§21.1–§21.5); Integration Gateway security contract
(§17, §25, §26, §32); AI Operations Intelligence spec (§5.1–§5.9); Operations
Data Contract spec; Enterprise Provider ADR; Integration Fabric Comparison spec;
Context Provenance and Sensitivity spec (§5); Loop Operations Architecture
(§4.8); `shared_context/SAFETY_CONTRACT.md`, `VALIDATION.md`,
`MODEL_ROUTING.md`, `CONTEXT_GRAPH_SCHEMA.md`, `CONTEXT_PACK_GENERATOR_SPEC.md`;
`shared_context/loops/RUN_LEDGER_SCHEMA.json`, `LOOP_STATE_SCHEMA.json`,
`LOOP_REGISTRY.json`; Cloudflare API Shield Read-Only Adapter Review 002;
Provider Adapter Scaffold Review 001.

The specification's own overlap matrix was not relied on; it was treated as a
claim to be checked.

## 6. Independent method

Repository identity gate before any read of the artifact; canonical remote gate
with one authorized fetch and fresh verification of `clean-origin/main`;
immutable baselines recorded as Git blob IDs before any edit; review branch
created from the reviewed commit; every numeric claim recounted directly from
the specification text; all matrices rebuilt independently and compared against
the canonical owners; the lifecycle graph reconstructed as an explicit adjacency
list and tested for terminal closure, exits, and reachability of every state
each normative section demands; all 32 original scenarios and 10 additional
adversarial scenarios replayed; severity assigned strictly by the task's
definitions; post-edit re-verification that every reviewed document remained
byte-identical.

## 7. Immutable baselines

Seventeen canonical blob IDs plus the four shared-context blob IDs were recorded
before any edit and are listed in full in the review record, Section 9. Every
reviewed and cross-checked document was re-verified byte-identical after the
review commit. The architecture specification
(`0039230452b50c60e276feeec3ebda0e4e6042f7`) and its task report
(`92c0cba76837c03bfd2557f9ca2957e566824de3`) are unchanged.

Independently recounted dimensions matched the claims for: 43 sections; 6
frameworks; 15 identifiers; 9 separation states; 17 lifecycle states with 5
terminal, 4 waiting, and 2 pending; 11 authorization facts; 14 envelope field
groups; 9 bridge operations; 7 Shared Context operations; 6 memory categories; 6
handoff kinds; 7 tool stages; 8 routing dimensions; 7 routing artifacts; 14
ledger record kinds; 12 event categories; 8 isolation boundaries; 6 race
behaviors; 10 approval triggers; 16 security threats; 13 operator views; a 6 × 13
compatibility matrix; 7 runtime modes; 32 scenarios; 5 reconciliation-bearing
scenarios; 20 documents in the overlap matrix; and the three carried-forward
Cloudflare constraints. Three counts did not match and are recorded as `P3-01`
(context-flow trace is 16 fields, not 17), `P3-02` (handoff envelope contents
are 12, not 11), and `P3-03` (38 error rows carry 40 distinct class names).

## 8. Ownership result

Twenty concerns assessed: **13 `CONSISTENT`, 2 `COMPLEMENTARY`, 2 `AMBIGUOUS`,
3 `CONFLICTING`.**

Conflicting: the `lifecycle_status` projection versus Control Plane §8.2 and
§9.5/§9.7 (`P1-01`); authorization facts 5 and 6 versus Registry §21.3's
provider-scoped record types (`P1-02`); attempt evidence versus AI Operations
Intelligence §5.1/§5.9 record identity and deduplication (`P1-03`). Ambiguous:
agent-run identity form versus the existing run-ledger `run_id` form, and agent
runs versus loop runs (`P2-03`).

The architecture task report's claim of "0 blocking conflicts" is **not**
independently confirmed.

## 9. Lifecycle result

All 17 states reconstructed with predecessors, successors, terminal and waiting
classification, evidence, actor, and reconciliation implications. Verified:
every non-terminal state has a safe exit; terminal states have zero successors;
`reconciliation_required` cannot become terminal without a recorded
reconciliation outcome; `cancellation_requested` is never treated as
`cancelled`; `timed_out` is never used when an external outcome is unknown;
`blocked` and `failed` are distinct; waiting states do not imply continued
external execution; transition evidence is complete with separate `observed_at`
and `recorded_at`; and the `actor` vocabulary correctly excludes `agent`,
`model`, `tool`, and `provider`.

**One defect:** §23.6 mandates `run_state:waiting_for_operator` for an
unresolved routing tie, but §12.3 does not permit that transition from
`waiting_for_model`, which §12.2 defines as the state for awaiting a routing
decision (`P1-04`). Projection into `lifecycle_status` is mechanically total but
not conforming to the canonical owner (`P1-01`).

## 10. Authorization-fact result

Registry §21.1's eight facts remain exactly eight and unmodified; no aggregate
readiness boolean is permitted; the four canonical non-implications are stated
explicitly; fact 11 is per-operation and digest-bound; `authorization_status` is
a computed, never-stored view matching Registry §21.2 rule 5. Facts 1–4 and
7–11 pass independent review.

**Facts 5 and 6 fail.** Registry §21.3 defines `tenant_provider_authorization`
and `tenant_capability_authorization` as provider-scoped records requiring a
`provider_id`, and fact 10 already delegates entirely to all eight Registry
facts — so facts 5 and 6 are either duplicates nested inside fact 10, or
agent-scoped facts with no defined record type or owner. §14 also does not state
which capability vocabulary fact 6 evaluates (`P1-02`).

## 11. Execution-envelope result

All 14 field groups present and correct. The envelope binds every dimension the
review required, prohibits credentials, raw secrets, environment variables,
provider tokens, OAuth grants, account identifiers, connection strings, and
complete sensitive context bodies, carries sensitive context by reference
resolved at the point of use, is immutable once an attempt starts, requires a
new attempt and re-evaluation of Section 14 on change, rejects rather than
repairs on digest failure, and fails closed on absence.

**One under-specification:** `model_routing_decision_ref` is nullable "until
decided", but routing decisions are step-scoped and therefore occur after the
envelope is frozen and digest-bound (`P2-02`).

## 12. Framework Bridge result

All 9 minimum operations defined with fail-closed behavior. Every required
bridge dimension is covered for all six frameworks. No framework-native
convenience feature can bypass the Model Router, the Tool Gateway, the
Integration Gateway, canonical context writes, canonical memory persistence,
retry self-authorization, or agent self-spawning. Honest capability reporting is
mandatory and silence is explicitly not a capability claim. The 6 × 13
compatibility matrix is repeatedly and correctly labelled a planning position
rather than verified capability testing; this review verified nothing about any
framework and installed, imported, connected, and executed none. **No finding.**

## 13. Shared Context result

Seven operations genuinely distinct in effect and required authority; agents
never write canonical state; canonical mutation has a separate approval-bound
authority; concurrent proposals are both recorded and neither auto-applied;
provenance survives transformations and sensitivity does not decay; access is
tenant- and sensitivity-scoped with denials that do not reveal existence;
unavailable context is never silently substituted and untraced context is
treated as absent; rejection is auditable. `sensitivity_level` correctly reuses
the canonical vocabulary rather than a parallel scale.

**One gap:** stale-snapshot resolution is selected by a policy that is never
defined, required to be declared, or required to be deterministic (`P2-01`).

## 14. Memory result

Six categories remain distinct across owner, duration, persistence,
shareability, canonical status, read authority, write authority, promotion path,
and expiry. Existence is never permission. Framework-native memory —
LangGraph checkpoints, CrewAI crew memory, AutoGen conversation history, OpenAI
Agents SDK session state, Claude Code session context — is category 2 at most,
bridge-local, never automatically canonical, never crossing a run boundary
without explicit normalized admission, and never crossing a tenant boundary at
all. Each promotion requires an explicit, separately authorized step with its own
evidence. **No finding.**

## 15. Handoff result

Receipt is not acceptance; acceptance and rejection are explicit and recorded;
the recipient's permissions are never widened and the effective scope is an
intersection; a sender cannot grant what it does not own; context references are
revision-bound; the output contract, budget, and deadline are explicit; budget
is carved from the parent and children never exceed it; duplicates are
suppressed by canonical digest and return the recorded decision; cancellation
propagates per declared policy; delegation depth is bounded; broadcast creates
no implicit acceptance; handoff content is untrusted data and an instruction
inside it is never an authorization.

**One gap:** concurrent acceptance of one broadcast proposal has no specified
race behavior, unlike the five races §29.2 does specify (`P2-04`).

## 16. Tool/provider result

Seven tool stages separated with an explicit "does not mean" column; arguments
validated against the pinned contract revision under §8.3 type discipline before
dispatch; results validated and classified before use, and only as data; unknown
tools deny and are never redirected; consequential unknown outcomes yield
`EXTERNAL_OUTCOME_UNKNOWN` and `reconciliation_required`, never a blind retry.

One provider path only, with no fallback and no emergency path; the runtime
never selects credentials, reads or forwards provider secrets, executes a
provider-native fallback, infers an authentication mode, bypasses scope
validation, re-implements Gateway policy, or presents a proposal as an executed
operation; agents produce bounded, typed, digest-bound proposals carrying no
credential; the Gateway independently re-derives every authorization input. A
direct credential request is refused without echo. **No finding.**

Cloudflare `P2-04` is carried forward as an unresolved provider-registration
constraint and is not treated as discharged. The provider checkpoint is
correctly not treated as live-provider readiness: the Gateway §32 seventeen-item
gate is required and none of it currently passes.

## 17. Model Router result

The runtime requests and never decides; the router produces a decision plus a
complete explanation including rejected alternatives; substitution is governed;
no automatic fallback may cross a sensitivity, provider, quality, cost, or
approved-set boundary; no permitted model blocks rather than degrading; an
unresolved tie escalates rather than picking arbitrarily; operator override is
bounded and audited; pricing uncertainty stays unknown rather than zero.
Consistent with Control Plane §9.2's routing precedence and §19's no-eligible-route
handling; `shared_context/MODEL_ROUTING.md` is correctly treated as complementary
tool-role guidance rather than a competing contract.

**The tie outcome's run state is unreachable from the state the specification
itself assigns to awaiting a routing decision** (`P1-04`).

## 18. Ledger/event result

The specification correctly declines to own the ledger record and positions
itself as an append-only producer of 14 record kinds, with corrections that
supersede rather than edit, evidence distinguished from canonical business
truth, `operator_approved` not authority, and audit-reservation failure blocking
consequential work. Events carry stable versioned schemas, a closed
`source_identity`, monotonic per-attempt `sequence` with gaps surfaced as
`evidence_state:partial`, separate observed and recorded times, no raw secrets,
and explicit `unmapped` events that are never dropped.

**One conflict:** AI Operations Intelligence §5.9 deduplicates by `run_id` and
§5.1 carries one `outcome`/`model`/`provider` per run, while this specification
introduces multiple attempts per `run_id` and requires every attempt's ledger
records to remain intact and addressable — never reconciled, and not amendable
by a declared non-owner (`P1-03`). Related: agent-run identity is not reconciled
with the existing run-ledger `run_id` form or with loop runs (`P2-03`).

## 19. Cancellation/retry result

The six cancellation concepts are genuinely distinct and the model does not
overclaim: a request is not a stop, a forced local stop is not proof external
effects stopped, `cancelled` requires confirmation that every in-flight external
effect did not occur or was reverted, a timeout with any unknown outcome is
`reconciliation_required`, and no guarantee is asserted that a framework, tool,
or provider cannot provide.

The seven retry concepts are distinct; no consequential action is retried
blindly; unknown outcomes require a fresh authoritative read, comparison against
the approved after-state, verification evidence on success, a new proposal and
approval if not applied, and `PARTIAL_APPLICATION` with the exact partial state
if partially applied; fact 11 is evaluated afresh per consequential attempt;
idempotency keys are canonical and never shared across tenants, runs, or
intended actions; `reconciliation_required` is an open obligation, neither
failure nor success. **No finding.**

## 20. Isolation result

All 8 boundaries reviewed and correct: tenant (absolute, denying without
revealing existence), run, agent-local state, framework-process, context
namespace, memory namespace, tool session, provider session. Five race
behaviors are correctly specified. No global mutable framework state may
silently become trusted canonical state.

**Two gaps:** concurrent broadcast acceptance (`P2-04`) and runtime-instance
failure or restart with an attempt in an unknown state (`P2-05`).

## 21. Security result

All 16 threat rows carry prevention, detection, fail-closed result, and audit
obligation, and cover every concern the review required, including
agent-to-agent injection (via the prompt-injection row plus §32 rule 1),
malicious primitive subclasses, arbitrary object representation, digest
collision, forged provenance, cost exhaustion, and infinite loops. Audit
evidence is content-free wherever content would be sensitive. External content
— including other agents' output, agent-generated code, prompts, plans, and tool
arguments — is untrusted until classified and validated, quarantine is terminal,
and instruction-bearing content never changes policy, permissions, routing,
budgets, or run state. **No finding.**

Canonical serialization and digest discipline (`P2-03` carried forward from
Cloudflare Review 002) is the strongest part of the specification and passes
independent review on all eight rules.

## 22. Error result

Gateway §25.2 classes are adopted unchanged and not fragmented; `STALE_STATE`,
`CONTRACT_CONFLICT`, `APPROVAL_STALE`, `AUDIT_RESERVATION_FAILED`,
`PARTIAL_APPLICATION`, `INDETERMINATE`, and `INJECTION_SUSPECTED` were each
independently confirmed to resolve to a canonical owner, so no scenario cites an
undefined class. `P3-01` from Cloudflare Review 002 is correctly discharged:
structurally malformed input, invalid canonical type, and sensitive-value
rejection are three distinct classes. Every class the review required to remain
distinct is distinct. Outward classes are coarse while audit records carry the
precise inward denial reason. No error, event, summary, export, or audit record
may contain a raw sensitive value.

Counting note only: 38 rows carry 40 distinct class names (`P3-03`), and
`INSUFFICIENT_PRICING_DATA` appears in no taxonomy anywhere in the repository
(`P3-04`).

## 23. Scenario result

**Original 32: 30 resolve deterministically.** Scenario 15 does not — the
mandated `waiting_for_operator` outcome is unreachable from `waiting_for_model`
(`P1-04`). Scenario 25 is policy-conditioned with an undefined policy
(`P2-01`).

**Additional 10 (scenarios 33–42): 9 resolve.** Scenario 42 — runtime restarts
with an attempt in an unknown state — does not (`P2-05`).

The architecture task report's claim that "none requires architectural
interpretation" is **not** independently confirmed.

## 24. Implementability result

Thirteen of fifteen Agent Package Contract concerns can be specified from the
architecture as written. Two cannot: `declared_capabilities` and
`permission_requirements` both intersect downward with authorization records
whose scope and vocabulary are ambiguous (`P1-02`). A Package Contract author
additionally needs to know how a package revision's runs are projected into
canonical lifecycle status (`P1-01`) and recorded in the Run Ledger (`P1-03`),
and a Framework Bridge Contract author needs the routing-tie transition
(`P1-04`) and the envelope's routing-decision binding (`P2-02`).

**The downstream Agent Package Contract cannot be written entirely without
architectural interpretation.**

## 25. Finding counts

| Severity | Count | IDs |
| --- | --- | --- |
| **P0** | **0** | — |
| **P1** | **4** | `P1-01` `lifecycle_status:active` projection conflicts with Control Plane §8.2 and §9.5/§9.7; `P1-02` authorization facts 5 and 6 duplicate Registry facts 5 and 6 with undefined scope; `P1-03` attempt evidence contradicts AI Ops §5.1/§5.9 ledger record identity and deduplication; `P1-04` lifecycle cannot express the routing-tie outcome §23.6 mandates |
| **P2** | **5** | `P2-01` undefined stale-snapshot policy; `P2-02` `model_routing_decision_ref` inside an immutable envelope; `P2-03` agent-run identity vs. existing run-ledger form and loop runs; `P2-04` concurrent broadcast acceptance unspecified; `P2-05` runtime-instance restart unaddressed |
| **P3** | **5** | `P3-01` trace is 16 fields not 17; `P3-02` handoff envelope contents are 12 not 11; `P3-03` 38 rows carry 40 class names; `P3-04` `INSUFFICIENT_PRICING_DATA` undefined and nine-state/eleven-fact mapping unstated; `P3-05` Python-specific phrasing in a language-neutral architecture |

## 26. Gate decision

### `FAIL_REMEDIATION_REQUIRED`

Four P1 findings exist. PASS is impossible with any P0 or P1 outstanding.
Canonical ownership is not unambiguous, one lifecycle transition requires
interpretation, two authorization facts are duplicated with undefined scope, two
of thirty-two original scenarios do not resolve deterministically, and the
downstream Agent Package Contract cannot be written without architectural
interpretation.

The decision is narrow. No P0 exists: no direct credential or provider path, no
cross-tenant execution possibility, no canonical-context mutation bypass, no
authorization or approval bypass, no secret exposure, and no unsafe consequential
retry was found. The canonical serialization and digest discipline,
package/runtime separation, framework-bridge prohibitions, memory categories,
handoff acceptance model, single provider path, cancellation honesty, retry and
reconciliation rules, isolation boundaries, approval properties, security model,
external-content posture, runtime modes, and inert v1 boundary all pass
independent review without a finding. The four P1s are seam conflicts — three
against canonical owners, one internal to the lifecycle — not defects in the
safety model.

## 27. Agent Package eligibility

`MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001` is **not eligible** for
authorization. Downstream Agent Runtime documents — Agent Package Contract,
Framework Bridge Contract, Shared Context Bridge, Agent Runtime Scaffold, first
Agent Package, Cross-Agent Smoke, and Integration Review — **remain blocked**.
Agent Runtime implementation remains blocked.

## 28. Exact next task

`MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REMEDIATION-001` — a bounded
documentation remediation of `P1-01` through `P1-04`, with `P2-01`–`P2-05` and
`P3-01`–`P3-05` addressed or explicitly adjudicated. Not started, not authorized
by this review, and not an implementation task. `P1-01` and `P1-03` may require a
companion amendment to the canonical owner documents under those documents' own
amendment rules rather than a unilateral change to the Agent Runtime
specification; that choice belongs to the Operator.

## 29. Shared-context updates

Bounded updates to exactly four files, recording the review outcome, the finding
counts, the gate decision, the blocked downstream state, and the exact next
task:

1. `shared_context/PROJECT_STATE.md`
2. `shared_context/ROADMAP.md`
3. `shared_context/RUN_QUEUE.md`
4. `shared_context/AGENT_HANDOFF.md`

The global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` is unchanged, not
reordered, not replaced, and not reinterpreted.

## 30. Validation

- Validator: `py -3.9 scripts/validate_project_state.py` — output and exit code
  recorded in the final execution report.
- `git diff --check`, `git status --short`, `git diff --name-only`,
  `git diff --stat` — recorded in the final execution report.
- Files changed: exactly six, all within the approved allowlist.
- Architecture specification, architecture task report, and all fifteen
  canonical cross-check documents re-verified **byte-identical** by Git blob ID.
- No source file, test file, canonical provider document, or prior review was
  changed.
- Review record sections: 54. Reviewed documents: 6 reviewed + 17 canonical
  cross-check sources. Ownership results: 20. Lifecycle states accounted for:
  17/17. Authorization facts accounted for: 11/11. Frameworks reviewed: 6/6.
  Original scenarios replayed: 32/32. Additional scenarios replayed: 10/10.
- Introduced secret-pattern count: 0.
- `pytest: NOT_RUN`
- Reason tests were not applicable: this review changes no source or test file
  and introduces no executable behavior. The repository's existing suite is
  unaffected by a documentation-only change and would produce no evidence about
  it. It is reported as `NOT_RUN`, never as passing.
- Unavailable validators: Black, flake8, and mypy were not run and are not
  claimed passing. No dependency was installed.

## 31. Explicit non-authorizations

This review authorizes none of: Agent Runtime implementation; framework bridge
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

Live provider work remains blocked and unauthorized. Migration triggers #1, #4,
#5, #6, and #7 remain uncrossed by this review.

## 32. No-push state

One local documentation commit was created on
`docs/mellycore-agent-runtime-architecture-spec-review-001`. It was **not**
pushed. No pull request, merge, remote branch, amend, reset, restore, stash,
clean, rebase, squash, cherry-pick, force operation, or deployment occurred.

Commit SHA: reported in the final execution report.

The global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` is unchanged, not
reordered, and not reinterpreted.
