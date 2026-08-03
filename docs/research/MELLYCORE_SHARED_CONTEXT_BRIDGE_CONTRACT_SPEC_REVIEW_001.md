# MellyCore Shared Context Bridge Contract Spec — Independent Review 001

**Review task ID:** `MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-REVIEW-001`
**Reviewed artifact:** `docs/specs/MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_SPEC_001.md`
**Reviewed contract identity:** `MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_001`, version **1.0**
**Reviewed commit:** `d3f8b737e67dd3e0afed76f15b1e50be41f2db61` (short `d3f8b73`)
**Reviewed subject SHA-256 (first 16):** `57cdbdf663778361` — 77,499 bytes, 1,445 lines
**Review branch:** `docs/mellycore-shared-context-bridge-contract-spec-review-001`

**Gate decision:** `PASS_WITH_NON_BLOCKING_FINDINGS` (§13).
**P0 = 0, P1 = 0, P2 = 8, P3 = 2.**

The specification is accepted as a **documentation contract only**, under the ten
constraints recorded in §12. **No Shared Context Bridge, canonical mutation
engine, context storage, database, vector store, memory service, compression
implementation, validation implementation, or proposal-lifecycle runtime
exists.** Empirical framework validation remains `NOT_PERFORMED`. All seven
upstream P2 findings remain **open and contained**.

---

## 1. Review independence and method

This review was performed by a party that did not author the specification. The
specification's own task report
(`docs/tasks/MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-001.md`, SHA-256
`62d39a6f3a9709c7`) was read in full but **treated as an unverified claim set,
never as evidence**. Its stated outcome
(`SHARED_CONTEXT_BRIDGE_CONTRACT_SPECIFIED_UNVERIFIED`), its metrics, its
containment assertions, and its error-taxonomy assertions were each independently
reconstructed from the reviewed document and the canonical owner documents.

Method:

1. **Section structure** extracted mechanically by regular expression over `^## N. `.
2. **Every table row counted programmatically** by parsing markdown table blocks
   and attributing each to its enclosing section; ordered-list metrics counted by
   parsing `^\d+\. ` items within measured line ranges.
3. **Owner lists extracted from the owner documents themselves**, not from the
   reviewed spec's description of them: Agent Runtime §17.1 (seven operations),
   §17.2 (ten fields), §17.3 (five rules), §17.4 (six conditions), §18 (six memory
   categories), §19 (seventeen trace fields), §33 (49 classes + six adopted Gateway
   classes); `CONTEXT_GRAPH_SCHEMA.md` §5 (nine relation types); Control Plane §7.1,
   §7.2, §8.1 (six status dimensions), §9.3; Integration Gateway §25.2; Agent
   Package §21; Framework Bridge §23.2/§23.3; Context Ingestion Gate §3, §6, §7.
4. **Error-taxonomy collision audit run mechanically**: all `UPPER_SNAKE_CASE`
   backtick-delimited tokens were extracted from eight owner documents into a
   union index, then tested against the eleven bridge-owned classes for exact-name
   collision and, separately, for semantic-neighbour stems.
5. **Absence tested with explicit checklists**, not prose reading: each owner
   concept was grepped for by name in the reviewed spec, and a zero-hit result was
   recorded as an absence finding rather than assumed intentional.
6. **Overclaim and normative-modal scans** run over the whole document.
7. **No online documentation was consulted. No empirical framework testing was
   performed. No validator was claimed to pass that did not run.**

### 1.1 Independence caveat recorded honestly

Two areas were reviewed by document inspection alone and cannot be discharged by
any documentation review: whether a future implementation actually honours the
fail-closed rules, and whether the deferred contracts of §46 will preserve these
boundaries. Both remain future gate obligations, not findings against this text.

---

## 2. Repository baseline and Git-scope protection

`C:\` is itself a separate Git repository containing unrelated local changes.
**Every Git command in this review was explicitly scoped** with
`git -C "C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios"`. No unscoped Git
command ran. The outer `C:\` repository was never inspected, staged, reset,
cleaned, or committed.

| Baseline item | Expected | Observed | Result |
| --- | --- | --- | --- |
| Repository root | `…/01_Repo/mellycore-aios` | identical | ✅ |
| Starting branch | `docs/mellycore-shared-context-bridge-contract-spec-001` | identical | ✅ |
| Full HEAD | `d3f8b737e67dd3e0afed76f15b1e50be41f2db61` | identical | ✅ |
| Short HEAD | `d3f8b73` | identical | ✅ |
| Commit subject | `docs: define shared context bridge contract` | identical | ✅ |
| Worktree | clean | clean (`git status --short` empty) | ✅ |
| Upstream tracking | none | `fatal: no upstream configured` | ✅ |
| Recorded outcome | `SHARED_CONTEXT_BRIDGE_CONTRACT_SPECIFIED_UNVERIFIED` | recorded in `RUN_QUEUE.md`, `PROJECT_STATE.md`, `AGENT_HANDOFF.md` | ✅ |
| Review 001 artifacts | absent | absent (both paths) | ✅ |
| Review 001 branch | absent | absent | ✅ |
| Implementation | none | zero code references in `scripts/`, `tests/`, `site/` | ✅ |

Remotes `origin` and `clean-origin` exist and **neither was contacted**. No fetch,
pull, push, PR, merge, or deployment occurred at any point.

### 2.1 Implementation-absence evidence

A repository-wide search for `shared_context_bridge`, `SharedContextBridge`,
`context_envelope`, `context_proposal`, `canonical_mutation`, and
`mutation_eligib` across `scripts/`, `tests/`, and `site/` returned **zero
matches**. The tracked tree is 229 markdown, 69 Python, 26 JSON, 5 CSS, 2 HTML,
1 JS files; no Python module, test, or fixture implements or references any
bridge concept.

### 2.2 Immutable review subjects

SHA-256 (first 16 hex) recorded **before** any artifact was written and re-verified
after commit (§14.4). Every file below was byte-identical at both points.

| File | SHA-256 (16) |
| --- | --- |
| `docs/specs/MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_SPEC_001.md` | `57cdbdf663778361` |
| `docs/tasks/MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-001.md` | `62d39a6f3a9709c7` |
| `docs/specs/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001.md` | `bf5f47d45f11326f` |
| `docs/research/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_REVIEW_001.md` | `20bc87bdd7644fb4` |
| `docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md` | `020b4a63fec214c5` |
| `docs/research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_001.md` | `5d88cb9815990197` |
| `docs/research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_002.md` | `d459d9af7b28b559` |
| `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md` | `92fe7d83c9f025f1` |
| `docs/research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_001.md` | `9c8bf2c86bc03fec` |
| `docs/research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_002.md` | `c09012cf3680c03d` |
| `docs/specs/MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001.md` | `66941687467a3a50` |
| `docs/specs/MELLYCORE_CONTEXT_GATE_IMPLEMENTATION_SPEC_001.md` | `8ccbf09fdf453f30` |
| `docs/specs/MELLYCORE_CONTEXT_INGESTION_GATE_SPEC_001.md` | `b65d73e75af290fa` |
| `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` | `134afb244ad3700d` |
| `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` | `5999c380d2f32252` |
| `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md` | `327d3715c884015f` |
| `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md` | `a9b4b91ed4dd64e6` |
| `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` | `5d622f44fedc216f` |
| `shared_context/CONTEXT_GRAPH_SCHEMA.md` | `3321c2eafaa08586` |
| `shared_context/CONTEXT_PACK_GENERATOR_SPEC.md` | `a7672db74862501d` |
| `shared_context/SAFETY_CONTRACT.md` | `d7ad99ec0335fd7f` |
| `shared_context/MODEL_ROUTING.md` | `1c18f755a8f030c3` |
| `shared_context/VALIDATION.md` | `cc89fc215340d69f` |
| `shared_context/DECISIONS.md` | `51de81365c5c2f1a` |
| `shared_context/CROSS_AGENT_CONTEXT.md` | `40880fc36a261cf9` |

---

## 3. Independent canonical owner map

Reconstructed from the owner documents, not from §3 of the reviewed spec.

| Concern | Canonical owner (verified) | Bridge claim | Independent verification method | Result |
| --- | --- | --- | --- | --- |
| Canonical Shared Context state | Shared Context Layer; Context Gate; Control Plane §9.3 | Consumes; proposals terminate at the gate | Read Runtime §17 preamble: "**Agents never write it.**" Read bridge §4.1, §4.2, §11 | ✅ Consistent |
| Seven context operations | Agent Runtime §17.1 | Consumes by name; defines no eighth | Extracted all seven names from §17.1; confirmed bridge names them and adds none | ✅ |
| Required context-record metadata | Agent Runtime §17.2 (ten fields) | References unchanged | Extracted the ten field names; bridge envelope cites `context_class`, `sensitivity_level`, `retention_policy`, `confidence` by owner name | ✅ (four envelope slots use different local labels, each disclosed inline) |
| Snapshot staleness policy | Agent Runtime §17.4 (six conditions) | Consumes unchanged | Read all six conditions and five rules; bridge §25 defines no competing rule and cites §17.4 rules 2 and 4 | ✅ |
| Memory categories | Agent Runtime §18 (**six**) | Maps eight scopes on by semantic name | Extracted all six category names; compared row-by-row against bridge §19's eight rows | ⚠ **`NEW-P2-05`** — two rows map to no §18 category; one collapses categories 5 and 6 |
| Memory layers (operator surface) | Control Plane §9.3 (**five** layers) | Not referenced | Read §9.3's "Memory layers" row: immutable evidence, working memory, task memory, project memory, long-term knowledge | ⚠ Third taxonomy unaddressed — folded into `NEW-P2-05` |
| Context-flow trace record | Agent Runtime §19 (seventeen fields) | References as transfer evidence; adds no eighteenth | Counted §19's table: 17 rows; bridge §8 rule 3 and §41 rule 2 reference it, add nothing | ✅ |
| Graph relation types | `CONTEXT_GRAPH_SCHEMA.md` §5 (**nine**) | Uses only existing relations | Extracted all nine; bridge §15 uses six (`references`, `supersedes`, `contradicts`, `produced_by`, `validated_by`, `belongs_to`), invents none, reverses none | ✅ |
| Provenance, `sensitivity_level`, `allowed_use` | Context Provenance and Sensitivity spec; `SourceRef` | Preserves and augments; defines no vocabulary | Bridge §14, §17 define no scale and cite the owner | ✅ |
| Context ingestion and admission | Context Ingestion Gate; Context Gate Implementation | Consumes; MUST NOT bypass, weaken, replace | Ingestion Gate §6 defines **five** validation outcomes in precedence order and §7 defines **nine** refusal codes R1–R9; none is named anywhere in the bridge | ⚠ **`NEW-P2-03`** |
| Context entities (`ContextPacket`, `ContextSource`, `MemoryRecord`) | Control Plane §7.2, §9.3 | `ContextSource` cited once; `ContextPacket` and `MemoryRecord` never | Grepped all three names in the reviewed spec: 1 / 0 / 0 hits | ⚠ **`NEW-P2-06`** |
| Six status dimensions | Control Plane §8.1 | Adds none; projects nothing | Extracted all six dimension names; bridge §12 and §40 declare no projection; all ten phase names are `proposal_`-prefixed | ✅ |
| Runtime error taxonomy | Agent Runtime §33 (**49** classes, one-class-per-row invariant) | Consumes nine; adds eleven genuinely absent | Extracted the 49; plus the six explicitly Gateway-owned adopted classes | ⚠ **`NEW-P2-01`**, **`NEW-P2-02`** |
| Provider-boundary error taxonomy | Integration Gateway §25.2 | Audited per §29 preamble | Extracted §25.2; `CONTENT_QUARANTINED` and `INJECTION_SUSPECTED` found; neither reconciled in the bridge | ⚠ **`NEW-P2-01`**, **`NEW-P2-02`** |
| Package error taxonomy | Agent Package §21 | Consumes `CONTEXT_CLASS_UNDECLARED` | Verified §21 defines it (line 873) | ✅ |
| Framework Bridge taxonomy | Framework Bridge §23.3 (nine classes) | Emits none of them | Verified `PROJECTION_UNSUPPORTED` / `BRIDGE_UNSUPPORTED_BEHAVIOR` appear only in denials; `PROJECTION_LOSS_UNACCEPTABLE` never appears | ⚠ **`NEW-P2-01`** (loss-class neighbour) |
| Capability resolution, policy order, approval binding | Integration Gateway §12, §17, §18 | References decisions; grants nothing | All three sections verified to exist; bridge §9, §30, §31 reference rather than evaluate | ✅ |
| Provider facts, MCP server records | Provider Registry §21.1, §24, §24.2 | References; authorizes nothing | All three verified; bridge §35, §37 preserve `output_trust_level: untrusted` | ✅ |
| Model selection and routing | Model Router (Runtime §23; `MODEL_ROUTING.md`) | References only | Bridge §35 rules 5–6 select nothing | ✅ |
| Context compression contract | Future, separate task | Bounds safety envelope only | Bridge §21 specifies no algorithm, ratio, model, or implementation | ✅ |
| Observability, audit, cost | Control Plane; AI Operations §5; Operations Data Contract | Supplies projections and evidence | Bridge §40 adds no dimension and defines no cost schema | ✅ |
| Batch compatibility | Future Batch Orchestration contract | Declares compatibility only | Bridge §39 authorizes no execution, mutation, push, PR, merge, or deployment | ✅ |

**No owner conflict was found that could not be resolved to a single owner.** The
findings below are ownership **incompleteness** — an owner not cited, a neighbour
not reconciled, a mapping not stated — not two documents asserting incompatible
authority.

### 3.1 Out-of-scope owner observation (not a finding against this contract)

Agent Package Contract §21 states "Fifteen stable rejection classes" above a table
containing **sixteen** rows. This is recorded in Agent Package Review 002 as
`NEW-P3-02` and is an upstream defect. It is **not** re-adjudicated here, does not
affect the Shared Context Bridge's consumption of `CONTEXT_CLASS_UNDECLARED`, and
no correction to any owner document was made by this review.

---

## 4. Document metrics — full independent recount

All 34 rows of §48 were recomputed mechanically. **All 34 reproduce.**

| # | Metric | Reported (§48) | Independently measured | Match | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Specification sections | 50 | 50 | ✅ | `^## N. ` headings, numbered 1–50 with no gap or duplicate |
| 2 | Terminology entries | 31 | 31 | ✅ | §2 table rows |
| 3 | Architectural ownership rows | 20 | 20 | ✅ | §3 table rows |
| 4 | Canonical-vs-projected register rows | 13 | 13 | ✅ | §4.3 table rows |
| 5 | Context identity fields | 14 | 14 | ✅ | §5.1 table rows, numbered 1–14 |
| 6 | Context envelope fields | 14 | 14 | ✅ | §6.1 table rows, numbered 1–14 |
| 7 | Selection requirements | 8 | 8 | ✅ | §7 ordered list, max index 8 |
| 8 | Projection prohibitions | 9 | 9 | ✅ | §8 ordered list, max index 9 |
| 9 | Projection eligibility preconditions | 12 | 12 | ✅ | §9 table rows |
| 10 | Read-boundary consumers | 10 | 10 | ✅ | §10 table rows |
| 11 | Write/mutation concepts | 5 | 5 | ✅ | §11 table rows |
| 12 | Proposal lifecycle phases | 10 | 10 | ✅ | §12 table rows |
| 13 | Return-path checks | 13 | 13 | ✅ | §13 table rows |
| 14 | Namespace categories | 10 | 10 | ✅ | §16 table rows |
| 15 | Secret prohibitions | 6 | 6 | ✅ | §18 ordered list, max index 6 |
| 16 | Memory scopes | 8 | 8 | ✅ | §19 table rows (count correct; mapping defective — `NEW-P2-05`) |
| 17 | Memory proposal elements | 8 | 8 | ✅ | §20 table rows |
| 18 | Compression prohibitions | 7 | 7 | ✅ | §21 ordered list, max index 7 |
| 19 | Transformation classes | 8 | 8 | ✅ | §22 table rows |
| 20 | Context-loss classes | 6 | 6 | ✅ | §23 table rows; four marked fail-closed |
| 21 | Quarantine conditions | 9 | 9 | ✅ | §28 table rows |
| 22 | Consumed rejection classes | 9 | 9 | ✅ | §29.1 table rows (count correct; one owner misattributed — `NEW-P2-02`) |
| 23 | Bridge-owned rejection classes | 11 | 11 | ✅ | §29.2 table rows |
| 24 | Validation layers | 13 | 13 | ✅ | §30 table rows |
| 25 | Mutation-eligibility conditions | 11 | 11 | ✅ | §31 table rows |
| 26 | Agent Runtime interaction stages | 10 | 10 | ✅ | §32 table rows |
| 27 | Batch compatibility declarations | 8 | 8 | ✅ | §39 table rows |
| 28 | Observability projections | 19 | 19 | ✅ | §40 table rows |
| 29 | Audit evidence questions | 9 | 9 | ✅ | §41 table rows |
| 30 | Security threats | 21 | 21 | ✅ | §42 table rows |
| 31 | Failure-closed conditions | 8 | 8 | ✅ | §44 ordered list, max index 8 |
| 32 | Non-goals | 20 | 20 | ✅ | §45 ordered list, max index 20 |
| 33 | Deferred dependencies | 13 | 13 | ✅ | §46 table rows |
| 34 | Acceptance criteria | 28 | 28 | ✅ | §47 ordered list, max index 28 |

**Zero count discrepancies.** The §48 metrics table is the strongest feature of
this document: it is the first contract in this track to carry one at drafting
time, it caught two drifts before commit, and it survives independent recount
intact. It correctly discharges Framework Bridge Review 001's `NEW-P3-01`.

---

## 5. Verdicts

### 5.1 Task and artifact identity — **PASS**

Task ID, contract identity, and version are internally consistent and match the
recorded state in `RUN_QUEUE.md`, `PROJECT_STATE.md`, `AGENT_HANDOFF.md`,
`ROADMAP.md`, `TASK_INDEX.md`, and `PROJECT_HISTORY.md`. Filename conventions
match the three prior contracts in this track. Section numbering is contiguous
1–50. The header states the document is **unverified and not accepted** pending
this review — accurate at the time of writing.

### 5.2 Architectural ownership — **PASS**

The contract owns only the exchange boundary: envelope, selection, projection
eligibility, return-path validation, quarantine, context loss, bridge rejection
classes, and per-consumer read boundaries. It takes ownership from no other
document. §3.1's precedence chain is additive-only ("MAY add requirements
stricter … MUST NOT subtract from any") and no rule in the document subtracts
from an owner. §50 rules 4–6 prohibit silent modification of an owner contract's
meaning through this document.

### 5.3 Canonical-versus-projected direction — **PASS** (load-bearing)

The permitted direction (§4.1) and the prohibited direction are both stated
explicitly. A full-document search found **no alternate or accidental
direct-write path**. Specifically verified:

- §4.2 rule 2 enumerates six non-admission events (framework use, agent return,
  framework session storage, package presence, tool emission, model generation,
  structural validation) and denies each.
- §4.2 rule 4: byte-identical round-trip is still returned content.
- §11 rule 4: "**No bridge, adapter, package, tool, provider, plugin, hook,
  command, MCP server, or batch worker holds mutation authority under any
  condition.**"
- §11 rule 5 prohibits escalation of kind (rejected proposal → mutation request).
- §31 rule 3 and §32 rule 3 keep canonical mutation with the canonical owner and
  outside the Runtime interaction table.
- §38 rule 1 covers plugins, hooks, skills, and commands.
- §39 prohibits Batch compatibility from authorizing Shared Context mutation.
- §33 rule 1: package declarations grant nothing.

**No P0 exists.** No canonical-context mutation bypass, cross-tenant path,
credential path, approval bypass, or secret-exposure path was found.

### 5.4 Context identity — **PASS**

Exactly **three** identities are minted (`context_envelope_id`, `projection_id`,
`proposal_id`), independently confirmed against §5.1's fourteen rows: the other
eleven are attributed to Shared Context Layer, Context Graph Schema, Agent Runtime
§8.1, Framework Bridge, Provenance spec, or Integration Gateway §18. Each minted
identity is necessary (envelope, projection act, and inward proposal are three
distinct objects with distinct lifetimes), non-overlapping, and correctly owned.
§5.2 rule 3 prohibits encoding namespace, tenant, sensitivity, or policy outcome
in an identity — matching Control Plane §7.1's "IDs MUST NOT encode mutable
state". §5.2 rule 5 prevents a `proposal_id` becoming a `context_item_id`.

### 5.5 Context envelope — **PASS with `NEW-P2-06`**

The envelope is explicitly logical (§6.1 preamble, §6.2 rule 6: no serialization,
encoding, transport, storage location, or persistence mechanism). It grants no
authority (§6.2 rule 2), carries no secret values (§6.2 rule 3), binds to exactly
one `permitted_consumer` (§6.2 rule 4), and cannot self-assert `validation_state`
(§6.2 rule 5). Absence of any required field denies projection (§6.2 rule 1).

The defect is not the envelope's content but its unreconciled overlap with Control
Plane §9.3's `ContextPacket` — see `NEW-P2-06`.

### 5.6 Selection and projection — **PASS with `NEW-P2-08`**

Selection is purpose-bounded, consumer-bounded, policy-aware, namespace-aware,
provenance-preserving, minimal, observable, and reproducible where required (§7,
eight requirements). **Unrestricted project-context requests fail closed**: §7
rule 1 rejects "all context", an unbounded namespace, and unscoped wildcards.
§7 rule 2 prevents selection expanding as a side effect of transformation,
compression, or retry. §7 rule 3 correctly separates selection from eligibility.

All nine projection prohibitions are present and none is qualified. §8 rule 2
correctly treats an inexpressible restriction as safety-relevant loss failing
closed. §8 rule 4 preserves point-of-use re-evaluation per Runtime §17.3 rule 1.

The "subtractive or equal" property (§8 rule 1) is normatively correct but is not
evaluated by any validation layer or eligibility precondition — see `NEW-P2-08`.

### 5.7 Projection eligibility — **PASS**

All twelve preconditions were reconstructed; each has an identified owner and a
deterministically available input. §9 rule 1 states eligibility does not imply
execution authorization; rule 2 forbids caching across consumers, purposes, or
namespaces; rule 4 states plainly "**There is no default-allow state**". Unknown
or unresolved policy denies (precondition 5, "never a default allow").

§9 rule 3 is notable: **an unvalidated framework profile cannot become
context-projection eligible here.** This is *stricter* than the Framework Bridge's
own position and correctly does not purport to close that contract's `NEW-P2-04`.

### 5.8 Read boundary — **PASS**

All ten consumer categories are bounded. **No category receives implicit access by
being declared, available, installed, or selected**: §10 rule 1 restates Runtime
§18 rule 1 ("Existence is not permission"); §10 rule 2 makes the tenant boundary
absolute and non-existence-revealing; §10 rule 3 forbids inferring the existence
of unreadable context. Per-subsystem sections reinforce this: §35 rule 8
(`provider selectable ≠ provider authorized`), §36 rule 3 (tool availability is
not authorization), §37 rules 6–7 (no automatic MCP connection, no implicit
trust), §38 rule 3 (declaration is never activation).

### 5.9 Write, proposal, eligibility, approval, mutation — **PASS** (load-bearing)

The five concepts of §11 are correctly separated, with "**No concept implies the
next**" stated at the head of the table and each row's canonical-state effect
given explicitly ("None" for the first four). Only concept 5 changes canonical
state and only the canonical owner may perform it.

Mutation eligibility (§31) requires all eleven conditions **simultaneously** for
the exact proposal, namespace, tenant, and consumer. Independently checked for
omissions: approval is present (condition 11), conflict is present (condition 6),
provenance is present (condition 3), quarantine exclusion is present (condition 9),
policy-decision reference is present (condition 10), snapshot currency is present
(condition 7). Integrity and transformation are covered transitively via condition
1 (all §30 layers) and condition 2 (§13's thirteen checks). §31 rules 1–2 keep
eligibility distinct from mutation and from Operator approval. **No optional
condition is treated as sufficient.**

### 5.10 Proposal lifecycle — **PASS with `NEW-P2-03`**

Exactly ten phases, stable identities, all `proposal_`-prefixed. No collision with
Agent Package lifecycle, Runtime `run_state`, Framework Bridge lifecycles, or
Control Plane's six dimensions — each independently checked. §12 explicitly
defines **no projection onto any Control Plane §8.1 dimension**, and §40 rule 1
forbids rendering bridge fields as `lifecycle_status`, `evidence_state`, or
`approval_state`. Terminal behaviour is stated for quarantine (§12 rule 3).
§12 rule 2 forbids inferring a phase from another's absence. §12 rule 4 honestly
defers the full transition-rule contract to §46 item 11.

The defect is the omission of the Context Ingestion Gate from the non-collision
claim — see `NEW-P2-03`.

### 5.11 Return-path validation — **PASS with `NEW-P2-04`**

All thirteen checks reconstructed. The untrusted posture holds across every listed
producer (agents, tools, frameworks, providers, plugins, hooks, MCP servers, batch
workers) and survives all five bypass temptations tested: first-party producer,
byte-identity (§13 rule 2, §4.2 rule 4), framework-reported success, structural
validation passing (§4.2 rule 3), and provenance being present (§14 rule 5,
"Provenance preserved does **not** mean content trusted"). §13 rule 3 forbids
treating returned content as instructions. §13 rule 4 ensures a validation failure
never itself mutates, fetches, installs, or resolves anything.

Check 6's `Reject or quarantine` disposition is non-deterministic — see
`NEW-P2-04`.

### 5.12 Provenance and lineage — **PASS**

Provenance is preserved and augmented across all nine named stages. §14 rule 1
states plainly that provenance "**MUST NOT be replaced with only the most recent
producer**"; augmentation appends and never overwrites the origin chain. §14 rule
2 keeps `source_refs` non-empty at every stage per `CONTEXT_GRAPH_SCHEMA.md` §2.1.
Provenance loss fails closed (§14 rule 4, §23 row 3).

Lineage uses **six** of the nine relation types the Context Graph Schema defines,
invents none, reverses no direction, and overloads none. §15 rule 1 routes any
relationship needing a non-existent relation into `transformation_history` instead
of asserting it; §15 rule 2 forbids proposing a schema amendment. The choice to
express derivation via `references` plus the transformation record — rather than
minting a `derived_from` relation — is a conservative, explicitly disclosed
under-specification and is owner-correct.

### 5.13 Namespace, classification, sensitivity, secret boundary — **PASS**

Ten namespace categories, each with a distinct binding. §16 rule 1 prohibits
flattening, merging, defaulting, inferring, and collapsing. Rule 2 requires an
explicit, recorded, policy-evaluated act for cross-namespace movement. Rule 3
makes the tenant boundary supersede every namespace rule. Rule 4 makes namespace
escape a fail-closed safety failure. Cross-run and cross-agent leakage are covered
by rows 4 and 2 plus §42.

Classification and sensitivity remain distinct and owner-defined; no parallel
scale is created. §17 rule 1 makes recorded redaction the only downgrade
mechanism (matching Runtime §17.3 rule 5); rule 2 states "**Sensitivity does not
decay**" with highest-of-sources inheritance; rule 3 prevents lower-trust
consumers receiving higher-authorization context; rule 4 permits stricter but
never looser `allowed_use`; rule 5 makes unrecorded downgrade a safety failure.
Unknown classification denies via §9 rule 4.

The secret boundary is correct and complete. Six prohibitions cover payloads,
provider keys, `.env`, framework/session/agent memory, logging and observability,
and proposal persistence. §18 rule 1 distinguishes reference from value; rule 2
states a bridge never holds, reads, requests, derives, or forwards a credential;
rule 3 ensures the detection record itself contains no value. §40 rule 5 and §41
rule 3 close the observability and audit surfaces.

### 5.14 Memory scopes and durable-memory proposals — **PASS with `NEW-P2-05`**

Agent Runtime §18's six categories were extracted independently and confirmed:
immutable run context; short-term working memory; agent-local memory; shared
derived memory; canonical project context; operator-approved long-term memory.
No seventh Runtime category is created by the bridge, and **no ordinal numbering
is used anywhere** — the mapping is by semantic name throughout, deliberately
avoiding the defect Framework Bridge Review 001 recorded as `NEW-P2-03`.

§19's protective rules are sound: rule 1 forbids silent promotion to durable
canonical memory; rule 3 caps framework-native memory/history/checkpoints at
short-term working memory "regardless of its own labelling"; rule 4 restates
`working memory ≠ durable memory`; rule 5 declares no new category or retention
rule.

Memory proposals (§20) require eight elements, never write (preamble: "A system
MAY **propose** durable memory. It MUST NOT write it."), follow §12 and §30
exactly, deny on any missing element, and cannot self-assert approval,
confidence, or validation state. `confidence` is correctly bounded to where the
canonical owner supports it (Runtime §17.2).

The mapping table itself is defective — see `NEW-P2-05`.

### 5.15 Compression, transformation, context loss — **PASS**

Compression ownership remains external and no implementation is implied (§21
preamble: "no algorithm, ratio, model, or implementation"). All seven
prohibitions hold: no fabrication, no provenance erasure, no hidden or weakened
policy restrictions, no permission-scope change, **no uncertainty-to-certainty
conversion**, no removal of rejection/refusal/quarantine evidence, no silent
merging of conflicts. §21 rule 2 preserves highest-of-sources sensitivity; rule 3
states `Compression ≠ truth` and `summarization ≠ evidence`; rule 4 fails closed
on safety- or authority-relevant loss.

Eight transformation classes, each distinct and constrained. Filtering is
subtractive only; redaction is the sole sensitivity-lowering mechanism; schema
projection is field selection with no field invention; framework adaptation is
shape only, never authority. §22 rules 1–3 require recording, invalidate the
envelope on an unrecorded transformation, and forbid adding content, authority,
certainty, or classification. §22 rule 4 keeps `normalize_result` explicitly out
of scope with the strongest available wording: "Nothing here may be cited as
satisfying that obligation."

Six loss classes, four failing closed (provenance, classification, policy,
namespace). §23 rule 2 is the key safety property: "**Ambiguity resolves to
loss**" — where survival cannot be determined, the detail is treated as lost.
Rule 3 prevents accumulation of declared non-safety loss into safety-relevant
loss. Rule 4 makes loss observable and never concealed.

### 5.16 Conflict, versioning, staleness, leases, retention, deletion — **PASS**

Conflicts are surfaced with provenance and precedence and never adjudicated by
the bridge (§24 rules 1–3), expressed via the owner's `contradicts` relation. A
proposal that would silently overwrite a conflicting claim is rejected. Conflict
concealment is a named threat.

Staleness is consumed unchanged from Runtime §17.4; the bridge defines no
competing rule. Snapshot version, context version, stale projection, expired
lease, superseded context, and concurrent proposal are separated in §25's table
with distinct owners. §25 rule 3 explicitly disclaims any locking, persistence,
transaction, or concurrency-control mechanism — the lease semantics **do not**
overreach into storage or access-control runtime ownership.

Leases are correctly bounded: expiry terminates eligibility unless §9 is
re-evaluated in full; no implicit extension by retry or transformation; and §26
rule 4 states "**A lease is not an authorization**".

Retention and deletion are handled with unusual honesty. §27 rule 4 keeps
canonical deletion and external-copy deletion **separately observable** and
forbids any projection claiming otherwise; rule 5 records unestablished external
deletion as `unknown`, "never as deleted". **This does not over-specify deletion
propagation beyond what a future adapter can guarantee** — it binds the bridge's
own retention (rules 1–3) and refuses to assert anything about external copies.
The limitation is represented truthfully.

### 5.17 Quarantine, rejection, error taxonomy — **PASS with `NEW-P2-01`, `NEW-P2-02`, `NEW-P2-04`**

Nine quarantine conditions. Quarantined context cannot be projected or
canonically committed, is isolated in its own namespace, never contributes to a
selection, is terminal absent explicit recorded Operator action, and its evidence
cannot be deleted or contain secret values.

**Exact-name uniqueness confirmed mechanically**: all eleven bridge-owned classes
were tested against a union index built from eight owner documents. **Zero exact
name collisions.** The discriminators that are stated are genuine — the
`CONTEXT_LEASE_EXPIRED` / `STALE_STATE` and `CONTEXT_NAMESPACE_VIOLATION` /
`TENANT_ISOLATION_VIOLATION` separations are both correct and deterministic.

However, uniqueness of name is not uniqueness of meaning, and §29 rule 1's claim
that each class "carries a stated deterministic discriminator" does not survive
independent testing against four owner-defined semantic neighbours — see
`NEW-P2-01`. One consumed class is attributed to the wrong owner — see
`NEW-P2-02`. Quarantine and rejection lack a precedence rule — see `NEW-P2-04`.

§29.2 rule 2 correctly refuses to arbitrate the Framework Bridge's
`PROJECTION_UNSUPPORTED` / `BRIDGE_UNSUPPORTED_BEHAVIOR` overlap and emits
neither class. §29 rule 4 forbids suppressing the original failing detail.

### 5.18 Validation model — **PASS with `NEW-P2-08`**

Thirteen ordered layers, each with a stated owner, input, and output; later layers
may not run before earlier layers reach a determination. §30.14 is unambiguous
about what validation does **not** do: it does not authorize execution, authorize
provider or model access, perform a canonical mutation, resolve an unrelated
bridge error, or imply trust — closing with `context validation ≠ trust` and
`context validation ≠ mutation authorization`.

On the duplication question raised as a special target: return-path validation
appears once as layer 10 and once as §13's thirteen-check pipeline. **This is not
a duplication.** Layer 10's Input column reads "§13's thirteen checks" — the layer
is the ordered *position* of the §13 pipeline within the layer sequence, not a
second, competing evaluation. The discriminator is explicit in the table itself.

No layer evaluates §8 rule 1's subtractive-or-equal property — see `NEW-P2-08`.

### 5.19 Subsystem boundaries — **PASS**

**Runtime** (§32): ten stages remain distinct, none implies the next, canonical
mutation is deliberately not a stage, and the bridge owns neither scheduling nor
result normalization. **Package** (§33): declarations request but grant nothing;
unlisted classes are unreadable and unproposable; no ordinal is used; no lifecycle
rendering field and no canonically-current version is declared. **Framework**
(§34): seven rules, four of which are explicit non-resolutions of the four open
Framework Bridge findings; rule 7 states no rule depends normatively on any of
them. **Provider and model** (§35): minimization before provider projection,
untrusted return, Registry and Router ownership intact, no credential projection,
availability ≠ permission. **Tool** (§36): minimum-necessary slices, §13 return,
identity preserved, availability ≠ authorization. **MCP** (§37): reference-only
consumption, `output_trust_level: untrusted` preserved, prompts are data never
instruction, no automatic connection, no implicit trust, Registry owns identity.
**Plugin / hook / skill / command** (§38): all four bounded, none gains canonical
mutation, namespace ownership, automatic activation, or unrestricted persistence;
no protected command class enumerated. **Batch** (§39): eight compatibility
declarations covering isolated snapshots, per-agent namespaces, bounded writable
scopes, batch-local proposals, integration-owner review, conflict detection, and
owner-only reconciliation — and an explicit prohibition on authorizing parallel
execution, file mutation, Shared Context mutation, push, PR creation, merge, or
deployment.

### 5.20 Observability and audit evidence — **PASS**

Nineteen projections cover request, selection, removal, transformation,
projection, consumer, return, validation, quarantine/rejection, eligibility, and
mutation reference. §40 rule 1 labels bridge fields as bridge-domain data; rule 2
forbids synthesizing a universal healthy/green state; rule 3 states `NOT_RUN` /
`NOT_IMPLEMENTED` never renders as pass; rule 4 forbids collapsing rejections,
quarantines, and losses away; rule 10 (projection 10) requires per-layer
validation results "never collapsed to one boolean". **No new Control Plane
status dimension is created.**

Nine audit questions reconstruct the full exchange. §41 rule 2 restates Runtime
§19's "a transfer with no trace record is not a transfer". Rule 4: absence of
evidence is `unknown`, never success. Redaction, deletion, lease state, and
conflict each have covering evidence via projections 11, 12, 15 and §27 rule 5.

### 5.21 Security and privacy — **PASS**

All twenty-one threats were reconstructed and each cited mitigation was verified
to exist at the cited section. Spot-verified in full: prompt injection (§13 rule
3 + §28), context poisoning (§13 + §11 + §28), provenance spoofing (§14),
namespace escape (§16), sensitivity downgrade (§17 rules 1–2), permission
amplification (§8 rule 1 + §9 rule 1), secret exfiltration (§18), memory
contamination (§19), malicious compression (§21), transformation ambiguity (§22
rule 2 + §28 condition 7), stale-context use (§25 rule 1), cross-run and
cross-agent leakage (§16 rows 4 and 2), tool- and MCP-return poisoning (§36, §37),
plugin/hook injection (§38), framework-memory persistence (§19 rule 1), policy
stripping (§23 row 5 + §21 rule 3), evidence deletion (§41 rule 1 + §21 rule 6),
and conflict concealment (§24).

One mitigation is only partially supported by the section it cites — see
`NEW-P2-07` (proposal replay).

Privacy holds: purpose limitation, minimum-necessary context, retention
limitation, consumer-specific projection with broadcast prohibited, and no
relaxation for personal or user-namespace context.

### 5.22 Failure behavior — **PASS**

All eight §44 conditions fail closed, and the closing sentence is categorical:
"There is no default-allow state, no substituted context, no cached fallback, and
no nearest-available context." Cross-checked against §9 rule 4, §6.2 rule 1,
§16 rule 4, §17, §23 rules 1–2, §25 rule 2, §28, and §30 — every ambiguous
authority, provenance, namespace, policy, sensitivity, identity, transformation,
loss, conflict, retention, and lease state denies.

### 5.23 Internal consistency, normative modals, cross-references — **PASS with `NEW-P3-01`, `NEW-P3-02`**

- **Modals:** 109 `MUST`, 71 `MUST NOT`, 8 `MAY`, **0 `SHOULD`**, **0 `SHALL`** —
  consistent with the repository's MUST/MUST NOT/MAY discipline.
- **No inverted modal constructions.** A targeted search for the `No X MUST`
  pattern (the defect class recorded as Agent Package Review 002 `NEW-P3-03`)
  returned **zero** matches. Every prohibition is expressed as `MUST NOT` or as
  a negative subject with a positive verb ("No bridge … holds mutation
  authority").
- **Cross-references:** all fifteen distinct `[[wikilink]]` targets resolve to
  existing repository files. All internal `§N` references fall within 1–50; no
  reference is out of range. All cited external section numbers were verified to
  exist in their owner documents (Runtime §8.1/§8.3/§11.2/§15.1/§16/§17.1–17.4/
  §18/§19/§23.1/§31/§32/§33; Framework Bridge §4.2/§10.1/§18/§23/§27.2; Agent
  Package §10.2/§12.2/§15/§21; Gateway §12/§17/§18/§25; Control Plane §7.1/§8.1/
  §9.3/§16; Provider Registry §21.1/§24/§24.2).
- Two editorial defects recorded as `NEW-P3-01` and `NEW-P3-02`.

### 5.24 Overclaim review — **PASS**

A full-document scan for the overclaim vocabulary (implemented, integrated,
available, enabled, installed, operational, executable, production-ready,
supported, tested, validated, accepted, approved, passed, live, deployed,
trusted, canonical mutation, durable memory, storage, database) found **no false
claim**.

- Every occurrence of "implement" is a scope exclusion, a prohibition, or a
  `NOT_IMPLEMENTED` state row.
- Every occurrence of "trust" is a denial: `context validation ≠ trust`,
  `tool output ≠ trusted context`, "no implicit trust", "not trusted, not
  eligible", "Provenance preserved does not mean content trusted".
- §1.4's thirteen-row implementation-state table is accurate against the
  repository: no bridge, mutation engine, storage, database, vector store, index,
  memory service, compression, validation, or proposal-lifecycle code exists;
  envelopes, proposals, and canonical mutations are **zero**.
- §1.4 closes with "A validator that did not run records `NOT_RUN`, never a
  defaulted pass."
- **Empirical framework validation is correctly recorded as `NOT_PERFORMED`** and
  §9 rule 3 refuses to substitute for it.
- §1.5's migration-trigger claim is accurate: the document implements nothing, so
  triggers #1, #4, #5, #6, #7 remain uncrossed.

**No false implementation, runtime, storage, or empirical-validation claim exists
anywhere in the document.**

---

## 6. Upstream P2 containment — all seven verified open and contained

| Finding | Required isolation | Specification evidence | Disposition | Regression risk |
| --- | --- | --- | --- | --- |
| Framework Bridge `NEW-P2-01` — `normalize_result` has no counterpart rule | Own no run-output normalization | §22 rule 4: "does not define, own, resolve, or substitute for" it; "Nothing here may be cited as satisfying that obligation." §34 rule 5. §46 item 1. Only three `normalize_result` mentions, all denials or deferrals | **OPEN, contained** | Low. §22 class 4 is named "Normalization" but is scoped to context structure and explicitly disclaimed; naming adjacency only |
| Framework Bridge `NEW-P2-02` — `PROJECTION_UNSUPPORTED` / `BRIDGE_UNSUPPORTED_BEHAVIOR` overlap | Resolve nothing; emit neither | §29.2 rule 2: "does not resolve, arbitrate, or select between… emits neither class". §34 rule 6. §46 item 2. Grep confirms both names appear **only** inside the denial and the deferral row | **OPEN, contained** | None |
| Framework Bridge `NEW-P2-03` — capability numbering divergence | Use no cross-document ordinal | §33 rule 3: "referenced by semantic name, never by cross-document ordinal position". §34 rule 3. §46 item 3. A scan for capability/state ordinals found **no** ordinal citation anywhere | **OPEN, contained** | None |
| Framework Bridge `NEW-P2-04` — validation obligation not wired to eligibility | Treat no unvalidated profile as eligible | §9 rule 3 wires it into *this* contract's eligibility and states validation "remains `NOT_PERFORMED`". §34 rule 4. §46 items 4 and 12 | **OPEN, contained** | None. The bridge is stricter than the owner without resolving the owner's gap |
| Agent Package `NEW-P2-01` — missing package-lifecycle rendering field | Define no such field | §33 rule 4: "defines no package lifecycle rendering field". §46 item 5 | **OPEN, contained** | None |
| Agent Package `NEW-P2-02` — contract-version discrepancy | Declare no version canonically current | §33 rule 4: "asserts **no** Agent Package contract version as canonically current". §46 item 6. A grep for Agent Package version assertions returned **zero** hits | **OPEN, contained** | None |
| Agent Package `NEW-P2-03` — protected command classes unenumerable | Enumerate none | §38 rule 2: "This contract enumerates no protected command classes"; ownership passed to the future Command Registry. §46 item 7 | **OPEN, contained** | None |

**No upstream finding is silently resolved. No normative rule in this contract
depends on the resolution of any of them.** Neither the Agent Package Contract
nor the Framework Bridge Contract was edited — both verified byte-identical
(§2.2).

---

## 7. New findings — P2 (non-blocking)

### `NEW-P2-01` — Four owner-defined semantic neighbours are never audited or discriminated, falsifying §29 rule 1

- **Severity:** P2
- **File / section:** `docs/specs/MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_SPEC_001.md` §29, §29.2, §47 criterion 21
- **Precise claim:** §29's preamble asserts that "the Agent Runtime §33 taxonomy,
  the Framework Bridge §23 taxonomy, the Shared Context owner documents, the
  Integration Gateway §25 taxonomy, the Context Graph Schema, and the Operations
  contracts were audited." §29 rule 1 then asserts: "No class above duplicates an
  owner-defined class; **each carries a stated deterministic discriminator**."
  §47 criterion 21 restates this as an acceptance criterion.
- **Canonical owners:** Integration Gateway §25.2; Agent Runtime §33; Framework
  Bridge §23.3.
- **Evidence:** A mechanical union index of `UPPER_SNAKE_CASE` classes across
  eight owner documents confirms **zero exact name collisions**, but identifies
  four owner-defined classes that are semantic neighbours of bridge-owned classes
  and that appear **zero times** in the reviewed specification:

  | Bridge class | Stated discriminator | Unreconciled owner neighbour | Owner | Occurrences in reviewed spec |
  | --- | --- | --- | --- | --- |
  | `CONTEXT_QUARANTINED` | "Quarantine only" | `CONTENT_QUARANTINED` — "Inbound payload failed validation/authentication … Quarantine with provenance; never processed" | Gateway §25.2 | **0** |
  | `CONTEXT_PROVENANCE_MISSING` | "Absence of provenance, not denial of access" | `PROVENANCE_VERIFICATION_FAILED` — "Provenance evidence did not verify" | Runtime §33 | **0** |
  | `CONTEXT_INTEGRITY_FAILED` | "Integrity only" | `ENVELOPE_INTEGRITY_FAILED` — "`envelope_digest` did not reproduce" | Runtime §33 | **0** |
  | `CONTEXT_LOSS_UNACCEPTABLE` | "Loss classification only" | `PROJECTION_LOSS_UNACCEPTABLE` — "Safety-relevant projection loss detected" | Framework Bridge §23.3 | **0** |

- **Why this is incorrect:** Each stated discriminator distinguishes its class
  from a *different* neighbour than the one that actually collides. "Quarantine
  only" does not distinguish `CONTEXT_QUARANTINED` from a Gateway class whose
  entire purpose is quarantining inbound payloads that fail validation — and the
  bridge's own §13 return path covers provider and MCP returns, which is precisely
  the Gateway's inbound boundary. "Absence of provenance" does not separate a
  missing `source_refs` from provenance that is present but unverifiable, yet §13
  check 2 requires provenance be "present **and traceable**", making untraceable
  provenance indistinguishable from failed verification. "Integrity only" does not
  say whether the bridge's context envelope digest is a different object from the
  Runtime's run-envelope digest. "Loss classification only" does not separate
  bridge context loss (§23) from Framework Bridge projection loss (§24.1), which
  the review brief specifically required be discriminated.
- **Required correction:** Extend §29.2's discriminator column to name each of the
  four owner neighbours explicitly and state the deterministic condition that
  selects between them, in the same form §29.2 already uses successfully for
  `CONTEXT_LEASE_EXPIRED` vs `STALE_STATE` and `CONTEXT_NAMESPACE_VIOLATION` vs
  `TENANT_ISOLATION_VIOLATION`. Alternatively, consume the owner class where the
  meaning is genuinely the same.
- **Gate impact:** Non-blocking. Every branch is fail-closed and no branch admits
  context; the defect is determinism of class selection, not authority.
  **Blocking for** any adapter, validator, or runtime task that emits rejection
  classes — class selection is not deterministic between live classes as written.

### `NEW-P2-02` — `INJECTION_SUSPECTED` is attributed to the wrong canonical owner

- **Severity:** P2
- **File / section:** §29.1, row `INJECTION_SUSPECTED`
- **Precise claim:** §29.1 lists `INJECTION_SUSPECTED` under "Consumed classes —
  owned elsewhere" with owner "**Agent Runtime §33**".
- **Canonical owner:** **Integration Gateway §25.2**.
- **Evidence:** Agent Runtime §33's class table contains **49 rows and 49 distinct
  Agent Runtime-layer class names** under a normative one-row-one-class invariant.
  `INJECTION_SUSPECTED` is **not** among them. The text immediately following that
  table states explicitly: "The Gateway classes `CONTRACT_CONFLICT`,
  `APPROVAL_STALE`, `AUDIT_RESERVATION_FAILED`, `PARTIAL_APPLICATION`,
  `INDETERMINATE`, and `INJECTION_SUSPECTED` are likewise adopted unchanged, are
  **not** restated in this table, and **remain owned by**
  `[[MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001]]` §25.2." Gateway
  §25.2 defines it: "Instruction-shaped untrusted content detected | n/a | Record,
  surface, continue treating as data". Framework Bridge Review 001 already
  operated on this distinction, counting "55 Runtime classes" (49 + 6 adopted).
- **Why this is incorrect:** §29's discipline is that consumed classes are
  "consumed, not redefined", and §47 criterion 3 requires that "every consumed
  concept cites its canonical owner". Citing the adopting document rather than the
  owning document breaks that invariant for one of nine consumed classes. A
  reader following the citation to Runtime §33 will not find the class.
- **Required correction:** Change the owner cell to Integration Gateway §25.2.
  Separately, consider noting that the Gateway defines the class as
  record-and-continue-as-data while the bridge escalates prompt-injection
  suspicion to quarantine (§13 check 12, §28 condition 3) — a permitted stricter
  treatment under §3.1, but one worth stating so the disposition difference is not
  read as a redefinition.
- **Gate impact:** Non-blocking. Factual owner-reference defect with no safety
  consequence: the bridge's fail-closed quarantine posture is unaffected.

### `NEW-P2-03` — The proposal lifecycle and rejection vocabulary overlap the Context Ingestion Gate, the one owner omitted from the non-collision claim

- **Severity:** P2
- **File / section:** §12 (preamble and ten phases), §29, §3 row "Context ingestion
  and admission workflow"
- **Precise claim:** §12 states its phases "are distinct from the Agent Package
  lifecycle, the Agent Runtime `run_state`, the Framework Bridge lifecycles, and
  Control Plane's six status dimensions."
- **Canonical owner:** `MELLYCORE_CONTEXT_INGESTION_GATE_SPEC_001` §3, §6, §7;
  `MELLYCORE_CONTEXT_GATE_IMPLEMENTATION_SPEC_001`.
- **Evidence:** §3 correctly names the Ingestion Gate and Context Gate as owners of
  "Context ingestion and admission workflow", with the bridge's role stated as
  "Consumes; **proposals terminate at the gate**". The Ingestion Gate defines an
  eight-step admission workflow with per-step ownership (§3), **five validation
  outcomes evaluated in precedence order, first match wins** — `REFUSE`,
  `CONTRADICTION_FOUND`, `NEEDS_HUMAN_REVIEW`, `ACCEPT_WITH_WARNINGS`, `ACCEPT`
  (§6) — and **nine refusal reason codes R1–R9** (§7). A grep of the reviewed
  specification for each of `REFUSE`, `CONTRADICTION_FOUND`, `NEEDS_HUMAN_REVIEW`,
  and `ACCEPT_WITH_WARNINGS` returns **zero** hits. The four systems §12 does
  disclaim collision with are precisely those that do **not** own proposal
  admission; the one that does is omitted.

  Concrete unmapped pairs over the same artifact:

  | Bridge concept | Ingestion Gate concept | Divergence |
  | --- | --- | --- |
  | `proposal_validated` — "Passed §30; not trusted, not eligible" | `ACCEPT` — "passed every check cleanly… eligible to be presented for the human decision" | Two "passed validation" states, no mapping |
  | `proposal_rejected` — carries a §29 class; terminality unstated | `REFUSE` — "**Terminal? Yes, for this submission**", "not human-overridable at gate level" | Different terminality for the same refusal |
  | `proposal_awaiting_operator_approval` (§12 phase 8), §31 condition 11 | Step 7 human review; "`ACCEPT` never means admitted" | Two human-approval concepts, no mapping |
  | `CONTEXT_CONFLICT_UNRESOLVED` (§29.2) | `CONTRADICTION_FOUND` + Contradiction Ledger routing (§11) | Two conflict outcomes, no precedence |
  | §29.2 eleven classes | R1–R9 reason codes (e.g. `incomplete_metadata`, `secret_content`) | Two reason vocabularies over one artifact |
  | §30's thirteen ordered layers | §6's five outcomes "first match wins"; §7 "evaluated first, fail fast" | Two orderings, composition unstated |

- **Why this is incorrect:** §12 rule 4 defers "the full transition-rule, evidence,
  and event contract" to §46 item 11 — a *future implementation*, not a mapping to
  the existing owner. The result is a parallel lifecycle and reason vocabulary over
  the same artifact with no stated composition, while the document simultaneously
  claims those proposals "terminate at the gate".
- **Required correction:** Extend §12's non-collision statement to name the Context
  Ingestion Gate and state how the bridge's ten phases compose with its five
  outcomes and eight-step workflow — at minimum, which system's determination is
  authoritative at each boundary and whether bridge validation precedes, follows,
  or wraps gate validation. Add an Ingestion Gate row to §46 if the mapping is
  genuinely deferred.
- **Gate impact:** Non-blocking. The composition is strictly conjunctive — both
  systems deny independently and §3.1 permits the bridge to be stricter — so no
  path admits context that either system would refuse, and the Ingestion Gate's
  `REFUSE` remains binding. Ownership is correctly assigned; only the mapping is
  missing. **Blocking for** the proposal-lifecycle implementation task (§46 item
  11) and any context-validation implementation.

### `NEW-P2-04` — Quarantine and rejection have no precedence rule; seven of nine quarantine conditions have a conflicting §13 disposition

- **Severity:** P2
- **File / section:** §13 (thirteen checks), §28 (nine conditions), §12 phases 4–5
- **Precise claim:** §28 designates nine conditions as **quarantine** conditions,
  and §28 rule 3 makes quarantine "terminal absent explicit, recorded Operator
  action". §13 independently assigns a failure disposition to each of its thirteen
  checks.
- **Canonical owner:** This contract (both sections are bridge-owned).
- **Evidence:** Seven of the nine §28 conditions correspond to a §13 check whose
  stated disposition is **Reject**, not quarantine:

  | §28 condition | Corresponding §13 check | §13 disposition |
  | --- | --- | --- |
  | 1 Unknown or untraceable provenance | 2 Provenance present and traceable | Reject |
  | 2 Schema validation failure | 5 Schema conformance | Reject |
  | 4 Policy conflict | 4 Policy satisfied | Reject |
  | 5 Unauthorized namespace | 3 Namespace authorized | Reject |
  | 6 Sensitivity mismatch | 7 Sensitivity consistent | Reject |
  | 7 Transformation ambiguity | 10 Transformation record complete | Reject |
  | 9 Integrity failure | 9 Integrity evidence | Reject |

  Only conditions 3 and 8 have consistent quarantine dispositions (§13 checks 12
  and 13, "Quarantine on suspicion"). **§13 check 6 (Content safety) is explicitly
  non-deterministic: "Reject or quarantine"**, with no discriminator anywhere in
  the document. No precedence rule exists in §12, §13, §28, §29, or §30 stating
  which disposition governs when a condition appears in both tables.
- **Why this is incorrect:** The two dispositions have materially different
  consequences. Quarantine is terminal absent Operator action (§28 rule 3),
  isolated in its own namespace, and "never contributes to a selection" (§28 rule
  2). Rejection has no equivalent isolation or terminality rule — §11 rule 5 only
  prohibits retrying a rejected proposal *as a mutation request*. An implementer
  choosing rejection where quarantine was intended produces materially weaker
  containment, and check 6 — content safety — is the sharpest instance because it
  is the one check where the document itself declines to choose.
- **Required correction:** Add a precedence rule stating that a condition meeting
  any §28 trigger quarantines regardless of the §13 disposition (or the converse),
  and replace §13 check 6's "Reject or quarantine" with a deterministic
  discriminator.
- **Gate impact:** Non-blocking. Both dispositions are fail-closed and neither
  admits the context; the defect is determinism and terminality, not authority.
  **Blocking for** any validation or proposal-lifecycle implementation.

### `NEW-P2-05` — Two of eight memory scopes map to no Agent Runtime §18 category, contradicting §47 criterion 17

- **Severity:** P2
- **File / section:** §19 mapping table; §2 term "Durable Memory"; §47 criterion 17
- **Precise claim:** §19 states "The scopes below are referenced **by semantic
  name** and mapped onto the owner's categories by name", and §47 criterion 17
  states "Memory scopes map onto Agent Runtime §18's six categories **by semantic
  name**, with no new category and no renumbering (§19)."
- **Canonical owners:** Agent Runtime §18 (six categories); Control Plane §9.3
  (five operator-surface memory layers).
- **Evidence:** Agent Runtime §18's six categories were extracted independently:
  (1) immutable run context, (2) short-term working memory, (3) agent-local memory,
  (4) shared derived memory, (5) canonical project context, (6) operator-approved
  long-term memory. Row-by-row against §19's eight scopes:

  | # | Bridge scope | Mapped to | Assessment |
  | --- | --- | --- | --- |
  | 1 | Working memory | cat 2 | ✅ |
  | 2 | Execution-local memory | "cat 1 / cat 2, **per record**" | ✅ discriminator stated |
  | 3 | Framework-session memory | cat 2 at most | ✅ |
  | 4 | Package-declared memory | "**no category of its own**" | ⚠ maps to no §18 category |
  | 5 | Agent memory | cat 3 | ✅ |
  | 6 | Shared Context | cat 5 | ✅ |
  | 7 | Durable MellyCore memory | "cat 5; cat 6" | ⚠ two categories, **no discriminator** |
  | 8 | Archival evidence | "Append-only evidence surfaces (Runtime **§17.1 `append_evidence`**)" | ⚠ cites an *operation*, not a §18 memory category |

  Row 8's `Canonical?` cell reads "Immutable, never mutated" — a third value in a
  column that is otherwise strictly Yes/No. Runtime §18 category 4 (**shared
  derived memory**) is mapped by no bridge scope in §19, though it is correctly
  addressed in §4.3's register. §2's "Durable Memory" definition repeats row 7's
  two-category collapse.

  Decisively: Control Plane §9.3 — a section this contract cites twice (§2 term
  "Shared Context"; §3 ownership row) — enumerates five memory layers including
  "**Immutable evidence**", which is the natural owner for row 8. The bridge's
  eighth scope is therefore not ownerless in the repository; it cites the wrong
  owner document, and Control Plane §9.3's five-layer taxonomy is nowhere
  reconciled with either the Runtime's six or the bridge's eight.
- **Why this is incorrect:** §47 criterion 17 asserts a property of all eight rows
  that holds for six. Row 7's collapse of categories 5 and 6 is material because
  the two have different owner semantics — category 6 requires approval to persist
  and Operator-only discard — so a proposal targeting "Durable MellyCore memory"
  does not determine which category's rules apply. §3's ownership row forbids
  conflating two categories.
- **Required correction:** Restate §19 so each row either names exactly one §18
  category or explicitly declares itself not a §18 memory category and cites its
  real owner (Control Plane §9.3 "immutable evidence" for row 8; a declaration-only
  note for row 4). Give row 7 a per-record discriminator in the form row 2 already
  uses. Reconcile — or explicitly defer — Control Plane §9.3's five layers.
  Amend §47 criterion 17 to match.
- **Gate impact:** Non-blocking. **No taxonomy expansion actually occurs in
  substance**: §19 rule 5 declares no new category, §19 rule 1 blocks silent
  promotion, no ordinal numbering is used anywhere, and §31 condition 11 requires
  Operator approval on the mutation path regardless of which durable category is
  meant. The defect is that the mapping table does not support the claim made
  about it. **Blocking for** the durable-memory contract (§46 item 9).

### `NEW-P2-06` — The context envelope overlaps Control Plane's `ContextPacket` entity, which is never cited or distinguished

- **Severity:** P2
- **File / section:** §6.1 (fourteen fields), §5.1, §3 (no owner row for context
  entities)
- **Precise claim:** §6 defines a fourteen-field context envelope as a new
  bridge-owned logical carrier, and §3 assigns no owner row to Control Plane's
  context entities.
- **Canonical owner:** Control Plane §7.2 (entity catalogue) and §9.3.
- **Evidence:** Control Plane §7.2 defines `ContextPacket` — "Approved context
  manifest; `context_packet_id`" — with fields "version, source_refs,
  compression_strategy, token_estimate, redactions, confidence, scope,
  approval_ref, digest, status" and applicable status fields `lifecycle_status`,
  `freshness_state`, `approval_state`, `evidence_state`. Control Plane §9.3 names
  `ContextSource`, `ContextPacket`, and `MemoryRecord` as the key entities of
  "Context Compression and Shared Context", with fields including "layer, source,
  strategy, summary ref, confidence, freshness, retention, project scope, agent
  visibility, token estimate, redaction, approval, digest".

  Field-level overlap with §6.1: `source` ↔ `source_refs`;
  `transformation_history` ↔ `redactions` / `compression_strategy`;
  `retention_hint` ↔ retention; `integrity_metadata` ↔ `digest`;
  `projection_scope` ↔ `scope`; `validation_state` ↔ `status` / `approval_ref`.

  Grep of the reviewed specification: **`ContextPacket` 0 hits,
  `context_packet_id` 0 hits, `MemoryRecord` 0 hits.** `ContextSource` appears
  once (§5.1 row 13), correctly attributed. §3's Control Plane row cites only
  §7.1 and §8.1 — the common entity contract and the status dimensions — not §7.2's
  entity catalogue.
- **Why this is incorrect:** §9.3 is a section this contract cites twice as its
  Shared Context owner, so `ContextPacket` is not an obscure entity in an uncited
  document. The two objects are genuinely distinguishable — an envelope is
  per-projection, per-consumer, and pre-approval, whereas a `ContextPacket` is an
  approved, task-scoped manifest carrying `approval_state` — but the specification
  never states that distinction, leaving an implementer free either to build the
  envelope *as* a `ContextPacket` (inheriting an `approval_state` the envelope must
  not carry, contra §6.2 rule 2) or to duplicate it.
- **Required correction:** Add a §3 ownership row for Control Plane §7.2's context
  entities and state in §6 how `context_envelope_id` relates to `context_packet_id`
  — distinct objects, a projection of one onto the other, or an explicitly deferred
  mapping.
- **Gate impact:** Non-blocking. No authority is created and §6.2 rule 2 keeps the
  envelope authority-free regardless. **Blocking for** any observability, storage,
  or Shared Context implementation task that must instantiate either object.

### `NEW-P2-07` — The proposal-replay mitigation cites a mechanism that governs projections, not proposals

- **Severity:** P2
- **File / section:** §42 row "Proposal replay"; §26; §12
- **Precise claim:** §42 mitigates the named threat "Proposal replay" with: "A
  proposal binds to one exact namespace, tenant, consumer, and snapshot currency
  (§31); **expiry ends eligibility (§26)**."
- **Canonical owner:** This contract.
- **Evidence:** The first clause is accurate — §31's preamble binds the proposal to
  the exact namespace, tenant, and consumer, and condition 7 requires snapshot
  currency. The second clause is not: §26 rule 1 reads "**A projection** MAY carry
  a bounded lease", and §9 precondition 12 places lease validity in *projection*
  eligibility. §31's eleven mutation-eligibility conditions contain **no lease
  condition**. No proposal-level expiry, time bound, idempotency key, or
  replay-detection rule exists anywhere in the document. §12 provides
  `proposal_withdrawn` and `proposal_superseded` states but no rule preventing a
  withdrawn or rejected proposal being resubmitted; §11 rule 5 prohibits only
  escalation to a mutation request.
- **Why this is incorrect:** A named security threat is mitigated by citing a
  mechanism that does not apply to the object under threat. §25 correctly lists
  "Concurrent proposal → surfaced as a conflict, never merged", so concurrency is
  handled; replay and staleness of a *proposal* are not.
- **Required correction:** Either add a proposal-level expiry or idempotency rule
  to §12/§31, or correct §42's mitigation to cite only the §31 binding and record
  proposal replay as a deferred dependency under §46 item 11.
- **Gate impact:** Non-blocking. A replayed proposal still traverses §30 and §31 in
  full, including snapshot currency (condition 7) and Operator approval (condition
  11), so replay cannot produce an unapproved canonical mutation. The defect is an
  inaccurate mitigation citation and an unclosed lifecycle gap.

### `NEW-P2-08` — "Subtractive or equal" is normative but no validation layer or eligibility precondition evaluates it

- **Severity:** P2
- **File / section:** §8 rule 1; §9 (twelve preconditions); §30 (thirteen layers);
  §47 criterion 8
- **Precise claim:** §8 rule 1: "Projection is **subtractive or equal** with respect
  to authority: the projected form expresses a subset of what the canonical slice
  permits." §47 criterion 8 makes this an acceptance criterion. §42 cites it as the
  mitigation for permission amplification.
- **Canonical owner:** This contract.
- **Evidence:** All thirteen §30 layers were enumerated: envelope, identity,
  provenance, namespace, policy, permission, sensitivity, schema, transformation,
  return-path, conflict, retention, observability. **None evaluates whether a
  projection is authority-subtractive.** All twelve §9 preconditions were
  enumerated: identity, provenance, consumer, purpose, policy, permission,
  classification, namespace, retention, sensitivity, transformation, lease.
  **None is "projection is subtractive or equal".** No definition of the comparison
  procedure — what constitutes the authority set of a canonical slice, or how
  subset-hood is decided — appears anywhere in the document, and §46 does not
  record it as deferred.
- **Why this is incorrect:** The property is load-bearing (it is the sole cited
  mitigation for permission amplification) but is not deterministically measurable
  as written, and no layer is responsible for measuring it. A projection that
  broadened authority would not be caught by §30.
- **Required correction:** Add a projection-authority-subset validation layer to
  §30 (or a precondition to §9), define the deterministic comparison, or record
  the measurement procedure as a deferred dependency in §46 and adjust §42's
  mitigation accordingly.
- **Gate impact:** Non-blocking. Defence in depth holds: §8's nine prohibitions are
  independently normative, §30 layer 6 validates permission, and §8 rule 4 plus
  Runtime §17.3 rule 1 re-evaluate the consumer's permission at the point of use,
  so an amplified projection is still denied on use. **Blocking for** the
  context-validation implementation (§46 item 10).

---

## 8. New findings — P3 (editorial, non-blocking)

### `NEW-P3-01` — §30's only sub-heading is numbered `30.14` although §30 has no subsections 30.1–30.13

- **Severity:** P3
- **File / section:** §30, heading `### 30.14 What validation does not do`
- **Evidence:** §30's thirteen validation layers are **table rows**, not
  subsections. A heading-extraction pass over the document confirms `### 30.14` is
  the only `###` heading within §30; there is no `### 30.1` … `### 30.13`. The
  numbering implies a subsection structure that does not exist. All references to
  §30.14 (§2 "Context Validation", §4.2 rule 3, §30 closing paragraph, §47
  criterion 22) resolve correctly, so no cross-reference is broken.
- **Required correction:** Renumber to `### 30.1`, or introduce §30.1–§30.13 as
  genuine subsections, and update the four citing locations if the number changes.
- **Gate impact:** None. Editorial.

### `NEW-P3-02` — `context_bridge_contract_version` is used normatively but defined nowhere

- **Severity:** P3
- **File / section:** §50 rule 1
- **Evidence:** §50 rule 1 reads "This document may be amended only additively
  unless a major `context_bridge_contract_version` bump is explicitly declared."
  The token appears **exactly once** in the document. It is absent from §2's
  thirty-one terminology entries, from §5.1's fourteen identity fields, and from
  §48's metrics. The document header states "**Version:** 1.0" but never binds that
  value to this field name. By contrast, the Framework Bridge Contract defines
  `supported_bridge_contract_range` and `BRIDGE_CONTRACT_VERSION_INCOMPATIBLE`
  explicitly, and the Agent Package Contract defines `contract_version` in its §22.
- **Note on scope:** This is not a fourth minted identity in breach of §5.2 rule 2
  — §5.2 rule 2 is scoped to §5.1's context identity and correlation fields, and
  §2's "Context Version" correctly disclaims minting any context-item version. The
  defect is solely that a normatively used term is undefined.
- **Required correction:** Define `context_bridge_contract_version` in §2 or §50
  and bind it to the header's declared value.
- **Gate impact:** None. Editorial.

---

## 9. Safety-posture distinctions — all verified preserved

Each distinction below was tested against the document rather than assumed.

| Distinction | Verified at |
| --- | --- |
| canonical context ≠ projected context | §4.3 register; §2 "Context Projection" |
| projected context ≠ authorized context | §8 rule 4; §10 rule 1 |
| context selected ≠ context exposed | §7 rule 3 |
| context exposed ≠ unrestricted access | §7 rule 1; §10 |
| context proposal ≠ canonical mutation | §11 rows 3 and 5; §11 rule 2 |
| context validation ≠ trust | §30.14 rule 5, stated verbatim |
| context validation ≠ mutation authorization | §30.14 rule 3, stated verbatim |
| framework memory ≠ Shared Context | §19 row 3; §34 rule 1 |
| working memory ≠ durable memory | §19 rule 4, stated verbatim |
| package declaration ≠ context permission | §33 rule 1 |
| tool output ≠ trusted context | §36 rule 2, stated verbatim |
| provider output ≠ canonical fact | §35 rule 3; §4.3 row 10 |
| compression ≠ truth | §21 rule 3, stated verbatim |
| summarization ≠ evidence | §21 rule 3, stated verbatim |
| provenance preserved ≠ content trusted | §14 rule 5, stated verbatim |
| mutation eligible ≠ mutation performed | §31 rule 1, stated verbatim |
| review pass ≠ runtime implementation | This review; §12 below |
| bridge specified ≠ bridge implemented | §1.4 |

---

## 10. Verdict summary

| Area | Verdict |
| --- | --- |
| Task and artifact identity | PASS |
| Architectural ownership | PASS |
| Canonical-versus-projected direction | PASS |
| Context identity | PASS |
| Context envelope | PASS with `NEW-P2-06` |
| Selection and projection | PASS with `NEW-P2-08` |
| Projection eligibility | PASS |
| Read boundary | PASS |
| Write / proposal / eligibility / approval / mutation | PASS |
| Proposal lifecycle | PASS with `NEW-P2-03` |
| Return-path validation | PASS with `NEW-P2-04` |
| Provenance and lineage | PASS |
| Namespace, classification, sensitivity, secret boundary | PASS |
| Memory scopes and memory proposals | PASS with `NEW-P2-05` |
| Compression, transformation, context loss | PASS |
| Conflict, versioning, staleness, lease, retention, deletion | PASS |
| Quarantine, rejection, error taxonomy | PASS with `NEW-P2-01`, `NEW-P2-02`, `NEW-P2-04` |
| Validation model and mutation eligibility | PASS with `NEW-P2-08` |
| Runtime / Package / Framework / Provider / Router / Tool / MCP / Plugin / Hook / Skill / Command / Batch boundaries | PASS |
| Observability and audit evidence | PASS |
| Security and privacy | PASS with `NEW-P2-07` |
| Failure behavior | PASS |
| Seven upstream P2 containment | PASS — all open, all contained |
| Document metrics | PASS — 34 / 34 reproduce |
| Internal consistency and modals | PASS with `NEW-P3-01`, `NEW-P3-02` |
| Overclaim review | PASS |

| Severity | Count | IDs |
| --- | --- | --- |
| **P0** | **0** | — |
| **P1** | **0** | — |
| **P2** | **8** | `NEW-P2-01` … `NEW-P2-08` |
| **P3** | **2** | `NEW-P3-01`, `NEW-P3-02` |

---

## 11. Gate decision and exact reasoning

**`PASS_WITH_NON_BLOCKING_FINDINGS`.**

Derived from the findings, against the repository's canonical gate criteria:

1. **P0 = 0 and P1 = 0.** No blocking finding exists.
2. **No direct or ambiguous canonical-write authority.** A full-document search
   found no alternate or accidental direct-write path. §11 rule 4 is categorical
   across every external actor class, and §4.2, §31, §32 rule 3, §33 rule 1, §38
   rule 1, and §39 each independently close a potential bypass.
3. **No unresolvable owner conflict.** Every concern resolves to exactly one owner.
   The ownership findings (`NEW-P2-01`, `-02`, `-03`, `-05`, `-06`) are
   incompleteness — an owner uncited, a neighbour unreconciled, a mapping unstated
   — not two documents claiming incompatible authority.
4. **Duplicated error ownership is present but does not block.** The duplication is
   in reason vocabulary and state naming (`NEW-P2-01`, `-03`), not in ownership of
   a decision: §3 correctly cedes admission to the Context Gate and Ingestion Gate,
   and §29.2 rule 2 refuses to arbitrate the one overlap it inherited. Exact-name
   uniqueness was confirmed mechanically across eight owner documents.
5. **No false implementation, storage, mutation, runtime, or empirical-validation
   claim.** The overclaim scan is clean and §1.4's state table is accurate against
   the repository.
6. **All 34 metrics reproduce independently.** Zero count discrepancies.
7. **All seven upstream P2 findings are open and contained**; none is silently
   resolved and no normative rule depends on any.
8. **Every remaining finding is incomplete-but-fail-closed**, which canonical
   repository policy permits to remain non-blocking. In each case both branches of
   the ambiguity deny, and none creates authority.

Validator success was **not** treated as creating a pass: `git diff --check` and
the project-state validator concern repository hygiene, not architectural
correctness, and contributed nothing to this decision.

This matches the precedent set by Framework Bridge Review 001
(`PASS_WITH_NON_BLOCKING_FINDINGS`, P0 0 / P1 0 / P2 4 / P3 4) and Agent Package
Review 002 (P0 0 / P1 0 / P2 3 / P3 4).

---

## 12. Acceptance constraints

`MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_001` version 1.0 is accepted as a
**documentation contract only**, under these ten constraints:

1. `NEW-P2-01` — four owner neighbours must be discriminated before any component
   emits bridge rejection classes.
2. `NEW-P2-02` — `INJECTION_SUSPECTED`'s owner citation must be corrected to
   Integration Gateway §25.2.
3. `NEW-P2-03` — the proposal lifecycle must be composed with the Context
   Ingestion Gate's five outcomes and eight-step workflow before any
   proposal-lifecycle or validation implementation.
4. `NEW-P2-04` — quarantine/rejection precedence and §13 check 6 must be made
   deterministic.
5. `NEW-P2-05` — §19's mapping must name exactly one owner category per row or
   declare the row out of §18's taxonomy, and reconcile Control Plane §9.3.
6. `NEW-P2-06` — the envelope's relationship to Control Plane `ContextPacket` must
   be stated.
7. `NEW-P2-07` — proposal replay must be genuinely mitigated or explicitly
   deferred.
8. `NEW-P2-08` — "subtractive or equal" must be made measurable or explicitly
   deferred.
9. `NEW-P3-01`, `NEW-P3-02` — editorial corrections.
10. **Acceptance is of documentation only.** It authorizes no Shared Context
    Bridge, canonical mutation engine, storage, database, vector store, index,
    memory service, compression, validation, or proposal-lifecycle implementation;
    no Agent Runtime, Framework Adapter, package loading, provider connection,
    credential, model call, MCP connection, Batch Orchestration, frontend,
    backend, network operation, or deployment.

**No downstream task is authorized by this review.** Each remains blocked behind
its own gate and separate explicit Operator authorization.

---

## 13. Implementation state after this review (normative, truthful)

| Dimension | State |
| --- | --- |
| Shared Context Bridge | `NOT_IMPLEMENTED` |
| Canonical mutation engine | `NOT_IMPLEMENTED` |
| Context storage, database, vector store, index | `NOT_IMPLEMENTED` |
| Memory service, durable memory store | `NOT_IMPLEMENTED` |
| Context compression | `NOT_IMPLEMENTED` |
| Context validation, proposal lifecycle | `NOT_IMPLEMENTED` |
| Context envelopes created | **Zero** |
| Context proposals submitted | **Zero** |
| Canonical mutations performed via this bridge | **Zero** |
| Framework Bridge, Framework Adapters | `NOT_IMPLEMENTED` / `NONE_EXIST` |
| Agent Runtime, Agent Package Contract | `NOT_IMPLEMENTED` |
| Empirical framework validation | **`NOT_PERFORMED`** |
| Migration triggers #1, #4, #5, #6, #7 | Uncrossed |

---

## 14. Validation performed by this review

| # | Check | Outcome |
| --- | --- | --- |
| 1 | `git diff --check` (scoped) | exit `0`, baseline and post-commit |
| 2 | `py -3.9 scripts/validate_project_state.py` (Python 3.9.13) | `PASS MellyCore project scaffold validation passed`, exit `0`, baseline and post-commit |
| 3 | Changed-file allowlist | exactly eight files, all within the allowlist |
| 4 | Reviewed-subject immutability | `57cdbdf663778361` before and after |
| 5 | Original task-report immutability | `62d39a6f3a9709c7` before and after |
| 6 | Owner-document immutability | all 23 remaining files in §2.2 byte-identical |
| 7 | Exact task-ID consistency | consistent across all changed files; no variant spelling |
| 8 | 50-section recount | 50, numbered 1–50, no gap or duplicate |
| 9 | 34-row metrics recount | 34 / 34 reproduce |
| 10 | Canonical owner-reference audit | one misattribution (`NEW-P2-02`); all others correct |
| 11 | Context identity collision audit | three minted, eleven referenced, no collision |
| 12 | Context envelope overlap audit | `ContextPacket` overlap (`NEW-P2-06`) |
| 13 | Proposal lifecycle ownership and transition audit | Ingestion Gate overlap (`NEW-P2-03`) |
| 14 | Memory-category and scope audit | two unmapped rows (`NEW-P2-05`) |
| 15 | Context Graph relation audit | six of nine used, none invented, none reversed |
| 16 | Namespace audit | ten categories, no flattening path |
| 17 | Direct canonical-write audit | **no direct-write path found** |
| 18 | Return-path audit | thirteen checks; untrusted posture holds |
| 19 | Provenance audit | preserved across nine stages; never collapses |
| 20 | Sensitivity and secret-boundary audit | no downgrade path; no secret path |
| 21 | Compression and transformation audit | seven and eight, all bounded |
| 22 | Context-loss audit | six classes, four fail closed; ambiguity resolves to loss |
| 23 | Conflict and staleness audit | never auto-resolved; §17.4 consumed unchanged |
| 24 | Lease, retention, deletion audit | no storage overreach; deletion honesty verified |
| 25 | Quarantine and rejection audit | precedence gap (`NEW-P2-04`) |
| 26 | Error-taxonomy semantic-collision audit | zero name collisions; four semantic (`NEW-P2-01`) |
| 27 | Validation-layer ordering audit | thirteen ordered; layer 10 correctly discriminated |
| 28 | Mutation-eligibility intersection audit | eleven conditions, no omission found |
| 29 | Upstream seven-P2 containment audit | all seven open and contained |
| 30 | Runtime and Framework Bridge boundary audit | PASS |
| 31 | Provider / Router / tool / MCP / plugin / hook / skill / command / Batch audit | PASS |
| 32 | Observability and audit-evidence audit | no new dimension; evidence sufficient |
| 33 | Normative-modal check | 109 MUST / 71 MUST NOT / 8 MAY / 0 SHOULD / 0 SHALL; no inverted construction |
| 34 | Cross-reference and wikilink check | 15 / 15 wikilinks resolve; all §N in range; all external sections exist |
| 35 | Overclaim scan | clean |
| 36 | Secret and configuration scope check | no `.env`, secret, token, credential, provider key, workflow YAML, source, test, runtime, storage, database, vector-store, or memory configuration changed |
| 37 | Post-commit immutable verification | all 25 subjects byte-identical |

**Validators not run and not claimed passing:** `pytest`, `black`, `flake8`,
`mypy` — none applies to a documentation-only change touching no source or test
file. **Empirical framework validation: `NOT_PERFORMED`.**

---

## 15. Recommended next task

The gate passed, so no remediation task is created. Per canonical
`shared_context/RUN_QUEUE.md`, the next item in this track after this review is
recorded as the **plain name "Agent Runtime Scaffold" (inert)** — no framework
process, no provider call, no credential, no model call, no tool execution, no
deployment. It remains **blocked** and requires its own specification, independent
review, and separate explicit Operator authorization. **No identifier was minted,
started, or authorized by this review.**

The repository-wide current gate remains the OpenAI Batch final canonical state
reconciliation chain already recorded in `RUN_QUEUE.md`, unchanged, not reordered,
and not reinterpreted by this review.

---

## 16. References

- `docs/specs/MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_SPEC_001.md` (reviewed)
- `docs/tasks/MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-001.md` (read, not evidence)
- `docs/tasks/MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-REVIEW-001.md` (this review's task report)
- All owner documents enumerated in §2.2 and §3.
