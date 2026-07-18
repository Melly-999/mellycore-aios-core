# Run Queue

This file contains actionable sequencing and gates. Completed-task detail belongs
in `docs/tasks/` and Git history, not duplicated here.

## Integration Gate

1. Review the single signed local commit produced by
   `MELLYCORE-POSITIONING-REFRESH-001`.
2. Under separate authorization, push only that immutable commit to a new
   canonical remote branch and create a review PR.
3. Do not start the next roadmap task until the positioning refresh is integrated.

## Exact Next Roadmap Task

`MELLYCORE-AI-OPERATIONS-INTELLIGENCE-001`

Type: documentation/specification.

Goal boundary: define the operational-intelligence contract for Mission Control,
Agent Activity, Context Pulse, Model Router, Unified Run Ledger, Approval Queue,
Memory & Recommendation Ledger, AI Estate Inventory, Skill Gap Detector, and
Memory Freshness Monitor.

Required posture:

- distinguish implemented evidence from planned capability;
- preserve operator approval for consequential action;
- define visibility, provenance, audit, freshness, and recommendation boundaries;
- do not implement adapters, backend execution, autonomous improvement, merge,
  deployment, scheduler, or safety-rule mutation;
- do not store provider keys or credentials.

## Later Roadmap Domains

After a reviewed intelligence specification, separately approved work may address
real adapters, guarded operations, observability UI, and validation evidence.
No implementation task is authorized by this queue entry.

## Deferred Work

- Cross-agent context smoke testing remains a separate clean-worktree task.
- Provider/runtime integrations, deployment, releases, and Holographic UI
  implementation remain separately gated.
- Legacy NASA prototype cleanup is a future implementation decision, not part of
  the current product roadmap and not performed by the positioning task.

## Completed Milestone Index

- Static homepage and Living Context Graph prototype — historical reports under
  `docs/tasks/` and showcase evidence under `docs/showcase/`.
- Operational Trust / Loop Operations — closed; architecture and task evidence
  under `docs/architecture/`, `docs/research/`, and `docs/tasks/`.
- Context Gate I1–I4 — implemented; canonical evidence under
  `shared_context/context_provenance/` and completed reports under `docs/tasks/`.
- Live Cockpit V2 / `v0.2.0` — historical release and legacy prototype evidence.
- Holographic UI specification / PR #4 — accepted documentation; Source Arena
  hero contract preserved, implementation not claimed.
- Positioning refresh — current local documentation task; durable report at
  `docs/tasks/MELLYCORE-POSITIONING-REFRESH-001.md`.

## Standing Safety Gate

No push, PR, merge, force operation, rebase, squash, branch deletion, tag,
release, deploy, workflow mutation, trading behavior, credential storage, or
retired-remote contact without explicit operator authorization.
