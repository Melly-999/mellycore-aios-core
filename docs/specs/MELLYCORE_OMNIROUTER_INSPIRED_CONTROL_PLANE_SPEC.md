# MellyCore OmniRouter-Inspired Control Plane Specification

**Spec ID:** `MELLYCORE-OMNIROUTER-INSPIRED-CONTROL-PLANE-SPEC-001`
**Version:** 1.0
**Status:** `SPEC_ONLY` · `CONTROL_PLANE_ONLY` · `STATIC_DEMONSTRATION_PLANNED` ·
`RUNTIME_NOT_IMPLEMENTED` · `NO_PROVIDER_CONNECTIONS` · `NO_SECRETS` ·
`NO_LIVE_EXECUTION` · `NO_DEPLOY`

This is the canonical product, information-architecture, interaction, safety,
and frontend contract for a future MellyCore AIOS Control Plane. It creates no
frontend, backend, runtime, integration, authentication, database, provider
connection, model call, agent run, tool action, deployment, or 3D renderer.

Normative terms `MUST`, `MUST NOT`, `SHOULD`, and `MAY` describe future
implementation obligations. They do not claim that the described capability
exists today.

## 1. Executive Summary

The MellyCore AIOS Control Plane is the operator-facing coordination and
governance layer above future runtime integrations. It makes the AI estate,
routing intent, shared context, agent contracts, run evidence, cost, queues,
artifacts, approvals, recommendations, and security boundaries visible and
inspectable without performing the underlying work.

The current phase supports specification of:

- inspection and evidence review;
- policy definition and conflict detection;
- deterministic routing simulation and dry-run explanations;
- context-packet assembly previews;
- batch and artifact planning;
- explicit approval contracts;
- static demonstrations and unavailable-runtime states.

It does not support provider calls, model calls, agent launches, tool execution,
integration connections, account usage, persistence, streaming, retries,
authentication, or artifact generation. Those belong to a separately specified,
separately approved future Data Plane.

The frontend is ready to implement a truthful static Control Plane when it can
render every state and workflow in this document without inventing product
behavior. A static implementation MUST identify itself as a demonstration and
MUST keep unavailable runtime data visibly unavailable.

## 2. Product Positioning

### 2.1 Canonical positioning

> MellyCore AIOS Control Plane is a safety-first, operator-controlled
> coordination and governance surface for inspecting an AI estate, planning
> routes and context, reviewing evidence, and approving narrowly scoped future
> actions.

It sits inside MellyCore's established identity as a local-first,
operator-controlled AI Operations Observatory. It follows the controlled loop:

`observe → analyze → recommend → approve → implement → validate → record`

The Control Plane owns the first four concerns and the evidence around the last
three. It never treats recommendation as approval, approval as implementation,
or implementation as validation.

### 2.2 Intended operators

| Role | Needs | Authority |
| --- | --- | --- |
| Primary operator | Situational awareness, evidence, policy, approvals, cost, safety | Sole human authority for consequential action |
| Reviewer | Traceability, comparisons, validator evidence, redacted inspection | Read-only unless an explicit operator approval delegates a future narrow action |
| Frontend implementer | Exact fields, states, layouts, component behavior | May implement only the separately authorized static slice |
| Future runtime integrator | Stable Control Plane contracts and seams | No authority from this specification to build or connect runtime |

The first product version assumes one primary technical operator. Multi-operator
roles, delegated approval, and organizational RBAC are future decisions.

### 2.3 Prohibited positioning

The Control Plane MUST NOT be presented as:

- a live autonomous super-agent;
- an already-running model router or provider proxy;
- a live orchestration backend or execution engine;
- a secrets-manager implementation or credential-entry surface;
- a trading terminal or any part of MellyTrade execution;
- a guaranteed cost, quality, latency, or savings optimizer;
- an autonomous self-improvement system;
- proof that a provider, model, agent, tool, or integration is connected.

### 2.4 Relationship to existing MellyCore surfaces

Source Arena remains MellyCore's leading visual metaphor and product hero.
The Control Plane overview's orbital routing core is an operational diagram
inside the cockpit, not a replacement product hero and not decorative-only.
Model Arena and the OpenRouter Observatory remain static, truthful precedents
for comparison, cost uncertainty, route explanation, and safety labels.

## 3. Control Plane vs Data Plane

### 3.1 Boundary

| Concern | Control Plane specified here | Future Data Plane / runtime |
| --- | --- | --- |
| Providers and models | Inventory metadata, capability and availability evidence | Provider authentication, requests, responses, rate limits |
| Routing | Policy authoring, precedence, simulation, explanation | Route selection during execution, failover, retries |
| Agents | Identity, contract, permissions, assignment preview | Agent process/session creation and execution |
| Skills and tools | Inventory, allowed-use metadata, gap recommendations | Skill/tool loading, invocation, side effects |
| Integrations | Catalog, access class, scope, risk, validation metadata | OAuth, connection, network communication, read/write operations |
| Context and memory | Source inspection, packet manifest, compression preview, approval | Retrieval, assembly, persistence, cache, refresh |
| Runs and traffic | Historical evidence and future event-contract inspection | Message transport, streaming, tool calls, retries |
| Queues and artifacts | Plans, manifests, dependencies, review states | Scheduling, dispatch, generation, storage |
| Approvals | Exact typed target, ID, version, digest, scope, expiry, decision, audit contract | Guard enforcement around a separately authorized action |
| Cost | Estimates, confirmed records when available, unknown states | Meter collection, account reconciliation, billing |
| Security | Metadata, least-privilege policy, redaction and audit requirements | Secret store, credential lifecycle, authentication enforcement |

### 3.2 Current-phase rule

Every current interaction terminates in inspection, comparison, simulation,
preview, configuration approval, rejection, or manifest export. No interaction
crosses into runtime execution. A future Data Plane may consume approved,
versioned manifests only after its own architecture, threat model, implementation
task, and validation gates are accepted.

### 3.3 Trust boundary

The Control Plane is never an authority merely because it displays a record.
Authority comes from an exact operator approval whose target type, ID, version,
digest, scope, allowed actions, constraints, expiry, and revocation state all
validate. A future runtime MUST refuse missing, expired, revoked, replayed, or
target-binding-mismatched approval.

## 4. Design Principles

1. **Operator control.** Consequential changes require explicit human intent.
2. **Read-only first.** Inspection and simulation are the default behaviors.
3. **Evidence before assertion.** File-, validator-, or source-backed facts outrank
   generated summaries.
4. **Unknown stays unknown.** Missing measurements never become zero or success.
5. **Policy is explicit.** Precedence, constraints, conflicts, and overrides are
   visible.
6. **Recommendation is not execution.** The UI never collapses the controlled loop.
7. **Least privilege.** Scope is project-, action-, and time-bounded.
8. **Static/live distinction.** Repository evidence, fixtures, simulations,
   unavailable runtime data, and future placeholders are visibly different.
9. **Clarity over spectacle.** Orbital depth supports comprehension and flattens
   whenever it harms legibility, accessibility, or performance.
10. **Progressive enhancement.** Every workflow remains usable without 3D,
    animation, hover, or a wide screen.
11. **Append-oriented audit.** Corrections supersede; they do not erase history.
12. **MellyCore only.** Trading, broker, order, and MellyTrade runtime behavior are
    outside the boundary.

## 5. Scope and Non-Goals

### 5.1 In scope

- the ten Control Plane modules in Section 9;
- the intelligence modules in Section 10;
- navigation, entity, state, workflow, responsive, accessibility, and
  performance contracts;
- static fixture and future-runtime presentation contracts;
- approvals, provenance, redaction, and security metadata;
- frontend component boundaries and future integration seams.

### 5.2 Explicitly out of scope

- edits to `site/` or any frontend implementation;
- backend, API, provider, model, agent, tool, or integration code;
- credentials, secret values, `.env`, OAuth, account IDs, or key-entry UX;
- databases, persistence, migrations, queues, schedulers, streaming, retries;
- automatic routing, fallback, context refresh, skill creation, or remediation;
- execution controls named Run, Start, Execute, Launch, Connect Live, Buy, or Sell;
- workflow YAML, dependencies, Vercel configuration, deployment, release;
- WebGL, Canvas, shaders, Three.js, or the 3D Scene Foundation;
- trading, brokerage, orders, positions, or MellyTrade runtime linkage.

## 6. Information Architecture

### 6.1 Desktop navigation decision

Desktop uses five primary destinations. Secondary navigation appears within the
selected destination.

| Primary destination | Secondary destinations |
| --- | --- |
| **Overview** | Operator Console, status, approvals and alerts |
| **Estate** | Providers & Models, Agents, Skills & Tools, Integrations |
| **Work** | Routing, Context & Memory, Traffic, Runs & Costs, Queues & Artifacts |
| **Governance** | Approvals, Recommendations, Security |
| **System** | Project settings metadata, safety policies, audit notices |

This grouping avoids twelve equal-weight top-level destinations. The primary
sidebar remains stable; the secondary rail may collapse to a dropdown below
1366px.

### 6.2 Global frame

- **Project switcher:** always shows current project and scope; switching clears
  local selection, filters, simulations, and unexported manifests.
- **Global search:** searches metadata and identifiers only. Secret/private
  contents are never indexed into frontend search.
- **Command palette:** safe navigation and read-only commands only; it does not
  provide hidden execution verbs.
- **Breadcrumbs:** `Project / Primary / Secondary / Entity`, with stable IDs in
  the inspector rather than the breadcrumb label.
- **Time range:** applies only to evidence-bearing temporal views and always
  shows timezone and whether data is complete.
- **Filters:** persist per module in session-local UI state; a visible "Clear
  filters" restores the truthful unfiltered result.
- **Inspector:** opens on the right on desktop, as a detail sheet on compact
  layouts, and never obscures the provenance/source label.

### 6.3 Mobile navigation

Bottom navigation contains **Status**, **Approvals**, **Work**, **Alerts**, and
**More**. `More` opens Estate, Governance, System, search, and project switching.
Mobile is an operator companion focused on review; dense traffic graphs and full
comparison matrices are not default views.

## 7. Core Entity Model

### 7.1 Common entity contract

Every entity has a stable, opaque ID; `schema_version`; `project_id`; owner or
steward; `created_at`; `updated_at`; provenance; evidence references; a
truthful-state label; and a source-mode label. IDs MUST NOT encode mutable state.
Unknown timestamps are `null`, never fabricated. Static fixtures use reserved
`fixture:` IDs and cannot collide with future runtime IDs.
Applicable status fields use only the six canonical field names in Section 8;
domain fields such as outcome, verdict, trust, basis, and configuration state
remain typed entity data and are not additional status dimensions.

Provenance minimally includes `source`, `source_type`, `captured_at`,
`validated_at`, `freshness`, `confidence`, `verification_state`,
`immutability`, `estimation_basis`, `supersedes`, and `conflict_state`.

### 7.2 Entity catalogue

| Entity | Purpose and stable ID | Minimum entity-specific fields | Applicable status fields | Relationships and representation |
| --- | --- | --- | --- | --- |
| `Project` | Scope boundary; `project_id` | name, description, safety_policy_ids, budget_policy, allowed_asset_ids | `lifecycle_status`, `evidence_state` | Owns all scoped entities; fixture is one explicit demo project; future runtime enforces isolation |
| `Provider` | Provider metadata; `provider_id` | name, access_class, authentication_mode, purpose, capabilities, modalities, status, last_validation | `availability_status`, `evidence_state`, `freshness_state` | Has Models; fixture never implies connection; runtime may expose health evidence |
| `Model` | Model/alias metadata; `model_id` | provider_id, display_name, exact_or_alias, capabilities, context_window, tool_support, cost_class, status, snapshot_date | `availability_status`, `evidence_state`, `freshness_state`, `selection_state` | Belongs to Provider; candidate in RoutingPolicy; fixture values are reviewed snapshots |
| `Agent` | Inspectable agent contract; `agent_id` | name, role, owner, version, autonomy_class, model_policy_id, skills, tools, context_access, safety_contract, last_validation | `lifecycle_status`, `availability_status`, `evidence_state`, `freshness_state` | Uses policies/assets; fixture is inspection-only; runtime may emit runs |
| `Skill` | Governed capability; `skill_id` | name, version, purpose, owner, allowed_projects, risk_class, validation_state | `lifecycle_status`, `availability_status`, `evidence_state`, `freshness_state` | Assigned to Agents; recommendations never create it automatically |
| `Tool` | Governed callable capability metadata; `tool_id` | name, category, allowed_actions, read_write_class, risk_class, approval_requirement, status | `availability_status`, `evidence_state`, `freshness_state` | Assigned to Agents and Integrations; no invocation in static phase |
| `Integration` | External-system metadata; `integration_id` | name, category, access_mode, allowed_actions, read_write_class, risk_class, project_scope, status, last_validation | `availability_status`, `evidence_state`, `freshness_state`, `approval_state` | May expose Tools; fixture includes no credentials or connection flow |
| `RoutingPolicy` | Versioned selection intent; `routing_policy_id` | name, version, mode, criteria, constraints, fallback_chain, precedence, approval_requirement, status | `lifecycle_status`, `approval_state`, `selection_state`, `evidence_state` | Evaluates Models for Task manifests; simulation only now |
| `ContextSource` | Provenance-bearing input metadata; `context_source_id` | source_identity, source_type, verification_state, trust_level, sensitivity, freshness, allowed_use, conflict_state | `availability_status`, `evidence_state`, `freshness_state` | Feeds ContextPackets and MemoryRecords; protected contents may remain undisclosed |
| `ContextPacket` | Approved context manifest; `context_packet_id` | version, source_refs, compression_strategy, token_estimate, redactions, confidence, scope, approval_ref, digest, status | `lifecycle_status`, `freshness_state`, `approval_state`, `evidence_state` | Used by planned Task/Run; current representation is a manifest preview |
| `MemoryRecord` | Memory metadata and lineage; `memory_record_id` | layer, source_ref, summary_ref, freshness, retention, trust, relevance, authorization, supersession | `lifecycle_status`, `freshness_state`, `evidence_state` | May feed ContextPackets; immutable history is retained |
| `Task` | Planned unit of work; `task_id` | title, purpose, owner_agent_id, dependencies, policy_id, context_packet_id, expected_artifacts, stop_conditions, status | `lifecycle_status`, `approval_state`, `evidence_state` | Parent of Runs/QueueItems; current phase prepares plans only |
| `Run` | Normalized historical execution evidence; `run_id` | task_id, agent_id, model_id, provider_id, timestamps, duration, token fields, costs, outcome, commit_sha, approval_ref, policy_id, context_packet_id | `lifecycle_status`, `evidence_state`, `freshness_state` | Has RunEvents, artifacts, validators, costs; outcome remains entity data; fixtures never claim execution |
| `RunEvent` | Ordered event evidence; `run_event_id` | run_id, sequence, event_type, occurred_at, actor, correlation_id, redaction_state, payload_summary_ref, outcome | `lifecycle_status`, `evidence_state`, `freshness_state` | Builds traffic timeline/graph; outcome remains entity data; static events are explicitly illustrative |
| `QueueItem` | Planned batch/artifact work; `queue_item_id` | task_id, priority, dependencies, approval_state, estimated_cost, assigned_agents, policy_id, context_packet_id, validators, retry_policy, stop_conditions, status | `lifecycle_status`, `approval_state`, `evidence_state` | May reference expected Artifacts; no dispatch in current phase |
| `Artifact` | Output or planned-output metadata; `artifact_id` | run_id, path_or_uri, artifact_class, digest, change_kind, created_at, status, sensitivity | `lifecycle_status`, `evidence_state`, `freshness_state` | Traceable to Run, ContextPacket, Validators; content display follows sensitivity |
| `ValidatorResult` | One actual or planned check; `validator_result_id` | target_ref, validator_identity, verdict, ran_at, evidence_ref, notes | `evidence_state`, `freshness_state` | Belongs to Run/Artifact; verdict remains entity data; `NOT_RUN` never renders as pass |
| `Recommendation` | Proposed change with evidence; `recommendation_id` | source, reason, evidence_refs, expected_impact, risk, cost, decision, implementation_task, validator_outcome, final_outcome | `lifecycle_status`, `approval_state`, `evidence_state`, `freshness_state` | May create Approval; controlled-loop decision/outcomes remain entity data; never self-implements |
| `Approval` | Exact operator authorization; `approval_id` | target_type, target_id, target_version, target_digest, approval_subject, requester_id, operator_id, scope, decision, constraints, authorized_actions, prohibited_actions, requested_at, issued_at, expires_at, revoked_at, evidence_refs, provenance_refs, decision_note, audit_event_id, recommendation_id (optional source reference) | `approval_state`, `evidence_state`, `freshness_state` | Gates one exact typed and versioned future action set; Recommendation is not a universal target wrapper; no blanket, inferred, or cross-entity authority |
| `Operator` | Human authority metadata; `operator_id` | display_name, role, project_scopes, approval_class, status | `lifecycle_status`, `evidence_state` | Owns approvals; fixture identity is a generic placeholder, no account ID |
| `SafetyPolicy` | Immutable/versioned safety rules; `safety_policy_id` | name, version, rules, precedence, owner, effective_at, supersedes, status | `lifecycle_status`, `approval_state`, `evidence_state`, `freshness_state` | Applies to Project, Policy, Agent, Task, Approval; system cannot modify it |
| `CostRecord` | Measured or estimated cost; `cost_record_id` | run_id, amount, currency, basis, calculation_method, pricing_source, pricing_timestamp, confirmed_at | `evidence_state`, `freshness_state` | Aggregates into budgets; basis remains entity data; unknown is null; estimate never equals confirmed |

### 7.3 Relationship rules

- Cross-project references are prohibited unless a future safety policy and exact
  approval explicitly permit a metadata-only reference.
- Deleting an entity from a view never deletes evidence; historical entities are
  `historical` or `superseded`.
- A Run can reference at most one effective RoutingPolicy and ContextPacket
  version, but may record evaluated alternatives.
- `Approval.target_type + Approval.target_id + Approval.target_version +
  Approval.target_digest` form one immutable target binding. `recommendation_id`
  MAY identify the proposal that led to an approval, but it is optional and
  MUST NOT substitute for the typed target binding.
- Approval, ValidatorResult, and CostRecord remain independent evidence objects.
- The model is conceptual and frontend-facing; it is not a production database
  schema.

## 8. Status Taxonomy

### 8.1 Canonical per-dimension enum contract

Status is represented by six orthogonal fields. The machine identity of an enum
member is the dimension-qualified pair, for example
`{dimension: "availability_status", value: "degraded"}`. An unqualified raw
value is not a valid status contract. This permits honest human labels such as
`Unknown`, `Expired`, or `Rejected` in more than one domain without making their
machine meaning ambiguous.

| Owning dimension / field | Purpose | Legal values | Applicability and display | Unknown behavior |
| --- | --- | --- | --- | --- |
| Lifecycle / `lifecycle_status` | Progression and retained history only | `draft`, `planned`, `queued`, `ready`, `active`, `blocked`, `completed`, `failed`, `cancelled`, `superseded`, `historical` | Versioned plans, policies, packets, tasks, runs, queue items, artifacts, and recommendations; display as `Lifecycle: <label>` | No lifecycle `unknown` member; omit the field when inapplicable and expose missing lifecycle evidence separately |
| Availability / `availability_status` | Operational reachability or usable capacity | `available`, `degraded`, `unavailable`, `disconnected`, `unknown` | Providers, models, agents, tools, integrations, and sources; display as `Availability: <label>` | `unknown` means availability cannot be established, never available or disconnected |
| Evidence / `evidence_state` | Truth/source mode and evidence completeness | `canonical`, `static_demo`, `simulated`, `future_live`, `partial`, `unknown` | Every rendered evidence-bearing record or surface; display persistently as `Evidence: <label>` | `unknown` means source mode or evidence coverage is not established |
| Freshness / `freshness_state` | Age against a declared review/expiry boundary | `fresh`, `aging`, `stale`, `expired`, `unknown` | Time-sensitive sources, packets, memory, runs, cost, and validation evidence; display timestamp/boundary with `Freshness: <label>` | `unknown` means no defensible freshness conclusion; never coerce to fresh |
| Approval / `approval_state` | Operator decision state for one exact target binding | `not_required`, `awaiting_approval`, `approved`, `rejected`, `expired`, `revoked` | Approval records and approval-gated targets; display as `Approval: <label>` | No approval `unknown` member; missing or unresolved approval evidence authorizes nothing |
| Selection / `selection_state` | UI or routing-candidate selection result | `eligible`, `preferred`, `selected`, `rejected`, `fallback`, `excluded` | Frontend-local selection and deterministic simulation candidates; display as `Selection: <label>` | No selection `unknown` member; absence means no selection decision is represented |

`static_demo` is the sole evidence enum for fixture-backed demonstration data.
It corresponds to the human-facing `STATIC FIXTURE` record badge and the
`STATIC DEMONSTRATION — NOT LIVE` bundle notice; `fixture` is not a second,
equivalent enum value. `configured` / `not_configured` remain security or access
metadata, not availability states.

### 8.2 Orthogonality, ownership, and rendering rules

- One entity MAY hold one value from each applicable dimension at the same time.
  For example, a ContextPacket may be lifecycle `ready`, freshness `aging`,
  approval `approved`, and evidence `static_demo`.
- Every legal enum member belongs to exactly the field in Section 8.1. The full
  machine value is always the field/value pair, so `freshness_state:expired`
  cannot be interpreted as `approval_state:expired`, and
  `approval_state:rejected` cannot be interpreted as
  `selection_state:rejected`.
- `active` is lifecycle-only and means an effective policy/configuration. It
  MUST NOT describe connectivity, a running agent, selected UI state, or general
  availability.
- A `StatusChip`, badge, filter, sort, query parameter, fixture, or integration
  seam MUST carry the dimension field with the value. Visible and screen-reader
  labels MUST include or programmatically expose the dimension.
- Filters MUST NOT collapse dimensions. Module summaries MAY show multiple chips
  and MUST NOT synthesize a universal "healthy", "active", or green state.
- A module `Statuses` row is a cross-dimensional state contract only when it
  groups every value under its owning dimension. Flat untyped status lists are
  prohibited.

## 9. Module Specifications

All modules inherit Sections 7, 8, 15, 16, 18, 19, and 20. Every module must
render loading, empty, unknown, degraded, error, static-fixture, simulated, and
future-live-placeholder states explicitly.

### 9.1 Provider Registry and Model Gateway

| Contract item | Requirement |
| --- | --- |
| Purpose/users | Operator and reviewer inspect provider/model inventory, access class, fit, status, and evidence |
| Key entities/fields | Provider and Model; plan/access class, authentication mode metadata, purpose, cost class, capabilities, modalities, context window, tool support, allowed projects, last validation, availability, provenance, notes |
| Statuses | Availability: `available`, `degraded`, `unavailable`, `unknown`. Evidence: `static_demo`, `future_live`. `configured` is access metadata and never implies availability |
| Primary views | Provider table, model constellation/list, model detail inspector, capability matrix, evidence drawer |
| Interactions | Inspect, filter, compare, trace validation, copy IDs; no connect or credential action |
| Empty/unknown/degraded | Empty explains no reviewed inventory; unknown fields show `— / Unknown`; degradation lists missing evidence and affected routes |
| Static/future behavior | Static entries carry snapshot/source labels; future health may update from evidence but never exposes secrets |
| Responsive/accessibility | Desktop table + inspector; mobile provider cards and model list; semantic table alternative, 44px targets, text status |
| Safety/provenance | Authentication mode is metadata only; operator notes forbid secrets; source, capture/validation time, freshness, confidence always visible |

### 9.2 Routing Policy Center

| Contract item | Requirement |
| --- | --- |
| Purpose/users | Operator defines and reviewer inspects deterministic/adaptive routing intent without executing a route |
| Key entities/fields | RoutingPolicy; criteria, quality floor, cost ceiling, latency preference, privacy/capability constraints, project allowlist, approval rules, fallback chain, precedence, override policy, version, digest |
| Statuses | Lifecycle: `draft`, `ready`, `active` (effective only), `blocked`, `superseded`. Approval: `awaiting_approval`, `approved`, `rejected`, `expired`, `revoked`. Selection: `eligible`, `preferred`, `selected`, `rejected`, `fallback`, `excluded`. Evidence: `static_demo`, `simulated`, `future_live` |
| Primary views | Policy list, rule builder, precedence stack, conflict panel, simulation form, route explanation |
| Interactions | Prepare policy, reorder explicit precedence, detect conflicts, Simulate, Compare, Approve configuration, Export manifest |
| Explanation output | Selected candidate, rejected alternatives with reasons, applied rules, estimated cost/basis, confidence/basis, fallback route/tradeoffs, override status |
| Empty/unknown/degraded | No policy yields "No effective policy"; missing costs produce insufficient-data output; unresolved conflict blocks `ready` |
| Static/future behavior | Current simulations are deterministic local examples; adaptive policies are specification-only and may not learn/change themselves |
| Responsive/accessibility | Rule rows become ordered cards on mobile; route graph has an equivalent ordered text explanation |
| Safety/provenance | No live routing; safety and privacy rules outrank cost/latency; override requires exact approval and audit |

Routing precedence is: safety policy → project restriction → approval requirement
→ privacy/data handling → required capability/quality → operator override →
cost/latency preference → deterministic tie-breaker. Adaptive recommendations may
propose a policy revision but cannot mutate precedence or activate themselves.

### 9.3 Context Compression and Shared Context

| Contract item | Requirement |
| --- | --- |
| Purpose/users | Operator assembles a minimal, provenance-aware context manifest and inspects memory health |
| Key entities/fields | ContextSource, ContextPacket, MemoryRecord; layer, source, strategy, summary ref, confidence, freshness, retention, project scope, agent visibility, token estimate, redaction, approval, digest |
| Memory layers | Immutable evidence, working memory, task memory, project memory, long-term knowledge |
| Statuses | Lifecycle: `draft`, `ready`, `blocked`, `superseded`. Freshness: `fresh`, `aging`, `stale`, `expired`, `unknown`. Approval: `awaiting_approval`, `approved`, `rejected`, `expired`, `revoked`. Evidence: `canonical`, `static_demo`, `simulated`, `future_live`, `partial`, `unknown` |
| Primary views | Source table, packet builder, assembly preview, token budget, conflict view, Memory Freshness panel |
| Interactions | Filter sources, preview inclusion/exclusion, choose reviewed compression strategy, mark redaction requirement, Prepare manifest, Approve configuration, Export manifest |
| Empty/unknown/degraded | No sources explains admission requirement; `freshness_state:stale` / `freshness_state:expired` remain visible; conflicts show both sources and block silent resolution |
| Static/future behavior | Current packet is an unexecuted manifest; future runtime may assemble only the exact typed, versioned, digest-bound approved packet |
| Responsive/accessibility | Mobile shows packet summary then source cards; no dense graph; conflicts and redactions use text/icons, not color alone |
| Safety/provenance | Secret/high-risk contents remain undisclosed; redaction is explicit; trust, freshness, relevance, and authorization remain separate |

Compression strategies are named, versioned policies such as `extractive`,
`hierarchical_summary`, `deduplicate_then_summarize`, or `no_compression`.
Generated summaries never replace immutable source evidence and carry their own
provenance/confidence. A stale context packet cannot silently become `ready`.

### 9.4 Agent Runtime Directory

| Contract item | Requirement |
| --- | --- |
| Purpose/users | Inspect agent identity, ownership, capabilities, constraints, and safety contract |
| Key entities/fields | Agent; ID/name, role, owner, model/provider policy, skills, tools, context access, allowed projects, autonomy class, approvals, status, version, safety contract, last validation |
| Statuses | Lifecycle: `draft`, `ready`, `superseded`. Availability: `available`, `degraded`, `unavailable`, `unknown`. Evidence: `canonical`, `static_demo`, `future_live`, `partial`, `unknown` |
| Primary views | Directory, comparison, agent detail inspector, permission matrix, evidence drawer |
| Interactions | Inspect, Compare, Trace, View evidence, Copy identifier; no Launch agent |
| Empty/unknown/degraded | Empty says no agents registered; degradation enumerates invalid/missing policy, skill, tool, or validation refs |
| Static/future behavior | Current directory is inspection-only; future runtime status must be event-backed and time-stamped |
| Responsive/accessibility | Mobile role cards and tabbed detail sheet; permission matrix has a list alternative |
| Safety/provenance | Autonomy class never grants authority; effective permissions are intersection of agent, project, policy, approval, and tool/integration limits |

### 9.5 Agent Traffic Inspector

| Contract item | Requirement |
| --- | --- |
| Purpose/users | Reviewer traces future/historical agent messages, hops, context, tool requests, approvals, blocks, retries, errors, tokens, costs, artifacts |
| Key entities/fields | Run, RunEvent, Approval, ContextPacket, Artifact; correlation ID, run ID, task ID, sequence, timestamps, actors, redaction, outcome |
| Statuses | Lifecycle: `planned`, `blocked`, `completed`, `failed`, `cancelled`, `historical`. Availability: `available`, `degraded`, `unavailable`, `unknown`. Evidence: `canonical`, `static_demo`, `future_live`, `partial`, `unknown`. Freshness: `fresh`, `aging`, `stale`, `expired`, `unknown` |
| Primary views | Timeline, traffic graph, event inspector, filters, trace search |
| Interactions | Filter, Trace, Explain route, open linked evidence/artifact; no replay/retry action |
| Empty/unknown/degraded | No events is not "quiet"; it means unavailable/not captured; partial sequence shows gaps and last confirmed event |
| Static/future behavior | Static graph carries a persistent `STATIC DEMO` banner; future traffic is accepted only from a defined event contract |
| Responsive/accessibility | Mobile defaults to ordered timeline; graph is opt-in and has a complete list alternative |
| Safety/provenance | Message bodies may be redacted or content-free; identifiers and metadata remain traceable without exposing secrets/private content |

### 9.6 Integration Gateway

| Contract item | Requirement |
| --- | --- |
| Purpose/users | Inspect a metadata-only catalog for GitHub, Drive, Gmail, Calendar, Slack, Notion, Figma, Vercel, Supabase, AI providers, and local tools |
| Key entities/fields | Integration; ID, name, category, access mode, required approval, allowed actions, read/write class, risk class, project scope, status, last validation, data-handling notes |
| Statuses | Availability: `available`, `degraded`, `unavailable`, `disconnected`, `unknown`. Evidence: `static_demo`, `future_live`, `partial`, `unknown`. `configured` is access metadata, not a status |
| Primary views | Catalog, risk/access matrix, integration inspector, validation evidence |
| Interactions | Inspect, Compare, Filter, View evidence; no Connect, OAuth, authorize, or credential-entry flow |
| Empty/unknown/degraded | Empty says no reviewed metadata; unknown does not imply disconnected; degraded states show affected actions |
| Static/future behavior | Current catalog entries are placeholders/fixtures; future connection health is metadata only in this surface |
| Responsive/accessibility | Mobile category cards and action-scope list; read/write/risk expressed in text |
| Safety/provenance | Never show secret values, tokens, account IDs, private scopes, or raw grants; write-capable future actions require separate approval |

### 9.7 Unified Run Ledger and Cost Observatory

| Contract item | Requirement |
| --- | --- |
| Purpose/users | Operator audits run outcomes, evidence, validators, model/provider use, and cost |
| Key entities/fields | Run, CostRecord, ValidatorResult, Artifact; run/task/agent/model/provider IDs, timestamps/duration, input/output/cache tokens, estimated/confirmed cost, currency, files, validators, artifacts, outcome, commit SHA, approval, errors, retries, packet/policy IDs |
| Statuses | Lifecycle: `planned`, `blocked`, `completed`, `failed`, `cancelled`, `historical`. Evidence: `canonical`, `static_demo`, `future_live`, `partial`, `unknown`. Freshness: `fresh`, `aging`, `stale`, `expired`, `unknown` |
| Primary views | Timeline, ledger table, cost breakdown, model/project comparison, anomaly and budget panels, missing-data view |
| Interactions | Inspect, Compare, filter time/project/model/outcome, Trace artifact, Export manifest/ledger view |
| Empty/unknown/degraded | Unmeasured tokens/cost show `—`; estimate and confirmed values never merge; incomplete capture shows partial coverage |
| Static/future behavior | Static runs are illustrative; future records are append-oriented, measured-or-null, and source-stamped |
| Responsive/accessibility | Mobile run cards prioritize outcome, time, approval, cost basis; tables retain semantic headers and list alternative |
| Safety/provenance | `NOT_RUN` validator is not pass; estimated cost cannot satisfy a budget; files show metadata/digest, not secret content |

Cost comparisons require the same currency, time window, and basis or explicitly
state why values are not comparable. Anomaly detection is a recommendation
signal, not an automatic budget or routing action.

### 9.8 Batch Run and Artifact Queues

| Contract item | Requirement |
| --- | --- |
| Purpose/users | Plan and review grouped work, dependencies, artifacts, validators, cost, and stop conditions |
| Key entities/fields | QueueItem, Task, Artifact; priority, dependencies, approval, estimated cost, agents, policy, packet, expected artifacts, validators, stop conditions, retry policy, status |
| Statuses | Lifecycle: `draft`, `planned`, `queued`, `ready`, `blocked`, `completed`, `failed`, `cancelled`. Approval: `awaiting_approval`, `approved`, `rejected`, `expired`, `revoked`. Evidence: `static_demo`, `future_live` |
| Primary views | Queue board, dependency list, batch review, manifest preview, artifact browser |
| Interactions | Prepare plan, Review batch, Approve configuration, Export manifest, Inspect dependencies |
| Empty/unknown/degraded | Empty says no planned items; unresolved dependency or unknown cost is explicit; blocked reason and owner required |
| Static/future behavior | Current queue is planning/inspection only; future dispatch is outside this surface/task |
| Responsive/accessibility | Mobile uses ordered cards grouped by approval/block state; dependency graph has a list equivalent |
| Safety/provenance | Labels `Run`, `Start`, `Execute`, and `Launch` are forbidden; retry policy is metadata, never an active control |

### 9.9 Security and Secrets Boundary

| Contract item | Requirement |
| --- | --- |
| Purpose/users | Operator inspects least-privilege, secret-health, grant, redaction, audit, revocation, and rotation metadata |
| Key entities/fields | SafetyPolicy, Integration, Provider, Approval; configured/not configured, scope, owner, validation status, rotation due, health, access class, risk, audit refs |
| Statuses | Lifecycle: `superseded`. Availability: `available`, `degraded`, `unavailable`, `unknown`. Approval: `awaiting_approval`, `approved`, `rejected`, `expired`, `revoked`. Evidence: `static_demo`, `future_live`, `partial`, `unknown`. `configured` / `not_configured` are metadata, not statuses |
| Primary views | Boundary map, permission matrix, metadata inventory, audit timeline, redaction policy inspector |
| Interactions | Inspect, Review, Trace, View evidence; no reveal/copy secret, key entry, OAuth, rotate, or revoke control in current phase |
| Empty/unknown/degraded | Unknown health stays unknown; absent metadata does not mean no secret exists; overdue rotation is warning metadata |
| Static/future behavior | Static records are examples only; future store and credential lifecycle remain outside Control Plane implementation |
| Responsive/accessibility | Mobile shows safety alerts and scoped metadata cards; never hides risk behind hover |
| Safety/provenance | Secret values never enter DOM, logs, exports, search, analytics, fixtures, or screenshots; refusal records are content-free |

### 9.10 Operator Console

| Contract item | Requirement |
| --- | --- |
| Purpose/users | Primary operator obtains situational awareness and reaches evidence, policy, approvals, and safe navigation |
| Key entities/fields | Project, SafetyPolicy, RoutingPolicy, ContextPacket, Approval, QueueItem, Run, CostRecord, Provider, Artifact, Recommendation |
| Statuses | Explicitly cross-dimensional summary. Lifecycle: `planned`, `ready`, `active`, `blocked`, `completed`, `failed`, `historical`. Availability: `available`, `degraded`, `unavailable`, `disconnected`, `unknown`. Evidence: `canonical`, `static_demo`, `simulated`, `future_live`, `partial`, `unknown`. Freshness: `fresh`, `aging`, `stale`, `expired`, `unknown`. Approval: `not_required`, `awaiting_approval`, `approved`, `rejected`, `expired`, `revoked`. Selection: `eligible`, `preferred`, `selected`, `rejected`, `fallback`, `excluded`. Each summary chip retains its dimension; no overall "healthy" state |
| Primary views | System status, current project, effective policy, selected packet, approvals, blocked work, recent runs, costs, provider health, alerts, artifacts, notices |
| Interactions | Inspect, Review, Compare, Preview, Trace, open destination; no execution shortcut |
| Empty/unknown/degraded | Each card has independent coverage/freshness; unavailable cards remain visible with cause and evidence link |
| Static/future behavior | Current overview is a labeled static demonstration; future data freshness is per-card, not a global pulse |
| Responsive/accessibility | Desktop rails + center workspace + timeline; mobile prioritizes status, approvals, alerts, blocks, then recent evidence |
| Safety/provenance | Priority order is awareness → evidence → review → policy → approvals → navigation; alerts cannot be dismissed without an audit contract in future |

## 10. Intelligence Modules

### 10.1 AI Estate Inventory

Unifies Provider, Model, Agent, Skill, Tool, Integration, plan/access class, and
capability records. It is a registry view, not an automatic discovery claim.
Duplicate identities, unvalidated capabilities, and conflicting sources remain
visible.

### 10.2 Skill Gap Detector

A candidate requires at least three evidence-linked repetitions of a process,
manual transformation, validation sequence, context assembly, or operator
intervention.

Minimum output: candidate skill, evidence refs, recurrence count/window,
expected benefit, maintenance cost, risk, confidence/basis, approval requirement,
owner, expiry, and status. It cannot create, edit, install, activate, or grant a
skill. Operator approval may authorize only a future authoring task.

### 10.3 Memory Freshness Monitor

Displays freshness, expiry, contradiction, stale reference, supersession,
immutable-history, and refresh-recommendation metadata. It separates existence,
trust, freshness, relevance, and task authorization. It never auto-refreshes,
deletes, or silently repairs memory.

### 10.4 Recommendation Ledger

Minimum fields: recommendation ID, source, reason, evidence, expected impact,
risk, cost/basis, decision, implementation task, validator outcome, final
outcome, lifecycle events, supersession, and timestamps. All transitions are
append-oriented and evidence-linked.

### 10.5 Controlled Self-Improvement Loop

The only permitted lifecycle is:

`observe → analyze → recommend → approve → implement → validate → record`

Human approval is mandatory before implementation. The system cannot
autonomously change safety rules, permissions, provider access, approval
requirements, secret policy, or execution permissions. Current Control Plane
work stops at recommendation/configuration approval and records that later
implementation remains separately authorized.

## 11. Operator Workflows

Each workflow is non-executing and ends in inspection, approval of a
configuration/manifest, or export.

1. **Inspect provider/model availability:** open Estate → filter project and
   capability → distinguish configuration metadata from
   `availability_status` and `evidence_state` → inspect last validation and
   provenance → trace degradation → copy IDs or compare.
2. **Simulate routing:** open Work/ Routing → select task profile and policy
   version → enter constraints and token assumptions → Simulate → inspect selected
   and rejected candidates, rules, cost basis, confidence, fallback, overrides →
   export explanation. No route is called.
3. **Assemble/approve context manifest:** open Context → select sources → inspect
   sensitivity/freshness/conflicts → choose reviewed compression strategy →
   preview token/redaction effects → resolve or explicitly block conflicts →
   review target type/ID/version/digest/scope → Approve configuration or export
   draft manifest.
4. **Inspect an agent:** open Estate/Agents → select agent → review role, owner,
   policies, skills/tools, context/project access, autonomy class, approvals,
   safety contract, validation → trace evidence. No launch control exists.
5. **Review a proposed batch:** open Queues → select batch → inspect dependencies,
   cost basis, assignments, policy, packet, artifacts, validators, stop/retry
   metadata → review blocks → Approve configuration or reject/return to draft.
6. **Investigate failed historical run:** open Runs → filter `failed` → inspect
   timeline/event gaps/errors/retries → trace policy, packet, approval, model,
   artifacts, validators → compare related runs → export evidence view. No retry.
7. **Review skill recommendation:** open Governance/Recommendations → verify
   recurrence threshold and evidence → inspect benefit/risk/maintenance →
   approve only a future authoring task, reject with reason, or defer; record
   decision.
8. **Inspect security metadata:** open Governance/Security → choose project →
   review access/risk/configuration/rotation/validation metadata → trace policy
   and content-free audit refs. No value reveal or connection flow.
9. **Compare models:** open Providers & Models → set capability/quality floor,
   cost basis, and time/snapshot → compare context/tool/modalities/status/cost →
   mark incomparable unknowns → open route simulation if needed.
10. **Trace an artifact:** open Artifact Browser → select artifact → verify digest,
    sensitivity, run, task, agent, model/provider, policy, packet, approvals,
    validators, cost → open immutable evidence refs.

## 12. Overview Screen

### 12.1 Composition

- **Center:** functional orbital routing core.
- **Around center:** provider/model constellation and agent rings.
- **Inbound path:** selected context packet and source stream.
- **Outbound planning paths:** candidate, blocked, and fallback routes.
- **Left rail:** system/project status, evidence coverage, provider health.
- **Right rail:** approvals, safety alerts, blocked work, recommendations.
- **Bottom timeline/drawer:** recent runs, costs, artifacts, and missing-data
  coverage.

### 12.2 Orbital core semantics

The core MUST explain, in text and accessible structured data:

- effective routing policy/version;
- available, degraded, unknown, and static-demo providers;
- candidate/rejected models and rule reasons;
- selected context-packet ID/version/digest;
- proposed agent assignment;
- blocked and fallback routes;
- estimated cost and latency envelope with basis;
- simulation time and source mode.

Visual position, glow, line motion, or node size never solely communicates state.
No path animation implies traffic. When 3D/effects are unavailable, the same
information renders as a two-column decision map plus ordered route explanation.
There are no live execution controls.

## 13. Desktop Experience

### 13.1 Layout system

Use a 12-column workspace grid with an 8px spacing base. Primary sidebar:
72px collapsed / 232px expanded. Secondary rail: 200–240px when present.
Inspector: 360–480px resizable. Bottom drawer: 240–420px resizable. The central
workspace has `min-width: 0`; dense tables scroll inside their panel, never the
page.

| Viewport | Required behavior |
| --- | --- |
| 1366×768 | Collapsed primary sidebar by default; compact secondary selector; one rail at a time; bottom drawer closed |
| 1440×900 | Expanded sidebar optional; center + one 360px inspector; approvals rail may collapse |
| 1920×1080 | Expanded sidebar; center workspace; both contextual rail and inspector available; bottom timeline preview |
| 2560×1440 | Maximum content measure prevents stretched copy; wider graph/table detail and 440px inspector |
| Ultrawide | Three operational zones allowed; empty width becomes gutters, not extra card columns; no critical content at extreme edges |

Minimum supported desktop width is 1180px. Below that, compact/tablet behavior
applies. Panels can be resized by keyboard and pointer, expose current size, and
provide Reset layout. Multi-monitor mode may detach only read-only inspectors or
timelines in a future task; it cannot move approvals into an unaudited window.

### 13.2 Density and focus

Tables use sticky headers, column visibility, deterministic sorting, and row
selection. Default density must remain readable at 1366×768. The inspector
preserves selection when filters change only if the entity remains in scope;
otherwise it closes with an explanatory notice.

## 14. Mobile Experience

Mobile prioritizes: status, approvals, alerts, effective policy, queue/blocks,
recent runs, provider degradation, context freshness, and artifact review.

- Use single-column cards and full-height detail sheets.
- Convert tables to labeled key/value cards with sort/filter sheets.
- Default traffic to timeline, not graph.
- Default routing to explanation and candidates, not constellation.
- Show the complete approval target type/ID/version/digest, scope, and expiry
  before decision controls in a future approval-capable task.
- Use 44×44px minimum touch targets and 8px separation.
- Gestures are limited to standard scroll, sheet dismissal, and optional
  non-exclusive swipe between peer tabs.
- Never require long-press, hover, pinch, or drag to obtain evidence.
- Disable parallax, blur-heavy backgrounds, continuous orbit motion, and dense
  star fields on mobile.
- Support 320px safety width without page-level horizontal overflow; design
  target is 390×844.

Bottom navigation remains reachable above system insets. Alerts and pending
approvals display counts only when the source coverage is known; unknown is an
explicit `?`, not zero.

## 15. Interaction States

| Interaction or typed state | Visual/content requirement |
| --- | --- |
| default | Neutral surface plus source mode and last-known freshness |
| hover | Optional emphasis only; no exclusive content |
| focus | High-contrast visible outline, not clipped by glow/transform |
| `selection_state:selected` | Text/icon/aria state; distinct from lifecycle `active` policy |
| loading | Skeleton or progress label with retained context; never fake data |
| empty | Explains whether no records, no matches, or no source exists |
| `freshness_state:stale` | Visible timestamp/review boundary and affected dependents |
| dimension-qualified `unknown` | `Unknown` text, owning dimension, and reason; never gray blank/zero |
| `availability_status:degraded` | Available subset, missing subset, impact, and evidence |
| `lifecycle_status:blocked` | Blocking reason, owner, dependency, and safe next review action |
| `approval_state:awaiting_approval` | Exact target type, ID, version, digest, scope, expiry, and risk summary; rendered as `Approval: awaiting approval` |
| error | Error class/signature, last good evidence if permitted, no success badge |
| `availability_status:disconnected` | Future source connection unavailable; static UI remains usable |
| `evidence_state:static_demo` | Persistent `STATIC FIXTURE` badge and example notice |
| `evidence_state:simulated` | Persistent `SIMULATED RESULT` badge and policy/version |
| `evidence_state:future_live` | `FUTURE RUNTIME — NOT AVAILABLE` placeholder, never a green/live signal |

## 16. Safety and Approval Model

### 16.1 Approval contract

Every future mutating action requires:

- explicit operator intent and human-readable scope preview;
- exact `target_type`, `target_id`, `target_version`, and `target_digest`;
- authorized and prohibited actions;
- constraints, risk class, stop conditions, and expiry;
- operator identity and decision;
- confirmation after any material change;
- append-oriented audit event;
- cancellation and, when technically possible, rollback/compensation plan;
- independent validation and final outcome.

Approval to prepare or approve a configuration does not authorize its execution.
Approval scope remains separated for commit, push, PR creation, ready state,
merge, deployment, external write, provider call, and tool action. A higher
safety policy can refuse an otherwise well-formed approval.

The four target fields form an immutable approval binding. `target_digest` MUST
be computed for the exact entity identified by `target_type`, `target_id`, and
`target_version`; an approval is valid only when all four fields match. Any
target mutation or version change invalidates or supersedes the approval and
requires a new decision. An approval MUST NOT be reused across entity classes,
IDs, or versions. Direct approvals of RoutingPolicy, QueueItem, ContextPacket,
Integration configuration, Security configuration, or a future approved
configuration manifest use their own typed target; `recommendation_id`, when
present, remains an optional source reference.

The Approval Inbox MUST resolve and display the complete bound identity before
decision: target type, human label, target ID, version, digest, scope, risk,
expiry, and provenance. A future execution layer MUST verify the complete
binding before honoring an approval. The current static UI only displays and
simulates this contract; it performs no authorization or execution.

### 16.2 Hard prohibitions

No self-approval, blanket approval, inferred consent, approval replay, hidden
side effect, autonomous safety-policy change, or permission widening. No
MellyTrade, broker, trading, order, buy/sell, or live-execution control.

## 17. Security and Secrets Boundary

Secret values, credentials, OAuth tokens/grants, provider keys, environment
values, private keys, cookies, account IDs, and secure-store contents MUST never
enter the Control Plane DOM, logs, exports, search index, URLs, analytics,
fixtures, screenshots, error messages, or artifacts.

Permitted metadata only:

- `configured` / `not_configured` / `unknown`;
- authentication mode, never value;
- project and action scope;
- owner/steward;
- validation state/time/evidence;
- rotation due date;
- health and revocation metadata;
- read/write and risk class;
- store type as a generic label.

Future credential storage, retrieval, OAuth, rotation, and revocation require a
separate security architecture. The Control Plane may later request such an
operation through a guarded seam, but cannot implement the store or reveal a
value.

Threat requirements include prompt-injection isolation, poisoned-provenance
flags, digest mismatch refusal, confused-deputy prevention, least privilege,
redaction before rendering, content-free refusal logs, and independent
validation. Security metadata with unknown coverage must not render "secure."
Confused-deputy prevention MUST compare the complete Approval target binding;
matching a digest, recommendation, display label, or scope without matching
target type, ID, and version authorizes nothing.

## 18. Provenance and Trust

Every critical surface exposes:

- source and source type;
- captured at and validated at;
- freshness/review boundary;
- confidence and stated basis;
- mutable/immutable classification;
- estimated/confirmed basis;
- static/simulated/runtime-unavailable source mode;
- supersession and conflict state;
- evidence references and validator verdict.

Repository-derived, verified evidence is not automatically current; generated
content is not authoritative; externally sourced content retains its origin and
review status. Trust, freshness, relevance, and authorization are independent.
Conflicts display both claims and precedence/rationale. The UI never silently
chooses a winner.

## 19. Failure and Unknown States

| Condition | Required presentation/behavior |
| --- | --- |
| Missing provider validation | `availability_status:unknown` or `availability_status:unavailable`; no inferred availability |
| Partial provider/model data | `availability_status:degraded` plus `evidence_state:partial`; list missing fields and affected routes |
| Missing price/token measurement | Cost `null`/`—`; budget `unenforceable` |
| Policy conflict | Show conflicting rules and precedence; prevent lifecycle `ready` if unresolved |
| No eligible model | `NO ELIGIBLE ROUTE`; show `selection_state:rejected` or `selection_state:excluded` alternatives and reasons |
| Stale/invalid context | Set `freshness_state:stale` or `freshness_state:expired`; flag packet and dependent simulations; no silent refresh |
| Context conflict | Show both sources; require operator resolution or exclude packet |
| Missing traffic sequence | Set `evidence_state:partial`; mark gap/partial capture; no fabricated event |
| Failed/absent validator | `REJECT` or `NOT_RUN`; never pass |
| Expired/revoked approval | `approval_state:expired` or `approval_state:revoked`; authorizes nothing; future action refused |
| Secret/private content | Redact/refuse content; retain content-free category/evidence |
| Fixture parse failure | Error state with `evidence_state:static_demo` identity; do not fall back to "live" |
| Future runtime unavailable | Keep static shell usable; display `evidence_state:future_live` with `availability_status:unavailable` |

Recovery actions in this phase are Inspect, Review evidence, adjust a draft,
re-run a local simulation, or export a corrected manifest. There is no
auto-fix, live retry, or hidden fallback.

## 20. Static Fixture Strategy

### 20.1 Required source modes

Every rendered record carries one visible evidence mode:

- `evidence_state:canonical` → `CANONICAL REPOSITORY EVIDENCE`
- `evidence_state:static_demo` → `STATIC FIXTURE`
- `evidence_state:simulated` → `SIMULATED RESULT`
- `evidence_state:future_live` → `RUNTIME DATA UNAVAILABLE` or
  `FUTURE INTEGRATION`, according to applicability
- `evidence_state:partial` → `PARTIAL EVIDENCE`
- `evidence_state:unknown` → `EVIDENCE UNKNOWN`

Fixtures are deterministic, versioned, locally stored in a future authorized
slice, and contain `schema_version`, `fixture_id`, `example_notice`,
`generated_at` or `snapshot_date`, source note, safety note, and provenance.
Fixture timestamps describe capture/authoring, not current freshness.

### 20.2 Coexistence rules

Mixed-source screens label every card/row, plus a screen-level coverage summary.
Fixture values never fill gaps in repository evidence without changing the
mode to `STATIC FIXTURE`. A simulation records its input fixture IDs and policy
version. A future live source cannot silently replace a fixture; the transition
requires its own readiness review and visible source-mode change.

The OpenRouter Observatory labels remain mandatory where its data is reused:
`STATIC SNAPSHOT`, `NO API KEY`, `NO MODEL CALLS`, `NO ACCOUNT USAGE`,
`NOT LIVE PRICING`, `FUTURE-GATED LIVE CATALOG`.

### 20.3 Deterministic fixture set

A future static slice uses one cross-linked fixture bundle containing providers,
models, agents, routing policies, context packets, runs, costs, queues,
artifacts, approvals, recommendations, and security metadata. The bundle MUST:

- include at least one complete, incomplete, stale, degraded, unavailable,
  blocked, failed, unknown, awaiting-approval, and superseded example wherever
  the entity supports that state;
- use fixed timestamps, IDs, digests, policy versions, and provenance so repeat
  renders and simulations are deterministic;
- give every Approval fixture a resolvable target type, ID, version, and digest;
- include desktop-scale and mobile-scale record volumes without changing
  semantics;
- contain no keys, credentials, account IDs, private content, or live-access
  claims;
- keep every cross-reference resolvable or deliberately mark it as a tested
  missing-reference failure;
- place a `STATIC DEMONSTRATION — NOT LIVE` notice at bundle and record level.

## 21. Accessibility

- Meet WCAG 2.2 AA for the future implementation.
- All functions are keyboard operable with logical focus order and visible,
  unclipped focus.
- Landmarks, headings, breadcrumbs, tabs, tables, dialogs, sheets, and
  status/live regions use native semantics first.
- Graphs, constellations, timelines, and matrices have complete structured text
  alternatives with the same selections and evidence links.
- Color, position, animation, glow, and line style never carry exclusive meaning.
- Body and label contrast is at least 4.5:1 on actual panel backgrounds; large
  text at least 3:1; non-text controls/focus at least 3:1.
- `prefers-reduced-motion` freezes orbital motion and route animation; the
  interface remains complete.
- `forced-colors`, 200% zoom, browser text resize, and reflow at 320px preserve
  content and controls.
- Pointer targets are at least 44×44px on touch surfaces.
- Loading, error, stale, unknown, degraded, blocked, and approval states are
  announced without excessive repetition.
- Redacted content is announced as redacted with category, never as an empty
  field.

## 22. Performance Budgets

Budgets apply to a future static frontend and are acceptance targets, not current
measurements:

- critical shell, title, safety labels, and primary navigation render within
  2 seconds on a mid-range laptop under a local cold-cache profile;
- usable shell and critical text without 3D or animation;
- initial static route JavaScript ≤ 180KB gzip and CSS ≤ 100KB gzip, excluding a
  separately gated enhanced renderer;
- any separately authorized optional 3D payload is lazy, ≤ 500KB gzip, loads
  only after the usable semantic shell, never blocks interaction, and falls
  back without data or control loss;
- no more than 1,000 DOM rows mounted in a dense table; virtualize above 200
  visible records while preserving accessibility;
- filter/search response ≤ 100ms for 5,000 fixture metadata records on a
  mid-range desktop;
- inspector open/selection feedback ≤ 100ms;
- no continuous animation on mobile or under reduced motion;
- animation targets 60 FPS on reference desktop and must freeze/fall back after
  a sustained three-second average below 30 FPS;
- decorative animation ≤ 2 concurrent groups and ≤ 1% average main-thread time
  after idle on reference desktop;
- layout shift target CLS < 0.1;
- no page-level horizontal overflow at supported widths;
- charts/graphs progressively summarize above 500 nodes and provide a complete
  filtered table;
- low-power, `prefers-reduced-motion`, `prefers-reduced-data`, failed capability
  detection, and background-tab states use the static semantic fallback;
- background polling is absent in the static phase.

If an effect threatens readability, input latency, memory, battery, or fallback
parity, remove the effect.

## 23. Component Inventory

All components accept `sourceMode`, provenance, and status inputs where they
render data. Outputs are selection/navigation/configuration-draft events only.

| Component | Purpose; inputs → outputs | States/responsive/accessibility | Safety constraint |
| --- | --- | --- | --- |
| `ControlPlaneShell` | Project, nav, notices → navigation | desktop rails/mobile bottom nav; landmarks/skip links | No hidden execution routes |
| `GlobalStatusBar` | Project, source coverage, safety/approval counts → destination navigation | sticky desktop bar/mobile Status summary; announced changes | Counts unknown when coverage unknown; no false global health |
| `ProjectSwitcher` | projects/current scope → scope selection | loading/empty/unknown; combobox/sheet | Clears drafts; never widens scope silently |
| `GlobalSearch` | metadata index/query → entity navigation | compact overlay/mobile full screen; combobox | Metadata only; no secret/private indexing |
| `ProviderRegistry` | providers/filters → provider selection | table/cards; semantic headers | Configured ≠ available |
| `ModelGatewayGrid` | models/policy context → model selection/compare | constellation/grid/list; text equivalent | Selection is not routing |
| `RoutingPolicyCenter` | policy draft/rules → draft changes | rule table/cards; reorder controls | Safety precedence locked |
| `RoutingSimulationPanel` | task/policy/packet assumptions → explanation request | loading/insufficient/conflict/result; stacked mobile form | Deterministic local simulation only |
| `RoutingExplanation` | selected/rejected candidates, rules, basis → evidence navigation | graph plus ordered text/mobile text first; keyboard-selectable candidates | Explanation is not route execution or approval |
| `ContextSourceTable` | sources/filters → selection | table/cards; redaction labels | Protected content not rendered |
| `ContextPacketBuilder` | selected refs/strategy → manifest preview | dimension-qualified draft/conflict/blocked/ready presentation | Approval binds exact packet type, ID, version, and digest |
| `MemoryFreshnessPanel` | memory metadata → review navigation | status list/mobile cards | No auto-refresh or deletion |
| `AgentDirectory` | agents/filters → agent selection | grid/table/mobile list | No launch control |
| `AgentDetailInspector` | agent contract/evidence → trace links | side inspector/detail sheet | Authority not inferred from autonomy class |
| `AgentTrafficGraph` | events/filters → event selection | graph/timeline/list fallback | Static demo vs future traffic persistent |
| `RunLedger` | runs/filters → run selection/export view | virtual table/cards | Unknown/partial evidence retained |
| `CostObservatory` | cost records/basis → comparisons | chart/table/card fallback | Estimate distinct from confirmed |
| `QueueBoard` | queue items/status → review selection | board/ordered mobile cards | Planning only; forbidden execution verbs |
| `ArtifactBrowser` | artifact metadata → trace/open permitted artifact | tree/table/cards | Sensitivity and digest enforced |
| `IntegrationCatalog` | integrations/filters → inspector | category grid/cards | No connect/credential flow |
| `SecurityBoundaryPanel` | policy/access metadata → evidence trace | matrix/list/mobile alerts | No secret value in DOM |
| `ApprovalInbox` | approvals with target type/ID/version/digest → bound-target resolution and decision draft | split view/mobile detail-first; target identity precedes controls | Full typed target, scope, risk, expiry, and provenance before decision; never resolves by digest or Recommendation alone |
| `RecommendationLedger` | recommendations → review decision | lifecycle/table/timeline | No automatic implementation |
| `OperatorConsole` | aggregate evidence → safe navigation | rails/core/timeline/mobile cards | Per-card coverage; no false global health |
| `ProvenanceBadge` | source/freshness/trust → evidence drawer | text-first tooltip/detail | Unknown stays unknown |
| `StaticDemoBadge` | source mode → no data mutation | persistent at all breakpoints | Cannot be hidden by compact mode |
| `StatusChip` | dimension, value, label, and applicable provenance/evidence context → dimension-preserving filter | text/icon/color; visible or programmatic dimension; accessible name such as `Availability: degraded` | Rejects unqualified values; never merges orthogonal states |
| `EvidenceDrawer` | evidence refs → trace navigation | bottom/right sheet | Read-only and redaction-aware |
| `CommandPalette` | safe commands → navigation/filter | keyboard/mobile search | Allowlist excludes execution verbs |

## 24. Decision Records

| Decision | Rationale | Rejected alternative | Consequence / frontend implication | Safety implication |
| --- | --- | --- | --- | --- |
| Five primary navigation groups | Reduces top-level overload while preserving domain reach | Twelve equal top-level tabs | Secondary rails and route hierarchy required | Safer actions remain discoverable, not hidden |
| Control Plane and Data Plane are separate | Prevents UI specification from implying runtime | One full-stack "orchestrator" surface | Frontend uses explicit seams/placeholders | No execution authority from display state |
| Source Arena remains product hero | Preserves accepted design identity | Replace it with orbital router branding | Orbital core stays functional Overview content | Avoids overstating a live router |
| Static-first with explicit source modes | Current repo is static and evidence-driven | Fake live telemetry | Every record carries mode/coverage | Fixtures cannot masquerade as runtime |
| Six orthogonal status dimensions | Eliminates ambiguous "active/green" | One universal status enum | Components accept lifecycle, availability, evidence, freshness, approval, and selection as typed dimension/value pairs | Availability, evidence, freshness, approval, and selection never imply one another |
| Deterministic routing simulation | Reviewable and reproducible | Adaptive black-box routing in current phase | Explanations include rules/rejections/basis | No live call or self-changing policy |
| Exact typed, versioned, digest-bound approvals | Matches established approval contract | General toggle, digest-only lookup, or blanket consent | Approval detail resolves and displays target type, ID, version, digest, and scope | Prevents replay, confused-deputy reuse, and permission widening |
| Metadata-only security surface | Useful visibility without exposure | Credential entry/reveal in Control Plane | Generic store/health labels only | Secret values never enter frontend |
| Mobile as operator companion | Dense desktop graphs do not translate safely | Shrink desktop dashboard | Status/approval/evidence first; graphs optional | Reduces accidental decisions and hidden scope |
| Complete non-3D fallback | Clarity and resilience outrank spectacle | 3D-only orbital interaction | Same semantic model renders as lists/maps | Accessibility and degraded-state parity |

## 25. Integration Seams

These are conceptual, versioned frontend contracts for future work, not APIs:

- `EstateSnapshotReader` → providers, models, agents, skills, tools, integrations.
- `RoutingSimulationService` → deterministic request and explanation response.
- `ContextManifestService` → packet draft, digest, conflict, redaction metadata.
- `TrafficEventReader` → paged RunEvents with correlation and redaction.
- `RunLedgerReader` → Runs, costs, validators, artifacts.
- `QueueManifestService` → plans and exported manifests; no dispatch method.
- `ApprovalRecordService` → approval records and decisions; no executor method.
- `SecurityMetadataReader` → content-free configuration/health metadata.
- `ProvenanceResolver` → evidence refs, freshness, supersession, conflicts.

Every seam returns `schema_version`, `source_mode`, `coverage`, `generated_at`,
and explicit error/partial states. Pagination, cancellation, timeouts, caching,
authentication, authorization, rate limits, and transport remain future Data
Plane/read-adapter specifications. No frontend key or provider credential is
permitted.

## 26. Open Questions

### 26.1 Blocking for this specification

None. Navigation, module ownership, state dimensions, approval boundaries,
responsive behavior, and static/runtime separation are decided.

### 26.2 Non-blocking for a static frontend task

- Exact visual token values within the accepted design system.
- Which safe metadata columns are default-visible in each dense table.
- Whether the inspector width preference persists only for the local session.
- Which deterministic fixture volume is used for performance QA.

### 26.3 Deferred and separately gated

- Runtime event transport and persistence.
- Provider/public catalog readiness and live availability semantics.
- Authentication, RBAC, multi-operator approval, and credential store.
- Data Plane command protocol, retries, rollback, and cancellation enforcement.
- Adaptive policy evaluation and evidence thresholds.
- Artifact storage/viewer security.
- Enhanced 3D renderer implementation.

No deferred question authorizes implementation or weakens a safety rule.

## 27. Frontend Readiness Gate

A future static frontend task may begin only when it:

- treats this specification and the accepted source contracts as normative;
- declares exact file scope and excludes backend/runtime/provider work;
- uses deterministic local fixtures with source-mode labels;
- implements all ten modules only to the authorized slice depth;
- preserves navigation, entity fields, state dimensions, workflows, and safe
  vocabulary without inventing execution;
- treats Approval target type, ID, version, and digest as one indivisible
  binding and renders that identity without Recommendation inference;
- carries the owning dimension through every status chip, badge, filter, table,
  card, inspector, and mobile summary;
- provides desktop/mobile/non-3D/reduced-motion/table alternatives;
- includes loading, empty, unknown, stale, degraded, blocked, error, and
  unavailable-runtime states;
- keeps security/credential metadata content-free;
- validates no external requests, keys, account usage, model calls, provider
  connections, workflow/dependency/deploy changes;
- receives separate operator authorization.

This specification passes the design-level readiness gate. It does not start or
authorize the frontend task.

## 28. Acceptance Criteria

- [ ] Product is positioned as an operator-controlled coordination/governance
      layer, not a live autonomous router.
- [ ] Control Plane and future Data Plane responsibilities are unambiguous.
- [ ] Five primary navigation groups and their secondary destinations are used.
- [ ] All ten Control Plane modules implement every module contract item.
- [ ] Intelligence modules remain recommendation/inspection only.
- [ ] All core entities expose stable IDs, ownership, timestamps, provenance,
      relationships, status, static representation, and future representation.
- [ ] Orthogonal lifecycle, availability, evidence, freshness, approval, and UI
      selection states are not collapsed.
- [ ] Every status enum member has one dimension owner, and every module status
      row is dimension-qualified or explicitly cross-dimensional.
- [ ] All ten operator workflows terminate without live execution.
- [ ] Overview orbital core explains policy, candidates, context, assignment,
      blocks, fallbacks, cost, and latency in text and visual form.
- [ ] Desktop layouts cover 1366×768 through ultrawide and remain usable without
      3D.
- [ ] Mobile is independently designed and has no dense default routing graph.
- [ ] Every critical surface distinguishes repository evidence, fixture,
      simulation, unavailable runtime, and future placeholder.
- [ ] Unknown, missing, unmeasured, stale, degraded, and failed data remain honest.
- [ ] Safe action vocabulary is enforced; execution/trading/connect-live verbs
      do not appear as controls.
- [ ] Every future mutation is intent-, digest-, scope-, approval-, audit-, stop-,
      cancellation-, and validation-gated.
- [ ] Every Approval binds one exact target type, ID, version, and digest;
      mutation requires reapproval and the Approval Inbox renders the bound
      identity without inference.
- [ ] No secret value or account identifier can enter a rendered/exported path.
- [ ] Source Arena remains the leading product metaphor; Overview orbit is
      functional and supporting.
- [ ] Accessibility and performance budgets are testable.
- [ ] No current provider connection, agent launch, live traffic, account usage,
      backend, or runtime capability is implied.

## 29. Explicitly Deferred Work

- any frontend/static Control Plane implementation;
- fixture authoring and fixture validation;
- 3D Scene Foundation and all renderer work;
- backend/read adapters and runtime contracts;
- provider/model calls and routing execution;
- agent/tool/skill execution;
- integration authentication or connection;
- context retrieval, compression runtime, persistence, and refresh;
- traffic collection, streaming, queue dispatch, retries, and scheduling;
- artifact generation/storage;
- secrets storage, OAuth, RBAC, and multi-operator workflows;
- cost/account usage ingestion and billing reconciliation;
- deployment, release, push, PR, merge, and production validation;
- all MellyTrade, trading, broker, order, and execution functionality.

Task-local next task after this specification's local commit:
`MELLYCORE-OMNIROUTER-INSPIRED-CONTROL-PLANE-SPEC-PUBLISH-001`.

Product next task after specification acceptance:
`MELLYCORE-3D-SCENE-FOUNDATION-001`, still separately gated and unauthorized by
this document.
