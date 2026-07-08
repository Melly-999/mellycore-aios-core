# MellyCore Knowledge Graph Static UI Spec 001

**Task ID:** MELLYCORE-KNOWLEDGE-GRAPH-STATIC-UI-SPEC-001
**Status:** Draft static UI specification
**Scope:** Docs-only UI specification for displaying `shared_context/context_graph_fixture_001.json` in the MellyCore static website

---

## 1. Purpose

This document specifies a static, safety-first UI presentation for the existing MellyCore Living Context Graph fixture. It describes how the reviewed fixture can be represented in a future static website section or page while preserving the current project posture: static HTML/CSS first, honest status copy, and no live system claims.

This is not:

- Live graph generation.
- Runtime ingestion.
- Backend, API, database, provider, or MCP integration.
- Obsidian integration.
- Deployment, GitHub Pages enablement, or workflow YAML.
- Frontend/site implementation.

## 2. Source Fixture

The source fixture is `shared_context/context_graph_fixture_001.json`.

Fixture counts:

- Clusters: 8
- Nodes: 45
- Edges: 66

The fixture is hand-authored and reviewable. It is a static snapshot derived from repo docs, task reports, shared context, safety rules, and reviewed inspiration summaries. UI copy must describe it as a "static fixture", "reviewed snapshot", or "preview", never as a generated-live graph or production service.

## 3. User Experience Goals

The UI should help an operator, reviewer, or future agent understand the MellyCore context graph at a glance:

- Show the major clusters and the relationships between them.
- Make nodes, relation types, source references, confidence, status, and safety boundaries visible without requiring raw file access.
- Preserve a premium cinematic command-center feeling consistent with `docs/design/MELLYCORE_DESIGN_SYSTEM_001.md`.
- Stay honest: the graph is static, evidence-backed, and not connected live.
- Make safety constraints more visible than decorative effects.

## 4. Layout Proposal

Future implementation should use one static section or page with these regions:

1. **Header strip:** Page title, fixture count summary, "Static fixture" badge, and "Last reviewed fixture" copy.
2. **Graph canvas mock area:** A static SVG, CSS-positioned map, or static visual composition of clusters, nodes, and edges. No JavaScript is required for the first implementation.
3. **Cluster rail:** A left or top list of the 8 clusters with count badges, short descriptions, and cluster accents.
4. **Node detail panel:** A static representative detail panel for the selected or featured node model. If the first implementation is fully static, show a curated default node such as `MellyCore AIOS` or `Fixture 001`.
5. **Edge/relation legend:** Always-visible relation legend matching `shared_context/CONTEXT_GRAPH_SCHEMA.md`.
6. **Safety/risk panel:** Prominent badges for no secrets, no provider keys, no runtime backend, no deploy, no workflow YAML, no live trading UX, fake-live-claim risk, and old-origin-main unrelated risk.
7. **Source references section:** A compact drawer-like section or table listing repo-relative source references used by the featured node and graph snapshot.
8. **Contradiction/risk ledger preview:** A static preview that links graph contradictions and risks to `shared_context/CONTRADICTION_LEDGER.md`; if there are no live entries, say so plainly.
9. **Context pack preview panel:** A future-looking panel describing the read-only context-pack concept from `shared_context/CONTEXT_PACK_GENERATOR_SPEC.md`, clearly marked "planned" and "not implemented".

## 5. Graph Display Model

The UI should display graph data through reviewed metadata only:

| Fixture field | UI treatment |
|---|---|
| `clusters` | Cluster rail, canvas group labels, legend swatches, summary counts |
| `nodes` | Static node glyphs plus accessible list/card fallback |
| `edges` | Static edge paths or relation rows with visible line-style legend |
| `relation` | Encoded by line style and text label, not color alone |
| `confidence` | Text badge: high, medium, low |
| `sourceRefs` / `evidenceRefs` | Repo-relative source reference chips or table rows |
| `safeToDisplay` | Safety badge or suppressed from UI if false in a future fixture |
| `status` | Status chip: current, complete, draft, future, active-risk, do-not-touch |
| `importance` | Optional text badge; do not use it as the only sizing rule |

Node size should continue to follow the visual-language rule: structural graph weight, not editorial importance. Importance may be shown as a small label in the node card.

## 6. Cluster Visual Language

Use the existing MellyCore token family only. Do not introduce a new hue system for this feature. Because there are 8 clusters and 4 primary accents in the current graph visual language, reuse accents and differentiate with labels, shape, grouping, and ordering.

| Cluster | UI treatment |
|---|---|
| `product-foundation` | Orbital Violet accent; positioned as the root cluster in the map |
| `static-showcase` | Plasma Blue accent; connected to site and preview evidence nodes |
| `shared-context` | Signal Cyan accent; represented as the memory backbone cluster |
| `safety-governance` | Safe Status Green plus amber risk treatments where needed |
| `knowledge-graph` | Orbital Violet accent with denser relation visibility |
| `repository-governance` | Muted Lavender with caution badges for old-origin risk |
| `future-modules` | Dormant gray / muted lavender; visibly future and approval-gated |
| `external-inspiration` | Dashed or dotted source styling; confidence labels always visible |

Color must never be the only differentiator. Each cluster row should include its label and summary, and the canvas should remain understandable through text, grouping, shape, and legend.

## 7. Node Card Model

Every node detail card should include:

- `label`
- `type`
- `cluster`
- `status`
- `importance`
- `confidence`
- `summary`
- `sourceRefs`
- Safety badge from `safeToDisplay`
- Related edges count, split by incoming and outgoing when space allows

Recommended card copy pattern:

- Title: node label.
- Meta row: type, cluster, status, confidence.
- Summary: one reviewed sentence from the fixture.
- Evidence: repo-relative source reference chips.
- Safety: "Safe to display: reviewed metadata only" when applicable.
- Relations: count and a compact list of the most important relations.

## 8. Edge / Relationship Legend

The relation legend must be always visible and keyboard/screen-reader readable. It must include all relation types from the fixture and schema:

| Relation | Static visual treatment |
|---|---|
| `depends_on` | Solid line with arrow toward the dependency |
| `defines` | Solid line, no arrowhead, authoritative label |
| `references` | Thin dashed line |
| `contradicts` | Double amber line and contradiction badge |
| `supersedes` | Solid line with midpoint tick |
| `produced_by` | Dotted line |
| `validated_by` | Solid line with check glyph |
| `blocked_by` | Amber line with stop mark |
| `belongs_to` | Thin reduced-opacity structural line |

No relation meaning may depend on hover, animation, or color alone.

## 9. Safety UX

Safety content is a first-class UI layer, not footer text. The graph section should show badges or warnings for:

- `no-secrets`
- `no-provider-keys`
- `no-runtime-backend`
- `no-deploy`
- `no-workflow-yaml`
- `no-live-trading-ux`
- `fake-live-claim-risk`
- `old-origin-main-unrelated-risk`

Badge copy should be short and honest:

- "No secrets in fixture"
- "No provider keys"
- "No runtime backend"
- "No deploy"
- "No workflow YAML"
- "No trading UX"
- "Static-only claim"
- "Old origin untouched"

If a future fixture includes a node with `safeToDisplay: false`, that node must be excluded from the committed public fixture rather than hidden only in CSS.

## 10. Static Implementation Constraints

Any future implementation based on this spec must remain:

- Static HTML/CSS first.
- No backend.
- No API.
- No database.
- No provider keys.
- No runtime ingestion.
- No deploy unless separately approved.
- No workflow YAML unless separately approved.
- No JavaScript in the first scaffold unless a separate task explicitly changes scope.

The static page may reference the fixture counts and selected metadata, but it must not claim to fetch, parse, ingest, or refresh live data.

## 11. Responsive Behavior

| Viewport | Behavior |
|---|---|
| Mobile | Use a linear grouped list by cluster. Node cards stack vertically. Relation legend appears before or after the list. Avoid horizontal canvas scrolling. |
| Tablet | Use a simplified graph preview above a collapsible-style static cluster list. Keep labels readable; reduce visible edges rather than shrinking text below minimums. |
| Desktop | Show cluster rail, graph canvas, node detail panel, and legend in a balanced command-center layout. |
| Wide desktop | Keep max content width controlled. The canvas can breathe, but text panels should not stretch beyond readable measure. |

The mobile fallback is not optional. The graph information must remain available without relying on a dense canvas.

## 12. Accessibility

The static graph UI must provide:

- Readable contrast on void black / deep-space backgrounds and glass panels.
- Semantic headings in a logical order.
- Keyboard-readable document structure.
- Text alternatives for graph information through a cluster/node/edge list.
- Reduced-motion compatibility; the first static implementation should have no required motion.
- No graph-only information hidden from screen readers.
- Relation types represented by line style plus text labels.
- Status and safety information represented by text, not color alone.

## 13. Empty / Error States

Even though the first implementation is static, the spec should define honest fallback copy:

- **Fixture unavailable:** "Context graph fixture is not available in this static preview. Review `shared_context/context_graph_fixture_001.json` in the repository."
- **Source ref missing:** "Source reference missing from reviewed fixture. Do not display this node as verified until reviewed."
- **Unverified inspiration:** "External inspiration is conceptual and unverified. It is not copied source material."
- **Future module not implemented:** "Planned concept only. No runtime, provider, backend, or integration is implemented."

Avoid retry loops, spinners, or live-error language that implies backend infrastructure.

## 14. Copy Guidelines

Use honest wording:

- "static fixture"
- "preview"
- "planned"
- "not connected live"
- "evidence-backed"
- "reviewed metadata"
- "docs/spec phase"

Avoid:

- "live graph"
- "production"
- "autonomous ingestion"
- "deployed"
- "connected to providers"
- "real-time"
- "online"
- "auto-refreshing"

No copy should suggest a live website URL, production graph, provider connection, or runtime graph service.

## 15. Future Implementation Tasks

Recommended follow-up tasks:

- `MELLYCORE-KNOWLEDGE-GRAPH-STATIC-UI-SPEC-REVIEW-001`
- `MELLYCORE-KNOWLEDGE-GRAPH-STATIC-UI-SCAFFOLD-001`
- `MELLYCORE-KNOWLEDGE-GRAPH-STATIC-UI-VISUAL-QA-001`
- `MELLYCORE-OBSIDIAN-3D-PAGE-SPEC-001`

The review task should happen before any scaffold task. The scaffold task should remain static HTML/CSS unless a separate operator-approved task changes scope.

---

*This is a docs-only static UI specification. It creates no frontend/site/backend/runtime/API/database/provider/MCP/Obsidian integration and does not authorize deployment.*
