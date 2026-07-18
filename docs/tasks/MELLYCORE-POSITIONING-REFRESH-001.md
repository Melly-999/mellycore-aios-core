# MELLYCORE-POSITIONING-REFRESH-001

Status: complete locally (docs-only, one signed commit, not pushed).

## Purpose and Scope

Refresh MellyCore AIOS after the PR #4 specification merge so current
documentation positions the product as a local-first, operator-controlled AI
Operations Observatory. This task changes documentation/shared context only. It
does not modify the site, runtime tooling, evidence records, workflows, or remote
state.

## Previous Positioning Problem

Current public and shared-context documents still led with the Living Context
Graph or NASA Images demo and repeated transient PR, branch, and commit facts.
That obscured the operator, the operational-intelligence direction, and the
boundary between implemented foundations and future capability. It also created
the maintenance/drift risk identified by Sourcery's advisory review.

## Refreshed Canonical Positioning

MellyCore AIOS is a **local-first, operator-controlled AI Operations
Observatory**. Its purpose is to make models, agents, runs, context, memory,
recommendations, and approvals visible, inspectable, approval-gated, and
auditable.

Controlled improvement loop:

`observe → analyze → recommend → approve → implement → validate → record`

Human/operator approval remains mandatory for consequential action. The system
does not autonomously alter safety rules, merge, deploy, execute recommendations,
or use uncontrolled tools.

## Current Versus Planned Capability

Implemented today:

- static local documentation and presentation surfaces;
- report-only Loop Operations with immutable evidence;
- Context Gate through I4 with guarded admission, canonical records, a
  content-free index, computed audit, and read-only Context surface;
- human-invoked `project-health` evidence;
- a legacy Live Cockpit V2 / Social Source Arena prototype.

Specified but not implemented:

- the accepted Holographic Source Arena 390×844 model-lens hero and 3D treatment.

Planned:

- Mission Control;
- Agent Activity;
- Context Pulse;
- Model Router;
- Unified Run Ledger;
- Approval Queue;
- Memory & Recommendation Ledger;
- AI Estate Inventory;
- Skill Gap Detector;
- Memory Freshness Monitor;
- real adapters, guarded runtime operations, and approval execution.

The next task defines the detailed AI Operations Intelligence contract. This
positioning task deliberately does not design its schema or implement it.

## NASA Images Disposition

NASA Images is no longer a current product pillar, roadmap module, or intended
core integration. Browser-side NASA Images API behavior remains in the repository
as legacy prototype implementation and historical `v0.2.0` evidence. No code was
removed by this documentation task, and completed task/release reports were not
rewritten. A future implementation cleanup may retire or replace the prototype
under separate authorization.

## Source Arena Visual Role

Source Arena remains the leading holographic metaphor and intended first hero
experience. The accepted PR #4 requirements remain intact: mobile 390×844
model-lens composition first; Source Arena lead image everywhere;
Overview/core/orbit/hull supporting only; visible real/simulated/planned labels.
The accepted specification remains specification-only and does not prove the
holographic UI exists.

## AI Operations Observatory Module Map

| Domain | Current status | Positioning boundary |
| --- | --- | --- |
| Mission Control | Planned | Objectives, gates, blockers, operator decisions. |
| Agent Activity | Planned | Inspectable activity/evidence, no uncontrolled tool use. |
| Context Pulse | Foundation partially implemented | Context Gate evidence exists; the Observatory view is planned. |
| Model Router | Planned | Roles are documented; evidence-backed routing runtime is not implemented. |
| Unified Run Ledger | Foundation partially implemented | Loop ledgers exist; unified cross-domain ledger is planned. |
| Approval Queue | Planned | Operator-gate concepts exist; execution surface is not implemented. |
| Memory & Recommendation Ledger | Planned | No recommendation-execution backend exists. |
| AI Estate Inventory | Planned | Inventory contract remains to be specified. |
| Skill Gap Detector | Planned | Analysis and evidence model remain to be specified. |
| Memory Freshness Monitor | Planned | Context freshness signals exist; unified monitor is planned. |

## Safety and Non-Goals

- No trading operations or MellyTrade runtime linkage.
- No autonomous safety-rule modification, merge, deployment, or recommendation execution.
- No provider keys, credentials, secrets, account identifiers, or private runtime state.
- No claim that a production backend, real adapter estate, approval executor, or
  autonomous improvement system already exists.
- Real adapters and guarded operations remain later, separately approved milestones.

## Sourcery Advisory Resolution

The three shared-context files now have distinct responsibilities:

- `PROJECT_STATE.md`: concise durable identity, implemented/spec/planned state,
  release integrity, and safety boundaries.
- `RUN_QUEUE.md`: actionable integration gate, exact next task, and later/deferred sequencing.
- `AGENT_HANDOFF.md`: minimum next-run context and safety reminders.

Long task narratives and transient PR/branch/SHA facts were removed from current
shared context. Durable audit evidence remains in completed task reports, release
records, and Git history.

## Files Changed

- `README.md`
- `docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md` (supersession notice only)
- `docs/tasks/MELLYCORE-POSITIONING-REFRESH-001.md`
- `shared_context/PROJECT_STATE.md`
- `shared_context/AGENT_HANDOFF.md`
- `shared_context/RUN_QUEUE.md`
- `shared_context/ROADMAP.md`
- `shared_context/DESIGN_SYSTEM.md`

Completed historical task reports, site code, canonical provenance records,
refusal logs, and loop evidence remain unchanged.

## Acceptance Review

- P1 Canonical identity: PASS.
- P2 Problem and operator: PASS.
- P3 Source Arena: PASS.
- P4 NASA disposition: PASS.
- P5 Implementation truthfulness: PASS.
- P6 Safety boundaries: PASS.
- P7 Next-task boundary: PASS.
- P8 Shared-context quality: PASS.
- P9 Transient facts: PASS.
- P10 Historical integrity: PASS.
- P11 Documentation-only scope: PASS.
- P12 No current-direction contradiction: PASS.

## Validation Evidence

The final signed commit was authorized only after all of the following passed:

- `py -3.9 -B -m scripts.context_gate audit --json` — 0 findings, index current, 0 writes.
- `py -3.9 -B -m scripts.loop_ops validate` — PASS.
- `py -3.9 -B scripts/validate_project_state.py` — PASS.
- `py -3.9 -B -m unittest discover` — 245 tests passing.
- `git diff --check` — clean.
- Scope/secret/credential/private-key/retired-URL/current-positioning searches — clean.

## Next Task

After this positioning commit is reviewed and integrated:

`MELLYCORE-AI-OPERATIONS-INTELLIGENCE-001`

That task is a specification task, not implementation authorization.
