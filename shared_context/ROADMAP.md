# Roadmap

## 7-Day Setup

- Confirm cross-agent context works across Codex, Claude, ChatGPT, GLM, Grok, Warp, Zed, VS Code, and GitHub.
- Prepare GitHub remote setup.
- Package context files for ChatGPT Project upload.
- Draft provider routing matrix for OmniRouter.

## 30-Day Prototype

- Build a non-runtime website prototype.
- Define design tokens and 3D visual direction.
- Create agent workflows for docs, review, and validation.

## 90-Day Public Showcase

- Publish a polished public showcase website.
- Document model routing, agent roles, and roadmap.
- Prepare reviewable architecture materials.

## 180-Day Modular AIOS Platform Vision

- Evolve toward a modular AIOS platform with provider routing, agent context, validation gates, and documented extension points.

## Milestone Tracks

Public-project facts (below) reflect only what has actually shipped in this repository. Future plans are marked pending or next; nothing here should be read as implemented until its status says so.

### Milestone A — Operational Trust

- Loop Operations Foundation (registry, contracts, read-only CLI, circuit breaker, canonical skills): **completed**.
- First external `project-health` dry run (`EXERCISED_EXTERNALLY_NOT_REGISTERED`): **completed**.
- Persistence review (safe evidence-persistence contract + token-semantics correction, docs-only): **completed**.
- History reconciliation (`MELLYCORE-PROJECT-HISTORY-AND-LOCALHOST-BOOT-001` — `PROJECT_STATE`/`ROADMAP` sync, localhost boot verification): **completed**.
- Persistence/token-contract implementation (`MELLYCORE-LOOP-PERSISTENCE-AND-TOKEN-CONTRACT-IMPLEMENTATION-001` — corrected token semantics, `persist-run` CLI, audit D4 closure, 150 passing tests): **completed**.
- Registered project-health run (`MELLYCORE-PROJECT-HEALTH-REGISTERED-RUN-001` — one real, honestly-derived run persisted for `project-health` via `persist-run --apply`; `audit` now reports `exercised: 1`, `production_enabled: 0`): **completed**.
- Live dashboard preview (`MELLYCORE-AIOS-LIVE-DASHBOARD-PREVIEW-001` — local, interactive `site/dashboard.html` reading real shared_context/loop files live at load, with a frozen CLI-output snapshot and clearly labeled mock data; no provider calls, no write actions): **completed**.
- Weekly L1 pilot (`MELLYCORE-L1-WEEKLY-PILOT-001` — a second real `project-health` run persisted additively via `persist-run --apply`; first run's evidence stays byte-unchanged; dashboard discovers the new run with no code change): **completed**.

**Milestone A status: closed.** Reviewed and confirmed coherent by `MELLYCORE-OPERATIONAL-TRUST-REVIEW-001` (git state, evidence/state consistency, dashboard discovery, and all validators/tests re-checked). No scheduler exists yet — every run above was a separate, explicit, human-invoked action, and remains so until a separate, explicitly approved task adds one.

### Milestone B — One Brain

Recommended first task: a docs-only provenance-and-sensitivity-tagging spec (see `docs/tasks/MELLYCORE-OPERATIONAL-TRUST-REVIEW-001.md` for the full rationale). No ingestion, database, MCP, or runtime implementation is authorized by this note; a spec must exist and be reviewed before any code change, matching this project's established docs-first pattern.

- Provenance and sensitivity tagging for ingested context: **pending** — recommended next.
- Ingestion gate (validation before context is trusted): **pending**.
- Contradiction/freshness handling across shared context files: **pending**.
- Context Pack Generator: **pending**.
- Living Context Graph integration (beyond the current static preview section): **pending**.

### Milestone C — Skill Intelligence

- Skill registry: **pending**.
- Usage evidence collection: **pending**.
- ROI estimation: **pending**.
- Skill Discovery Loop: **pending**.
- Evaluation and approval workflow: **pending**.

### Milestone D — Model Intelligence

- Capability registry: **pending**.
- Cost/safety policy: **pending**.
- Deterministic route simulation: **pending**.
- Maker/checker routing: **pending**.
- Optional council pilot: **pending**.

### Milestone E — Reflection and Voice

- Morning Insight Report: **pending**.
- Report-only scheduler (later; no autonomous actions): **pending**.
- Voice Inbox (later): **pending**.
- No autonomous actions are authorized at any point in this milestone without explicit, separate operator approval.

