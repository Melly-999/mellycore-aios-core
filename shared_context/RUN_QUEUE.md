# Run Queue

This file contains actionable sequencing and gates. Completed-task detail belongs
in `docs/tasks/` and Git history, not duplicated here.

## Integration Gate

1. Review the single signed local commit produced by
   `MELLYCORE-AI-OPERATIONS-INTELLIGENCE-001` on branch
   `docs/mellycore-ai-operations-intelligence-001`.
2. Under separate authorization, push only that immutable commit to a new
   canonical remote branch and create a review PR.
3. Do not start the next roadmap task until this specification is integrated.

## Exact Next Roadmap Task

`MELLYCORE-OPERATIONS-DATA-CONTRACT-001`

Type: documentation/fixture-and-schema specification.

Goal boundary: translate the approved logical contracts in
`docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` (AI Estate
Inventory, Unified Run Ledger, Skill Gap Detector, Memory Freshness Monitor,
Recommendation Ledger, and the exact operator-approval contract) into
fixture/schema artifacts and validation requirements.

Required posture:

- distinguish implemented evidence from planned capability;
- preserve operator approval for consequential action;
- preserve the existing run/token and Context Gate contracts, referencing rather
  than redefining them;
- define visibility, provenance, audit, freshness, and recommendation boundaries;
- do not implement adapters, backend execution, autonomous improvement, merge,
  deployment, scheduler, runtime-consumed schema, or safety-rule mutation;
- do not store provider keys or credentials.

## Later Roadmap Domains

After a reviewed intelligence specification, separately approved work may address
real adapters, guarded operations, observability UI, and validation evidence.
No implementation task is authorized by this queue entry.

## Parallel Decision Track — Source Arena Renderer

This track is independent of, and does not reorder, the primary roadmap
sequence above. It does not begin before, does not supersede, and does not
require `MELLYCORE-OPERATIONS-DATA-CONTRACT-001` to be integrated first.

1. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-001` — complete (docs-only, this
   commit). Records `docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md`,
   status PROPOSED, pending push/PR and independent review.
2. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-001` — independent
   Codex/GPT-5.6 Sol review of supersession scope, consistency, Git diff, and
   acceptance criteria. Not started.
3. `MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001` — remove active NASA
   API calls and `nasa-*` active runtime handles from the Source Arena surface,
   preserving historical evidence; may run as the first bounded slice of task 4
   if the accepting review prefers that grouping. Not started.
4. `MELLYCORE-3D-SCENE-FOUNDATION-001` — implement the shared state, complete
   CSS fallback, vendored/pinned Three.js enhanced renderer, lifecycle,
   context-loss recovery, and mobile-first Source Arena. Not started.
5. `MELLYCORE-3D-SCENE-ACCESSIBILITY-PERFORMANCE-QA-001` — keyboard/screen-reader
   parity, reduced-motion, forced-fallback, context-loss, memory/RAF cleanup,
   mobile and desktop performance. Not started.
6. `MELLYCORE-3D-SCENE-INTEGRATION-REVIEW-001` — independent final review
   before any merge or release claim. Not started.

None of tasks 2–6 is implemented, active, or authorized by this entry alone.

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
- Positioning refresh — integrated into canonical main; durable report at
  `docs/tasks/MELLYCORE-POSITIONING-REFRESH-001.md`.
- AI Operations Intelligence specification — current local documentation task;
  durable report at `docs/tasks/MELLYCORE-AI-OPERATIONS-INTELLIGENCE-001.md`.
- Source Arena Hybrid renderer ADR — current local documentation task,
  PROPOSED status, pending review/integration; durable report at
  `docs/tasks/MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-001.md`.

## Standing Safety Gate

No push, PR, merge, force operation, rebase, squash, branch deletion, tag,
release, deploy, workflow mutation, trading behavior, credential storage, or
retired-remote contact without explicit operator authorization.
