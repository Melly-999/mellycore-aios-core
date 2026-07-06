# MellyCore AIOS — UI Sections Implementation Brief

**Task ID:** MELLYCORE-HOMEPAGE-SPEC-001 (companion)
**Version:** 1.0
**Status:** Complete
**Scope:** Compact implementation brief for future frontend agents building the MellyCore AIOS homepage

---

## Section Registry

### hero-command-center

| Field | Value |
|---|---|
| **Section ID** | `hero-command-center` |
| **Name** | Hero — MellyCore AIOS Command Center |
| **Priority** | P0 — Must have |
| **Purpose** | Establish identity, prototype status, and core value proposition in first viewport. |
| **Required Data** | Headline text, subtitle, prototype tag, safety badge labels, CTA anchor targets. All static. |
| **Static/Dynamic** | Static only. No data fetching. |
| **Allowed Implementation** | HTML/CSS hero section, static orbital cube (CSS illustration or static image), anchor-link CTAs, safety badges. |
| **Blocked Implementation** | 3D libraries (Three.js, etc.) in first slice, animated cube, live-data indicators, connect-live CTAs, form elements. |
| **Future Components** | `HeroSection`, `OrbitalCubeVisual`, `HeroCtaGroup`, `PrototypeStatusBanner` |
| **Validation Notes** | Must render without JavaScript. CTAs must be anchor links only. No forbidden CTAs. |
| **Safety Notes** | Prototype status visible before any CTA. No live connectivity implied. Safety badges accurate. |

### agent-constellation

| Field | Value |
|---|---|
| **Section ID** | `agent-constellation` |
| **Name** | Agent Constellation |
| **Priority** | P0 — Must have |
| **Purpose** | Visualize supervised multi-agent fleet with OmniRouter as central hub. |
| **Required Data** | Agent list (10 nodes), role labels, "supervised" status, route connections to OmniRouter. All static. |
| **Static/Dynamic** | Static only. Node positions authored in CSS/markup. |
| **Allowed Implementation** | CSS-positioned constellation diagram, static SVG route lines, agent node cards, mobile card list. |
| **Blocked Implementation** | Interactive node dragging, live agent status, animated route lines, real-time connectivity indicators. |
| **Future Components** | `AgentConstellationSection`, `ConstellationMap`, `ConstellationNode`, `AgentCardList` |
| **Validation Notes** | OmniRouter must be visually central. All nodes show "supervised." Mobile converts to list. |
| **Safety Notes** | No autonomous agents implied. No live status. OmniRouter is the routing hub connecting all nodes. |

### model-router-panel

| Field | Value |
|---|---|
| **Section ID** | `model-router-panel` |
| **Name** | OmniRouter / Model Router Panel |
| **Priority** | P1 — High priority |
| **Purpose** | Show model routing architecture with OmniRouter as preferred gateway. No live connectivity. |
| **Required Data** | Provider list (5 placeholders), routing role labels, OmniRouter hub description, "no live routing" notice. All static. |
| **Static/Dynamic** | Static only. |
| **Allowed Implementation** | Control-panel layout, placeholder provider cards with dormant styling, "no live routing" notice, routing role labels. |
| **Blocked Implementation** | Provider selection UI, API key inputs, routing simulation, live provider health checks, "add provider" buttons. |
| **Future Components** | `ModelRouterPanel`, `ProviderPlaceholderCard`, `OmniRouterHub`, `RouterNode` |
| **Validation Notes** | No form elements. All providers show "placeholder" status. "No live routing" notice present. |
| **Safety Notes** | No secrets. No keys. Provider keys stated as "outside the repo." No connection forms. |

### shared-context-memory

| Field | Value |
|---|---|
| **Section ID** | `shared-context-memory` |
| **Name** | Shared Context / Memory Layer |
| **Priority** | P0 — Must have |
| **Purpose** | Show unified coordination memory that all agents share. |
| **Required Data** | File list (10 context files), file descriptions, type badges. All static. |
| **Static/Dynamic** | Static only. |
| **Allowed Implementation** | Card grid (2-3 columns), memory cards with file metadata, glass panel styling, type badges. |
| **Blocked Implementation** | File browser, content preview, download links, dynamic file listing, filesystem access. |
| **Future Components** | `SharedContextSection`, `MemoryCardGrid`, `ContextFileCard` |
| **Validation Notes** | No file contents displayed. Only metadata. Grid responds to viewport. |
| **Safety Notes** | No secrets in card content. No real file values. Static file list only. |

### roadmap-orbit-map

| Field | Value |
|---|---|
| **Section ID** | `roadmap-orbit-map` |
| **Name** | Roadmap Orbit Map |
| **Priority** | P0 — Must have |
| **Purpose** | Visualize project phases as orbital progression. Honest roadmap state. |
| **Required Data** | Phase list (6 phases), status per phase, deliverable bullets, blocked/later labels. All static. |
| **Static/Dynamic** | Static only. |
| **Allowed Implementation** | CSS orbital rings with positioned phase markers, status chips, expandable detail (optional), mobile timeline list. |
| **Blocked Implementation** | Timeline animation, real-time project tracking, GitHub issue integration, drag-to-reorder phases. |
| **Future Components** | `RoadmapOrbitMap`, `OrbitRing`, `OrbitNode`, `RoadmapPhaseMarker`, `RoadmapTimeline` |
| **Validation Notes** | All 6 phases visible. Blocked/later phase dimmed but not hidden. Runtime phase shows "requires approval." |
| **Safety Notes** | Honest roadmap state. No implied progress beyond actual. Runtime phase explicitly gated. |

### safety-control-layer

| Field | Value |
|---|---|
| **Section ID** | `safety-control-layer` |
| **Name** | Safety / Control Layer |
| **Priority** | P0 — Must have |
| **Purpose** | Make safety architecture visible and prominent. First-class section. |
| **Required Data** | Safety rules list (13 rules), safety badge labels, GLM reference note. All static. |
| **Static/Dynamic** | Static only. |
| **Allowed Implementation** | Safety panel with checklist, safety badges, glass panel with accent border, GLM reference notice. |
| **Blocked Implementation** | Toggleable rules, dismissable badges, fake safety indicators, runtime validation display. |
| **Future Components** | `SafetyControlSection`, `SafetyChecklist`, `SafetyBadgeGroup`, `GlmReferenceNotice` |
| **Validation Notes** | All rules visible. Badges accurate. GLM note explicitly states no files copied. |
| **Safety Notes** | Every badge corresponds to an actually enforced constraint. No fake safety claims. |

### tooling-layer

| Field | Value |
|---|---|
| **Section ID** | `tooling-layer` |
| **Name** | Tooling Layer |
| **Priority** | P1 — High priority |
| **Purpose** | Show controlled developer tool surfaces. |
| **Required Data** | Tool list (8 tools), role descriptions, "controlled" status. All static. |
| **Static/Dynamic** | Static only. |
| **Allowed Implementation** | Card grid (2-4 columns), tool cards with geometric placeholder icons, "controlled" status chips. |
| **Blocked Implementation** | Tool logos (use placeholder initials), "open in tool" buttons, deep links, live tool status. |
| **Future Components** | `ToolingLayerSection`, `ToolCard`, `ToolGrid` |
| **Validation Notes** | All 8 tools present. No "open" buttons. No live status. |
| **Safety Notes** | All tools shown as "controlled." No autonomous execution implied. |

### next-actions

| Field | Value |
|---|---|
| **Section ID** | `next-actions` |
| **Name** | CTA / Next Actions |
| **Priority** | P1 — High priority |
| **Purpose** | Safe navigation to page sections and documentation. |
| **Required Data** | CTA labels and anchor targets. All static. |
| **Static/Dynamic** | Static only. |
| **Allowed Implementation** | Anchor-link button group, glass-styled buttons, responsive layout. |
| **Blocked Implementation** | Form submissions, external redirects, connect-live CTAs, sign-up forms, deploy buttons. |
| **Future Components** | `NextActionsSection`, `CtaButtonGroup` |
| **Validation Notes** | All CTAs are anchor links or documentation links. Zero forbidden CTAs. |
| **Safety Notes** | No system activation implied. No external service connections. |

### footer-status

| Field | Value |
|---|---|
| **Section ID** | `footer-status` |
| **Name** | Footer / Project Status |
| **Priority** | P1 — High priority |
| **Purpose** | Reinforce honest project state. Transparent metadata. |
| **Required Data** | Project name, status label, 5 status confirmations, repo metadata (optional), attribution. All static. |
| **Static/Dynamic** | Static only. |
| **Allowed Implementation** | Glass panel footer, status checklist, HUD label metadata, footer links. |
| **Blocked Implementation** | Dynamic git data fetching, live deployment status, misleading dates, production claims. |
| **Future Components** | `FooterStatusPanel`, `ProjectStatusChecklist`, `FooterLinks` |
| **Validation Notes** | All 5 confirmations present. "GLM not copied" explicit. No production claims. |
| **Safety Notes** | Honest phase representation. No secrets reference. No misleading status. |

---

## Recommended First Static Slice Order

Build in this order for maximum impact and progressive validation:

1. **hero-command-center** — Establishes identity and tone. Build and validate first.
2. **safety-control-layer** — Safety is first-class. Build early to establish trust patterns.
3. **shared-context-memory** — Core coordination concept. Builds on hero narrative.
4. **roadmap-orbit-map** — Shows project state. Validates orbital visual patterns.
5. **agent-constellation** — Multi-agent visualization. Tests constellation/routing patterns.
6. **model-router-panel** — OmniRouter routing. Builds on constellation patterns.
7. **tooling-layer** — Tool surfaces. Reuses card patterns from earlier sections.
8. **next-actions** — CTA group. Simple, quick to build.
9. **footer-status** — Footer. Final section, establishes closing patterns.

---

## Minimum Viable Homepage

For the absolute first deployable slice, these sections are required:

| Section | Reason |
|---|---|
| hero-command-center | Identity, prototype status, first impression |
| safety-control-layer | Safety-first architecture |
| shared-context-memory | Core coordination concept |
| roadmap-orbit-map | Project state visibility |
| footer-status | Honest project state closing |

These 5 sections form a complete narrative: identity, safety, context, roadmap, status.

---

## Nice-to-Have Later Interactions

| Interaction | Section | Priority |
|---|---|---|
| Hover-highlight route lines | agent-constellation | P2 |
| Expandable phase detail | roadmap-orbit-map | P2 |
| Subtle card border brighten on hover | shared-context-memory, tooling-layer | P3 |
| Scroll-triggered section fade-in | all sections | P3 |
| Orbital cube slow rotation | hero-command-center | P3 |
| Constellation node hover detail tooltip | agent-constellation | P3 |
| Router panel hover glow on provider card | model-router-panel | P3 |

---

## Blocked Runtime Features

These features are explicitly blocked until runtime integration phase (which requires explicit human approval):

- Provider API key input forms
- Live provider connection status indicators
- Real-time agent activity dashboards
- Model routing simulation or execution
- File content browsing or download
- GitHub issue/PR integration
- Dynamic project state from git
- Deploy or "go live" workflows
- Trading execution UI from MellyTrade
- Any feature implying live system operation

---

## Visual QA Checklist

Before any deployment, verify:

- [ ] All sections render without JavaScript enabled.
- [ ] No section implies live connectivity.
- [ ] All status indicators include text labels (not color-only).
- [ ] Color contrast meets WCAG AA on all text elements.
- [ ] Glass panels maintain readability through blur layer.
- [ ] Mobile layout stacks correctly without horizontal scroll (test at 375px).
- [ ] Tablet layout adapts correctly (test at 768px and 1024px).
- [ ] Desktop layout fills correctly (test at 1280px and 1920px).
- [ ] No forbidden CTAs present anywhere on the page.
- [ ] No forbidden design patterns from the design system (Section 20).
- [ ] Safety section is prominent, not buried.
- [ ] Prototype status visible in hero and footer.
- [ ] GLM reference note present and accurate.
- [ ] OmniRouter shown as central routing hub in constellation and router sections.
- [ ] All agents shown as "supervised" — no autonomous nodes.
- [ ] Blocked/later roadmap phases visible but dimmed.
- [ ] No secrets, keys, or real values in any displayed content.
- [ ] Text is readable at 200% browser zoom.
- [ ] Reduced motion preference disables all animations.
- [ ] No emoji used as UI icons.
- [ ] No trading/broker UI patterns present.

---

*This implementation brief is designed for future frontend agents. It translates the homepage specification into actionable, prioritized implementation guidance while maintaining safety and static-first constraints.*
