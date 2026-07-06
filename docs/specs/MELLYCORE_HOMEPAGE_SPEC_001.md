# MellyCore AIOS — Homepage Specification

**Task ID:** MELLYCORE-HOMEPAGE-SPEC-001
**Version:** 1.0
**Status:** Complete
**Scope:** Complete homepage section-by-section specification for the MellyCore AIOS command center website

---

## Section 1: Hero — MellyCore AIOS Command Center

### Section Purpose
Establish immediate understanding of what MellyCore AIOS is: a coordinated AI command center that unifies multiple agents, models, and tools under one supervised architecture. Set the prototype tone honestly.

### User Message
"You are looking at the architectural preview of MellyCore AIOS — the shared coordination layer for supervised multi-agent AI. This is not live. This is the blueprint."

### Content / Copy Direction
- **Headline:** "MellyCore AIOS" — large, commanding, cold white with optional orbital violet glow.
- **Subtitle:** "The shared command center for supervised multi-agent AI coordination." One sentence. Clear. No hype.
- **Prototype tag:** "Static Prototype — Docs & Spec Phase" displayed as a HUD label or static preview notice.
- **One-liner:** "One shared context layer. Many supervised agents. OmniRouter at the center."
- **Description paragraph (optional, 2-3 sentences):** MellyCore AIOS coordinates ChatGPT, Claude, Codex, GLM, Grok, and developer tools through a shared context layer, model routing constellation, and safety-first architecture. Currently in documentation and specification phase. No live provider connections.

### Visual Behavior
- Full-viewport hero section with void black background and subtle star field.
- Orbital cube as the primary visual element — static, with soft nebula glow, positioned beside or behind headline text.
- No animation, no pulse, no live-data indicators.
- OmniRouter referenced visually as the central routing anchor in any diagrammatic elements.
- Safety badges visible: "No Secrets Loaded", "Static Preview", "Supervised Only".

### UI Components
- `<CommandCenterShell>` — outer container.
- `<SectionHeaderCluster>` — headline + subtitle + HUD labels.
- `<StaticPreviewNotice>` — prototype status badge.
- `<SafetyBadge>` — 2-3 safety status indicators.
- Orbital cube visual (CSS or static image — no 3D library required in prototype).

### Interaction Notes
- CTAs are anchor links to page sections — no external navigation, no form submissions.
- No hover effects required for comprehension.
- Scroll indicator (subtle down arrow or line) optional.

### Responsive Behavior
- Desktop: headline left, orbital cube right, or headline centered over cube.
- Tablet: headline centered, cube scaled down below.
- Mobile: headline centered, cube hidden or reduced to small decorative element. CTAs stack vertically.

### Safety Notes
- Hero must never imply live connectivity. No "connected" indicators. No pulsing dots.
- All CTAs are safe: navigate to page sections or documentation.
- Prototype status is visible before any CTA.

### Static / Dynamic Guidance
- Entirely static. All content authored in markup.
- No data fetching, no API calls, no dynamic rendering.

### Forbidden CTAs
- "Connect Live", "Add API Key", "Execute", "Deploy Now", "Launch", "Start Trading", "Go Live".

### Allowed CTAs
- "View Roadmap" (anchor to Section 5)
- "Review Context Packet" (anchor to Section 4)
- "Explore Design System" (anchor to design system documentation)

### Future Component Candidates
- `HeroSection`, `OrbitalCubeVisual`, `HeroCtaGroup`, `PrototypeStatusBanner`

### Acceptance Criteria
- [ ] Headline, subtitle, and prototype tag are visible and readable.
- [ ] Orbital cube is present but static.
- [ ] At least 2 safety badges are visible.
- [ ] All CTAs are anchor links to page sections.
- [ ] No forbidden CTAs exist.
- [ ] Hero renders correctly without JavaScript.
- [ ] Mobile layout stacks correctly without horizontal scroll.

---

## Section 2: Agent Constellation

### Section Purpose
Visualize the supervised multi-agent fleet. Show that MellyCore AIOS coordinates many AI agents and tools — not as independent services, but as supervised nodes in a constellation with OmniRouter as the central routing hub.

### User Message
"MellyCore AIOS coordinates multiple AI agents and developer tools through a shared constellation. Every agent is supervised. OmniRouter routes between them."

### Content / Copy Direction
- **Section title:** "Agent Constellation"
- **Subtitle:** "Supervised AI agents and tools coordinated through OmniRouter."
- **Agent nodes:** ChatGPT (strategy, context synthesis, planning), Claude / Claude Code (architecture, reasoning, documentation), Codex (implementation, validation), GLM 5.2 / Z.ai (drafting, iteration, exploration), Grok / xAI (critique, adversarial review), OmniRouter (central routing hub).
- **Tool nodes:** Warp (terminal workflows), Zed (editor-agent workspace), VS Code (editor workspace), GitHub (source control, PRs, review trail).
- **Each node:** Name, 2-3 word role label, status chip ("supervised").

### Visual Behavior
- Constellation diagram: nodes arranged in a radial pattern with OmniRouter at the center.
- Route lines connect each agent node to OmniRouter — not directly to each other.
- OmniRouter node is larger or more prominent — it is the routing hub.
- All agent nodes show "supervised" status chip.
- No animation. Static constellation.

### UI Components
- `<SectionHeaderCluster>` — title + subtitle.
- `<ConstellationNode>` — one per agent/tool (10 nodes).
- `<RouteLine>` — connections through OmniRouter.
- `<StatusChip>` — "supervised" for each node.
- `<HudLabel>` — role labels.

### Interaction Notes
- Hover on node may highlight its route lines (optional, progressive enhancement).
- No click actions required — informational section.
- On mobile, constellation converts to a vertical card list.

### Responsive Behavior
- Desktop: full radial constellation with OmniRouter at center.
- Tablet: simplified constellation (fewer nodes visible, or 2-column layout).
- Mobile: stacked agent cards in a single column. OmniRouter card at top as the routing hub.

### Safety Notes
- Every agent node shows "supervised" — no autonomous agents implied.
- No "running" or "active" status indicators.
- No connection to live provider status.

### Static / Dynamic Guidance
- Entirely static. Node positions and labels are authored in markup/CSS.
- No real-time agent status. No live connectivity indicators.

### Future Component Candidates
- `AgentConstellationSection`, `ConstellationMap`, `AgentCardList` (mobile)

### Acceptance Criteria
- [ ] All 10 agents/tools are represented as nodes.
- [ ] OmniRouter is visually the central hub.
- [ ] All nodes show "supervised" status.
- [ ] Route lines connect to OmniRouter, not directly between agents.
- [ ] Mobile layout converts to card list.
- [ ] No live status indicators present.

---

## Section 3: OmniRouter / Model Router Panel

### Section Purpose
Show model and provider routing at a high architectural level. Communicate that OmniRouter is the preferred gateway for model routing — without implying live connectivity, loaded keys, or active provider sessions.

### User Message
"OmniRouter is the central routing layer. It coordinates which model handles which task. This is an architectural preview — no providers are currently connected."

### Content / Copy Direction
- **Section title:** "Model Router"
- **Subtitle:** "OmniRouter coordinates model and provider routing at the architecture level."
- **HUD label:** "ARCHITECTURE PREVIEW — NO LIVE ROUTING"
- **Provider placeholders:** ChatGPT, Claude, Codex, GLM 5.2, Grok — shown as routing targets, not connected providers.
- **Routing roles:** Each provider shows its routing purpose (strategy, architecture, implementation, drafting, critique).
- **Central hub note:** "OmniRouter serves as the preferred gateway when available. Provider API keys stay outside the repo."

### Visual Behavior
- Control-panel style layout: OmniRouter as central element with provider targets branching outward.
- Provider targets shown as placeholder cards with role labels and "placeholder" status chips.
- No live routing indicators. No "connected" badges. No active data flow visualization.
- Dormant node gray for provider cards — they are architectural placeholders.

### UI Components
- `<SectionHeaderCluster>` — title + subtitle + HUD label.
- `<GlassPanel>` — router panel container.
- `<ConstellationNode>` or `<RouterNode>` — OmniRouter center.
- `<StatusChip>` — "placeholder" for each provider.
- `<HudLabel>` — routing role per provider.

### Interaction Notes
- Informational only. No click actions.
- No provider selection, no routing simulation, no key input.

### Responsive Behavior
- Desktop: radial or horizontal layout with OmniRouter center.
- Tablet: 2-column with OmniRouter spanning top.
- Mobile: vertical stack with OmniRouter card first.

### Safety Notes
- No API key inputs. No provider connection forms. No "add provider" buttons.
- Explicit "no live routing" notice visible.
- Provider keys stated as "outside the repo."

### Static / Dynamic Guidance
- Entirely static. Provider list and roles are authored content.
- No runtime routing. No model selection. No provider health checks.

### Future Component Candidates
- `ModelRouterPanel`, `ProviderPlaceholderCard`, `OmniRouterHub`

### Acceptance Criteria
- [ ] OmniRouter shown as central routing element.
- [ ] All placeholder providers visible with role labels.
- [ ] "No live routing" notice present.
- [ ] No API key inputs or connection forms.
- [ ] All providers show "placeholder" status.

---

## Section 4: Shared Context / Memory Layer

### Section Purpose
Show that MellyCore AIOS uses a unified shared context layer — a set of coordination memory files that all agents read from and write to. This is the "memory" that makes multi-agent coordination possible.

### User Message
"All agents share context through a unified memory layer. These files are the coordination backbone — readable by every agent in the constellation."

### Content / Copy Direction
- **Section title:** "Shared Context / Memory Layer"
- **Subtitle:** "Unified coordination memory that every agent reads from."
- **Memory cards (one per context file):**
  - `shared_context` — The root coordination memory directory.
  - `AGENT_HANDOFF.md` — Cross-agent handoff protocol and state transfer.
  - `RUN_QUEUE.md` — Prioritized task queue for all agents.
  - `SAFETY_CONTRACT.md` — Safety rules: no secrets, no keys, no live execution.
  - `ROADMAP.md` — Project phases: 7-day, 30-day, 90-day, 180-day.
  - `MODEL_ROUTING.md` — Agent roles and OmniRouter routing matrix.
  - `DESIGN_SYSTEM.md` — Visual direction and design constraints.
  - `PROJECT_STATE.md` — Current project status and next tasks.
  - `VALIDATION.md` — Baseline validation commands and checks.
  - `TOOLING.md` — Tool and workspace definitions.
- **HUD label:** "STATIC FILE LIST — NO RUNTIME ACCESS"

### Visual Behavior
- Grid of memory cards (2-3 columns on desktop).
- Each card shows file name, one-line description, and type badge (contract, routing, roadmap, state, validation, tooling).
- Cards use glass panel styling with subtle borders.
- No file contents displayed — only metadata.

### UI Components
- `<SectionHeaderCluster>` — title + subtitle.
- `<MemoryCard>` — one per context file (10 cards).
- `<HudLabel>` — type badge per card.
- `<GlassPanel>` — section container.

### Interaction Notes
- Informational only. No file browsing, no content preview, no download.
- Hover on card may subtly brighten border (optional).

### Responsive Behavior
- Desktop: 3-column grid.
- Tablet: 2-column grid.
- Mobile: single-column stack.

### Safety Notes
- No actual file contents displayed. Only file names and descriptions.
- No secrets, no keys, no real values in any card.
- "Static file list" notice visible.

### Static / Dynamic Guidance
- Entirely static. File metadata is authored in markup.
- No filesystem access. No dynamic file listing.

### Future Component Candidates
- `SharedContextSection`, `MemoryCardGrid`, `ContextFileCard`

### Acceptance Criteria
- [ ] All 10 context files represented as cards.
- [ ] Each card shows file name, description, and type badge.
- [ ] No file contents displayed.
- [ ] "Static file list" notice present.
- [ ] Grid responds correctly to viewport changes.

---

## Section 5: Roadmap Orbit Map

### Section Purpose
Visualize the project roadmap as an orbital system. Show completed phases as inner orbits, future phases as outer orbits, and blocked/deferred phases as dimmed. Honest representation of project state.

### User Message
"The MellyCore AIOS roadmap progresses through phases. Here is where we are — and what comes next."

### Content / Copy Direction
- **Section title:** "Roadmap Orbit Map"
- **Subtitle:** "Project phases as orbital progression."
- **Phases:**
  - **Bootstrap** (inner orbit, complete) — Repo scaffold, shared context files, safety contract.
  - **Cross-agent smoke** (mid orbit, pending) — Verify context works across Codex, Claude, ChatGPT, GLM, Grok, Warp, Zed, VS Code, GitHub. Not yet run; tracked in `shared_context/RUN_QUEUE.md`. No implied progress beyond this pending state.
  - **Context / Roadmap / Safety / Design specs** (mid orbit, active) — Documentation architecture, design system, homepage spec, safety contract.
  - **Static website** (outer orbit, planned) — HTML/CSS prototype of command center homepage.
  - **MVP demo** (outer orbit, planned) — Interactive prototype with navigation and visual polish.
  - **Runtime / Provider integrations** (outermost orbit, blocked/later) — Live provider routing, API integration, runtime orchestration. Explicitly marked "later — requires explicit approval."
- **HUD label:** "STATIC ROADMAP — UPDATED MANUALLY"

### Visual Behavior
- Concentric orbital rings with phase markers.
- Inner rings (complete): safe status green accents.
- Mid rings (active): plasma blue accents.
- Outer rings (planned): muted lavender accents.
- Outermost ring (blocked/later): dormant node gray, amber "later" badge.
- Current phase highlighted with slightly brighter glow.

### UI Components
- `<SectionHeaderCluster>` — title + subtitle.
- `<OrbitNode>` — one per phase (6 phases).
- `<StatusChip>` — complete, active, planned, blocked/later.
- `<RoadmapPhaseMarker>` — expandable phase detail (optional).
- `<HudLabel>` — "STATIC ROADMAP" notice.

### Interaction Notes
- Click/hover on phase marker may show expandable detail (optional progressive enhancement).
- No timeline animation. Static orbital positions.

### Responsive Behavior
- Desktop: full radial orbit map.
- Tablet: simplified orbit (fewer rings visible, or semi-circular layout).
- Mobile: vertical timeline list. Each phase is a list item with status chip.

### Safety Notes
- Blocked/later phases are visible and honestly labeled — not hidden.
- Runtime phase explicitly notes "requires explicit approval before activation."
- No implied progress beyond actual state.

### Static / Dynamic Guidance
- Entirely static. Phase data authored in markup.
- No real-time project tracking. No integration with GitHub issues or project boards.

### Future Component Candidates
- `RoadmapOrbitMap`, `OrbitRing`, `PhaseMarkerDetail`, `RoadmapTimeline` (mobile)

### Acceptance Criteria
- [ ] All 6 phases visible with correct status.
- [ ] Inner orbits = complete, outer = future, outermost = blocked/later.
- [ ] Blocked/later phase is dimmed but visible.
- [ ] Runtime phase shows "requires explicit approval" note.
- [ ] Mobile converts to vertical timeline.

---

## Section 6: Safety / Control Layer

### Section Purpose
Make the safety architecture visible and prominent. This is not a legal footer — it is a first-class section showing that MellyCore AIOS has explicit, documented safety constraints.

### User Message
"MellyCore AIOS has explicit safety constraints. No secrets, no keys, no live execution, no copied workspaces. Safety is architectural, not decorative."

### Content / Copy Direction
- **Section title:** "Safety / Control Layer"
- **Subtitle:** "Explicit safety constraints, visible at every layer."
- **Safety rules (displayed as safety badges or panel items):**
  - No secrets in the repository.
  - No real API keys committed.
  - No provider tokens in tracked files.
  - No `.env` values in version control.
  - No destructive git operations without explicit approval.
  - No deploy without explicit approval.
  - No MellyTrade mutation from MellyCore AIOS.
  - No wholesale import of the GLM workspace — reference only.
  - No `.git` import from reference workspaces.
  - No database files committed.
  - No local runtime state committed.
  - Static-first before any runtime integration.
  - Honest validation — no fake live status indicators.
- **GLM reference note:** "The GLM/Z.ai workspace is reference only. No GLM files have been copied into this repository. Visual inspiration is acknowledged; wholesale import is forbidden."
- **HUD label:** "SAFETY CONTRACT ACTIVE — ALL RULES ENFORCED"

### Visual Behavior
- Safety panel with prominent green/cyan accents.
- Each rule displayed as a checklist item with check icon and label.
- Safety badges for key constraints ("No Secrets", "No Keys", "No Live Execution", "No Copied Workspace").
- Panel uses glass panel styling with slightly brighter border to draw attention.

### UI Components
- `<SectionHeaderCluster>` — title + subtitle.
- `<GlassPanel>` — safety panel container with accent border.
- `<SafetyBadge>` — 4 primary safety badges.
- Safety checklist items (styled list with check icons).
- `<HudLabel>` — "SAFETY CONTRACT ACTIVE" notice.
- `<StaticPreviewNotice>` — "No live status indicators" confirmation.

### Interaction Notes
- Informational only. No toggle, no dismiss, no edit.
- Safety rules are always visible — not collapsible.

### Responsive Behavior
- Desktop: 2-column checklist or single panel with badges above.
- Tablet: single column checklist.
- Mobile: single column, badges stack vertically.

### Safety Notes
- This section IS the safety section. It must be accurate and honest.
- If any safety rule is violated in the actual repo, this section must reflect that honestly.
- No fake safety badges — every badge must correspond to an actually enforced constraint.

### Static / Dynamic Guidance
- Entirely static. Safety rules are authored in markup.
- No runtime safety checking. No live validation display.

### Future Component Candidates
- `SafetyControlSection`, `SafetyChecklist`, `SafetyBadgeGroup`, `GlmReferenceNotice`

### Acceptance Criteria
- [ ] All safety rules visible as checklist items.
- [ ] At least 4 safety badges present.
- [ ] GLM reference note explicitly states no files copied.
- [ ] No fake safety indicators.
- [ ] Section is prominent — not buried in footer.

---

## Section 7: Tooling Layer

### Section Purpose
Show the developer tools and surfaces that MellyCore AIOS coordinates with. These are controlled workflow surfaces — not autonomous agents, not live integrations.

### User Message
"MellyCore AIOS works with established developer tools as controlled workflow surfaces. Each tool has a defined role in the coordination architecture."

### Content / Copy Direction
- **Section title:** "Tooling Layer"
- **Subtitle:** "Controlled workflow surfaces for the multi-agent architecture."
- **Tool cards:**
  - **Warp** — Safe terminal workflows, operator prompts, repeatable runbooks.
  - **Zed** — Editor-agent workspace, fast code navigation, local editing ergonomics.
  - **VS Code** — Broadly compatible editor workspace, settings examples, extension-compatible docs.
  - **GitHub** — Remote source control, issues, PRs, review trail, collaboration history.
  - **Claude Code** — Architecture, reasoning, documentation, review workflows.
  - **Codex** — Implementation, validation, local git hygiene, PR preparation.
  - **GLM 5.2** — Drafting, iteration, exploration, reference implementation ideas.
  - **ChatGPT** — Strategy, context synthesis, prompt generation, planning, memory.
- **HUD label:** "CONTROLLED SURFACES — NO AUTONOMOUS EXECUTION"

### Visual Behavior
- Card grid (2-4 columns on desktop).
- Each card shows tool name, role description, and "controlled" status chip.
- Cards use glass panel styling.
- No tool logos in prototype — geometric placeholder icons with initials.

### UI Components
- `<SectionHeaderCluster>` — title + subtitle.
- `<GlassPanel>` — section container.
- Tool cards (reusing `<MemoryCard>` or dedicated `<ToolCard>` primitive).
- `<StatusChip>` — "controlled" per tool.
- `<HudLabel>` — "CONTROLLED SURFACES" notice.

### Interaction Notes
- Informational only. No tool launching, no configuration, no linking.

### Responsive Behavior
- Desktop: 4-column grid.
- Tablet: 2-column grid.
- Mobile: single-column stack.

### Safety Notes
- All tools shown as "controlled" — no autonomous execution implied.
- No "open in [tool]" buttons. No deep links to tool instances.
- No live tool status indicators.

### Static / Dynamic Guidance
- Entirely static. Tool metadata authored in markup.
- No tool detection, no IDE integration, no live status.

### Future Component Candidates
- `ToolingLayerSection`, `ToolCard`, `ToolGrid`

### Acceptance Criteria
- [ ] All 8 tools represented as cards.
- [ ] Each card shows name, role, and "controlled" status.
- [ ] No "open" or "launch" buttons.
- [ ] No live tool status indicators.

---

## Section 8: CTA / Next Actions

### Section Purpose
Provide clear, safe next actions for the user. All CTAs navigate within the page or to documentation — no external services, no forms, no live actions.

### User Message
"Here is what you can explore next — all within this architectural preview."

### Content / Copy Direction
- **Section title:** "Next Actions"
- **Subtitle:** "Explore the MellyCore AIOS architecture."
- **CTA buttons (safe only):**
  - "View Roadmap" — anchor to Section 5.
  - "Review Context Packet" — anchor to Section 4.
  - "Explore Design System" — anchor to design system documentation.
  - "Review Safety Contract" — anchor to Section 6.
  - "View Agent Constellation" — anchor to Section 2.

### Visual Behavior
- Compact section with centered or left-aligned CTA group.
- Buttons use glass panel styling with orbital violet border on hover.
- No aggressive styling — CTAs are calm, inviting, not pushy.

### UI Components
- `<SectionHeaderCluster>` — title + subtitle.
- CTA button group (styled buttons, not `<CtaButton>` primitive — simple anchor elements).

### Forbidden CTAs
- "Connect Live", "Add API Key", "Execute", "Deploy Now", "Launch", "Start Trading", "Sign Up", "Get Started Free".

### Responsive Behavior
- Desktop: horizontal button row.
- Tablet: 2-column button grid.
- Mobile: vertical button stack.

### Safety Notes
- Every CTA is an anchor link or documentation link.
- No form submissions. No external service redirects.
- No CTAs that imply system activation.

### Acceptance Criteria
- [ ] At least 4 safe CTAs present.
- [ ] Zero forbidden CTAs.
- [ ] All CTAs are anchor links or documentation links.
- [ ] No form elements present.

---

## Section 9: Footer / Project Status

### Section Purpose
Reinforce project state honestly. Confirm that this is a prototype in documentation phase. Provide transparent project metadata.

### User Message
"This project is in documentation and specification phase. No live connections, no secrets, no runtime. Here is the honest project state."

### Content / Copy Direction
- **Project name:** MellyCore AIOS
- **Status:** "Prototype — Docs & Spec Phase"
- **Status confirmations:**
  - "No live provider connections."
  - "No secrets or API keys loaded."
  - "No runtime code in this repository."
  - "GLM reference workspace not copied."
  - "Static preview planned — not yet deployed."
- **Repo info:** Branch name (if available), last commit date (if available), or "Static content" if no git data.
- **Links:** Link to shared context files (if published), link to design system doc.
- **Copyright/attribution:** "MellyCore AIOS — MellyGenix AI Coordination Layer"

### Visual Behavior
- Footer status panel with glass panel styling.
- Status confirmations as a compact checklist (smaller than Section 6 safety panel).
- Muted colors — footer is informational, not attention-grabbing.
- Project metadata in HUD label style.

### UI Components
- `<GlassPanel>` — footer container.
- `<StatusChip>` — "Prototype" status.
- Status checklist (compact).
- `<HudLabel>` — project metadata labels.
- Footer links (simple anchor elements).

### Interaction Notes
- Informational only. Links navigate to documentation or page sections.

### Responsive Behavior
- Desktop: 2-column footer (status left, links right).
- Tablet: stacked.
- Mobile: single column, compact.

### Safety Notes
- Footer honestly states project phase.
- "GLM reference not copied" explicitly confirmed.
- No misleading copyright dates or production claims.

### Static / Dynamic Guidance
- Entirely static. Footer content authored in markup.
- No dynamic git data fetching in prototype.

### Future Component Candidates
- `FooterStatusPanel`, `ProjectStatusChecklist`, `FooterLinks`

### Acceptance Criteria
- [ ] Project name and status visible.
- [ ] All 5 status confirmations present.
- [ ] "GLM reference not copied" explicitly stated.
- [ ] No misleading production claims.
- [ ] Footer renders correctly without JavaScript.

---

*This homepage specification defines the complete section-by-section architecture for the MellyCore AIOS command center website. All sections are designed for static-first implementation with progressive enhancement for future interactivity.*
