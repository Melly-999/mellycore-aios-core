# MellyCore AIOS — Command Center Cockpit Specification

**Canonical owner:** `MELLYCORE-COMMAND-CENTER-COCKPIT-SPEC-001`
**Established by:** `MELLYCORE-COCKPIT-V3-CANONICALIZATION-001`
**Version:** 1.0
**Status:** Complete specification; **no frontend implementation claimed or performed**
**Implementation foundation:** existing static HTML/CSS/JavaScript under `site/`
**Owned surface:** `site/dashboard.html` and its dedicated assets
(`site/css/dashboard.css`, `site/js/dashboard.js`, `site/data/*.json`)

---

## 1. Ownership and boundaries

This specification owns the **Command Center cockpit** — MellyCore's dense AI
operations workstation surface. It is the canonical behavioral owner for
`site/dashboard.html`, which previously had no spec owner.

Explicit non-overlap, to avoid competing specifications:

| Concern | Canonical owner | This spec's relationship |
|---|---|---|
| Homepage / commercial showcase | `docs/specs/MELLYCORE_HOMEPAGE_SPEC_001.md` | Does not modify. The homepage remains product-led and is not a runtime console. |
| Homepage `command-center-preview` section | `docs/specs/MELLYCORE_UI_SECTIONS.md` | That section stays a **preview**. This spec owns the full surface it previews. |
| Knowledge graph data model, node/edge semantics, safety overlay | `docs/product/knowledge_graph_console_spec.md` (`MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001`) | **Reused, not duplicated.** Section 5 below defers all graph data semantics to that spec. |
| Graph visual language | `docs/design/knowledge_graph_visual_language.md` | Reused. |
| Source Arena holographic hero | `docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md` | Unaffected. See `shared_context/DESIGN_SYSTEM.md` §"Surface ownership". |
| Global design tokens and colour direction | `shared_context/DESIGN_SYSTEM.md` | Subordinate. Where this spec and the Design System conflict, the Design System wins. |

If wording here conflicts with `shared_context/DESIGN_SYSTEM.md` or
`shared_context/SAFETY_CONTRACT.md`, those files win.

## 2. Purpose and identity

The cockpit must read as **a sophisticated operator-controlled AI operating
system workstation**.

It must **not** read as a marketing landing page, a generic SaaS admin
dashboard, a trading terminal, a game HUD, or a default component-library
admin template.

Primary visual targets: **1920×1080** and **1600×900**.

The cockpit's job is to make MellyCore's *architecture and coordination state*
legible at a glance — not to imply that a runtime is executing.

## 3. Accepted visual direction

The accepted direction is **MellyCore Cockpit V3.1**, an Operator-selected
design input recorded by `MELLYCORE-COCKPIT-V3-CANONICALIZATION-001`.

**This specification — not the V3.1 artifact — is the durable canonical source
of truth for implementation.** The V3.1 standalone HTML is a bundled design
artifact held outside version control. It may be consulted for composition and
density, but its bundled runtime, generated component architecture, and
artifact-host glue must never be copied into `site/`.

Defining characteristics:

- dense AI operations workstation, high information density;
- a dominant central Knowledge & Operations Graph;
- compact technical instrumentation in both side columns;
- a supervised, seven-stage AI Operations Workflow;
- compact technical primary navigation;
- near-black technical canvas;
- restrained cyan / blue / violet / amber / green subsystem accents;
- truthful static / prototype state throughout.

## 4. Layout contract

| Property | Requirement |
|---|---|
| Shell | Three-column cockpit at ≥1440px: left instrumentation, central graph workspace, right instrumentation. Command bar above; workflow band below; navigation compact. |
| Graph share | Central graph workspace occupies approximately **56–62%** of main workspace width at desktop targets, and most of its height. |
| Cockpit gaps | approximately **8–12px** |
| Panel padding | approximately **12–16px** |
| Radii | small |
| Borders | 1px, restrained |
| Depth | subtle; restrained glow only |
| Viewport | No accidental empty region below the application shell. Main-page scrolling avoided at 1600×900 and 1920×1080 where practical; bounded internal panel scrolling is acceptable. |

Side columns stay compact. They must not be widened merely to eliminate all
internal scrolling; use compact row spacing, hierarchy, progressive disclosure,
and thin integrated scrollbars instead.

## 5. Required surfaces

All data below must be **repository-backed static content or clearly labelled
fixture/architecture content**. No surface may introduce a backend, a graph
database, live ingestion, a provider connection, or runtime execution.

### 5.1 Command Bar

Compact technical status regions rather than a row of unrelated pills. Required
semantics, using existing repository vocabulary:

- **SYSTEM MODE** — `STATIC PREVIEW · SUPERVISED`
- **EXECUTION** — `EXECUTION LOCKED · NO LIVE PROVIDERS`
- **CONTEXT** — repository/docs sync state

Current view state and frozen snapshot state must be visually distinct and must
never be conflated. Where a frozen snapshot is displayed, label its source
separately from the current view branch.

**Prohibited in the command bar and anywhere else on the surface:** uptime,
active requests, requests/min, tokens/min, error rate, cost/hour, live provider
traffic, success rate, and active-agent percentages. See §7.

### 5.2 Context Management

Compact instrumentation over MellyCore's own context corpus. Permitted sources:
`shared_context/context_graph_fixture_001.json`,
`shared_context/CONTEXT_GRAPH_SCHEMA.md`,
`site/data/context_audit_snapshot.json`.

Entity counts must be labelled as fixture/snapshot-derived, never as live
counts.

### 5.3 Model Routing

Projects `shared_context/MODEL_ROUTING.md`, which describes **routing roles for
agents and tools** (strategy, implementation, review, critique, gateway) — not
provider traffic.

Must present routing as *configured intent*. Must not present request
distribution percentages, per-model traffic shares, latency, or cost as current
measured state.

### 5.4 Knowledge & Operations Graph

The visual acceptance centrepiece and dominant element.

- **MellyCore Core must be immediately identifiable and visually dominant.**
- Clusters must be readable and drawn only from repository-supported concepts:
  Shared Context, Core Services, Models / AI lanes, Tools, Governance,
  Products / Surfaces.
- Relationship hierarchy must be visible through edge opacity/weight.
- Labels must remain readable at normal screenshot scale, without clipping.
- Must avoid generic mind-map aesthetics.

**Data model, node/edge semantics, provenance, contradiction handling, and the
safety overlay are owned by `docs/product/knowledge_graph_console_spec.md` and
must be reused, not redefined here.**

Topology must be disclosed as derived from the repository and not from a live
runtime. No live ingestion. No graph database. No invented integrations added
merely to fill the canvas.

Permitted interactions, only where they fit the existing static architecture:
node hover/focus, selected node, relationship emphasis, basic layer/filter
control, fit/center, inspector reveal. Force simulation, physics, backend
persistence, and realtime activity are **not** permitted and **not** required.
The graph must remain excellent as a static screenshot.

### 5.5 AI Agents / Loop Registry

Compact registry of MellyCore's defined agent/loop roles, drawn from
`shared_context/` and `docs/`.

Each row must communicate a **defined or planned** state. Rows must not claim
`Running`, `Idle`, `Active`, or a completion percentage unless backed by actual
recorded runtime evidence. Where a role is planned, label it planned.

### 5.6 Architecture Snapshot

Frozen architectural/observability posture derived from repository documents.

Must carry explicit `FROZEN · NOT LIVE` disclosure and identify its snapshot
source. Must not present latency, success rate, throughput, or cost as current.

### 5.7 Attention Queue

Compact list of outstanding governance items — open gates, pending reviews,
recorded contradictions, blocked tasks — sourced from
`shared_context/TASK_INDEX.md`, `shared_context/RUN_QUEUE.md`, and
`shared_context/CONTRADICTION_LEDGER.md`.

Severity must be communicated by text plus colour, never colour alone. Red is
reserved for genuinely critical items.

### 5.8 AI Operations Workflow

A seven-stage band with strong secondary visual presence:

1. Context Ingestion
2. Intent & Routing
3. Tool Orchestration
4. Approval & Guardrails
5. **Execution**
6. Validation
7. Audit Trail

**Stage 5 (Execution) must be visually and semantically constrained** and must
carry an explicit locked/unavailable treatment for as long as canonical runtime
execution is not enabled. The band must never imply that an unauthorised live
execution path exists.

### 5.9 Primary Navigation

Compact technical navigation, visually secondary to the cockpit. Dashboard's
active state must be obvious.

Destinations may be named (Dashboard, Operations, Agents, Models, Tools,
Context, Policies, Audit), but **this specification does not authorize
implementing any secondary destination page.** Unbuilt destinations must be
presented honestly rather than linking to a broken or fabricated surface.

## 6. Responsive behaviour

| Range | Requirement |
|---|---|
| ≥1440px | Full three-column cockpit. |
| ~1024–1439px | Central graph dominance preserved. Side panels may narrow, collapse, or become drawers if the existing architecture supports it. |
| Tablet | Graph becomes primary; secondary instrumentation may stack into panels/drawers. |
| Mobile (390×844) | **Do not shrink the desktop cockpit until unreadable.** Provide an intentional compact overview prioritising system state, graph summary / selected topology, context, agent state, and navigation. Desktop visual fidelity is *not* required at mobile; usability is. |

Validation widths: 1920×1080, 1600×900, 1440×900, 1280×800, 1024×768, 390×844.
Each must be free of horizontal overflow, panel clipping, graph clipping,
header collision, and unreadable microtext.

## 7. Truthfulness rules (binding)

The cockpit must preserve these distinctions at all times:

visual presence ≠ implementation · planned ≠ implemented · implemented ≠ tested ·
tested ≠ connected · connected ≠ authorized · static preview ≠ live telemetry ·
configured ≠ exercised · defined ≠ running ·
architecture topology ≠ active runtime topology

**Prohibited unless backed by actual recorded runtime evidence:** `LIVE`,
`RUNNING`, `OPERATIONAL`, `HEALTHY`, `ACTIVE REQUESTS`, `REQUESTS/MIN`,
`TOKENS/MIN`, `COST/HOUR`, `ERROR RATE`, `SUCCESS RATE`, uptime percentages,
per-agent activity percentages, and provider traffic figures.

**Approved truthful vocabulary** — reuse the existing repository terms; do not
mint a new global state taxonomy:

`STATIC PREVIEW` · `SUPERVISED` · `EXECUTION LOCKED` · `NO LIVE PROVIDERS` ·
`FROZEN · NOT LIVE` · `TOPOLOGY DERIVED FROM REPOSITORY · NOT LIVE RUNTIME` ·
`ARCHITECTURE` · `PLANNED` · `SIMULATED` · `FIXTURE` · `SNAPSHOT`

Fixture, snapshot, simulated, and planned content must be labelled **at point
of use**, not only in a global footnote.

A visually rich cockpit must never be turned into a fake production dashboard.

## 8. Accessibility expectations

Required, preserving or improving current behaviour:

- semantic landmarks and correct heading hierarchy;
- critical content present in semantic HTML and visible without JavaScript;
- full keyboard navigation with visible focus, including graph controls,
  panel controls, and any inspector/drawer;
- state communicated by text plus colour, never colour alone;
- minimum readable type; no unreadable microtext;
- appropriate touch targets at mobile;
- `prefers-reduced-motion` respected — no content may be removed and no
  interaction may become unusable under reduced motion;
- **the graph must not be the only representation of important architecture or
  state.** An accessible textual/structured equivalent is required.

No WCAG conformance may be claimed unless formally validated.

## 9. Motion

Motion is secondary; the cockpit must look complete without animation.

Permitted: 100–180ms hover/focus transitions, graph relationship emphasis,
small inspector transitions, subtle active-state transitions.

Forbidden: pulsing "live" indicators, fake streaming, moving particles implying
traffic, continuously flowing graph edges, excessive parallax, and breathing
glows that imply active runtime state.

Critical content must never depend on an animation completing.

## 10. Static implementation constraints

- Preserve the existing static HTML/CSS/vanilla-JS architecture under `site/`.
  **No framework migration.** No React/Next/Vite introduced because the design
  artifact used them.
- Prefer deterministic **SVG/CSS** rendering. Do not add Three.js, WebGL,
  canvas engines, heavyweight graph packages, or animation frameworks if
  HTML/SVG/CSS suffices. Any proposed dependency must be justified explicitly.
- No backend, no API, no database, no live ingestion.
- No provider integration, no model calls from the product, no MCP execution,
  no runtime activation.
- No secrets, API keys, provider tokens, `.env` values, or runtime state.
- Do not copy the bundled V3.1 artifact, its bundler runtime, or its generated
  component architecture into `site/`.
- Typography must use the repository's approved strategy. **No remote font
  dependency** may be introduced. Where exact artifact font metrics cannot be
  matched safely, prioritise readability and layout fidelity over font
  imitation.
- Reuse existing tokens, primitives, and components where suitable rather than
  duplicating them.

## 11. Implementation posture

This specification defines the target. It does **not** implement it, and it
does **not** authorize merging or deploying it.

Implementation is owned by `MELLYCORE-COCKPIT-V3-IMPLEMENTATION-001`.
Independent acceptance is owned by
`MELLYCORE-COCKPIT-V3-IMPLEMENTATION-ACCEPTANCE-001`.
