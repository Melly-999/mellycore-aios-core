# Project History

Canonical, chronological ledger of MellyCore AIOS milestones. This is a summary
index only — durable per-task evidence remains in `docs/tasks/`, `docs/research/`,
`docs/decisions/`, and Git history, none of which this file duplicates or
supersedes. Where this file and a durable report disagree, the durable report
and Git history win.

Naming a milestone here does not, by itself, claim implementation. Each entry
states its actual status (`SPECIFIED`, `IMPLEMENTED`, `ACCEPTED`, `MERGED`,
`RETIRED`) as recorded in the linked evidence.

## Genesis

- **2026-07-06** — Project scaffold bootstrapped. `AGENTS.md`, `CLAUDE.md`,
  `PROJECT_RULES.md`, and the `shared_context/` contract set created. MellyCore
  AIOS established as separate from MellyTrade, docs-first, no runtime app code
  until explicitly authorized.
- **2026-07-06** — MellyCore Design System and Homepage specification added.

## Foundational Phase

- Static homepage and Living Context Graph prototype shipped; historical
  evidence under `docs/tasks/` and `docs/showcase/`.
- **Operational Trust / Loop Operations** — closed as report-only: immutable
  run evidence, no scheduler, no production-enabled loop. Architecture under
  `docs/architecture/`.
- **One Brain / Context Gate I1–I4** — implemented: guarded admission,
  canonical write-once records, content-free index, computed audit, read-only
  dashboard surface. Canonical evidence under `shared_context/context_provenance/`.
- **Live Cockpit V2 / `v0.2.0`** — historical release; superseded legacy
  dashboard prototype, not the complete Observatory.
- **Holographic UI specification / PR #4** — accepted as documentation only.
  Source Arena hero contract preserved; 3D/WebGL treatment not implemented at
  this point.
- **Positioning refresh** — integrated into canonical `main`; durable report
  `docs/tasks/MELLYCORE-POSITIONING-REFRESH-001.md`.

## AI Operations Intelligence and Data Contract

- **AI Operations Intelligence specification** (`MELLYCORE-AI-OPERATIONS-INTELLIGENCE-001`)
  — integrated into canonical `main` via PR #7. Logical contracts and
  truth/safety boundaries only; modules remain `SPECIFIED`, no runtime
  adapters or approval execution claimed.
- **Operations Data Contract** (`MELLYCORE-OPERATIONS-DATA-CONTRACT-001`) —
  integrated into canonical `main` via PR #13 (merge commit
  `e0db28f06613d29028df96a2d651b6dfdf2f2aa8`). Fourteen dashboard-facing
  fixture entities and their `shared_context/operations/` schemas landed as
  documentation/schema/fixture scope, not runtime implementation. Branch
  reconciliation and AI-Estate/Skill-Gap/Memory-Freshness folding recorded in
  `docs/tasks/MELLYCORE-OPERATIONS-DATA-CONTRACT-POST-MERGE-STATE-SYNC-001.md`.

## Source Arena Renderer Track

- **Source Arena Hybrid renderer ADR** — status `ACCEPTED_CANONICAL_MAIN`
  (decision/specification level only); merged into canonical `main` via PR #8,
  merge commit `f93be7018a1da3bba50eb66346b1f9e627a46dd2`, 2026-07-20. Full
  review chain (review 001 `NEEDS_FIXES` → remediation 001 → review 002
  `NEEDS_FIXES` → remediation 002 → review 003 `PASS` → operator acceptance →
  acceptance review 001 `NEEDS_FIXES` → acceptance remediation 001 →
  acceptance review 002 `PASS` → PR #8 merged) recorded under `docs/tasks/`.
  No Three.js implementation, dependency vendoring, or deployment exists at
  this milestone.
- **Post-merge state sync / P2 remediation chain** — PR #11 merged into
  canonical `main` via merge commit `cad4e07f73f80c5794f9af2897fc10d922637ab3`.
- **NASA Images runtime retirement**
  (`MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001`) — executable runtime
  retired from `site/dashboard.html` / `site/js/dashboard.js`; merged via PR
  #15 (merge commit `e0cbc332ff90f8787d981c9d86be717633f22d4d`), replaced with a
  local deterministic Source Archive.
- **Static CSS/DOM renderer slice** — canonical on `main` via PR #17 (merge
  commit `537a84c8`): source core, orbital nodes, orbit ring, command
  inspector. Replaced the prior social-feed primary UX. Full 3D/WebGL renderer
  and the ADR's CSS-complete fallback remain **not complete**.

## Enterprise Provider and Cloudflare Track

- Enterprise Provider Integration architectural research recorded — not
  implemented; see `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md`
  and `shared_context/PROJECT_STATE.md`'s corresponding section.
- **Cloudflare API Shield read-only adapter 001** — local implementation
  complete → review 001 `FAIL_REMEDIATION_REQUIRED` → remediation 001 →
  review 002 `PASS_WITH_NON_BLOCKING_FINDINGS`. Provider-foundation checkpoint
  complete; not live-provider readiness. `P2-03`, `P2-04`, `P3-01` carried
  forward as constraints on later provider and Agent Runtime work.

## Deploy Path and Production Authorization

- **Option B Deploy Path — Static AIOS Showcase + OpenRouter Observatory** —
  historical deploy path, completed; see `shared_context/RUN_QUEUE.md`'s
  "Historical Option B Deploy Path" section.
- **Vercel Static Root** — accepted, verified, published, state-synced, merged.
- **Production Deployment Authorization — Model A Contract** (Operator
  decision, 2026-07-27, temporary, static-phase-only) — recorded in
  `shared_context/PROJECT_STATE.md`. Nine canonical, blocking migration
  triggers require Model B reconsideration before crossing.
- **OpenAI Batch Controlled Activation** — Stage B merged; Stage C
  unauthorized; final canonical state reconciliation gate is the current
  global higher-priority pointer in `shared_context/RUN_QUEUE.md`.

## Agent Runtime Product Track

1. `MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001` — architecture specified
   across 43 sections and 6 frameworks; complete as one local documentation
   commit, not pushed. Nothing implemented, connected, or executed.
2. `MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-001` — gate
   `FAIL_REMEDIATION_REQUIRED` (P0 0 / P1 4 / P2 5 / P3 5).
3. `MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REMEDIATION-001` — all fourteen
   findings remediated; two owner documents (Control Plane, AI Operations
   Intelligence) amended additively; remediation claims unverified pending
   review.
4. `MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-002` — gate
   `PASS_WITH_NON_BLOCKING_FINDINGS` (P0 0 / P1 0 / P2 0 / P3 1 new,
   `NEW-P3-01`). Architecture accepted as canonical foundation for this track.
5. `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001` — two sub-phases complete
   under one task ID. **Phase 1** (documentation synchronization): recorded
   the Developer Platform and Agent Package Ecosystem planning direction
   across `shared_context/ROADMAP.md`, `RUN_QUEUE.md`, `PROJECT_STATE.md`,
   this file, and `TASK_INDEX.md`. **Phase 2** (the specification itself,
   **current active task**; see `shared_context/AGENT_HANDOFF.md`'s Latest
   Update): drafted the canonical Agent Package Contract —
   `docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md` (29 sections,
   durable report `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001.md`)
   — defining package identity, boundary, layout, manifest relationships, a
   five-state capability separation, a permission/approval model, a
   dependency model, six-framework compatibility projection,
   Skill/Command/Hook/Plugin/MCP asset boundaries, Shared Context and Agent
   Runtime interaction, an eleven-state package lifecycle, validation,
   trust and provenance, observability, error taxonomy, Batch Orchestration
   eligibility, security considerations, and twelve named follow-up
   contracts. **Unverified; not accepted.** Complete as one local
   documentation commit on
   `docs/mellycore-agent-package-contract-spec-001`, not pushed. Nothing
   implemented; no Agent Package Store, Package Registry, Package
   Validator, loader, registry, or signing mechanism exists. Full detail:
   `shared_context/PROJECT_STATE.md`'s "Agent Package Contract Spec 001 —
   Specification Drafted" section.
6. `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-001` — **current active
   task** (see `shared_context/AGENT_HANDOFF.md`'s Latest Update).
   Independent, read-only review of item 5's specification. **Gate:
   `FAIL_REMEDIATION_REQUIRED`** (P0 0 / P1 1 / P2 3 / P3 3). All 24
   self-reported metrics recount correctly; 12 of 13 ownership rows
   independently confirm. Blocking finding `P1-01`: the package-lifecycle
   and trust-state sections claim a projection onto Control Plane's six
   status dimensions without the row-complete mapping table or owner
   amendment the `run_state` precedent required and received; four
   lifecycle states and five trust-state categories have no legal
   projection target. The reviewed specification was not edited; every
   canonical cross-check source remained byte-identical after the review
   commit. Complete as one local documentation commit on
   `docs/mellycore-agent-package-contract-spec-review-001`, not pushed.
   Full detail:
   `docs/research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_001.md`.
7. `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001` — `COMPLETE`.
   Remediated all seven findings of item 6, advancing the specification to
   **version 1.1**. `P1-01` closed by removing the unsupported Control
   Plane projection claim (package lifecycle/trust state restated as
   Agent Package domain concepts under Control Plane §7.1's typed-field
   allowance; no Control Plane amendment made or needed). `P2-01`–`P2-03`
   closed with targeted corrections (non-normative Provider Registry
   citations; a deterministic `DEPENDENCY_UNRESOLVED` evaluation boundary;
   a new normative command-namespace-collision subsection with a
   dedicated error class). `P3-01`–`P3-03` closed editorially.
   **Unverified; gate not re-opened; specification remains not accepted**
   pending `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-002`. All twelve
   canonical cross-check sources, including both Review 001 artifacts,
   remained byte-identical after this commit. Complete as one local
   documentation commit on
   `docs/mellycore-agent-package-contract-spec-remediation-001`, not
   pushed. Full detail:
   `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001.md`.
8. `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-002` — `ACCEPTED`
   (documentation only), 2026-08-03. Independent, read-only re-review of the
   remediated specification (version 1.1, commit `ad1d1fc`). Gate
   **`PASS_WITH_NON_BLOCKING_FINDINGS`** — P0 0 / P1 0 / P2 3 / P3 4. All
   seven Review 001 findings independently `CLOSED`, the single P1 closed in
   full: every Control Plane status-dimension reference in the specification
   was audited and each is an explicit denial of projection or a
   non-collision statement, with zero surviving projection claims and no
   invented enum member. Every canonical owner document was verified
   byte-identical to the baseline Review 001 recorded before the remediation
   ran. Seven new non-blocking findings recorded and none discarded,
   including the §17.3 rule 1 Provider Registry analogy — assessed
   independently and found technically accurate and **not** an ownership
   overreach. `MELLYCORE_AGENT_PACKAGE_CONTRACT_001` v1.1 is **accepted as a
   documentation contract only**, under those seven constraints; **no
   implementation of any kind exists** — no store, registry, validator,
   loader, package, installation, execution, runtime, provider connection,
   credential, or deployment. Review 001 remains historically failed; the
   Agent Runtime Review 002 gate is not reopened. The reviewed specification
   was not edited. Complete as one local documentation commit on
   `docs/mellycore-agent-package-contract-spec-review-002`, not pushed. Full
   detail:
   `docs/research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_002.md`,
   `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-002.md`.
9. `MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001` — `SPECIFIED`
   (documentation only, **unverified**), 2026-08-03. Defines the
   provider-agnostic **Framework Bridge Contract**
   (`docs/specs/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001.md`, version 1.0,
   39 sections). The task identifier was **minted by explicit Operator
   authorization** after the preceding run found no identifier anywhere in the
   repository and stopped before mutation rather than invent one. Fixes the
   one-directional projection chain — MellyCore canonical contract →
   framework-neutral bridge semantics → framework-specific adapter projection
   — prohibits the inverse, and bars any framework from redefining agent or
   package identity, capability states, permissions, approvals, trust,
   provenance, lifecycle, run state, Shared Context ownership, observability
   ownership, error taxonomy, or Operator authority. Adds a sixth
   **framework-supported** capability state that never implies MellyCore
   authorization; keeps thirteen permission categories deny-by-default against
   framework defaults; routes every framework model request through the Model
   Router; fails closed on safety-relevant projection loss; and defines six
   bounded per-framework profiles across the canonical closed set, with no
   seventh identifier added. All three open Agent Package P2 findings were
   **contained, not resolved**, and recorded as deferred dependencies; **no
   owner document was edited**. Agent Runtime §11.3/§35 per-framework cells
   remain **unvalidated planning positions**, with the validation obligation
   assigned to each future per-framework adapter specification. **Nothing
   implemented, integrated, or installed** — no bridge, adapter, SDK,
   framework session, runtime, provider connection, credential, or deployment.
   Complete as one local documentation commit on
   `docs/mellycore-framework-bridge-contract-spec-001`, not pushed. Full
   detail: `docs/tasks/MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001.md`.
10. `MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-REVIEW-001` — `ACCEPTED`
   (documentation only), 2026-08-03. Independent, read-only architecture,
   ownership, interoperability, and safety review of the Framework Bridge
   Contract (version 1.0, commit `278eae0`). Gate
   **`PASS_WITH_NON_BLOCKING_FINDINGS`** — P0 0 / P1 0 / P2 4 / P3 4. Owner
   lists were reconstructed mechanically from Agent Runtime §11.1, §11.2, §16,
   §33 and Agent Package §10.1, then tested against the reviewed text rather
   than accepted from its claims; every canonical owner document was verified
   byte-identical before and after. Verified correct: the exact closed
   six-member framework set with no alias for `mellycore_custom`; all six
   Runtime §11.2 bridge rules preserved; canonical-versus-projected direction;
   thirteen deny-by-default permission categories with flattening prohibited;
   proposal-only Shared Context with mandatory return-path re-validation; five
   separated memory scopes; non-bypassable routing; fail-closed projection loss
   with ambiguity resolving to loss; validation that does not authorize
   execution; no new Control Plane dimension; and six conceptual framework
   profiles with zero overclaim. The framework-validation obligation of Runtime
   §11.3/§35 was judged **honest and owner-correct as a documentation-only
   deferral** — not a P1 failure — and **empirical framework validation remains
   `NOT_PERFORMED`**. Eight new non-blocking findings were recorded and none
   discarded, the sharpest being that four of Runtime §16's nine bridge
   operations are never named and `normalize_result` has no counterpart rule.
   All three open Agent Package P2 findings remain **contained and open**, and
   the Agent Package Contract was not edited. The specification is **accepted
   as a documentation contract only**; **no implementation of any kind
   exists** — no bridge, adapter, SDK, framework session, runtime handle,
   runtime, provider connection, credential, or deployment. Complete as one
   local documentation commit on
   `docs/mellycore-framework-bridge-contract-spec-review-001`, not pushed. Full
   detail:
   `docs/research/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_REVIEW_001.md`,
   `docs/tasks/MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-REVIEW-001.md`.
11. `MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-001` — `SPECIFIED`
   (documentation only, **unverified**), 2026-08-03. Defines the canonical
   **Shared Context Bridge Contract**
   (`docs/specs/MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_SPEC_001.md`, version
   1.0, 50 sections). The task identifier was **minted by explicit Operator
   authorization** for the queued plain-name item "Shared Context Bridge",
   after a repository-wide search confirmed no conflicting identifier existed.
   Fixes the one-directional exchange chain — canonical Shared Context →
   bounded selection → validated projection → execution-local or
   framework-local context → returned proposal → validation, provenance,
   policy and approval gates → optional canonical mutation **by the canonical
   owner alone** — and prohibits the inverse: **no framework, agent, package,
   provider, tool, plugin, hook, command, MCP server, adapter, or batch worker
   may independently mutate canonical Shared Context**. Defines the logical
   context envelope, purpose- and consumer-bounded selection, projection
   eligibility, ten read boundaries, five separated write/mutation concepts, a
   ten-phase proposal lifecycle, thirteen mandatory return-path checks treating
   all returned context as untrusted, provenance that never collapses to the
   latest producer, ten never-flattened namespaces, a secret boundary,
   compression and transformation envelopes, fail-closed context loss,
   quarantine, thirteen validation layers that authorize nothing, eleven
   mutation-eligibility conditions, and twenty-one security threats. Memory
   scopes are mapped **by semantic name** onto Agent Runtime §18's six owner
   categories, creating no seventh category. **All seven upstream P2 findings
   were contained, not resolved**, and remain open; neither the Agent Package
   Contract nor the Framework Bridge Contract was edited. A **document-metrics
   table** was included deliberately, addressing Framework Bridge Review 001's
   `NEW-P3-01`; it caught two drafting drifts corrected before commit.
   **Nothing implemented** — no bridge, mutation engine, storage, database,
   vector store, memory service, compression, validation, or proposal-lifecycle
   runtime; context envelopes, proposals, and canonical mutations are **zero**;
   empirical framework validation remains `NOT_PERFORMED`. Complete as one
   local documentation commit on
   `docs/mellycore-shared-context-bridge-contract-spec-001`, not pushed. Full
   detail:
   `docs/tasks/MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-001.md`.
12. `MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-REVIEW-001` —
   `PASS_WITH_NON_BLOCKING_FINDINGS` (documentation only), 2026-08-04.
   Independent, read-only architecture, ownership, memory, security, and
   consistency review of the Shared Context Bridge Contract (version 1.0, commit
   `d3f8b73`). **P0 = 0, P1 = 0, P2 = 8, P3 = 2.**
   `MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_001` version 1.0 is **accepted as a
   documentation contract only**, under ten recorded constraints.
   **Owner lists were reconstructed mechanically, not accepted from the
   specification's claims**: Agent Runtime §17.1's seven operations, §17.2's ten
   fields, §17.4's six staleness conditions, §18's six memory categories, §19's
   seventeen trace fields and §33's 49 classes; `CONTEXT_GRAPH_SCHEMA.md` §5's
   nine relation types; Control Plane §7.1/§7.2/§8.1/§9.3; Integration Gateway
   §25.2; Agent Package §21; Framework Bridge §23; and the Context Ingestion
   Gate's five validation outcomes and nine refusal codes were each extracted
   from the owner document and tested against the reviewed text. **Every
   canonical owner document is byte-identical before and after this review.**
   **All 34 document-metric rows reproduce independently with zero
   discrepancies**, and the 50-section structure recounts exactly — the §48
   metrics table, added in response to Framework Bridge Review 001's
   `NEW-P3-01`, survives independent recount intact.
   **Verified `PASS` on the load-bearing safety properties:** a full-document
   search found **no direct or ambiguous canonical-write path** — no framework,
   agent, package, provider, tool, plugin, hook, command, MCP server, adapter,
   or batch worker may mutate canonical Shared Context, and only the canonical
   owner may, after the eleven-condition intersection and Operator approval;
   returned context stays untrusted against all five bypass temptations
   including byte-identity; provenance never collapses to the latest producer;
   ten namespaces are never flattened; sensitivity does not decay and only a
   recorded redaction may lower it; the secret boundary distinguishes reference
   from value throughout; safety- and authority-relevant loss fails closed with
   ambiguity resolving to loss; conflicts are surfaced and never adjudicated;
   thirteen validation layers authorize nothing; no new Control Plane status
   dimension is created; and the overclaim scan is clean, with every "implement"
   a scope exclusion or `NOT_IMPLEMENTED` row and every "trust" a denial.
   **New P2 findings (all non-blocking, all fail-closed):** four owner-defined
   semantic neighbours never audited or discriminated
   (`CONTENT_QUARANTINED`, `PROVENANCE_VERIFICATION_FAILED`,
   `ENVELOPE_INTEGRITY_FAILED`, `PROJECTION_LOSS_UNACCEPTABLE`);
   `INJECTION_SUSPECTED` attributed to Agent Runtime §33 when Runtime §33
   explicitly cedes ownership to Integration Gateway §25.2; the ten proposal
   phases and eleven rejection classes overlapping the Context Ingestion Gate's
   five outcomes and R1–R9 codes, the one owner omitted from the non-collision
   claim; seven of nine quarantine conditions carrying a conflicting §13
   "Reject" disposition with no precedence rule, and §13 check 6 explicitly
   "Reject or quarantine"; two of eight memory scopes mapping to no Agent
   Runtime §18 category with Control Plane §9.3's five layers unreconciled; the
   context envelope overlapping Control Plane's `ContextPacket` without citation;
   a proposal-replay mitigation citing a projection-only lease mechanism; and
   "subtractive or equal" being normative yet evaluated by no validation layer
   or eligibility precondition. **New P3 findings:** a `30.14` sub-heading over
   absent subsections, and an undefined `context_bridge_contract_version`.
   **All seven upstream P2 findings remain open and contained** — the contract
   owns no result normalization, emits neither overlapping class, uses no
   capability ordinal, treats no unvalidated framework profile as eligible,
   defines no package lifecycle rendering field, declares no Agent Package
   version canonically current, and enumerates no protected command class.
   **Neither upstream contract was edited.**
   **Nothing implemented** — no Shared Context Bridge, canonical mutation
   engine, storage, database, vector store, memory service, compression,
   validation, or proposal-lifecycle runtime; context envelopes, proposals, and
   canonical mutations remain **zero**; empirical framework validation remains
   `NOT_PERFORMED`. The reviewed specification was **not edited** and this
   review repaired nothing. Complete as one local documentation commit on
   `docs/mellycore-shared-context-bridge-contract-spec-review-001`, not pushed.
   Full detail:
   `docs/research/MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_SPEC_REVIEW_001.md`,
   `docs/tasks/MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-REVIEW-001.md`.

## How to Extend This File

Append new entries under the relevant phase heading (or a new heading for a
new track) as milestones complete, in the same style: what happened, its
actual status, and a pointer to the durable evidence. Do not backfill claims
this file cannot verify against `docs/tasks/`, `docs/research/`, or Git
history.
