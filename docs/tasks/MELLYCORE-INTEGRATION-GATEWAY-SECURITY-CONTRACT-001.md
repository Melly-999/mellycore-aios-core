# MELLYCORE-INTEGRATION-GATEWAY-SECURITY-CONTRACT-001

## Purpose

Create the canonical Integration Gateway Security Contract governing how
MellyCore AIOS may later route requests between operators, agents, provider
adapters, integration fabrics, MCP servers, webhooks, and downstream
enterprise providers — establishing the trust boundary, identity chain,
deterministic policy-evaluation order, credential custody, approval
binding, envelopes, error taxonomy, audit and delivery semantics, failure
containment, and runtime enablement gate.

This task creates a **security contract only**. It does not authorize
Gateway implementation, runtime execution, provider credentials, provider
authentication, provider API access, MCP connection, integration-fabric
connection, webhook registration, deployment, or production use.

## Starting repository state (verified)

- Authorized path: `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`;
  resolved git root matched exactly
  (`C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios`). Not MellyTrade, not
  `alpha_data_scraper_ai`, not a multi-repository parent.
- Recovery-remediation branch:
  `docs/mellycore-integration-gateway-security-contract-001` — matched.
- Starting HEAD: `7c3b971e93790e1ad10b1c6cf452ac1c5c60f7c6` — matched.
- Subject: `docs: extend provider registry contract` — matched.
- Parent: `0695292a987ed31d0a70cf86d28753c3170ca715` — matched.
- The original authoring attempt was interrupted with a dirty worktree.
  Recovery assessment later verified the five pre-existing dirty paths and
  authorized remediation preserved them rather than recreating the work.
- `clean-origin` → `https://github.com/Melly-999/mellycore-aios-core.git`,
  confirmed canonical; `origin` remains an unrelated, uncontacted mirror.

## Remote and chain gate

- Read-only `git fetch clean-origin` during recovery remediation.
- `clean-origin/main` = `947f33d27d5546775186e96bdc61e30db78c0b3d` —
  **no drift**.
- Provider Registry commit `7c3b971e…` re-verified: single parent
  `0695292a…`, exactly its reported six files.
- No remote branch exists for
  `docs/mellycore-integration-gateway-security-contract-001`.
- No equivalent committed Integration Gateway contract or task report was
  found locally or on fetched `clean-origin` refs. The untracked contract
  and task report were preserved as recovery evidence.

## Dependency chain

```text
947f33d2 (clean-origin/main)
  └── adcceae9  ENTERPRISE-PROVIDER-ROADMAP-SYNC-001                 (local)
        └── e4b8db4a  ENTERPRISE-PROVIDER-DECISION-RECORD-001         (local)
              └── 40afc862  CLOUDFLARE-API-SHIELD-CONNECTOR-CONTRACT-001 (local)
                    └── 0695292a  ENTERPRISE-PROVIDER-DOCUMENT-INTEGRITY-REMEDIATION-001 (local)
                          └── 7c3b971e  PROVIDER-REGISTRY-CONTRACT-EXTENSION-001 (local)
                                └── <this task>  INTEGRATION-GATEWAY-SECURITY-CONTRACT-001 (local)
```

At recovery start, the target branch still pointed to
`7c3b971e93790e1ad10b1c6cf452ac1c5c60f7c6`, **not**
`clean-origin/main`, preserving the full five-commit chain.

## Canonical sources read

- `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md`
- `docs/specs/MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md`
  (read completely during recovery remediation)
- `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`
  (read completely during recovery remediation)
- `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` —
  §3.1 Control/Data Plane boundary, §3.2 current-phase rule, §3.3 trust
  boundary, §8 status taxonomy, §9.6 Integration Gateway module, §16.1
  approval contract, §16.2 hard prohibitions, §17 secrets boundary, §18
  provenance, §19 failure states, §25 integration seams
- `docs/specs/MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001.md`
- `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md` (§1.5)
- `docs/tasks/MELLYCORE-PROVIDER-REGISTRY-CONTRACT-EXTENSION-001.md`
  (read completely during recovery remediation)
- `shared_context/PROJECT_STATE.md`, `ROADMAP.md`, `RUN_QUEUE.md`,
  `AGENT_HANDOFF.md`, `SAFETY_CONTRACT.md`, `VALIDATION.md`

Repository-wide searches were run for `integration gateway`,
`integration_gateway`, `webhook`, and for any existing `*SECURITY*` or
`*GATEWAY*` document.

## Gateway owner discovered

The only existing definition is
`docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` §9.6
"Integration Gateway" — a **metadata-only display catalogue** whose
Interactions row reads "Inspect, Compare, Filter, View evidence; **no
Connect, OAuth, authorize, or credential-entry flow**". No enforcement-
boundary contract exists anywhere in the repository. No webhook or
event-ingestion contract exists.

## Document strategy

**Dedicated contract that normatively extends the Control Plane spec
without modifying it.**

The decisive evidence is in the Control Plane spec itself:

- **§3.1** assigns Integrations' "OAuth, connection, network
  communication, read/write operations" to the **future Data Plane**
  column, not the Control Plane.
- **§3.2** states a future Data Plane "may consume approved, versioned
  manifests only after its own architecture, threat model, implementation
  task, and validation gates are accepted."

This contract **is** that anticipated Data Plane architecture and threat
model for the integration path. Writing it as a separate document is what
that spec requires, not a workaround. §9.6 remains the display projection;
this contract governs the enforcement boundary beneath it — the same
layering the Registry contract established for `ProviderRecord` versus the
§7.2 `Provider`/`Integration` entities. Ownership and location were
therefore **unambiguous**; no stop condition was triggered, and no
material conflict was found among the accepted contracts.

## Paths

- **Contract:**
  `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`
  (new; 40 numbered sections; contract ID
  `MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_001`; v1.0). Naming
  follows the established precedent (task ID `…-CONTRACT-001` → file
  `…_CONTRACT_SPEC_001.md`).
- **Task report:**
  `docs/tasks/MELLYCORE-INTEGRATION-GATEWAY-SECURITY-CONTRACT-001.md`
  (this file).

## Trust-boundary decision

**The Gateway is a policy-enforcement boundary, not a proxy** (§6.1). It
does not forward requests: it re-derives the authorization decision from
authoritative records on every call and **constructs a new bounded provider
request** from validated inputs. A caller's request is a *proposal
describing intent*, never a request to relay. Any design passing through a
caller-supplied URL, method, body, header set, or tool invocation is
declared non-conforming.

Fourteen categories of untrusted input are enumerated (§6.2), with a
**claim-to-fact resolution rule** (§6.3): a claim is only ever used to
*look up* an authoritative record, never as the operative value — a caller
claiming `tenant_id: T` causes resolution of the *authenticated* tenant and
a comparison; mismatch denies.

## Identity model

Twelve identities (§8.1), each classified across five independent axes:
authenticated, authorization subject, execution actor, credential owner,
audit actor. Six normative rules (§8.2), including: session/conversation/
context/agent/model identifiers are **never authorization**; an agent may
request but never approve; a credential is a means, not an actor; **the
fabric is transport, never subject**; service-account actions are always
labelled; and identities may legitimately differ across the chain — what
may never happen is any of them being lost, merged, or substituted.

## Acting-identity chain

Ten links (§9.1) with per-link requirement and absence behavior (§9.2) and
six validation rules (§9.3): continuity (a break denies, never bridged by
inference); **no substitution** — most importantly a fabric must not
replace downstream identity with its own; no collapsing to endpoints;
impersonation prevention (a link is assertable only by the component that
authenticated it); immutability in flight; and full audit representation.

## Provider Registry resolution model

All sixteen facts resolved from authoritative records before any external
execution (§11), mapped explicitly onto the Registry's eight authorization
facts. Two rules added: **any unresolved, missing, stale, deprecated,
suspended, conflicting, or unverified mandatory record denies** — no
partial resolution proceeds; and **revision pinning**, where the registry
and provider-contract revisions are pinned into the envelope and re-checked
immediately before execution, with mid-flight change denying via
`CONTRACT_CONFLICT`.

## Capability-resolution model

One capability ID resolves to **exactly one bounded operation** (§12.1);
seven prohibited resolution targets enumerated (arbitrary HTTP, arbitrary
MCP tool, arbitrary provider methods, unrestricted search-and-execute,
dynamic mutation discovery, hidden fallback, undocumented actions). Nine
resolution rules (§12.2), notably: **an alias may never widen permissions,
risk tier, or scope**; a deprecated ID resolves to a *denial*, never
silently to a successor; the **higher** of generic and provider-specific
risk tier governs; and any ambiguity denies — the Gateway never guesses.
§12.3 forbids capability selection from untrusted text.

## Tenant and scope model

Two independent boundaries — the MellyCore tenant boundary and the
provider-native resource boundary — with fourteen provider-native
dimensions (§13.1). Seven rules (§13.2): caller scope claims untrusted;
targets resolve through Registry allowlists; wildcards fail closed and are
never permitted at R3–R5; R3–R5 require exact enumeration; cross-tenant
reuse prohibited for cache, context, session, queue, credential,
idempotency key, and response; provider account scope is not a tenant
boundary; fabric tenancy does not replace downstream tenancy.

§13.3 adds a security refinement: **denial is coarse outward, precise
inward**, so the Gateway does not become an existence oracle for resources
the caller may not know about, without losing audit fidelity.

## Credential-custody model

Eight exposure prohibitions (§14.1); credentials handled exclusively
through opaque references resolved outside model-visible context at the
moment of use and never returned upward. Eight required selection inputs
producing **deterministic** selection (§14.2). Seven prohibited selection
behaviors (§14.3), each with an audited-security-event consequence:
automatic widening, cross-tenant fallback, delegated→service-account
fallback, read→write escalation, Global API Key fallback, "best available
credential" selection, and selection influenced by untrusted content.
Rule 14.4 makes a provider permission failure **terminal** — never retried
with a broader credential.

## Delegated-user and service-account rules

Delegated execution (§15) preserves end-user identity, uses only that
user's scopes, fails on absent/expired grants, **never silently switches to
a service account**, and records the delegated subject. Service-account
execution (§16) is explicitly labelled everywhere, requires tenant policy
permitting it, uses a separately registered profile, may carry stricter
limits but never looser, and is never presented as user-executed.
Rule 16.7 enforces exclusivity: exactly one identity type per request —
both, or neither, denies.

## Policy-evaluation order

Twenty-six ordered steps with a named failure class each (§17). Three
rules make the ordering load-bearing rather than decorative:

- **17.1 no compensation** — no later step may compensate for a failed
  earlier one.
- **17.2 no reordering**, with the security reasoning stated: credential
  resolution (step 14) occurs *after* authorization (9–12), so an
  unauthorized request never causes a credential to be resolved; approval
  binding (18) after validation (17); concurrency (19) after binding, so an
  approval can never be bound to state it did not describe.
- **17.3 two-stage durable audit** — step 21 reserves and acknowledges the
  exact R3–R5 execution intent before step 22 execution; step 25 appends
  completion after verification and before step 26 delivery. Reservation
  failure prevents execution; completion failure prevents success and
  triggers reconciliation without re-executing the mutation.

## Approval-binding model

Twelve bound elements (§18.1), explicitly **extending** rather than
replacing the Control Plane §16.1 four-field immutable core. Four rules
(§18.2): re-approval on any change; recompute-before-execute; single use,
single target, no replay; no self-approval or blanket consent. §18.3
enumerates eight insufficient approval forms, including "allow Cloudflare
changes", "approve this session", and a digest match without matching
target type/ID/version. §18.4 clarifies that R0–R2 resolve to
`approval_state: not_required` — a **resolved** decision that is recorded,
not an absent one.

## Native / fabric / MCP boundaries

**Native adapters** (§19) must expose eleven bounded artifacts. Rule 19.1
forbids any arbitrary-request or `execute_any` escape hatch to autonomous
agents. Rule 19.2: the adapter does not decide — an adapter performing its
own capability resolution, credential selection, or approval
interpretation is non-conforming.

**Fabrics** (§20) must preserve the full chain and declare thirteen
properties. Four rules: lost provenance **prohibits R3–R5**; fabric
fallback across provider/credential/tenant/capability/region/mode requires
a **fresh policy decision and fresh approval** (silent failover is a
violation, not resilience); policy enforcement stays in MellyCore and a
fabric's claim to have already evaluated policy carries no weight; and a
fabric is never the cybersecurity execution boundary.

**MCP** (§21) registers separately with fourteen declarations and nine
fail-closed defaults, including: tool descriptions are untrusted metadata;
MCP tools must map to registered MellyCore capability IDs; unregistered
tools are not executable; **discovery never authorizes**; dynamic
discovery cannot authorize mutation; and Cloudflare MCP remains
documentation-only. Four phases are defined with Rule 21.4 requiring a
contract amendment **and** explicit operator authorization to advance —
never implicit, never inferred from usage, never granted by the server
itself. Rule 21.5: MCP output is never evidence.

## Webhook security model

Thirteen mandatory inbound controls (§22.2). §22.3 separates what inbound
events **may** create (observations, alerts, draft proposals, queued review
items) from what they may **not** do (authorize a consequential action,
select a capability or credential, satisfy an approval, alter policy or
allowlists, or trigger a mutation directly *or transitively*).

Rule 22.4 states the structural asymmetry plainly: **there is no path by
which a provider can cause MellyCore to act on that provider by sending it
an event.** Every outbound consequential action re-enters §17 from step 1
with its own identity chain, approval, and audit. Rule 22.5 quarantines
unverifiable sources with provenance intact.

## Request and response envelopes

Request envelope: 27 fields (§23), carrying an **opaque credential profile
reference only** and sanitized parameters validated against the
capability's declared shape, with unknown fields rejected rather than
carried. Response envelope: 18 fields (§24), with Rule 24.1 stating that
transport success is not operation success — `execution_status`,
`provider_status`, `read_after_write_status`, and `delivery_status` are
independent and never collapsed; Rule 24.2 marking every provider-authored
field untrusted with provenance; Rule 24.3 sanitizing errors outward while
audit stays precise.

## Error and failure model

**Reconciled, not invented** (§25.1). The accepted Cloudflare contract §28
already defines a canonical class set, so **those names are adopted
unchanged as the base**, and Gateway-layer classes added only where no
equivalent existed. Material dispositions recorded: `tenant mismatch`,
`capability unauthorized`, and `target scope denied` were **merged** into
the existing `AUTHZ_DENIED_MELLYCORE` refined by an internal
`denial_reason`, because separate outward classes would make the Gateway an
existence oracle; `credential insufficient` merged into
`AUTHZ_DENIED_PROVIDER`; several proposed names mapped onto existing
classes; two genuinely new classes added (`CONTENT_QUARANTINED`,
plus Gateway-layer `IDENTITY_UNRESOLVED`, `PROVIDER_UNREGISTERED`,
`RUNTIME_NOT_ENABLED`, `AUDIT_RESERVATION_FAILED`,
`AUDIT_COMPLETION_FAILED`, `AUDIT_UNAVAILABLE_FOR_READ`,
`AUDIT_RECORD_INDETERMINATE`, `DELIVERY_FAILED` and others with no
Cloudflare counterpart).

§25.3 makes the outward-coarse/inward-precise asymmetry **required, not
optional**. §25.4 forbids silent degradation.

## Retry, idempotency, and concurrency

Reads retry only on `RATE_LIMITED`/`PROVIDER_UNAVAILABLE` with bounded
backoff and a per-`(tenant, credential_profile)` budget (§26.1). Mutations
are **never blindly retried** (§26.2). §26.3 makes `INDETERMINATE`
reconciliation mandatory: fresh authoritative read → compare to approved
after-state → success with evidence, or new proposal + new approval, or
`PARTIAL_APPLICATION` with the exact partial state. Idempotency keys are
derived from tenant, provider, capability, enumerated targets, approval
reference, and before-state digest, and are never shared across tenants
(§26.4). §27 requires fresh state, version preconditions, target and
approval fingerprints, per-resource serialization, and — Rule 27.1 — that
state change after approval **invalidates the approval and requires
re-approval** rather than silent reconciliation.

## Audit and delivery model

§29 defines a two-stage durable audit model. Stage A reserves the exact
R3–R5 execution intent and obtains durable acknowledgement before any
external mutation. Stage B appends attempt, response, verification,
containment, and delivery evidence while preserving Stage A. Completion
failure never authorizes a provider retry: it blocks success, starts
reconciliation/containment, and uses a durable outbox for the audit append.
The contract explicitly rejects a fictitious distributed transaction
across the audit store and provider. Provider/fabric request IDs are absent
or `not_applicable` before an attempt and use `not_returned`,
`not_supported`, or `unknown_after_timeout` when an attempted call yields
no ID; IDs are never invented.

§30 defines **six independent delivery statuses** — executed,
acknowledged, verified, audited, notified, received — never collapsed into
one `success`. Rule 30.2: critical security notifications never degrade
silently to an internal-only success state. Rule 30.3: delivery failure
stays visible without retroactively invalidating truthfully recorded
earlier statuses.

## Failure containment

Ten triggers mapped to containment actions (§31), with Rule 31.1 noting
that **containment is itself governed** — a containment action that mutates
provider state is a mutation requiring approval, idempotency,
verification, and audit. Rule 31.2 states no containment action is
authorized for runtime by this contract. Rule 31.3 requires a tracked
follow-up, since reducing enforcement is itself a posture regression.

## Runtime enablement gate

All seventeen conditions must be evidenced (§32), and **Rule 32.1 asserts
that none currently pass for any provider, including Cloudflare** —
consistent with the repository rule that a validator which did not run
records `NOT_RUN`, never a defaulted pass.

## Cloudflare conformance result

**Enforceable with no weakening detected** (§34.7). Six representative
flows were worked through, each showing identity chain, required Registry
facts, credential profile class, target scope, risk tier, approval
behavior, execution path, audit evidence, verification requirement, and
fail-closed conditions:

1. **Read-only operations inventory** (R1) — `CF_READ` only; fact 8
   resolves `not_required` and is recorded; truncated pagination may not
   back a deletion or replacement proposal.
2. **Proposal-only WAF rule change** (R2) — `CF_READ` only; a D2
   capability issued a write credential is non-conforming; no write
   request is ever issued.
3. **Endpoint-specific Schema Validation `block`** (R4→R5) — operator
   required; the 17-stage rollout must already have reached stage 12 and
   the emergency containment path must be proven reachable *before*
   execution.
4. **Zone-wide `block`** (R5 always, never downgraded) — exact zone
   enumeration, wildcard prohibited, R5 enhanced audit, verification
   control-plane only and never reported as edge enforcement.
5. **Endpoint deletion** (R5, irreversible) — dependency lookup and
   affected-feature list in the approval view; **absent traffic evidence
   blocks deletion**, since unknown is never read as zero.
6. **Documentation-only Cloudflare MCP** (R0) — operator-initiated only,
   no account grant, Phase 1 only, `code_mode_execute` prohibited, MCP
   output never evidence.

Every Cloudflare-specific restriction is either enforced by a generic
Gateway rule or preserved by §33's stricter-only inheritance. Read-only
Cloudflare API access **remains unauthorized** in every flow, because facts
5–7 are unsatisfied and `adapter_state` is `blocked`.

## Unresolved questions

§38 records seven, split by origin.

**Inherited from the Registry contract** (§38.1): where tenant-provider and
tenant-capability authorization records live — this contract fixes that
they must be explicit, separate, independently revocable records resolved
at §17 steps 9–10 whose absence denies, but leaves storage, issuance
workflow, and revocation propagation to the provider-pack specs and the
adapter-scaffold authorization; and how a fabric demonstrates
approval/audit equivalence to a native adapter — the *consequence* of
failure is fixed (R3–R5 prohibited) but the positive evidence standard is
not.

**New to this contract** (§38.2): cryptographic binding of the
acting-identity chain; credential verification without a broad probe;
bounded skew and replay-window values for webhooks; whether operator-only
low-level adapter diagnostics should exist at all in v1.0; and whether
multi-target R5 operations should be permitted or decomposed into
single-target operations.

## Recovery remediation

`MELLYCORE-INTEGRATION-GATEWAY-DIRTY-WORKTREE-RECOVERY-ASSESSMENT-001`
classified the work `REMEDIATION_REQUIRED`: the contract was coherent and
all 40 required sections were present, but the original policy order wrote
audit evidence only after external execution while claiming that audit
availability blocked R3–R5 execution. That P1 contradiction is closed by
the Stage A/Stage B durable audit protocol in §§17, 25, 29–31 and the
corresponding testing/prerequisite updates. The remediation also corrects
premature Git-state claims in this report and shared context, records
request-ID absence semantics, removes the duplicated next-task pointer,
and adds the previously missing handoff entry. No original dirty file was
discarded or replaced.

## Shared-context updates

Only the enterprise-provider parallel track was touched. The **global
OpenAI Batch pointer
(`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`) was not modified**
in any file — verified by per-file occurrence counts against `HEAD` and by
diff inspection confirming no pointer line was removed.

- `shared_context/RUN_QUEUE.md` — item 5 marked complete with the contract
  pointer; item 6 (`-CYBERSECURITY-PROVIDER-PACK-SPEC-001`) becomes the
  exact next task; items 7–8 remain queued; item 9 (adapter scaffold)
  remains explicitly blocked and unauthorized.
- `shared_context/ROADMAP.md` — sequence item 5 marked complete; item 6 is
  now next.
- `shared_context/PROJECT_STATE.md` — a concise "Integration Gateway
  security contract — complete" pointer; outstanding-work list updated.
- `shared_context/AGENT_HANDOFF.md` — new "Latest Update" entry; prior
  entry relabelled "Previous Update" per the file's reverse-chronological
  convention, and its now-stale next-task pointer reframed as a
  creation-time historical snapshot.

Concise pointers only; no contract content duplicated into shared context.

## Validation results (recovery remediation)

| Check | Result |
| --- | --- |
| `py -3.9 scripts/validate_project_state.py` | **PASS** — `PASS MellyCore project scaffold validation passed`, exit `0` |
| `git diff --check` / `git diff --cached --check` | Clean, exit `0` |
| `git status --short` / `--name-only` / `--stat` | Exactly the six allowlisted paths |
| Task-ID uniqueness | No pre-existing occurrence outside forward references in the ADR, Registry contract, and shared context |
| Contract-ID / title uniqueness | No pre-existing `MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT` anywhere |
| Gateway is a policy boundary, not a proxy | §6.1, §36 first two rows |
| Authentication separate from authorization | §10.1 (eight rejected equivalences), §10.2 |
| Session/context IDs not authorization | §8.2 rule 1, §10.1 |
| Eight Registry facts remain separate | §11, §17 steps 7–17 |
| Registration does not authorize runtime | §10.1, §11 |
| Capability existence does not authorize | §12, §17 step 10 |
| Tenant and provider-native scopes separate | §13.1 |
| Cross-tenant fallback prohibited | §13.2 rule 5, §14.3 |
| Raw credentials outside model context and logs | §14.1, §23.1, §29.3 |
| Delegated-user fallback prohibited | §15 rule 4, §14.3 |
| Service-account execution labelled | §16.1 |
| Deterministic evaluation order | 26 steps in §17 + rules 17.1–17.3 |
| Approvals bind to exact requests | §18.1–§18.3 |
| Native adapters bounded | §19, Rule 19.1 |
| Fabrics preserve downstream identity/provenance | §20.1, §20.3 |
| Lost fabric provenance prohibits R3–R5 | Rule 20.4 |
| MCP discovery does not authorize | §21.2 rules 6–7 |
| Cloudflare MCP documentation-only | §21.2 rule 9, §34.6 |
| Webhooks cannot authorize mutations | §22.3, Rule 22.4 |
| Mutation retries not blind | §26.2 |
| Unknown outcomes require reconciliation | §26.3 |
| Stale state invalidates approval | Rule 27.1 |
| External content untrusted | §28, Rules 28.1–28.2 |
| Audit reservation blocks R3–R5 before execution | §17 step 21, §29.2 and §29.6, Rule 17.3 |
| Audit completion failure blocks success and provider retry | §25.2, §29.3 and §29.6 |
| Request-ID absence is explicit | §29.4 |
| Read-after-write mandatory | §17 step 24, §35 item 11 |
| Delivery failure separate from execution success | §30, Rule 30.1 |
| Provider contracts cannot weaken generic safety | §33 rule 3 |
| Cloudflare contract representable | §34.7 |
| Adapter scaffolding remains blocked | §37 item 5; shared context |
| Global OpenAI Batch pointer unchanged | Verified by occurrence count and diff |
| Nothing described as active/connected/deployed | §1.2 states the opposite for every dimension; prohibited-claim scan reviewed |
| Secret/credential scan | No `.env` content, API key, token, account ID, zone ID, or secret-shaped value |
| No prior commit amended or rewritten | Starting HEAD remained `7c3b971e…` throughout remediation and was used as the sole parent for the authorized commit |

### Validator evidence

- `py -3.9 scripts/validate_project_state.py` → `PASS MellyCore project
  scaffold validation passed`, exit `0`.
- `python -m pytest -q` → **NOT_RUN**: this documentation-only remediation
  did not authorize or require pytest execution and forbade installing
  dependencies. Recorded as `NOT_RUN`, **never** as passing. Non-blocking:
  the change set is documentation-only across six Markdown files, touching
  no Python module, test, fixture, dependency, or lockfile.
- `git diff --check` → no output, exit `0`.

No unavailable validator is reported as passing.

### Final six-file staged allowlist

Validation prepared and the explicit staging phase verified exactly:

- `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`
  (`A`)
- `docs/tasks/MELLYCORE-INTEGRATION-GATEWAY-SECURITY-CONTRACT-001.md`
  (`A`)
- `shared_context/PROJECT_STATE.md` (`M`)
- `shared_context/ROADMAP.md` (`M`)
- `shared_context/RUN_QUEUE.md` (`M`)
- `shared_context/AGENT_HANDOFF.md` (`M`)

No other staged or unstaged path remained at the pre-commit gate.

## Final local commit

The recovery-remediation execution is authorized to create exactly one new
local commit with subject `docs: define integration gateway security
contract`, on branch
`docs/mellycore-integration-gateway-security-contract-001`, parent
`7c3b971e93790e1ad10b1c6cf452ac1c5c60f7c6`, containing only the six
allowlisted documentation paths. The resulting commit SHA is recorded in
the execution task's final report after commit creation; no placeholder or
unverified SHA is asserted here. No amend or history rewrite is permitted.

## Explicit no-push state

Not pushed to any remote. No pull request. No merge. No tag. No release. No
remote branch. No deployment. No provider authentication. No provider API
call — including read-only. No Cloudflare API call. No MCP connection. No
integration-fabric connection. No webhook endpoint created or registered.
No credential or secret created, read, or stored. No `.env` touched. No
Gateway implementation, adapter, scaffold, proxy, router, JSON Schema,
TypeScript, Python, SQL, migration, source code, workflow YAML, dependency,
or lockfile change. No destructive git operation. The MellyTrade /
`alpha_data_scraper_ai` repository was not accessed.

## Exact next task

`MELLYCORE-CYBERSECURITY-PROVIDER-PACK-SPEC-001` — not started.

Adapter scaffolding (`MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-001`) remains
blocked and unauthorized. The global track's live next task,
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`, is unchanged by this
task.
