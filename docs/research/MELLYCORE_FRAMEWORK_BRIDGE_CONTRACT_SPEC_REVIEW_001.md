# MellyCore Framework Bridge Contract Spec — Independent Review 001

## 1. Review identity

**Task ID:** MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-REVIEW-001
**Reviews:** `MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_001`, **version 1.0**, commit
`278eae0c47af31c67c69417d447ee4f9bdb7e049`.
**Consumes:** `MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001`
(reported outcome `FRAMEWORK_BRIDGE_CONTRACT_SPECIFIED_UNVERIFIED`).
**Status:** Independent, read-only architecture, ownership, interoperability,
and safety review. This record is a documentation artifact only; it
implements, connects, executes, or authorizes nothing.
**Gate decision:** `PASS_WITH_NON_BLOCKING_FINDINGS` (§28). P0 = 0 and P1 = 0;
eight new non-blocking findings are recorded (four P2, four P3).

**Empirical framework validation: `NOT_PERFORMED`.** No framework was
installed, imported, connected, configured, or executed by this review. No
online documentation was consulted. Every framework-related conclusion derives
from repository-owned contracts and deliberately high-level conceptual review.

This review did not accept the specification task report's assertions. Every
verdict below was re-derived from the committed specification text and the
canonical owner documents, and every metric was recounted independently.

## 2. Repository and baseline

- Root: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios`
- Starting branch: `docs/mellycore-framework-bridge-contract-spec-001`
- Starting HEAD: `278eae0c47af31c67c69417d447ee4f9bdb7e049` (short `278eae0`)
- Latest subject at start: `docs: define agent framework bridge contract`
- Starting worktree/index: clean (`git status --short` empty)
- Upstream tracking: **none**
- Configured remotes: `origin`, `clean-origin` (neither contacted)
- Review branch created from that exact HEAD:
  `docs/mellycore-framework-bridge-contract-spec-review-001` (did not
  previously exist)
- **No network operation occurred at any point in this review.**

Every required baseline matched. Review 001 artifacts did not previously
exist. `RUN_QUEUE.md`, `PROJECT_STATE.md`, `AGENT_HANDOFF.md`, and
`TASK_INDEX.md` all record this review as the exact next task, and
`TASK_INDEX.md` records the specification task as `COMPLETE … unverified`.

### 2.1 Environmental Git-scope protection

`C:\` is itself a separate Git repository with unrelated uncommitted changes.
**Every** Git command in this review was explicitly scoped with
`git -C "C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios"`. No unscoped Git
command was run. The outer `C:\` repository was never inspected, staged,
reset, cleaned, or committed.

## 3. Reviewed artifact and version

`docs/specs/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001.md`, version **1.0**,
**39 sections** (§1–§39), read in full. Its task report
`docs/tasks/MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001.md` was read in full
as context, not as authority.

## 4. Review methodology

1. Read-only scoped identity gate before any mutation.
2. Immutable baselines recorded as Git blob IDs (§6) before any edit.
3. Review branch created from the verified commit.
4. The complete specification read end to end.
5. **Owner lists reconstructed mechanically, then compared against the
   specification's claims** — Runtime §11.1's framework set, §11.2's six rules,
   §16's nine operations, §33's error classes, and Agent Package §10.1's
   capability states were each extracted directly from the owner document and
   tested against the reviewed text, rather than accepting the specification's
   statement that it consumes them.
6. Every self-reported count recomputed directly from the cited section.
7. Every `[[wikilink]]` resolved against the filesystem.
8. Normative-modal scan for inverted constructions.
9. Severity assigned strictly by the repository's existing P0/P1/P2/P3
   taxonomy and gate names (`PASS`, `PASS_WITH_NON_BLOCKING_FINDINGS`,
   `FAIL_REMEDIATION_REQUIRED`) as already used by Agent Package Review 001
   §34 and Agent Runtime Review 002 §36. No taxonomy was invented.
10. Nothing found wrong was repaired. The reviewed specification was not
    edited.

## 5. Independent owner map

| Concern | Canonical owner | Framework Bridge claim | Independent verification method | Result |
| --- | --- | --- | --- | --- |
| Closed `framework_type` set | Agent Runtime §11.1 | Consumes unchanged; adds no seventh | Extracted the six members from Runtime §11.1; grepped every backticked identifier in the reviewed spec | ✅ Exact; `custom` absent as an identifier; `other`/`generic`/`auto` appear only inside the prohibition sentence |
| Six normative bridge rules | Agent Runtime §11.2 | Consumes as a binding floor, stricter only | Located each rule in Runtime; counted explicit `Runtime §11.2 rule N` citations in the reviewed spec | ✅ All six cited by number (rule 1 ×5, rule 2 ×5, rules 3–5 ×1, rule 6 ×2); none weakened |
| Nine bridge operations and fail-closed outcomes | Agent Runtime §16 | "Consumes verbatim … never a tenth operation" | Extracted all nine operation names from Runtime §16; grepped each in the reviewed spec | ⚠ Four never named; one (`normalize_result`) has no counterpart rule — `NEW-P2-01` |
| Runtime error taxonomy | Agent Runtime §33 | Consumes existing; adds only genuinely absent classes | Extracted all 55 Runtime classes and Agent Package's 16; compared against the nine bridge-owned classes | ✅ Zero exact name collisions; ⚠ one semantic overlap — `NEW-P2-02` |
| Capability-state model | Agent Package Contract §10 | Adds a sixth state "without collapsing any existing one" | Extracted both numbered lists and compared row by row | ⚠ Model preserved and tightened, but owner rows 2–5 silently renumbered — `NEW-P2-03` |
| Package identity, boundary, lifecycle, trust | Agent Package Contract | Projects read-only; defines no package concept | Read §7, §8, §14, §20.4 against the Package Contract | ✅ No package concept defined; no lifecycle field invented |
| Model selection and routing | Model Router (Runtime §23; Control Plane §9.2; `MODEL_ROUTING.md`) | Routes framework requests; never selects | Read Runtime §23.1–§23.4 against reviewed §22 | ✅ Framework configuration cannot bypass routing; fallback prohibitions preserved |
| Provider authorization, MCP server records | Provider Registry §21.1, §24 | References only | Read reviewed §17 against Provider Registry §24.2 | ✅ Reference-only; transport-neutral; no credential, connection, or tunnel |
| Capability resolution, policy order, approvals | Integration Gateway §12, §17, §18 | Preserves decisions; grants nothing | Read reviewed §9, §10 against Gateway | ✅ Decisions carried by reference, never copied authority |
| Shared Context canonical truth | Shared Context Layer; `CONTEXT_GRAPH_SCHEMA.md` | Proposal-only; never writes canonical state | Read reviewed §18 against Runtime §11.2 rule 4 and §17.1 | ✅ Proposal-only; return-path re-validation mandatory |
| Six status dimensions | Control Plane §7.1, §8.1 | Bridge fields are typed entity data | Read reviewed §20.3 and §26.1 against Control Plane §7.1 | ✅ No seventh dimension created |
| Per-framework planning positions | Agent Runtime §11.3, §35 | Records them as unvalidated; assigns the obligation | Read Runtime §11.3/§35's own wording against reviewed §27.2 | ✅ Honest and owner-correct; ⚠ not wired into §25 — `NEW-P2-04` |
| Command namespace ownership | Future Command Registry | Never activates, owns, or resolves | Read reviewed §14 in full | ✅ No protected class enumerated; `NEW-P2-03` of the Agent Package remains contained |

No concern was found with two incompatible canonical owners. **No ownership
was taken from any owner document, and no owner document was edited.**

## 6. Immutable-source baseline

Recorded as Git blob IDs at review start, before any edit.

### 6.1 Reviewed subject (MUST NOT change)

| Blob ID | Path |
| --- | --- |
| `09b762201934543b3c03d492fa756bb5e081477f` | `docs/specs/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001.md` |
| `80b0560318eac2e0b2e6db137c93e8485d73ef55` | `docs/tasks/MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001.md` |

### 6.2 Canonical owner documents (MUST NOT change)

| Blob ID | Path |
| --- | --- |
| `3e085f97141fc0cb505ab4d9a738592d7ca601f7` | `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md` |
| `12b67752f041fef38d769221a2bd9a4df2891068` | `docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md` |
| `d0ae398dce0ffffd1c982c7ab798dbd991a0eaa4` | `docs/research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_002.md` |
| `47af39e4364971a3ec0a24719d1c740629e01c4d` | `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-002.md` |
| `f35f0e157879322c9edbaf834043902579a6d98f` | `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` |
| `fa90b65b4f91545550247d81fc181eb10cca942a` | `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md` |
| `65192fa157b57a2a46768ceca4660aed1584f649` | `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` |
| `4ea189989665907b0b931c2a86dcc112285d69b8` | `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` |
| `13b2df338ad53cff02eb236ba0d30d34cd35bf20` | `docs/decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001.md` |
| `e8f8961f5c1a12275527cc05c83c432c9312d0d6` | `shared_context/CONTEXT_GRAPH_SCHEMA.md` |
| `a70500a9909ee5bbe2bf60cdfe9e779fc47877a0` | `shared_context/SAFETY_CONTRACT.md` |
| `b4441133b4529c1260de205b147d2c42b5063a5d` | `shared_context/MODEL_ROUTING.md` |

## 7. Recalculated metrics

Every count recomputed directly from the committed text.

| Dimension | Independently recounted | Specification's own statement | Result |
| --- | --- | --- | --- |
| Sections | **39** (§1–§39) | §37 criterion 1 says "All 37 sections" | ⚠ `NEW-P3-02` |
| Terminology entries (§2) | 20 | §37 criterion 2: "at least the twenty terms" | ✅ |
| Ownership rows (§3) | 17 | — | ✅ |
| Canonical-vs-projected register rows (§4.3) | 11 | — | ✅ |
| Framework members (§5.1) | 6 | "six members" | ✅ |
| Adapter fields (§6.1) | 12 | — | ✅ |
| Version axes (§6.3) | 4 | "four independent" | ✅ |
| Capability states (§9.1) | 6 | "sixth … state" | ✅ (but see `NEW-P2-03`) |
| Permission categories (§10.1) | 13 | "thirteen categories" | ✅ |
| Memory scopes (§19) | 5 | "Five memory scopes" | ✅ |
| Runtime-interaction stages (§21) | 11 | "Eleven distinct stages" | ✅ |
| Consumed error classes (§23.2) | 12 | — | ✅ |
| Bridge-owned error classes (§23.3) | 9 | — | ✅ |
| Projection-loss tiers (§24.1) | 4 | — | ✅ |
| Validation layers (§25.1) | 10 | "ten layers" | ✅ |
| Observability projections (§26) | 16 | — | ✅ |
| Security threats (§34) | 15 | "fifteen threats" (§37 criterion 16) | ✅ |
| Non-goals (§35) | 16 | — | ✅ |
| Deferred dependencies (§36) | 12 | — | ✅ |
| Acceptance criteria (§37) | 19 | — | ✅ |

**Nineteen of twenty recounted dimensions reproduce exactly.** The single
discrepancy is §37 criterion 1's section count.

**No document-metrics table exists** — see `NEW-P3-01`.

## 8. Runtime §11 framework-set verdict — **PASS**

Runtime §11.1's closed set was extracted directly: `claude_code`,
`openai_agents_sdk`, `langgraph`, `crewai`, `autogen`, `mellycore_custom`.

- All six present in reviewed §5.1 and each has a profile (§28–§33). ✅
- **No seventh valid identifier exists.** ✅
- **`custom` is not accepted as an alias** — it appears nowhere as a backticked
  identifier, and §5.2 rule 3 states expressly that "`custom` alone is not a
  valid `framework_type` value". ✅ This is a correct handling of a naming trap:
  the canonical member is `mellycore_custom`.
- `other`, `generic`, `auto` appear exactly once, inside §5.2 rule 2's
  prohibition ("There is no `other`, `generic`, or `auto` member"). ✅
- The closed vocabulary is not broadened; §5.2 rule 4 requires an owner
  amendment to add one and forbids anticipating it. ✅

## 9. Runtime §11.2 rule verdict — **PASS**

All six rules are cited by number and preserved:

| Runtime §11.2 rule | Preserved at | Weakened? |
| --- | --- | --- |
| 1 — No policy bypass | §10.1 rows 3–4, §11.6, §12.3, §15.6, §16.6, §29 | No — restated and extended to auto-loaded surfaces |
| 2 — No direct provider access / no credential | §10.1 rows 5–6, §17.5, §22.3 | No |
| 3 — No direct model access | §22.2 | No |
| 4 — No canonical writes | §18.2 | No |
| 5 — Honest capability reporting | §6.2 rule 2, §24.2 rule 2 | No — strengthened ("Silence is not a capability claim") |
| 6 — Framework-native state is not canonical | §4.2 rule 3, §19, §30 | No |

Framework support is nowhere treated as authorization: §9.2 rule 3 states
expressly that "a framework's ability to perform an action MUST NOT be
interpreted as MellyCore authorization." No framework-native bypass is created.

## 10. Runtime §16 operation verdict — **PARTIAL** (`NEW-P2-01`)

The nine canonical operations were extracted directly from Runtime §16 and
each grepped in the reviewed specification:

| Operation | Named in reviewed spec? | Behavior covered? |
| --- | --- | --- |
| `validate_package_compatibility` | Yes | Yes — §21 stage 3 |
| `prepare_invocation` | Yes | Yes — §23.3 `FRAMEWORK_INITIALIZATION_FAILED` |
| `translate_envelope` | Yes | Yes — §8.2 rule 2 |
| `start_execution` | **No** | Partially — §21 rule 3 (inert modes, `EXECUTION_BLOCKED`) |
| `stream_events` | **No** | Yes — §21 stage 9 (`unmapped` event, never dropped) |
| `request_cancellation` | **No** | Yes — §21 stage 11 (`CANCELLATION_UNSUPPORTED`) |
| `normalize_result` | **No** | **No — no counterpart anywhere** |
| `normalize_failure` | Yes | Yes — §23.1 rule 2 |
| `report_unsupported_behavior` | Yes | Yes — §6.1 field 9, §6.2 rule 2 |

No operation's authority is removed — §3 consumes §16 verbatim and §33 item 2
binds a custom adapter to "no behavior outside the nine bridge operations."
No tenth operation is created, and no fail-closed outcome contradicts Runtime.
But four operations are never named and one is substantively uncovered. See
`NEW-P2-01`.

## 11. Framework-validation-obligation verdict — **HONEST AND OWNER-CORRECT, with one gap**

This was treated as a special review target and was **not** accepted merely
because the task was forbidden from executing frameworks.

**What the owner actually requires.** Runtime §11.3: "Every row MUST be
independently validated by the future Framework Bridge Contract task **before
any bridge is implemented**." Runtime §35 repeats this per cell. The obligation
is therefore expressed as a precondition of **implementation**, not of
specification acceptance.

**What the reviewed contract does.** §27.1 states plainly that no framework was
installed, imported, connected, configured, or executed and that no profile is
implemented, tested, installed, available, or operational. §27.2 states
expressly that **"this task cannot discharge that obligation"**, records the
cells as unvalidated planning positions, and assigns the obligation onward.

**Assessment against the brief's six questions:**

| Question | Answered? | Where |
| --- | --- | --- |
| What must eventually be validated? | Yes | §27.2 item 2 — "its own framework's cells" |
| By whom? | Yes | §27.2 item 2 — each future per-framework adapter specification |
| At what stage? | Yes | §27.2 item 2 — "before any adapter for that framework may be implemented" |
| With what evidence? | Partially | "with recorded evidence" — the evidence class is not specified |
| What remains blocked until validation? | Yes | Adapter implementation for that framework; §36 item 12 |
| Can unvalidated cells affect runtime eligibility? | **No — unanswered** | Not stated; §25 contains no such layer — `NEW-P2-04` |

**Verdict: a correct limitation honestly recorded, and a permitted
documentation-only deferral — not a P1 ownership failure and not a false
validation claim.** The contract neither claims the obligation was discharged
nor weakens it; it upgrades no Runtime §35 cell. Because the owner scoped the
obligation to "before any bridge is implemented" and no adapter exists, the
deferral does not breach the owner's requirement. The one genuine gap is that
the obligation is not connected to §25's validation layers or to Bridge
Eligibility, recorded as `NEW-P2-04`.

## 12. Canonical-versus-projected-state verdict — **PASS**

§4.1 fixes the required direction and prohibits the inverse. §4.3's eleven-row
register marks **every** projected form non-authoritative. Each prohibition
the brief required was tested:

| Must be prevented | Prevented at | Result |
| --- | --- | --- |
| Framework-native state becoming canonical | §4.2 rule 3, §19 rule 2 | ✅ |
| SDK configuration redefining MellyCore identity | §4.2 rule 2, §7.1–§7.2 | ✅ |
| Projected lifecycle replacing canonical lifecycle | §20.4 rule 3, §4.3 | ✅ |
| Framework memory becoming Shared Context | §19 rule 1 | ✅ |
| Framework tool availability becoming permission | §12.2 | ✅ |
| Adapter selection becoming execution authorization | §21 rule 1 | ✅ |

§4.2 rule 2 is the strongest clause: a framework SDK's schema requirement is
explicitly not a canonical justification.

## 13. Capability-state verdict — **MODEL PRESERVED, NUMBERING DIVERGES** (`NEW-P2-03`)

Reconstructed from Agent Package §10.1 and compared row by row:

| # | Agent Package §10.1 (owner) | # | Framework Bridge §9.1 |
| --- | --- | --- | --- |
| 1 | Declared | 1 | Declared |
| 2 | Runtime-supported | 2 | **Framework-supported** (new) |
| 3 | Policy-allowed | 3 | Runtime-supported |
| 4 | Operator-approved | 4 | Policy-allowed |
| 5 | Active | 5 | Operator-approved |
| — | — | 6 | Active |

**Owner-consistent aspects.** No owner state is removed, merged, or given a new
meaning. Framework support is genuinely orthogonal — it is established by the
framework via the adapter's validated `projection_capabilities`, independent of
every other state. §9.2 rule 1 *tightens* the conjunction from five to six and
rule 2 preserves intersection-never-union, which §3.1 permits as stricter-only.
§9.2 rule 4 states expressly that framework support is "necessary but not
sufficient", so it cannot independently grant capability eligibility. ✅

**The defect.** Owner rows 2–5 are silently renumbered, and no divergence
warning exists anywhere in the reviewed document. See `NEW-P2-03`.

## 14. Permission and approval verdict — **PASS**

All thirteen categories audited individually against §10.1. Every category
carries a projection rule that constrains rather than relaxes:

filesystem read (exact declared paths) · filesystem write (exact writable-file
ownership) · shell execution (`operator_only`; framework-native shell tool must
be disabled or intercepted) · network access (bounded; framework HTTP helpers
disabled) · provider access (Provider Registry's eight facts; no direct access)
· **secret access (denied by construction — no projection may carry credential
material)** · Git mutation · PR operations · MCP access · plugin loading · hook
execution · batch execution · deployment.

§10.1's header states all thirteen default **DENY** and that "**Framework
defaults MUST NOT override MellyCore deny-by-default policy** in any category."
§10.2 rule 4 prohibits permission flattening into a coarse framework switch —
directly addressing the amplification path a framework's single "allow tools"
setting would otherwise create. §10.2 rule 1 binds approval to a tuple that
includes `adapter_revision_id`, so a changed adapter invalidates prior
approvals. §10.2 rule 5 carries a decision *reference*, never copied authority.

## 15. Prompt, tool, skill, command, hook, plugin, and MCP verdicts

| Area | Verdict | Basis |
| --- | --- | --- |
| **Prompt / instruction** | **PASS** | §11.3's five-level precedence puts Safety Contract and policy highest and framework-native defaults lowest; §11.4 protects Operator precedence from project-level instruction files and SDK defaults; §11.6 states framework-native instruction sources "MUST NOT acquire authority by virtue of the framework loading them automatically"; §11.2 treats package prompt content as untrusted data. A framework-native system prompt cannot gain canonical authority. |
| **Tool** | **PASS** | §12.1 converts framework tool calls to runtime tool proposals; §12.2 states availability ≠ authorization; §12.3 forbids leaving framework built-ins enabled; §12.4 prohibits substitution with name-similarity/nearest-match failing closed; §12.5 reuses Runtime's `TOOL_UNKNOWN`/`TOOL_DENIED` rather than competing; §12.6 keeps results untrusted. |
| **Skills** | **PASS** | §13.2 forbids self-activation; §13.5 defers full ownership to the Skill Registry; no skill is activated by projection. |
| **Commands** | **PASS** | §14.1's five prohibitions cover activation, namespace ownership, collision resolution, reserved-command override, and registration-by-projection. §14.2 rule 3 defines and enumerates **no** protected command classes. §14.2 rule 4 keeps the Command Registry as owner. |
| **Hooks** | **PASS** | §15.1–§15.3 keep hooks declarations-only and inert; §15.4 requires unguaranteed ordering to be declared rather than emulated, failing closed for order-dependent safety; §15.6 requires auto-discovery mechanisms to be disabled. |
| **Plugins** | **PASS** | §16.2 fixes the Framework Adapter / Plugin distinction explicitly — a plugin never becomes an adapter and an adapter never acquires a plugin's package-declared permissions; §16.3 availability ≠ approval; §16.6 no automatic loading. |
| **MCP** | **PASS** | §17.1 reference-only, no registration payload; §17.4 transport-neutral (names no transport, port, socket, URL, or spawn method); §17.5 no credential material; §17.6 no automatic connection; §17.7 no implicit tunnel; §17.2 exposure is visibility, never authorization, with `output_trust_level: untrusted` preserved. Provider Registry ownership intact. |

## 16. Shared Context and memory verdict — **PASS**

**Shared Context (§18).** Reads bounded to declared `required_context_classes`;
writes **proposal-only** with the bridge never writing canonical state (rule 2,
citing Runtime §11.2 rule 4); namespace isolation per tenant, environment, and
run with cross-tenant visibility a `TENANT_ISOLATION_VIOLATION`; provenance
retained and extended with `adapter_revision_id`; transformation must not alter
meaning, sensitivity, or provenance; sensitivity or provenance loss is
safety-relevant and fails closed; execution-local state is not auto-promoted;
**return-path re-validation is mandatory and a projected value returning
unchanged does not bypass it**; and no adapter-scoped shortcut around the
Context Gate exists.

**Memory (§19).** Five scopes separated — framework session, execution-local,
package-declared, Shared Context, durable MellyCore memory. Rule 1 forbids
silent promotion; rule 2 forces any framework "automatic memory, history, or
checkpoint feature" into scope 1 regardless of the framework's own labelling —
which correctly forecloses the LangGraph checkpoint and CrewAI memory paths.
Rule 3 declares no new memory category, preserving Runtime §18's six.

## 17. Lifecycle verdict — **PASS**

§20.1–§20.3 define only framework-session, adapter, and bridge-evaluation
lifecycles, each declared typed entity data with **no** projection onto any
Control Plane §8.1 dimension. §20.4 states expressly that the contract defines
no canonical package-lifecycle rendering field, that no normative rule depends
on one, that adapters MUST NOT render, synthesize, or infer canonical package
lifecycle, and that future contracts needing it MUST wait for the Agent Package
Contract owner's correction. **Agent Package `NEW-P2-01` is not reopened,
resolved, or worked around.**

## 18. Runtime and routing verdict — **PASS**

**Runtime interaction (§21).** All eleven stages present and distinct —
discovery, package validation, bridge compatibility evaluation, adapter
selection, policy evaluation, instantiation eligibility, activation gating, run
creation, observation, suspension, termination. Ownership is correctly assigned
per stage; the bridge participates only in stages 3 and 9. Rule 1 states
**adapter selected ≠ runtime authorized** and that stage 7 alone gates a run.
Rule 3 keeps inert modes away from a framework runtime.

**Routing (§22).** Frameworks cannot choose providers directly (rules 2–3);
framework-native model settings are requests only (rule 4, which additionally
names API-key and base-URL fields as surfaces that must be disabled or
intercepted); the Model Router remains canonical (rule 1); Provider Registry
remains authoritative for provider facts (rule 8); credentials never enter
projection (rule 3); Runtime §23.4's fallback prohibitions are carried
unchanged (rule 7). §22.4's closing clause — "a model name present in framework
configuration is **not** an authorization" — is the decisive statement.

## 19. Runtime §33 error-taxonomy collision verdict — **NO DUPLICATED OWNERSHIP; ONE SEMANTIC OVERLAP**

All 55 Runtime §33 classes and all 16 Agent Package §21 classes were extracted
and compared against the nine bridge-owned classes.

**Exact name collisions: zero.** ✅

**Ownership:** §23.2 correctly lists twelve classes as Runtime-owned and
consumed — including `BRIDGE_UNSUPPORTED_BEHAVIOR`,
`BRIDGE_FAILURE_UNCLASSIFIED`, `EXECUTION_BLOCKED`, `CANCELLATION_UNSUPPORTED`,
and `PACKAGE_MISMATCH`. The bridge does not claim ownership of any of them. ✅

**Error suppression:** §23.1 rule 1 requires the original framework error text,
type, and code to be preserved; rule 3 prohibits suppression and routes
unmappable failures to Runtime's `BRIDGE_FAILURE_UNCLASSIFIED`. No bridge class
can be used to hide an original framework error. ✅

**Per-class assessment of the nine bridge-owned classes:**

| Class | Equivalent owner class exists? | Trigger deterministic? | Verdict |
| --- | --- | --- | --- |
| `ADAPTER_INVALID` | No | Yes — §25 layers 1–2 | ✅ |
| `ADAPTER_UNVERIFIED` | No (`PACKAGE_UNVERIFIED` is a different subject) | Yes — §6.2 rule 3 | ✅ |
| `BRIDGE_CONTRACT_VERSION_INCOMPATIBLE` | No (Package's `CONTRACT_VERSION_INCOMPATIBLE` is scoped to the package contract) | Yes — §6.3 | ✅ Correctly disambiguated by prefix |
| `PROJECTION_UNSUPPORTED` | **Overlaps `BRIDGE_UNSUPPORTED_BEHAVIOR`** | **No** | ⚠ `NEW-P2-02` |
| `PROJECTION_LOSS_UNACCEPTABLE` | No | Yes — §24.1 tier 3 | ✅ |
| `FRAMEWORK_INITIALIZATION_FAILED` | No (Runtime §16 assigns a run outcome, not a class) | Yes — `prepare_invocation` | ✅ |
| `CONTEXT_PROJECTION_FAILED` | No (`CONTEXT_ACCESS_DENIED` is a different condition) | Yes — §18 | ✅ |
| `TOOL_PROJECTION_FAILED` | No (`TOOL_DENIED`/`TOOL_UNKNOWN` are different) | Yes — §12 | ✅ |
| `LIFECYCLE_MISMATCH` | No, but coexistence with Runtime's mandatory `unmapped` event is unstated | Partially | ⚠ `NEW-P3-03` |

No ownerless class was found: every bridge class is claimed by this contract
and every consumed class cites its owner.

## 20. Projection-loss and validation verdict — **PASS**

**Projection loss (§24).** Four deterministic tiers — lossless, declared
non-safety loss, safety-relevant loss, unsupported semantic. Safety-relevant
loss (capability, permission, approval, trust, provenance, sensitivity, tenant
isolation, identity, cancellation) **MUST fail closed**. §24.2 rule 2 prohibits
emulation, silent degradation, approximation, and claimed success. Rule 4 is
the strongest clause: **ambiguity resolves to loss** — if it cannot be
determined whether a detail survived, it is treated as lost. Rule 5 prevents
declared non-safety loss accumulating unnoticed into safety-relevant loss.
Unsupported semantics are observable via §26 items 9 and 11.

**Validation (§25).** Ten layers, each with a clear input and a fail-closed
output; layer 9 (safety) fails closed "regardless of any other layer's result";
layer 10 makes an unobservable adapter ineligible. §25.2 states expressly that
**validation MUST NOT authorize execution** and that passing all ten layers
establishes Bridge Eligibility only, preserving `validated ≠ trusted`,
`validated ≠ executable`, and `compatible ≠ enabled`. No layer has an
authorization side effect.

## 21. Observability verdict — **PASS**

All sixteen required projections are present: canonical package ID, canonical
agent ID, framework ID, adapter ID and version, bridge-contract version,
package-contract version range, requested projection, accepted projection,
rejected semantics with reason class, denied capabilities, projection loss,
policy decision reference, runtime handle, framework session reference, failure
reason, cost-attribution reference.

§26 states every field is typed entity data, **not** a Control Plane §8.1 status
dimension; §26.1 forbids displaying bridge fields as `lifecycle_status`,
`evidence_state`, or `approval_state` values, forbids synthesizing a universal
"healthy" state, keeps `NOT_RUN`/`NOT_IMPLEMENTED` from rendering as pass, and
requires rejected semantics and projection loss to be rendered rather than
collapsed into a success boolean. **No new Control Plane status dimension is
created.** ✅

## 22. Framework-profile verdicts

§27.1 labels every profile bounded, conceptual, and non-implementation, states
that no framework was installed, imported, connected, configured, or executed,
that no online documentation was consulted, and that no profile may be cited as
evidence of a framework's actual behavior. An independent scan of §28–§33 found
**zero** occurrences of `installed`, `tested`, `integrated`, `operational`,
`available`, or `executed` as a claim. ✅

| Profile | Verdict | Notes |
| --- | --- | --- |
| **`claude_code` (§28)** | **PASS** | Treats project instruction files (of the `CLAUDE.md` kind), settings, skills, commands, hooks, plugins, MCP, and subagents as framework-native configuration surfaces, not canonical artifacts. States that such content is untrusted data and "MUST NOT acquire authority merely because the framework loads it". Requires subagent spawning to be re-expressed as a governed `sub_run` proposal. Closes with "**Claude Code remains one projection target, not the canonical architecture**". **Not privileged as the canonical package model.** ✅ |
| **`openai_agents_sdk` (§29)** | **PASS** | Covers agents, tools, handoffs, sessions, guardrails, tracing. Correctly states a framework guardrail "is **not** a MellyCore policy decision and MUST NOT be counted as one". All claims trace to Runtime §11.3/§35; **no current external SDK behavior is asserted** — §29 closes with "No API call is made or claimed by this document." ✅ |
| **`langgraph` (§30)** | **PASS** | Covers graph nodes, state, transitions, persistence, checkpoints, tool nodes. **Graph state is explicitly not equated with Shared Context** — it is forced into memory scope 1 "regardless of how durable or structured it appears", and Runtime §35's `C` persistence rating is correctly read as constraining reliance rather than conferring canonicality. Adds a genuine safety rule: a checkpoint restore MUST NOT resurrect a no-longer-authorized capability, and resumed state is untrusted. ✅ |
| **`crewai` (§31)** | **PASS** | Covers agents, crews, tasks, tools, processes, memory. Requires crew-level delegation to be re-expressed as governed handoffs and adds the correct corollary: **delegation is not capability transfer**; per-agent capability intersection is enforced rather than a crew-wide union. ✅ |
| **`autogen` (§32)** | **PASS** | Covers conversational agents, group-chat patterns, routing, tools, termination. States a speaker change is not an authorization event and that a framework termination condition firing is not a MellyCore run completion. Bounds message routing to authorized context classes. ✅ |
| **`mellycore_custom` (§33)** | **PASS** | Twelve minimum conformance requirements. Closes the bypass risk explicitly: "**Being 'custom' confers no relaxation**", subject to every rule in the contract. The requirements cover all six Runtime §11.2 rules, all six capability states, all thirteen permission categories, bridge-local state, routing, proposal-only context, fail-closed loss, declared limitations, all ten validation layers, and all sixteen observability projections — strong enough to prevent the custom path becoming a bypass around requirements applied to named frameworks. ✅ |

Framework-specific vocabulary does not become canonical in any profile: each
maps framework concepts onto MellyCore concepts, never the reverse.

## 23. Security verdict — **PASS**

All fifteen threats are addressed at §34, each with a mitigation citing a
specific section rather than asserting safety in the abstract: framework-native
prompt injection; adapter impersonation; capability amplification; permission
flattening; policy bypass; tool substitution; command or hook activation;
plugin auto-loading; MCP credential exfiltration; context poisoning; memory
contamination; provider-routing bypass; semantic-loss concealment; error
suppression; provenance spoofing.

Each mitigation was checked against its cited section and each cited rule
exists and says what §34 claims. No threat is mitigated only by assertion.

## 24. Agent Package P2 containment verdict — **ALL THREE CONTAINED AND STILL OPEN**

| Finding | Contained? | Independent evidence |
| --- | --- | --- |
| `NEW-P2-01` (missing package-lifecycle rendering field) | ✅ **Yes** | Every occurrence of "package-lifecycle rendering" in the reviewed spec is a denial or deferral (§2 term definition explicitly *excludes* it; §20.4 items 1–4). No such field is defined; no normative rule depends on one. |
| `NEW-P2-02` (contract-version self-contradiction) | ✅ **Yes** | §6.3 declares the four version axes independent, fixes the bridge-contract version at 1.0, states the package-contract currency is "**disputed and unresolved**", and declares **no value** as canonically current. Adapters express package compatibility as a **range**. The only "v1.1" mention (§1.4) is a factual statement that the Agent Package Contract *document* is version 1.1 and was accepted as documentation — which is true and is not an assertion about the disputed `contract_version` currency. **Neither 1.0 nor 1.1 is declared canonically current.** |
| `NEW-P2-03` (protected command classes unenumerated) | ✅ **Yes** | §14 contains **no** enumeration of protected command classes. §14.2 rule 3 states the contract "defines no protected command classes and enumerates none", MUST NOT translate or act on one, and that no normative rule depends on one. |

All three remain **open**, are recorded as deferred dependencies at §36 items
1–3 with the correct owners, and **none was silently resolved**. The Agent
Package Contract is byte-identical (§6.2). ✅

## 25. Version-axis verdict — **PASS**

§6.3 fixes four independent axes — `adapter_version`, bridge-contract version,
package-contract version, framework-compatibility range — and states they MUST
NOT be conflated. The bridge-contract version is internally coherent at 1.0:
§6.1 field 5 requires an adapter to declare a supported range, §23.3 supplies
`BRIDGE_CONTRACT_VERSION_INCOMPATIBLE` for exclusion, §25 layer 3 validates it,
§26 item 5 renders it, and §39 governs amendment. Supported package-contract
ranges do **not** silently resolve `NEW-P2-02`: §6.3 states the resolution must
come from the Agent Package Contract owner. Runtime and framework versions
remain separate axes.

## 26. Overclaim review — **PASS**

Every occurrence of `implemented`, `integrated`, `available`, `enabled`,
`installed`, `operational`, `executable`, `production-ready`, `supported`,
`tested`, `validated`, `accepted`, `approved`, `passed`, `live`, and `deployed`
was reviewed in context. Every hit is one of:

- an **unambiguous negation** (`NOT_IMPLEMENTED`, `NONE_EXIST`,
  `NOT_INSTALLED`, `NOT_IMPORTED`, `NOT_EXECUTED`, "**Zero**", "No profile is
  implemented, tested, installed, available, or operational");
- a **defined contract state name** (`framework-supported`, `runtime-supported`,
  `policy-allowed`, `Operator-approved`, `validation_state`, `validated`,
  `supported_environments`, `supported_bridge_contract_range`);
- or **explicit prose stating non-existence** (§1.4's implementation-state
  table, §27.1's no-framework-executed statement).

§1.4's table records `NOT_IMPLEMENTED` / `NONE_EXIST` / "**Zero**" for every
dimension and states no row may be advanced by a documentation task. §1.5
confirms migration triggers #1, #4, #5, #6, #7 remain uncrossed. **No framework
adapter, SDK integration, runtime, provider integration, or execution
capability is falsely implied anywhere.** ✅

## 27. New findings

### P0 — Critical

**None.** No credential path, no cross-tenant execution possibility, no Shared
Context mutation bypass, no authorization or approval bypass, no secret
exposure, no self-authorizing adapter permission, and no framework-native
policy bypass was found.

### P1 — Blocking

**None.** No ownership was taken from any owner document; no owner document was
edited; the closed framework set is exact; no Runtime error class ownership is
duplicated; no false framework-validation claim exists; and the specification
is fail-closed throughout.

### P2 — Material, non-blocking

**`NEW-P2-01` — Four of Runtime §16's nine bridge operations are never named,
and `normalize_result` has no counterpart rule anywhere.**

- **Location:** §3 (ownership row for Runtime §16), §21, §23.3.
- **Claim under review:** §3 states the contract "Consumes verbatim; adds
  projection semantics around them, never a tenth operation."
- **Canonical owner:** Agent Runtime §16 (owns the operations); this contract
  owns the projection semantics around them.
- **Evidence:** the nine operation names were extracted directly from Runtime
  §16 and grepped. `start_execution`, `stream_events`, `request_cancellation`,
  and `normalize_result` appear **zero** times. Behavior for the first three is
  covered without naming them (§21 rule 3, §21 stage 9, §21 stage 11).
  **`normalize_result` — "Map framework output to the run's output contract …
  Contract unmet → `failed`, never a coerced success" — has no counterpart.**
  Searches for "output contract", "run output", "normalize_result", and
  "result normaliz" return nothing; the only "coerced success" hits are §24.2
  and §34, both about *projection loss*, not run-output normalization.
- **Why this is a defect:** run-output normalization is the boundary where a
  framework's result becomes a MellyCore run outcome, and "never a coerced
  success" is safety-relevant — a coerced success is precisely the
  semantic-loss concealment §34 names as a threat. An adapter author reading
  this contract for projection guidance receives none for output. Separately,
  because the nine operations are never enumerated, a reader cannot check the
  consumption claim from this document alone.
- **Required correction:** add a run-output projection rule (or a §21 stage)
  covering output-contract normalization with the never-coerced-success rule,
  and enumerate the nine operations so the consumption claim is checkable.
- **Gate impact:** **non-blocking.** §3 consumes §16 verbatim and §33 item 2
  binds a custom adapter to "no behavior outside the nine bridge operations",
  so the Runtime obligation still binds by consumption. The gap is elaboration,
  not authority, and nothing is granted.

**`NEW-P2-02` — `PROJECTION_UNSUPPORTED` overlaps the Runtime-owned
`BRIDGE_UNSUPPORTED_BEHAVIOR` with no stated discriminator.**

- **Location:** §23.3 (class definition) against §24.1 (tier 4) and Runtime
  §11.2 rule 5 / §16 `translate_envelope`.
- **Claim under review:** §23.3 introduces `PROJECTION_UNSUPPORTED` for "a
  required projection … outside the adapter's validated
  `projection_capabilities` (§9.1 state 2)".
- **Canonical owner:** Agent Runtime §33 owns `BRIDGE_UNSUPPORTED_BEHAVIOR`;
  Runtime §11.2 rule 5 makes it *the* class by which a bridge reports
  unsupported behavior, and §16 routes any unrepresentable required field to it.
- **Evidence:** §24.1 routes "Unsupported semantic" to
  `BRIDGE_UNSUPPORTED_BEHAVIOR`, while §23.3 routes an unsupported required
  projection to `PROJECTION_UNSUPPORTED`. A required projection an adapter
  cannot perform satisfies **both** descriptions, and no rule states which
  applies.
- **Why this is a defect:** class selection is non-deterministic, so two
  adapters may report the identical condition differently — weakening §26 item
  9 ("rejected semantics, with the reason class") as a comparable observability
  contract. It is *not* duplicated ownership: §23.2 correctly lists
  `BRIDGE_UNSUPPORTED_BEHAVIOR` as Runtime-owned and consumed.
- **Required correction:** state the discriminator explicitly — for example,
  `PROJECTION_UNSUPPORTED` for a declared-capability mismatch detected at
  Bridge Validation time and `BRIDGE_UNSUPPORTED_BEHAVIOR` for an envelope
  translation failure at runtime — or drop the bridge class and consume the
  Runtime class.
- **Gate impact:** **non-blocking.** Both classes fail closed; no authority is
  granted under either reading.

**`NEW-P2-03` — The contract silently renumbers the Agent Package Contract's
capability states.**

- **Location:** §9.1 against Agent Package Contract §10.1.
- **Claim under review:** §9.1 states framework support is "a **sixth,
  independent** state introduced by this contract, inserted without collapsing
  any existing one."
- **Canonical owner:** Agent Package Contract §10 owns the capability-state
  model.
- **Evidence:** Package §10.1 numbers 1 Declared, 2 Runtime-supported, 3
  Policy-allowed, 4 Operator-approved, 5 Active. §9.1 numbers 1 Declared, 2
  **Framework-supported**, 3 Runtime-supported, 4 Policy-allowed, 5
  Operator-approved, 6 Active. Owner rows 2–5 each shift by one. A search for
  any divergence warning ("renumber", "numbering", "differs from §10.1", "row
  numbers") returns **nothing**. §23.3 then cites "(§9.1 state 2)" for
  framework support, while the Package Contract cites "§10.1 state 2" for
  runtime support and "§10.1 row 5" for active.
- **Why this is a defect:** the *model* is preserved and correctly tightened —
  no owner state is removed, merged, or re-meant, §9.2 rule 1 requires all six,
  rule 2 keeps intersection-never-union, and rule 4 makes framework support
  necessary-but-not-sufficient, all permitted as stricter-only under §3.1. But
  the **numbering** now collides across two live contracts, so "capability
  state 2" resolves to two different concepts depending on which document the
  reader holds — a real implementation hazard for anyone wiring gates by index.
- **Required correction:** refer to the states by name rather than index in
  §9.1 and its cross-references, or add an explicit mapping note stating that
  §9.1 rows 3–6 correspond to Agent Package §10.1 rows 2–5.
- **Gate impact:** **non-blocking.** No ownership is transferred, no state is
  collapsed, and the conjunction is strictly tightened rather than relaxed.

**`NEW-P2-04` — The framework-validation obligation is not connected to Bridge
Validation or Bridge Eligibility.**

- **Location:** §27.2 against §25.
- **Claim under review:** §27.2 assigns the Runtime §11.3/§35 validation
  obligation to each future per-framework adapter specification, "before any
  adapter for that framework may be implemented", "with recorded evidence".
- **Canonical owner:** Agent Runtime §11.3 and §35 state the obligation; this
  contract owns the validation layers (§25).
- **Evidence:** §25's ten Bridge Validation layers contain **no** layer
  referencing Runtime §35 cell validation, and §25.2's definition of Bridge
  Eligibility does not require it. A search of §27.2 for "eligib", "§25", or
  "validation layer" returns nothing.
- **Why this is a defect:** the review brief asks specifically whether
  unvalidated cells can affect runtime eligibility, and the contract does not
  say. As written, an adapter could satisfy all ten layers and reach Bridge
  Eligibility while its framework's §35 cells remain unvalidated. The ordering
  is probably safe in practice — no adapter can exist without implementation,
  which §27.2 blocks — but the contract does not state the connection, and
  §27.2 also leaves the required evidence *class* unspecified.
- **Required correction:** add a validation layer (or a clause in §25.2)
  stating that Bridge Eligibility for a named framework additionally requires
  that framework's Runtime §35 cells to be validated, and name the evidence
  class required.
- **Gate impact:** **non-blocking.** Nothing is authorized; §27.2's
  implementation block stands independently of §25.

### P3 — Editorial / maintainability

**`NEW-P3-01` — No document-metrics table, breaking a two-document convention
and removing the repository's count-drift safety net.**

- **Location:** §1 (no §1.4) and §39.
- **Evidence:** Agent Runtime §1.4 and Agent Package Contract §1.4 both carry a
  normative "Document metrics" table, and Agent Package §1.4 states it follows
  "exactly as required by `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]`
  §1.4". Agent Package §29 further requires an amendment to "recompute §1.4's
  document metrics". The reviewed specification has neither the table nor any
  recompute obligation in §39.
- **Why this matters:** that mechanism is precisely what surfaced the Agent
  Package chain's own `NEW-P3-02` (a stale "Fifteen" against 16 rows). Its
  absence removes the drift-detection discipline — and this review found
  exactly such a drift at §37 criterion 1 (`NEW-P3-02` below).
- **Required correction:** add a §1.4 document-metrics table with recomputed
  counts and extend §39 with a recompute obligation.
- **Gate impact:** non-blocking, editorial/maintainability.

**`NEW-P3-02` — §37 acceptance criterion 1 states "All 37 sections" against a
39-section document.**

- **Location:** §37 criterion 1.
- **Evidence:** independent recount is **39** sections (§1–§39). Criterion 1
  reads "All 37 sections are present and each required topic is addressed."
- **Fair reading:** it plausibly means "the 37 *required* sections", which is
  true — §1–§37 map 1:1 onto the brief's required list, with §38 References and
  §39 Amendment added per repository convention. The defect is that it is
  stated as an unqualified count of the document's sections and reads false on
  a literal check.
- **Required correction:** "All 37 required sections (§1–§37) are present, plus
  References (§38) and Amendment (§39)."
- **Gate impact:** non-blocking, editorial. Same class and severity as the
  Agent Package chain's `NEW-P3-02`, applied consistently.

**`NEW-P3-03` — `LIFECYCLE_MISMATCH`'s coexistence with Runtime's mandatory
`unmapped` event is unstated.**

- **Location:** §23.3 against §21 stage 9 and Runtime §16 `stream_events`.
- **Evidence:** Runtime §16 mandates "Unmappable event → emit an explicit
  `unmapped` event; never silently drop." §21 stage 9 correctly preserves this.
  §23.3 then defines `LIFECYCLE_MISMATCH` for "a framework lifecycle event
  [that] has no canonical counterpart and cannot be normalized (§20, §21 stage
  9)" — citing the very stage whose owner rule mandates an event rather than an
  error, without stating how the two coexist.
- **Why this matters:** no rule is weakened, since both are stated. But an
  implementer could read the error class as *replacing* the mandatory
  `unmapped` event, which Runtime forbids.
- **Required correction:** state that `LIFECYCLE_MISMATCH` accompanies, and
  never replaces, the mandatory `unmapped` event.
- **Gate impact:** non-blocking, clarity.

**`NEW-P3-04` — The specification task's outcome code is not recorded in the
repository.**

- **Location:** repository state documents;
  `docs/tasks/MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001.md`.
- **Evidence:** `FRAMEWORK_BRIDGE_CONTRACT_SPECIFIED_UNVERIFIED` appears in
  **no** tracked file. `TASK_INDEX.md` records `COMPLETE (specification only,
  local, not pushed) — unverified`, which conveys the same substance.
- **Why recorded:** a reader reconstructing the chain from the repository alone
  cannot recover the reported outcome code. This is a weak convention at most —
  the repository durably records *gate* decisions (Agent Package Review 002's
  `PASS_WITH_NON_BLOCKING_FINDINGS` is recorded in five state files) but has no
  established practice of recording specification-task outcome codes.
- **Required correction:** none strictly required; a future task report may
  state its outcome code inline.
- **Gate impact:** none.

## 28. Finding counts and gate decision

| Severity | Count | IDs |
| --- | --- | --- |
| **P0** | **0** | — |
| **P1** | **0** | — |
| **P2** | **4** | `NEW-P2-01`, `NEW-P2-02`, `NEW-P2-03`, `NEW-P2-04` |
| **P3** | **4** | `NEW-P3-01`, `NEW-P3-02`, `NEW-P3-03`, `NEW-P3-04` |

### `PASS_WITH_NON_BLOCKING_FINDINGS`

Derived from the findings using the repository's existing gate taxonomy and the
rule established by Agent Package Review 001 §34 and applied by Agent Runtime
Review 002 §36: **any P0 or P1 blocks; `PASS` requires zero new findings; new
non-blocking findings yield `PASS_WITH_NON_BLOCKING_FINDINGS`.**

Each condition was tested independently and each is met:

1. **P0 = 0** and **P1 = 0**.
2. **No ownership conflict.** The owner map (§5) resolves to exactly one owner
   per concern, and every canonical owner document is byte-identical (§6.2).
3. **No false framework-validation claim.** §27.2 states expressly that the
   obligation was not discharged; no Runtime §35 cell is upgraded, confirmed,
   or weakened; §27.1 denies installation, execution, and external
   documentation.
4. **No duplicated Runtime error ownership.** Zero exact name collisions;
   §23.2 correctly attributes all twelve consumed classes to the Agent Runtime.
   The one semantic overlap (`NEW-P2-02`) is an ambiguity, not an ownership
   claim.
5. **Framework-agnostic and fail-closed.** The closed six-member set is exact
   with no alias and no seventh identifier; every projection grants nothing;
   safety-relevant loss fails closed; ambiguity resolves to loss.
6. **Independent of all three open Agent Package P2 findings** (§24).
7. **Every safety distinction holds**, including `canonical ≠ projected`,
   `framework-supported ≠ MellyCore-supported`, `adapter selected ≠ runtime
   authorized`, `framework session ≠ MellyCore run`, `framework memory ≠ Shared
   Context`, `framework lifecycle ≠ package lifecycle`, `MCP declared ≠ MCP
   connected`, and `bridge specified ≠ bridge implemented`.

The outcome is `PASS_WITH_NON_BLOCKING_FINDINGS` rather than `PASS` **solely**
because this review introduced eight new findings. The distinction is recorded
honestly rather than resolved in the specification's favour.

The decision rests on none of: the specification task report's claims, its
self-reported counts, its self-reported hashes, or validator success.
`py -3.9 scripts/validate_project_state.py` passing proves only that repository
scaffolding is well-formed; it proves nothing about ownership, projection
correctness, or interoperability, and no architectural conclusion here rests
on it.

## 29. Specification acceptance and required follow-up

### 29.1 Acceptance

`MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_001`, version **1.0**, is **accepted as a
documentation contract** for the Framework Bridge track, under the eight
non-blocking constraints recorded in §27.

Acceptance is of a **documentation contract only**. It establishes what a
future Framework Adapter must satisfy. It does **not** establish that any of
the following exists, and none does: a Framework Bridge implementation, a
Framework Adapter for any framework, an installed or imported SDK, a framework
session, a runtime handle, an Agent Runtime implementation, a package loader,
any package installation or execution, any command, hook, plugin, MCP, or batch
capability, any provider connection, any credential, or any deployment.

### 29.2 Required follow-up

| Finding | Must be corrected before | Reason |
| --- | --- | --- |
| `NEW-P2-01` | the first per-framework adapter specification | run-output normalization is unspecified, and "never a coerced success" is safety-relevant |
| `NEW-P2-02` | any adapter specification emitting rejection classes | class selection is non-deterministic between two live classes |
| `NEW-P2-03` | any contract citing capability states by index | "state 2" resolves differently in two live contracts |
| `NEW-P2-04` | any adapter claiming Bridge Eligibility | eligibility does not currently require framework-cell validation |

The four P3 findings are editorial and may be closed in any future additive
amendment. **None is discarded**; each carries a location and a required
correction.

## 30. Acceptance limitations

1. This is a **documentation review**. It verifies ownership, internal
   consistency, fail-closed discipline, and cross-reference integrity. It
   cannot verify bridge behavior, because no bridge, adapter, framework
   session, or runtime exists.
2. **Empirical framework validation: `NOT_PERFORMED`.** No framework was
   installed, imported, or executed, and no external documentation was
   consulted. Runtime §11.3/§35's per-framework cells therefore remain
   **unvalidated** after this review, exactly as they were before it.
3. **Validator success proves nothing architectural.**
4. Acceptance is **bounded by the eight findings** of §27, which remain open
   and are not waived by this gate.
5. This review **authorizes no downstream work**. The next queued item is
   identified by plain name only; its identifier is neither minted nor
   authorized.
6. The Agent Package Contract's three open P2 findings remain **open** and are
   untouched by this review.
7. `pytest`, Black, flake8, and mypy were **`NOT_RUN`** — no source or test file
   changed. They are not claimed passing.

## 31. Exact next task

The next item already present in canonical `shared_context/RUN_QUEUE.md` for
this track, after this review, is the **Shared Context Bridge** — recorded
there as a plain name with **no task identifier**, followed by Agent Runtime
Scaffold (inert), Scaffold Review, first Agent Package, Cross-Agent Smoke
(inert modes only), Integration Review, the six per-framework adapter
specifications, and the twelve Agent Package follow-up contracts.

Each remains **blocked**, requiring its own specification, independent review,
and separate explicit Operator authorization. Consistent with the repository
convention that a task identifier is minted at the moment of Operator
authorization, **this review neither mints, starts, nor authorizes an
identifier for it.**

## 32. Implementation status (unchanged by this review)

| Dimension | State |
| --- | --- |
| Framework Bridge | `NOT_IMPLEMENTED` |
| Framework Adapters (all six) | `NONE_EXIST` |
| SDKs / frameworks | `NOT_INSTALLED`, `NOT_IMPORTED`, `NOT_EXECUTED` |
| Framework sessions created / runtime handles issued | **Zero** |
| Agent Runtime | Unchanged; `NOT_IMPLEMENTED` |
| Agent Package Contract | Unchanged; v1.1, documentation only; its three P2 findings remain open |
| Package loading, execution, commands, hooks, plugins, MCP, batch | **None** |
| Provider connection, credential, model call, deployment | **None** |
| Migration triggers #1, #4, #5, #6, #7 | Uncrossed |

## 33. Explicit non-authorizations

This review authorizes none of: any edit to the reviewed specification or its
task report; any Agent Runtime, Agent Package, Control Plane, Provider
Registry, Integration Gateway, or Shared Context amendment; any Framework
Adapter or bridge implementation; any SDK installation or framework execution;
any package, command, hook, plugin, MCP, or batch execution; any provider
connection, credential configuration, or model call; any network operation; any
push, pull request, merge, remote branch, or deployment; any MellyTrade
interaction.

## 34. Amendment and supersession

This review record is superseded only by a later, independently authored review
of a later version of the specification. It does not amend the reviewed
specification, any canonical owner document, or any prior review or remediation
record.

## 35. References

### 35.1 Reviewed

- `docs/specs/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001.md` (version 1.0)
- `docs/tasks/MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001.md`

### 35.2 Canonical cross-check sources

Listed with blob IDs in §6.2, plus `shared_context/RUN_QUEUE.md` and
`shared_context/TASK_INDEX.md` for sequencing.

### 35.3 External

**None.** No external standard, SDK, API, or online documentation was consulted.
