# Project History

Canonical, chronological ledger of MellyCore AIOS milestones. This is a summary
index only — durable per-task evidence remains in `docs/tasks/`, `docs/research/`,
`docs/decisions/`, and Git history, none of which this file duplicates or
supersedes. Where this file and a durable report disagree, the durable report
and Git history win.

Naming a milestone here does not, by itself, claim implementation. Each entry
states its actual status (`SPECIFIED`, `IMPLEMENTED`, `ACCEPTED`, `MERGED`,
`RETIRED`) as recorded in the linked evidence.

## Genesis

- **2026-07-06** — Project scaffold bootstrapped. `AGENTS.md`, `CLAUDE.md`,
  `PROJECT_RULES.md`, and the `shared_context/` contract set created. MellyCore
  AIOS established as separate from MellyTrade, docs-first, no runtime app code
  until explicitly authorized.
- **2026-07-06** — MellyCore Design System and Homepage specification added.

## Foundational Phase

- Static homepage and Living Context Graph prototype shipped; historical
  evidence under `docs/tasks/` and `docs/showcase/`.
- **Operational Trust / Loop Operations** — closed as report-only: immutable
  run evidence, no scheduler, no production-enabled loop. Architecture under
  `docs/architecture/`.
- **One Brain / Context Gate I1–I4** — implemented: guarded admission,
  canonical write-once records, content-free index, computed audit, read-only
  dashboard surface. Canonical evidence under `shared_context/context_provenance/`.
- **Live Cockpit V2 / `v0.2.0`** — historical release; superseded legacy
  dashboard prototype, not the complete Observatory.
- **Holographic UI specification / PR #4** — accepted as documentation only.
  Source Arena hero contract preserved; 3D/WebGL treatment not implemented at
  this point.
- **Positioning refresh** — integrated into canonical `main`; durable report
  `docs/tasks/MELLYCORE-POSITIONING-REFRESH-001.md`.

## AI Operations Intelligence and Data Contract

- **AI Operations Intelligence specification** (`MELLYCORE-AI-OPERATIONS-INTELLIGENCE-001`)
  — integrated into canonical `main` via PR #7. Logical contracts and
  truth/safety boundaries only; modules remain `SPECIFIED`, no runtime
  adapters or approval execution claimed.
- **Operations Data Contract** (`MELLYCORE-OPERATIONS-DATA-CONTRACT-001`) —
  integrated into canonical `main` via PR #13 (merge commit
  `e0db28f06613d29028df96a2d651b6dfdf2f2aa8`). Fourteen dashboard-facing
  fixture entities and their `shared_context/operations/` schemas landed as
  documentation/schema/fixture scope, not runtime implementation. Branch
  reconciliation and AI-Estate/Skill-Gap/Memory-Freshness folding recorded in
  `docs/tasks/MELLYCORE-OPERATIONS-DATA-CONTRACT-POST-MERGE-STATE-SYNC-001.md`.

## Source Arena Renderer Track

- **Source Arena Hybrid renderer ADR** — status `ACCEPTED_CANONICAL_MAIN`
  (decision/specification level only); merged into canonical `main` via PR #8,
  merge commit `f93be7018a1da3bba50eb66346b1f9e627a46dd2`, 2026-07-20. Full
  review chain (review 001 `NEEDS_FIXES` → remediation 001 → review 002
  `NEEDS_FIXES` → remediation 002 → review 003 `PASS` → operator acceptance →
  acceptance review 001 `NEEDS_FIXES` → acceptance remediation 001 →
  acceptance review 002 `PASS` → PR #8 merged) recorded under `docs/tasks/`.
  No Three.js implementation, dependency vendoring, or deployment exists at
  this milestone.
- **Post-merge state sync / P2 remediation chain** — PR #11 merged into
  canonical `main` via merge commit `cad4e07f73f80c5794f9af2897fc10d922637ab3`.
- **NASA Images runtime retirement**
  (`MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001`) — executable runtime
  retired from `site/dashboard.html` / `site/js/dashboard.js`; merged via PR
  #15 (merge commit `e0cbc332ff90f8787d981c9d86be717633f22d4d`), replaced with a
  local deterministic Source Archive.
- **Static CSS/DOM renderer slice** — canonical on `main` via PR #17 (merge
  commit `537a84c8`): source core, orbital nodes, orbit ring, command
  inspector. Replaced the prior social-feed primary UX. Full 3D/WebGL renderer
  and the ADR's CSS-complete fallback remain **not complete**.

## Enterprise Provider and Cloudflare Track

- Enterprise Provider Integration architectural research recorded — not
  implemented; see `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md`
  and `shared_context/PROJECT_STATE.md`'s corresponding section.
- **Cloudflare API Shield read-only adapter 001** — local implementation
  complete → review 001 `FAIL_REMEDIATION_REQUIRED` → remediation 001 →
  review 002 `PASS_WITH_NON_BLOCKING_FINDINGS`. Provider-foundation checkpoint
  complete; not live-provider readiness. `P2-03`, `P2-04`, `P3-01` carried
  forward as constraints on later provider and Agent Runtime work.

## Deploy Path and Production Authorization

- **Option B Deploy Path — Static AIOS Showcase + OpenRouter Observatory** —
  historical deploy path, completed; see `shared_context/RUN_QUEUE.md`'s
  "Historical Option B Deploy Path" section.
- **Vercel Static Root** — accepted, verified, published, state-synced, merged.
- **Production Deployment Authorization — Model A Contract** (Operator
  decision, 2026-07-27, temporary, static-phase-only) — recorded in
  `shared_context/PROJECT_STATE.md`. Nine canonical, blocking migration
  triggers require Model B reconsideration before crossing.
- **OpenAI Batch Controlled Activation** — Stage B merged; Stage C
  unauthorized; final canonical state reconciliation gate is the current
  global higher-priority pointer in `shared_context/RUN_QUEUE.md`.

## Agent Runtime Product Track

1. `MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001` — architecture specified
   across 43 sections and 6 frameworks; complete as one local documentation
   commit, not pushed. Nothing implemented, connected, or executed.
2. `MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-001` — gate
   `FAIL_REMEDIATION_REQUIRED` (P0 0 / P1 4 / P2 5 / P3 5).
3. `MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REMEDIATION-001` — all fourteen
   findings remediated; two owner documents (Control Plane, AI Operations
   Intelligence) amended additively; remediation claims unverified pending
   review.
4. `MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-002` — gate
   `PASS_WITH_NON_BLOCKING_FINDINGS` (P0 0 / P1 0 / P2 0 / P3 1 new,
   `NEW-P3-01`). Architecture accepted as canonical foundation for this track.
5. `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001` — **current active task**
   (started this entry; see `shared_context/AGENT_HANDOFF.md`'s Latest
   Update). Documentation-only: records the Developer Platform and Agent
   Package Ecosystem planning direction across `shared_context/ROADMAP.md`,
   `RUN_QUEUE.md`, `PROJECT_STATE.md`, this file, and `TASK_INDEX.md`.
   Nothing implemented; no registry, validator, CLI command, plugin loader,
   or MCP integration exists. Full detail: `shared_context/ROADMAP.md`'s
   "Developer Platform & Agent Package Ecosystem" section.

## How to Extend This File

Append new entries under the relevant phase heading (or a new heading for a
new track) as milestones complete, in the same style: what happened, its
actual status, and a pointer to the durable evidence. Do not backfill claims
this file cannot verify against `docs/tasks/`, `docs/research/`, or Git
history.
