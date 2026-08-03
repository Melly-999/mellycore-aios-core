# MellyCore Agent Package Contract Spec Remediation 001 — Task Report

## 1. Task identity and baseline

- Task ID: `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001`
- Root: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios`
- Starting branch: `docs/mellycore-agent-package-contract-spec-review-001`
- Starting HEAD: `f8b465bd7744343a2a3ee8e294117d1409b42437`
- Latest subject at start: `docs: review agent package contract`
- Starting worktree/index: clean (`git status --short` empty)
- Upstream tracking at start: none
- Remediation branch created from `f8b465b`:
  `docs/mellycore-agent-package-contract-spec-remediation-001`

**No network operation occurred at any point in this task.**

## 2. Reviewed specification version and review commit

- Specification reviewed: `MELLYCORE_AGENT_PACKAGE_CONTRACT_001`, version 1.0,
  commit `708e2658f57d4dccd675e16fe858ca84b143dd2b`.
- Independent review commit:
  `f8b465bd7744343a2a3ee8e294117d1409b42437`
  (`docs: review agent package contract`).
- This task advances the specification to **version 1.1**, remediating the
  review's findings; version 1.1 is itself unverified pending Review 002.

## 3. Independent review outcome consumed

`MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-001` — gate
`FAIL_REMEDIATION_REQUIRED`. P0 = 0, P1 = 1, P2 = 3, P3 = 3. Full record:
`docs/research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_001.md`
(§32–§34), cross-checked against
`docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-001.md`. Every
finding below was re-read directly from the review record's §32 before any
edit; none was reconstructed from memory.

## 4. Full finding inventory

| ID | Severity | Review record location |
| --- | --- | --- |
| `P1-01` | P1 (blocking) | §32 "P1 — Blocking" |
| `P2-01` | P2 | §32 "P2 — Material, non-blocking" |
| `P2-02` | P2 | §32 "P2 — Material, non-blocking" |
| `P2-03` | P2 | §32 "P2 — Material, non-blocking" |
| `P3-01` | P3 | §32 "P3 — Editorial / maintainability" |
| `P3-02` | P3 | §32 "P3 — Editorial / maintainability" |
| `P3-03` | P3 | §32 "P3 — Editorial / maintainability" |

All seven findings were locatable and precise in the review record; no
evidence was missing.

## 5. Remediation matrix (printed before editing, reproduced here)

| Finding ID | Severity | Exact source location | Canonical owner | Required correction | Files expected to change |
| --- | --- | --- | --- | --- | --- |
| `P1-01` | P1 | §4 (`Package Trust State` term), §17.1 intro, §16 stage 7, §5 Control Plane row | Control Plane (owns `lifecycle_status`/`approval_state`/`evidence_state` closed enums) | Remove the exact-projection claim; state package lifecycle/trust state are Agent Package domain concepts (typed entity data under Control Plane §7.1's general allowance), not projected onto Control Plane's six dimensions; state any future projection requires a dedicated mapping contract or explicit Control Plane amendment (out of scope here) | `docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md` |
| `P2-01` | P2 | §11.1 row 3, §16 stage 9, §17.3 rule 2 | Provider Registry §24 (scoped to MCP/restricted-tool records) | Rephrase all three citations as explicitly non-normative ("modeled on," not "reused from") | same file |
| `P2-02` | P2 | §12.2 rule 2 (old numbering), §18.1 layer 4 | This contract (dependency validation) vs. Agent Runtime (instantiation eligibility) | Define a deterministic evaluation boundary: dependency validation (§18.1 layer 4) is the exclusive owner of the `DEPENDENCY_UNRESOLVED` determination, evaluated before and consumed (not re-derived) by Runtime's instantiation eligibility; unresolved optional dependencies narrow scope without denying | same file |
| `P2-03` | P2 | §14 Command row, §24 command-shadowing row, §18.1 layer list | This contract (validation model) | Add explicit, enumerated, fail-closed command-namespace collision detection under §18.1 layer 1, with a dedicated normative subsection | same file |
| `P3-01` | P3 | §13.2 `claude_code` row | This contract | Replace the circular restatement with a substantive, `claude_code`-specific compatibility fact | same file |
| `P3-02` | P3 | §21 error taxonomy | This contract | Add a dedicated `COMMAND_NAMESPACE_COLLISION` error class | same file |
| `P3-03` | P3 | §7.1 `license_metadata` row, §7.2 rules | This contract | Move the absence-handling statement out of the table cell into a `§7.2` rule, consistent with how the other eleven fields' absence-handling is covered | same file |

## 6. Finding-by-finding correction table

| Finding ID | Original issue | Correction | File and section | Canonical owner preserved | Verification |
| --- | --- | --- | --- | --- | --- |
| `P1-01` | Package lifecycle (§17.1) and trust-state (§4/§19) claimed a one-directional projection onto Control Plane's `lifecycle_status`/`evidence_state`/`approval_state` "exactly as `run_state` already does," with no mapping table and no Control Plane amendment; four lifecycle states and five trust-state categories had no legal target value | Removed the exact-projection claim from §4 (`Package Trust State` entry), §17.1's intro, and §16 stage 7 (renamed "Lifecycle rendering"); each now states explicitly that package lifecycle state and Package Trust State are **Agent Package domain concepts, typed entity data under Control Plane §7.1's general allowance**, and that **this contract defines no projection onto any Control Plane §8.1 dimension**; added a clarifying sentence to §5's Control Plane ownership row and a labeling requirement in §20.2 | §4, §5, §16 (stage 7), §17.1, §20.2 | Control Plane — **not edited**; its closed enums are untouched and no new member was invented | `git hash-object docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` unchanged (§14 below); P1-regression scan (§9) found zero surviving exact-projection claims |
| `P2-01` | Provider Registry §24.2/§24.3's `operator_only`/suspension pattern cited as though reused/owned in three locations for concerns §24 does not itself govern | Rephrased all three citations (§11.1 row 3, §16 stage 9, §17.3 rule 2) as explicit non-normative parentheticals: "modeled on, but not owned or governed by, Provider Registry §24.x... §24 does not itself extend to generic package X" | §11.1, §16 (stage 9), §17.3 | Provider Registry — **not edited**; §24's scope statement is quoted, not altered | Direct re-read of all three edited passages; no fourth, previously-unflagged occurrence in the same class was found *within the review's own finding scope* (see §15, Remaining limitations, for one adjacent citation the review did not flag and this task therefore did not touch) |
| `P2-02` | `DEPENDENCY_UNRESOLVED`'s evaluation point was ambiguous between this contract's own validation time (§18.1 layer 4) and the Agent Runtime's instantiation-eligibility time (§16 stage 5) | §12.2 rule 2 (new) makes dependency validation (§18.1 layer 4) the **exclusive** owner of the `DEPENDENCY_UNRESOLVED` determination, evaluated before package verification (a precondition of instantiation eligibility); Runtime's instantiation-eligibility stage **consumes**, never re-derives, that determination; unresolved optional dependencies (new rule 4) narrow scope without denying; rule 1 states validation failure never itself installs or resolves anything | §12.2 (renumbered rules 2–5), §18.1 (layers 3–4 cross-referenced) | Agent Runtime — **not edited**; its instantiation-eligibility stage (§9) is referenced, not redefined | Re-read of §12.2, §16 stage 5, and §18.1 layers 3–4 for a single consistent reading; no remaining textual ambiguity between the two stages |
| `P2-03` | Reserved-command-collision detection required by §14/§24 was not enumerated among §18.1's nine validation layers | Added new **§14.1 "Command namespace and collision detection (normative)"** with all seven sub-requirements from the task brief (duplicate identifiers/aliases, reserved-command collisions, authorized-namespace collisions, Unicode-normalization collisions, protected-command-class overrides, package-local-declaration-is-not-activation); cross-referenced explicitly from §18.1 layer 1 and from §14's Command row and §24's command-shadowing row | §14 (new §14.1), §18.1 (layer 1), §24 | Future Command Registry remains the owner of full namespace policy (§14.1's closing sentence, §26 item 5) — this contract fixes only pre-registration rejection rules | Command-shadowing check (§13 below) confirms §18.1 layer 1 now names the check explicitly and it is enumerated with a dedicated error class |
| `P3-01` | §13.2's `claude_code` row restated the §4 terminology footnote rather than adding new compatibility information | Replaced with a substantive five-way asset-type correspondence (Skill↔skill, Hook↔hook, Command↔slash command, Plugin↔plugin, MCP Declaration↔MCP server reference) explicitly framed as "naming and shape parallel only," with the activation/permission/validation boundary restated as framework-independent | §13.2 | Runtime §11.1's six-framework closed set — unchanged | Direct re-read; row now adds information the other five rows already had |
| `P3-02` | No error class in §21 was dedicated to command-collision rejection | Added `COMMAND_NAMESPACE_COLLISION` to §21's table, and cross-referenced it from §14.1, §18.1 layer 1, and §24's command-shadowing row | §21, §14.1, §18.1, §24 | Gateway §25's error-taxonomy pattern (outward coarse, inward precise) — unchanged, reused | Error-class count recounted: 15 → 16 (§1.4 updated to match) |
| `P3-03` | `license_metadata`'s absence-handling was stated in prose inside the §7.1 table cell rather than in the rule-based format §7.2 uses for the other eleven fields | Removed the prose from the §7.1 table cell; added a new §7.2 rule 4 stating the identical substance in the same rule format as rules 1–3 | §7.1, §7.2 | No canonical owner implicated — purely this contract's own internal formatting | Direct re-read of §7.1 and §7.2 for format consistency across all twelve identity fields |

## 7. P1 architectural decision

**Remediation removed the unsupported Control Plane projection claim. No
mapping table was created, and no already-existing legal canonical mapping
was found or used.** The task brief's preferred resolution (remove the
claim; state these are Agent Package domain concepts; state that any future
projection requires a dedicated mapping contract or explicit Control Plane
amendment) was applied exactly as specified. The alternative resolution — a
minimal, additive Control Plane amendment, mirroring how `running` was
added to `lifecycle_status` for the Agent Runtime's own `P1-01` — was
**not** used, because this task's scope explicitly prohibits editing the
Control Plane owner contract to make this specification pass, and no
already-existing legal, complete mapping covering all eleven lifecycle
states and seven trust-state categories was found anywhere in the
repository. Per the task brief's stop condition, if the *only* correct
resolution required a Control Plane amendment, this task would have had to
stop and report that requirement — but it did not need to, because the
narrower, owner-preserving resolution (removing the claim) was fully
sufficient and is the one applied.

## 8. Provider Registry scope corrections

All three locations the review named (§11.1 row 3, §16 stage 9, §17.3 rule
2) were corrected to explicit non-normative "modeled on" language, stating
plainly that Provider Registry §24 does not itself govern the concern in
question. No Provider Registry responsibility was broadened; no field,
record type, or rule was added to the Provider Registry contract itself
(unedited — confirmed in §14 below).

## 9. `DEPENDENCY_UNRESOLVED` evaluation boundary

Resolved by rule, not by implementation:

- **Detecting stage:** §18.1 layer 4 (Dependency validation), exclusively.
- **Validation category:** dependency validation, explicitly distinguished
  from reference validation (layer 3), which checks only that a reference
  *resolves*, not that a dependency *constraint is satisfiable*.
- **Ordering:** dependency validation MUST complete, and reach a
  determination, before package verification (Runtime §9 state 3) — which
  is a precondition of every later state, including instantiation
  eligibility (§16 stage 5) and activation gating (§16 stage 6).
- **Required vs. optional:** an unresolved *required* dependency denies with
  `DEPENDENCY_UNRESOLVED` at validation time; an unresolved *optional*
  dependency narrows the effective feature set and MUST NOT be silently
  treated as present, active, or satisfied.
- **Owning component:** this Agent Package Contract owns the
  `DEPENDENCY_UNRESOLVED` determination itself; the Agent Runtime's
  instantiation-eligibility stage consumes that determination as one of
  Runtime §9's prerequisite states and does not independently re-derive it.
- **No installation implied:** §12.2 rule 1 now states explicitly that a
  validation failure never itself installs, fetches, activates, or resolves
  anything — this contract defines no dependency-installation mechanism.

## 10. Command-shadowing validation correction

New §14.1 (normative) enumerates all seven required checks from the task
brief and assigns each a fail-closed disposition under §18.1 layer 1:
duplicate identifiers within one package; duplicate aliases within one
package; collisions with reserved MellyCore commands (`ROADMAP.md`'s
Planned Commands); collisions with already-authorized runtime command
namespaces; Unicode NFKC-normalization-equivalent collisions; absolute,
non-liftable prohibition on overriding safety/validation/approval/Git/
provider/deployment command classes; and an explicit statement that
package-local declaration is a reference candidate only, never
environment-wide activation or namespace ownership, which remains the
future Command Registry's exclusive concern. A new `COMMAND_NAMESPACE_COLLISION`
error class (§21) gives this check a stable, dedicated rejection identity.

## 11. Editorial corrections (P3)

- `P3-01`: §13.2's `claude_code` row now states a genuine five-way
  asset-type correspondence instead of restating the §4 footnote.
- `P3-02`: `COMMAND_NAMESPACE_COLLISION` added to §21 (also closes `P2-03`'s
  missing-error-class gap).
- `P3-03`: `license_metadata`'s absence-handling moved from a §7.1 table
  cell into §7.2 rule 4, matching the rule-based format used for the other
  eleven identity fields.

## 12. Files changed

Exactly eight:

1. `docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md` (edited —
   version 1.0 → 1.1)
2. `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001.md`
   (new)
3. `shared_context/PROJECT_STATE.md` (modified)
4. `shared_context/ROADMAP.md` (modified)
5. `shared_context/RUN_QUEUE.md` (modified)
6. `shared_context/AGENT_HANDOFF.md` (modified)
7. `shared_context/PROJECT_HISTORY.md` (modified)
8. `shared_context/TASK_INDEX.md` (modified)

**Not edited:** the independent review record, the independent review task
report, the original specification task report, or any canonical
cross-check owner document (Agent Runtime, Control Plane, Provider
Registry, Integration Gateway, AI Operations Intelligence, Enterprise
Provider ADR, Shared Context contracts). No source file, test file,
workflow YAML, or `.env` file was changed.

## 13. Validators executed and exact outcomes

1. `git diff --check` → exit `0` (only benign LF/CRLF warnings).
2. `py -3.9 scripts/validate_project_state.py` → `PASS`.
3. Changed-file allowlist check: `git status --short` lists exactly the
   eight files in §12; none falls outside the authorized scope.
4. Finding-resolution check: all seven finding IDs (`P1-01`, `P2-01`,
   `P2-02`, `P2-03`, `P3-01`, `P3-02`, `P3-03`) appear in §6 above with a
   concrete disposition.
5. P1-regression check: searched the corrected specification for
   `exactly as .?run_state`, `exact control plane projection`, `direct
   mapping into closed control plane`, `lifecycle state equals control
   plane`, `trust state equals control plane`, and every remaining
   `project(s)? onto` occurrence. Every hit is either an explicit denial
   ("this contract defines no projection... onto Control Plane") or an
   unrelated, legitimate use (framework-compatibility projection onto a
   Runtime Adapter or a framework's native graph/task/turn concepts, §13,
   §16 stage 3 — never Control Plane's enums). Zero regressions.
6. Control Plane enum integrity check: `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md`
   re-hashed after this commit — byte-identical to its pre-remediation
   baseline (§14). No new Control Plane enum value appears anywhere in the
   corrected specification, and no package state is presented as a valid
   Control Plane status without an owner-defined mapping — the corrected
   text explicitly denies any such mapping exists.
7. Provider Registry ownership check: every Provider Registry reference in
   the corrected specification (nine occurrences) was reviewed; three are
   now explicit non-normative analogies, the remainder cite §24/§21 exactly
   as they did before remediation (reference-only, never redefinition).
8. Dependency evaluation check: §12.2 and §18.1 together state a single,
   deterministic evaluation stage (§9 above); no ambiguity remains.
9. Command-shadowing check: §18.1 layer 1 explicitly names the check;
   §14.1 enumerates all seven required sub-rules; §21 carries a dedicated
   error class.
10. Cross-reference and section-number check: no top-level section was
    renumbered (§14.1 and the new §7.2 rule 4 are additive subsections/rules
    within their existing parents); every internal `§` reference this task
    added or touched was checked against its target; every `[[...]]`
    wikilink resolves to an existing file.
11. Duplicate task-ID check:
    `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001` appears
    consistently across all eight changed files with one meaning.
12. Overclaim scan: see §13 (Overclaim review) below.
13. Secret and configuration scope check: no `.env` file changed; no
    secret, credential, token, or provider key introduced; no workflow YAML
    changed; no runtime or provider configuration changed.
14. Immutable-source verification: see §14 below.

`pytest`: `NOT_RUN` — no source or test file changed; not claimed passing.
Black, flake8, and mypy: not run, not claimed passing.

## 14. Overclaim review and immutable-source verification

Searched the full diff for `implemented`, `available`, `enabled`,
`installed`, `operational`, `executable`, `production-ready`, `supported`,
`accepted`, `approved`, `passed`, `live`, `deployed`. Every hit reviewed in
context is either a negated claim, a reused field/state name already
present in version 1.0 (`supported_environments`, `installed_reference`,
`runtime-enabled`), or explicit prose stating the gate remains failed and
the document remains **not accepted**. No occurrence of `passed` or
`approved` asserts this document's own gate passed or was approved; the
header explicitly states version 1.1 "does not re-open or re-claim a passed
gate."

Immutable-source verification — re-hashed after this task's commit:

| Path | Result |
| --- | --- |
| `docs/research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_001.md` | unchanged |
| `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-001.md` | unchanged |
| `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001.md` | unchanged |
| `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md` | unchanged |
| `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` | unchanged |
| `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md` | unchanged |
| `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` | unchanged |
| `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` | unchanged |
| `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md` | unchanged |
| `docs/decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001.md` | unchanged |
| `shared_context/CONTEXT_GRAPH_SCHEMA.md` | unchanged |
| `shared_context/SAFETY_CONTRACT.md` | unchanged |

## 15. Remaining limitations

1. This remediation is itself **unverified** pending independent Review 002
   — the same procedural state Remediation 001 of the Agent Runtime
   architecture occupied before its own Review 002.
2. One adjacent, previously-unflagged occurrence of the same citation
   pattern `P2-01` addressed was noticed but **deliberately not touched**:
   §17.3 rule 1 ("`retired` is terminal... mirroring Provider Registry
   §24.3's `provider_id` rule") uses the identical "mirroring Provider
   Registry" phrasing the review flagged in three *other* locations, but
   the review's `P2-01` finding did not name this occurrence, and this
   task's scope is to resolve only findings the review record actually
   raised, not to perform opportunistic cleanup beyond it. A future review
   may choose to flag it.
3. The eleven-state package lifecycle (§17.1) and seven-category trust
   vocabulary (§19.1) remain, as before, package-scoped typed data with no
   full transition-rule contract — that remains the named "Package
   Lifecycle" and "Package Distribution" follow-up contracts (§26), not
   something this remediation was scoped to complete.
4. No new capability, permission, registry, validator, or execution
   mechanism was implemented; every fail-closed distinction the task brief
   listed (`specified ≠ implemented`, `declared ≠ authorized`, etc.)
   remains textually intact and was not weakened by any correction above.

## 16. Recommended next task

`MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-002` — an independent,
read-only re-review of this remediation, in the same sequence used for the
Agent Runtime architecture (Remediation 001 → Review 002). Not started, not
authorized by this task.
