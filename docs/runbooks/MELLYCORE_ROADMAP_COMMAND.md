# MellyCore `/roadmap` Operator Command

**Status:** active (added by `MELLYCORE-ROADMAP-COMMAND-001`). This is a docs-only command definition — a standard operator prompt/checklist that a human or agent answers by reading the files listed below. No command registry, CLI subcommand, or dashboard command list exists anywhere in this repository, so `/roadmap` is not backed by any executable code.

## Definition

```
/roadmap:
Show current MellyCore AIOS roadmap, milestone completion, task counts, current
release, branch state, next recommended task, model/effort recommendation, and
safety reminders.
```

`/roadmap` is the standard operator command for a full project-status read. Any agent asked to run `/roadmap` should produce the eight items below, each sourced from a specific committed file — never invented, never carried over from memory of a prior session.

## What `/roadmap` reports, and where each field comes from

1. **Current project state** — `shared_context/PROJECT_STATE.md`, top summary and the current "work in progress" / status section.
2. **Current branch / HEAD / release** — `git branch --show-current` and `git rev-parse HEAD`, cross-checked against `shared_context/PROJECT_STATE.md`'s "Current official release" section (release tag, commit, release URL).
3. **Milestone status** — `shared_context/ROADMAP.md`, the "## Milestone Tracks" section (Milestones A–E), reading each milestone's **completed** / **pending** / **closed** markers.
4. **Task counts remaining per milestone** — count the bullets marked `**pending**` under each milestone heading in `shared_context/ROADMAP.md`.
5. **Current next task** — `shared_context/AGENT_HANDOFF.md`'s "Next recommended task" line, cross-checked against the most recent numbered entry in `shared_context/RUN_QUEUE.md`.
6. **Recommended model and effort** — `shared_context/MODEL_ROUTING.md`'s routing roles (Claude for architecture/reasoning/documentation/review; Codex for implementation/validation/PR prep; Grok for critique/adversarial review; GLM for cheap drafting/iteration), matched to the next task's nature. State it in the same short form already used in `docs/tasks/MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I1-001.md` ("Recommended model/effort: **<Model>, <Effort>**").
7. **Safety posture** — `shared_context/SAFETY_CONTRACT.md` plus the "Safety boundaries (current)" section of `shared_context/PROJECT_STATE.md`. Never read canonical `ContextSource` record bodies for this.
8. **Push/release status** — `shared_context/PROJECT_STATE.md`'s "Current official release" section (published SHA/tag/URL) plus the most recent `shared_context/RUN_QUEUE.md` entry's push/no-push note.

## Example answer shape

```
MellyCore AIOS — /roadmap

State:      <one-line summary from PROJECT_STATE.md>
Branch:     <branch> @ <HEAD short SHA>
Release:    <tag> (<commit>) — <published URL, or "not yet released">
Milestones: A closed | B implemented through I4 | C/D/E pending
Remaining:  A 0 pending | B 3 pending | C 5 pending | D 5 pending | E 3 pending
Next task:  <task ID from AGENT_HANDOFF.md "Next recommended task">
Model/effort: <Model>, <Effort>
Safety:     static-first; no secrets/live trading/deploy/push without explicit approval
Push state: <pushed to clean-origin/main at <SHA> | committed, not pushed>
```

The remaining-count figures above are illustrative snapshots as of this command's addition (`MELLYCORE-ROADMAP-COMMAND-001`, at HEAD `de6ae75f`) — always recount live against `shared_context/ROADMAP.md` rather than trusting this example, since it drifts as tasks complete.

## Legacy naming note

An informal `/status-aios` heading was used exactly once, as an ad hoc section title in `docs/tasks/MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I3-001.md`'s preflight section. It was never a registered command, never defined anywhere, and is not referenced by any other doc, runbook, or command registry (no command registry exists in this repository). Because it was not "already referenced heavily," per this task's own instructions `/status-aios` is **not** carried forward as a supported legacy alias. `/roadmap` is the first formally documented operator status command in this repository. The one historical heading in the I3 task report is left untouched as an accurate record of what that task actually did at the time — it is not renamed retroactively.

## Scope and posture

- Docs-only. No command registry, CLI subcommand, dashboard command list, or command palette exists anywhere in this repository (`site/dashboard.html` and `site/js/dashboard.js` were checked and contain no such surface), so per this task's own instructions, no dashboard/site code was touched.
- No `ContextSource` record was read, created, or modified. `/roadmap`'s safety-posture output pulls only from `SAFETY_CONTRACT.md` and `PROJECT_STATE.md`, never canonical provenance records or the refusal log.
- `/roadmap` is a read-only operator status prompt, not an executable script, CLI command, or dashboard feature. Running it never writes to the repository, calls a provider, or pushes to any remote.

## Related documents

- `[[../../shared_context/AGENT_HANDOFF]]`
- `[[../../shared_context/ROADMAP]]`
- `[[../../shared_context/RUN_QUEUE]]`
- `[[../../shared_context/PROJECT_STATE]]`
- `[[../../shared_context/MODEL_ROUTING]]`
- `[[../../shared_context/SAFETY_CONTRACT]]`
- `[[../tasks/MELLYCORE-ROADMAP-COMMAND-001]]`
