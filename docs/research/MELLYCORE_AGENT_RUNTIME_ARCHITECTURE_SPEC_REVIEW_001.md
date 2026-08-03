# MellyCore Agent Runtime Architecture Spec Review 001

## 1. Title and status

**Task ID:** MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-001
**Reviewed contract:** MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_001 v1.0
**Review type:** Independent, read-only architecture, security, consistency, and
implementability review.
**Reviewer relationship to the artifact:** The reviewer did not author
`MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001`. Every architectural claim was
treated as unverified until independently confirmed against the specification
text, the canonical contracts, and deterministic scenario replay.
**Gate decision:** `FAIL_REMEDIATION_REQUIRED`
**Finding counts:** P0 = 0 · **P1 = 4** · P2 = 5 · P3 = 5
**Status:** Complete as one local documentation commit; **not pushed**.

This review authorizes no implementation, no framework installation or
connection, no agent execution, no model-provider call, no tool invocation, no
provider authentication, no credential configuration, no persistence, no
frontend, and no deployment. It does not repair any finding.

## 2. Purpose

Determine independently whether
`docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md` provides a safe
and deterministic canonical foundation for the Agent Package Contract, the
Framework Bridge Contract, the Shared Context Bridge, the Agent Runtime
Scaffold, the first Agent Package, cross-agent smoke testing, and future
operator observability — and to issue one defensible architecture-gate
decision.

The review optimizes for identifying duplicated canonical ownership, lifecycle
contradictions, collapsed authorization facts, framework bypasses, unsafe
context or memory writes, ambiguous handoff acceptance, direct provider or
credential paths, non-deterministic model routing, unsafe retries, cancellation
overclaims, missing reconciliation states, digest and canonical-serialization
weaknesses, insufficient tenant or run isolation, ambiguous Agent Package or
Framework Bridge boundaries, and architecture that cannot be implemented
without interpretation. It does not optimize for producing a PASS.

## 3. Scope

In scope: repository and commit identity verification; one authorized read-only
`git fetch clean-origin`; complete reading of the architecture specification and
its task report; targeted complete reading of the canonical cross-check
sources; independent construction of ownership, terminology, identifier,
lifecycle, authorization, envelope, bridge, context, memory, handoff, tool,
provider, routing, ledger, event, cancellation, retry, isolation, approval,
security, error, observability, and runtime-mode matrices; replay of the
original 32 scenarios and 10 additional adversarial scenarios; implementability
assessment for the next contract; documentation validators; one review record;
one review task report; bounded updates to four shared-context files; and one
local documentation commit.

Out of scope and not performed: any modification of the reviewed specification
or any canonical document; any remediation; any source or test change; any
drafting of the Agent Package Contract, Framework Bridge Contract, Shared
Context Bridge, or Agent Runtime Scaffold; any framework SDK installation,
import, connection, or execution; any agent execution; any model-provider call;
any tool execution; any provider access, authentication, or credential
handling; any MCP or integration-fabric connection; any dependency
installation; any push, pull request, merge, remote branch, or deployment; and
any MellyTrade interaction.

## 4. Starting repository state

| Item | Verified value |
| --- | --- |
| Working tree root | `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios` |
| Starting branch | `docs/mellycore-agent-runtime-architecture-spec-001` |
| Starting HEAD | `17da8603fbe8b75082cfea44223745b3c63f14de` |
| Parent | `95a31316b0c4871343637a6b414f4aaa79dee76d` |
| Subject | `docs: define agent runtime architecture` |
| Worktree / index at start | Clean (`git status --short --branch` returned only the branch line) |
| Canonical remote | `clean-origin` → `https://github.com/Melly-999/mellycore-aios-core.git` |
| Freshly verified `clean-origin/main` | `947f33d27d5546775186e96bdc61e30db78c0b3d` — matched the expected value; **no drift** |
| Review branch before creation | Absent locally; absent on `clean-origin` and `origin` |
| Review branch created | `docs/mellycore-agent-runtime-architecture-spec-review-001`, from `17da8603fbe8b75082cfea44223745b3c63f14de` |

Exactly one network operation occurred during this task: `git fetch
clean-origin` (exit code `0`), executed during the canonical remote gate. No
other network access of any kind occurred: no `origin` access, no pull, no
push, no GitHub API call, no provider endpoint, no model-provider endpoint, no
framework package download, no MCP or fabric connection, no telemetry, and no
deployment.

## 5. Reviewed commit

Commit `17da8603fbe8b75082cfea44223745b3c63f14de` — `docs: define agent runtime
architecture`, parent `95a31316b0c4871343637a6b414f4aaa79dee76d`. The commit
contains **exactly six paths**, independently confirmed by
`git show --pretty=format: --name-only`:

1. `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md`
2. `docs/tasks/MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001.md`
3. `shared_context/AGENT_HANDOFF.md`
4. `shared_context/PROJECT_STATE.md`
5. `shared_context/ROADMAP.md`
6. `shared_context/RUN_QUEUE.md`

No source file, test file, canonical provider document, or prior review record
is present in the commit.

## 6. Reviewed files

Read completely: the architecture specification (1,502 lines), its task report
(382 lines), and the four shared-context files at the reviewed commit.

## 7. Canonical cross-check sources

Read completely or by complete section, as relevant:

| Source | Sections independently read |
| --- | --- |
| `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` | §7.1 common entity contract; §7.2 entity catalogue; §7.3 relationship rules; §8.1 six-dimension enum contract; §8.2 orthogonality and rendering rules; §9.1–§9.7 module contracts; §19 failure and unknown states |
| `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md` | §21.1 eight independent facts; §21.2 rules; §21.3 authorization-record custody; §21.4 lifecycle and transition authority; §21.5 issuance and revocation |
| `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` | §17 policy-evaluation order; §25 error taxonomy; §26 retry and `INDETERMINATE` reconciliation; §32 seventeen-item runtime-enablement gate |
| `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` | §5 Unified Run Ledger, §5.1–§5.9 |
| `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md` | Fixture-entity and truthful-label scope |
| `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md` | Tenant isolation, identity/credential model, external-content posture |
| `docs/specs/MELLYCORE_INTEGRATION_FABRIC_COMPARISON_SPEC_001.md` | Fabric equivalence standard |
| `docs/architecture/MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001.md` | §4.8 Run Ledger; loop run/state relationship |
| `shared_context/SAFETY_CONTRACT.md` | Complete |
| `shared_context/VALIDATION.md` | Complete |
| `shared_context/MODEL_ROUTING.md` | Complete |
| `shared_context/CONTEXT_GRAPH_SCHEMA.md`, `CONTEXT_PACK_GENERATOR_SPEC.md` | Scope and relationship to admitted context |
| `docs/specs/MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001.md` | §5 sensitivity labels and `allowed_use` |
| `shared_context/loops/RUN_LEDGER_SCHEMA.json`, `LOOP_STATE_SCHEMA.json`, `LOOP_REGISTRY.json` | Loop run identity and ledger contract |
| `docs/research/MELLYCORE_CLOUDFLARE_API_SHIELD_READ_ONLY_ADAPTER_REVIEW_002.md` | `P2-03`, `P2-04`, `P3-01` |
| `docs/research/MELLYCORE_PROVIDER_ADAPTER_SCAFFOLD_REVIEW_001.md` | Inert-scaffold precedent and review-record convention |
| `shared_context/PROJECT_STATE.md`, `ROADMAP.md`, `RUN_QUEUE.md`, `AGENT_HANDOFF.md` | Current-state entries, task pointers, global pointer |

Repository-wide read-only searches were performed for every existing definition
of: agent, run, attempt, step, task, event, context packet, memory record,
approval, model routing, run ledger, agent status, cancellation, retry, replay,
runtime enablement, package verification, framework bridge, shared context, and
canonical state. The specification's own overlap matrix was **not** relied on;
it was used only as a claim to be checked.

## 8. Independent method

1. Repository identity gate (branch, HEAD, parent, subject, clean worktree and
   index, canonical remote) before any read of the artifact.
2. Canonical remote gate: one authorized `git fetch clean-origin`; fresh
   verification of `clean-origin/main`; re-verification that the local branch,
   HEAD, worktree, and index were unchanged; confirmation of the six-path
   commit scope; confirmation that no conflicting local or remote review branch
   existed.
3. Immutable baselines recorded as Git blob IDs before any edit (Section 9).
4. Review branch created from the reviewed commit, never from `clean-origin/main`.
5. Every numeric claim recounted directly from the specification text rather
   than accepted from the task report.
6. Ownership, terminology, identifier, lifecycle, authorization, envelope,
   bridge, context, memory, handoff, tool, provider, routing, cost, ledger,
   event, cancellation, retry, isolation, approval, security, error,
   observability, and runtime-mode matrices rebuilt independently and compared
   against the canonical owners.
7. Lifecycle graph reconstructed as an explicit adjacency list and tested for
   terminal closure, exits, unreachable required states, and reachability of
   every state each normative section demands.
8. All 32 original scenarios and 10 additional adversarial scenarios replayed
   against the reconstructed matrices.
9. Findings severity assigned strictly by the task's P0/P1/P2/P3 definitions;
   no finding repaired.
10. Post-edit re-verification that every reviewed document remained
    byte-identical to its recorded baseline.

## 9. Immutable baselines

Git blob IDs recorded at `17da8603fbe8b75082cfea44223745b3c63f14de` before any
edit. Every one was re-verified unchanged after the review commit (Section 52).

| Blob ID | Path |
| --- | --- |
| `0039230452b50c60e276feeec3ebda0e4e6042f7` | `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md` |
| `92c0cba76837c03bfd2557f9ca2957e566824de3` | `docs/tasks/MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001.md` |
| `35a2f8008b17d36214cc84b0334db7bb1cdc5aa5` | `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` |
| `fa90b65b4f91545550247d81fc181eb10cca942a` | `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md` |
| `65192fa157b57a2a46768ceca4660aed1584f649` | `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` |
| `f866546b466ee3ec045502b2d483968b5fb7ff7c` | `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` |
| `13fa511f6228d4f8f13295dbd857c7586a163333` | `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md` |
| `0d2768be8d9ae19b5a14ce1c61441550081113e3` | `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md` |
| `5febae25d2fb315072a35cbe556d02c709308f59` | `docs/specs/MELLYCORE_INTEGRATION_FABRIC_COMPARISON_SPEC_001.md` |
| `38c847d684e6d6f08f8b76ff482237b4c7685e37` | `docs/architecture/MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001.md` |
| `a70500a9909ee5bbe2bf60cdfe9e779fc47877a0` | `shared_context/SAFETY_CONTRACT.md` |
| `a4acf641d3cc1551ad1513bcc8ec0cc619be941b` | `shared_context/VALIDATION.md` |
| `b4441133b4529c1260de205b147d2c42b5063a5d` | `shared_context/MODEL_ROUTING.md` |
| `e8f8961f5c1a12275527cc05c83c432c9312d0d6` | `shared_context/CONTEXT_GRAPH_SCHEMA.md` |
| `373a9313dbec3d30f9673931ab74c742738e2adb` | `shared_context/CONTEXT_PACK_GENERATOR_SPEC.md` |
| `dbcbb87b90b1e4939c0ae96abff28784126ab23a` | `docs/research/MELLYCORE_CLOUDFLARE_API_SHIELD_READ_ONLY_ADAPTER_REVIEW_002.md` |
| `5af0e1010798a809fed7681daa59f3e2d80c3aa6` | `docs/research/MELLYCORE_PROVIDER_ADAPTER_SCAFFOLD_REVIEW_001.md` |

Shared-context baselines (these four are within the approved editable set and
were changed by this review):
`393ab347ecd56e555d00c65ee85cdfbac46a6707` `shared_context/PROJECT_STATE.md`;
`6c61331f3e147276011c0df3a5f30acc379280b3` `shared_context/ROADMAP.md`;
`d7cb797ea72e9ac376aba0c1c255968d596387b4` `shared_context/RUN_QUEUE.md`;
`a6231156ced987064374f3ad7eb8179c683d49eb` `shared_context/AGENT_HANDOFF.md`.

### 9.1 Independently recounted dimensions

| Dimension | Claimed | Independently counted | Result |
| --- | --- | --- | --- |
| Specification sections | 43 | 43 (§1–§43) | ✅ |
| Framework types | 6 | 6 | ✅ |
| Canonical identifiers | 15 | 15 (§8.1) | ✅ |
| Package/runtime separation states | 9 | 9 (§9) | ✅ |
| Run lifecycle states | 17 | 17 (§12.2) | ✅ |
| Terminal states | 5 | 5 (`completed`, `failed`, `cancelled`, `timed_out`, `blocked`) | ✅ |
| Waiting states | 4 | 4 | ✅ |
| Pending (non-terminal, non-waiting) states | 2 | 2 | ✅ |
| Authorization facts | 11 | 11 (§14) | ✅ |
| Execution-envelope field groups | 14 | 14 (§15.1) | ✅ |
| Framework Bridge operations | 9 | 9 (§16) | ✅ |
| Shared Context operations | 7 | 7 (§17.1) | ✅ |
| Memory categories | 6 | 6 (§18) | ✅ |
| Context-flow trace fields | 17 | **16** (§19) | ❌ P3-01 |
| Handoff kinds | 6 | 6 (§20.1) | ✅ |
| Handoff envelope contents | 11 (task report §14) | **12** (§20.2) | ❌ P3-02 |
| Tool-access stages | 7 | 7 (§21.1) | ✅ |
| Routing request dimensions | 8 | 8 (§23.2) | ✅ |
| Routing artifacts | 7 | 7 (§23.3) | ✅ |
| Ledger record kinds | 14 | 14 (§25) | ✅ |
| Event categories | 12 | 12 (§26.1) | ✅ |
| Isolation boundaries | 8 | 8 (§29.1) | ✅ |
| Race/conflict behaviors | 6 | 6 (§29.2) | ✅ |
| Human-approval triggers | 10 | 10 (§30.1) | ✅ |
| Security threats | 16 | 16 (§31) | ✅ |
| Error classes | 38 | 38 **rows**, **40 distinct class names** (§33) | ⚠ P3-03 |
| Operator views | 13 | 13 (§34) | ✅ |
| Framework compatibility matrix | 6 × 13 | 6 columns × 13 rows (§35) | ✅ |
| Runtime modes | 7 | 7 (§36) | ✅ |
| Deterministic scenarios | 32 | 32 (§38) | ✅ |
| Scenarios producing a reconciliation obligation | 5 | 5 (19, 20, 21, 23, 30) | ✅ |
| Documents assessed in the overlap matrix | 20 | 20 rows (task report §4) | ✅ |
| Cloudflare constraints carried forward | `P2-03`, `P2-04`, `P3-01` | 3, present at §8.3, §22.5, §33 | ✅ |

## 10. Ownership matrix

Independently constructed. Results use the required vocabulary: `CONSISTENT`,
`COMPLEMENTARY`, `AMBIGUOUS`, `CONFLICTING`, `UNOWNED`.

| # | Concern | Existing canonical owner | Runtime-spec claim | Result | Decision |
| --- | --- | --- | --- | --- | --- |
| 1 | Provider records | Registry §7, §21 | Reads; never registers or mutates (§7.3, §22.4) | `CONSISTENT` | Accept |
| 2 | Provider authorization | Registry §21.1 evaluated by Gateway §17 | Fact 10 delegates entirely (§14 rule 3, §22.4) | `CONSISTENT` | Accept |
| 3 | Provider execution | Gateway | Proposal only; single path (§22.1–22.3) | `CONSISTENT` | Accept |
| 4 | Model routing | Control Plane §9.2 + future Model Router | Requests, never decides (§23.1) | `CONSISTENT` | Accept |
| 5 | Run Ledger record definition | AI Operations Intelligence §5 | Producer only (§7.2, §25) | `CONFLICTING` | **P1-03** — attempt identity vs. §5.9 dedup by `run_id`; §5.1 one `outcome`/`model`/`provider` per run |
| 6 | Run identity form | AI Ops §5.1 (compatible with `shared_context/loops/RUN_LEDGER_SCHEMA.json`) | `run_id` assigned by Agent Runtime, opaque (§8.1, §8.2 rule 3) | `AMBIGUOUS` | **P2-03** |
| 7 | Approvals | Control Plane §16 + Gateway §18 | Enforces; never self-approves (§30.2) | `CONSISTENT` | Accept |
| 8 | Shared Context truth | `shared_context/**`, Context Gate, Control Plane §9.3 | Reads snapshots, proposes; never writes canonically (§17) | `CONSISTENT` | Accept |
| 9 | Memory persistence | This specification (categories); future Shared Context Bridge (mechanism) | Scopes and isolates (§18) | `COMPLEMENTARY` | Accept |
| 10 | Context provenance and sensitivity | Context Provenance and Sensitivity Spec §5; `context_provenance/**` | Reuses the canonical vocabulary explicitly (§17.2) | `CONSISTENT` | Accept |
| 11 | Task state and live sequencing | `RUN_QUEUE.md`, echoed in `AGENT_HANDOFF.md` | Consumer (§7.4) | `CONSISTENT` | Accept |
| 12 | Agent lifecycle / run status projection | Control Plane §8 (status vocabulary), §9.5, §9.7 | `run_state` typed field projecting to `lifecycle_status` (§12.1–12.2) | `CONFLICTING` | **P1-01** — six states project to `lifecycle_status:active`, which Control Plane §8.2 forbids for a running agent |
| 13 | Agent packages | Deferred — future Agent Package Contract | States required metadata only (§10) | `COMPLEMENTARY` | Accept |
| 14 | Framework bridges | Deferred — future Framework Bridge Contract | Fixes minimum operations and prohibitions (§16, §11.2) | `COMPLEMENTARY` | Accept |
| 15 | Runtime events | This specification (§26), consumed by Control Plane §9.5 | Producer and schema owner | `CONSISTENT` | Accept |
| 16 | Cost accounting | Control Plane §9.7 + AI Ops §5.2–5.3 | Emits estimates and actuals separately; never reconciles billing (§24) | `CONSISTENT` | Accept |
| 17 | Operator UI projections | Control Plane §9.4, §9.5, §9.7, §9.10 | Information architecture only (§34) | `CONSISTENT` except where it depends on concern 12 | Accept, contingent on **P1-01** |
| 18 | Tenant/capability authorization records | Registry §21.3 (`tenant_provider_authorization`, `tenant_capability_authorization`, both provider-scoped) | Runtime facts 5 and 6 (§14) | `CONFLICTING` / `UNOWNED` | **P1-02** |
| 19 | Runtime enablement (agent) vs. runtime enablement (provider) | Registry fact 7 (provider) | Runtime fact 7 (agent), separated by `RUNTIME_DISABLED` vs. `PROVIDER_DISABLED` (§33) | `CONSISTENT` | Accept — separation is explicit |
| 20 | Loop runs vs. agent runs | Loop Operations Architecture §4.8 + `shared_context/loops/**` | Not mentioned anywhere in the specification | `AMBIGUOUS` | **P2-03** (same root as concern 6) |

**Result: 3 `CONFLICTING` and 2 `AMBIGUOUS` ownership outcomes affecting
implementation.** The task report's claim of "0 blocking conflicts" is not
independently confirmed.

## 11. Terminology and entity review

- `run_state` is correctly declared a **typed entity field**, not a seventh
  status dimension (§12.1), consistent with Control Plane §7.1's rule that
  domain fields remain typed entity data. The field-qualified machine identity
  (`{field: "run_state", value: "blocked"}`) mirrors Control Plane §8.1's
  dimension-qualified pair. **Correct.**
- Label reuse across `lifecycle_status` and `run_state` is legitimate under
  Control Plane §8.1–8.2. **Correct.**
- **Projection is not deterministic-and-conforming.** Control Plane §8.2 states
  that `active` "is lifecycle-only and means an effective policy/configuration.
  It MUST NOT describe connectivity, **a running agent**, selected UI state, or
  general availability." The specification projects `starting`, `running`,
  `waiting_for_model`, `waiting_for_tool`, `waiting_for_agent`, and
  `cancellation_requested` to `lifecycle_status:active` — precisely the
  prohibited use. Independently, Control Plane §9.5 (Agent Traffic Inspector)
  and §9.7 (Unified Run Ledger) enumerate the Run-bearing lifecycle set as
  `planned`, `blocked`, `completed`, `failed`, `cancelled`, `historical` — which
  contains neither `active`, nor `queued`, nor `draft`, nor `ready`. See
  **P1-01**.
- Loop runs and agent runs: the specification never mentions loop runs. The
  distinction asserted in the task report §4 is **absent from the canonical
  artifact**. See **P2-03**.
- Task state and run state remain separate: `Task` (Control Plane §7.2) is not
  redefined, and §7.4 records `RUN_QUEUE.md` as owner. **Correct.**
- Approval entities: §30.2's scoped / time-bound / revision-bound /
  action-bound / auditable properties map cleanly onto Control Plane §7.2
  `Approval` (`target_type`, `target_id`, `target_version`, `target_digest`,
  `expires_at`, `authorized_actions`, `prohibited_actions`). **Correct.**
- `ContextPacket` and `MemoryRecord` are not redefined incompatibly; §17.2 and
  §18 add runtime-scoped access semantics without renaming or re-typing the
  Control Plane entities. **Correct.**

Entities reused unchanged: `Agent`, `Approval`, `Operator`, `SafetyPolicy`,
`Tool`, `ContextSource`, `ContextPacket`, `MemoryRecord`, `Task`, `CostRecord`,
`ValidatorResult`. Entities extended: `Run` (attempts, steps, sub-runs,
`run_state`), `RunEvent` (twelve categories, §26.2 properties). Entities newly
introduced: agent package, package revision, installed agent, runtime instance,
attempt, step, sub-run, handoff envelope, context snapshot, tool invocation,
model invocation, provider operation proposal, execution envelope, framework
bridge.

## 12. Identifier review

All fifteen §8.1 identifiers were checked against owner, tenant scope, revision
binding, uniqueness boundary, serialization, hashing, alias policy, and
lifecycle.

| Identifier | Owner | Tenant-scoped | Revision-bound | Result |
| --- | --- | --- | --- | --- |
| `agent_definition_id` | Agent Registry | Yes (§8.2 rule 2) | n/a | ✅ |
| `agent_package_id` | Package Store | Yes | n/a | ✅ |
| `package_revision_id` | Package Store | Yes | **Is** the revision; never reused or re-pointed | ✅ |
| `installed_agent_id` | Agent Registry | Yes | Binds one revision to one tenant+environment | ✅ |
| `runtime_instance_id` | Agent Runtime | Yes | n/a | ✅ but see **P2-05** |
| `run_id` | Agent Runtime | Yes | Carries `package_revision_id` (§8.2 rule 6) | ⚠ **P2-03** (form vs. AI Ops §5.1 / loop ledger) |
| `attempt_id` | Agent Runtime | Yes | Inherits run authorization | ✅ |
| `step_id` | Agent Runtime | Yes | Within one attempt | ✅ |
| `sub_run_id` | Agent Runtime | Yes | Also a `run_id`; explicit parentage | ✅ |
| `handoff_id` | Agent Runtime | Yes | Digest-bound (§20.2) | ✅ |
| `context_snapshot_id` | Shared Context Layer | Yes | Immutable, versioned (§17.3 rule 4) | ✅ |
| `tool_invocation_id` | Tool Gateway | Yes | Pinned tool contract revision (§21.1) | ✅ |
| `model_invocation_id` | Model Router | Yes | Bound to a routing decision | ✅ |
| `provider_operation_proposal_id` | Agent Runtime | Yes | Digest-bound (§22.3) | ✅ |
| `trace_id` | Agent Runtime | Yes | n/a | ✅ |

Rules verified: immutability; tenant-scoped resolution that **denies** rather
than returning empty; opacity (no encoding of mutable state, permissions,
sensitivity, model or provider names, or authorization outcomes); exact-match
lookup with prefix, suffix, case-insensitive, whitespace-tolerant,
Unicode-normalizing, similarity, and "nearest" resolution prohibited at every
trust boundary; no runtime aliases (display names and slugs never accepted in
an envelope, handoff, approval binding, ledger record, or audit record); and
revision preservation through every carrier. **All hold.**

## 13. Canonical serialization and digest review

Cloudflare Review 002 `P2-03` is carried forward correctly and, in this
reviewer's independent assessment, is the strongest part of the specification.

| Requirement | §8.3 rule | Verified |
| --- | --- | --- |
| Exact built-in primitive types only | 1 | ✅ — `type(value) is str`, not `isinstance`, with the analogous check for every primitive |
| Subclasses rejected or canonically converted **before** normalization, comparison, reference construction, or digest input; conversion explicit and recorded | 2 | ✅ |
| Serialization never calls `repr()`, `str()`, `__format__`, `__hash__`, `__eq__`, or any overridable protocol on an untrusted value | 3 | ✅ |
| Deterministic hashing over normalized bytes, SHA-256 or stronger | 4 | ✅ |
| Type-tagged fields so distinct inputs cannot serialize identically | 5 | ✅ |
| Canonical form total and unambiguous (key order, numeric form, string normalization, absent-vs-null, container framing) — one byte sequence per logical value and one logical value per byte sequence | 6 | ✅ |
| No identity from arbitrary representations, enumerated across fingerprints, context hashes, artifact refs, handoff envelopes, tool-result and model-response identities, audit records, replay records, provenance, dedup keys, cache keys, idempotency keys | 7 | ✅ |
| Digest collisions are security events with quarantine, `evidence_state:unknown`, and dependent-run blocking | 8 | ✅ |

No user-supplied hash becomes canonical evidence without validation: §19
requires `canonical_hash` to be computed under §8.3, and §31's forged-provenance
row requires provenance to be signed/verified evidence rather than a
self-asserted field. **No finding.** One editorial note is recorded as
**P3-05** (Python-specific phrasing inside a language-neutral architecture).

## 14. Package/runtime separation review

The nine §9 states are individually defined with an establishing authority and
an explicit "absence means" column, and the section closes with a prohibition
on any `ready` / `enabled` / `installed` / `ok` / `healthy` / `status: active`
field standing for two or more, on deriving a later state from an earlier one,
and on presenting them as a single progress bar.

Tested for accidental implication:

| Tested implication | Present anywhere? |
| --- | --- |
| Installation implied by verification | No — state 3 → 4 requires the Agent Registry |
| Registration implied by installation | No — state 4 → 5 requires a conforming current agent record |
| Runtime enablement implied by registration | No — state 6 requires explicit, recorded operator enablement |
| Run authorization implied by runtime enablement | No — §14 rule 2 states it explicitly |
| Activity implied by authorization | No — state 9 requires an accepted envelope and execution evidence |

**No finding.** One minor observation: §9's state 2 ("package artifact exists")
has no corresponding entry in the eleven authorization facts, and the
nine-state-to-eleven-fact mapping is never stated. This is deliberate rather
than contradictory (the two lists answer different questions), but it is
recorded as **P3-04** because a reader may expect a 1:1 correspondence.

## 15. Lifecycle-state review

All seventeen states reconstructed with entry preconditions, allowed
predecessors and successors, terminal and waiting classification, required
evidence, responsible actor, and reconciliation implications.

| `run_state` | Terminal | Waiting | Predecessors | Successors | Safe exit? |
| --- | --- | --- | --- | --- | --- |
| `proposed` | No | No | — (entry) | `validated`, `blocked` | ✅ |
| `validated` | No | No | `proposed` | `authorized`, `blocked` | ✅ |
| `authorized` | No | No | `validated` | `queued`, `blocked` | ✅ |
| `queued` | No | No | `authorized` | `starting`, `cancellation_requested`, `blocked`, `timed_out` | ✅ |
| `starting` | No | No | `queued` | `running`, `failed`, `cancellation_requested`, `blocked` | ✅ |
| `running` | No | No | `starting`, all four waiting states | 10 successors | ✅ |
| `waiting_for_model` | No | **Yes** | `running` | `running`, `cancellation_requested`, `reconciliation_required`, `failed`, `timed_out`, `blocked` | ✅ but see **P1-04** |
| `waiting_for_tool` | No | **Yes** | `running` | same six | ✅ |
| `waiting_for_agent` | No | **Yes** | `running` | same six | ✅ |
| `waiting_for_operator` | No | **Yes** | `running` | `running`, `cancellation_requested`, `failed`, `timed_out`, `blocked` | ✅ |
| `cancellation_requested` | No | Pending | `queued`, `starting`, `running`, all four waiting states | `cancelled`, `reconciliation_required`, `failed`, `completed` | ✅ |
| `reconciliation_required` | No | Pending | `running`, three waiting states, `cancellation_requested` | `completed`, `failed`, `cancelled`, `blocked` | ✅ |
| `completed` | **Yes** | — | `running`, `cancellation_requested`, `reconciliation_required` | none | n/a |
| `failed` | **Yes** | — | many | none | n/a |
| `cancelled` | **Yes** | — | `cancellation_requested`, `reconciliation_required` | none | n/a |
| `timed_out` | **Yes** | — | `queued`, `running`, all four waiting states | none | n/a |
| `blocked` | **Yes** | — | all non-terminal except `cancellation_requested` | none | n/a |

Verified: every non-terminal state has at least one safe exit; every terminal
state has zero successors; `reconciliation_required` cannot become terminal
without a recorded reconciliation outcome (§12.4 rule 6);
`cancellation_requested` is never treated as `cancelled` (§12.4 rule 4, §27.2
rule 3); `timed_out` is never used when an external outcome is unknown (§12.4
rule 5, §27.2 rule 4); `blocked` and `failed` are distinct in both meaning and
projection; the four waiting states do not imply continued external execution;
and every state is reachable from `proposed`.

## 16. Transition review

Transition evidence (§12.5) is complete and correct: `run_id`, `attempt_id`,
`from_state`, `to_state`, `reason_code`, `actor`, `observed_at`, `recorded_at`,
`evidence_refs`, `trace_id`, and the canonical digest of the transition input.
The `actor` vocabulary is closed to `runtime`, `operator`, `policy`,
`bridge_report`, `scheduler` and explicitly excludes `agent`, `model`, `tool`,
and `provider` — this correctly prevents an agent, a model output, a tool
result, or external content from asserting a transition (§12.4 rule 7).
`observed_at` and `recorded_at` are separate, never merged, and `observed_at`
is `null` rather than substituted when it cannot be established. **Correct.**

The nine forbidden transitions are each independently justified and none is
contradicted elsewhere. `cancellation_requested → completed` is correctly
permitted and correctly fenced ("never used to report a cancelled run as
successful").

**One defect.** §23.6 requires that an unresolved routing tie produce
`run_state:waiting_for_operator`, and §12.2 defines `waiting_for_model` as
"blocked on a **routing decision** or model response". The §12.3 table does not
permit `waiting_for_model → waiting_for_operator`. See **P1-04**.

Projection determinism into `lifecycle_status` is mechanically total (every
`run_state` has exactly one projection) but is not conforming to the canonical
owner — see **P1-01**.

## 17. Run / attempt / step / retry / replay review

| Requirement | Verified |
| --- | --- |
| One logical run may have multiple attempts | ✅ §13 |
| Attempts are append-only; a retry never overwrites the original attempt's states, events, evidence, or ledger records | ✅ §13 rule 1 — but see **P1-03** for the ledger-side contradiction |
| Attempt identity unique and monotonic; numbers never reused after failure | ✅ §13 rule 2 |
| Steps belong to exactly one attempt | ✅ §13 definition |
| Sub-runs have explicit parentage and their own authorization | ✅ §13, §15.1 `parent_run_id` / `sub_run_id` |
| Retry creates a new attempt under the same authorization; denied if the authorization expired, drifted, or was revoked | ✅ §13 rule 3 |
| Replay creates a distinct run | ✅ §13 rule 4 |
| Replay records changed inputs, models, tools, policies, plus `source_run_id`, `source_package_revision_id`, and a `replay_fidelity` of `exact` / `divergent` / `not_comparable` | ✅ §13 rule 4 |
| Replay never re-executes a consequential external operation | ✅ §13 rule 5 → `UNSAFE_RETRY_REFUSED` |
| A successful sub-step is not run completion | ✅ §13 rule 6, §12.4 rule 8 |
| Cost and provenance remain attributable | ✅ §24, §19 |
| Duplicate suppression does not collapse valid retries or replays | ⚠ Within the specification, yes (§28 keys on idempotency keys and handoff digests). **Against the canonical ledger owner, no** — AI Ops §5.9 dedups by `run_id`. See **P1-03** |

## 18. Authorization-fact review

| # | Fact | Stated owner | Evidence type | Scope | Expiry | Revision binding | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Agent defined | Agent Registry | Definition record | Tenant | Implicit | — | ✅ |
| 2 | Package verified | Future Package Contract | Integrity + provenance + declaration evidence | Revision | Implicit | Yes | ✅ |
| 3 | Package installed | Agent Registry | Installation record | Tenant + environment | Implicit | Yes | ✅ |
| 4 | Agent registered | Agent Registry | Conforming current agent record | Tenant | Implicit | Yes | ✅ |
| 5 | Tenant authorized | "Provider Registry custody / tenant policy" | Unstated | **Unstated** | Unstated | — | ❌ **P1-02** |
| 6 | Capability authorized | "Tenant-capability authorization record" | Registry §21.3 record type | **Unstated which capability vocabulary** | Per record | — | ❌ **P1-02** |
| 7 | Runtime enabled | Explicit runtime enablement | Recorded enablement | Tenant + environment | Per record | — | ✅ (separated from provider enablement by `RUNTIME_DISABLED` vs. `PROVIDER_DISABLED`) |
| 8 | Run authorized | Recorded run authorization | Authorization record | This exact run | Yes (`RUN_AUTHORIZATION_EXPIRED`) | Yes | ✅ |
| 9 | Tool authorized | Tool Gateway | Tenant/agent/tool authorization | Tool + revision | Per record | Yes | ✅ |
| 10 | Provider authorized | Registry §21.1 evaluated by Gateway §17 | Delegated entirely | Provider + capability + scope | Per record | — | ✅ |
| 11 | Operation approved | Operator | Digest-bound approval | One exact typed target | Yes | Yes | ✅ |

Verified: Registry's original eight remain exactly eight and unmodified; no
aggregate readiness boolean is permitted (§14 rule 1); no fact implies another
(§14 rule 2, with the four canonical non-implications spelled out); operation
approval is independent and per-operation (§14 rule 4); `authorization_status`
may be computed at evaluation time but never stored, cached past its inputs, or
written (§14 rule 5) — matching Registry §21.2 rule 5 exactly.

**Defect:** facts 5 and 6 are not independent of fact 10. Registry §21.3
defines both `tenant_provider_authorization` (fact 5) and
`tenant_capability_authorization` (fact 6) as **provider-scoped** records
requiring a `provider_id`, and fact 10 already delegates to all eight Registry
facts — which include those two. See **P1-02**.

## 19. Execution-envelope review

All fourteen §15.1 field groups reviewed. The envelope binds tenant,
environment, agent identity, package revision, bridge contract revision, run
and attempt, requested capability, model-routing request, context snapshots,
memory scope, tool scope, provider scope, budgets, cancellation and retry
policy, authorization and approval references, audit and trace identity, and
the expected output contract. **Every item the review required is present.**

| Requirement | Verified |
| --- | --- |
| Raw secrets and credentials prohibited | ✅ §15.2 — credentials, raw secrets, environment variables, provider tokens/keys/session IDs, OAuth grants or codes, account identifiers, connection strings, and complete sensitive context bodies |
| Sensitive context carried by reference and resolved at point of use, never inlined into an envelope, handoff, log, event payload, error message, or audit record | ✅ §15.2 |
| References cannot silently drift to another revision | ✅ §8.2 rule 6 + Scenario 31 |
| Envelope mutation after authorization prohibited | ✅ §15.3 |
| A changed envelope requires a new attempt and re-evaluation of Section 14 | ✅ §15.3 |
| Digest failure rejects rather than repairs | ✅ `ENVELOPE_INTEGRITY_FAILED` |
| Optional fields cannot weaken mandatory gates | ✅ §6 principle 3; nullable fields are `parent_run_id`, `sub_run_id`, `model_routing_decision_ref` only |
| Absent fields fail closed | ✅ §6 principle 3 |

**One under-specification:** `model_routing_decision_ref` is "nullable until
decided", yet §23.3 places routing requests at step scope (carrying `step_id`),
which exists only inside a started attempt, while §15.3 freezes the envelope at
attempt start and binds it with `envelope_digest`. See **P2-02**.

## 20. Framework Bridge review

All nine §16 operations are defined with a responsibility and an explicit
fail-closed behavior. Checked against the required minimum set:
framework-neutral invocation boundary (`prepare_invocation`,
`translate_envelope`, `start_execution`); lifecycle translation (§11.3 row 2);
model-call translation (row 4); tool-call translation (row 3); handoff
translation (row 5); state and memory limits (rows 7–9); streaming
normalization (row 8, `stream_events`); cancellation limitations (row 6,
`request_cancellation`); failure normalization (`normalize_failure`,
`normalize_result`); tracing requirements (§26.2 `source_identity` includes
`bridge`); direct-provider prohibition (row 10, §11.2 rule 2);
direct-credential prohibition (row 11, §11.2 rule 2). **All present.**

Bypass tests:

| Could a framework-native convenience feature… | Prevented by |
| --- | --- |
| bypass the Model Router | §11.2 rules 1 and 3 — a bridge never constructs a model client from its own configuration |
| bypass the Tool Gateway | §11.2 rule 1 + §21 ("Agents **never** invoke tools directly") |
| bypass the Integration Gateway | §11.2 rules 1–2 + §22.1 ("no other path, no fallback path, and no emergency path") |
| write canonical context directly | §11.2 rule 4 + §17 |
| persist canonical memory directly | §11.2 rule 6 + §18 rule 2 |
| self-authorize retries | §28 rule 3 + §12.4 rule 7 (`bridge_report` is an actor for reporting, not for transitioning on its own authority) |
| self-authorize additional agents | §20.3 rule 1 + §20.3 rule 6 (`DEPTH_LIMIT_EXCEEDED`) |

`report_unsupported_behavior` with "silence is not a capability claim" and
`BRIDGE_UNSUPPORTED_BEHAVIOR` / `BRIDGE_FAILURE_UNCLASSIFIED` correctly prevent
silent emulation or degradation. **No finding.**

## 21. Framework compatibility review

The 6 × 13 matrix (§35) is explicitly and repeatedly labelled an architectural
planning position rather than a verified capability test, in both §11.3 and
§35, with the additional statement that no framework was installed, imported,
connected, or executed and that no cell may be cited as evidence of a
framework's behavior. `RR` is used where the specification declines to assert
without evidence, and `U1` for persistence is explicitly clarified as "MellyCore
will not rely on framework-native persistence in v1 — not that the framework
lacks it."

**This reviewer treated the matrix as planning only and verified nothing about
any framework.** No framework SDK was installed, imported, connected, or
executed during this review. The matrix is honest about its own epistemic
status. **No finding.**

## 22. Shared Context review

The seven §17.1 operations are genuinely distinct in effect and in required
authority. `propose_update` (a reviewable artifact) and
`request_canonical_mutation` (entry to an approval path) are explicitly
separated, and neither mutates canonical state on its own.

| Requirement | Verified |
| --- | --- |
| Agents never write canonical state directly | ✅ §17 preamble, §18 categories 5–6 ("Never by an agent"), Scenario 9 |
| Canonical mutation has a separate authority | ✅ `request_canonical_mutation` → operator approval bound per Control Plane §16.1 |
| Stale snapshots detected | ✅ §17.3 rule 4, §29.2 — but the resolution branch is policy-conditioned; see **P2-01** |
| Concurrent proposals do not silently overwrite | ✅ §17.3 rule 3, §29.2, Scenario 26 → `waiting_for_operator` |
| Provenance survives transformations | ✅ §17.2 `source_provenance`, §17.3 rule 5 (sensitivity does not decay; derived context inherits the highest sensitivity unless an explicit recorded redaction lowers it) |
| Access is tenant- and sensitivity-scoped | ✅ §17.3 rule 2 (denial does not reveal existence), §17.2 `access_scope` + `sensitivity_level` from the canonical vocabulary |
| Unavailable context is never silently substituted | ✅ §17.3 rule 1, §19 ("A transfer with no trace record is not a transfer") |
| Context rejection is auditable | ✅ §19 `acceptance_state` / `rejection_reason`, §34 Context flow view |

`sensitivity_level` correctly reuses the canonical vocabulary from the Context
Provenance and Sensitivity Spec §5 (`public`, `internal`, `private`, `secret`,
`regulated_high_risk`) rather than inventing a parallel scale. **No finding
beyond P2-01.**

## 23. Memory review

| # | Category | Owner | Duration | Persist | Share | Canonical | Read authority | Write authority | Promotion | Expiry |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Immutable run context | Run | Run | Yes, as evidence | By reference only | No | Within run | None | — | Never |
| 2 | Short-term working memory | Attempt | Attempt | No | No | No | Within attempt | Within attempt | 2→3 explicit | At attempt end |
| 3 | Agent-local memory | (agent, tenant) | Retention policy | Yes, tenant-scoped | **No** | No | Agent + tenant | Agent + tenant | 3→4 explicit | On retention expiry |
| 4 | Shared derived memory | Tenant | Until invalidation | After acceptance | Within tenant | No | Authorized scope | No direct write; propose only | 4→5, 4→6 explicit | On invalidation |
| 5 | Canonical project context | Shared Context Layer | Indefinite | Yes | Yes | **Yes** | Within scope | **Never by an agent** | — | Superseded only |
| 6 | Operator-approved long-term memory | Operator | Indefinite | After approval | Within scope | No | Within scope | **Never by an agent** | — | Operator only |

Verified: existence is never permission (§18 rule 1); categories are never
conflated by any field, store, or API (rule 3); framework-native memory —
LangGraph checkpoints, CrewAI crew memory, AutoGen conversation history, OpenAI
Agents SDK session state, Claude Code session context — is **category 2 at
most**, bridge-local, never automatically canonical, never crossing a run
boundary without explicit normalized admission, and **never crossing a tenant
boundary at all** (rule 2); each promotion (2→3, 3→4, 4→5, 4→6) requires an
explicit, separately authorized step with its own evidence (rule 4).

Framework-native memory cannot become shared memory, canonical project state,
or operator-approved long-term memory automatically. **No finding.**

## 24. Context-flow trace review

§19 requires an immutable trace record on **every** context transfer — between
agents, between runs, into a handoff, or into a derived record — and states that
"a transfer with no trace record is not a transfer: the receiving side treats
untraced context as absent." That is the correct fail-closed posture.

Fields verified present: `source_agent_id`, `destination_agent_id`,
`source_run_id`, `source_step_id`, `context_class`, `source_reference`,
`canonical_hash`, `transformation_id`, `redaction_applied`,
`sensitivity_level`, `access_decision`, `acceptance_state`, `rejection_reason`,
`observed_at`, `recorded_at`, `trace_id` — **sixteen fields, not seventeen**
(**P3-01**). Every field the review required (source, destination, source run
and step, context class, source reference, canonical digest, transformation,
redaction, sensitivity, access decision, acceptance decision, timestamps, trace
identity) is present.

Rejected transfers remain auditable via `acceptance_state: rejected` plus
`rejection_reason`. Digest rules follow §8.3. Redaction is recorded as a
distinct field alongside `transformation_id`, so a redaction changes both the
resulting `canonical_hash` and the provenance record. Identical hashes do not
imply equivalent authorization: `access_decision` is evaluated at the point of
use per §17.3 rule 1. **No finding beyond the count.**

## 25. Handoff review

All six §20.1 kinds reviewed. §20.2 enumerates **twelve** required envelope
contents (the task report says eleven — **P3-02**).

| Requirement | Verified |
| --- | --- |
| Receipt is not acceptance | ✅ §20.3 rule 1 — "A handoff envelope has no effect until the receiving agent's runtime independently evaluates Section 14 for the receiving side" |
| Acceptance and rejection are explicit and recorded | ✅ §20.3 rule 1, Scenarios 11 and 12 |
| Recipient permissions never widened | ✅ §20.3 rule 2 — effective scope is the intersection; Scenario 13 |
| A sender cannot grant what it does not own | ✅ §20.3 rule 2 (intersection) + §10.2 rule 2 (declarations intersect downward) |
| Context references revision-bound | ✅ `context_snapshot_id` is immutable and versioned; §8.2 rule 6 carries `package_revision_id` through every handoff |
| Output contract explicit | ✅ `output_contract_ref` |
| Budget and deadline explicit | ✅ `budget`, `deadline`; §20.3 rule 5 — budget is carved from the parent, never created; children never exceed the parent |
| Duplicate handoffs deterministic | ✅ §20.3 rule 4 — identity is the canonical digest of source identity, recipient, purpose, scope, context refs, and output contract; a duplicate returns the recorded decision without re-execution (Scenario 24) |
| Cancellation propagates per declared policy | ✅ `cancellation_behavior` |
| Sub-agent delegation depth bounded | ✅ §20.3 rule 6 → `DEPTH_LIMIT_EXCEEDED` |
| Broadcast creates no implicit acceptance | ✅ §20.1 — "at most one may accept"; acceptance is still explicit under rule 1 |
| Handoff content untrusted | ✅ §20.3 rule 3, §32 rule 1, Scenario 18 |

**One gap:** concurrent acceptance of one `broadcast_proposal` by two eligible
recipients has no specified race behavior, although §29.2 specifies race
behavior for concurrent context proposals, shared derived records, duplicate
handoffs, competing approvals, and cancellation races. See **P2-04**.

## 26. Tool-access review

The seven §21.1 stages are separated with an explicit "what it does **not**
mean" column: discovered ≠ registered; registered ≠ authorized; capability
declared ≠ enabled; contract revision pinned ≠ current; authorized ≠ enabled;
runtime enabled ≠ approved; invocation approved ≠ executed.

Verified: tool arguments produced by an agent or a model are untrusted and
validated against the **pinned** contract revision under §8.3 type discipline
before dispatch (§21.2 rule 1); results are validated and classified for
external content before use, and then only as data (rule 2); an unknown,
deprecated, ambiguous, or unregistered tool denies with `TOOL_UNKNOWN` and is
**never redirected** to a similar tool (rule 3); a timeout or ambiguous result
from a consequential tool yields `EXTERNAL_OUTCOME_UNKNOWN` and
`reconciliation_required`, never a blind retry (rule 4). **No finding.**

## 27. Provider-access review

§22.1 fixes exactly one path — Agent → Agent Runtime → Provider Registry
resolution → Integration Gateway → accepted provider adapter → provider — with
"no other path, no fallback path, and no emergency path."

§22.2 prohibits the Agent Runtime from selecting credentials; reading,
requesting, deriving, caching, or forwarding provider secrets; executing a
provider-native fallback; inferring a provider authentication mode; bypassing
provider scope validation; re-implementing Gateway policy evaluation; and
presenting a proposal as an executed operation. §22.3 makes the agent's output a
**bounded, typed, digest-bound proposal carrying no credential and performing
nothing**, with the Gateway independently re-deriving every authorization input
from authoritative records rather than forwarding the runtime's claims.

No agent accesses provider credentials anywhere in the specification; Scenario 8
makes a direct credential request `SENSITIVE_VALUE_REJECTED` with a content-free
security event and no value echoed. **No finding.**

## 28. Model Router review

| Requirement | Verified |
| --- | --- |
| Runtime requests, never decides | ✅ §23.1 |
| Router produces a decision **and** an explanation | ✅ §23.3 — selected candidate, rejected alternatives with per-candidate reasons, applied rules and precedence, estimated cost and basis, confidence and basis, fallback route and trade-offs, override status |
| Model substitution governed | ✅ §23.3 substitution policy; §31 model-substitution row binds the decision digest |
| No silent fallback across sensitivity, provider, quality, cost, or approved-set boundaries | ✅ §23.4 — crossing any requires a new routing decision and, where policy demands, a new approval |
| No permitted model blocks | ✅ §23.5 `NO_PERMITTED_MODEL` + `blocked`; never "best available", never a silent downgrade, never unrouted execution |
| Unresolved ties deterministic | ✅ declared tie-breaker recorded in the explanation; otherwise `ROUTING_TIE_UNRESOLVED` + operator escalation — never random or arbitrary. **The resulting state is unreachable from `waiting_for_model`; see P1-04** |
| Operator override bounded and audited | ✅ §23.3 — exact, scoped, time-bound, auditable |
| Pricing uncertainty stays unknown | ✅ §24 rule 2 — `null` with an explicit state, never `0`, never inferred from a similar model |
| Runtime must not request a model by name as an authorization shortcut, and must not accept a model outside an authorized set | ✅ §23.2 |

Compatibility with existing routing documents: Control Plane §9.2's routing
precedence (safety → project restriction → approval requirement → privacy →
capability/quality → operator override → cost/latency → deterministic
tie-breaker) is consistent with §23.4 and §23.6. `shared_context/MODEL_ROUTING.md`
is human/agent tool-role guidance and an OmniRoute gateway note, not a runtime
Model Router contract; treating it as complementary is correct.
Control Plane §19's `NO ELIGIBLE ROUTE` is a presentation string, not a
competing error class. **No finding beyond P1-04.**

## 29. Cost and token review

Estimates, reservation, actuals, and reconciliation are four separate field
groups, separately sourced, and never merged (§24). Verified: an estimate is
never presentable as a confirmed cost; missing price is `null` with an explicit
`INSUFFICIENT_PRICING_DATA` state, never `0`, never silently omitted, never
inferred from a similar model; a budget over unknown pricing is unenforceable
and must be labelled so; pricing outside its validity window is
`freshness_state:expired` and blocks budget-dependent runs; an estimate
exceeding budget denies **before** execution (Scenario 16); and token semantics
reuse AI Ops §5.2 unchanged with no competing vocabulary.

This is consistent with AI Ops §5.2's rule that zero must not mean unknown and
that budget enforcement must report `unenforceable` rather than `pass`, and with
Control Plane §9.7's requirement that estimate and confirmed values never merge.

`INSUFFICIENT_PRICING_DATA` appears in no error taxonomy or canonical
vocabulary anywhere in the repository — recorded as **P3-04**.

## 30. Run Ledger review

The specification correctly declines to own the ledger record (§7.2, §25) and
positions the Agent Runtime as an append-only producer of fourteen record
kinds. Rules verified: append-only with corrections as new superseding records;
"the ledger is evidence, not necessarily canonical business state";
`operator_approved` is not authority (AI Ops §5.8); and ledger unavailability
blocks consequential work via `AUDIT_RESERVATION_FAILED`, consistent with
Gateway §29.

**Defect.** AI Ops §5.9 states "Duplicate run events (same `run_id`) are
deduplicated to one record", and §5.1's logical record carries one `outcome`,
one `model`, and one `provider` per `run_id`. The Agent Runtime introduces
multiple attempts under a single `run_id` and requires (§13 rule 1) that every
attempt's ledger records remain intact and addressable. The specification never
reconciles attempt identity with the owner's record identity or its dedup rule,
and, as a declared non-owner, cannot amend it. See **P1-03**.

Related: AI Ops §5.1 requires `run_id` to be "compatible with the existing
run-ledger `run_id` form", which `shared_context/loops/RUN_LEDGER_SCHEMA.json`
constrains by pattern; §8.1 assigns `run_id` to the Agent Runtime and §8.2 rule 3
requires opacity. See **P2-03**.

## 31. Runtime-event review

Twelve categories (§26.1). Every event carries `event_id`, `schema_version`,
`category`, `event_type`, a closed `source_identity` (`runtime`, `bridge`,
`router`, `tool_gateway`, `integration_gateway`, `operator`, `scheduler`),
`run_id`, `attempt_id`, nullable `step_id`, `trace_id`, `sequence`,
`observed_at`, `recorded_at`, `payload_summary_ref`, `redaction_state`, and
`canonical_digest`.

Verified: event types are versioned and a changed shape is a new version, never
a silent field change; no raw secrets in payloads, summaries, errors, or
references; `sequence` is monotonic per attempt and gaps are reported as
`evidence_state:partial` with the last confirmed sequence rather than rendered
as quiet — matching Control Plane §19's "missing traffic sequence" row and §9.5's
"no events is not quiet"; observed and recorded times remain distinct and are
never merged, substituted, or back-filled; and unmappable framework events are
emitted as `unmapped` with the bridge's raw category recorded as untrusted data
and never dropped. Ledger evidence is explicitly distinguished from canonical
business truth (§25 rule 2). **No finding.**

## 32. Cancellation and timeout review

The six §27.1 concepts are genuinely distinct: cancellation request,
cancellation acknowledgement, framework cancellation support (with
`constrained` and `unsupported` as legitimate values), external-effect
uncertainty, forced local stop, and reconciliation required.

Verified: a cancellation request is never recorded as `cancelled` on its own
strength; a forced local stop is recorded as exactly what it is and is never
proof that external effects stopped; `cancellation_requested → cancelled` is
permitted only when every in-flight external effect is confirmed not to have
occurred or confirmed reverted, otherwise the required transition is
`reconciliation_required`; a timeout with any unknown external outcome is
`reconciliation_required`, not `timed_out`; and the runtime never asserts a
cancellation guarantee a framework, tool, or provider cannot provide.

This matches the honest posture required and does not overclaim. **No finding.**

## 33. Retry and reconciliation review

The seven §28 concepts (safe retry, unsafe retry, idempotent operation, unknown
external result, duplicate suppression, attempt identity, reconciliation task)
are distinct and correctly defined. Verified: no consequential provider or tool
action is retried blindly, mirroring Gateway §26.2–26.3 without weakening it; on
an unknown outcome the required sequence is a fresh authoritative read, a
comparison against the approved after-state, success recorded **with
verification evidence** if applied, a **new proposal and new approval** if not
applied, and `PARTIAL_APPLICATION` with the exact partial state if partially
applied; a retry is never permission to repeat a consequential action, because
fact 11 is evaluated afresh for each consequential attempt; idempotency keys are
derived under §8.3 and never shared across tenants, runs, or intended actions;
and `reconciliation_required` is neither failure nor success but an open
obligation visible to operators until resolved. **No finding.**

## 34. Concurrency and isolation review

All eight §29.1 boundaries reviewed: tenant (absolute — no identifier, context,
memory, cache, budget, event, or error crosses, and cross-tenant resolution
denies without revealing existence), run, agent-local state, framework-process,
context namespace, memory namespace, tool session, provider session.

| Condition | Specified behavior | Result |
| --- | --- | --- |
| Concurrent runs | Runs share no mutable state; one run's failure never mutates another | ✅ |
| Same agent in multiple runs | Agent-local memory scoped to `(agent, tenant)`, never shared across agents; each run has its own namespaces | ✅ |
| Cross-tenant contamination | Denied at identifier resolution, context, memory, cache, budget, event, and error | ✅ |
| Stale context snapshots | Digest/version comparison; never silently refreshed | ⚠ **P2-01** (resolution branch policy-conditioned) |
| Concurrent context proposals | Both recorded, neither auto-applied, conflict surfaced with provenance and precedence | ✅ |
| Race on a shared derived record | Optimistic concurrency with expected-version precondition → `STALE_STATE`, never silent overwrite | ✅ |
| Duplicate handoffs | Suppressed by handoff digest; recorded decision returned | ✅ |
| Competing approvals | At most one effective per exact target binding; second rejected `APPROVAL_CONFLICT`; both audited | ✅ |
| Cancellation races | Completed-before-cancellation is honestly `completed` with the request recorded; unknown effect is `reconciliation_required` | ✅ |
| Shared framework process state | Framework-process isolation requires containment so global state, monkey-patching, or a crash cannot alter runtime decisions or another run's state; mechanism explicitly deferred (§41.3) | ✅ requirement fixed |
| Memory namespace collisions | Each run writes only within its `memory_namespace_id` | ✅ |
| Tool sessions | Never reused across runs or tenants | ✅ |
| Provider sessions | Gateway-owned, never shared across tenants; the runtime holds none | ✅ |
| Concurrent broadcast acceptance | **Unspecified** | ❌ **P2-04** |
| Runtime-instance restart with an attempt in an unknown state | **Unspecified** | ❌ **P2-05** |

No global mutable framework state may silently become trusted canonical state
(§11.2 rule 6, §18 rule 2, §29.1). **Correct.**

## 35. Human-approval review

§30.2 requires every operator approval to be scoped (exact allowed and
prohibited actions), time-bound (explicit expiry), revision-bound (exact
`package_revision_id`, `target_version`, `target_digest`), action-bound (one
exact typed target, never a class), and auditable (append-only record with
operator identity, decision, and rationale reference). Non-transferability and
non-replayability follow from the reuse, unchanged, of Control Plane §16.2 and
Gateway §18.3: no self-approval, no blanket approval, no inferred consent, no
approval replay, no hidden side effect, no autonomous safety-policy change, no
permission widening; and approval to prepare or approve a configuration does not
authorize execution. An approval bound to an older package revision does not
authorize a run on a newer one (Scenario 32).

All ten §30.1 triggers are present and each is independently justified. Agents
cannot approve their own consequential operations: `agent` is excluded from the
§12.5 actor vocabulary, §6 principle 9 makes the operator the only authority,
and no-self-approval is reused from the canonical owners. **No finding.**

## 36. Security-threat review

Sixteen rows (§31), each with prevention, detection, fail-closed result, and
audit obligation. Required coverage was checked item by item:

| Required threat | Present | Fail-closed class |
| --- | --- | --- |
| Prompt injection | ✅ | `INJECTION_SUSPECTED`; content stays data; no policy change |
| Tool-result injection | ✅ | `EXTERNAL_CONTENT_REJECTED` or quarantine |
| Agent-to-agent injection | ✅ (§32 rule 1 + Scenario 18) | `INJECTION_SUSPECTED` |
| Context poisoning | ✅ | Proposal rejected; dependent runs blocked |
| Malicious package | ✅ | `PACKAGE_UNVERIFIED` / `PACKAGE_MISMATCH` |
| Framework drift | ✅ | `CONTRACT_CONFLICT` |
| Model substitution | ✅ | `MODEL_UNAUTHORIZED` |
| Tenant confusion | ✅ | `TENANT_ISOLATION_VIOLATION`, denying without revealing existence |
| Credential exfiltration | ✅ | `SENSITIVE_VALUE_REJECTED`, never echoed |
| Excessive disclosure | ✅ | `CONTEXT_ACCESS_DENIED` |
| Unsafe retry | ✅ | `UNSAFE_RETRY_REFUSED` + `reconciliation_required` |
| Forged provenance | ✅ | `PROVENANCE_VERIFICATION_FAILED`, record quarantined |
| Digest collision | ✅ | `DIGEST_COLLISION_SUSPECTED`, both inputs quarantined |
| Malicious primitive subclass | ✅ | `INVALID_CANONICAL_TYPE`, no value echo |
| Arbitrary object representation | ✅ | `INVALID_CANONICAL_TYPE` |
| Cost exhaustion | ✅ | `BUDGET_EXCEEDED` before execution |
| Infinite loops | ✅ | `STEP_LIMIT_EXCEEDED` / `DEPTH_LIMIT_EXCEEDED` / `LOOP_DETECTED` |

**Exact count: 16 threat rows**, matching the claim; the required list of
seventeen concerns above is fully covered because agent-to-agent injection is
handled by the prompt-injection row plus §32 rule 1 rather than as a separate
row. Every audit obligation is content-free where content would be sensitive.
**No finding.**

## 37. External-content review

§32 makes all model output, tool results, provider responses, file content, web
content, and other agents' output untrusted until classified and validated, and
requires every untrusted payload to carry `content_origin`, `trust_state`,
`sensitivity_level`, `instruction_bearing_content`, `sanitization_applied`,
`transformation_id`, `validation_result`, and `acceptance_state`.

Verified: agent-to-agent content is external content with respect to the
receiving run; instruction-bearing content sets a flag and records a security
event but never changes policy, permissions, routing, budgets, or run state;
sanitization is recorded rather than assumed, and an untransformed payload stays
`untrusted`; quarantine is terminal for that payload, never re-submitted
automatically and never inlined into an error, event, or audit record; and
agent-generated code, prompts, plans, and tool arguments remain untrusted until
validated against their contracts. This is consistent with the ADR's
external-content posture and Gateway §28. **No finding.**

## 38. Error-taxonomy review

Gateway §25.2 classes are adopted unchanged for the provider boundary and are
not restated or fragmented — independently confirmed: `STALE_STATE`,
`CONTRACT_CONFLICT`, `APPROVAL_STALE`, `AUDIT_RESERVATION_FAILED`,
`PARTIAL_APPLICATION`, `INDETERMINATE`, and `INJECTION_SUSPECTED` all resolve to
the Gateway (or, for `INJECTION_SUSPECTED`, to Gateway §25 plus §31 here), so no
scenario cites an undefined class.

`P3-01` is correctly discharged: `INVALID_REFERENCE_SHAPE`,
`INVALID_CANONICAL_TYPE`, and `SENSITIVE_VALUE_REJECTED` are three distinct
classes and a structurally invalid reference is never reported as a
sensitive-data error.

Every class the review required to remain distinct is distinct: invalid
reference shape, invalid canonical type, sensitive value rejected, unsupported
framework, package mismatch, authorization denied, context denied, tool denied,
provider denied, runtime disabled, execution blocked, timeout, cancellation
incomplete, external outcome unknown, reconciliation required, and budget
exceeded. Outward classes are coarse while audit records carry the precise
inward `denial_reason`, failing evaluation step, and resolved facts. No error
message, event payload, summary, export, or audit record may contain a raw
sensitive value; rejection records the field path and class.

Counting note: the table has **38 rows** but **40 distinct class names**,
because one row carries `STEP_LIMIT_EXCEEDED` / `DEPTH_LIMIT_EXCEEDED` /
`LOOP_DETECTED` (**P3-03**).

## 39. Observability review

All thirteen §34 views expose truthful state and each carries an explicit "must
never imply" column that blocks exactly the wrong inference: active ≠ approved;
queued ≠ started; blocked ≠ failed; waiting ≠ progress; a graph edge ≠ accepted
work; context flow never exposes a body beyond its sensitivity; model
availability ≠ authorization; tool registration ≠ authorization; a provider
proposal ≠ an executed operation; an estimate ≠ a billing fact; errors never
carry a raw sensitive value; approval display ≠ authority; security events never
carry quarantined content. Every view carries the applicable canonical status
dimensions and an explicit source mode, and no view may synthesize a universal
"healthy", "active", or green state — matching Control Plane §8.2 and §9.

The section correctly defines no component, route, framework, or styling and
performs no frontend work. **The only defect is inherited:** the Active-runs and
Waiting-states views depend on the `lifecycle_status` projection challenged in
**P1-01**.

## 40. Runtime-mode review

Seven modes (§36), and the required distinctions map exactly:
`validation_only`, `dry_run`, `simulated`, `fixture_only`, `locally_executable`
(the canonical equivalent of "local"), `externally_connected`,
`production_enabled`. Each row states independently whether it reaches a
framework runtime, a model, a tool, and a provider.

Verified: v1 must distinguish all seven and collapsing any two is
non-conforming; the four inert modes must carry a persistent, non-dismissible
source-mode label and must not produce output, events, ledger records, or UI
states resembling live execution; a fixture result is never a provider request,
model response, or tool result and is labelled `evidence_state:static_demo`
everywhere it appears; mode is never inferred and an absent or unknown mode
denies with `EXECUTION_BLOCKED`; and `externally_connected` and
`production_enabled` require the Gateway §32 seventeen-item runtime-enablement
gate, **none of which currently passes**.

Fixture, simulation, and dry-run therefore cannot visually or semantically
resemble live execution. **No finding.**

## 41. Original 32-scenario replay

Each scenario was replayed independently against the reconstructed matrices.
"Resolves" means the outcome follows from the specification without
architectural interpretation.

| # | Facts / entities | Starting state | Decision | Resulting `run_state` | Reason class | Ledger event | Reconciliation | Operator | Resolves |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Fact 1 ✓, 2 ✗ | `validated` | Deny | `blocked` | `PACKAGE_UNVERIFIED` | Authorization decision | No | No | ✅ |
| 2 | Facts 2–3 ✓, 4 ✗ | `validated` | Deny | `blocked` | `AGENT_UNREGISTERED` | Authorization decision | No | No | ✅ |
| 3 | Facts 1–6 ✓, 7 ✗ | `validated` | Deny | `blocked` | `RUNTIME_DISABLED` | Authorization decision | No | No | ✅ |
| 4 | Facts 1–7 ✓, 8 ✗ | `validated` | Deny | `blocked` | `AUTHORIZATION_DENIED` | Authorization decision | No | No | ✅ |
| 5 | Facts 1–8 ✓; model outside set | `running` | Deny step | `blocked` | `MODEL_UNAUTHORIZED` | Routing request + rejected candidate | No | No | ✅ |
| 6 | Facts 1–8 ✓, 9 ✗ | `running` | Deny; no dispatch | `blocked` | `TOOL_DENIED` | Tool request + denial | No | No | ✅ |
| 7 | Facts 1–9 ✓, 10 ✗ | `running` | Deny; no provider request | `blocked` | `PROVIDER_DENIED` (Gateway class inward) | Proposal + Gateway decision | No | No | ✅ |
| 8 | Any | any | Deny; never satisfied | `blocked` | `SENSITIVE_VALUE_REJECTED` + security event | Content-free security event | No | No | ✅ |
| 9 | Any | `running` | Refuse write; no mutation | `running` | `CONTEXT_ACCESS_DENIED` | Access decision | No | No | ✅ |
| 10 | Produced class ✓, propose scope ✓ | `running` | Accept the proposal only | `running` | n/a | Proposal + provenance | No | No | ✅ |
| 11 | Recipient facts 1–8 ✓ | recipient `validated` | Accept explicitly | recipient `authorized` | n/a | Handoff + acceptance | No | No | ✅ |
| 12 | Recipient declines | source `running` | Reject explicitly | source `running`; no recipient run | recorded `rejection_reason` | Handoff + rejection | No | No | ✅ |
| 13 | Handoff grants scope recipient lacks | recipient `validated` | Deny; no widening | recipient `blocked` | `CONTEXT_ACCESS_DENIED` | Intersection result | No | No | ✅ |
| 14 | Candidate set empty after policy | `waiting_for_model` | Deny; no "best available" | `blocked` | `NO_PERMITTED_MODEL` | Request + all rejections | No | No | ✅ (transition permitted) |
| 15 | Tie, no declared tie-breaker | `waiting_for_model` | Escalate | `waiting_for_operator` | `ROUTING_TIE_UNRESOLVED` | Request + tied candidates | No | **Yes** | ❌ **P1-04** — transition not in §12.3 |
| 16 | Estimate > budget | `validated`/`authorized` | Deny before execution | `blocked` | `BUDGET_EXCEEDED` | Estimate + basis + budget | No | No | ✅ |
| 17 | Instruction-shaped tool result | `running` | Flag; keep as data | `running` | `INJECTION_SUSPECTED` → `EXTERNAL_CONTENT_REJECTED` | Security event + tool ref | No | No | ✅ |
| 18 | Agent-to-agent instructions | recipient `running` | Treat as data | `running` | `INJECTION_SUSPECTED` | Context trace + security event | No | No | ✅ |
| 19 | Cancel during model call, response unknown | `waiting_for_model` → `cancellation_requested` | Local stop; not `cancelled` | `reconciliation_required` | `CANCELLATION_INCOMPLETE` + `EXTERNAL_OUTCOME_UNKNOWN` | Cancellation request + ack + in-flight refs | **Yes** | Yes | ✅ |
| 20 | Cancel during consequential tool call | `waiting_for_tool` → `cancellation_requested` | Local stop | `reconciliation_required` | `CANCELLATION_INCOMPLETE` | Same + tool ref | **Yes** | Yes | ✅ |
| 21 | Timeout, effect unknown | `waiting_for_*` | Not `timed_out` | `reconciliation_required` | `EXTERNAL_OUTCOME_UNKNOWN` | Limit + elapsed + in-flight | **Yes** | Yes | ✅ |
| 22 | Idempotent, prior effect known absent | `running` | New attempt, same authorization | `running` | n/a | New `attempt_id`; original intact | No | No | ✅ |
| 23 | Consequential, outcome unknown | `running` | Refuse retry | `reconciliation_required` | `UNSAFE_RETRY_REFUSED` | Key state + prior attempt | **Yes** | Yes | ✅ |
| 24 | Identical handoff digest decided | unchanged | Return recorded decision | unchanged | n/a | Duplicate-suppression record | No | No | ✅ |
| 25 | Snapshot digest/version stale | `running` | Never silently refresh | `blocked` **or** re-read per policy | `STALE_STATE` (Gateway class) | Held vs. current digest | No | Possibly | ⚠ **P2-01** — branch selected by an undefined policy |
| 26 | Two contending proposals | `running` | Surface both; apply neither | `waiting_for_operator` | n/a | Both proposals + precedence | No | **Yes** | ✅ |
| 27 | `str` subclass at a digest boundary | `running` | Reject or convert before hashing | `blocked` | `INVALID_CANONICAL_TYPE` | Field path + class, no echo | No | No | ✅ |
| 28 | Digest collision | `running` | Quarantine both; block dependents | `blocked` | `DIGEST_COLLISION_SUSPECTED` | Both encodings by reference | No | Yes | ✅ |
| 29 | Provider auth mode unresolved (`P2-04`) | `running` | Deny; never infer a mode | `blocked` | `PROVIDER_DENIED` + `CONTRACT_CONFLICT` inward | Registry ref + unresolved-finding ref | No | Yes | ✅ |
| 30 | `CANCELLATION_UNSUPPORTED` | `cancellation_requested` | Forced local stop; no guarantee | `reconciliation_required` if in flight, else `cancelled` | `CANCELLATION_UNSUPPORTED` | Bridge report + in-flight inventory | **Yes, if in flight** | Yes | ✅ (condition is factual, not policy) |
| 31 | Authorized revision ≠ installed | `validated` | Deny; never silently upgrade | `blocked` | `PACKAGE_MISMATCH` | Both revision IDs and digests | No | Yes | ✅ |
| 32 | Approval binding ≠ current target | `validated` | Deny; fresh decision required | `blocked` | `APPROVAL_STALE` (Gateway class) | Full binding vs. current | No | **Yes** | ✅ |

**Result: 30 of 32 resolve deterministically. Scenario 15 does not (P1-04);
Scenario 25 is policy-conditioned with an undefined policy (P2-01).** The task
report's claim that "none requires architectural interpretation" is not
independently confirmed.

## 42. Additional scenario replay

| # | Scenario | Governing sections | Decision | Resulting state | Reason class | Reconciliation | Resolves |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 33 | Framework emits an unknown event type | §16 `stream_events`, §26.3 rule 5 | Emit explicit `unmapped` event with raw category as untrusted data; never drop | unchanged | n/a | No | ✅ |
| 34 | Framework writes native memory outside the bridge | §11.2 rules 1 and 6, §18 rule 2, §29.1 framework-process isolation | Contained as category 2 at most; bridge-local; never canonical, never cross-run without normalized admission, never cross-tenant; discarded at attempt end | unchanged | `BRIDGE_UNSUPPORTED_BEHAVIOR` if the behavior is required and unrepresentable | No | ✅ (mechanism deferred, requirement fixed) |
| 35 | Agent requests a model outside the approved provider set | §23.2, §23.4, §31 model substitution | Deny step; no model call | `blocked` | `MODEL_UNAUTHORIZED` | No | ✅ |
| 36 | Agent requests a provider operation while provider registration is unresolved | §22.5, Scenario 29, Registry fact 1 | Deny; never infer a mode; `P2-04` not discharged | `blocked` | `PROVIDER_DENIED` + `CONTRACT_CONFLICT` inward | No | ✅ |
| 37 | Handoff references a superseded package revision | §8.2 rule 6, §10.2 rule 4, §20.3 rule 1, Scenario 31 | Recipient re-evaluates facts 2–4 against the current installed revision; deny | recipient `blocked` | `PACKAGE_MISMATCH` | No | ✅ |
| 38 | Approval expires while a run waits in a queue | §6 principle 3, §14 rule 4, §30.2, §12.3 (`queued → blocked`) | Deny at dispatch; expired authority authorizes nothing | `blocked` | `RUN_AUTHORIZATION_EXPIRED` or `APPROVAL_REQUIRED` | No | ✅ (re-evaluation at dispatch follows from fail-closed principle 3, though it is not separately mandated) |
| 39 | Two agents propose conflicting canonical-state updates | §17.3 rule 3, §29.2, Scenario 26 | Record both; auto-apply neither; surface with provenance and precedence | `waiting_for_operator` | n/a — conflict recorded | No | ✅ |
| 40 | Duplicate model responses arrive out of order | §8.1 `model_invocation_id`, §26.3 rules 3–4, §28 duplicate suppression | Suppress the duplicate against the invocation identity; order by `sequence`; gaps as `evidence_state:partial` | unchanged | n/a | No | ✅ |
| 41 | Cancellation and completion race | §29.2 cancellation-race row, §12.3 (`cancellation_requested → completed`) | If the run finished first, honest terminal state is `completed` with the request recorded; if any effect unknown, `reconciliation_required` | `completed` or `reconciliation_required` | `CANCELLATION_INCOMPLETE` in the unknown branch | Conditional | ✅ (branch condition is factual) |
| 42 | Runtime restarts with an attempt in an unknown state | §8.1 `runtime_instance_id`, §12.5 durable append, §28, §41.3 deferral | Last durably appended state is authoritative; no rule requires the orphaned attempt to be resolved to `reconciliation_required` | **Undefined** | — | Should be **Yes**, unstated | ❌ **P2-05** |

**Result: 9 of 10 additional scenarios resolve; scenario 42 does not.**

## 43. Implementability review

Can `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001` be written without reopening
Agent Runtime architecture?

| Package concern | Fixed by the architecture? |
| --- | --- |
| Package identity | ✅ `agent_package_id`, `package_revision_id` (§8.1) |
| Manifest | ✅ §10.1 minimum metadata |
| Provenance | ✅ `package_provenance` (source, build, signer, digest, verification evidence) |
| Framework type | ✅ closed six-member vocabulary (§11.1) |
| Entrypoint reference | ✅ opaque, bridge-interpreted |
| Capabilities | ⚠ `declared_capabilities` is fixed as a declaration, but the authorization vocabulary it intersects with is ambiguous — see **P1-02** |
| Tools | ✅ `declared_tools` with exact identifiers and revisions |
| Context requirements | ✅ `required_context_classes` / `produced_context_classes` |
| Outputs | ✅ `output_contract_ref` (§15.1), `normalize_result` (§16) |
| Permissions | ⚠ `permission_requirements` intersect downward with tenant policy — the tenant-authorization record type is ambiguous (**P1-02**) |
| Model requirements | ✅ capability class, context window, modality, quality floor; never a model-name binding |
| Budgets | ✅ `resource_limits`, stricter-of-package-and-policy |
| Cancellation posture | ✅ `cancellation_support`, bridge-corroborated, defaulting to `constrained` |
| Sensitivity | ✅ `sensitivity_posture` from the canonical vocabulary |
| External-content posture | ✅ `external_content_posture` |

Two of fifteen package concerns cannot be specified without first resolving
**P1-02**. Additionally, a Package Contract author must know how a package
revision's runs will appear in the Run Ledger (**P1-03**) and in operator
lifecycle projections (**P1-01**), and the Framework Bridge Contract author must
know whether a bridge may observe a routing decision through the envelope
(**P2-02**) and how to translate a routing tie into a run state (**P1-04**).

**Conclusion: the downstream Agent Package Contract cannot be written entirely
without architectural interpretation.** Per the review's own rule, this is at
least P1.

## 44. Cloudflare constraints

| Finding | Status after this review |
| --- | --- |
| `P2-03` | **Correctly carried forward and materially strengthened** into §8.3's canonical serialization, exact-type, subclass, `repr()`-independence, normalized-byte hashing, type-tagging, no-arbitrary-representation, and collision-as-security-event rules, bound to run fingerprints, context-block hashes, artifact references, handoff envelopes, tool-result identities, model-response identities, audit records, and replay records, and exercised by Scenarios 27 and 28. **Not resolved here; not required to be.** |
| `P2-04` | **Correctly carried forward and explicitly not resolved.** §22.5 assumes no Cloudflare delegated authentication, treats no descriptor as registered or executable, binds no agent to a Cloudflare authentication mode, requires Registry and Gateway mediation and registration-time compatibility validation, and keeps live provider operations blocked. It names the exact gates that must not proceed until resolution or formal adjudication. **This review does not adjudicate it.** |
| `P3-01` | **Correctly discharged in structure** by distinct `INVALID_REFERENCE_SHAPE`, `INVALID_CANONICAL_TYPE`, and `SENSITIVE_VALUE_REJECTED` classes, with the explicit rule that structurally invalid input is never reported as a sensitive-data error. |

The specification does **not** treat the provider checkpoint as live-provider
readiness: §36 rule 5 requires the Gateway §32 seventeen-item gate, "none of
which currently passes", and §1.2 records every provider dimension as
`NOT_CONNECTED` / `NOT_CONFIGURED`. **Correct.**

## 45. New findings

### P0 — Critical

**None.** No direct credential or provider path, no cross-tenant execution
possibility, no canonical-context mutation bypass, no authorization or approval
bypass, no secret exposure, and no unsafe consequential retry was found.

### P1 — Blocking

**P1-01 — `lifecycle_status:active` projection contradicts the canonical status
owner.**
§12.2 projects six `run_state` values — `starting`, `running`,
`waiting_for_model`, `waiting_for_tool`, `waiting_for_agent`, and
`cancellation_requested` — to `lifecycle_status: active`. Control Plane §8.2
states that `active` "is lifecycle-only and means an effective
policy/configuration. It MUST NOT describe connectivity, **a running agent**,
selected UI state, or general availability." Independently, the two Control
Plane modules that render Runs — §9.5 Agent Traffic Inspector and §9.7 Unified
Run Ledger — enumerate the Run lifecycle set as `planned`, `blocked`,
`completed`, `failed`, `cancelled`, `historical`, which contains none of
`active`, `queued`, `draft`, or `ready`. The specification declares (§7.2) that
the runtime "must not own … the status vocabulary (Control Plane §8)" and (§34)
that it "extends Control Plane §9.4, §9.5, §9.7, and §9.10 without modifying
them", yet its projection table does both. §12.1's terminology reconciliation
addresses only label reuse across dimensions; it does not address the §8.2
prohibition or the module-level value sets.
*Impact:* an implementer building the Operator Console or the ledger projection
cannot render an agent run's `lifecycle_status` without either violating the
canonical owner or reinterpreting this specification. Ownership result:
`CONFLICTING`.
*Classification:* P1 — canonical ownership conflict.

**P1-02 — Authorization facts 5 and 6 duplicate Registry facts 5 and 6, and
their scope is undefined.**
§14 fact 5 is "Tenant authorized", owner "Provider Registry custody / tenant
policy"; fact 6 is "Capability authorized", owner "Tenant-capability
authorization record". Registry §21.3 defines exactly two authorization record
types — `tenant_provider_authorization` (Registry fact 5) and
`tenant_capability_authorization` (Registry fact 6) — and **both require a
`provider_id`**. Agent Runtime fact 10 already "delegates entirely" to all eight
Registry facts, which include those two.
Under the literal reading, facts 5 and 6 are re-implementations of provider
facts nested inside fact 10, contradicting §14 rule 3 ("the Agent Runtime never
re-implements … the eight provider facts") and rule 2 ("no fact implies
another"); a purely local agent run that touches no provider could not be
authorized at all, because no `provider_id` exists to bind the required records.
Under the alternative reading — that these are agent-scoped tenant and
capability authorizations — no canonical document defines such a record type,
the stated owner attribution is wrong, and the concern is `UNOWNED`. §14 also
does not state which capability vocabulary fact 6 evaluates: the agent's
`declared_capabilities` or a provider `capability_id` (§10.1 defines both, in
separate fields).
*Impact:* the Agent Package Contract cannot specify how `declared_capabilities`
and `permission_requirements` intersect downward (§10.2 rule 2) without
inventing the missing authorization scope.
*Classification:* P1 — ambiguous and duplicated authorization facts;
downstream contract requires architectural invention.

**P1-03 — Attempt evidence contradicts the canonical Run Ledger's record
identity and deduplication rule.**
§13 rule 1 requires that a retry never overwrite the original attempt and that
the original attempt's "states, events, evidence, **and ledger records** remain
intact and addressable", with §13 rule 2 requiring unique, monotonic, never
reused attempt identity. The canonical owner, AI Operations Intelligence §5,
which §7.2 and §25 explicitly forbid this specification from redefining, states
in §5.9 that "duplicate run events (same `run_id`) are deduplicated to one
record", and its §5.1 logical record carries exactly one `outcome`, one `model`,
and one `provider` per `run_id`. The Agent Runtime introduces multiple attempts,
multiple steps, and potentially multiple models under a single `run_id` and
never reconciles attempt identity with the owner's record identity, never states
that ledger records are keyed by `(run_id, attempt_id)`, and — as a declared
non-owner — cannot amend §5.9 itself.
*Impact:* an implementer must either violate AI Ops §5.9 or lose per-attempt
ledger evidence. The lost evidence is precisely the attempt-identity evidence
that §28 requires for reconciliation of unknown external outcomes, so this is an
audit-integrity defect, not merely a schema mismatch.
*Classification:* P1 — canonical ownership conflict; duplicate suppression
collapses valid retries.

**P1-04 — The lifecycle cannot express the routing-tie outcome it mandates.**
§23.6 requires that an unresolved routing tie produce `ROUTING_TIE_UNRESOLVED`
and `run_state:waiting_for_operator`, and Scenario 15 repeats that outcome.
§12.2 defines `waiting_for_model` as "blocked on a **routing decision** or model
response", so a run awaiting a routing decision is in `waiting_for_model`. The
§12.3 allowed-transition table permits `waiting_for_model` to reach only
`running`, `cancellation_requested`, `reconciliation_required`, `failed`,
`timed_out`, and `blocked` — **not** `waiting_for_operator`. (The comparable
outcome in §23.5, `NO_PERMITTED_MODEL` → `blocked`, *is* reachable, which
confirms the table was intended to cover routing outcomes.)
Two readings exist, and the specification chooses neither: if §12.3 is a closed
set, §23.6 and §12.3 directly contradict each other; if it is not closed, the
implementer must invent either a direct transition or an unstated
`waiting_for_model → running → waiting_for_operator` hop, and §12.4's forbidden
list gives no guidance.
*Impact:* a lifecycle transition required by a normative section and by a
"deterministic" scenario cannot be performed without interpretation.
*Classification:* P1 — lifecycle ambiguity.

### P2 — Material, non-blocking

**P2-01 — Stale-snapshot resolution is selected by an undefined policy.**
Scenario 25's expected state is "`blocked` **or** re-read per policy", and
§29.2 says the run "blocks or re-reads under policy". No section defines that
policy, requires it to be declared, or requires it to be deterministic —
unlike §23.6, which explicitly requires a *declared* tie-breaker and escalates
when none resolves. Both branches are fail-safe and the safety-critical
prohibition ("never silently refreshed") is unambiguous, so behavior remains
fail-closed; the branch selection can be constrained by the Shared Context
Bridge.

**P2-02 — `model_routing_decision_ref` cannot be populated inside an immutable
envelope.**
§15.1 places `model_routing_decision_ref` ("nullable until decided") in the
envelope, §15.3 freezes the envelope at attempt start and binds it with
`envelope_digest` (mismatch → `ENVELOPE_INTEGRITY_FAILED`, never repaired in
place), and §23.3 scopes routing requests to a `step_id`, which exists only
inside a started attempt (§13). A decision made after start therefore cannot
enter the envelope without either forcing a new `attempt_id` per model call —
which contradicts §13's model of multiple model turns as steps within one
attempt — or mutating a digest-bound structure. The specification does not state
whether the field is expected to remain `null` in the ordinary case, leaving
both `envelope_digest` coverage and the binding site of the routing decision
under-specified. Fail-closed (a changed envelope fails the digest), so
non-blocking; resolvable in the Framework Bridge Contract.

**P2-03 — Agent-run identity is not reconciled with the existing run-ledger
`run_id` form or with loop runs.**
AI Ops §5.1 requires `run_id` to be "compatible with the existing run-ledger
`run_id` form"; `shared_context/loops/RUN_LEDGER_SCHEMA.json` enforces
`^[a-z0-9][a-z0-9-]{0,63}--[0-9]{8}T[0-9]{6}Z--[0-9a-f]{12}$`, which encodes a
loop id and a timestamp. §8.1 assigns `run_id` to the Agent Runtime and §8.2
rule 3 requires identifiers to be opaque. The specification never references the
loop run ledger, never mentions loop runs at all, and never states how agent-run
identity and loop-run identity coexist in the Unified Run Ledger. The
distinction asserted in the architecture task report §4 ("loop runs are a
distinct, narrower concept; not renamed or absorbed") appears nowhere in the
canonical artifact.

**P2-04 — Concurrent acceptance of a broadcast handoff is unspecified.**
§20.1 requires that for a `broadcast_proposal` "at most one may accept", and
§20.3 rule 5 requires that the sum of children's budgets never exceed the
parent's remaining reserve. §29.2 specifies race behavior for concurrent context
proposals, shared derived records, duplicate handoffs, competing approvals, and
cancellation races, but not for two eligible recipients accepting one broadcast
concurrently. Each accepting run would still be independently authorized, so
there is no authorization bypass; the exposure is a violable budget invariant
and duplicated work.

**P2-05 — Runtime-instance failure or restart with an attempt in an unknown
state is unaddressed.**
`runtime_instance_id` exists (§8.1), §12.5 requires each transition to be
durably appended with separate `observed_at` and `recorded_at`, and §28 covers
unknown external outcomes — but no rule states what becomes of an attempt whose
owning runtime instance disappears, and §12.4 rule 7 ("only the runtime
transitions a run") does not say which instance. The safe outcome
(`reconciliation_required` whenever anything was in flight) is derivable but is
not normative. Partly mitigated by the explicit deferral of run persistence,
scheduling, and queue architecture (§41.3).

### P3 — Editorial / maintainability

**P3-01 —** §19's context-flow trace enumerates **16** fields; the dimension is
described elsewhere as a 17-field trace.

**P3-02 —** The architecture task report §14 states "eleven required envelope
contents (§20.2)"; §20.2 enumerates **twelve**.

**P3-03 —** §33 has **38 table rows** but **40 distinct class names**, because
one row carries `STEP_LIMIT_EXCEEDED` / `DEPTH_LIMIT_EXCEEDED` / `LOOP_DETECTED`.
The "38 error classes" claim counts rows.

**P3-04 —** `INSUFFICIENT_PRICING_DATA` (§24 rule 2) is used as a named state
but appears in no error taxonomy or canonical vocabulary anywhere in the
repository. Relatedly, §9's state 2 ("package artifact exists") has no
corresponding authorization fact and the nine-state-to-eleven-fact mapping is
never stated.

**P3-05 —** §8.3 rule 1 expresses the type discipline in Python-specific terms
(`type(value) is str` rather than `isinstance`) inside an otherwise
language-neutral architecture that must bind non-Python bridges.

## 46. Finding counts

| Severity | Count | IDs |
| --- | --- | --- |
| **P0** | **0** | — |
| **P1** | **4** | `P1-01`, `P1-02`, `P1-03`, `P1-04` |
| **P2** | **5** | `P2-01`, `P2-02`, `P2-03`, `P2-04`, `P2-05` |
| **P3** | **5** | `P3-01`, `P3-02`, `P3-03`, `P3-04`, `P3-05` |

## 47. Gate decision

### `FAIL_REMEDIATION_REQUIRED`

Four P1 findings exist. Per the gate rules, any P0 or P1 requires
`FAIL_REMEDIATION_REQUIRED`, and PASS is impossible with a P1 outstanding. The
specific gate conditions that are not met:

- **Canonical ownership is not unambiguous** — `P1-01` (status vocabulary),
  `P1-02` (tenant/capability authorization records), `P1-03` (Run Ledger record
  identity).
- **Lifecycle transitions require interpretation** — `P1-04`.
- **Authorization facts are not fully independent** — `P1-02`.
- **The downstream Agent Package Contract cannot be written without
  architectural interpretation** — `P1-02` directly, with `P1-01` and `P1-03`
  affecting how a package revision's runs are projected and recorded.
- **Not all 32 scenarios resolve deterministically** — Scenario 15 (`P1-04`)
  and Scenario 25 (`P2-01`).

This decision is narrow. The specification is strong across most of its
surface: the canonical serialization and digest discipline (§8.3), the
package/runtime separation (§9), the framework-bridge prohibitions (§11.2,
§16), the memory categories (§18), the handoff acceptance model (§20.3), the
single provider path (§22), the cancellation honesty model (§27), the retry and
reconciliation rules (§28), the isolation boundaries (§29), the approval
properties (§30), the security model (§31), the external-content posture (§32),
the runtime modes (§36), and the inert v1 boundary (§37) all pass independent
review without a finding. **No P0 exists**: no direct credential or provider
path, no cross-tenant execution possibility, no canonical-context mutation
bypass, no authorization or approval bypass, no secret exposure, and no unsafe
consequential retry was found. The four P1s are conflicts and gaps at the
seams — three against canonical owners and one internal to the lifecycle — not
defects in the safety model itself.

## 48. Agent Package eligibility

`MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001` is **not eligible** for
authorization. Downstream Agent Runtime documents — Agent Package Contract,
Framework Bridge Contract, Shared Context Bridge, Agent Runtime Scaffold, first
Agent Package, Cross-Agent Smoke, and Integration Review — **remain blocked**.

## 49. Implementation status

Nothing is implemented and nothing was implemented, connected, or executed by
this review. No Agent Runtime, agent registry, agent package, framework bridge,
or scaffold exists. No agent framework is installed, imported, connected, or
executed. Zero agents have been executed. No model provider is connected and no
model-provider call has occurred. No tool is connected or invoked. No provider
is connected, registered, authenticated, or enabled. No credential is
configured. No context or memory backend, queue, or frontend is implemented. No
deployment occurred. Agent Runtime implementation remains blocked.

## 50. Exact next task

`MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REMEDIATION-001`

A bounded documentation remediation of `P1-01`, `P1-02`, `P1-03`, and `P1-04`,
with `P2-01` through `P2-05` and `P3-01` through `P3-05` addressed or explicitly
adjudicated. It is not started, not authorized by this review, and not an
implementation task. `P1-01` and `P1-03` may require a companion amendment to
the canonical owner documents under those documents' own amendment rules rather
than a unilateral change to the Agent Runtime specification; that choice belongs
to the Operator, not to this review.

## 51. Explicit non-authorizations

This review authorizes none of: Agent Runtime implementation; framework bridge
implementation; Agent Package Contract, Framework Bridge Contract, or Shared
Context Bridge drafting; Agent Runtime Scaffold work; agent framework SDK
installation, vendoring, or dependency declaration; execution of any agent,
sub-agent, workflow, graph, crew, or conversation; any model-provider API call;
any tool invocation; any provider connection, authentication, credential
configuration or verification, OAuth flow, or token creation; any MCP or
integration-fabric connection or webhook registration; persistence, database, or
queue implementation; backend or frontend implementation; dependency
installation, workflow YAML, release, or deployment; any push, pull request,
merge, or remote branch; or any MellyTrade interaction.

Live provider work remains blocked and unauthorized. Migration triggers #1, #4,
#5, #6, and #7 remain uncrossed by this review. The global higher-priority
pointer `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` is unchanged, not
reordered, and not reinterpreted.

## 52. Validation evidence

| Check | Result |
| --- | --- |
| `py -3.9 scripts/validate_project_state.py` | Result and exit code recorded in the final execution report |
| `git diff --check` | Recorded in the final execution report |
| `git status --short`, `git diff --name-only`, `git diff --stat` | Recorded in the final execution report |
| Files changed | Exactly six, all within the approved allowlist |
| Architecture specification byte-identical | ✅ blob `0039230452b50c60e276feeec3ebda0e4e6042f7` unchanged |
| Architecture task report byte-identical | ✅ blob `92c0cba76837c03bfd2557f9ca2957e566824de3` unchanged |
| All canonical cross-check documents byte-identical | ✅ all 15 baseline blobs in Section 9 unchanged |
| Source or test files changed | **None** |
| Review record sections | 54 |
| Reviewed documents | 6 reviewed + 17 canonical cross-check sources |
| Ownership matrix results | 20 rows: 13 `CONSISTENT`, 2 `COMPLEMENTARY`, 2 `AMBIGUOUS`, 3 `CONFLICTING` |
| Lifecycle states accounted for | 17 of 17 |
| Authorization facts accounted for | 11 of 11 |
| Frameworks reviewed | 6 of 6 |
| Original scenarios replayed | 32 of 32 |
| Additional scenarios replayed | 10 of 10 |
| Finding counts | P0 = 0, P1 = 4, P2 = 5, P3 = 5 |
| Introduced secret-pattern count | 0 |
| `pytest` | `NOT_RUN` |
| Reason tests were not applicable | This review changes no source or test file and introduces no executable behavior. The existing suite is unaffected by a documentation-only change and would produce no evidence about it. Reported as `NOT_RUN`, never as passing |
| Unavailable validators | Black, flake8, and mypy were not run and are not claimed passing. No dependency was installed |

Every P0/P1 blocks the gate; PASS is impossible with a P1 outstanding; the gate
decision matches the finding counts; the shared-context next task matches the
gate; the Agent Package eligibility wording matches the gate; implementation
remains blocked; live provider work remains blocked; and the global pointer is
unchanged.

## 53. Amendment and supersession

This review record is amended only by an explicit, Operator-approved successor
review that names it and states exactly what changes. Superseded content is
retained and marked, never deleted. A future remediation task does not amend
this record; it produces its own record, and a subsequent independent review
decides the gate afresh.

## 54. References

### 54.1 Reviewed

- `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md`
- `docs/tasks/MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001.md`

### 54.2 Canonical cross-check sources

- `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md`
- `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`
- `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`
- `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md`
- `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md`
- `docs/specs/MELLYCORE_INTEGRATION_FABRIC_COMPARISON_SPEC_001.md`
- `docs/specs/MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001.md`
- `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md`
- `docs/architecture/MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001.md`
- `docs/research/MELLYCORE_CLOUDFLARE_API_SHIELD_READ_ONLY_ADAPTER_REVIEW_002.md`
- `docs/research/MELLYCORE_PROVIDER_ADAPTER_SCAFFOLD_REVIEW_001.md`
- `shared_context/SAFETY_CONTRACT.md`, `PROJECT_STATE.md`, `ROADMAP.md`,
  `RUN_QUEUE.md`, `AGENT_HANDOFF.md`, `VALIDATION.md`, `MODEL_ROUTING.md`,
  `CONTEXT_GRAPH_SCHEMA.md`, `CONTEXT_PACK_GENERATOR_SPEC.md`
- `shared_context/loops/RUN_LEDGER_SCHEMA.json`, `LOOP_STATE_SCHEMA.json`,
  `LOOP_REGISTRY.json`

### 54.3 External

None. No external source was fetched. No framework documentation, SDK, or
service was consulted, installed, or contacted during this review. The only
network operation was one authorized read-only `git fetch clean-origin`.
