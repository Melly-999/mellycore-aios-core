# MellyCore Agent Runtime Architecture Spec 001 — Task Report

## 1. Purpose

Create the canonical architecture specification for the MellyCore Agent
Runtime: how MellyCore AIOS represents, coordinates, isolates, observes, and
governs agents implemented with Claude Code, the OpenAI Agents SDK, LangGraph,
CrewAI, AutoGen, and custom MellyCore-compatible agents.

This is a documentation and architecture task only. No Agent Runtime code,
framework bridge, agent execution, provider call, model-provider connection,
tool execution, credential, secret, queue, persistence, frontend component, or
deployment was created.

## 2. Starting repository state

- Root: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios`
- Starting branch:
  `docs/mellycore-cloudflare-api-shield-read-only-adapter-review-002`
- Starting HEAD: `95a31316b0c4871343637a6b414f4aaa79dee76d`
- Parent: `1a9acd2f1ad7b4597bce795d5d626424f34466e2`
- Subject: `docs: verify Cloudflare adapter remediation`
- Canonical remote: `clean-origin` →
  `https://github.com/Melly-999/mellycore-aios-core.git`
- Fresh canonical main after the one authorized fetch:
  `947f33d27d5546775186e96bdc61e30db78c0b3d` (matched the expected value; no
  drift)
- Starting worktree/index: clean
- Architecture branch before creation: local absent; `clean-origin` absent
  (`git branch -a --list '*agent-runtime*'` returned nothing)
- Branch created from `95a31316b0c4871343637a6b414f4aaa79dee76d`:
  `docs/mellycore-agent-runtime-architecture-spec-001`

Exactly one network operation occurred: `git fetch clean-origin`. No later
network access occurred.

## 3. Provider-checkpoint dependency

This task consumed the provider-foundation checkpoint completed by
`MELLYCORE-CLOUDFLARE-API-SHIELD-READ-ONLY-ADAPTER-REVIEW-002`
(`PASS_WITH_NON_BLOCKING_FINDINGS`; P0 = 0, P1 = 0, P2 = 2, P3 = 1; review
commit `95a31316b0c4871343637a6b414f4aaa79dee76d`, parent
`1a9acd2f1ad7b4597bce795d5d626424f34466e2`).

It did not reopen provider implementation, did not adjudicate any Cloudflare
finding, and did not advance any provider state. Live Cloudflare work remains
blocked, unauthorized, unconnected, unauthenticated, disabled, and undeployed.

The three carried-forward findings are recorded in Section 27.

## 4. Existing-document discovery

Repository-wide read-only discovery searched all specs, ADRs, research records,
task reports, and shared-context files for: `agent runtime`, `agent package`,
`agent registry`, `framework bridge`, `shared context`, `context bridge`,
`handoff`, `run ledger`, `model router`, `model gateway`, `OpenAI Agents`,
`LangGraph`, `CrewAI`, `AutoGen`, `Claude Code`, `custom agent`, `orchestrator`,
`workflow`, `subagent`, `tool permission`, `cost`, `trace`, and `provenance`.

Overlap matrix:

| Existing document | Authority | Relevant concepts | Conflict risk | Treatment |
| --- | --- | --- | --- | --- |
| `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` | Canonical | §7.2 entities (`Agent`, `Run`, `RunEvent`, `Task`, `ContextPacket`, `MemoryRecord`, `Approval`); §8 six status dimensions; §9.1–9.7 modules incl. Agent Runtime Directory and Agent Traffic Inspector; §16 approvals; §17 secrets; §18 provenance; §19 unknown states | High | **Canonical** — reused and extended without modification |
| `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md` | Canonical | §7.5 acting identities; §11 scope; §12.1 authentication targets; §13.2 credential classes; §21.1 eight independent facts | High | **Canonical** — reused verbatim; extended to eleven runtime facts without collapsing any of the eight |
| `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` | Canonical | Enforcement boundary; §17 26-step order; §18 approval binding; §25 error taxonomy; §26.3 `INDETERMINATE` reconciliation; §29 two-stage audit; §32 seventeen-item gate | High | **Canonical** — provider/tool boundary owner; classes adopted unchanged |
| `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md` | Canonical | Tenant isolation, credential model, external-content posture | Medium | **Canonical** — inherited, not superseded |
| `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` | Canonical | §5 Unified Run Ledger; token/cost semantics; §5.8; §9 approval contract | High | **Canonical** — Run Ledger owner; Agent Runtime is a producer only |
| `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md` | Canonical | Fourteen fixture entities; truthful-state labels | Low | **Complementary** |
| `docs/specs/MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md` | Canonical | 58 capabilities; D1–D4 domains | Low | **Complementary** — not reopened |
| `docs/specs/MELLYCORE_INTEGRATION_FABRIC_COMPARISON_SPEC_001.md` | Canonical | Fabric equivalence standard | Low | **Complementary** |
| `docs/specs/MELLYCORE_CYBERSECURITY_PROVIDER_PACK_SPEC_001.md`, `MELLYCORE_MARKETING_PROVIDER_PACK_SPEC_001.md` | Canonical | Provider packs, R0–R2 ceiling | Low | **Complementary** |
| `docs/research/MELLYCORE_CLOUDFLARE_API_SHIELD_READ_ONLY_ADAPTER_REVIEW_002.md` | Canonical review | `P2-03`, `P2-04`, `P3-01` | Medium | **Canonical** — constraints carried forward, findings not adjudicated |
| `docs/research/MELLYCORE_PROVIDER_ADAPTER_SCAFFOLD_REVIEW_001.md` | Canonical review | Inert-scaffold precedent; no representable success outcome | Medium | **Canonical** — precedent reused for the inert v1 boundary |
| `docs/architecture/MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001.md`, `shared_context/loops/**` | Canonical (report-only) | Loop registry, `RUN_LEDGER_SCHEMA.json`, loop budgets | Medium | **Complementary** — loop runs are a distinct, narrower concept; not renamed or absorbed |
| `shared_context/MODEL_ROUTING.md` | Canonical (workspace) | Routing roles, OmniRoute | Low | **Complementary** — human/agent tool-role guidance, not the runtime Model Router |
| `docs/specs/MELLYCORE_OPENROUTER_MODEL_OBSERVATORY_SPEC.md` | Canonical | Static model/cost snapshot | Low | **Complementary** |
| `shared_context/CONTEXT_GRAPH_SCHEMA.md`, `CONTEXT_PACK_GENERATOR_SPEC.md`, `context_provenance/**`, `docs/specs/MELLYCORE_CONTEXT_*` | Canonical | Context provenance, sensitivity, admission gate | Medium | **Canonical** — Shared Context owner; consumed, never mutated |
| `docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md`, `MELLYCORE_HOMEPAGE_SPEC_001.md`, `MELLYCORE_UI_SECTIONS.md`, `MELLYCORE_KNOWLEDGE_GRAPH_STATIC_UI_SPEC_001.md`, `MELLYCORE_FRONTEND_SCAFFOLD_PLAN_001.md`, `MELLYCORE_OBSIDIAN_3D_PAGE_SPEC_001.md` | Canonical | Frontend surfaces | None | **Unrelated** to this task's scope |
| `docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md` | Canonical | Renderer decision | None | **Unrelated** |
| `docs/tasks/**` completed reports | Historical | Creation-time snapshots | None | **Historical** — not current-state claims |
| `archive/mellycore-operations-data-contract-001-superseded-by-v2` (branch) | Superseded | Earlier ODC scope | None | **Superseded** — untouched |

**No canonical Agent Runtime architecture exists.** No spec, ADR, or research
record owns the concern. No two accepted documents own a runtime concern
incompatibly. No ADR is silently superseded. No stop condition triggered.

## 5. Ownership decisions

| Concern | Canonical owner | Agent Runtime's role |
| --- | --- | --- |
| Provider access, credentials, provider policy order | Integration Gateway contract | Submits bounded proposals; never bypasses |
| Provider records, eight facts, acting identities, credential classes | Provider Registry contract | Reads; never registers or mutates |
| Model routing control surface | Control Plane §9.2 + future Model Router | Requests; never selects |
| Shared Context truth, admission, provenance | Shared Context Layer / Context Gate | Reads snapshots, submits proposals; never writes canonically |
| Memory categories | This specification (categories); future Shared Context Bridge (mechanism) | Scopes and isolates; never auto-promotes |
| Permissions and approval semantics | Control Plane §16 + Gateway §18 | Enforces; never self-approves |
| Agent packages | Deferred — future Agent Package Contract | States its required metadata only |
| Run Ledger record | AI Operations Intelligence §5 | Producer only; append-only |
| Task state and live sequencing | `RUN_QUEUE.md`, echoed in `AGENT_HANDOFF.md` | Consumer |
| Agent runtime coordination | **This specification** | Owner |

## 6. Agent Runtime boundary

Defined as a **control and coordination layer** (spec §7). It must not own
provider credentials, provider transport, model-provider SDK credentials,
canonical Shared Context truth, permanent external tool trust, deployment
infrastructure, or MellyTrade execution. Its relationships with the Agent
Registry, Agent Package Store, Framework Bridges, Shared Context Layer, Memory
Layer, Model Router, Provider Registry, Integration Gateway, Tool Gateway, Run
Ledger, Cost Observatory, Operator Console, and audit/provenance systems are
fixed in spec §7.3.

## 7. Supported frameworks

Six, as a closed `framework_type` vocabulary: `claude_code`,
`openai_agents_sdk`, `langgraph`, `crewai`, `autogen`, `mellycore_custom`.
There is no `other`, `generic`, or `auto` member; an unknown value denies with
`UNSUPPORTED_FRAMEWORK`.

## 8. Lifecycle model

Seventeen `run_state` values (spec §12.2), reconciled with Control Plane §8 by
declaring `run_state` a **typed entity field**, not a seventh status dimension
— consistent with Control Plane §7.1's rule that domain fields are not
additional status dimensions. Its machine identity is the field-qualified pair.
A projection table maps every `run_state` to the canonical `lifecycle_status`.

Five terminal states (`completed`, `failed`, `cancelled`, `timed_out`,
`blocked`); four waiting states; two pending states
(`cancellation_requested`, `reconciliation_required`). Allowed transitions,
nine forbidden transitions, and a mandatory transition-evidence record with
separate `observed_at` / `recorded_at` are fixed in §12.3–12.5.

## 9. Identity model

Fifteen identifiers (§8.1), all immutable, tenant-scoped, opaque, exact-match
only, alias-free at runtime boundaries, and revision-preserving. Canonical
serialization, exact built-in primitive typing, subclass rejection or canonical
conversion, `repr()`-independent encoding, type-tagged fields, and
collision-resistant digests over normalized bytes are fixed in §8.3.

## 10. Execution envelope

Immutable, framework-neutral, digest-bound (§15). Fourteen field groups cover
identity, isolation, agent, intent, routing, context, memory, permissions,
limits, authorization, audit, cost, behavior, and integrity. Credentials, raw
secrets, environment variables, provider tokens, and complete sensitive context
bodies are prohibited contents.

## 11. Authorization facts

**Eleven**, conjunctive and independently established, evidenced, and revoked
(§14). Registry §21.1's eight provider facts remain exactly eight, unmodified;
fact 10 delegates to them entirely. No `ready` boolean, no collapsing field, no
implication between facts. Facts 1–10 are standing state; fact 11 is
per-operation and digest-bound.

## 12. Shared Context model

Seven separate operations (§17.1): `read_snapshot`, `propose_update`,
`append_evidence`, `create_derived_context`, `request_canonical_mutation`,
`create_handoff_context`, `invalidate_derived_context`. Agents never write
canonical state. Context availability is not context-access authorization.
Conflicts are surfaced, never silently resolved.

## 13. Memory model

Six separated categories (§18): immutable run context, short-term working
memory, agent-local memory, shared derived memory, canonical project context,
and operator-approved long-term memory, each with explicit read/write/propose/
persist/share/discard rules. Framework-native memory is category 2 at most and
never becomes canonical automatically. Memory existence is not permission to
read or write it.

## 14. Handoff model

Six kinds (§20.1); eleven required envelope contents (§20.2). Receiving is not
accepting — the recipient's runtime independently evaluates the eleven facts
and records an explicit acceptance or rejection. A handoff never widens the
recipient's permissions; the effective scope is an intersection. Handoff
content is untrusted. Duplicates are suppressed by canonical digest. Budget is
carved from the parent, and depth is bounded.

## 15. Tool model

Seven separated stages (§21.1): discovered, registered, capability declared,
contract revision pinned, authorized, runtime enabled, invocation approved.
Tool discovery is not registration; registration is not authorization. Input
validation precedes dispatch; output validation precedes use. Unknown tools
deny and are never redirected.

## 16. Provider model

One path only: Agent → Agent Runtime → Provider Registry resolution →
Integration Gateway → accepted adapter → provider (§22.1). The runtime never
selects credentials, reads provider secrets, executes provider-native
fallbacks, infers authentication modes, or bypasses scope validation. Agents
produce **proposals**, never executed operations.

## 17. Model-routing boundary

The runtime requests; the Model Router decides; the runtime records and
enforces (§23). Eight requestable dimensions. Seven routing artifacts including
a mandatory explanation with rejected alternatives. No automatic fallback may
cross a sensitivity boundary, provider boundary, quality floor, cost ceiling,
or approved-model set. No permitted model yields `NO_PERMITTED_MODEL` and
`blocked`; an unresolved tie yields `waiting_for_operator`.

## 18. Run Ledger

Owned by AI Operations Intelligence §5; the Agent Runtime is a producer only
(§25). Fourteen append-only record kinds. Corrections supersede, never edit.
The ledger is evidence, not necessarily canonical business state.
`operator_approved` is not authority. Audit-reservation failure blocks
consequential work.

## 19. Cost and token accounting

Estimates and actuals are separate fields, separately sourced, never merged
(§24). An estimate is not a billing fact. Unknown pricing stays `null` with
`INSUFFICIENT_PRICING_DATA`, never zero. A budget over unknown pricing is
unenforceable. Expired pricing evidence is not authority. Estimate-exceeding
budget denies before execution.

## 20. Cancellation and retry

Cancellation request, acknowledgement, framework support, external-effect
uncertainty, forced local stop, and reconciliation-required are six distinct
concepts (§27). A cancellation request is not a stop; a forced local stop is
not proof external effects stopped; a timeout with unknown outcome is
`reconciliation_required`, not `timed_out`. No consequential provider or tool
action is retried blindly; a retry is not permission to repeat a consequential
action (§28).

## 21. Isolation

Eight boundaries (§29.1): tenant, run, agent-local state, framework-process,
context namespace, memory, tool-session, and provider-session. Six race and
conflict behaviors are specified (§29.2), including concurrent context
proposals, stale snapshots, duplicate handoffs, competing approvals, and
cancellation races.

## 22. Human approval

Ten trigger conditions (§30.1). Approval must be scoped, time-bound,
revision-bound, action-bound, and auditable (§30.2). No self-approval, blanket
approval, inferred consent, replay, hidden side effect, autonomous
safety-policy change, or permission widening — reused unchanged from Control
Plane §16.2 and Gateway §18.3.

## 23. Security model

Sixteen threats, each with prevention, detection, fail-closed result, and audit
evidence (§31): prompt injection, tool-result injection, context poisoning,
malicious agent package, framework bridge drift, model substitution, tenant
confusion, credential exfiltration, excessive context disclosure, unsafe retry,
forged provenance, digest collision, malicious primitive subclass, arbitrary
object representation, cost exhaustion, and infinite agent loops.

## 24. Observability

Thirteen operator views with explicit "must expose" and "must never imply"
columns (§34). **Information architecture only** — no component, route,
framework, or styling is defined, and no frontend work was performed.

## 25. Framework compatibility

A 6 × 13 matrix with five statuses (§35). Every cell is explicitly labelled an
architectural planning position, not a verified capability test. No framework
was installed, imported, connected, or executed. Cells marked `requires
research` decline to assert a position without evidence; each cell must be
independently validated by the Framework Bridge Contract task.

## 26. Deterministic scenarios

**32 scenarios** (§38), each with relevant facts, expected `run_state`,
expected decision, denial or transition reason class, audit record, and
reconciliation requirement. Five scenarios (19, 20, 21, 23, 30) produce an open
reconciliation obligation. None requires architectural interpretation.

## 27. Cloudflare Review 002 constraints

| Finding | Carried forward as |
| --- | --- |
| `P2-03` — a `str` subclass passed fixture validation, escaped normalization, and produced a demonstrated digest collision via `repr()` | Spec §8.3: exact built-in primitive types at trust boundaries; rejection or canonical conversion of subclasses; serialization independent of `repr()` and every overridable object protocol; deterministic hashing over normalized bytes; type-tagged fields; no provenance, deduplication, cache, handoff, or run identity from arbitrary object representations; collision-resistant digest rules; collisions are security events. Applies to run fingerprints, context-block hashes, artifact references, handoff envelopes, tool-result identities, model-response identities, audit records, and replay records. Scenarios 27 and 28 |
| `P2-04` — Registry §26.1 records Cloudflare `supported_auth_modes` as scoped `api_token` while delegated capability classes require `delegated_oauth` | Spec §22.5: **not resolved here**. No assumption of Cloudflare delegated authentication; no descriptor treated as registered or executable; no agent bound to a Cloudflare authentication mode; all provider operations must pass Provider Registry and Integration Gateway; registration-time compatibility validation required before runtime use; live provider operations remain blocked. Recorded explicitly as requiring resolution or formal adjudication **before** provider registration, credential configuration, credential verification, live Cloudflare transport, and delegated Cloudflare execution. Scenario 29 |
| `P3-01` — malformed reference shapes were denied with a sensitive-value error code | Spec §33: distinct classes for invalid reference shape, invalid canonical type, sensitive value rejected, unsupported value, authorization denial, runtime-disabled denial, provider-disabled denial, external-content rejection, and reconciliation required. Structurally invalid input is never collapsed into a sensitive-data error |

## 28. Files changed

Exactly six:

1. `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md` (new)
2. `docs/tasks/MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001.md` (new)
3. `shared_context/PROJECT_STATE.md` (modified)
4. `shared_context/ROADMAP.md` (modified)
5. `shared_context/RUN_QUEUE.md` (modified)
6. `shared_context/AGENT_HANDOFF.md` (modified)

No source file, test file, canonical provider document, or prior review was
changed. Every existing canonical document remains immutable.

## 29. Validation

- Validator: `py -3.9 scripts/validate_project_state.py` — output and exit code
  recorded in the final execution report.
- `git diff --check`, `git status --short`, `git diff --name-only`,
  `git diff --stat` — recorded in the final execution report.
- Specification section count: 43
- Frameworks covered: 6
- Lifecycle `run_state` count: 17
- Deterministic-scenario count: 32
- Error-category count: 38 Agent Runtime-layer classes, added on top of the
  Gateway §25.2 set, which is adopted unchanged and not restated
- Overlap/conflict count: 20 documents assessed; 0 blocking conflicts
- Introduced secret-pattern count: 0
- `pytest: NOT_RUN`
- Reason tests were not applicable: this task changes no source or test file
  and introduces no executable behavior. The repository's existing suite is
  unaffected by a documentation-only change, and running it would produce no
  evidence about this change. It is reported as `NOT_RUN`, never as passing.
- No dependency was installed. Black, flake8, and mypy were not run and are not
  claimed passing.

## 30. Known limitations

1. The Section 35 framework compatibility matrix is an architectural planning
   position, not verified capability testing. No framework SDK was installed,
   imported, connected, or executed, so no cell is evidence of a framework's
   actual behavior. Five dimensions are marked `requires research` rather than
   asserted.
2. The Agent Package Contract, Framework Bridge Contract, and Shared Context
   Bridge are deferred. This specification fixes only the boundaries and
   minimum expectations placed on them, so it can be reviewed before those
   contracts exist.
3. The framework-process isolation *mechanism* (process, container, or
   interpreter boundary) is deferred; only the isolation *requirement* is
   fixed.
4. Run persistence, scheduling, and queue architecture are deferred.
5. Cloudflare `P2-04` remains unresolved by design; this task carries it
   forward as a provider-registration constraint and does not adjudicate it.
6. No runtime, bridge, scaffold, or agent exists, so no claim in this
   specification has been exercised against a running system.

## 31. Exact next task

`MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-001` — an independent,
read-only architecture review. It is not started, not authorized by this task,
and not an implementation task.

## 32. Explicit non-authorizations

This task authorizes none of: Agent Runtime implementation; framework bridge
implementation; agent framework SDK installation, vendoring, or dependency
declaration; agent, sub-agent, workflow, graph, crew, or conversation
execution; any model-provider API call; any tool invocation; any provider
connection, authentication, credential configuration or verification, OAuth
flow, or token creation; any MCP connection or execution; any
integration-fabric connection or webhook registration; persistence, database,
or queue implementation; backend or frontend implementation; dependency
installation, workflow YAML, release, or deployment; any push, pull request,
merge, or remote branch; or any MellyTrade interaction.

Implementation tasks remain blocked pending independent architecture review.
Live provider work remains deferred and blocked. Migration triggers #1, #4, #5,
#6, and #7 are implicated by later phases of this architecture and are not
crossed by this task.

## 33. No-push status

One local documentation commit was created on
`docs/mellycore-agent-runtime-architecture-spec-001`. It was **not** pushed. No
pull request, merge, remote branch, amend, reset, restore, stash, clean,
rebase, squash, cherry-pick, force operation, or deployment occurred.

Commit SHA: reported in the final execution report.

The global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` is unchanged, not
reordered, and not reinterpreted.
