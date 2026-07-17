# MELLYCORE-LOOP-OPERATIONS-FOUNDATION-001

## Task ID

`MELLYCORE-LOOP-OPERATIONS-FOUNDATION-001`

## Outcome

PASS_LOOP_OPERATIONS_FOUNDATION_COMMITTED

## Scope

Implement a safety-first Loop Operations Foundation for MellyCore AIOS: machine-readable definitions, state contracts, deterministic read-only tooling, canonical agent skills, and documentation for recurring agent workflows ("loops").

Adapted from concepts associated with the external `loop-engineering` project. **No external code was vendored and the repository was not fetched** — see `[[../research/LOOP_ENGINEERING_ADOPTION_REVIEW_001]]`.

## Accepted Capabilities

**Registry and contracts** (`shared_context/loops/`)

- `LOOP_REGISTRY.json` — 9 loops: 6 REPORT_ONLY, 3 DISABLED
- `LOOP_REGISTRY_SCHEMA.json`, `LOOP_STATE_SCHEMA.json`, `RUN_LEDGER_SCHEMA.json`
- `RUN_LEDGER.example.json` — labelled an example, not evidence
- `LOOP_BUDGETS.json` — estimates only, labelled `ESTIMATE_NOT_MEASURED`
- `LOOP_CONSTRAINTS.md`, `README.md`, `states/README.md`

JSON rather than YAML so that no parsing dependency is introduced.

**CLI** (`scripts/loop_ops/`, standard library only, Python 3.9)

- `validate` — registry structure, unique IDs, lifecycle states, human gates, positive budgets, forbidden-path superset, Phase 1 report-only gate, state-file/template rules
- `audit` — capability tiers, distinguishing configured / validated / exercised / human_approved / production_enabled
- `guard` — deterministic circuit breaker; no model, no network
- `estimate-cost` — no-op / report / assisted / realistic scenarios with maker-checker and parallel multipliers, always labelled an estimate
- `worktree-audit` — read-only; no mutation path exists
- `redact-check` — reports file, line, and category; never a value; never rewrites

Exit codes: `0` ok/CONTINUE, `1` invalid/BLOCK_INVALID_STATE, `2` ESCALATE_HUMAN/PAUSE_BUDGET.

**Canonical skills** (`agent_prompts/loops/`) — `mellycore-loop-constraints`, `-triage`, `mellycore-context-drift`, `-verifier`, `-budget-guard`, `mellycore-worktree-audit`. Owned in one location; Claude and Codex wrappers reference rather than restate them, so they cannot drift into two rulebooks.

**Tests** (`tests/`) — 102 unittest tests, no network, no provider, no secrets, no real worktree mutation.

**Documentation** — adoption review, architecture, safety contract.

## Deferred Capabilities

Not implemented, not authorized, not reachable:

- scheduler / cron / hooks / workflow YAML — every run is started by a human
- GitHub connectors, PR comments, approvals, merges
- MCP servers
- automated fixes (`ci-sweeper`, `dependency-sweeper` DISABLED)
- dependency changes (`dependency-sweeper` DISABLED)
- worktree cleanup (`post-merge-cleanup` DISABLED)
- push, merge, deploy
- ASSISTED (L2) and unattended (L3) operation
- dashboard / frontend integration
- provider or runtime integration

## Validation Evidence

Every command below was run from `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios` on branch `publish/mellycore-main-001`.

| Command | Outcome |
| --- | --- |
| `py -3.9 scripts/validate_project_state.py` (baseline, before changes) | PASS |
| `py -3.9 scripts/validate_project_state.py` (after changes) | PASS |
| `py -3.9 -m scripts.loop_ops validate` | PASS — 9 loops, 0 findings, exit 0 |
| `py -3.9 -m scripts.loop_ops audit --json` | exit 0 — 0 exercised, 0 production_enabled |
| `py -3.9 -m unittest discover -s tests -p "test_loop_ops*.py"` | OK — 102 tests |
| `py -3.9 -m compileall -q scripts/loop_ops` | PASS |
| `git diff --check` | PASS — no whitespace errors |
| `py -3.9 -m scripts.loop_ops redact-check --path shared_context/loops` | PASS — no findings |
| Forbidden-path / capability scan of changed files | PASS — matches were prohibition text only |

**Not claimed:** no linter, type checker, or coverage tool was run — none is configured in this repository. No loop was executed, so there is no run evidence and no measured token spend.

## Remaining Risks And Limitations

1. **No loop has ever been run.** The foundation is configured and validated, not exercised. The guard's behaviour is proven against fixtures, not against a real agent run.
2. **The adoption review cites no commit SHA.** The external repository was not fetched, per this task's safety posture. Claims about its limitations are inherited from the task brief and independently unverified.
3. **Redaction is heuristic.** A clean scan is not proof that no secret is present.
4. **`validators.py` enforces the JSON Schema files in plain Python**, since no dependency may be added. The two could drift; that would be a defect to fix, not a rule to reinterpret.
5. **Budget enforcement is inert today.** With no measured token data, the guard reports budgets as `unenforceable`. This is deliberate and honest, but it means budgets are currently a contract, not a control.
6. **Worktree `task_hint` is heuristic**, derived from branch naming. It may miss a collision or flag a false one.
7. **The `changelog-drafter` write scope is empty**, so its draft is returned in the run report rather than written. That is a Phase 1 constraint, not a finished workflow.

## Safety Confirmation

No secrets, no `.env`, no provider keys or integration, no network calls, no workflow YAML, no dependency changes, no frontend/backend/runtime code, no trading or broker capability, no MellyTrade mutation, no push/merge/deploy, no destructive git, no scheduler.

The repository was not fetched from `loop-engineering` and no external code was vendored.

## Recommended Phase 2

`MELLYCORE-LOOP-REPORT-ONLY-DRY-RUN-001` — hand-run the `project-health` loop once, produce a real run ledger, and check the guard against real input. Narrow: one loop, one run, no new capability.

## Related Documents

- `[[../research/LOOP_ENGINEERING_ADOPTION_REVIEW_001]]`
- `[[../architecture/MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001]]`
- `[[../safety/MELLYCORE_LOOP_SAFETY_CONTRACT_001]]`
- `[[../../shared_context/loops/README]]`
- `[[../../agent_prompts/loops/README]]`
