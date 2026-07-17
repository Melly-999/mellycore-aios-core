# MELLYCORE-ROADMAP-COMMAND-001

## Task ID

`MELLYCORE-ROADMAP-COMMAND-001`

## Outcome

`PASS_ROADMAP_COMMAND_COMMITTED_NO_PUSH`

## Scope

Rename/reframe the project status command from `/status-aios` to `/roadmap` as the standard operator command for showing: current project state, current branch/HEAD/release, milestone status, task counts remaining per milestone, current next task, recommended model and effort, safety posture, and push/release status. Docs-only per the task's own instruction ("implement docs-only unless a command registry already exists").

## 1. Preflight

- Repo root: `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios` (confirmed)
- HEAD: `de6ae75fe48975a378d88ce2b9e55beaf435dce1` (confirmed, matching the prior committed task)
- Working tree: clean before any edit

## 2. Where `/status-aios` was documented

Searched the full repository for `status-aios`, `project-status`, `/status`, any `.claude/commands/` directory, and any command list/palette in `site/dashboard.html` or `site/js/dashboard.js`. Found exactly **one** occurrence: a section heading (`## `/status-aios` preflight`) in `docs/tasks/MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I3-001.md`, an informal label a prior task used for its own preflight section — never a registered command, never documented as reusable, never referenced by any other file. No command registry exists anywhere in this repository.

Conclusion: implementation is docs-only (per the task's own instruction), and `/status-aios` is **not** carried forward as a supported legacy alias, since it was not "already referenced heavily" (it appears exactly once, informally). That one historical heading is left untouched as an accurate record of what that task did at the time — it is not renamed retroactively.

## 3. What changed

- **New:** `docs/runbooks/MELLYCORE_ROADMAP_COMMAND.md` — the full `/roadmap` command definition: the eight required output fields, exactly which committed file each field is sourced from, an example answer shape (with milestone pending-counts verified against the current `shared_context/ROADMAP.md`), the legacy-naming note explaining why `/status-aios` is not kept as an alias, and an explicit scope/posture statement (docs-only; no dashboard/site code touched; no `ContextSource` record read).
- **New:** `docs/tasks/MELLYCORE-ROADMAP-COMMAND-001.md` (this report).
- **Updated:** `shared_context/ROADMAP.md` — added an "## Operator Commands" section at the top with the `/roadmap` definition and a pointer to the full runbook.
- **Updated:** `shared_context/RUN_QUEUE.md` — added item 59 recording this task's completion.
- **Updated:** `shared_context/PROJECT_STATE.md` — added a `/roadmap` completion note under "Post-v0.2.0 work"; also corrected a stale claim found while editing this file: `MELLYCORE-GITHUB-SOURCE-PROVIDER-DEMO-001` was still described as "being added" (in progress) even though it is complete and committed at HEAD — corrected to **complete** in the same edit, since leaving a known direct contradiction in a file already being edited for this task would be worse than fixing it.
- **Updated:** `shared_context/AGENT_HANDOFF.md` — added a new top "Latest completed task" entry for this task (moving the prior entry to "Previous completed task"), and updated the bottom "Next recommended task" line to keep the still-open GitHub-provider-card review recommendation (it was performed in-conversation in a prior session but produced no committed report, per its own strict read-only/no-commit instructions, so it is not yet reflected as done here) while adding the new recommended review of this `/roadmap` doc.

## 4. Command registry check

No `.claude/commands/` directory, no CLI command dispatcher, and no dashboard command list or command palette exist anywhere in this repository (`site/dashboard.html` and `site/js/dashboard.js` were both grepped and contain no such surface — the only matches were unrelated references to `shared_context/ROADMAP.md` the data file). Per the task's own instruction, dashboard/site code was **not** touched.

## 5. Validation

| Check | Result |
| --- | --- |
| `py -3.9 -m scripts.context_gate audit --json` | 0 findings, index current |
| `py -3.9 -m scripts.loop_ops validate` | PASS |
| `py -3.9 -m scripts.validate_project_state` | PASS |
| `py -3.9 -m unittest discover` | 245/245 passing |
| `git diff --check` | clean, no whitespace errors |

## 6. Safety confirmation

- Docs-only; no dashboard/site code, script, or test file was changed.
- No `ContextSource` record was read, created, or modified; no canonical `shared_context/context_provenance/` file was touched.
- No secrets, API keys, or credentials were added or referenced.
- No push, PR, merge, or deploy performed; commit is local only.
- Old `origin` remote was not fetched, read, or pushed.

## 7. Next recommended task

An independent read-only review of this `/roadmap` command doc — confirm each field's sourcing is accurate, confirm the milestone pending-counts in the example match `shared_context/ROADMAP.md`, and confirm no dashboard/site scope creep occurred — before any further operator-tooling work. The previously recommended independent review of the GitHub Repository provider-demo card (`MELLYCORE-GITHUB-SOURCE-PROVIDER-DEMO-001`) also remains open in the repository's own record, since that review's own instructions forbade committing a report.
