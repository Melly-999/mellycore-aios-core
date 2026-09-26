# MELLYCORE-SKILL-PLUGIN-ROUTING-CONTRACT-001
## Final Report

## 1. RESULT

`PASS_WITH_LIMITATIONS`

Limitations: the contract is **drafted and unverified** (no independent
review has run — by design, the author cannot review its own work under
`AGENTS.md`); Klaus does not exist in canonical state, so Klaus coverage is a
forward contract only; no repository-native validator checks spec semantics,
so architecture validation below is by reading, not by tooling.

## 2. BASELINE

Repository: `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios` (remote
`clean-origin` → `Melly-999/mellycore-aios-core`)
Worktree: primary checkout (the repository also has other registered
worktrees; none touched)
Branch: `docs/claude-code-workflow-hardening-landing-001` — the same branch
used by the two immediately preceding docs tasks
(`CLAUDE-CODE-WORKFLOW-HARDENING-LANDING-001`,
`MELLYCORE-PROMPT-STANDARDIZATION-001`); 6 commits ahead of and 0 behind
`clean-origin/main` at start.
Start HEAD: `d7336ad4092da66819e8b85f364f3cbce51d1f40`
End HEAD: recorded in session tool output rather than self-declared here
(this file is part of the commit that produces it).
Initial status: clean tracked tree; 8 pre-existing untracked user paths
(`.opencode/`, `opencode.jsonc`, screenshot/image files under `docs/`),
unrelated and left untouched.
Note: `C:\AI` itself is not a git repository; the session's initial
git-status snapshot did not describe this repository.

## 3. INPUTS USED

Read in full: `AGENTS.md`, `CLAUDE.md`, `PROJECT_RULES.md`,
`.claude/commands/plan-task.md`, `shared_context/MODEL_ROUTING.md`,
`TOOLING.md`, `VALIDATION.md`.
Read in targeted sections: `shared_context/RUN_QUEUE.md` (head),
`TASK_INDEX.md` (conventions, Developer Platform lane),
`ROADMAP.md` (Developer Platform milestones), `AGENT_HANDOFF.md` (format),
`SAFETY_CONTRACT.md` (headings);
`docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md` §1, §14, §17, §19, §26;
`docs/specs/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001.md` header, section
map, §13–§14;
`docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md` header, §11, §15, §23;
`docs/decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001.md` header;
`docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md` §13;
`docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` §12 and
risk-tier references; `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md`
§7.2 `Skill` entity row; `docs/tasks/MELLYCORE-PROMPT-STANDARDIZATION-001.md`
(report template).
External: Codex skill discovery roots and the `agents/openai.yaml`
`policy.allow_implicit_invocation` default, from the `openai/codex` source via
Context7 (read-only).
Repository search: `klaus` → zero matches in the repository's Markdown.

## 4. FILES CHANGED

| File | Change |
| --- | --- |
| `docs/specs/MELLYCORE_SKILL_PLUGIN_ROUTING_CONTRACT_SPEC_001.md` | New — the contract |
| `docs/tasks/MELLYCORE-SKILL-PLUGIN-ROUTING-CONTRACT-001.md` | New — this report |
| `shared_context/TASK_INDEX.md` | +2 rows (contract, review); Skills Layer note extended |
| `shared_context/ROADMAP.md` | Skills Layer milestone: lane-order note |
| `shared_context/AGENT_HANDOFF.md` | New top entry |

No `site/**`, `scripts/**`, `tests/**`, `skills/**`, `.claude/**`, config,
workflow YAML, `.env`, or runtime file changed.

## 5. KEY FINDINGS DRIVING THE DESIGN

1. **Existing owners already frame the seam.** Package §26 names Skill and
   Plugin Registries; `TASK_INDEX.md` already holds `PLANNED`
   `MELLYCORE-SKILLS-LAYER-SPEC-001`, `-PLUGIN-LAYER-SPEC-001`,
   `-DEVELOPER-PLATFORM-SPEC-001`, and `-PACKAGE-ECOSYSTEM-SPEC-001`. The new
   contract is scoped to *selection/routing* and imposes requirements on
   those specs instead of duplicating them.
2. **Runtime §23 is the routing pattern to reuse** (request → decide →
   record; `NO_PERMITTED_MODEL`, `ROUTING_TIE_UNRESOLVED`).
3. **Runtime §15's envelope already is the "execution plan"** — hence no
   Execution Planner contract.
4. **Runtime §11.1 has no `codex` framework type** — hence adapters are
   packaging projections, not bridges.
5. **Canonical R0–R5 risk tiers already exist** (ADR §13, Gateway). A first
   draft defined a conflicting R0–R4 ladder; verification caught it and it
   was corrected to consume the canonical vocabulary before commit.
6. **Codex implicit invocation defaults to `true`** — a silent trust widening
   the Codex adapter must override.

## 6. SKILLS USED

| Skill | Reason | Decision informed |
| --- | --- | --- |
| `engineering:architecture` | Entry command; ADR-level framing | D-01–D-06 structure and ownership table |
| `engineering:system-design` | Router/registry/adapter design frame | §7 request and outcomes, §8 advisor diagram, trade-offs |
| `ecc:agent-architecture-audit` | Independent routing-ownership lens | Klaus as consumer (D-04); undeclared fallback = hidden repair loop (§7.6); "use tool X" in skill text is not a grant (D-05) |
| `ecc:hexagonal-architecture` | Targeted port/adapter check | §9 adapter model; inward dependency; regenerable adapters |
| `ecc:architecture-decision-records` | Formalize decisions | Nygard-form D-01–D-06 inside the spec; its `docs/adr/` layout rejected in favour of this repository's `docs/decisions/` convention |
| `product-management:synthesize-research` | Consolidate Anthropic/Codex/ECC/third-party patterns | §15 adoption matrix; §10–§11 adapter semantics |
| `product-management:roadmap-update` | Register the lane after decisions | ROADMAP note framed as a dependency re-map, not a reprioritization |

## 7. SKILLS CONSIDERED BUT NOT USED

- `ecc:autonomous-loops` — not invoked; loop compatibility for use case D was
  checked directly against Runtime §28 (retry/reconciliation) instead (spec
  §12.3 closing note).
- `cowork-plugin-management:create-cowork-plugin`,
  `cowork-plugin-management:cowork-plugin-customizer` — prohibited in this
  run; considered by name only.
- `ecc:agentic-os`, `ecc:backend-patterns` — not needed; no runtime design.
- `engineering:deploy-checklist`, `engineering:incident-response` — out of
  scope by instruction.

## 8. FUTURE TASK MATRIX

| Task ID | Decision | Dependencies | Reason | Model | Effort | Skills |
| --- | --- | --- | --- | --- | --- | --- |
| `MELLYCORE-SKILL-PLUGIN-ROUTING-CONTRACT-REVIEW-001` | KEEP (minted, `ELIGIBLE`) | this contract | Mandatory independent gate | Opus (different session) | High | `.claude/commands/review.md`, `ecc:agent-architecture-audit` |
| `MELLYCORE-SKILL-LIBRARY-ARCHITECTURE-001` | REJECT (duplicate) | — | Same slot as existing `MELLYCORE-SKILLS-LAYER-SPEC-001` | — | — | — |
| `MELLYCORE-SKILL-REGISTRY-001` | REJECT as a new ID | — | Registry spec = Skills Layer; registry implementation is a later, unnamed task after that spec passes review | — | — | — |
| `MELLYCORE-SKILLS-LAYER-SPEC-001` (existing) | AMEND (dependency added) | review above | Must satisfy spec §6 | Opus | High | `engineering:system-design` |
| `MELLYCORE-PLUGIN-LAYER-SPEC-001` (existing) | KEEP | review above | Plugin ≠ routing unit (spec §4) | Opus | High | `engineering:architecture` |
| `MELLYCORE-CLAUDE-SKILL-ADAPTER-001` | DEFER | Skills Layer spec accepted | Needs the canonical schema first | Sonnet or Codex | Medium | `plugin-dev:skill-development` |
| `MELLYCORE-CODEX-SKILL-ADAPTER-001` | DEFER | Skills Layer spec accepted | Same; must emit `allow_implicit_invocation: false` for `explicit_only` | Codex | Medium | Codex docs via Context7 |
| `KLAUS-SKILL-ROUTER-001` | REJECT | — | Klaus must not own routing (D-04) | — | — | — |
| `KLAUS-CORE-SKILL-PACK-001` | DEFER | Klaus registered as an agent package; Skills Layer accepted | Klaus absent from canonical state | Opus | High | `engineering:architecture` |
| `MELLYCORE-SKILL-EVALS-001` | DEFER | Skills Layer accepted | Eval fixtures need the schema | Sonnet | Medium | `ecc:eval-harness` |
| `MELLYCORE-SKILL-LIBRARY-UI-001` | DEFER | Skills Layer implemented; frontend gates | Frontend is gated; the Control Plane `Skill` projection owns the UI surface | — | — | — |
| `MELLYCORE-EXECUTION-PLAN-CONTRACT-001` | REJECT | — | Runtime §15 envelope already owns it (D-03) | — | — | — |
| Runtime §15 skill-reference amendment (plain name, no ID minted) | DEFER | review above | Additive; owned by the Runtime spec | Opus | High | `engineering:architecture` |

## 9. VALIDATION EXECUTED

| Command | Result | Evidence |
| --- | --- | --- |
| `python scripts/validate_project_state.py` | passed | `PASS MellyCore project scaffold validation passed`, exit 0 |
| `git diff --check` | passed | exit 0, no output |
| Trailing-whitespace grep on the new spec | passed | no matches |
| Secret-pattern grep (OpenAI / AWS / GitHub / Slack / private-key / literal api-key patterns) over the new spec and the three edited `shared_context` files | passed | exit 1 (no matches) |
| Wiki-link resolution for every `[[…]]` in the new spec | passed | 8/8 targets exist |
| `git status --short` | as expected | only this task's paths plus the 8 pre-existing untracked user paths |

The checks above ran before this report was created; they are re-run over
the final file set before commit, and that re-run is recorded in session
output.

Architecture validation (by reading, not tooling): criteria 1–10 of spec §20
hold; §3 assigns exactly one owner per concern; the canonical risk-tier and
lifecycle vocabularies are consumed, not redefined.

## 10. VALIDATION NOT AVAILABLE

- No repository-native Markdown linter or spec-schema validator exists.
- The unit test suite (`tests/`) exercises runtime modules this docs-only
  change does not touch; not run, as not applicable.
- No automated check exists for cross-spec ownership conflicts; this was done
  by manual reading and is the main thing the independent review must
  re-verify.

## 11. SAFETY CONFIRMATION

No runtime, backend, or frontend code; no dependency, plugin, or MCP
installation; no provider integration or credentialed call (the Context7
documentation lookup is read-only and credential-free); no secrets or `.env`
accessed; no workflow YAML; no push, merge, PR, deploy, or destructive git
command. The Global Pointer and frontend gates are unchanged.

## 12. NEXT CANONICAL TASK

`MELLYCORE-SKILL-PLUGIN-ROUTING-CONTRACT-REVIEW-001`
