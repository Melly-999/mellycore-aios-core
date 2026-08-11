# MellyCore Agent Package Contract Spec — Independent Review 001

## 1. Title and status

**Task ID:** MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-001
**Reviews:** `MELLYCORE_AGENT_PACKAGE_CONTRACT_001`, version 1.0, commit
`708e265`.
**Status:** Independent, read-only architecture, ownership, and consistency
review. This record is itself a documentation artifact only; it implements,
connects, executes, or authorizes nothing.
**Gate decision:** `FAIL_REMEDIATION_REQUIRED` (§34). One P1 finding exists;
the gate cannot pass while any P0 or P1 finding is open.

## 2. Purpose

Independently verify whether
`docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md` is internally
consistent, correctly attributes ownership to every canonical owner document
it cites, contains no hidden ownership duplication, and preserves the
fail-closed discipline the task brief required — without repairing anything
found wrong. This review does not draft, edit, or remediate the specification
itself.

## 3. Scope

In scope: every one of the reviewed specification's 29 sections; its
citations of the Agent Runtime architecture, Provider Registry, Integration
Gateway, Control Plane, AI Operations Intelligence, Enterprise Provider ADR,
and Shared Context contracts; its own §1.4 document-metrics table, recounted
independently; and its 14 acceptance criteria (§27), replayed against the
document's actual text.

Out of scope: drafting or editing the reviewed specification; drafting any
follow-up contract it names; any implementation, execution, or connection of
any kind.

## 4. Starting repository state

- Root: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios`
- Starting branch: `docs/mellycore-agent-package-contract-spec-001`
- Starting HEAD: `708e2658f57d4dccd675e16fe858ca84b143dd2b`
- Subject: `docs: define agent package contract`
- Starting worktree/index: clean (`git status --short` empty)
- Review branch created from that exact HEAD:
  `docs/mellycore-agent-package-contract-spec-review-001`
- **No network operation occurred at any point in this review** — no fetch,
  pull, push, or remote access. The reviewed commit was already local; no
  canonical-remote gate was required.

## 5. Reviewed commit

`708e2658f57d4dccd675e16fe858ca84b143dd2b`, subject
`docs: define agent package contract`, parent
`9575bce8ae4aff2517838143f767a3a3979c77f8` (`docs: record Developer Platform
and Agent Package Ecosystem direction`) — the sole commit on
`docs/mellycore-agent-package-contract-spec-001`. The reviewer did not
author this commit's content in a capacity independent of this review
session; every claim below was re-derived from the document's own text and
from the canonical owner documents, not accepted from the document's own
task report.

## 6. Reviewed files

`docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md` (primary) and
`docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001.md` (its task report,
cross-checked for count and ownership-claim consistency, not accepted as an
independent source).

## 7. Canonical cross-check sources

| Source | Blob ID at review start | Used for |
| --- | --- | --- |
| `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md` | `3e085f97141fc0cb505ab4d9a738592d7ca601f7` | §8.1 identifiers, §9 separation states, §10.1 eighteen fields, §11 framework set, §14 facts, §18 memory categories |
| `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` | `f35f0e157879322c9edbaf834043902579a6d98f` | §7 entity catalogue, §8 six status dimensions, §9.8 Batch surface |
| `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md` | `fa90b65b4f91545550247d81fc181eb10cca942a` | §21.1 eight facts, §24 MCP registration/suspension |
| `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` | `65192fa157b57a2a46768ceca4660aed1584f649` | §12 capability resolution, §17 policy order, §21 MCP security contract, §25 error taxonomy |
| `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` | `4ea189989665907b0b931c2a86dcc112285d69b8` | §5 Run Ledger record identity |
| `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md` | `13fa511f6228d4f8f13295dbd857c7586a163333` | Fixture entity scope, unaffected |
| `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md` | `0d2768be8d9ae19b5a14ce1c61441550081113e3` | Tenant isolation, external-content posture |
| `docs/decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001.md` | `13b2df338ad53cff02eb236ba0d30d34cd35bf20` | Precedent for how the `run_state` → `lifecycle_status` seam was actually closed |
| `docs/research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_002.md` | `fb77b573c5351ddf4afab8ff6eb6580a2c39d3fc` | Precedent for gate criteria, severity definitions, and review method |
| `shared_context/CONTEXT_GRAPH_SCHEMA.md` | `e8f8961f5c1a12275527cc05c83c432c9312d0d6` | Shared Context provenance requirement |
| `shared_context/SAFETY_CONTRACT.md` | `a70500a9909ee5bbe2bf60cdfe9e779fc47877a0` | Safety boundary, unweakened |

## 8. Independent method

1. Repository identity gate (branch, HEAD, subject, clean worktree) before any
   read.
2. Immutable baselines recorded as Git blob IDs (§7, §9) before any edit.
3. Review branch created from the reviewed commit.
4. Every numeric claim in the reviewed document's own §1.4 recounted directly
   from its cited section, not accepted from the table.
5. Every ownership claim in the reviewed document's §5 independently rebuilt
   against the canonical owner document it cites, not accepted from the
   claim.
6. Every projection claim (package lifecycle onto Control Plane's six
   dimensions; package trust state onto the same) tested against Control
   Plane §8.1's actual closed enum vocabularies, exactly as Review 001 of the
   Agent Runtime architecture tested `run_state` against `lifecycle_status`.
7. All 14 acceptance criteria (spec §27) replayed against the document's
   actual text.
8. Findings severity assigned strictly by the Agent Runtime review's
   precedent definitions (P0 critical / P1 blocking / P2 material
   non-blocking / P3 editorial); no finding repaired.
9. Post-review re-verification that every cross-checked canonical document
   remained byte-identical to its recorded baseline (§35).

## 9. Immutable baselines

Recorded in §7 above (canonical sources) and here (reviewed artifact and
shared-context files this review's own state synchronization will edit):

| Blob ID | Path |
| --- | --- |
| `6020572ecfaa64c0d7d5aa2ee6e7f2e0c1f5df43` | `docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md` (reviewed; not edited by this review) |
| `9a392a730b345c14df4c184f65200beca0bfbea6` | `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001.md` (reviewed; not edited by this review) |
| `c493e16a1feea1a3906b771c0c4ff5bb67fad35d` | `shared_context/ROADMAP.md` (will be edited — state sync) |
| `1dafde4e390253674e34d5916f220e7c1e26bc89` | `shared_context/RUN_QUEUE.md` (will be edited — state sync) |
| `e1d0e3653a3164cfc587f8778940a0b7147b7b1e` | `shared_context/PROJECT_STATE.md` (will be edited — state sync) |
| `9dd5c4da26ea308483eba3df54e1ef49b4df9b3c` | `shared_context/AGENT_HANDOFF.md` (will be edited — state sync) |
| `e2890341f4e91820d5ecceb683a6668f41156651` | `shared_context/PROJECT_HISTORY.md` (will be edited — state sync) |
| `1664bf38d441d1c5370062a1cc68fef9fc76ba1a` | `shared_context/TASK_INDEX.md` (will be edited — state sync) |

### 9.1 Independently recounted dimensions

| Dimension | Claimed (spec §1.4) | Independently counted | Result |
| --- | --- | --- | --- |
| Specification sections | 29 | 29 (§1–§29) | ✅ |
| Terminology entries | 21 | 21 (§4 table rows) | ✅ |
| Architectural ownership rows | 13 | 13 (§5 table rows) | ✅ |
| Prohibited package contents | 7 | 7 (§6.2) | ✅ |
| Package identity fields | 12 | 12 (§7.1) | ✅ |
| Reused Agent Runtime package-metadata fields | 18 | 18, verified byte-for-byte against Runtime §10.1's own eighteen field names — no name drift | ✅ |
| Asset categories in the layout model | 9 | 9 (§8.1) | ✅ |
| Manifest relationship rows | 6 | 6 (§9 table) | ✅ |
| Capability states | 5 | 5 (§10.1) | ✅ |
| Permission/approval categories | 12 | 12 (§11.1) | ✅ |
| Framework compatibility rows | 6 | 6 (§13.2), matching Runtime §11.1's six-member closed set exactly | ✅ |
| Asset-type boundary rows | 5 | 5 (§14 table) | ✅ |
| Shared Context rules | 8 | 8 (§15) | ✅ |
| Runtime-interaction stages | 9 | 9 (§16 table) | ✅ |
| Package lifecycle states | 11 | 11 (§17.1) | ✅ |
| Validation layers | 9 | 9 (§18.1) | ✅ |
| Trust-state categories | 7 | 7 (§19.1) | ✅ |
| Observability projections | 11 | 11 (§20.1) | ✅ |
| Error/rejection classes | 15 | 15 (§21 table) | ✅ |
| Batch eligibility declarations | 7 | 7 (§23) | ✅ |
| Security threats | 12 | 12 (§24 table) | ✅ |
| Non-goals | 12 | 12 (§25) | ✅ |
| Follow-up contracts | 12 | 12 (§26) | ✅ |
| Acceptance criteria | 14 | 14 (§27) | ✅ |

**Every claimed count independently reproduces.** Unlike the Agent Runtime
architecture's first review, which found three count discrepancies (`P3-01`
through `P3-03` there), this document's self-reported metrics table contains
no counting error at review time. This is a materially different starting
condition from that review and is recorded as a positive finding, not
assumed.

## 10. Ownership matrix — independent rebuild

Rebuilt from the six canonical owner documents directly, then compared
against the reviewed document's own §5 table.

| Concern | Canonical owner (independently confirmed) | Matches spec §5? |
| --- | --- | --- |
| Package format, identity, boundary, declarations | This Agent Package Contract | ✅ Owner, correctly self-claimed |
| Agent/run identity, package/runtime separation states, execution envelope | Agent Runtime spec §8, §9 | ✅ Consumed verbatim; no field renamed |
| Package artifact storage | Agent Package Store (Runtime §7.3, unnamed elsewhere) | ✅ Correctly deferred |
| Package discovery/index/trust lookup | Package Registry (new term, reconciled in spec §4) | ✅ Reconciliation is explicit and does not rename Runtime's term |
| Package/agent installation and registration | Agent Registry (Runtime §7.3, §9) | ✅ Correctly deferred |
| Package verification ("Package verified" state) | This Agent Package Contract (Runtime §9 row 3 names it so) | ✅ Correctly self-claimed, matches Runtime's own reservation |
| Provider facts, credential classes, MCP server registration | Provider Registry §21.1, §24 | ✅ Referenced, not restated; MCP Declarations carry only `mcp_server_id` + `tool_contract_revision` |
| Capability resolution, policy order, approval binding, MCP security contract | Integration Gateway §12, §17, §18, §21 | ✅ Referenced, not restated |
| Six status dimensions, entity catalogue, Batch queue surface | Control Plane §7, §8, §9.8 | ⚠ Consumed by name, but the *projection* of two new typed fields (package lifecycle, package trust state) onto these dimensions is asserted without a verified mapping — see `P1-01` (§32) |
| Safety and approval layers | Safety Contract, Control Plane §16, Gateway §18 | ✅ Referenced, not restated |
| Twelve follow-up contracts | Named, not owned by this document | ✅ Correctly bounded, not fully specified |
| Batch Orchestration | Future, separate; Control Plane §9.8 is the consuming surface | ✅ Package-side declarations only, no implementation claimed |

**Result: 12 of 13 rows independently confirm; 1 row (Control Plane
projection) carries the review's sole P1 finding.** No second, incompatible
canonical owner was found for any concern — the ownership matrix is
otherwise unambiguous.

## 11. Terminology review

All 21 terms (§4) were checked for (a) internal self-consistency and (b)
non-collision with an existing canonical term of the same name used
differently elsewhere in the repository.

- **`Capability`** is explicitly reconciled against Integration Gateway
  §12's "one capability, one bounded operation" — the spec correctly states
  the two uses are "related but not identical" rather than silently
  presenting them as the same thing. Confirmed non-colliding.
- **`Skill`** is explicitly reconciled against Control Plane §7.2's `Skill`
  entity — the spec correctly states the entity is "that entity's
  frontend/observability projection... not its source of truth." Confirmed
  non-colliding, and confirmed the Control Plane `Skill` entity's own field
  list (`name, version, purpose, owner, allowed_projects, risk_class,
  validation_state`) is untouched.
- **`Package Registry`** vs. **`Agent Package Store`** — the reconciliation
  text was checked for internal use elsewhere in the document; both terms
  are used consistently with the stated split (Registry = discovery/index/
  trust; Store = artifact storage) in every other section that mentions
  either term (§5, §9, §16). No drift found.
- **`Provider Pack`** — confirmed as a genuinely unrelated, pre-existing
  term (`MELLYCORE_CYBERSECURITY_PROVIDER_PACK_SPEC_001`,
  `MELLYCORE_MARKETING_PROVIDER_PACK_SPEC_001`), and confirmed neither
  Provider Pack document was touched by the reviewed commit.

No terminology finding.

## 12. Identity and reused-field review

Every one of the eighteen reused Runtime §10.1 fields was checked
individually against Runtime's own table (read in full, not sampled): field
name, purpose, and fail-closed-on-absence behavior all match without
modification. `agent_definition_id`, `agent_package_id`, and
`package_revision_id` (Runtime §8.1) are used with Runtime's own stability
and opacity rules unchanged (§7.2 rules 1–3 restate, not alter, Runtime §8.2
rules 5–6). No finding.

## 13. Package boundary review

Section 6.2's seven prohibited-content categories were checked against the
Safety Contract's own blocklist (`shared_context/SAFETY_CONTRACT.md`): "no
secrets," "no real API keys," "no provider tokens," "no `.env` values," and
"no account IDs" are each covered by category 1–3. No category in §6.2
narrows anything the Safety Contract already forbids; category 7
(self-authorized runtime permissions) is additive, not present in the
Safety Contract, and does not conflict with it. No finding.

## 14. Layout and manifest-relationship review

The nine-category layout model (§8.1) and the illustrative tree (§8.2) were
checked for the "illustrative, not implemented" label the task brief
required — present and repeated at both the section header and the tree's
own inline comment. The six manifest-relationship rows (§9) were each
checked for whether they fully specify a follow-up contract's internal
shape; none does — every row states only a reference identifier and a
revision requirement, consistent with the task brief's "define their
boundary, minimum references, and ownership" instruction. No finding.

## 15. Capability-declaration review

The five-state separation (§10.1) was tested against Runtime §9's "no state
implies the next" discipline by attempting to construct a case where a
declared capability becomes active without passing through all four
intermediate states: no such path exists in the document's own text, and
§10.2 rule 1 explicitly requires all five simultaneously. Confirmed
structurally equivalent to Runtime's own nine-state separation in rigor. No
finding.

## 16. Permission and approval review

All twelve categories (§11.1) were checked for a default-deny statement:
present collectively in §11.1's header sentence and individually
unqualified in every row. One row's *citation*, not its substance, is
flagged: row 3 (shell execution) and two other locations cite Provider
Registry §24.2's `operator_only` pattern by analogy for concerns §24.2 does
not itself govern (§24 is scoped to MCP and restricted-tool records only,
not generic shell execution or generic package suspension). See `P2-01`
(§32). The default-deny outcome itself is not affected — the citation issue
is attribution, not authorization strength.

## 17. Dependency review

Section 12.2 rule 2 states an unresolved dependency "denies package
instantiation eligibility (§16)... with `DEPENDENCY_UNRESOLVED`." Checked
against §16's own stage table: instantiation eligibility is stage 5, owned
by "Agent Runtime," while dependency-declaration validation is explicitly
this contract's own concern under §18.1 layer 4 ("Dependency validation").
The document does not state whether `DEPENDENCY_UNRESOLVED` is raised at
this contract's own validation time (§18, this contract's owned concern) or
at Runtime's later instantiation-eligibility time (§16 stage 5, Runtime's
owned concern) — both readings are textually available. See `P2-02` (§32).

## 18. Provider-agnostic compatibility review

The six-row projection table (§13.2) was checked against Runtime §11.1's
closed set: identical membership, no seventh framework introduced, and the
document correctly restates Runtime §11.3's "architectural planning
position, not a verified capability test" caveat rather than upgrading it.
One row (`claude_code`) was checked for substantive content beyond the §4
terminology footnote it restates; it adds no new compatibility fact. See
`P3-01` (§32) — editorial, not a correctness defect.

## 19. Skill/Command/Hook/Plugin/MCP review

Each of the five rows in §14's table was checked for the six columns the
task brief required (declarative purpose, ownership boundary, validation
expectation, activation boundary, security implication, future registry) —
all six present in all five rows. The MCP Declaration row was checked in
depth against Provider Registry §24.1's exact record-field list and against
Gateway §21's phase model: the reviewed document correctly restricts itself
to two reference fields (`mcp_server_id`, `tool_contract_revision`) and
introduces no third field that would duplicate a §24.1 record field.
Confirmed non-duplicating.

One gap: §14's Command row requires "collision detection" against reserved
operator command names, and §24 repeats "command shadowing" as a named
threat, but §18.1's nine validation layers do not name reserved-command
collision detection under any specific layer. See `P2-03` (§32).

## 20. Shared Context review

All eight rules (§15) were checked against the Context Gate's actual
admission requirements (`shared_context/CONTEXT_GRAPH_SCHEMA.md` §2.1's
`source_refs`-must-be-non-empty rule, cited correctly at §15 rule 3) and
against Runtime §17's seven-operation model (cited correctly, unmodified, at
§15 rule 5). No rule in §15 grants a package-derived write path the Context
Gate does not already require for any other source. No finding.

## 21. Runtime-interaction review

The nine-stage table (§16) was checked against Runtime §9's nine
package/runtime separation states for a 1:1 or clearly-stated correspondence
at each stage; stages 1–2 correspond to Runtime states 2–3, stages 5–6
correspond to Runtime states 7–8, and stage 9 is explicitly new (not a
Runtime state) and explicitly attributed to a future owner. No stage claims
an authorization Runtime §14's eleven facts do not already gate. No finding
beyond the projection issue already raised at stage 7 (`P1-01`, §32, since
stage 7 is exactly where the unmapped lifecycle projection is invoked).

## 22. Package-lifecycle review

This is the section carrying the review's principal finding. The eleven
states (§17.1) were checked individually against Control Plane §8.1's six
closed enum vocabularies for a legal, unambiguous projection target:

| Package lifecycle state | Best candidate projection | Legal in Control Plane §8.1? |
| --- | --- | --- |
| `draft` | `lifecycle_status:draft` | ✅ legal |
| `submitted_for_validation` | `lifecycle_status:queued` (unstated) | ⚠ plausible, not stated |
| `validation_failed` | `lifecycle_status:failed` | ✅ legal |
| `validated` | `lifecycle_status:ready` (unstated) | ⚠ plausible, not stated |
| `awaiting_operator_approval` | `approval_state:awaiting_approval` | ✅ legal |
| `approved` | `approval_state:approved` | ✅ legal |
| `published` | no candidate stated | ❌ no legal member fits without interpretation |
| `installed_reference` | no candidate stated | ❌ no legal member fits without interpretation |
| `deprecated` | no legal `lifecycle_status` member named `deprecated` exists | ❌ unmapped |
| `revoked` | `approval_state:revoked` | ✅ legal |
| `retired` | no legal `lifecycle_status` member named `retired` exists; closest is `historical`, unstated | ❌ unmapped |

Four of eleven states have no stated, legal projection target, and the
document never provides the row-by-row mapping table Runtime §12.2 provides
for its own seventeen `run_state` values — it asserts the *pattern* exists
("may project one-directionally... exactly as `run_state` already does")
without doing the mapping work the precedent required. The same defect
recurs for the seven trust-state categories (§19.1) against `evidence_state`
and `approval_state`: `local`, `first_party`, `third_party`, `imported`, and
`generated` have no stated legal target in either dimension's closed
vocabulary. See `P1-01` (§32).

## 23. Validation-model review

The nine layers (§18.1) were checked for the task brief's required
distinction ("clearly distinguish validation success from execution
authorization"): §18.2 states this explicitly and correctly ties it back to
Runtime §9's own state separation. Each layer's trigger condition is
internally consistent with the error class it corresponds to in §21 (layer
7 ↔ `PACKAGE_BOUNDARY_VIOLATION`/safety failure; layer 3 ↔
`REFERENCE_UNRESOLVED`; layer 4 ↔ `DEPENDENCY_UNRESOLVED`), except the
command-collision check identified in §19 above, which has no explicit
layer. No new finding beyond `P2-03`.

## 24. Trust-and-provenance review

Checked for the task brief's explicit instruction not to claim
cryptographic signing exists: §19.2 states this correctly and unambiguously
("No key management, signature format, or trust-root implementation exists
or is authorized by this document"). The seven categories were checked
against `package_provenance` (Runtime §10.1, reused) for whether the
contract invents a second, competing provenance field: it does not — §19
builds the trust vocabulary on top of the existing field rather than beside
it. No finding beyond the projection gap already counted under `P1-01`.

## 25. Observability review

The eleven projections (§20.1) were checked against Control Plane §7.1's
common entity contract and against the rendering rule in §20.2 (no
projection may synthesize a universal "healthy" state, restated correctly
from Control Plane §8.2). Projection 9 ("Activation status") was checked
for whether it could be misread as `availability_status:available`; the
document's own text ("never implying authorization by itself") heads this
off explicitly. No new finding.

## 26. Error-taxonomy review

All fifteen classes (§21) were checked for a unique trigger condition (no
two classes share an identical trigger description) and for whether each is
referenced from at least one other section of the document: all fifteen are
referenced elsewhere. `CONTRACT_VERSION_INCOMPATIBLE` and
`REVISION_IMMUTABILITY_VIOLATION` were checked against §22's versioning
rules and found consistent. No finding.

## 27. Versioning review

Section 22's seven rules were checked for a defined `contract_version`
value the document itself declares (`1.0`, per its own header) and for
whether "additive" vs. "breaking" change criteria are objectively
distinguishable from the rules given: they are (a required-field removal or
narrowing is unambiguously breaking; a new optional field is unambiguously
additive). No finding.

## 28. Batch-compatibility review

Section 23's seven declarations were checked against Control Plane §9.8's
explicit prohibition on the labels "Run," "Start," "Execute," and "Launch":
none of those four words appears anywhere in §23 as a control label (they
appear only in prose describing what is *not* authorized). Checked against
the task brief's explicit instruction "do not specify Batch Orchestration
itself as implemented": §23's opening sentence states this correctly. No
finding.

## 29. Security-threat review

All twelve threats (§24) were checked against the task brief's required
list — prompt injection, malicious hooks, command shadowing, dependency
confusion, undeclared network access, secret exfiltration, filesystem
escape, privilege escalation, plugin impersonation, provenance spoofing,
context poisoning, validator bypass — all twelve present, each with a
mitigation posture that cites a specific section rather than asserting
safety in the abstract. No finding beyond the command-shadowing/§18 gap
already counted under `P2-03`.

## 30. Follow-up-contract review

All twelve items (§26) were checked against the task brief's required
minimum list (Agent Manifest, Capability Contract, Skill/Hook/Command/
Plugin/MCP Registries, Package Validation, Package Lifecycle, Package
Distribution, Package Repository, Batch Orchestration compatibility review)
— all present, none assigned a task ID (correctly deferred to Operator
sequencing per the reviewed document's task report §7). No finding.

## 31. Acceptance-criteria replay

All fourteen criteria from the reviewed document's own §27 were replayed
against its actual text:

| # | Criterion | Result |
| --- | --- | --- |
| 1 | All 29 sections present | ✅ |
| 2 | ≥19 terminology entries | ✅ (21) |
| 3 | No concern owned by more than one document | ⚠ 12/13 — see `P1-01` |
| 4 | Every prohibited content category maps to a validation layer and error class | ✅ |
| 5 | Capability/permission/dependency declarations are requests, never grants | ✅ |
| 6 | Five-state capability separation and eleven-state lifecycle do not collide with Runtime's states | ✅ (no collision found — but see `P1-01` for the *projection*, a distinct concern from collision) |
| 7 | No framework named canonical owner | ✅ |
| 8 | Every asset type states all six required attributes | ✅ |
| 9 | Shared Context interaction does not weaken the Context Gate | ✅ |
| 10 | Batch compatibility declares requirements only | ✅ |
| 11 | All twelve security threats addressed | ✅ |
| 12 | Non-goals and follow-ups internally consistent | ✅ |
| 13 | No implementation claimed anywhere | ✅ |
| 14 | Metrics table matches actual counts | ✅ (§9.1) |

**Thirteen of fourteen self-declared acceptance criteria hold exactly as
claimed; criterion 3 holds for 12 of 13 ownership rows.** The document's own
acceptance criteria were not gamed to declare success; criterion 3's own
wording ("every concern... cites its canonical owner") is what exposes
`P1-01`, since a projection *claim* onto an owner's vocabulary without that
owner's vocabulary actually accommodating it is a partial ownership gap, not
a fully cited one.

## 32. New findings

### P0 — Critical

**None.** No direct credential or provider path, no cross-tenant execution
possibility, no canonical Shared Context mutation bypass, no authorization or
approval bypass, no secret exposure, and no unsafe consequential retry was
found anywhere in the reviewed document.

### P1 — Blocking

**P1-01 — Package lifecycle and trust-state projection claims are unmapped
against Control Plane's closed enum vocabularies.**

§17.1 and §19.1 each assert that their own typed field (package lifecycle
state; package trust state) "may project one-directionally onto" specific
Control Plane §8.1 dimensions (`lifecycle_status`/`approval_state`/
`evidence_state`), "exactly as the Agent Runtime's `run_state` projects onto
`lifecycle_status`." That precedent (`[[../decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001]]`)
is a *specific, verified, row-complete* mapping: Runtime §12.2 provides all
seventeen rows, Review 002 independently recounted every row, and the one
member the mapping needed (`running`) was added to `lifecycle_status`'s own
closed set through an explicit, additive owner amendment.

The reviewed document does neither. §22 of this review (Package-lifecycle
review) shows four of eleven package lifecycle states — `published`,
`installed_reference`, `deprecated`, `retired` — have no legal target value
in `lifecycle_status`'s twelve-member closed set (`draft`, `planned`,
`queued`, `ready`, `active`, `running`, `blocked`, `completed`, `failed`,
`cancelled`, `superseded`, `historical`), and five of seven trust-state
categories — `local`, `first_party`, `third_party`, `imported`,
`generated` — have no legal target in `evidence_state`'s six-member set
(`canonical`, `static_demo`, `simulated`, `future_live`, `partial`,
`unknown`) or `approval_state`'s six-member set. No amendment to Control
Plane exists or is proposed anywhere in the reviewed document; the
projection is invoked as though it already holds.

*Impact:* an implementer of §20's observability projections cannot render a
Package Instance's lifecycle or trust state through the claimed mechanism
without either inventing new Control Plane enum members (which would
require an owner amendment this document never makes) or reinterpreting
four-plus states as some existing member by guesswork — precisely the
"cannot render... without either violating the canonical owner or
reinterpreting this specification" impact class the Agent Runtime
architecture's own `P1-01` finding described.

*Classification:* P1 — canonical ownership/projection conflict, following
the identical pattern and identical remediation shape (a minimal, additive,
owner-participated amendment, or an explicit statement that these states do
not project and are typed-entity-data only per Control Plane §7.1's general
allowance) already used to close the Agent Runtime's own `P1-01`.

### P2 — Material, non-blocking

**P2-01 — Provider Registry §24.2's `operator_only` pattern is cited by
analogy for concerns §24 does not itself govern.**

§11.1 row 3 (shell execution), §16 stage 9 (termination/suspension
projection), and §17.3 rule 2 (revocation inertness) each cite or pattern-
match Provider Registry §24.2/§24.3, which is explicitly scoped to "MCP
servers and restricted tools" record types — not generic package shell-
execution permission, generic package suspension, or generic package
revocation. The borrowed pattern is a defensible design choice and does not
weaken the default-deny outcome in any of the three locations, but citing a
scoped owner section as the source of a pattern applied outside that
section's stated scope risks a future reader treating Provider Registry §24
as though it already governs non-MCP package concerns, which it does not
and does not claim to.

*Impact:* non-blocking — no capability is granted, weakened, or
misauthorized as a result; this is an attribution clarity issue, resolvable
by rephrasing the three citations as "modeled on" rather than "reused from"
the Provider Registry pattern, or by moving the pattern's statement into
this contract's own text without a scoped-owner citation.

**P2-02 — The evaluation point for `DEPENDENCY_UNRESOLVED` is ambiguous
between this contract's own validation time and the Agent Runtime's
instantiation-eligibility time.**

§12.2 rule 2 ties `DEPENDENCY_UNRESOLVED` to §16's instantiation-eligibility
stage (Runtime-owned), while §18.1 layer 4 assigns dependency validation to
this contract's own nine-layer validation model. Both readings are textually
available and the document does not state which is authoritative or whether
both must independently agree.

*Impact:* non-blocking — either reading is fail-closed (an unresolved
dependency denies either way), so no authorization bypass exists; a future
Package Validation or Package Lifecycle follow-up contract needs this
resolved before an actual validator could be built consistently.

**P2-03 — Reserved-command collision detection is required by §14 and §24
but not enumerated among §18's nine validation layers.**

§14's Command row and §24's "command shadowing" threat both require
structural detection of a package-declared command name colliding with a
reserved operator command name (`ROADMAP.md`'s Planned Commands), but none
of §18.1's nine named layers (structural, schema/contract, reference,
dependency, capability, compatibility, safety, provenance, policy)
explicitly claims this check. It most plausibly belongs to layer 1
(structural) or layer 7 (safety), but the document does not say which.

*Impact:* non-blocking — the requirement itself is stated clearly enough
that a future Package Validator implementer would not miss it, but the
missing cross-reference is exactly the kind of internal-consistency gap
this review's method is designed to surface before it compounds in a
follow-up contract.

### P3 — Editorial / maintainability

**P3-01 —** §13.2's `claude_code` compatibility-projection row restates the
§4 terminology footnote about shared-shape-not-shared-ownership rather than
adding a new, `claude_code`-specific compatibility fact, unlike the other
five rows in the same table.

**P3-02 —** No error class in §21 is explicitly dedicated to the
reserved-command-collision case identified in `P2-03`; an implementer would
have to infer whether `MANIFEST_MALFORMED` or `SCHEMA_VIOLATION` applies.

**P3-03 —** §7.1's `license_metadata` field states "absence is legal
metadata, never a security fact" but is the only one of the twelve identity
fields whose absence-handling is stated in prose rather than being covered
by the same fail-closed table format §7.1 uses for the other eleven fields
implicitly via §7.2's rules.

## 33. Finding counts

| Severity | Count | IDs |
| --- | --- | --- |
| **P0** | **0** | — |
| **P1** | **1** | `P1-01` |
| **P2** | **3** | `P2-01`, `P2-02`, `P2-03` |
| **P3** | **3** | `P3-01`, `P3-02`, `P3-03` |

## 34. Gate decision

### `FAIL_REMEDIATION_REQUIRED`

One P1 finding exists. Per the gate rule already established by the Agent
Runtime architecture's own Review 001 (§47 there) and reused unchanged
here, **any P0 or P1 finding requires `FAIL_REMEDIATION_REQUIRED`; PASS is
impossible with a P1 outstanding.** The specific gate condition not met:
**canonical ownership is not unambiguous** for the package-lifecycle and
trust-state projection claim (`P1-01`).

No P0 exists: no direct credential or provider path, no cross-tenant
execution possibility, no canonical Shared Context mutation bypass, no
authorization or approval bypass, no secret exposure, and no unsafe
consequential retry was found. The three P2 findings are each independently
fail-closed and do not, on their own, block the gate; they are recorded as
required remediation alongside `P1-01` because a remediation pass touching
the same sections is the efficient place to close them, following the same
practice the Agent Runtime remediation used for its own P2/P3 findings.

## 35. Implementation status (unchanged by this review)

| Dimension | State |
| --- | --- |
| Agent Package Store, Package Registry, Package Validator | `NOT_IMPLEMENTED` |
| Agent Packages | `NONE_EXIST` |
| Packages executed | **Zero** |
| Agent Runtime | Unchanged; still `NOT_IMPLEMENTED`; Review 002's `PASS_WITH_NON_BLOCKING_FINDINGS` gate is not reopened by this review |
| Every canonical cross-check source (§7) | Re-verified byte-identical to its recorded baseline after this review's commit (git blob IDs match §7 exactly) |

This review performed exactly one class of repository mutation: creating
this research record, its task report, and the bounded state-synchronization
edits named in §36. No specification, spec-adjacent code, registry,
validator, loader, or Skill/Hook/Command/Plugin/MCP mechanism was created,
modified, or executed.

## 36. Exact next task

`MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001` — remediate `P1-01`
(and, in the same pass, `P2-01` through `P2-03` and `P3-01` through
`P3-03`) in the reviewed specification, following the same governing rule
the Agent Runtime remediation used: **the existing canonical owner wins
unless it provably cannot represent the required semantics, and no seam is
hidden by redefining another subsystem's vocabulary inside this contract.**
For `P1-01` specifically, the two available remediation shapes are (a) a
minimal, additive Control Plane amendment adding the missing enum members,
mirroring exactly how the Agent Runtime remediation added `running` to
`lifecycle_status`, or (b) an explicit statement, consistent with Control
Plane §7.1's own general allowance for typed domain fields, that package
lifecycle and trust state are typed entity data only and do not project onto
any of the six canonical dimensions at all. Not started, not authorized by
this review.

## 37. Explicit non-authorizations

This review authorizes none of: any edit to the reviewed specification or
its task report; any Agent Package Store, Package Registry, Package
Validator, loader, or registry implementation; any Control Plane amendment;
any package, agent, skill, command, hook, plugin, or MCP execution; any
provider connection, credential configuration, or model-provider call; any
push, pull request, merge, or remote branch; any MellyTrade interaction.

The Agent Runtime architecture gate (Review 002,
`PASS_WITH_NON_BLOCKING_FINDINGS`) is not reopened. The Agent Package
Contract specification itself is **not accepted** — this review's
`FAIL_REMEDIATION_REQUIRED` decision means it remains exactly as unaccepted
as it was before this review, now with a documented reason. Framework
Bridge Contract, Shared Context Bridge, Agent Runtime Scaffold, first Agent
Package, Cross-Agent Smoke, Integration Review, and all twelve Agent Package
follow-up contracts remain blocked. The global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` is unchanged, not
reordered, and not reinterpreted.

## 38. Validation evidence

- `git diff --check` — recorded in the final execution report.
- `py -3.9 scripts/validate_project_state.py` — recorded in the final
  execution report.
- Every canonical cross-check source's Git blob ID (§7, §9) was
  re-hashed after this review's commit and found unchanged.
- Independently recounted dimensions: 24 of 24 match the reviewed
  document's own claims exactly (§9.1) — zero count discrepancies, a
  materially different starting condition from the Agent Runtime
  architecture's own first review.
- Acceptance-criteria replay: 13 of 14 hold exactly; criterion 3 holds for
  12 of 13 ownership rows (§31).
- `pytest`: `NOT_RUN` — no source or test file changed; not claimed passing.
  Black, flake8, and mypy: not run, not claimed passing.

## 39. Amendment and supersession

This review record is superseded only by a later, independently authored
review of the same or a remediated version of the specification. It does
not itself amend the reviewed specification, any canonical owner document,
or any prior Agent Runtime review record.

## 40. References

### 40.1 Reviewed

- `docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md`
- `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001.md`

### 40.2 Canonical cross-check sources

Listed in full in §7.

### 40.3 External

None.
