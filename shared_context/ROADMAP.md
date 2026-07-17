# Roadmap

## Operator Commands

`/roadmap`: Show current MellyCore AIOS roadmap, milestone completion, task counts, current release, branch state, next recommended task, model/effort recommendation, and safety reminders. This is the standard operator command for a full project-status read — docs-only, no CLI/dashboard implementation, answered by reading this file plus `shared_context/AGENT_HANDOFF.md`, `shared_context/RUN_QUEUE.md`, `shared_context/PROJECT_STATE.md`, `shared_context/MODEL_ROUTING.md`, and `shared_context/SAFETY_CONTRACT.md`. Full field-by-field definition: `docs/runbooks/MELLYCORE_ROADMAP_COMMAND.md`. Added by `MELLYCORE-ROADMAP-COMMAND-001`, superseding the informal one-off `/status-aios` heading previously used in a single task report; that heading was never a registered command and is not kept as an alias.

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

- Provenance and sensitivity tagging for ingested context (`MELLYCORE-CONTEXT-PROVENANCE-AND-SENSITIVITY-SPEC-001` — docs-only spec: the `ContextSource` record shape, provenance/sensitivity/trust labels, an `allowed_use` matrix, staleness policy, contradiction precedence guidance, an admission workflow extending `SOURCE_INGEST_WORKFLOW.md`, and future dashboard fields): **completed (spec only)**.
- Ingestion gate (validation before context is trusted) (`MELLYCORE-CONTEXT-INGESTION-GATE-SPEC-001` — docs-only spec: admissible inputs, required metadata, nine refusal rules, five validation outcomes with `ACCEPT` never meaning admitted, human-review parking conditions, stale-claim detection, contradiction routing to the ledger, write-once recording conventions, no-write preview mode with future operator-gated apply, and future implementation boundaries): **completed (spec only)**. The later hand dry run, admissions, implementation spec, and read-only I1 implementation are tracked below; see `docs/tasks/MELLYCORE-CONTEXT-INGESTION-GATE-SPEC-001.md`.
- Contradiction/freshness handling across shared context files: **pending** — precedence guidance specified above; the ledger and workflow already exist (`CONTRADICTION_LEDGER.md`, `SOURCE_INGEST_WORKFLOW.md`), no live entries yet.
- Context Pack Generator: **pending** — spec exists (`CONTEXT_PACK_GENERATOR_SPEC.md`), no implementation.
- Living Context Graph integration (beyond the current static preview section): **pending**.

- Ingestion gate dry run (`MELLYCORE-CONTEXT-INGESTION-GATE-DRY-RUN-001` — hand-exercised the gate in preview semantics on an 8-item batch of committed repo facts: 5 ACCEPT, 1 ACCEPT_WITH_WARNINGS, 1 REFUSE via the generated-content trust cap, 1 NEEDS_HUMAN_REVIEW for private sensitivity, 0 contradictions; 6 draft `ContextSource` records created under `shared_context/context_provenance_preview/`, all pending human Step 7 review): **completed (preview only — nothing admitted)**. See `docs/tasks/MELLYCORE-CONTEXT-INGESTION-GATE-DRY-RUN-001.md`.

- First admissions (`MELLYCORE-CONTEXT-FIRST-ADMISSION-REVIEW-001` — operator-delegated Step 7 review of the dry-run batch: all 6 drafts admitted, 1 with the gate warning acknowledged and a documented verification/trust upgrade; 0 rejected; the private repo-path item remains blocked on an operator question; records decided in place in the preview directory, now write-once immutable; canonical `context_provenance/` home deliberately not created — reserved for the implementation task): **completed**. See `docs/tasks/MELLYCORE-CONTEXT-FIRST-ADMISSION-REVIEW-001.md`.

- Gate implementation spec (`MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-SPEC-001` — docs-only: canonical `shared_context/context_provenance/` layout with write-once records and envelope/content split, hash-verified migration plan for the six admitted preview records, structurally aggregate-safe append-only refusal log, five CLI commands (`preview` default/non-writing, `validate-record`, `apply` gated on operator approval + expected HEAD with all checks re-run at write time, `rebuild-index`, `audit`), blocked-item lifecycle for the open C8 question, full test plan, dashboard-read contract, and four separately-approved implementation phases I1–I4): **completed (spec only)** — see `docs/tasks/MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-SPEC-001.md`.

- Context Gate implementation Phase I1 (`MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I1-001` — Python 3.9/stdlib `ContextSource` models, `validate-record`, no-write `preview`, full R1-R9 checks, deterministic aggregate-safe output, warnings/parking/staleness/contradiction handling, 50 focused tests): **completed (read-only implementation)**. No apply/store/migration/refusal-log/index/audit/dashboard code exists; see `docs/tasks/MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I1-001.md`.

- Context Gate implementation Phase I2 (`MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I2-001` — guarded `apply`, write-once canonical store, aggregate-safe refusal log, apply-time R1-R9 rechecks, verified migration of the six admissions, C7 backfill, preview tombstone, and durable C8 rejection): **completed**. See `docs/tasks/MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I2-001.md`.

- Context Gate implementation Phase I3 (`MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I3-001` — deterministic content-free `rebuild-index`, canonical-record validation, computed read-only `audit --json`, freshness/supersession/refusal/index-drift findings, and 95 focused tests): **completed**. The shipped audit is clean: 7 valid records, zero stale, one expiring, one aggregate-safe refusal, zero blocked, zero findings. See `docs/tasks/MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I3-001.md`.

- Context Gate dashboard Phase I4 / Live Cockpit V2 (`MELLYCORE-LIVE-COCKPIT-V2-001` — cinematic mobile-first `site/dashboard.html`, safe Context tab consuming the content-free index plus a clearly dated aggregate audit snapshot, keyless browser-side NASA Images API search/asset manifests, and an explicitly simulated Fable 5/Opus/GPT/GLM comparison feed): **completed locally, committed, not pushed or deployed**. The Context tab never opens canonical record bodies or the refusal log; NASA is the only external data request and requires no API key. See `docs/tasks/MELLYCORE-LIVE-COCKPIT-V2-001.md`.

- Live Cockpit V2 social realignment (`MELLYCORE-LIVE-COCKPIT-V2-SOCIAL-REALIGN-001` — TikTok/Hyperagent-pattern vertical source cockpit with a deeper black/violet identity, magenta interaction highlights, a right-side social action rail with clearly labeled demo counts, a top "Find related sources" bar with planned-provider chips, a bottom caption/hashtag block, en-US/ISO-pinned formatting, clamped Roadmap/RUN_QUEUE rendering, and mobile scroll-fade affordances): **completed**. NASA is repositioned as one demo provider ("Demo provider: NASA Images API") proving real external-source ingestion inside the renamed External Data Arena; Apollo/Mars/etc. are demo presets; model text remains explicitly simulated lenses over one real source. See `docs/tasks/MELLYCORE-LIVE-COCKPIT-V2-SOCIAL-REALIGN-001.md`.

**Live Cockpit V2 / Social Source Arena: released as `v0.2.0`.** PR #2 (`integrate/live-cockpit-v2` → `clean-origin/main`) merged via a normal merge commit at `09db8a7`, tagged and published as `v0.2.0` (not a pre-release): <https://github.com/Melly-999/mellycore-aios-core/releases/tag/v0.2.0>. This is a static/docs-first release; no hosted deployment is claimed. Beyond NASA Images API (the current real, keyless demo provider), all other listed source types (GitHub repositories, PDFs/docs, websites, changelogs, issues, CVs/job offers, research, marketplace/e-commerce data, local project files) remain **planned, not implemented**.

- GitHub Repository provider demo (`MELLYCORE-GITHUB-SOURCE-PROVIDER-DEMO-001`, post-`v0.2.0`, site/docs/shared_context only): added a **planned/demo** GitHub Repository provider preview card to External Data Arena — an expandable, collapsed-by-default panel naming the example source `liquidslr/system-design-notes` (link only), 26 original short topic-title labels (no chapter content reproduced), and six planned model-lens use cases (architecture summary, bottleneck detection, tradeoff extraction, scaling risk review, implementation task generation, provenance-aware source comparison): **completed**. Product story clarified in visible copy: NASA remains the current real no-key media API demo provider proving live ingestion works today; GitHub Repository is the next MellyCore-aligned planned/demo provider, positioned for architecture intelligence and system design review; all other source types stay explicitly planned, not implemented. No live GitHub fetch, backend, API key, or dependency was added — this is a pure HTML/CSS product-positioning card using the native `<details>` disclosure element, no new JavaScript behavior. See `docs/tasks/MELLYCORE-GITHUB-SOURCE-PROVIDER-DEMO-001.md`.

The project's first six admitted `ContextSource` records remain immutable in `shared_context/context_provenance/records/`; C8 remains a seventh canonical record with `decision: rejected`. The four-phase Context Gate implementation sequence is now complete through its read-only dashboard surface. No backend, provider integration, database, scheduler, or dashboard write path was introduced.

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
