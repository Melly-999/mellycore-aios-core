# MellyCore Living Context Graph — Knowledge Graph Console Spec

**Task ID:** MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001
**Version:** 1.0
**Status:** Draft specification (docs-only)
**Feature name:** MellyCore Living Context Graph ("Knowledge Graph Console")

---

## 1. Feature Name and Framing

**MellyCore Living Context Graph** is the product name for a future, static-first visualization of MellyCore's own `shared_context/` and `docs/` corpus as a browsable node/edge graph, presented through a **Knowledge Graph Console**. It is a read-only exploration surface over MellyCore's existing documentation and coordination memory — not a new data store, not a live database, not a runtime feature.

It extends the same command-center, cinematic, safety-first visual language already defined in `[[../design/MELLYCORE_DESIGN_SYSTEM_001]]` and the same static-first posture defined in `[[../specs/MELLYCORE_HOMEPAGE_SPEC_001]]`.

---

## 2. User Value

- **See the shape of the project at a glance.** Instead of reading file-by-file, a reviewer or operator can see how agents, tasks, docs, sources, decisions, risks, modules, and safety rules relate to each other.
- **Find contradictions before they cause confusion.** When two sources disagree (e.g., a stale handoff file vs. a corrected spec, as happened in `MELLYCORE-DOCS-ACCURACY-SYNC-001`), the graph surfaces it as a first-class, reviewable object instead of a buried prose note.
- **Trust the timeline.** A timeline overlay shows when a node/edge was introduced, superseded, or resolved — supporting the project's existing "honest state" discipline (see `[[../../shared_context/PROJECT_STATE.md]]`, which already tracks a false-completion-claim correction).
- **Trust the safety posture.** Every rendered node/edge passes through the same safety contract as the rest of MellyCore; a safety overlay makes that visible rather than assumed.
- **Zero new operational risk.** Because the console reads only static, human-reviewed fixtures, it carries none of the risk of a live index, live database, or agent-writable store.

---

## 3. Page / Console Layout

The Knowledge Graph Console is a single page, consistent with MellyCore's one-page, no-router precedent (`[[../specs/MELLYCORE_FRONTEND_SCAFFOLD_PLAN_001]]`, Section 3). Proposed regions, top to bottom / left to right:

```
+----------------------------------------------------------------+
|  Command Bar (existing MellyCore nav + "Static Fixture" badge) |
+---------------+--------------------------------------------------+
| Left Sidebar  |  Graph Canvas (nodes + edges)                    |
| - Node search |  - Cluster rendering                             |
| - Cluster     |  - Selected-node detail panel (on click)         |
|   filter      |  - Empty/loading/error states                    |
| - Relation    |                                                  |
|   filter      |                                                  |
| - Timeline    |                                                  |
|   overlay     |                                                  |
|   toggle      |                                                  |
| - Contra-     |                                                  |
|   diction     |                                                  |
|   overlay     |                                                  |
|   toggle      |                                                  |
| - Safety      |                                                  |
|   overlay     |                                                  |
|   toggle      |                                                  |
| - Relation    |                                                  |
|   legend      |                                                  |
+---------------+--------------------------------------------------+
|  Footer Status Panel (reuses MellyCore FooterStatusPanel)       |
+----------------------------------------------------------------+
```

This layout reuses existing design-system primitives (`GlassPanel`, `HudLabel`, `StatusChip`, `SafetyBadge`, `StaticPreviewNotice`) rather than inventing new ones, per `[[../design/MELLYCORE_DESIGN_SYSTEM_001]]` Section 9.

---

## 4. Left Sidebar

**Purpose:** Primary control surface for exploring the graph without requiring direct manipulation of the canvas (important for accessibility and for the static-first MVP, where the canvas itself may initially be a static SVG rather than an interactive force-directed layout).

**Contents:**
- Section title ("Explore the Context Graph") + one-line subtitle.
- Node search input (see Section 5).
- Cluster filter (see Section 6).
- Relation filter (see Section 7).
- Timeline overlay toggle (see Section 8).
- Contradiction overlay toggle (see Section 9).
- Safety overlay toggle (see Section 10).
- Relation legend (static list, always visible — not just a hover tooltip, per accessibility rule "no information available only on hover").

**Responsive behavior:** Collapses to a top drawer or stacked panel below the canvas on tablet/mobile, consistent with `[[../design/MELLYCORE_DESIGN_SYSTEM_001]]` Section 18 (orbit-map-to-list precedent).

---

## 5. Node Search

- A single text input filters visible nodes by name/label substring match, static (no backend call — search runs against the loaded static fixture in memory, or in the MVP, against a pre-rendered static list).
- Search results list shows node type badge + name, consistent with `MemoryCard`/`HudLabel` styling.
- Selecting a search result highlights the node in the canvas and opens its detail panel.
- No autocomplete calling any external or live service. No telemetry on search terms.

---

## 6. Cluster Filter

- A `ContextCluster` (see `[[../../shared_context/CONTEXT_GRAPH_SCHEMA]]`) is a named grouping of nodes (e.g., "Design System," "Safety," "Roadmap," "Agent Roster").
- The filter is a checklist of clusters; toggling a cluster shows/hides its member nodes and their edges.
- Default state: all clusters visible.
- Visual treatment: each cluster gets a consistent accent color drawn from the existing design-system palette (Orbital Violet, Plasma Blue, Signal Cyan, Muted Lavender) — never a new ad hoc color.

---

## 7. Relation Filter

- A checklist of edge/relation types (see relation type list in `[[../../shared_context/CONTEXT_GRAPH_SCHEMA]]`: `depends_on`, `defines`, `references`, `contradicts`, `supersedes`, `produced_by`, `validated_by`, `blocked_by`, `belongs_to`).
- Toggling a relation type shows/hides edges of that type only; node visibility is unaffected unless a node becomes fully disconnected from the visible edge set, in which case it dims (not hides) to preserve "honest state" (nothing disappears silently).
- Default state: all relations visible except `contradicts`, which is off by default and surfaced instead through the dedicated Contradiction Overlay (Section 9) to avoid visual noise.

---

## 8. Timeline Overlay

- A toggle plus a simple range/step control (e.g., a slider or a discrete list of dated snapshots — see `[[../../shared_context/CONTEXT_PACK_GENERATOR_SPEC]]` for snapshot naming) that filters the graph to nodes/edges that existed as of a selected date.
- Superseded nodes (see `supersedes` relation) fade to a dimmed style rather than disappearing, so history remains visible.
- In the static MVP, the timeline is driven by discrete named snapshots (dated fixture files), not continuous live time. No "now" auto-refresh.

---

## 9. Contradiction Overlay

- A toggle that, when on, highlights all nodes/edges connected to an open entry in `[[../../shared_context/CONTRADICTION_LEDGER]]` with a distinct visual treatment (amber outline, consistent with the existing "Soft Warning Amber" token — never a new color).
- Clicking a highlighted contradiction opens a detail panel showing the ledger entry: claim A, claim B, source refs, severity, status.
- Resolved contradictions (status = resolved) show a muted/checked variant, consistent with `Safe Status Green`.
- This overlay directly operationalizes the safety posture already established in `PROJECT_STATE.md`, where a prior false-completion claim was caught and corrected (`MELLYCORE-DOCS-ACCURACY-SYNC-001`).

---

## 10. Safety Overlay

- A toggle that highlights every node of type `safety_rule` and every edge of type `validated_by` or `blocked_by`, making the safety-constraint layer visually traceable through the whole graph — consistent with `[[../design/MELLYCORE_DESIGN_SYSTEM_001]]`'s "safety as a first-class visual layer" principle.
- When active, a small persistent panel confirms: "Safety Overlay Active — showing safety_rule nodes and validated_by/blocked_by edges only where present in reviewed fixtures." This must never claim real-time validation; it reflects only the last human-reviewed static fixture.

---

## 11. Static MVP

The first shippable slice (subject to separate implementation approval) is:

1. A single static graph fixture (JSON, per `[[../../shared_context/CONTEXT_GRAPH_SCHEMA]]`) hand-authored or produced by one human-reviewed ingest pass (`[[../../shared_context/SOURCE_INGEST_WORKFLOW]]`), covering MellyCore's own existing `shared_context/` and `docs/design`/`docs/specs` files as the initial corpus.
2. A static SVG or CSS-positioned rendering of that fixture — no force-directed physics engine, no WebGL, no client-side graph library dependency in the first slice (consistent with the zero-JavaScript-first-slice precedent in `[[../specs/MELLYCORE_FRONTEND_SCAFFOLD_PLAN_001]]`, though light JS may be proposed later for search/filter interactivity — subject to its own approval and safety review).
3. Sidebar controls (search, cluster filter, relation filter, legend) that operate purely on the static fixture already loaded — no network calls.
4. Timeline, contradiction, and safety overlays implemented against the static fixture's authored metadata — no live computation.
5. Explicit "Static Fixture — Last Reviewed [date]" badge, consistent with MellyCore's existing `StaticPreviewNotice` pattern.

## 12. Future Phases (Not Authorized by This Document)

- **Phase 2 — Interactive layout:** client-side force-directed or hierarchical layout with light JavaScript, still reading only static fixtures (no backend).
- **Phase 3 — Multi-snapshot comparison:** side-by-side or diff view between two named snapshots (extends the Neon-inspired "branchable snapshot" metaphor from `[[../research/external_inspiration_llm_wiki_graph_001]]`), still static-file-based.
- **Phase 4 — Assisted ingest tooling:** a semi-automated pass that proposes new nodes/edges/contradiction-ledger entries from newly added sources, always gated by human review before becoming a committed fixture (per `[[../../shared_context/SOURCE_INGEST_WORKFLOW]]`).
- **Phase 5 (explicitly blocked/later, requires separate approval and safety review):** any live backing store, any write API, any multi-user editing, any automatic ingestion without human review. This phase is not scoped, designed, or authorized here.

Every phase beyond the Static MVP requires its own explicit operator approval before implementation, consistent with the gating pattern already used for `[[../specs/MELLYCORE_FRONTEND_SCAFFOLD_PLAN_001]]`.

---

*This product specification is a docs-only artifact of `MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001`. It authorizes no runtime, backend, database, or frontend implementation.*
