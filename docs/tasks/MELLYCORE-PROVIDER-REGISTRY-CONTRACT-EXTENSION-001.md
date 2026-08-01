# MELLYCORE-PROVIDER-REGISTRY-CONTRACT-EXTENSION-001

## Purpose

Create the canonical Provider Registry contract extension enabling MellyCore
AIOS to describe, govern, and validate enterprise, cybersecurity, marketing,
integration-fabric, and restricted-MCP providers through one stable,
safety-first, fail-closed record structure — without any provider record
implying connection, credential existence, capability permission, or
execution authority.

This task is **specification-level only**. It does not authorize registry
implementation, adapter scaffolding, provider authentication, credential
access, provider API execution, MCP or fabric connection, or deployment.

## Starting repository state (verified)

- Authorized path: `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`;
  resolved git root matched exactly
  (`C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios`). Not MellyTrade, not
  `alpha_data_scraper_ai`, not a multi-repository parent.
- Starting branch:
  `docs/mellycore-enterprise-provider-document-integrity-remediation-001`
  — matched expected.
- Starting HEAD: `0695292a987ed31d0a70cf86d28753c3170ca715` — matched.
- Subject: `docs: repair enterprise provider document integrity` — matched.
- Parent: `40afc86258af4f7e46e061a8c4a0eca19827a511` — matched.
- Worktree clean at session start.
- `clean-origin` → `https://github.com/Melly-999/mellycore-aios-core.git`,
  confirmed canonical; `origin` remains an unrelated, uncontacted mirror.

## Remote and chain gate

- Read-only `git fetch clean-origin --prune`.
- `clean-origin/main` = `947f33d27d5546775186e96bdc61e30db78c0b3d` —
  **no drift**.
- Remediation commit `0695292…` re-verified: single parent
  `40afc86…`, exactly its reported six files.
- No remote branch exists for any branch in the local enterprise-provider
  chain.
- No pre-existing Provider Registry extension branch, task report, or
  conflicting contract.

## Dependency chain

```text
947f33d2 (clean-origin/main)
  └── adcceae9  ENTERPRISE-PROVIDER-ROADMAP-SYNC-001            (local)
        └── e4b8db4a  ENTERPRISE-PROVIDER-DECISION-RECORD-001    (local)
              └── 40afc862  CLOUDFLARE-API-SHIELD-CONNECTOR-CONTRACT-001 (local)
                    └── 0695292a  ENTERPRISE-PROVIDER-DOCUMENT-INTEGRITY-REMEDIATION-001 (local)
                          └── <this task>  PROVIDER-REGISTRY-CONTRACT-EXTENSION-001 (local)
```

Branch created from `0695292a987ed31d0a70cf86d28753c3170ca715`, **not**
from `clean-origin/main`, preserving the full enterprise-provider chain.

## Canonical sources read

- `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md`
  (complete, including the cross-reference corrections applied by the
  preceding remediation).
- `docs/specs/MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md`
  (full heading map + §13.0 attribute list, for the conformance mapping).
- `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` —
  header/status, §7.1 common entity contract, §7.2 entity catalogue, §7.3
  relationship rules, §8.1/§8.2 status taxonomy, §9.1 Provider Registry and
  Model Gateway, §9.6 Integration Gateway, §9.9 Security and Secrets
  Boundary, §16 approval contract, §17 secrets boundary, §18 provenance,
  §19 failure states, §24 decision records, §25 integration seams.
- `docs/specs/MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001.md` —
  §4 provenance labels, §5 sensitivity labels, §5.1 hard rules, §5.2
  `allowed_use` matrix.
- `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md` — §1.5
  truthfulness rules and contract-spec format precedent.
- `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCUMENT-INTEGRITY-REMEDIATION-001.md`.
- `shared_context/PROJECT_STATE.md`, `ROADMAP.md`, `RUN_QUEUE.md`,
  `AGENT_HANDOFF.md`, `SAFETY_CONTRACT.md`, `PROVIDER_SETUP.md`,
  `MODEL_ROUTING.md`, `VALIDATION.md`.

## Existing Provider Registry source discovered

Repository-wide search for `provider registry` / `provider_registry` /
`ProviderRegistry` returned no dedicated contract. The closest — and only —
existing canonical definition is
`docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md`:

- **§7.2 entity catalogue** — a `Provider` entity (`provider_id`; AI model
  provider oriented: "Has Models", `modalities`, `access_class`,
  `authentication_mode`) and a separate `Integration` entity
  (`integration_id`; "External-system metadata", metadata-only catalogue
  with `access_mode`, `allowed_actions`, `read_write_class`, `risk_class`).
- **§9.1 "Provider Registry and Model Gateway"** — a UI module contract for
  inspecting provider/model inventory, explicitly "no connect or credential
  action".

The enterprise-provider ADR independently confirms the absence of a
Provider Registry *contract*, by repository-wide search recorded in its §1.

`shared_context/PROVIDER_SETUP.md` and `MODEL_ROUTING.md` are AI-model
placeholder/routing notes, not registry contracts.

## Extension strategy (and why)

**Chosen: a new dedicated extension specification that normatively extends
the Control Plane spec without modifying it.**

Reasons:

1. The Control Plane spec is a **frontend/IA contract**
   (`SPEC_ONLY · CONTROL_PLANE_ONLY`), and its own §7.3 states the entity
   model "is not a production database schema". Embedding an enterprise
   governance contract inside it would mix concerns.
2. Its `Provider` entity is scoped to **AI model providers**; its
   `Integration` entity is a deliberately **metadata-only** catalogue.
   Neither is a governance record for a provider holding R4/R5 security
   capabilities.
3. It is already **merged into canonical `main`** (PR #27) and carries its
   own acceptance and supersession rules; editing it in place from this
   unpushed chain would mutate a merged document and risk disturbing its
   accepted status statement.
4. The task ID, ADR §19 item 3, and all four shared-context files name this
   artifact a **contract extension**.

The location and strategy were therefore **unambiguous**; no stop condition
was triggered.

## Paths

- **Contract:**
  `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`
  (new; 32 numbered sections; contract ID
  `MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_001`; v1.0). Naming
  follows the established precedent: task ID `…-CONTRACT-001` → file
  `…_CONTRACT_SPEC_001.md`, matching both
  `MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md` and
  `MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md`.
- **Task report:**
  `docs/tasks/MELLYCORE-PROVIDER-REGISTRY-CONTRACT-EXTENSION-001.md`
  (this file).

## Field groups defined

Provider identity (7); provider categories (8); integration classes (9);
lifecycle (10); scope hierarchy (11); authentication modes (12); credential
profiles (13); capability records (14); risk and approval metadata (15);
data classification (16); external-content posture (17); API/connector
compatibility (18); health and availability (19); audit and provenance
(20); registration-versus-authorization separation (21); integration-fabric
chain (23); MCP registration and suspension/deprecation/retirement (24);
provider-specific inheritance (25); Cloudflare conformance (26); validation
(27); rejected designs (28); prerequisites (29); open questions (30);
amendment rules (31); references (32).

## Terminology reconciliation performed

The `Provider` versus `Integration` overlap in Control Plane §7.2 was a
genuine architectural tension: an enterprise security provider fits neither
(not a model provider; far more consequential than a metadata-only
catalogue entry).

**Resolved without weakening or editing that spec** (contract §7.4): this
contract defines a governance-layer `ProviderRecord` as the authoritative
object, and treats the Control Plane's `Provider` / `Integration` /
`Tool` entities as **display projections** of it, carrying display metadata
only and never authorization — consistent with §9.1's "no connect or
credential action" and §9.6's "no Connect, OAuth, authorize, or
credential-entry flow". Both documents remain simultaneously true. This
was recorded as a reconciliation, not an amendment.

## Lifecycle model

The candidate state list supplied for this task was **reviewed, not adopted
verbatim**, and split across three orthogonal axes (contract §10):

- **Axis A `registration_status`** (record governance): `candidate` →
  `research_recorded` → `architecture_accepted` → `contract_defined` →
  `conformance_verified`, with `suspended` / `deprecated` / `retired`.
- **Axis B `adapter_state`** (adapter implementation): `not_started` →
  `blocked` → `planned` → `scaffolded` → `implemented` → `test_verified`,
  plus `withdrawn`.
- **Axis C**: the eight authorization facts — **not** lifecycle states.

Material changes, all documented in contract §10.5:

| Proposed | Disposition | Reason |
| --- | --- | --- |
| `implementation_blocked`, `adapter_planned`, `adapter_scaffolded`, `test_only` | Moved to Axis B | They describe the adapter, not the provider record |
| `authorized_read_only`, `authorized_limited_write` | **Rejected as lifecycle states** | They are authorization facts; making them lifecycle states would collapse Axis C into Axis A — exactly the "registration as authorization" design the task requires rejecting. Authorization is per-tenant, per-capability, and independently revocable; a lifecycle state cannot express that |
| — | Added `conformance_verified` | §27 needs a "validated" state distinct from "a contract exists" |

Transitions are step-wise (no skipping), evidence-gated, operator-authorized
for `architecture_accepted` and beyond, reversible when evidence lapses
(the correct fail-closed response to contract drift), and **never**
authorizing.

## Capability model

27 required fields per capability (contract §14.1). Capability IDs are
immutable and provider-bound. Four fail-closed rules are explicit: absence
from the registry denies; a missing `risk_tier` denies (never defaults R0);
a missing `required_provider_scope` denies (never defaults wildcard); a
missing `approval_policy` denies (never defaults allow). `prohibited`
capabilities are registered deliberately so a request naming one is
recognized and audited rather than merely unsupported. The registry stores
record shape and references — it does **not** restate provider capability
tables, avoiding a second source of truth that could drift.

## Credential model

Four credential classes (`read`, `controlled_write`, `containment`,
`investigation`) with mandatory read/write separation, `secret_manager_ref`
as an opaque reference only, full lifecycle metadata (expiry, rotation,
revocation, last verification), and a `write_separation_ref` asserting
separation holds. Prohibited: raw secrets or secret-shaped values anywhere;
credential material in model-visible context; hidden cross-profile
fallback; automatic widening; one profile serving both read and write.

**Explicitly stated (contract §13.3): profile presence is not credential
existence.** A profile describes a credential that *would* be used; whether
one exists, and whether it is verified, are separate Section 21 facts.

## Registration versus authorization (the core)

Eight independent, conjunctive, fail-closed facts (contract §21): provider
registered; adapter implemented; credential configured; credential
verified; tenant authorized; capability authorized; runtime enabled;
operation approved. Any one missing, `unknown`, expired, or unresolved
denies, with no override. No field may collapse two or more. Facts 1–7 are
standing state; only fact 8 authorizes a specific operation, and only for
its exact digest-bound target. `authorization_status` is a **computed
view**, never a stored grant.

## Fabric and MCP model

**Fabric:** the chain `MellyCore → fabric → downstream provider → resource`
is preserved end to end; the fabric and downstream provider keep separate
`provider_id`s; each `(fabric, downstream)` pair is registered as its own
integration-class record because credential, audit, and enforcement
properties differ. A fabric must never obscure the downstream provider,
acting identity, capability, target, policy decision, or approval — if it
cannot surface all six, `provenance_loss_risk: high` and the pair is
**ineligible for R3–R5**. Policy enforcement never delegates to the fabric.

**MCP:** registered as a distinct record type with 18 fields. Defaults are
fail-closed: no unrestricted search-and-execute; no autonomous generic
execution; read-only or documentation-only unless a provider contract
authorizes more; `output_trust_level` always `untrusted`; and **dynamic
tool discovery is ineligible for autonomous use** (a tool set that can
change between sessions cannot be pre-approved). Provider-specific
contracts may only narrow these.

## Cloudflare conformance result

**Representable with no weakening detected** (contract §26). The
Cloudflare record maps to `provider_id: cloudflare`,
`provider_category: cybersecurity`, `integration_class: native_adapter`
(required, since it holds R4/R5), scope dimensions `tenant/account/zone`,
`registration_status: contract_defined`, `adapter_state: blocked`.

Its **58 capabilities** (16 read-only, 16 proposal-only, 23
approval-required mutations, 3 operator-investigation) plus **13
prohibited** map onto §14.1; its 25 per-capability attributes are a
**subset** of the registry's 27. The two extra registry fields —
`implementation_status` and `authorization_status` — are the registry's own
contribution, keeping description separate from readiness and
authorization.

Every Cloudflare safety rule checked is preserved by a generic mechanism:
legacy exclusions via `prohibited_legacy_surfaces` + no-legacy-fallback;
zone-wide `block` R5 via "provider contracts may raise, never lower";
read/write separation via two credential classes; the account-scope hazard
generalized into §11.3; documentation-only MCP via `mutation_prohibited` +
`operator_only` + `autonomous_agent_eligible: false`; mandatory
read-after-write for every `mutation` capability; and read-only Cloudflare
access still unauthorized because Section 21 facts 5–7 are unsatisfied.

**Notably, the registry deliberately records Cloudflare as
`contract_defined`, not `conformance_verified`**, because the Cloudflare
contract's own §8.8 carries open `UNVERIFIED` items and §27.1 item 14
requires those to be resolved and dated first. The registry does not
flatter the provider it was built to represent.

## Data classification

The task's suggested classification list was **not** adopted as a new
scale, because a canonical one already exists. `sensitivity_level` reuses
the five values from
`MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001` §5 (`public`,
`internal`, `private`, `secret`, `regulated_high_risk`) with its
`allowed_use` matrix and hard rules unchanged. The task's additional
notions (security telemetry, customer content, authentication data,
regulated data, …) are captured as an **orthogonal, descriptive
`data_categories` axis that maps into** that scale, raising the minimum
sensitivity but never lowering it, with the highest category governing a
mixed response. This satisfies the task's field requirement without
inventing a conflicting vocabulary.

## Unresolved questions

Six, recorded in contract §30: where tenant-provider and tenant-capability
authorization records live (deferred to the Integration Gateway contract);
credential-verification mechanics; how fabric "equivalence" to a native
adapter is concretely demonstrated; numeric freshness thresholds;
whether `regulated_high_risk` provider data can ever be admitted (the
sensitivity spec defers this to a process that still does not exist); and
registry storage format, deliberately unspecified to avoid edging into
implementation.

## Shared-context updates

Only the enterprise-provider parallel track was touched. The **global
OpenAI Batch pointer
(`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`) was not modified**
in any file — verified by per-file occurrence counts against `HEAD` and by
diff inspection.

- `shared_context/RUN_QUEUE.md` — item 4 marked complete with the contract
  pointer; item 5 (`-INTEGRATION-GATEWAY-SECURITY-CONTRACT-001`) becomes
  the exact next task; items 6–8 remain queued; item 9 (adapter scaffold)
  remains explicitly blocked and unauthorized.
- `shared_context/ROADMAP.md` — sequence item 4 marked complete; item 5 is
  now next.
- `shared_context/PROJECT_STATE.md` — a concise "Provider Registry contract
  extension — complete" pointer; outstanding-work list updated.
- `shared_context/AGENT_HANDOFF.md` — new "Latest Update" entry; prior
  entry relabelled "Previous Update" per the file's reverse-chronological
  convention.

Concise pointers only; no contract content duplicated into shared context.

## Validation results

| Check | Result |
| --- | --- |
| `python scripts/validate_project_state.py` | **PASS** — `PASS MellyCore project scaffold validation passed`, exit `0` |
| `git diff --check` / `git diff --cached --check` | Clean, exit `0` |
| `git status --short` / `--name-only` / `--stat` | Exactly the six allowlisted paths |
| Task-ID uniqueness | No pre-existing occurrence of `MELLYCORE-PROVIDER-REGISTRY-CONTRACT-EXTENSION-001` outside forward references in the ADR and shared context |
| Contract-ID / title uniqueness | No pre-existing `MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION` anywhere |
| Registration ≠ execution authorization | Contract §21, §6 principle 1, §28 |
| Provider state not one boolean | Contract §21.2 rule 2; §28 first row |
| Eight facts separate | Contract §21.1 |
| Provider/capability IDs stable | §7.1, §7.3, §14.2 rules 1–2 |
| Missing risk tier / scope / approval fail closed | §14.2 rules 3–5 |
| Read/write credentials separate | §13.1, §13.2 |
| Raw secrets prohibited | §13.2, §5 |
| Delegated-user fallback prohibited | §12 |
| Provider account ≠ tenant boundary | §11.3 |
| Fabrics preserve downstream identity | §23.1–§23.3 |
| MCP explicitly constrained | §24.1–§24.2 |
| Provider contracts cannot weaken generic safety | §25.1 rule 3, §25.2 |
| Cloudflare 58 capabilities representable | §26.2 |
| Cloudflare legacy exclusions intact | §26.3 |
| External content untrusted | §17 |
| Audit and provenance mandatory | §20, §20.4 |
| Lifecycle transitions require evidence | §10.2, §10.3 rule 2 |
| Suspension/deprecation fail closed | §24.3 |
| Adapter scaffolding still blocked | §29 item 6; shared context |
| Global OpenAI Batch pointer unchanged | Verified by occurrence count and diff |
| No provider described as connected/authenticated/deployed/runtime-enabled | §1.2 states the opposite for every dimension; prohibited-claim scan reviewed |
| Secret/credential scan | No `.env` content, API key, token, account ID, zone ID, or secret-shaped value |

### Validator evidence

- `python scripts/validate_project_state.py` → `PASS MellyCore project
  scaffold validation passed`, exit `0`.
- `python -m pytest -q` → **NOT_RUN**: pytest is not installed in this
  session's Python environment, and this task is explicitly forbidden from
  installing dependencies. Recorded as `NOT_RUN`, **never** as passing.
  Non-blocking: the change set is documentation-only across six Markdown
  files, touching no Python module, test, fixture, dependency, or lockfile.
- `git diff --check` → no output, exit `0`.

No unavailable validator is reported as passed.

## Final local commit

Exactly one new local commit, subject `docs: extend provider registry
contract`, on branch
`docs/mellycore-provider-registry-contract-extension-001`, parent
`0695292a987ed31d0a70cf86d28753c3170ca715`. Six files, all within the
printed allowlist. **Not amended.** No existing commit was reset, rebased,
squashed, cherry-picked, or rewritten.

## Explicit no-push status

Not pushed to any remote. No pull request. No merge. No tag. No release. No
remote branch. No deployment. No provider authentication. No provider API
call — including read-only. No Cloudflare API call. No MCP or
integration-fabric connection. No credential or secret created, read, or
stored. No `.env` touched. No registry implementation, adapter, scaffold,
JSON Schema, TypeScript, Python, SQL, migration, source code, workflow
YAML, dependency, or lockfile change. No destructive git operation. The
MellyTrade / `alpha_data_scraper_ai` repository was not accessed.

## Exact next task

`MELLYCORE-INTEGRATION-GATEWAY-SECURITY-CONTRACT-001` — not started.

Adapter scaffolding (`MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-001`) remains
blocked and unauthorized. The global track's live next task,
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`, is unchanged by this
task.
