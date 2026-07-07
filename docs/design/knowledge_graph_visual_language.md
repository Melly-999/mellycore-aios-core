# Knowledge Graph Visual Language

**Task ID:** MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001
**Version:** 1.0
**Status:** Draft specification (docs-only)
**Scope:** Visual design direction for the MellyCore Living Context Graph / Knowledge Graph Console

---

## 1. Relationship to the Core Design System

This document extends `[[../design/MELLYCORE_DESIGN_SYSTEM_001]]` (referred to below as "the core design system"). It does not redefine any color, type, or spacing token — it applies the existing tokens to a new visualization surface (the graph canvas). Where this document is silent, the core design system governs.

---

## 2. Black-Space Background

- Graph canvas background is Void Black / Deep Space Black, matching the core design system's Section 13 background guidance — not a separate "app background" color.
- The canvas may include the same sparse star field as the rest of the site (10-30% opacity, 50-100 points per 1920x1080), but density should be reduced further (target 30-50 points) directly behind dense node clusters so stars never compete with node/edge legibility.
- No canvas-filling nebula gradient behind the densest cluster region — reserve nebula gradient for the canvas edges/corners only, so it frames rather than obscures the graph.

---

## 3. Purple/Blue/Cyan Neon Clusters

- Each `ContextCluster` is assigned one accent from the existing palette only: Orbital Violet, Plasma Blue, Signal Cyan, or Muted Lavender (core design system Section 6). No new hues are introduced for clusters.
- A cluster's accent applies to: its nodes' border/glow, its cluster-filter checkbox accent in the sidebar, and its legend swatch. The same accent must be used consistently across all three, so a user can trace a color from legend to sidebar to canvas without ambiguity.
- If more than four clusters exist simultaneously, reuse accents rather than inventing new colors, and differentiate via node shape or label instead (see Section 4). Color alone must never be the only differentiator (accessibility rule, Section 9).

---

## 4. Node Sizing Rules

- Node size communicates **structural weight within the graph** (in-degree + out-degree — how many edges touch it), not importance or priority, to avoid implying an editorial ranking the graph doesn't actually compute.
- Three discrete size tiers only: small (1-2 edges), medium (3-6 edges), large (7+ edges). No continuous/proportional scaling — discrete tiers keep the canvas legible and consistent with the core system's "no dashboard clutter" principle.
- Node shape encodes node **type**, not cluster or size:
  - `agent` — hexagon (matches existing `ConstellationNode` agent styling).
  - `model` — hexagon with inner ring (distinguishes from `agent` while reusing the hex language).
  - `task` — rounded square.
  - `doc` — rectangle (document silhouette).
  - `source` — small circle with a dotted border (signals "external/immutable").
  - `decision` — diamond.
  - `risk` — triangle (reuses the existing warning-triangle association from the core system's iconography direction, Section 15).
  - `module` — square.
  - `safety_rule` — shield-outline shape (reuses the existing safety shield icon language, Section 15).
- Node fill is always a low-opacity tint of its cluster color; node border/glow is the full-strength cluster color. Fill alone must never be the sole way size or type is communicated — shape and a text label always accompany it.

---

## 5. Edge Styles

- Default edge: 1-2px line, Plasma Blue at reduced opacity (matches core system `RouteLine` primitive), matching the "no distracting animation" motion principle — edges are static, never animated to imply live data flow.
- Edge style by relation type (color reserved for cluster/node identity, so relation type is encoded by **line style**, not color, to avoid overloading color semantics):
  - `depends_on` — solid line, arrowhead at the depended-upon node.
  - `defines` — solid line, no arrowhead (bidirectional definitional link).
  - `references` — dashed line, thin.
  - `contradicts` — double line (two parallel thin lines) in the contradiction-overlay's amber accent, shown only when the Contradiction Overlay is active (see product spec, Section 9) or when the relation filter explicitly enables it.
  - `supersedes` — solid line with a small perpendicular tick mark at the midpoint (visually distinct from a plain arrow), pointing from the superseding node to the superseded node.
  - `produced_by` — dotted line.
  - `validated_by` — solid line with a small check-mark glyph at the midpoint.
  - `blocked_by` — solid line with a small stop-mark (short perpendicular bar) at the midpoint, Soft Warning Amber accent.
  - `belongs_to` — thin solid line, no arrowhead, reduced opacity (structural/containment link, visually recessive relative to semantic relations).
- Every edge style above must remain distinguishable in a static screenshot (no reliance on animation, hover, or hue alone) and must be documented in the always-visible Relation Legend (Section 7).

---

## 6. Label Density Rules

- Node labels: always visible for `large` tier nodes; visible on hover/focus or when zoomed for `medium`/`small` tier nodes in the interactive future phase; in the static MVP (no zoom/pan), all node labels are visible by default, since the fixture-driven canvas is expected to be modest in size.
- If label crowding occurs in the static MVP, prefer **fewer visible clusters at once** (via the cluster filter) over shrinking or truncating label text below the core system's minimum HUD label size (11px).
- Edge labels are never used (matches core system's `RouteLine` rule: "lines only — no labels on lines. Labels belong on nodes.").
- Cluster names appear once, as a section/legend heading, not repeated on every member node.

---

## 7. HUD Sidebar

- The left sidebar (product spec Section 4) is a `GlassPanel` per the core design system, using the same blur/border/shadow limits (Section 11 of the core system): one shadow max, 15-20% border opacity.
- Sidebar controls (search input, filter checklists, toggles) use existing primitives: `HudLabel` for section headings, `StatusChip`-style toggle states ("on"/"off" always paired with text, never color-only).
- Sidebar is non-scrolling-priority: on desktop it is fixed-position alongside the canvas; on mobile it collapses above the canvas as a stacked panel (core system Section 18 precedent).

---

## 8. Relation Legend

- Always visible (not hover-only), rendered as a compact static list in the sidebar: one row per relation type, showing the line-style swatch (Section 5) plus the relation name in HUD label style.
- The legend is the single source of truth for edge-style meaning; it must be kept in exact sync with `[[../../shared_context/CONTEXT_GRAPH_SCHEMA]]`'s relation type list. If the schema changes, this document and the legend must be updated together.

---

## 9. Empty / Loading / Error States

- **Empty state** (a filter combination yields zero visible nodes): a centered `GlassPanel` message — "No nodes match the current filters." plus a single "Reset Filters" action. Never a blank canvas with no explanation.
- **Loading state** (static MVP): since data is a static fixture bundled with the page, "loading" should be near-instant; if a loading placeholder is shown at all, it is a static skeleton (no spinner animation), consistent with the core system's "no spinning loaders" rule (Section 16).
- **Error state** (fixture fails to parse, or a future phase's fetch fails): a plain-text `GlassPanel` notice — "Context graph data could not be loaded." No fake retry-with-backoff UI implying live infrastructure; a simple manual "Reload page" link is sufficient for a static artifact.
- No state may imply a live backend is being retried or polled.

---

## 10. Accessibility

- All node/edge type distinctions are encoded in at least two channels (shape + color, or line-style + color) — never color alone, per the core system's accessibility guardrail #5.
- Every toggle (cluster filter, relation filter, timeline, contradiction overlay, safety overlay) is a real, labeled, keyboard-operable control (checkbox/button semantics), with visible focus rings in Signal Cyan or Orbital Violet, matching core system guardrail #2.
- Detail panels opened by selecting a node must be reachable and closable via keyboard alone.
- All canvas text (labels, legend, sidebar) meets WCAG AA contrast against the void-black/deep-space background, tested through any glass/blur layers per core system Section 11.
- The graph must remain meaningful as a static image: taking a screenshot with all overlays off must still convey cluster grouping, node type, and edge relation via shape/line-style — not only via color.

---

## 11. Reduced Motion

- The static MVP has no animation to reduce (no auto-layout physics, no pulsing).
- If a future interactive phase adds transitions (e.g., fade when a filter changes which nodes are visible), all such transitions must respect `prefers-reduced-motion: reduce` and become instant, per core system Section 16 — no exception for the graph canvas.
- No graph layout may depend on animation to be understood; the final settled layout must be legible from a single static frame.

---

## 12. Responsive Behavior

- **Desktop (≥1280px):** sidebar fixed at left (per core system spacing rhythm, Section 8), canvas fills remaining width, relation legend fully visible in sidebar.
- **Tablet (768-1279px):** sidebar collapses to a top drawer/panel above canvas; canvas simplifies by reducing default-visible clusters (user can re-enable via filter) rather than shrinking node/label size below minimums.
- **Mobile (≤767px):** canvas is not expected to render a full graph usefully; the MVP mobile behavior is a **linear list fallback** — nodes grouped by cluster in a vertical list (reusing `MemoryCard`-style cards), each showing its type, cluster, and a compact list of its edges by relation label. This mirrors the existing orbit-map-to-list and constellation-to-card-list precedents in `[[../design/MELLYCORE_DESIGN_SYSTEM_001]]` Section 18. No horizontal scroll at any breakpoint (375px, 768px, 1024px, 1280px, 1920px), consistent with the existing scaffold plan's responsive requirements.

---

*This visual language specification is a docs-only artifact of `MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001`. It authorizes no runtime, backend, or frontend implementation — it defines the design direction for a future, separately approved implementation task.*
