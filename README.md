# MellyCore AIOS

MellyCore AIOS is a static-first, docs-first demonstration of a Living Context Graph for structured context handoff between AI agents.

[Explore the static source](site/index.html) · [Open Live Cockpit V2](site/dashboard.html) · [Review the graph fixture](shared_context/context_graph_fixture_001.json) · [Open the canonical repository](https://github.com/Melly-999/mellycore-aios-core)

## Project Preview

The repository includes a responsive command-center showcase under [`site/`](site/). The HTML/CSS homepage presents the system concept, safety boundaries, shared-context model, and static Living Context Graph. [`site/dashboard.html`](site/dashboard.html) adds Live Cockpit V2: a local, read-only social source cockpit backed by repository snapshots plus a public, keyless NASA Images API demo. Neither surface is a deployed application or live AI runtime.

No screenshot binary is tracked in the repository. The reviewed viewport coverage and local evidence policy are documented in the [static preview evidence pack](docs/showcase/static_preview_evidence_pack_001.md) and [visual QA report](docs/tasks/MELLYCORE-KNOWLEDGE-GRAPH-STATIC-UI-VISUAL-QA-001.md).

## What It Demonstrates

- A hand-authored, reviewable context graph with **8 clusters, 45 nodes, and 66 edges**.
- A structured handoff concept for sharing project state, decisions, safety rules, evidence, and queued work between AI agents.
- A static Knowledge Graph Console presentation built with semantic HTML and CSS.
- Docs-first product architecture that keeps specifications, decisions, handoffs, and validation rules visible in source control.
- Safety-aware copy that distinguishes implemented static evidence from future concepts.
- Responsive visual QA documented across mobile, tablet, desktop, and wide desktop viewports from **375px to 1920px**.
- An Obsidian-inspired spatial graph visual direction documented for future static exploration, not presented as a current Obsidian integration or 3D runtime.
- A report-only Loop Operations Foundation with immutable run evidence, deterministic safety guards, and no production-enabled loops.
- A standard-library Context Gate with guarded admission, a content-free index, and a read-only audit surface.
- Live Cockpit V2 with a provenance-safe Context tab, one real external demo source, and model comparison copy explicitly labeled as simulated.

## Living Context Graph

Fixture 001 is stored in [`shared_context/context_graph_fixture_001.json`](shared_context/context_graph_fixture_001.json). It models repository-backed context as clusters, nodes, and evidence-linked edges. Each node carries a reviewed summary and source references; each edge records the relationship and its evidence references.

The fixture is a static snapshot authored from repository documentation. It is not generated from telemetry, a database, an external service, or live agent activity. The companion [fixture documentation](shared_context/CONTEXT_GRAPH_FIXTURE_001.md) explains its scope, review rules, schema mapping, and safety boundaries.

## Architecture And Data Flow

```text
Repository documentation and shared context
                    |
                    v
      Hand-authored JSON graph fixture
                    |
                    v
       Static HTML/CSS visualization

Project validator --------> repository structure and safety checks
Agent handoff docs --------> conceptual multi-agent coordination
Content-free index -------> read-only dashboard Context tab
Public NASA Images API ---> browser-side GET-only demo source
```

The layers are intentionally separate:

- **Static project fixture:** reviewed JSON data representing the current repository context.
- **Context graph model:** documented node, edge, cluster, source, and safety-display conventions.
- **Visualization layer:** the homepage is local HTML/CSS; Live Cockpit V2 adds dependency-free vanilla JavaScript for read-only local data rendering and public NASA API GET requests.
- **Validation layer:** a repository-specific Python script checks required files, safety-sensitive patterns, and core documentation contracts.
- **Conceptual handoff:** `AGENT_HANDOFF.md` and `RUN_QUEUE.md` show how agents can exchange reviewed context through files and Git history.

## Safety And Scope Boundaries

MellyCore AIOS currently provides a static project fixture, documentation, and local showcase. It does **not** provide:

- durable context ingestion or automatic graph refresh;
- a production AI-agent runtime or autonomous agent execution;
- backend services, authenticated provider connections, or databases;
- authentication, telemetry, workflow deployment, or hosted application infrastructure;
- Obsidian, MCP, or real-time synchronization;
- secrets, provider tokens, account identifiers, or committed runtime state.

The only implemented external data path is a browser-side, keyless, GET-only NASA Images API demo. Planned source types are labeled as planned, and model outputs are deterministic local simulations rather than provider responses.

MellyCore AIOS is separate from MellyTrade and contains no trading, broker, order, or execution functionality.

## Tech Stack

- **Interface:** HTML5, CSS3, and vanilla JavaScript
- **Fixture:** JSON
- **Documentation:** Markdown
- **Validation:** Python
- **Source control and review:** Git and GitHub

React, TypeScript, FastAPI, provider SDKs, and database libraries are not dependencies of this static repository.

## Local Setup

No package installation or build step is required.

1. Clone the canonical repository.
2. Open [`site/index.html`](site/index.html) directly in a browser.
3. Open [`site/dashboard.html`](site/dashboard.html) for Live Cockpit V2.
4. Review the static graph, read-only cockpit states, and repository documentation.

For dashboard data loading, serve the repository through the verified localhost command in [`docs/runbooks/MELLYCORE_LOCALHOST_QUICKSTART.md`](docs/runbooks/MELLYCORE_LOCALHOST_QUICKSTART.md). Bind only to `127.0.0.1`. A localhost address is a local preview, not a public deployment.

## Validation

Run the project-specific validator from the repository root:

```powershell
py scripts\validate_project_state.py
```

The validator checks required project files, shared-context documents, agent guidance, editor/workflow examples, absence of a committed `.env`, focused secret patterns, and core design/routing documentation terms.

The graph fixture and static UI evidence can also be reviewed directly:

- [Fixture review report](docs/tasks/MELLYCORE-KNOWLEDGE-GRAPH-FIXTURE-REVIEW-001.md)
- [Static UI scaffold review](docs/tasks/MELLYCORE-KNOWLEDGE-GRAPH-STATIC-UI-SCAFFOLD-REVIEW-001.md)
- [Responsive visual QA](docs/tasks/MELLYCORE-KNOWLEDGE-GRAPH-STATIC-UI-VISUAL-QA-001.md)

## Repository Structure

```text
site/             Static homepage and vanilla-JS read-only cockpit
shared_context/   Fixture, project state, handoff, safety, and model docs
docs/             Product, design, architecture, evidence, and task reports
agent_prompts/    Repo-specific guidance for supported agent workflows
scripts/          Project validation utilities
tests/            Standard-library tests for loop and context-gate tooling
```

## Current Limitations

- The graph is a hand-authored fixture, not a live knowledge system.
- Live Cockpit V2 is a local read-only preview; NASA is one demo provider, and all model comparison output is simulated.
- Loop execution remains report-only and human-invoked; no scheduler or production-enabled loop exists.
- Graph interactions shown in specifications are conceptual unless present in the static HTML/CSS preview.
- The Obsidian-inspired 3D direction remains documentation for future static work.
- Screenshot and HAR evidence is intentionally stored outside the repository; tracked reports describe the reviewed viewport coverage.
- No public website deployment is configured by this repository.

## Author And Related Work

**Mateusz Ozimkiewicz**

Full-Stack Developer | React · TypeScript · FastAPI · AI Tools

- [GitHub profile](https://github.com/Melly-999)
- [Canonical MellyCore AIOS repository](https://github.com/Melly-999/mellycore-aios-core)
- [MellyTrade](https://github.com/Melly-999/alpha_data_scraper_ai) — a separate safety-first, read-only AI trading workstation project

<!-- PORTFOLIO_URL_PENDING -->
