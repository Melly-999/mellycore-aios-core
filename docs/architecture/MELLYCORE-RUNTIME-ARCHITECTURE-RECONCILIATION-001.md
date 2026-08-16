# MELLYCORE-RUNTIME-ARCHITECTURE-RECONCILIATION-001

Status: **Specification / decision-record level only.** No runtime, adapter,
daemon, backend, credential, provider connection, or deployment work is
implemented or authorized by this document.

Scope: compares MellyCore AIOS's currently observed (documented and/or
implemented) architecture against a set of runtime-architecture patterns
inspired by **Multica**. Multica is used here strictly as an architectural
reference point for pattern names and shapes; no Multica source code,
configuration, or proprietary text is reproduced anywhere in this document.

## 1. Executive Decision

MellyCore should **selectively adopt Multica-inspired separation-of-concerns
and safety patterns as future specification targets**, not as an
implementation dependency and not on today's timeline.

- Four of the seventeen evaluated patterns are **already present** in
  MellyCore's accepted specifications (`KEEP`): provider adapters,
  capability discovery, an execution event log, and human approval gates.
  MellyCore's approval-gated operating loop already meets or exceeds the
  Multica-inspired human-approval pattern.
- Seven patterns are net-new and net-positive with low architectural risk
  (`ADOPT`): per-task workspace, MCP-per-agent/runtime, concurrency limits,
  watchdogs/timeouts, task-scoped execution tokens, issue/task/execution
  separation, and a secret broker in place of plaintext environment storage.
- Four patterns already exist in a different, weaker, or informal shape and
  should be reconciled rather than replaced (`ADAPT`): the
  Agent-!=-Runtime-!=-Task separation, task-scoped provider "home," session
  resumption, and canonical-skill-to-provider injection.
- Two patterns are architecturally acceptable in principle but their
  implementation is currently blocked by existing governance
  (`DEFER`): a local execution daemon/runtime host, and live
  heartbeat/runtime status.
- **Zero** patterns are rejected outright. All seventeen are compatible with
  MellyCore's local-first, vendor-neutral, fail-closed identity; none require
  abandoning an accepted contract.

None of this reconciliation authorizes implementation. MellyCore remains in
its docs-first phase (`CLAUDE.md`, `AGENTS.md`); every `ADOPT`/`ADAPT` item
below is a **specification target** for a future, separately authorized task,
and every `DEFER` item names the exact governance gate blocking it today.

## 2. Current Observed MellyCore Architecture

This section reflects only what is documented or implemented in this
repository at the time of writing (`shared_context/PROJECT_STATE.md`,
`shared_context/RUN_QUEUE.md`, `shared_context/SAFETY_CONTRACT.md`,
`shared_context/MODEL_ROUTING.md`, `AGENTS.md`, `docs/specs/`,
`docs/decisions/`, `scripts/`).

- **Product identity.** Local-first, operator-controlled AI Operating
  System. The controlled improvement loop is
  `observe → analyze → recommend → approve → implement → validate → record`.
  Consequential action requires explicit operator approval; the system does
  not autonomously change safety rules, merge, deploy, or store provider
  secrets.
- **Two product layers (locked, planned).** Layer 1, Command Center
  (control/observability/governance UX). Layer 2, ten planned AI Workspaces.
  Both are product/navigation surfaces that project canonical state; neither
  becomes a new canonical data owner.
- **Canonical logical modules (specification level).** Agent Runtime (owns
  run/attempt lifecycle), Framework Bridge (framework-neutral projection),
  Provider Registry (provider/model evidence: identity, credentials
  required, capabilities, availability, health, rate limits, pricing
  evidence), Model Router (capability-first filtering, policy precedence,
  fallback), Integration Gateway (credential use, authorization,
  provider-bound execution, data-handling controls), AI Operations / Cost
  Observatory (cost class, estimates, freshness). Defined in
  `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md`,
  `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md`, and
  `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`.
  None of these modules has a runtime implementation on canonical `main`.
- **Data contract (specification + fixtures, no runtime consumer).**
  `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md` defines
  fourteen dashboard-facing fixture entities with companion JSON Schema and
  example fixtures under `shared_context/operations/`. No script in
  `scripts/` reads, imports, or validates these files today
  (`shared_context/operations/README.md`).
- **Guarded local tooling (implemented).**
  - `scripts/context_gate/` — a guarded admission CLI: content-free index,
    computed audit, seven validated canonical records, read-only dashboard
    surface. Implements a `PROPOSE → DIFF → HUMAN APPROVAL → WRITE → VERIFY →
    AUDIT` pattern already, for context admission specifically.
  - `scripts/loop_ops/` — the Loop Operations Foundation: nine registered
    loops, one exercised, **zero production-enabled**, report-only by
    default.
  - `scripts/mellycore_batch/` — `activation.py` / `policy.py`: a local-only
    planning/validation layer for OpenAI Batch usage with a hard,
    hardcoded kill switch (`stage_c_live_execution_authorized = False`),
    an explicit request/token envelope, Decimal-only cost estimation against
    a hard USD cap, and a policy-level `live_provider_connections_allowed =
    false` gate that returns a distinct exit code. No credential value is
    ever read or printed; only presence/absence is checked. This is
    MellyCore's most mature example of fail-closed runtime-adjacent design
    today, despite having no live provider connection.
  - `scripts/validate_project_state.py`, `tests/` — 245 standard-library
    tests validate structure and safety-sensitive patterns; no external
    test framework dependency.
  - `agent_prompts/{chatgpt,claude,codex,glm,grok,loops,warp,zed}/` — a
    lightweight, already-existing precedent for "one canonical intent,
    multiple provider-specific renderings," documented per-provider rather
    than schema-driven.
- **Model/provider routing (documentation, not runtime).**
  `shared_context/MODEL_ROUTING.md` assigns human-facing roles per
  provider/agent (ChatGPT, Claude/Claude Code, Codex, GLM, Grok, OmniRouter,
  Warp, Zed, VS Code, GitHub) and states provider API keys stay local-only
  and must not be committed. This is a routing-role convention, not an
  implemented Model Router.
- **Safety posture.** `shared_context/SAFETY_CONTRACT.md` and `AGENTS.md`:
  no secrets, no real API keys, no provider tokens, no `.env` values, no
  account IDs, no destructive git without approval, no deploy without
  approval, no MellyTrade mutation. Production deployment currently follows
  an approved merge automatically via Vercel's Git integration with **no
  separate technical gate** — enforcement is procedural (Model A, temporary,
  static-phase-only, per-merge explicit approval), not technical.
- **What does not exist today.** No local execution daemon, no persistent
  runtime host process, no live heartbeat/status feed, no per-task
  filesystem/workspace isolation, no session-resumption mechanism, no
  secret broker (credentials are simply excluded from the repository and
  expected to live in the operator's local environment or OmniRoute), and
  no first-class `Issue` entity distinct from a `Run`/`Attempt`.

## 3. Multica-Inspired Pattern Evaluation

Legend: **KEEP** — already adequately present, no change needed. **ADOPT** —
absent; add substantially as-is. **ADAPT** — present in a different/weaker
form; extend or reshape MellyCore's existing concept rather than importing a
new one. **REJECT** — inappropriate for MellyCore. **DEFER** — architecturally
acceptable but currently blocked by an existing governance gate.

| # | Pattern | Classification |
|---|---|---|
| 1 | Agent != Runtime != Task | ADAPT |
| 2 | Local execution daemon / runtime host | DEFER |
| 3 | Provider adapters | KEEP |
| 4 | Capability discovery | KEEP |
| 5 | Per-task workspace | ADOPT |
| 6 | Task-scoped provider home | ADAPT |
| 7 | Session resumption | ADAPT |
| 8 | Canonical skills → provider-specific injection | ADAPT |
| 9 | MCP per agent/runtime | ADOPT |
| 10 | Execution event log | KEEP |
| 11 | Heartbeat/runtime status | DEFER |
| 12 | Concurrency limits | ADOPT |
| 13 | Watchdogs/timeouts | ADOPT |
| 14 | Task-scoped execution tokens | ADOPT |
| 15 | Human approval gates | KEEP |
| 16 | Issue/task/execution separation | ADOPT |
| 17 | Secret broker instead of plaintext env storage | ADOPT |

### 3.1 Agent != Runtime != Task — ADAPT

- **Reason.** The Control Plane spec already separates Agent Runtime
  (run/attempt lifecycle) from Framework Bridge (framework-neutral
  projection) and Model Router (selection). It does not yet formalize
  "Task" as a distinct entity from "Run"/"Attempt" — `RUN_QUEUE.md` today
  models tasks as long-form prose with embedded named identifiers
  (`MELLYCORE-<NAME>-NNN`), not schema entities.
- **Risk.** Low. Purely a naming/entity-boundary clarification at spec
  level; does not touch any implemented surface.
- **Implementation notes.** Extend
  `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md`'s entity
  catalogue (§7.2) to explicitly separate: **Agent** (a routing role/persona,
  e.g. "Claude Code"), **Runtime** (an execution host/process class, e.g. a
  future local execution daemon), and **Task** (a unit of approved work,
  independent of which agent or runtime executes it). This does not imply a
  1:1:1 binding between the three.
- **Affected modules/files.** `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md`,
  `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md`,
  `shared_context/operations/` (future entity addition), `shared_context/MODEL_ROUTING.md`.

### 3.2 Local execution daemon / runtime host — DEFER

- **Reason.** Compatible in principle with "local-first," but MellyCore has
  no implemented Agent Runtime, and introducing a persistent local execution
  process would cross **migration trigger #6 ("first execution-capable
  agent")** in the Model A Production Deployment Authorization Contract
  (`shared_context/PROJECT_STATE.md`), which requires a separate Model B
  reconsideration decision before any affected implementation or merge may
  proceed.
- **Risk.** High if implemented prematurely — a runtime host is the single
  largest blast-radius addition on this list (arbitrary local execution,
  potential credential exposure, new attack surface). Zero risk while
  deferred.
- **Implementation notes.** None authorized. When migration trigger #6 is
  deliberately crossed via its own governance decision, model the daemon as
  a capability-gated, fail-closed process analogous to
  `scripts/mellycore_batch/policy.py`'s existing hard gate pattern
  (explicit boolean allow-flag, distinct exit code, no default-on state).
- **Affected modules/files.** None today. Future: a new `scripts/` package,
  gated by a new entry in `shared_context/SAFETY_CONTRACT.md` and a Model B
  decision record under `docs/decisions/`.

### 3.3 Provider adapters — KEEP

- **Reason.** Already an accepted architectural concept: Provider Registry
  owns provider/model evidence, and adapters are explicitly named as the
  future implementation unit in
  `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`
  and the Enterprise Provider Architecture ADR. `agent_prompts/` is a
  present-day, lightweight precedent.
- **Risk.** None — no change proposed.
- **Implementation notes.** No action required by this reconciliation.
  Future adapter implementation remains gated behind its own
  specification-level acceptance (already stated as
  "specification-level acceptance only — no registry implementation,
  adapter, credential, provider authentication...").
- **Affected modules/files.** `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`
  (reference only).

### 3.4 Capability discovery — KEEP

- **Reason.** Already locked as a research direction: the federated,
  provenance-bearing Capability View and the future Hardware Capability
  Service (`shared_context/PROJECT_STATE.md`, "Capability View and Hardware
  Capability Service"). This already matches the Multica-inspired pattern's
  intent (discover what a provider/runtime/model can actually do before
  routing to it).
- **Risk.** None — no change proposed.
- **Implementation notes.** None. Continue to reference the existing locked
  direction rather than re-specifying it.
- **Affected modules/files.** `shared_context/PROJECT_STATE.md` (reference
  only).

### 3.5 Per-task workspace — ADOPT

- **Reason.** No current concept of an isolated working directory or state
  scope per task. Once any future task execution exists, unscoped shared
  state increases the chance of cross-task leakage (files, context,
  partial credentials). This aligns with MellyCore's own worktree-based
  session pattern already visible in this repository's layout
  (`02_Worktrees/`).
- **Risk.** Low at specification level. Medium at implementation time
  (requires filesystem/process isolation design) — but implementation is
  not authorized by this document.
- **Implementation notes.** Specify a per-task workspace as a
  deterministic, disposable directory scoped to one Task entity (see §3.1),
  cleaned up or archived after completion, never shared across concurrent
  tasks. Should compose with the existing Context Gate admission pattern
  rather than bypass it.
- **Affected modules/files.** Future addition to
  `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` and
  `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`.

### 3.6 Task-scoped provider home — ADAPT

- **Reason.** The Integration Gateway Security Contract already decided the
  **shape** of tenant-provider and tenant-capability authorization records
  as explicit, separate, independently revocable, with absence-denies
  semantics. What it does not yet name is a task-scoped "home" — a bounded
  location where a task's provider-facing state (session artifacts,
  temporary config, non-secret continuity data) lives, distinct from the
  authorization record itself.
- **Risk.** Low. Extends an already-accepted contract; does not change its
  authorization semantics.
- **Implementation notes.** Model "provider home" as a sub-scope of the
  per-task workspace (§3.5): task-scoped, provider-labeled, non-secret by
  construction (secrets are brokered per §3.17, never stored in the
  workspace). Must not become an alternate credential store.
- **Affected modules/files.** `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`.

### 3.7 Session resumption — ADAPT

- **Reason.** No current mechanism to resume a provider session
  (e.g., continue a Claude Code or Codex conversation) as a MellyCore
  concept. This is a genuinely useful UX/continuity pattern, but it must be
  bounded by the explicit constraint restated in §4: **provider sessions are
  a continuity cache, not canonical memory.** MellyCore's canonical memory
  is Shared Context / Context Gate, and that must not change.
  `shared_context/AGENT_HANDOFF.md` is today's manual, prose-based
  approximation of session continuity across agent handoffs.
- **Risk.** Medium if the boundary is not enforced — the main failure mode
  is a future implementation quietly treating resumed provider session
  state as authoritative, which would violate the Context Gate's
  guarded-admission model and reintroduce untraced state.
- **Implementation notes.** Specify session resumption strictly as a
  cache keyed by (Agent, Task) that MellyCore may use to reduce redundant
  setup, always re-derived from and reconcilable against canonical Shared
  Context; never a substitute write path into Shared Context.
- **Affected modules/files.** `shared_context/AGENT_HANDOFF.md` (today's
  manual analogue), future addition to
  `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md`.

### 3.8 Canonical skills → provider-specific injection — ADAPT

- **Reason.** `agent_prompts/{chatgpt,claude,codex,glm,grok,loops,warp,zed}/`
  already implements a primitive, hand-maintained version of this pattern:
  one intent, several provider-specific renderings. It is not schema-driven
  and has no single canonical source of truth that generates the
  provider-specific copies — each is authored independently, which risks
  drift.
- **Risk.** Low to adopt as a specification; the existing informal version
  already carries the real risk (documentation drift) that formalizing this
  pattern would reduce.
- **Implementation notes.** Specify a canonical skill/intent record (one
  per capability) with declared provider-specific injection/rendering rules,
  and treat the current `agent_prompts/*/README.md` files as the
  first migration candidates, not as the target state.
- **Affected modules/files.** `agent_prompts/` (all subdirectories), future
  schema addition under `shared_context/operations/` or a new
  `docs/specs/` document.

### 3.9 MCP per agent/runtime — ADOPT

- **Reason.** No current concept of scoping tool/MCP access per agent or
  runtime; `shared_context/MODEL_ROUTING.md` assigns roles but not tool
  scope. Different agents already have different practical trust levels in
  this workflow (e.g., a documentation-only agent vs. an implementation
  agent), and a shared, unscoped tool surface is a needless privilege
  expansion.
- **Risk.** Low to specify. Reduces risk once implemented (least-privilege
  tool access per agent/runtime is safer than a global tool surface).
- **Implementation notes.** Extend the Integration Gateway's trust-boundary
  model so that MCP/tool availability is declared per Agent × Runtime
  combination, with the same explicit/separate/revocable/absence-denies
  semantics already accepted for provider authorization (§3.6).
- **Affected modules/files.** `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`,
  `shared_context/MODEL_ROUTING.md`.

### 3.10 Execution event log — KEEP

- **Reason.** Already covered by the accepted Unified Run Ledger concept
  ("one inspectable history for validated runs and outcomes,"
  `README.md`, `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md`)
  and, in practice today, by Context Gate's computed audit and
  `docs/tasks/` durable reports.
- **Risk.** None — no change proposed.
- **Implementation notes.** None required by this reconciliation. A future
  Task entity (§3.1) should reference Unified Run Ledger entries rather
  than duplicate an event log.
- **Affected modules/files.** `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md`
  (reference only).

### 3.11 Heartbeat/runtime status — DEFER

- **Reason.** Runtime Constellation is already a locked flagship visual
  concept, but it is explicitly a **projection**, not a canonical runtime
  owner, and "displayed does not mean installed, supported, connected, or
  running" is an explicit invariant. A live heartbeat requires a live
  runtime process (§3.2), which is itself deferred behind migration
  trigger #6.
- **Risk.** Low while deferred. The main risk this pattern guards against
  (Runtime Constellation silently implying liveness it doesn't have) is
  already mitigated today by the explicit invariant above.
- **Implementation notes.** None authorized now. When a runtime host is
  eventually authorized (§3.2), heartbeat/status should feed Runtime
  Constellation as real telemetry rather than static display data, and the
  "displayed != running" invariant must be updated to reflect the new
  live signal rather than removed.
- **Affected modules/files.** None today. Future:
  `shared_context/PROJECT_STATE.md` (Runtime Constellation section).

### 3.12 Concurrency limits — ADOPT

- **Reason.** No current concept, but directly relevant: the Loop
  Operations Foundation already registers nine loops with zero
  production-enabled, which is itself an implicit, all-or-nothing
  concurrency ceiling (0) rather than a graduated limit.
- **Risk.** Low to specify; concurrency limits are a safety control, not a
  new capability — they only ever reduce the space of what an eventual
  runtime is allowed to do simultaneously.
- **Implementation notes.** Specify concurrency limits as a policy field
  owned by the future Agent Runtime module (per-agent and per-task-type
  ceilings), enforced at the same layer that currently enforces
  `scripts/mellycore_batch/policy.py`'s hard gates. Default should be the
  most restrictive value (as loops already default to report-only /
  non-production-enabled) until explicitly raised.
- **Affected modules/files.** `scripts/loop_ops/` (nearest existing
  analogue), future addition to
  `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md`.

### 3.13 Watchdogs/timeouts — ADOPT

- **Reason.** No general-purpose watchdog/timeout concept exists yet, but
  MellyCore already practices the same underlying philosophy in
  `scripts/mellycore_batch/activation.py`: hard request/input/output
  envelopes, a hardcoded `stage_c_live_execution_authorized = False` kill
  switch, and Decimal-only cost caps. This pattern generalizes that
  existing practice rather than introducing a new one.
- **Risk.** Low to specify; strictly reduces risk once implemented
  (bounds runaway execution time/cost).
- **Implementation notes.** Specify watchdogs/timeouts as a required
  property of any future Task execution: a maximum wall-clock duration and
  a fail-closed default action (abort and log, never silently continue).
  Model on `scripts/mellycore_batch/policy.py`'s existing exit-code
  convention for machine-readable failure classification.
- **Affected modules/files.** `scripts/mellycore_batch/activation.py`,
  `scripts/mellycore_batch/policy.py` (existing analogues), future
  addition to `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md`.

### 3.14 Task-scoped execution tokens — ADOPT

- **Reason.** No current concept, but the Integration Gateway Security
  Contract already decided that tenant-provider and tenant-capability
  authorization must be explicit, separate, and independently revocable
  (§3.6). A task-scoped execution token is the natural credential-shaped
  extension of that same decision, applied to a single task's runtime
  privileges rather than to provider access alone.
- **Risk.** Low to specify; this pattern is itself a risk-reducing control
  once implemented (bounds blast radius of a compromised or misbehaving
  task to that task's own token).
- **Implementation notes.** Specify execution tokens as short-lived,
  task-scoped, and revocable independent of any provider credential; they
  authorize *what a task may do*, not *which provider it may reach* (that
  remains the Integration Gateway's existing authorization-record job).
- **Affected modules/files.** `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`.

### 3.15 Human approval gates — KEEP

- **Reason.** This is already core to MellyCore's identity, not an
  addition: the `observe → analyze → recommend → approve → implement →
  validate → record` loop, the Approval Queue planned surface, the Model A
  per-merge explicit-approval contract, and the `PROPOSE → DIFF → HUMAN
  APPROVAL → WRITE → VERIFY → AUDIT / EVIDENCE` pattern already specified
  for future Obsidian writeback. MellyCore's approval posture is at least
  as strict as, and arguably more thoroughly documented than, the
  Multica-inspired pattern it's being compared against.
- **Risk.** None — no change proposed. The only risk here is regression:
  any future `ADOPT`/`ADAPT` item above must not weaken this gate.
- **Implementation notes.** None required. Every other item in this
  document must be implemented so that it composes with, not around, this
  existing gate.
- **Affected modules/files.** `shared_context/PROJECT_STATE.md`,
  `shared_context/SAFETY_CONTRACT.md`, `AGENTS.md` (reference only).

### 3.16 Issue/task/execution separation — ADOPT

- **Reason.** No current schema-level separation of a durable problem/goal
  (Issue) from a unit of approved work (Task) from a specific attempt
  (Execution/Run). Today, `shared_context/RUN_QUEUE.md` and
  `shared_context/PROJECT_STATE.md` conflate all three in long-form prose
  under a single named identifier per effort
  (`MELLYCORE-<NAME>-NNN`), which is a directly observed pain point in this
  repository: both files are large, and tracking "what's actually next"
  requires reading extensive historical narrative rather than querying
  distinct entities.
- **Risk.** Low to specify. The main implementation risk is scope creep
  (rebuilding all of `RUN_QUEUE.md` at once) — should be introduced
  incrementally, starting with new work rather than a retroactive rewrite.
- **Implementation notes.** Reuse the existing fourteen-entity
  Operations Data Contract pattern (`docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md`)
  as the template: add `Issue`, `Task`, and `Execution` as distinct fixture
  entities with their own JSON Schema, related by explicit foreign keys
  rather than prose cross-references. This does not require or imply any
  runtime consumer — it can remain fixture/schema-only, exactly like the
  existing fourteen entities, consistent with the docs-first constraint.
- **Affected modules/files.** `shared_context/operations/` (new entity
  schemas + example fixtures), `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md`.

### 3.17 Secret broker instead of plaintext env storage — ADOPT

- **Reason.** MellyCore's current posture is purely exclusionary: "no
  secrets in the repository," provider keys "stay local-only." That is
  necessary but not sufficient — it says where secrets must *not* live, not
  how they are issued, scoped, or revoked when a future runtime does need
  one. A secret broker (a component that issues short-lived, scoped,
  audited access to a credential rather than handing out the raw value)
  is a strict improvement over ambient plaintext environment variables,
  and is effectively already the *informal* role OmniRoute/OmniRouter
  plays for this operator's local tooling today.
- **Risk.** Low to specify; this pattern only ever reduces exposure
  compared to the plaintext-env alternative it replaces.
- **Implementation notes.** Formalize the broker role already implied by
  OmniRoute/OmniRouter (`shared_context/MODEL_ROUTING.md`) as an explicit
  architectural component: MellyCore code paths request a scoped,
  short-lived credential handle from the broker at the moment of use, and
  never read, log, or persist the raw secret value themselves — mirroring
  `scripts/mellycore_batch/policy.py`'s existing
  `credential_material_present()` pattern, which already checks
  presence/absence without ever reading the value.
- **Affected modules/files.** `shared_context/MODEL_ROUTING.md`,
  `shared_context/SAFETY_CONTRACT.md`,
  `scripts/mellycore_batch/policy.py` (existing analogue), future addition
  to `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`.

## 4. Explicit Binding Statements

The following are binding constraints on this reconciliation and on any
future task that cites it:

- **Do not fork or embed Multica as a MellyCore core dependency.** Multica
  is an architectural inspiration only. No Multica package, binary,
  container image, or source file is to be vendored, imported, or run by
  MellyCore.
- **Do not copy Multica source code.** Every pattern above is described in
  MellyCore's own terms and mapped to MellyCore's own existing modules and
  files. No Multica code, configuration, or proprietary documentation text
  is reproduced in this document or is to be reproduced in any future
  implementation task derived from it.
- **Do not store high-value secrets as plaintext env values.** This is a
  hard requirement of the secret-broker item (§3.17) and is already
  consistent with `shared_context/SAFETY_CONTRACT.md`. Any future
  implementation that reintroduces plaintext secret storage in an
  environment variable, config file, or committed artifact is a regression,
  not a valid implementation of §3.17.
- **Provider sessions are continuity cache, not canonical memory.** This
  bounds §3.7 exactly as stated there: a resumed provider session may
  accelerate setup but is never authoritative over, and never bypasses,
  Shared Context / Context Gate.
- **Agent completion does not equal task/project completion.** An
  individual agent, runtime, or provider session finishing its turn (per
  §3.1's Agent/Runtime/Task separation) says nothing about whether the
  Task it was working on, or the Issue that Task serves (§3.16), is
  actually done. Completion status must be evaluated at the Task/Issue
  level via the approval gate (§3.15) and the execution event log (§3.10),
  never inferred from agent-turn completion alone.

## 5. Proposed Next Canonical Tasks

Each of the following requires its own explicit Operator authorization
before it may proceed, per `AGENTS.md` and
`shared_context/SAFETY_CONTRACT.md`. None is authorized by this document.

1. **`MELLYCORE-RUNTIME-ARCHITECTURE-RECONCILIATION-REVIEW-001`** —
   independent, fresh-session review of this reconciliation record before
   any of its `ADOPT`/`ADAPT` items are specified further. Read-only.
2. **`MELLYCORE-ISSUE-TASK-EXECUTION-ENTITY-SPEC-001`** — specify the
   `Issue` / `Task` / `Execution` entities (§3.1, §3.16) as an extension of
   the existing Operations Data Contract, fixture/schema-only, following
   `MELLYCORE-OPERATIONS-DATA-CONTRACT-001`'s precedent (spec + JSON Schema
   + example fixtures, no runtime consumer).
3. **`MELLYCORE-SECRET-BROKER-ARCHITECTURE-SPEC-001`** — specify the
   secret-broker component (§3.17) as an extension of the Integration
   Gateway Security Contract, formalizing OmniRoute/OmniRouter's existing
   informal role. Specification-level only; no credential handling code.
4. **`MELLYCORE-CANONICAL-SKILL-INJECTION-SPEC-001`** — specify the
   canonical-skill-to-provider-injection schema (§3.8) and define a
   migration path for the existing `agent_prompts/` content, without
   deleting or restructuring `agent_prompts/` as part of the same task.
5. **`MELLYCORE-TASK-SCOPED-SAFETY-CONTROLS-SPEC-001`** — specify per-task
   workspace (§3.5), task-scoped provider home (§3.6), task-scoped
   execution tokens (§3.14), concurrency limits (§3.12), and
   watchdogs/timeouts (§3.13) together as one coherent Task-execution
   safety envelope, since they are mutually dependent and should not be
   specified in isolation from each other.
6. **`MELLYCORE-MCP-PER-AGENT-RUNTIME-SPEC-001`** — extend the Integration
   Gateway's trust-boundary model to scope MCP/tool availability per
   Agent × Runtime (§3.9).

None of tasks 2-6 authorizes implementation of a local execution daemon
(§3.2, `DEFER`) or live heartbeat/runtime status (§3.11, `DEFER`). Those
remain blocked behind migration trigger #6 in the Model A Production
Deployment Authorization Contract until a separate Model B reconsideration
decision is made.
