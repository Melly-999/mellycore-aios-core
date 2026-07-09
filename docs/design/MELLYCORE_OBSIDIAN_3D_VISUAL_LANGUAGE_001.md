# MellyCore Obsidian-Style 3D Graph Visual Language 001

Task ID: `MELLYCORE-OBSIDIAN-3D-VISUAL-LANGUAGE-001`

Status: future-facing visual language specification only

## Purpose

This document defines the visual language for a future Obsidian-style 3D graph page for MellyCore AIOS. It is a docs-only design artifact for later static scaffold work.

The visual direction extends the current MellyCore static website, the completed `Living Context Graph` static UI milestone, and Fixture 001:

- Source fixture: `shared_context/context_graph_fixture_001.json`
- Fixture scale: 8 clusters, 45 nodes, 66 edges
- Current static surface: `site/index.html`
- Current graph language: `docs/design/knowledge_graph_visual_language.md`
- Future page spec: `docs/specs/MELLYCORE_OBSIDIAN_3D_PAGE_SPEC_001.md`

This document does not authorize frontend implementation, JavaScript, WebGL, Three.js, Obsidian integration, MCP integration, backend APIs, database storage, runtime ingestion, workflow YAML, deployment, or production publishing.

## Relationship To Current Work

The existing static `Living Context Graph` section is a reviewable, local, HTML/CSS-only preview of Fixture 001. The future 3D page should feel like a spatial evolution of that preview, not a separate product.

The relationship is:

- Current static preview: flat command-center graph mock for local showcase and evidence.
- Future 3D page: spatial context-navigation concept using the same fixture semantics and safety posture.
- Future scaffold: static-first representation of the concept before any interactive or runtime work is considered.

The future page must keep the current truth boundary: the graph is fixture-backed, reviewable, and explicitly not live unless a separate approved task changes that posture.

## Core Visual Metaphor

Primary metaphor: command-center star map.

The page should read as a mission-control view of MellyCore knowledge. Nodes are not decorative stars; they are structured knowledge objects with source, safety, task, and product meaning.

Supporting metaphors:

- Context constellation: related tasks, specs, sources, and safety rules form recognizable clusters.
- Safety-governed knowledge nebula: risk and contradiction signals appear as controlled warning fields, not alarms or trading prompts.
- Agent memory galaxy: prior work, handoff state, and future modules are visible as navigable context, but inactive unless implemented by later approved work.

The mood should be premium, cinematic, low-noise, and institutional. Avoid game-like space combat, crypto dashboards, retail trading screens, or novelty sci-fi.

## Color And Atmosphere

Use the existing MellyCore design-system vocabulary:

- Base atmosphere: `Void Black`, `Deep Space`, transparent glass panels, faint starfield texture.
- Primary graph energy: `Orbital Violet`, `Plasma Blue`, `Signal Cyan`.
- Secondary depth: `Nebula Purple`, dormant gray, low-opacity glass borders.
- Safety states: `Safe Status Green`, `Soft Warning Amber`, and muted red only for clear contradiction or blocker states.

Color must never be the only differentiator. Shape, line style, labels, icons, legend text, and panel placement must carry the same meaning.

### Node State Treatments

- Trusted/source-backed nodes: crisp rim, stable glow, visible source indicator, high text contrast.
- Future/planned nodes: ghosted opacity, dashed orbit, "future concept" or "planned" copy.
- Risk/safety nodes: shield or triangular geometry, warning halo, nearby safety rail reference.
- Unverified inspiration nodes: dim glass node, dotted outline, explicit "unverified inspiration" status.
- Contradiction/risk markers: amber bracket or split-ring marker, never a destructive or executable control.

## Node System

Node styling should preserve the current graph language while adding spatial depth.

| Node class | Shape | Density / weight | Glow / intensity | Label behavior | Confidence indication | Safe-to-display rule |
| --- | --- | --- | --- | --- | --- | --- |
| Core product node | Large hexagonal or rounded orbital hub | Highest structural weight | Violet-blue stable core glow | Persistent label on desktop, summarized on mobile | Source count and review status chip | OK when tied to fixture or approved docs |
| Task/report node | Rounded square with small document notch | Medium weight | Soft cyan rim | Label visible when selected or in list fallback | Task outcome chip | OK for committed docs and reports |
| Source/evidence node | Small circle with dotted source ring | Low to medium weight | Low cyan glow | Label shown in source drawer and fallback list | Source path or evidence type | OK only with local repo path or approved external summary |
| Safety rule node | Shield-outline or shield-inscribed hex | High safety priority | Green or amber halo depending on state | Always readable in safety rail/fallback | "active guardrail" or "future guardrail" chip | OK when it states prohibition or review status |
| Risk node | Triangle or split-ring warning marker | High attention, low quantity | Amber glow, restrained pulse only if motion allowed | Label visible near risk lane and inspector | Risk severity and verification state | OK only as risk disclosure, not an action prompt |
| Future module node | Thin-outline cube or ghosted square | Low active weight | Dim violet rim | Label can be compact | "future only" chip | OK when explicitly non-implemented |
| External inspiration node | Small glass prism or dotted circle | Low weight | Muted lavender, no premium glow | Label must include "inspiration" or "unverified" | Review-needed chip | OK only with no copied implementation claim |

Node size indicates structural role and review priority, not business importance, profitability, or operational readiness.

## Edge System

Edges must remain legible in both spatial and text fallback modes. Every relation shown visually needs a legend entry and a readable fallback row.

| Relation | Visual treatment | Direction | Reduced-motion behavior | Text fallback |
| --- | --- | --- | --- | --- |
| `depends_on` | Solid violet-blue line, medium weight | Arrow toward dependency | Static line with arrow marker | "A depends on B" |
| `defines` | Solid cyan line, light glow | From defining doc to defined concept | Static solid line | "A defines B" |
| `references` | Dashed cyan line | From referring item to referenced item | Static dashed line | "A references B" |
| `contradicts` | Double amber line or split-edge bracket | Bidirectional unless fixture says otherwise | Static amber double line | "A contradicts B" |
| `supersedes` | Solid line with tick marker | From newer item to older item | Static line with tick | "A supersedes B" |
| `produced_by` | Dotted lavender line | From artifact to producer | Static dotted line | "A was produced by B" |
| `validated_by` | Solid green-cyan line with check marker | From item to validator | Static line with check text | "A is validated by B" |
| `blocked_by` | Amber line with stop marker | From blocked item to blocker | Static amber line | "A is blocked by B" |
| `belongs_to` | Thin low-opacity cluster line | From node to cluster | Static low-opacity line | "A belongs to cluster B" |

Line glow should be subtle. Dense edge bundles should fade into grouped lanes rather than creating visual noise. Selected relations may brighten, but the graph must still be understandable without hover, animation, or selection.

## Cluster Visual System

The 8 Fixture 001 clusters should appear as spatial neighborhoods rather than equal decorative bubbles.

Guidance:

- Cluster shells should be faint glass or nebula fields, not hard cards.
- Cluster labels must be visible in desktop and available in the fallback list on every viewport.
- Safety and source/evidence clusters should be closer to the inspector and safety rail than purely future-module clusters.
- Future or planned clusters should be ghosted and explicitly marked as future-only.
- Contradiction or risk-heavy areas should use amber boundary markers, not red emergency styling.

Spatial priority:

1. Core product/context cluster near the central gravity point.
2. Safety and validation clusters near the right-side or lower safety rail.
3. Source/evidence cluster adjacent to the source drawer.
4. Task/report clusters in an orbital lane around the core.
5. Future module clusters in the rear or outer orbit with ghosted depth.

## 3D Spatial Composition

The future 3D page should use depth to communicate context hierarchy, not to hide information.

Desktop composition:

- Foreground: selected node, source drawer, safety rail, relation legend.
- Midground: primary cluster constellation and current task path.
- Background: future modules, historical context, low-priority source nodes, faint starfield.
- Central gravity point: the current MellyCore context graph or selected knowledge pack.
- Orbital lanes: task history, source references, validation path, future concepts.
- Safety boundary: visible guardrail lane or shield arc separating actionable-sounding future ideas from current static evidence.

Camera and framing:

- Default view should show the whole constellation with one selected representative node.
- Avoid extreme perspective distortion that makes labels unreadable.
- Keep panels anchored and stable while the graph can appear spatial.
- The first viewport should communicate "MellyCore Obsidian-style context graph" without requiring scroll or interaction.

## Motion Principles

Motion is future guidance only. It must not be required for comprehension.

Allowed future motion:

- Slow ambient drift for inactive spatial depth.
- Gentle selected-node focus transition.
- Relation highlight when a relation is selected.
- Subtle depth parallax when scrolling or resizing.

Disallowed motion:

- Fast spinning constellations.
- Aggressive particle bursts.
- Trading-ticker urgency.
- Motion that implies live ingestion, real-time sync, production operation, or autonomous execution.

Reduced-motion mode must freeze ambient movement, preserve the selected state, and expose all critical data in static text.

## Panel System

The future page should maintain a graph-plus-evidence layout, not a graph-only spectacle.

Required panels:

- Node inspector: selected node type, label, summary, fixture/source status, related nodes, safety notes.
- Source drawer: file paths, fixture references, evidence status, and non-live wording.
- Contradiction/risk lane: contradiction preview, blocked-by relations, unresolved review flags.
- Context-pack preview: selected pack summary, included clusters, source count, review status, static/export-ready copy.
- Safety rail: no secrets, no provider keys, no runtime backend, no deploy, no workflow YAML, no live trading UX.
- Timeline/session path: committed tasks, completed reports, and future task ladder.
- Future module cards: explicitly future-only, ghosted, and not represented as active integrations.

Panels should use glass surfaces and compact HUD labels from `MELLYCORE_DESIGN_SYSTEM_001.md`. Do not place cards inside cards. Keep repeated node or source items as small cards only when they represent individual items.

## Accessibility And Fallback

The page must not rely on 3D perception, color, hover, or motion.

Required fallback behavior:

- Non-3D list or table summary of clusters, nodes, and relation types.
- Screen-reader summary that states: "Static fixture-backed context graph: 8 clusters, 45 nodes, 66 edges."
- Keyboard-readable structure with semantic headings and focusable inspector/fallback regions.
- Text alternative for every selected visual node and relation.
- High contrast labels and minimum readable text sizes.
- Persistent relation legend.
- Reduced-motion mode with no loss of content.

Critical safety or source information must appear in text panels, not only inside the graph.

## Responsive Behavior

Mobile:

- Use a stacked constellation summary.
- Show fixture counts, safety posture, selected node, relation legend, and fallback list before decorative depth.
- Avoid tiny labels and unreadable pills.
- Graph may become a static poster-like map with text fallback directly below.

Tablet:

- Use a condensed cluster map with inspector below or beside the map depending on width.
- Keep safety rail and source drawer readable.
- Prioritize cluster labels and selected-node details over dense edge rendering.

Desktop:

- Show the full constellation, inspector, relation legend, source drawer, and safety rail in one coherent command-center view.
- Keep selected context visible without requiring hover.

Wide desktop:

- Expand spatial depth and orbital lanes.
- Do not stretch panels into low-density decorative areas.
- Keep the graph centered and evidence panels close enough for scanning.

## Honest Copy And Status Rules

Allowed copy:

- "Obsidian-style 3D graph concept"
- "Static fixture-backed visual language"
- "Future static scaffold direction"
- "No live ingestion"
- "No runtime backend"
- "No Obsidian or MCP integration"
- "No provider keys"
- "No deployment configured"

Forbidden copy unless separately implemented and approved:

- "Live graph"
- "Production graph"
- "Real-time Obsidian sync"
- "MCP connected"
- "Three.js implementation complete"
- "WebGL implementation complete"
- "Provider-connected"
- "Autonomous memory ingestion"
- "Live URL"

The design must not include buy, sell, broker, order, execute, or live trading UX.

## Future Implementation Guardrails

Any future implementation task must remain static-first unless separately approved.

Guardrails:

- No provider keys or secrets.
- No `.env` changes.
- No backend/API/database/runtime ingestion without a separate approved task.
- No Obsidian vault reads without a separate approved task.
- No MCP integration without a separate approved task.
- No workflow YAML without a separate approved task.
- No deploy or GitHub Pages enablement without a separate approved task.
- No JavaScript, WebGL, or Three.js in this visual-language task.
- No claim that the graph is live, synced, deployed, production, or provider-connected.

## Future Task Ladder

Recommended next steps:

1. `MELLYCORE-OBSIDIAN-3D-VISUAL-LANGUAGE-REVIEW-001`
2. `MELLYCORE-OBSIDIAN-3D-STATIC-SCAFFOLD-001`
3. `MELLYCORE-OBSIDIAN-3D-STATIC-SCAFFOLD-REVIEW-001`
4. `MELLYCORE-OBSIDIAN-3D-VISUAL-QA-001`

Each future task should repeat the same safety posture: inspect first, no push unless explicitly requested, no deploy, no workflow YAML, no secrets, no runtime integration, and no fake live status.
