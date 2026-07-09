# MellyCore Obsidian-Style 3D Graph Page Spec 001

**Task ID:** MELLYCORE-OBSIDIAN-3D-PAGE-SPEC-001
**Status:** Draft product/design specification
**Scope:** Docs-only concept specification for a future Obsidian-like 3D graph page in MellyCore AIOS

---

## 1. Purpose

This document specifies a future Obsidian-like 3D graph page for MellyCore AIOS. The page would extend the completed Living Context Graph static UI milestone from a flat local preview into a spatial context-navigation concept for MellyCore docs, decisions, sources, safety gates, contradictions, and planned modules.

This document is a specification only. It does not implement frontend code, JavaScript, Three.js, WebGL, Obsidian sync, MCP integration, backend services, APIs, databases, runtime ingestion, deployment, workflow YAML, provider connections, or a live graph.

## 2. Relationship to the Completed Static Graph Milestone

The current source of truth remains `shared_context/context_graph_fixture_001.json`.

Current fixture counts:

- Clusters: 8
- Nodes: 45
- Edges: 66

The existing static milestone includes:

- Fixture documentation in `shared_context/CONTEXT_GRAPH_FIXTURE_001.md`.
- Schema guidance in `shared_context/CONTEXT_GRAPH_SCHEMA.md`.
- Static UI spec in `docs/specs/MELLYCORE_KNOWLEDGE_GRAPH_STATIC_UI_SPEC_001.md`.
- Static site scaffold in `site/index.html` and `site/css/`.
- Final showcase audit in `docs/tasks/MELLYCORE-KNOWLEDGE-GRAPH-STATIC-UI-FINAL-SHOWCASE-AUDIT-001.md`.
- External visual QA evidence stored outside the repository.

The 3D page concept must build on that milestone, not replace it. The product story is:

**From static context map to spatial context navigation.**

The first future implementation, if separately approved, should still be static-first and fixture-backed. It must not imply live Obsidian vault access, live graph generation, provider connection, runtime ingestion, or deployed availability.

## 3. User Experience Goals

The page should help a reviewer or operator:

- Understand the MellyCore project as a spatial knowledge system rather than a file tree.
- See how context, decisions, safety rules, tasks, risks, and future modules relate.
- Inspect graph evidence without opening raw source files first.
- Detect contradiction and safety-risk neighborhoods quickly.
- Distinguish current reviewed nodes from planned, disabled, or external-inspiration nodes.
- Preserve the premium cinematic command-center tone from `docs/design/MELLYCORE_DESIGN_SYSTEM_001.md`.
- Stay clear that the surface is a static concept until a separate implementation task says otherwise.

## 4. Conceptual Page Layout

A future page may use these regions:

1. **3D graph hero viewport:** A full-width spatial graph stage with static status copy, fixture counts, and no fake live indicators.
2. **Cluster constellation layer:** Eight fixture clusters arranged as constellations around a MellyCore context core.
3. **Node inspector panel:** A right-side or bottom panel for selected-node metadata, source refs, status, confidence, and safety display state.
4. **Source/evidence drawer:** A text-first evidence view listing repo-relative source references and edge evidence references.
5. **Contradiction/risk lane:** A dedicated lane for contradiction, blocked-by, stale-source, fake-live-claim, and old-origin-main risks.
6. **Context pack preview:** A planned panel showing what a static context pack could contain, clearly marked not implemented.
7. **Safety status rail:** Always-visible safety badges for no secrets, no provider keys, no runtime backend, no deploy, no workflow YAML, no live trading UX, and no fake live claim.
8. **Timeline/session path:** A static future concept for showing dated fixture snapshots or selected review paths. No continuous current-time or auto-refresh claim.
9. **Future module cards:** Ghosted or dormant nodes for separately approved future concepts such as cloud readiness, 3D visual language, or richer static scaffolds.

## 5. 3D Graph Model

The future 3D model should map the existing fixture without adding hidden runtime meaning:

| Fixture concept | 3D treatment |
|---|---|
| Clusters | Constellations or spatial groups with labels and text summaries |
| Nodes | Weighted objects with type shape, cluster accent, readable label, and metadata fallback |
| Edges | Relationship lines with style by relation type, not color alone |
| Source refs | Evidence anchors connected to node inspector and source drawer |
| Safety risks | Warning markers or shield overlays, always paired with text |
| Contradictions | Amber risk lane markers and relation highlights |
| Future modules | Dormant, ghosted, approval-gated nodes |
| External inspiration | Low-confidence boundary nodes with dashed styling and unverified labels |

Node size should continue to mean graph structure, not editorial importance. Importance, status, and confidence belong in text metadata.

## 6. Node Interaction Model

This section describes future behavior only. It is not implemented.

| State | Required behavior |
|---|---|
| Default | Node label, type cue, cluster cue, and text fallback are available. |
| Hover/focus | Highlight the node and its immediate edges; provide equivalent keyboard focus behavior. |
| Selected | Open the node inspector with label, type, cluster, summary, source refs, safety state, incoming/outgoing relation counts, and status. |
| Source refs visible | Show evidence anchors in the drawer; never fetch raw sources live. |
| Related-node highlight | Dim unrelated graph regions without hiding safety warnings or selected-node context. |
| Contradiction/risk highlight | Use amber text and line styling, plus a plain-language risk label. |
| Disabled/future module | Use dormant styling and copy such as "planned concept only" or "approval gated". |

No critical information may be available only through hover, animation, depth position, or color.

## 7. Safety UX Requirements

Safety content must be a first-class layer of the page, not a footer note.

The page must explicitly preserve:

- No secrets.
- No provider keys.
- No runtime backend.
- No API integration.
- No database.
- No deploy.
- No workflow YAML.
- No Obsidian sync.
- No MCP connection.
- No live trading, broker, order, buy, sell, or execute UX.
- No fake live graph claim.
- No fake live URL claim.
- No misleading production claim.
- Old `origin/main` remains unrelated and untouched unless a separate approved task says otherwise.
- External inspiration remains conceptual and unverified unless captured in a reviewed repo source.

Safety rail copy should use short, factual labels:

- "Static fixture"
- "No live ingestion"
- "No provider keys"
- "No deploy"
- "No workflow YAML"
- "No Obsidian sync"
- "No MCP connection"
- "No trading UX"
- "Old origin untouched"

## 8. Visual Language

The page should extend the existing MellyCore design system:

- Deep-space command-center background.
- Glass panels with controlled borders and blur.
- Orbital Violet, Plasma Blue, Signal Cyan, Muted Lavender, Safe Status Green, Soft Warning Amber, and Dormant Gray only.
- Sparse starfield and restrained nebula framing.
- Premium HUD typography with readable labels.
- Relation styles synced with `docs/design/knowledge_graph_visual_language.md`.
- Safety and status labels paired with text, never color alone.

The 3D graph should feel like a spatial knowledge observatory, not a trading terminal, crypto dashboard, or live operations console.

## 9. Accessibility and Fallbacks

A future 3D implementation must provide:

- A non-3D text fallback containing cluster, node, edge, source, and safety summaries.
- A keyboard-readable node list grouped by cluster.
- A screen-reader summary of the selected node and its relations.
- A static table fallback for edges and source references.
- Reduced-motion support that disables camera travel, auto-rotation, parallax, and animated graph transitions.
- No graph-only critical information.
- Logical semantic headings and labelled panels.
- Focus-visible states for every control.
- Text labels for status, risk, relation type, and safety state.
- Contrast that remains readable through glass panels and on dark backgrounds.

The page must remain understandable as a static screenshot.

## 10. Responsive Behavior

| Viewport | Expected behavior |
|---|---|
| Mobile | 3D view becomes a text-first stacked graph summary. Cluster list, node cards, relation legend, source drawer, and safety rail appear as readable sections. No horizontal scrolling is required. |
| Tablet | A simplified spatial preview may sit above condensed inspector and safety panels. Dense graph labels are reduced by grouping, not by shrinking text below readable sizes. |
| Desktop | Full constellation stage, cluster layer, node inspector, source drawer, risk lane, and safety rail can appear together. |
| Wide desktop | The graph stage may breathe, but text panels keep readable width. The page should not stretch metadata into long unreadable lines. |

Mobile fallback is required. The graph information must not depend on WebGL, a pointer device, or a wide canvas.

## 11. Implementation Constraints for Future Tasks

Any future implementation task must remain separately approved and must state its scope precisely.

The first scaffold should be:

- Static-first.
- Fixture-backed.
- Honest about concept status.
- Free of provider keys and secrets.
- Free of backend/API/database assumptions.
- Free of Obsidian vault reads unless separately approved.
- Free of MCP integration unless separately approved.
- Free of deploy or GitHub Pages unless separately approved.
- Free of workflow YAML unless separately approved.

Three.js, WebGL, JavaScript, or any interactive graph library may be considered only in a later explicitly approved implementation task with a safety review and fallback plan.

## 12. Honest Copy Guidelines

Allowed wording:

- "static concept"
- "planned 3D layer"
- "future spatial graph"
- "fixture-backed preview"
- "evidence-backed graph"
- "reviewed metadata"
- "not connected live"
- "approval gated"

Forbidden wording:

- "live Obsidian sync"
- "MCP connected"
- "real-time ingestion"
- "production graph"
- "deployed"
- "connected to providers"
- "autonomous runtime"
- "live URL"
- "provider-backed graph"
- "auto-refreshing graph"

## 13. Future Task Ladder

Recommended follow-up tasks:

1. `MELLYCORE-OBSIDIAN-3D-PAGE-SPEC-REVIEW-001` — review this spec for fixture alignment, design consistency, accessibility, responsive behavior, and safety correctness.
2. `MELLYCORE-OBSIDIAN-3D-VISUAL-LANGUAGE-001` — define the 3D-specific visual rules without implementing a page.
3. `MELLYCORE-OBSIDIAN-3D-STATIC-SCAFFOLD-001` — separately approved static scaffold only, if the spec and visual-language review pass.
4. `MELLYCORE-OBSIDIAN-3D-VISUAL-QA-001` — visual QA for any future static scaffold.

---

*This is a docs-only concept specification. It creates no frontend/site/backend/runtime/API/database/provider/MCP/Obsidian integration and does not authorize deployment.*
