# MellyCore Framework Bridge Contract Spec 001 — Task Report

## 1. Task identity and baseline

- Task ID: `MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001`
- Root: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios`
- Starting branch: `docs/mellycore-agent-package-contract-spec-review-002`
- Starting HEAD: `7fa3d8ad2d319312cc7785c4b4ef9f89a5a04776` (short `7fa3d8a`)
- Latest subject at start: `docs: review remediated agent package contract`
- Starting worktree/index: clean (`git status --short` empty)
- Upstream tracking at start: **none**
- Configured remotes: `origin`, `clean-origin` — **neither contacted**
- Branch created from `7fa3d8a`:
  `docs/mellycore-framework-bridge-contract-spec-001` (did not previously exist)

**No network operation occurred at any point in this task.**

### 1.1 Canonical task identity — minting record

At the time of the preceding run, `shared_context/RUN_QUEUE.md` and
`shared_context/TASK_INDEX.md` referred to this work only as the plain English
name **"Framework Bridge Contract"**, with **no task identifier anywhere in the
repository**. An exhaustive search for `MELLYCORE[-_]…BRIDGE…` and
`…FRAMEWORK[-_]BRIDGE…` identifier patterns across all tracked files returned
**zero matches**. That run therefore stopped before mutation and reported
`STOPPED_CANONICAL_TASK_IDENTITY_MISSING`, per the repository convention —
already evidenced by Agent Runtime §40 and Agent Package Contract §26 — that a
task identifier is minted **at the moment of Operator authorization**, not in
advance.

**Operator authorization was subsequently given explicitly**, minting and
recording the canonical identifier:

| Item | Authorized value |
| --- | --- |
| Task ID | `MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001` |
| Specification | `docs/specs/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001.md` |
| Task report | `docs/tasks/MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001.md` |
| Branch | `docs/mellycore-framework-bridge-contract-spec-001` |
| Commit subject | `docs: define agent framework bridge contract` |

The identifier follows the established convention triple confirmed against two
existing tracks (`AGENT_PACKAGE_CONTRACT_SPEC_001`,
`AGENT_RUNTIME_ARCHITECTURE_SPEC_001`): underscored spec path, hyphenated task
report path, lowercase hyphenated branch.

### 1.2 Identity gate result

Re-run fresh before mutation. Every required baseline matched: repository root;
branch; short HEAD `7fa3d8a`; subject; clean worktree; no upstream tracking;
Review 002 recording `PASS_WITH_NON_BLOCKING_FINDINGS`; Agent Package Contract
documentation-only; Framework Bridge Contract the exact next queued item; no
downstream implementation task active; target branch and both target files
absent.

## 2. Environmental Git-scope protection

`C:\` is itself a separate Git repository with unrelated uncommitted changes.
**Every** Git command in this task was explicitly scoped:

```
git -C "C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios" …
```

No unscoped Git command was run from `C:\`, `C:\Users\highe`, or any parent
directory. The outer `C:\` repository was never inspected, staged, reset,
cleaned, committed, or otherwise touched.

## 3. Files created

| Path | Role |
| --- | --- |
| `docs/specs/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001.md` | The Framework Bridge Contract specification, version 1.0, 39 sections |
| `docs/tasks/MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001.md` | This task report |

## 4. Files updated (bounded state synchronization)

`shared_context/PROJECT_STATE.md`, `ROADMAP.md`, `RUN_QUEUE.md`,
`AGENT_HANDOFF.md`, `PROJECT_HISTORY.md`, `TASK_INDEX.md`.

### 4.1 Changed-file allowlist (exactly eight)

1. `docs/specs/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001.md` (new)
2. `docs/tasks/MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001.md` (new)
3. `shared_context/PROJECT_STATE.md`
4. `shared_context/ROADMAP.md`
5. `shared_context/RUN_QUEUE.md`
6. `shared_context/AGENT_HANDOFF.md`
7. `shared_context/PROJECT_HISTORY.md`
8. `shared_context/TASK_INDEX.md`

**Not edited:** the Agent Package Contract specification; its task report; its
Review 001, Remediation 001, or Review 002 artifacts; the Agent Runtime
architecture; Control Plane; Provider Registry; Integration Gateway; AI
Operations Intelligence; Operations Data Contract; the seam-decision record;
the Enterprise Provider ADR; Shared Context contracts; the Safety Contract; any
source file; any test file; any configuration file; any workflow YAML; any
`.env` file.

## 5. Canonical owner documents consulted

| Path | Consulted for |
| --- | --- |
| `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md` | §11.1 closed framework set; §11.2 six normative bridge rules; §11.3 per-framework integration boundaries; §16 the nine bridge operations and fail-closed outcomes; §12 runtime lifecycle and `run_state`; §14 eleven authorization facts; §17 Shared Context access; §18 memory; §23 model routing; §26 events; §27 cancellation; §31–§32 security and external content; §33 error taxonomy (55 classes); §35 framework compatibility matrix; §36 runtime modes; §40 implementation sequence |
| `docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md` | §4 terminology; §10.1 five capability states; §11.1 permission categories; §13 provider-agnostic compatibility; §14/§14.1 asset types and command boundary; §17 package lifecycle; §19 trust; §23 batch; §24 threats; §26 follow-up contracts |
| `docs/research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_002.md` | The three open P2 findings and their exact scope |
| `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` | §7.1 common entity contract and typed-domain-field allowance; §8.1 six status dimensions; §9.2 Model Router control surface |
| `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md` | §21.1 eight provider-authorization facts; §24 MCP server registration and defaults |
| `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` | §12.1 one capability/one bounded operation; §17 policy order; §18 approval binding; §21 MCP security; §25.3 error-taxonomy pattern |
| `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` | §5 Run Ledger record identity for cost attribution |
| `docs/decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001.md` | Precedent for one-directional projection and additive owner amendment |
| `shared_context/MODEL_ROUTING.md` | Model Router / routing-policy ownership |
| `shared_context/CONTEXT_GRAPH_SCHEMA.md` | Shared Context admission and `source_refs` provenance |
| `shared_context/SAFETY_CONTRACT.md` | Safety boundary, unweakened |
| `shared_context/RUN_QUEUE.md`, `TASK_INDEX.md` | Canonical sequencing and task identity |

**No existing framework-adapter, bridge, or projection specification was found**
— confirmed by exhaustive search. `scripts/provider_adapters/` contains
**provider** adapters from `MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-001`, a
distinct concept the specification disambiguates from Framework Adapters at
§2 and §16.2.

## 6. P2 dependency-gate matrix

Performed against a baseline verified byte-identical to the run in which it was
first computed (HEAD `7fa3d8a`, clean worktree, all owner blob IDs unchanged).

| Finding | Does Framework Bridge depend on it? | Why | Safely deferrable? | Required handling |
| --- | --- | --- | --- | --- |
| `NEW-P2-01` — §20.1 of the Agent Package Contract defines no package-lifecycle rendering field, though its §16 stage 7 and §17.1 both direct implementers there | **No** | The bridge requires only *framework-session*, *adapter*, and *bridge-evaluation* lifecycles, all bridge-owned. Canonical package lifecycle is referenced read-only and never rendered by a bridge. | **Yes** | Spec §20.4 states explicitly that this contract defines no such field, that no normative rule depends on one, that adapters MUST NOT render or infer canonical package lifecycle, and that future contracts needing it MUST wait for the Agent Package Contract owner's correction |
| `NEW-P2-02` — the Agent Package Contract identifies itself as v1.1 while its §22 still declares the current contract version `1.0`, and v1.1 added mandatory rejection rules | **No** | An adapter declares a *supported package-contract range* (§6.1 field 6). It never needs to assert which value is canonically current. | **Yes** | Spec §6.3 declares the four version axes independent, fixes the bridge-contract version at 1.0, states the package-contract current version is **disputed and unresolved**, and declares **no value** as canonically current. Neither 1.0 nor 1.1 is asserted as the package contract's current version anywhere |
| `NEW-P2-03` — protected command classes (safety, validation, approval, Git, provider, deployment) have no canonical, deterministically enumerable owner list | **No** | Spec §14.1 forbids the bridge from activating commands, owning namespaces, resolving collisions, or overriding reserved commands. It therefore never needs to evaluate a protected class. | **Yes** | Spec §14.2 rule 3 states this contract defines and enumerates **no** protected command classes, MUST NOT translate or act on one, and that no normative rule depends on one. Full ownership deferred to the future Command Registry (rule 4) |

**Gate result: PASS.** The Framework Bridge Contract is **independent of all
three open P2 findings**. Each is recorded as a deferred dependency at spec
§36 items 1–3. No P2 was silently repaired, worked around, or resolved by this
task, and no remediation task identifier was invented.

## 7. Architectural ownership model

The specification's §3 assigns exactly one owner per concern. This contract
**owns** only: framework-neutral projection semantics; the adapter declared
boundary and metadata; the projection-loss taxonomy; the bridge validation
layers; and the per-framework projection profiles.

It **consumes without redefining**: the nine bridge operations and their
fail-closed outcomes (Runtime §16); the six normative bridge rules (Runtime
§11.2); the closed six-member `framework_type` set (Runtime §11.1); agent and
run identity, `run_state`, the execution envelope, and the eleven authorization
facts (Runtime §8, §12, §14, §15); the Runtime error taxonomy (§33); all Agent
Package concepts; Model Router decisions; Provider Registry facts and MCP
records; Gateway capability resolution, policy order, and approval binding;
Shared Context canonical truth; and Control Plane's six status dimensions.

Precedence (spec §3.1) places this contract **below** the Agent Runtime
architecture and **beside** the Agent Package Contract, stricter-only in both
directions, never subtractive.

## 8. Canonical-versus-projected decisions

Spec §4 fixes the direction rule — canonical contract → framework-neutral bridge
semantics → framework-specific adapter projection — and forbids the inverse.
Five rules follow: projection is one-directional; a framework requirement is
never a canonical justification; framework-native state is bridge-local;
no framework may redefine any of thirteen enumerated canonical concepts; and
round-trip is not identity. §4.3 gives an eleven-row register in which **no**
projected form is authoritative.

## 9. Framework profiles defined

Six, matching Runtime §11.1's closed set exactly: `claude_code` (§28),
`openai_agents_sdk` (§29), `langgraph` (§30), `crewai` (§31), `autogen` (§32),
`mellycore_custom` (§33).

**Identifier fidelity note.** The canonical sixth member is **`mellycore_custom`**,
per Runtime §11.1. Spec §5.2 rule 3 records that where planning language refers
informally to "custom agents", the canonical value remains `mellycore_custom`,
that no alias is introduced, and that `custom` alone is not a valid
`framework_type`. **No seventh identifier was introduced.**

**Honest limitation (spec §27.2).** Runtime §11.3 and §35 state that every
per-framework cell "MUST be independently validated by the future Framework
Bridge Contract task." **This task cannot discharge that obligation**, because
empirical validation requires installing and executing each framework, which
this authorization forbids. The specification therefore records those cells as
**unvalidated planning positions**, defines the validation obligation, and
assigns it to each future per-framework adapter specification, which MUST
validate its own framework's cells with recorded evidence before any adapter is
implemented. No profile upgrades, confirms, or weakens any Runtime §35 cell.

## 10. Projection boundaries defined

| Boundary | Spec section | Core rule |
| --- | --- | --- |
| Capability | §9 | Six separated states (declared / framework-supported / runtime-supported / policy-allowed / Operator-approved / active); intersection never union; **a framework's ability to act is not MellyCore authorization** |
| Permission and approval | §10 | Thirteen categories, all default DENY; **framework defaults MUST NOT override deny-by-default**; permission flattening prohibited; approval binds package revision + adapter revision + tenant + environment + capability |
| Prompt and instruction | §11 | Five-level precedence with Safety Contract highest and framework-native default lowest; framework-native instruction sources acquire no authority from being auto-loaded |
| Tool | §12 | Framework tool call → runtime tool proposal; **availability ≠ authorization**; substitution fails closed |
| Skills | §13 | Declaration-only projection; registry semantics deferred |
| Commands | §14 | Bridge MUST NOT activate, own namespaces, resolve collisions, or override reserved commands; **no protected command classes defined** |
| Hooks | §15 | Declaration-only; inert until authorized; unguaranteed ordering must be declared, not emulated; no auto-activation |
| Plugin | §16 | Metadata only; adapter-vs-plugin distinction fixed; availability ≠ approval; no auto-loading |
| MCP | §17 | Reference only; transport-neutral; no credential material; **no automatic connection, no implicit tunnel** |
| Shared Context | §18 | Read bounded by declared classes; **writes proposal-only**; namespace isolation; provenance retained; return-path re-validation mandatory |
| Memory | §19 | Five separated scopes; framework memory MUST NOT silently become canonical |

## 11. Runtime and routing boundaries

**Runtime (spec §21).** Eleven distinct stages — package discovery; package
validation; bridge compatibility evaluation; adapter selection; policy
evaluation; instantiation eligibility; activation gating; run creation;
observation; suspension; termination. The bridge participates in stages 3 and 9
and is consumed at every other stage. **Adapter selected ≠ runtime authorized**;
stage 7 alone gates a run and is owned entirely by the Agent Runtime. Inert
runtime modes MUST NOT reach a framework runtime.

**Routing (spec §22).** The runtime requests, the Model Router decides. No
direct model access, no direct provider access, no credentials. **Framework
configuration MUST NOT bypass canonical routing** — a model name in framework
configuration is not an authorization. Runtime §23.4's fallback prohibitions
apply unchanged. Provider selectable ≠ provider authorized.

**Error translation (spec §23).** Twelve existing Runtime-owned classes are
consumed unchanged (including `BRIDGE_UNSUPPORTED_BEHAVIOR`,
`BRIDGE_FAILURE_UNCLASSIFIED`, `EXECUTION_BLOCKED`, `PACKAGE_MISMATCH`,
`CANCELLATION_UNSUPPORTED`). Nine bridge-owned classes are added only where
genuinely absent from every existing taxonomy. Original framework errors MUST be
preserved; suppression is prohibited.

## 12. Security considerations

Fifteen threats addressed at spec §34, each with a section-citing mitigation:
framework-native prompt injection; adapter impersonation; capability
amplification; permission flattening; policy bypass; tool substitution; command
or hook activation; plugin loading; MCP credential exfiltration; context
poisoning; memory contamination; provider-routing bypass; semantic-loss
concealment; error suppression; provenance spoofing.

Projection loss (spec §24) is classified in four tiers, and **safety-relevant
loss MUST fail closed** with `PROJECTION_LOSS_UNACCEPTABLE`. Emulation, silent
degradation, and coerced success are prohibited; ambiguity resolves to loss.

## 13. Deferred dependencies

Twelve, recorded at spec §36: Agent Package `NEW-P2-01`, `NEW-P2-02`, and
`NEW-P2-03`; Agent Manifest Contract; Capability Contract; Skill Registry;
Command Registry; Hook Registry; Plugin Registry; MCP Registry; Package
Validation contract; and the six per-framework adapter specifications. None is
started or authorized by this task.

## 14. State synchronization

Bounded to recording that the specification exists and remains documentation
only:

| File | Change |
| --- | --- |
| `PROJECT_STATE.md` | Records the task complete, specification drafted and unverified, no adapter or framework integration, the three P2 findings still open and deferred, next task an independent review |
| `ROADMAP.md` | Adds the Framework Bridge Contract as a completed documentation item in the Agent track; downstream still blocked |
| `RUN_QUEUE.md` | Marks the queue item complete; records the next task; keeps all downstream items blocked |
| `AGENT_HANDOFF.md` | New Latest Update block with outcome and exact next task |
| `PROJECT_HISTORY.md` | Durable historical entry |
| `TASK_INDEX.md` | Registers the minted task ID and its status |

No state document asserts that any framework is integrated, available,
supported at runtime, installed, enabled, tested, or operational; that any
adapter exists; or that any bridge, runtime, package loader, command, hook,
plugin, MCP, or batch capability exists.

## 15. Validators executed and exact outcomes

1. `git diff --check` → exit `0` (benign LF/CRLF warnings only).
2. `py -3.9 scripts/validate_project_state.py` → `PASS MellyCore project
   scaffold validation passed`, exit `0`. Run at baseline and post-commit.
3. **Changed-file allowlist check** → exactly the eight files of §4.1.
4. **Exact task-ID consistency check** → `MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001`
   appears consistently across all changed files with one meaning; no variant
   spelling; no duplicate task ID.
5. **Required-section check** → all 37 brief-mandated sections present
   (specification carries 39, adding References and Amendment per repository
   convention).
6. **Owner-reference check** → every consumed concept cites its canonical owner;
   all `[[wikilink]]` targets resolve to existing files.
7. **Framework-identifier check** → only the six canonical members appear; **no
   unsupported or seventh identifier introduced**; `mellycore_custom` used as
   canonical, with the "custom" naming note recorded.
8. **Agent Package P2 containment check** → confirmed: no package-lifecycle
   rendering field defined; no package contract version declared canonically
   current (neither 1.0 nor 1.1); no protected command classes defined or
   enumerated; all three recorded as deferred dependencies at spec §36.
9. **Overclaim scan** → `implemented`, `integrated`, `available`, `enabled`,
   `installed`, `operational`, `executable`, `production-ready`, `supported`,
   `tested`, `accepted`, `approved`, `passed`, `live`, `deployed` reviewed in
   context across the full diff. Every hit is a negated claim, a defined state
   name (`framework-supported`, `runtime-supported`, `policy-allowed`,
   `Operator-approved`), a scan-term list, or explicit prose stating
   non-existence.
10. **Cross-reference check** → internal `§` references verified against their
    targets; the review/remediation chain and next-task pointer coherent.
11. **Duplicate task-ID check** → no collision with any existing task ID.
12. **Secret and configuration check** → no `.env` changed; no secret,
    credential, token, or provider key introduced; no workflow YAML changed; no
    source or test file changed.
13. **Immutable-source verification** → recorded before edits and re-verified
    after commit (§16).

`pytest`: **`NOT_RUN`** — no source or test file changed; not claimed passing.
Black, flake8, and mypy: **not run**, not claimed passing.

No repository gate validator was unavailable.

## 16. Immutable-source verification

Blob IDs recorded before any edit and re-verified after the commit; all
unchanged.

| Blob ID | Path |
| --- | --- |
| `12b67752f041fef38d769221a2bd9a4df2891068` | `docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md` |
| `9a392a730b345c14df4c184f65200beca0bfbea6` | `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001.md` |
| `69a8bcbe0ace5d3f7b46f2a5a46b438b5eb75f5d` | `docs/research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_001.md` |
| `de318f4721f0552db871672746faf3ea776baa50` | `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-001.md` |
| `2178bb0abc21a7556559861a6e6cec857509cbf1` | `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001.md` |
| `d0ae398dce0ffffd1c982c7ab798dbd991a0eaa4` | `docs/research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_002.md` |
| `47af39e4364971a3ec0a24719d1c740629e01c4d` | `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-002.md` |
| `3e085f97141fc0cb505ab4d9a738592d7ca601f7` | `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md` |
| `f35f0e157879322c9edbaf834043902579a6d98f` | `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` |
| `fa90b65b4f91545550247d81fc181eb10cca942a` | `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md` |
| `65192fa157b57a2a46768ceca4660aed1584f649` | `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` |
| `4ea189989665907b0b931c2a86dcc112285d69b8` | `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` |
| `13fa511f6228d4f8f13295dbd857c7586a163333` | `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md` |
| `13b2df338ad53cff02eb236ba0d30d34cd35bf20` | `docs/decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001.md` |
| `0d2768be8d9ae19b5a14ce1c61441550081113e3` | `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md` |
| `e8f8961f5c1a12275527cc05c83c432c9312d0d6` | `shared_context/CONTEXT_GRAPH_SCHEMA.md` |
| `a70500a9909ee5bbe2bf60cdfe9e779fc47877a0` | `shared_context/SAFETY_CONTRACT.md` |

## 17. Implementation status (unchanged by this task)

| Dimension | State |
| --- | --- |
| Framework Bridge | `NOT_IMPLEMENTED` |
| Framework Adapters (all six) | `NONE_EXIST` |
| SDKs / frameworks | `NOT_INSTALLED`, `NOT_IMPORTED`, `NOT_EXECUTED` |
| Framework sessions created | **Zero** |
| Agent Runtime | Unchanged; `NOT_IMPLEMENTED` |
| Agent Package Contract | Unchanged; v1.1, documentation only |
| Package loading / execution / commands / hooks / plugins / MCP / batch | **None** |
| Provider connection, credential, model call, deployment | **None** |
| Migration triggers #1, #4, #5, #6, #7 | Uncrossed |

## 18. Final commit

One local documentation commit on
`docs/mellycore-framework-bridge-contract-spec-001`, subject:

```
docs: define agent framework bridge contract
```

Not amended, not squashed, **not pushed**. No pull request, no merge, no
deployment, no destructive Git operation.

## 19. Next recommended task

`MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-REVIEW-001` — an independent,
read-only architecture, ownership, and safety review of this specification,
following the same gated sequence the Agent Runtime architecture and Agent
Package Contract were each subject to. Expected record:
`docs/research/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_REVIEW_001.md`.

**Not started, not authorized by this task.** All downstream work — Shared
Context Bridge, Agent Runtime Scaffold (inert), Scaffold Review, first Agent
Package, Cross-Agent Smoke, Integration Review, the six per-framework adapter
specifications, and the twelve Agent Package follow-up contracts — remains
blocked, each requiring its own gate and separate explicit Operator
authorization. The global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` remains unchanged and
takes precedence over this track.
