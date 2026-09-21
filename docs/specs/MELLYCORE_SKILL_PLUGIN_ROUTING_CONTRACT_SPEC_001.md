# MellyCore Skill and Plugin Routing Contract Spec

**Task ID:** MELLYCORE-SKILL-PLUGIN-ROUTING-CONTRACT-001
**Contract ID:** MELLYCORE_SKILL_PLUGIN_ROUTING_CONTRACT_001
**Version:** 1.0 — first draft.
**Date:** 2026-09-21
**Verification status:** **Unverified.** No independent review has run. This
document is **not accepted** until
`MELLYCORE-SKILL-PLUGIN-ROUTING-CONTRACT-REVIEW-001` completes with a passing
gate decision, in the same sequence used for
`[[MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001]]` and
`[[MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001]]` (spec → review →
remediation → review).
**Status:** Drafted, specification-level only, pending independent review.
**Task ID provenance:** minted by explicit Operator authorization in the
current turn (authority rank 1, `AGENTS.md`), the same precedent recorded for
`MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001` in
`shared_context/TASK_INDEX.md`.
**This status does not authorize:** Skill Registry, Plugin Registry, or Skill
Router implementation; any adapter generator; skill or plugin installation,
loading, activation, or execution; MCP server installation, registration, or
connection; provider integration or provider calls; model calls; telemetry
implementation; adaptive routing; frontend or dashboard work (including any
Skill Library UI); backend work; credential configuration; push, merge, or
deployment. It fixes the architecture a later, separately authorized
specification and implementation must satisfy. It does **not** reorder the
Global Pointer (`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`) and does
**not** unlock any frontend scaffold gate.
**Scope:** Defines the **routing, adaptation, and trust boundary** for
Skills and Plugins inside MellyCore AIOS: the minimum routing-relevant Skill
metadata, the Skill Router's request/decide/record contract and outcome
vocabulary, its relationship to the Agent Runtime's execution envelope and
Model Router, the Claude / Codex / Klaus adapter boundaries, initial skill-pack
taxonomy, an external adoption matrix, trust/provenance mapping, a staged
evaluation contract, and future telemetry and routing-feedback boundaries. It
does **not** specify the full Skill or Plugin declaration/activation schema,
which remain owned by `MELLYCORE-SKILLS-LAYER-SPEC-001` and
`MELLYCORE-PLUGIN-LAYER-SPEC-001` (§3).

---

## 1. Purpose

MellyCore needs one provider-neutral answer to: *given a task, which skills
should be offered to which agent, and under what constraints?* — without that
answer becoming a second orchestrator, a permission grant, or a
provider-owned format.

This contract exists because the accepted architecture already fixes the
surrounding seams but leaves this one open:

- `[[MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001]]` §14 fixes a Skill as a
  *declaration* and §26 item 3 names a future Skill Registry.
- `[[MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001]]` §13 fixes skill
  *projection* into frameworks and defers "full Skill Registry semantics".
- `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` §23 fixes the Model
  Router boundary and §15 the execution envelope, but neither names skill
  selection.
- `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` §7.2 fixes a `Skill`
  entity as an observability projection.

Nothing yet defines **how a skill is selected**. This document fills only
that gap.

## 2. Non-goals

1. The full Skill declaration schema and activation contract
   (`MELLYCORE-SKILLS-LAYER-SPEC-001`).
2. The full Plugin bundling/distribution contract
   (`MELLYCORE-PLUGIN-LAYER-SPEC-001`).
3. The capability-name vocabulary (Package §26 item 2, Capability Contract;
   Integration Gateway §12 remains the resolution owner).
4. MCP server registration (Provider Registry §24).
5. Any change to Runtime §11.1's closed `framework_type` vocabulary.
6. Registering Klaus, Hermes, or Yuzuki as agents.
7. A new "Execution Planner" orchestration layer (rejected, D-03).
8. Implementation of anything.

## 3. Architectural ownership

"The existing owner wins" (`[[../decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001]]`).

| Concern | Canonical owner | This contract's relationship |
| --- | --- | --- |
| Skill declaration (package-side reference) | Agent Package §14 | Consumes unchanged |
| Full Skill declaration + activation schema | `MELLYCORE-SKILLS-LAYER-SPEC-001` (PLANNED) | **Imposes requirements on** (§6); does not specify |
| Plugin bundling and distribution | `MELLYCORE-PLUGIN-LAYER-SPEC-001` (PLANNED) | Consumes; a Plugin is never a routing unit (§4) |
| Package lifecycle (11 states), trust categories (7) | Agent Package §17, §19 | Maps onto; adds one pre-package concept only (§13) |
| Framework projection of skills | Framework Bridge §13 | Consumes; runtime bridges stay there |
| Capability resolution, policy order, approval binding | Integration Gateway §12, §17, §18 | Consumes; **skill selection grants nothing** |
| Risk-tier vocabulary (R0–R5) | Enterprise Provider ADR §13; Integration Gateway | Consumes unchanged; defines no risk vocabulary |
| Model selection | Model Router (Runtime §23) | Skill Router emits model *requirements* only |
| Execution envelope (what one attempt may do) | Agent Runtime §15 | Skill selection becomes an envelope **input** (§8) |
| Skill observability entity | Control Plane §7.2 `Skill` | Projection target, never source of truth |
| Third-party distribution and trust | `MELLYCORE-PACKAGE-ECOSYSTEM-SPEC-001` (PLANNED) | Consumes; §13 and §15 are input to it |
| Agent roles (which tool does what) | `shared_context/MODEL_ROUTING.md` | Consumes as a role map |
| Safety floor | `shared_context/SAFETY_CONTRACT.md`, `AGENTS.md` | Subordinate |

## 4. Terminology — the non-collapsible separation

These concepts are distinct and MUST NOT be merged in any registry, adapter,
UI, or prompt:

| Concept | Definition | Is not |
| --- | --- | --- |
| **Model** | A specific LLM selected by the Model Router | A skill, an agent, a provider |
| **Provider** | The organization/endpoint serving a model or API | A model; a trust grant |
| **Agent** | A runtime identity (`agent_definition_id`) with declared capabilities (Runtime §8–§10) | A skill; a router |
| **Skill** | A declared, reusable, triggerable *workflow specification* with inputs, outputs, and required capabilities (Package §14) | Executable authority; a harmless prompt snippet; a permission |
| **Plugin / Package** | A distribution bundle of skills, commands, hooks, agents, MCP declarations (Package §14) | A routing unit; a trust grant ("bundling grants nothing") |
| **Tool** | A single invokable operation available to an agent at run time | A skill |
| **Connector** | A provider-side integration surface (e.g., a CRM API) | A skill; a capability |
| **MCP server** | A registered server record (Provider Registry §24) | A skill; a capability |
| **Capability** | A named class of behavior; resolves to one bounded operation (Gateway §12) | A tool list |
| **Memory / Context** | Governed Shared Context and memory scopes (Runtime §17–§18) | Skill content |
| **Persistence** | Durable storage of state or ledgers | Memory |
| **Observability** | Read-only telemetry/information architecture (Runtime §34) | Control |
| **Execution environment** | Where an attempt runs (framework, worktree, sandbox) | An agent |
| **Governance / Safety** | Policy, approval, and the safety floor | Anything a skill can declare into existence |

**The Skill Router routes skills only.** A Plugin is resolved to its
constituent skill declarations before routing; the router never selects "a
plugin".

## 5. Decisions (ADR-form)

Each decision below is **proposed** until this document passes review.

### D-01 — MellyCore owns the canonical skill contract; providers are adapters

- **Context:** Anthropic (`SKILL.md` + plugin manifests) and Codex
  (`SKILL.md` + `agents/openai.yaml`) use superficially similar but
  non-identical formats with different defaults (§10–§11). Adopting either as
  canonical makes MellyCore's governance depend on a vendor's schema churn.
- **Decision:** The canonical skill record is MellyCore-owned metadata (§6).
  Claude and Codex artifacts are generated **projections** of it.
- **Alternatives:** (a) Adopt Anthropic `SKILL.md` as canonical — rejected:
  no risk/trust/capability fields; tool pre-approval frontmatter would become
  a de facto permission surface. (b) Adopt the Codex format — rejected:
  `allow_implicit_invocation` defaults to `true`, the wrong default for
  governed skills.
- **Consequences:** + provider replaceability, one governance surface;
  − adapters must be maintained; projection loss must be reported (Bridge §24
  pattern).

### D-02 — The Skill Router follows the Model Router's request / decide / record shape

- **Context:** Runtime §23 already solves routing without a competing
  orchestrator: runtime **requests**, router **decides**, runtime **records and
  enforces**.
- **Decision:** Skill selection uses the identical shape and fail-closed
  semantics (§7). No skill router may execute, activate, or authorize.
- **Alternatives:** A Klaus-owned router — rejected (D-04). A semantic-only
  router — rejected: non-deterministic and unauditable.
- **Consequences:** + one routing mental model; + existing tie/no-match rules
  reused; − one extra artifact per step.

### D-03 — No new Execution Planner; the execution envelope is the plan

- **Context:** The task prompt proposes an Execution Planner composing model,
  agent, skills, tools, context, budget, and approvals.
- **Decision:** Runtime §15's envelope already carries every one of those
  groups except skills. The "plan" is the assembly of an envelope revision
  under Runtime §15.4 sequencing. Skill selection enters as a **reference**
  (§8). `MELLYCORE-EXECUTION-PLAN-CONTRACT-001` is **REJECTED** as a separate
  contract.
- **Alternatives:** A new planner contract — rejected: it duplicates Runtime
  §15 and §15.4 and creates a sixth router.
- **Consequences:** + no new orchestrator; − requires one future additive
  Runtime amendment (§8.3), owned by the Runtime, not by this document.

### D-04 — Klaus is a consumer/operator, never a registry or router owner

- **Context:** "Klaus" does not appear anywhere in this repository at this
  contract's baseline. It is not a registered agent.
- **Decision:** Klaus, once registered through the Agent Package contract,
  consumes routing decisions and canonical metadata (§12). It MUST NOT own the
  global Skill Registry, the Skill Router, permission policy, or model routing.
- **Consequences:** + no duplicate source of truth; − Klaus-specific tasks
  are DEFERRED until Klaus exists as an agent definition.

### D-05 — Skill selection never authorizes anything

- **Decision:** A `SELECTED` outcome is a recommendation input to envelope
  assembly. Tool, provider, capability, memory, and model access remain
  governed solely by Runtime §14 (eleven authorization facts) and Gateway §17.
  Skill text stating "use tool X" is untrusted content (Package §24, Bridge
  §13 rule 3) and is never a grant. A skill MUST NOT silently increase
  permissions.

### D-06 — Adapters are packaging projections, not runtime Framework Bridges

- **Context:** Runtime §11.1 fixes `framework_type` to six members; `codex` is
  not one. Generating a Codex `SKILL.md` is a static packaging act, not a run.
- **Decision:** Claude/Codex skill adapters are **distribution-format
  projections** (static artifacts). They do not create runtime bridges and do
  not require amending §11.1. Whether Codex needs a runtime `framework_type`
  is an open question for the Runtime owner (§19).

## 6. Canonical skill metadata — requirements on the Skill Registry

This section fixes the **minimum fields the router needs**. It is a
requirement imposed on `MELLYCORE-SKILLS-LAYER-SPEC-001`, which owns the full
schema and may add fields. Every field below has a routing or governance
use; fields without one were deliberately dropped.

### 6.1 Tier 1 — routing index (compact; the only tier shown to models)

| Field | Purpose |
| --- | --- |
| `skill_id` | Stable identity (`<pack>.<name>`, lowercase, NFKC-normalized per Package §14.1 rule 5) |
| `name` | Display |
| `version` | Semver; routing decisions bind to an exact version |
| `description` | One-paragraph semantic match surface (≤ 1024 characters) |
| `domain` | One of the pack domains (§16) |
| `triggers[]` | Positive intent phrases / task types |
| `negative_triggers[]` | Explicit exclusions (hard filter, §7.3 step 4) |
| `risk_class` | The **maximum canonical risk tier** of any capability the skill may request, in the existing vocabulary (`[[../decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001]]` §13 R0–R4, extended to R5 by the Integration Gateway). This contract defines **no** risk vocabulary of its own; a skill cannot declare a tier lower than its capabilities imply |
| `trust_category` | Package §19.1 category (§13) |
| `provider_compatibility[]` | Which adapters have a validated projection (§9) |
| `invocation_policy` | `explicit_only` or `implicit_allowed` (default `explicit_only` for canonical tier `R2` and above) |

### 6.2 Tier 2 — governance record (read by the router, never injected into model context)

| Field | Purpose |
| --- | --- |
| `owner` | Accountable maintainer (maps Control Plane `owner`) |
| `purpose` | Maps Control Plane `purpose` |
| `allowed_projects[]` | Maps Control Plane `allowed_projects`; project isolation filter |
| `provenance` | Origin, import source/date, generating process (Package §19.1) |
| `package_revision_id` | Binds the skill to its package lifecycle state (Package §17) |
| `required_capabilities[]` / `optional_capabilities[]` | Capability-class **requests** (Gateway vocabulary); never grants |
| `required_context[]` / `optional_context[]` | Context classes needed; drives `BLOCKED_CONTEXT` |
| `context_cost_estimate` | Tier-3 token size band; drives the budget filter |
| `model_requirements` | Runtime §23.2 fields only (`capability_class`, `context_window_requirement`, `quality_tier`, …) — **never a model name** |
| `approval_requirement` | Whether use requires Operator approval beyond envelope defaults |
| `input_contract_ref` / `output_contract_ref` | Typed I/O; output maps to envelope `output_contract_ref` |
| `stop_conditions[]` | Skill-specific stops; merged into envelope `stop_conditions` |
| `fallback` | `none` (default) or an explicit named fallback skill set — never implicit (§7.6) |
| `validation_level` | Highest passed eval level L0–L7 (§14); maps Control Plane `validation_state` |
| `last_review` | Date and reviewer; staleness input |
| `deprecation` | `deprecated_at`, `replaced_by` |

### 6.3 Tier 3 — body (loaded only after selection)

Full instructions, references, scripts, and assets. **Scripts are data until
a separately authorized run executes them under an authorized envelope.**

### 6.4 Prohibited content

No field, body, example, fixture, adapter output, or eval artifact may
contain credentials, tokens, keys, account identifiers, connection strings,
or `.env` values (Runtime §15.2 applies by analogy). A skill needing a
secret declares a **capability**; the credential stays behind the Gateway.

## 7. Skill Router contract

### 7.1 Boundary

The Agent Runtime (or the authorized step assembling an envelope revision)
**requests**; the Skill Router **decides a selection**; the Runtime **records
it** and enforces nothing new from it — enforcement stays with Runtime §14
and Gateway §17.

### 7.2 Routing request

`intent_text`, `task_type`, `domain` (optional), `project_id`,
`agent_definition_id`, `explicit_skill_ids[]` (optional),
`available_capability_classes[]` (what the envelope could authorize),
`available_context_classes[]`, `adapter_target` (`claude` | `codex` | `klaus`
| `mellycore_runtime`), `context_budget_tokens`, `max_risk_class`,
`tenant_id`, and `run_id` / `step_id` references.

### 7.3 Evaluation order (deterministic filters before ranking)

1. **Explicit invocation.** If `explicit_skill_ids` is set, evaluate only
   those and skip semantic ranking. Explicit invocation does **not** bypass
   steps 2–8.
2. **Lifecycle and trust gate.** Package state must be `published` or
   `installed_reference` and not `deprecated`, `revoked`, or `retired`; the
   trust category must be permitted for the tenant. Otherwise `BLOCKED_TRUST`
   (or `REQUIRES_REVIEW` for Discovery Records and stale reviews).
3. **Project and agent scope.** `project_id ∈ allowed_projects`, and the agent
   is permitted to use the skill. Otherwise excluded.
4. **Negative triggers.** Any match excludes, regardless of other scores.
5. **Risk ceiling.** `risk_class ≤ max_risk_class`. Otherwise
   `BLOCKED_PERMISSION`.
6. **Capability satisfiability.** `required_capabilities ⊆
   available_capability_classes`. Otherwise `BLOCKED_CAPABILITY`.
7. **Context satisfiability and budget.** `required_context ⊆
   available_context_classes` and `context_cost_estimate ≤
   context_budget_tokens`. Otherwise `BLOCKED_CONTEXT`.
8. **Adapter compatibility.** `adapter_target ∈ provider_compatibility`.
   Otherwise `INCOMPATIBLE_PROVIDER`.
9. **Implicit-invocation gate.** Non-explicit requests consider only
   `implicit_allowed` skills.
10. **Ranking (only now).** Trigger match, then semantic similarity over
    Tier-1 metadata, then (future, §18) historical evidence — each score
    recorded.
11. **Tie-break.** A declared deterministic tie-breaker (e.g., higher
    `validation_level`, then lower `context_cost_estimate`, then `skill_id`
    lexical order). Unresolved → `MULTIPLE_CANDIDATES`.

### 7.4 Outcomes

| Outcome | Meaning | Runtime effect (by analogy to Runtime §23.5–§23.6) |
| --- | --- | --- |
| `SELECTED` | Exactly one skill (or an explicitly composed set, §7.7) chosen | Reference recorded into the next envelope revision |
| `MULTIPLE_CANDIDATES` | Tie unresolved by the declared tie-breaker | Operator chooses **from the recorded set only**; never random |
| `NO_MATCH` | Nothing passes filters and the ranking threshold | Proceed without a skill, or stop — never a silent "best effort" skill |
| `BLOCKED_PERMISSION` | Risk class exceeds the ceiling or required approval absent | Blocked; approval path required |
| `BLOCKED_TRUST` | Lifecycle or trust state not routable | Blocked |
| `BLOCKED_CAPABILITY` | Required capability not available | Blocked |
| `BLOCKED_CONTEXT` | Required context missing or over budget | Blocked |
| `INCOMPATIBLE_PROVIDER` | No validated projection for the target | Blocked for that target |
| `REQUIRES_REVIEW` | Discovery Record only, review stale, or flagged | Not routable until reviewed |

### 7.5 Routing artifacts

`skill_routing_request`, `skill_routing_decision` (selected
`skill_id@version`, decision digest, timestamp), and
`skill_routing_explanation` (each rejected candidate with the filter step
that excluded it, scores, and the tie-breaker applied). Artifacts carry
references, never skill bodies or secrets.

### 7.6 Fallback prohibition

A failing skill MUST NOT be silently replaced by another skill. Substitution
requires an explicit `fallback` set declared in the skill record **and** is
recorded as a new routing decision. An undeclared substitution is a hidden
repair loop and is prohibited (cf. Runtime §23.4).

### 7.7 Composition

A task may select multiple skills (e.g., Klaus use case A, §12.3). Each
member is routed independently through §7.3; the composed set is the union of
`SELECTED` members only, and the resulting capability request is the
**intersection** of what the set requires and what is authorized (Bridge §9
rule 2 pattern).

## 8. Relationship to the execution envelope and other routers

### 8.1 One plan, several advisors

```
USER INTENT → task classification
      │
      ▼
Envelope assembly (Agent Runtime §15, §15.4)   ← the only "planner"
      ├── Skill Router (this doc)     → skill routing decision ref (proposed §8.3)
      ├── Model Router (§23)          → routing request / decision refs
      ├── Context access (§17)        → context_snapshot_refs, access scope
      ├── Tool/Provider governance    → tool_/provider_permission_refs (Gateway)
      ├── Cost (§24)                  → cost_budget_ref, reserved_budget
      └── Approvals (§14 fact 11, §30) → approval_refs
      ▼
Authorized envelope → execution → validation/review
      → ledger + cost (§24–§25) → human approval where required
```

Every advisor returns a **decision reference**; none executes, and none calls
another. Ordering: skill selection runs **before** model routing, because a
selected skill contributes `model_requirements` to the model routing request;
the Model Router still decides the model.

### 8.2 Agent routing

Agent choice is an Operator/task-prompt decision today
(`shared_context/MODEL_ROUTING.md` role map) and, in future, a handoff under
Runtime §20. The Skill Router takes `agent_definition_id` as an **input**; it
never chooses the agent.

### 8.3 Proposed future Runtime amendment (not applied here)

Runtime §15.1 has no skill field. A future additive amendment, owned by the
Agent Runtime spec and subject to its own review, should add to the Intent
group `skill_routing_decision_refs[]` (references only; bodies resolved at the
point of use). Until that amendment exists, no implementation may carry skill
selections in an envelope.

## 9. Adapter model (ports and adapters, targeted)

```
Canonical skill record (Tier 1–3)            ← domain (MellyCore-owned)
      │
Skill Registry port  /  Skill Router port    ← contracts (§6, §7)
      │
 ┌──────────────┬───────────────┬──────────────┬─────────────────────────┐
Claude adapter   Codex adapter   Klaus adapter   MellyCore runtime (Bridge §13)
(static package) (static package) (consumer)     (run-time projection)
```

Dependency points inward: adapters depend on the canonical record; the
canonical record never contains adapter-only fields. Every adapter:

1. MUST report projection loss (fields it cannot express) rather than drop
   them silently (Bridge §24 pattern);
2. MUST NOT widen invocation, tool, or permission scope beyond the canonical
   record;
3. MUST be regenerable deterministically from the canonical record, and its
   output MUST NOT be hand-edited;
4. MUST NOT embed secrets (§6.4).

## 10. Claude adapter

| Canonical element | Claude projection | Notes |
| --- | --- | --- |
| Tier 1 `name`, `description` | `SKILL.md` frontmatter `name`, `description` | Description is Claude's selection surface; triggers and negative triggers are rendered into it |
| Tier 3 body | `SKILL.md` body + supporting files | Progressive disclosure preserved |
| Pack (§16) | Plugin package (`.claude-plugin/plugin.json`) with `skills/` | Plugin = distribution only |
| Explicit-invocation entry | Slash command | Must pass Package §14.1 collision rules |
| Agent role binding | Plugin `agents/` definition | References an `agent_definition_id`; defines no new agent |
| Lifecycle automation | Hook | Only via the future Hook Registry; side-effecting hooks need approval (Package §14) |
| MCP-backed capability | MCP reference in plugin configuration | Reference to a Provider Registry §24 record only; never a new server |
| Connector requirement | Documented prerequisite | The adapter never configures a connector |

**Claude-only metadata** (adapter profile, not canonical): plugin marketplace
name and version, command argument hints, plugin author fields, model-hint
fields.

**Mandatory restriction:** tool pre-approval frontmatter (for example
`allowed-tools`) is a permission-widening surface. The adapter MUST omit it by
default and MAY emit it only as a strict subset already authorized by the
envelope.

## 11. Codex adapter

Verified against the Codex source (Context7, library `/openai/codex`,
retrieved 2026-09-21): Codex discovers `SKILL.md` directories under user
roots (`$CODEX_HOME/skills`, `~/.agents/skills`), project roots
(`.codex/skills`), admin/system roots, plugin skill roots, and repository
`.agents/skills` directories between the project root and the current
directory. A skill's `agents/openai.yaml` carries
`policy.allow_implicit_invocation`, which **defaults to `true`**; explicit
invocation uses `$skill`.

| Canonical element | Codex projection | Notes |
| --- | --- | --- |
| Tier 1 | `SKILL.md` frontmatter | Same description discipline as Claude |
| Tier 3 body | `SKILL.md` + `references/` | Progressive disclosure |
| Scripts | `scripts/` | Data until an authorized run executes them |
| Assets | `assets/` | No secrets; no binaries of unknown provenance |
| `invocation_policy` | `agents/openai.yaml` `policy.allow_implicit_invocation` | The adapter MUST emit `false` for `explicit_only`; it never relies on the `true` default |
| Placement | repository `.agents/skills/` (repo scope) | User/admin placement is an Operator act, never an adapter default |

**Codex-only metadata:** `agents/openai.yaml` interface/display fields and
scope hints.

**Discovery-root risk:** because Codex scans multiple roots, a same-named
skill in a user or plugin root can shadow a repository skill. Collision
detection (Package §14.1 rules 1–5, applied to skill identifiers) is a
required L0 check for Codex projections (§14).

## 12. Klaus adapter and use cases

### 12.1 Status

Klaus is **not registered** in MellyCore canonical state. Everything below is
the contract a future Klaus agent package must satisfy.

### 12.2 What Klaus consumes

Canonical Tier 1 metadata; Skill Router decisions (never its own ranking);
permission-policy outcomes; capability and context requirements; Model Router
decisions (never a model it picked itself); and approval requirements. Klaus
MAY hold a **read-only cached copy** of Tier 1 metadata, invalidated by
registry version; it MUST NOT hold a writable registry.

### 12.3 Use-case coverage check

| Use case | Skill chain (pack) | Highest risk | Gate |
| --- | --- | --- | --- |
| A. Find freelance opportunities | research (research) → lead qualification, opportunity scoring (klaus-opportunity-engine) → proposal generation (klaus-freelance) → review (safety) → approval | `R2` (draft/proposal); `R3`+ if anything is sent | Sending is an explicit-permission action; never autonomous |
| B. Review a repo and propose the next task | codebase onboarding (engineering) → architecture, tech-debt, system-design (architecture) → roadmap, task generation (product) | `R2` (proposal) | Output is a proposal; task minting stays Operator-authorized |
| C. Prepare a client proposal | client research (research) → feasibility, scope (engineering/product) → pricing support, drafting (klaus-freelance) → review | `R2` | Pricing is support, never a binding quote; delivery is an explicit-permission action |
| D. Continue MellyCore | context retrieval, canonical task lookup (context) → architecture guardrails (safety) → implementation handoff (engineering) → validation → final report | `R2` | Follows `AGENTS.md` preflight; the next task comes from `RUN_QUEUE.md`, never invented; repository mutation is governed by the envelope and `AGENTS.md`, not by the skill |

All four are expressible with §7 composition; none requires Klaus-owned
routing. Use case D is also compatible with a bounded
planner → implementer → validator → reviewer → remediation → human-approval
loop, provided each stage is a separate envelope and remediation is bounded
by the envelope's `max_steps` / retry policy (Runtime §28) rather than by a
skill.

## 13. Trust, provenance, and lifecycle mapping

No parallel lifecycle is introduced. The requested states map as follows:

| Requested state | Canonical representation |
| --- | --- |
| `DISCOVERED` | **Discovery Record** (net-new, pre-package): an observed external listing (marketplace, repository, plugin catalog). Zero trust, not a package, **never routable** (`REQUIRES_REVIEW`) |
| `REVIEWED` | Package §17 `validated` |
| `APPROVED` | Package §17 `approved` |
| `REGISTERED` | Package §17 `published` / `installed_reference` |
| `ENABLED` | Not a lifecycle state: the activation chain (Package §10 / Bridge §9) holding for a tenant and environment |
| `DISABLED` | Activation withdrawn; lifecycle unchanged |
| `QUARANTINED` | Package §19.1 category 7 (revoked/blocked) with reason `quarantine_pending_review`; immediate |
| `DEPRECATED` | Package §17 `deprecated` |

Trust rules:

1. Marketplace presence confers no trust.
2. Every external skill or plugin carries provenance (source, retrieval date,
   upstream version/commit, license) before it can leave `DISCOVERED`.
3. Default trust is `unsigned_or_unverified` (Package §19.2); no signing is
   claimed.
4. An `ADAPT` decision (§15) produces a **generated** package whose
   provenance records the upstream source; it becomes first-party only after
   MellyCore review.
5. A skill never inherits trust from the plugin that bundles it.

## 14. Skill evaluation contract

| Level | Checks | Evidence |
| --- | --- | --- |
| L0 | Schema/metadata valid; ID normalized; collision-free across adapter roots; no secret patterns | Validator output |
| L1 | Trigger and negative-trigger fixtures produce the expected SELECTED / excluded results | Fixture table |
| L2 | Deterministic workflow checks: required sections, stop conditions, output-contract conformance on fixed inputs | Fixture runs |
| L3 | Declared capabilities resolvable (Gateway §12); no undeclared tool use in the body | Static analysis |
| L4 | Permission/safety: no permission widening; risk class justified; no autonomous side effects | Review record |
| L5 | Agent integration: routed and consumed correctly inside an envelope | Run ledger (future) |
| L6 | Cross-provider: Claude and Codex projections behave equivalently on L1/L2 fixtures | Paired runs (future) |
| L7 | Acceptance/regression: Operator-accepted outcomes; no regression versus the prior version | Acceptance record |

A parseable `SKILL.md` is at most L0. Proposed routing-eligibility minimums
(canonical tiers): `R0`/`R1` ≥ L2; `R2` ≥ L4; `R3` and above ≥ L4 **plus** the
approval the canonical tier already requires, per use.

## 15. External adoption matrix

Decisions: **ADOPT** (use the pattern as-is), **ADAPT** (re-author under the
canonical contract), **REFERENCE_ONLY**, **DEFER**, **REJECT**. No row
authorizes installation, vendoring, or execution of any third-party code.

| Source | Decision | Useful pattern | Risk / trust boundary | Reuse | Do not reuse | Future use |
| --- | --- | --- | --- | --- | --- | --- |
| Anthropic Engineering | ADAPT | architecture/ADR, system-design, code-review, tech-debt, testing-strategy workflows | Low; external first-party vendor | Workflow structure and output formats | `deploy-checklist`, `incident-response` production workflows | `mellycore-engineering`, `mellycore-architecture` |
| Anthropic Product Management | ADAPT | synthesize-research, roadmap-update, write-spec | Low | Synthesis and roadmap structure | Project-tracker connector assumptions | `mellycore-product`; use case B |
| Anthropic Productivity | REFERENCE_ONLY | task and memory management | Medium: memory competes with Shared Context / Runtime §18 | Ideas only | Its memory model | — |
| Anthropic Operations | ADAPT | runbook, process-doc, risk-assessment, change-request | Low | Runbook and risk structure | Change-execution steps | `mellycore-operations` |
| Anthropic Small Business | REFERENCE_ONLY | router skill, lead finding, proposal building | R2–R3 connectors (CRM, email, payments) | Proposal and lead-qualification structure | Anything that sends, pays, or writes externally | `klaus-freelance` input |
| Anthropic Design | DEFER | design critique, accessibility review | Low | — | — | When the cockpit lane needs it |
| Anthropic Sales | REFERENCE_ONLY | lead triage, account research, outreach drafting | R3 outreach | Qualification rubrics | Outreach sending, CRM writes | `klaus-opportunity-engine` input |
| Anthropic Marketing | DEFER | campaign and content workflows | R3 publishing | — | Publishing | — |
| Anthropic Plugin Management | REFERENCE_ONLY | plugin creation/customization structure | Mutates installed plugins | Manifest structure as Claude-adapter reference | `create-cowork-plugin`, `cowork-plugin-customizer` (not invoked) | Claude adapter design |
| ECC architecture skills (`architecture-decision-records`, `agent-architecture-audit`, `hexagonal-architecture`, `autonomous-loops`, `agentic-os`, `backend-patterns`) | REFERENCE_ONLY (ADR format and 12-layer audit are ADAPT candidates) | ADR format, layered agent audit, ports/adapters | Third-party; ECC is never a canonical owner | Lenses and checklists | ECC's `docs/adr/` layout (this repo uses `docs/decisions/`) | `mellycore-architecture`, `mellycore-safety` |
| Exa | DEFER | search as a capability | External API key; R2 | Model as a capability behind the Gateway | Direct key use from a skill | Research pack, via Provider Registry |
| CRM / lead plugins (HubSpot Sales, monday CRM, Lusha, Leadfeeder) | REFERENCE_ONLY | vertical packaging: skills + one connector | PII, R3 writes, personal-data compilation | Connector-boundary pattern | Prospecting/enrichment execution | `klaus-opportunity-engine` design input |
| ActiveCampaign | REJECT (for now) | — | Email-marketing writes (R3) | — | All | Revisit only with a Model B decision (`AGENTS.md` trigger) |
| Chronograph-style vertical packs | REFERENCE_ONLY | domain pack = agents + skills + one scoped connector | Financial data; MellyTrade separation | The "vertical pack" packaging shape | Any financial or trading execution | Pack taxonomy (§16) |

## 16. Initial skill packs (not implemented)

| Pack | Scope | Owner | Max risk |
| --- | --- | --- | --- |
| `mellycore-engineering` | onboarding, code review, testing strategy, implementation handoff | MellyCore | R2 |
| `mellycore-architecture` | ADR, system design, audit lenses | MellyCore | R2 |
| `mellycore-product` | synthesis, spec, roadmap, task generation | MellyCore | R2 |
| `mellycore-design` | critique, accessibility review | MellyCore | R2 — **DEFER** |
| `mellycore-research` | source research, provenance capture | MellyCore | R1 |
| `mellycore-operations` | runbook, risk, status report | MellyCore | R2 |
| `mellycore-safety` | guardrail checks, diff audit, secret scan | MellyCore | R1 |
| `mellycore-context` | context retrieval, canonical task lookup | MellyCore | R1 |
| `klaus-core` | Klaus-side composition of the packs above | Klaus package (future) | inherits |
| `klaus-freelance` | proposal drafting, scope, pricing support | Klaus package (future) | R2 (R3+ gated) |
| `klaus-opportunity-engine` | lead qualification, opportunity scoring | Klaus package (future) | R1 |

"Max risk" uses the canonical tier vocabulary (§6.1) and is a ceiling for
skills admitted to the pack, not a grant.

The proposed `business` canonical domain is **not** adopted as a MellyCore
pack: business and freelance skills belong to Klaus packs, keeping MellyCore
core packs domain-neutral.

### 16.1 Library layout decision

The proposed `mellycore-skills/{canonical,adapters,registry,evals,references}`
shape is **AMENDED**: canonical records, adapter profiles, the registry
index, and evals are *logical* partitions whose physical location is decided
by `MELLYCORE-SKILLS-LAYER-SPEC-001`. No folder is created by this task. The
existing top-level `skills/` directory (one skill,
`docs-portfolio-asset-sync`) is the natural candidate root; generated Claude
and Codex outputs MUST live in a separate, regenerable location.

## 17. Context efficiency (progressive disclosure)

1. Models receive **Tier 1 only**, and only for candidates that survive §7.3
   steps 1–9.
2. Tier 2 is read by the router and never injected into model context.
3. Tier 3 loads only for `SELECTED` skills, and only the reference files the
   current step needs.
4. The full library is never loaded into any context.
5. The loaded size is recorded per load for §18.

## 18. Telemetry and routing feedback (future, not implemented)

Per skill invocation, a future ledger extension (owned by Runtime §24–§25)
should record: `skill_id@version`, `agent_definition_id`, model and provider
(from the Model Router decision), `run_id`/`step_id`, input and output
tokens, Tier-3 bytes loaded, latency, tool-call count, outcome, validator
result, review result, retries, cost, and **cost per accepted task** (the
cost of all attempts divided by Operator-accepted outcomes).

Routing feedback: historical success rate, model + skill acceptance rate,
retry rate, validator failure rate, context consumption, and cost per
accepted task MAY later become a **ranking signal at §7.3 step 10 only** —
never a filter override, never self-modifying trust, and never automatic
promotion across lifecycle states. Adaptive learning is out of scope and
requires its own contract.

## 19. Open questions

1. Does Codex need a Runtime `framework_type` member, or does it remain a
   packaging target only? Owner: Agent Runtime spec.
2. Can a single skill be quarantined without revoking its package? Owner:
   `MELLYCORE-SKILLS-LAYER-SPEC-001`.
3. Where does the physical skill library live (§16.1)? Owner: Skills Layer.
4. Klaus identity — which agent package, framework type, and owner? Owner:
   Operator, via the Agent Package contract.
5. Should `explicit_only` be the default for every risk class? Proposed: yes
   for `R2` and above; open for `R0`/`R1`.
6. The Runtime §15 amendment (§8.3) needs its own task identifier.
7. Canonical risk tiers are defined for *provider capabilities*. How a
   skill's purely local effects (for example repository edits) map onto that
   ladder, if at all, needs an owner decision; this contract only takes the
   maximum over declared capabilities. Owner: Capability Contract (Package
   §26 item 2).

## 20. Acceptance criteria

1. Skill ≠ Plugin ≠ Agent ≠ Tool ≠ MCP ≠ Model is preserved (§4).
2. MellyCore owns the canonical record; Claude and Codex are projections
   (D-01, D-06).
3. Klaus is a consumer only (D-04, §12).
4. The Skill Router neither executes nor authorizes (D-05, §7.1).
5. No new orchestrator is introduced (D-03, §8).
6. Permission ownership stays with Runtime §14 and Gateway §17.
7. Progressive disclosure is preserved (§17).
8. Third-party provenance and trust are modeled (§13, §15).
9. No duplicate canonical owner: every concern in §3 has exactly one owner.
10. No gate bypass: the Global Pointer and frontend gates are unchanged.

## 21. References

- `AGENTS.md`, `shared_context/SAFETY_CONTRACT.md`, `shared_context/MODEL_ROUTING.md`
- `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` §11, §14, §15, §20, §23, §24, §28
- `[[MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001]]` §10, §14, §17, §19, §24, §26
- `[[MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001]]` §9, §13, §24
- `[[MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001]]` §12, §17
- `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` §7.2
- `[[MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001]]` §24
- `[[../decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001]]`
- `[[../decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001]]` §13
- Codex skill discovery and `agents/openai.yaml` policy: `openai/codex` source
  via Context7 (retrieved 2026-09-21); external reference only.

## 22. Amendment and supersession

Amendments follow the spec → review → remediation → review sequence. This
document is superseded in part by `MELLYCORE-SKILLS-LAYER-SPEC-001` for any
field-level schema that spec fixes, provided that spec preserves §4, §5, and
§7's outcome vocabulary or explicitly supersedes them after review.
