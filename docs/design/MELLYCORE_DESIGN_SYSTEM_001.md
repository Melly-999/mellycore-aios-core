# MellyCore AIOS — Design System Specification

**Task ID:** MELLYCORE-DESIGN-SYSTEM-001
**Version:** 1.0
**Status:** Complete
**Scope:** Visual and UX design system for the MellyCore AIOS command center website

---

## 1. Project Identity

MellyCore AIOS is the central coordination layer for all MellyGenix AI products. It is not a trading platform, not a standalone SaaS, and not a MellyTrade frontend. It is the **AI command center** — the shared context, routing, safety, and orchestration backbone that unifies MellyTrade (trading intelligence) and MellyGenix (generative AI products) under one supervised multi-agent architecture.

**Visual feeling:** Cinematic deep-space command center. Intelligent, calm, powerful. The user should feel like they are looking at the nerve center of a coordinated AI fleet — not a dashboard, not a trading terminal, not a crypto hype page.

**Difference from MellyTrade:** MellyTrade is one product that runs *through* MellyCore AIOS. The design system must never imply trading execution, PnL displays, buy/sell controls, or broker connectivity. MellyCore AIOS coordinates agents and models; MellyTrade consumes that coordination.

**Connection to AI workspace / Life OS / command center direction:** The website communicates that MellyCore AIOS is the shared brain — context, memory, safety contracts, model routing, and roadmap — that every agent and product reads from. It is the Life OS for AI agents.

**Prototype honesty:** Every surface must honestly communicate that this is currently a **static prototype / preview**. No live provider connections are implied. No real-time data flows are suggested. The command center is architectural documentation made visual — a blueprint you can walk through, not a live system you can operate.

---

## 2. Product Story

The central narrative of MellyCore AIOS, expressed through design:

- **One shared context layer.** Every agent — ChatGPT, Claude, Codex, GLM, Grok — reads from and writes to the same `shared_context/` files. Context is not siloed per agent; it is unified.
- **Many supervised AI agents.** No agent runs autonomously. Every action is reviewed, approved, or gated by a human operator. The design communicates supervision, not autonomy.
- **OmniRouter as the central routing constellation.** Model and provider routing flows through OmniRouter as the preferred gateway. The constellation visualization shows providers as nodes coordinated through a central hub — not independent services.
- **Roadmap as orbit system.** Project phases orbit the core. Completed phases are inner orbits. Future phases are outer orbits. Blocked or deferred phases are visually distinct (dimmed, labeled "later").
- **Safety as control layer.** Safety is not a footer note — it is a first-class visual layer. The safety contract, the absence of secrets, the static-first posture, and the explicit-approval-before-runtime rule are all visible and prominent.
- **Static-first preview before runtime.** The website is a design artifact first. Runtime integration comes later. The design never implies live connectivity.

---

## 3. Brand Feeling

The visual identity of MellyCore AIOS is:

| Attribute | Expression |
|---|---|
| Cinematic | Deep-space backgrounds, subtle star fields, nebula gradients |
| Intelligent | Clean typography, structured layouts, clear hierarchy |
| Calm but powerful | Restrained glow, measured animation, no visual noise |
| Orbital | Circular/radial layouts for roadmap and agent relationships |
| Neon | Violet, blue, and cyan accents — never garish, always purposeful |
| Glass | Glassmorphism panels with controlled blur and border intensity |
| Deep-space | Void-black backgrounds, not flat gray |
| Technical | HUD-style labels, monospace data, grid overlays |
| Premium | Generous spacing, considered details, no clutter |
| Focused | One clear message per section, no competing visual priorities |
| Trustworthy | Honest status labels, no fake live indicators |
| Safety-first | Safety badges, contract visibility, no-secret confirmation |
| Controlled | Supervised agent nodes, approval gates, no autonomous execution implied |

---

## 4. First-Five-Seconds Impression

Within five seconds of loading, a user must understand:

1. **This is an AI command center.** Not a trading app, not a crypto dashboard, not a generic AI landing page.
2. **It coordinates agents, tools, and models.** Multiple AI agents work together through a shared context and routing layer.
3. **It is currently a prototype / static preview.** No live data, no real-time connections, no active provider integrations.
4. **No live provider connection is implied.** The design does not suggest that API keys are loaded, providers are connected, or models are responding.
5. **Safety and context are first-class.** This is not an afterthought — safety is architecturally central.

**Achieved through:** Hero copy that states "prototype" explicitly, static orbital cube (no live-pulse animation), status badges showing "docs/spec phase," and absence of any live-data indicators or connect-live CTAs.

---

## 5. Visual Principles

1. **Clarity before effects.** Every visual effect must serve communication. If a glow, blur, or animation does not clarify meaning, remove it.
2. **Safety/status visible before action.** Status chips, safety badges, and prototype notices appear before any interactive element.
3. **No fake live connectivity.** No pulsing dots, no "connected" indicators, no real-time counters, no simulated data streams.
4. **Static prototype honesty.** Every section that could be misread as "live" must include a visual or textual cue that it is static/architectural.
5. **One command center, many agents.** Layouts show coordination and hierarchy, not isolated agent cards.
6. **OmniRouter as constellation hub.** Model routing is visualized as a constellation with OmniRouter at the center — providers as orbiting nodes, not independent panels.
7. **Roadmap as orbit system.** Phases are concentric orbits, not a linear timeline. Inner = done, outer = future, dimmed = blocked/deferred.
8. **Context as memory layer.** Shared context is visualized as a persistent memory substrate that all agents read from.
9. **Cinematic but readable.** Deep-space aesthetics must never compromise text legibility or navigation clarity.
10. **Premium but not noisy.** Generous whitespace, restrained effects, no visual overload.

---

## 6. Color Language

All color names are descriptive design tokens. No CSS variables are defined here — these are semantic color definitions for future implementation.

| Color Name | Description | Intended Use | Emotional Meaning | Accessibility Note | Misuse Warning |
|---|---|---|---|---|---|
| **Void Black** | Near-absolute black (#050508 range) | Primary background, deep-space canvas | Depth, seriousness, technical authority | Ensure text on void black meets 4.5:1 contrast | Never use pure #000000 — slight warmth prevents dead-flat appearance |
| **Deep Space Black** | Very dark blue-black (#0A0B14 range) | Secondary background, panel backgrounds | Space, expanse, calm power | Maintain contrast with light text | Do not use for text — background only |
| **Orbital Violet** | Rich violet (#7C3AED range) | Primary accent, hero glow, active orbit rings | Intelligence, premium tech, creative energy | Test against both void and deep-space backgrounds | Do not use for body text — accent only |
| **Plasma Blue** | Electric blue (#3B82F6 range) | Secondary accent, route lines, active nodes | Technology, connectivity, data flow | Ensure 3:1 ratio for UI components | Never use for large fills — line and accent only |
| **Signal Cyan** | Bright cyan (#06B6D4 range) | Status indicators, HUD labels, constellation connectors | Clarity, signal, precision | High contrast on dark backgrounds | Avoid for body text — too bright for long reading |
| **Nebula Purple** | Soft purple gradient (#4C1D95 to #7C3AED) | Background gradients, nebula effects, orbit fills | Mystery, depth, cosmic atmosphere | Gradient must not reduce text readability | Never use as solid fill for interactive elements |
| **Cold White** | Off-white with slight blue (#E2E8F0 range) | Primary body text, headings | Clarity, readability, technical precision | Meets 7:1+ contrast on dark backgrounds | Never use pure #FFFFFF — slight cool tint reduces eye strain |
| **Muted Lavender** | Soft lavender (#C4B5FD range) | Secondary text, labels, captions | Gentleness, accessibility, approachability | Must meet 4.5:1 on dark backgrounds | Do not use for critical status information |
| **Soft Warning Amber** | Warm amber (#F59E0B range) | Caution states, blocked phases, pending items | Attention without alarm | Ensure visibility on dark backgrounds | Never use for error states — amber is caution, not failure |
| **Safe Status Green** | Muted green (#10B981 range) | Completed phases, confirmed states, safety confirmations | Safety, completion, approval | Test on dark backgrounds | Do not use as the sole indicator — pair with label/icon |
| **Glass Panel Surface** | Semi-transparent white (8-12% opacity) | Glass panel backgrounds, card surfaces | Modernity, layering, depth | Requires backdrop-blur and border for definition | Never use without border — invisible on dark backgrounds |
| **Command Center Border** | Subtle violet-white (15-20% opacity) | Panel borders, card edges, glass frames | Structure, containment, precision | Must be visible against void black | Do not use high-opacity borders — defeats glassmorphism |
| **Soft Nebula Glow** | Diffused violet/blue radial gradient | Background atmosphere, hero glow halos | Atmosphere, immersion, cosmic scale | Must not reduce foreground text contrast | Limit to 2-3 instances per viewport — visual noise risk |
| **Dormant Node Gray** | Muted gray (#6B7280 range) | Inactive agents, deferred phases, disabled states | Inactivity, waiting, dormancy | Must still be readable as label text | Do not use for error or warning states |
| **Active Route Blue** | Bright saturated blue (#2563EB range) | Active routing paths, selected constellation nodes | Active coordination, data flow, routing | High visibility on dark backgrounds | Reserve for truly active states — overuse dilutes meaning |

---

## 7. Typography Guidance

**Preferred feeling:** Technical precision meets cinematic confidence. Typography should feel like a well-designed HUD — clean, authoritative, readable at a glance.

**Style guidance by context:**

| Context | Style Direction | Weight | Size Guidance |
|---|---|---|---|
| **Headlines** | Bold, uppercase or title-case, slightly condensed | 700-800 | Large, commanding — hero headlines fill approximately 60% width on desktop |
| **Body text** | Clean sans-serif, generous line-height (1.6-1.8) | 400-500 | 16-18px base, never below 14px |
| **HUD labels** | Uppercase, letter-spaced (0.05-0.1em), monospace or condensed sans | 500-600 | 11-13px, but never below 11px even on mobile |
| **Code / technical** | Monospace, relaxed line-height | 400 | 14-15px, with syntax-aware color |
| **Navigation** | Clean sans-serif, medium weight, moderate letter-spacing | 500 | 14-16px |
| **Status labels** | Uppercase, condensed, tight letter-spacing | 600 | 10-12px minimum |
| **Captions** | Light weight, generous spacing | 300-400 | 13-14px |

**Readability rules:**
- Maximum body text width: 65-72 characters per line.
- Headlines: no more than 2 lines before breaking or truncating.
- HUD labels must remain legible at 100% zoom on a 1366px viewport.
- Never place light text on glass panels without verifying contrast through the blur layer.

**Future font suggestions (no files, no licensing):**
- Headlines: Inter, Space Grotesk, or similar geometric sans-serif.
- Body: Inter, IBM Plex Sans, or similar high-readability sans-serif.
- Monospace: JetBrains Mono, IBM Plex Mono, or similar clean monospace.
- HUD labels: Space Mono, Share Tech Mono, or similar technical display mono.

**Mobile constraints:**
- Headlines scale down to 75% of desktop size, never below 24px.
- Body text never below 16px on mobile.
- HUD labels may be hidden on mobile if they become unreadable — content over decoration.

---

## 8. Layout and Spacing Rhythm

**Desktop (1280px and above):**
- Full command-center layout: hero spans full width, sections stack vertically with generous breathing room.
- Max content width: 1200-1280px, centered.
- Section vertical rhythm: 120-160px between major sections.
- Card grids: 2-3 columns with 24-32px gutters.
- HUD clusters: tight internal spacing (8-12px) but generous external margin (32-48px).

**Tablet (768-1279px):**
- Panels stack to 2-column or single-column layouts.
- Section spacing reduced to 80-120px.
- Constellation and orbit maps simplify — reduce node count or switch to list layout.
- Glass panels increase padding for touch-friendly interaction zones.

**Mobile (767px and below):**
- Single column, full-width panels.
- Section spacing: 64-80px.
- Orbit maps convert to vertical lists.
- Constellation converts to stacked agent cards.
- HUD density reduced — show essential labels only, collapse secondary data.
- No decorative text that becomes unreadable at small sizes.

**Spacing rhythm:**
- Base unit: 8px.
- All spacing values are multiples of 8 (8, 16, 24, 32, 48, 64, 80, 96, 120, 160).
- Card internal padding: 24-32px.
- Card-to-card gap: 24px.
- Section header to first content: 32-48px.

**Visual hierarchy:**
- Each section has one primary message — do not compete with it.
- Use size, weight, and color to establish reading order — not position alone.
- Avoid dashboard clutter: if a section has more than 6-8 visible elements, consider progressive disclosure.

---

## 9. Reusable Design Primitives

### Command Center Shell
- **Purpose:** The outermost layout container that frames the entire page as a "command center."
- **Visual behavior:** Full-viewport dark background with subtle star field, containing all sections as nested panels.
- **Content rules:** Contains section containers, navigation, and footer. Never contains interactive controls directly.
- **Future component:** `<CommandCenterShell>`
- **Safety/UX:** Must not imply live system status. Background is atmospheric, not operational.

### Glass Panel
- **Purpose:** Primary content container for all section content.
- **Visual behavior:** Semi-transparent background (8-12% white), backdrop-blur, subtle border (15-20% violet-white), optional soft shadow.
- **Content rules:** Contains text, cards, HUD clusters, or orbit visualizations. Never raw background content.
- **Future component:** `<GlassPanel>`
- **Safety/UX:** Must maintain text contrast through blur layer. Test on all background variants.

### HUD Label
- **Purpose:** Small technical label for status, categorization, or metadata.
- **Visual behavior:** Uppercase, letter-spaced, monospace or condensed font, signal cyan or muted lavender color, optional subtle border.
- **Content rules:** Max 2-3 words. No sentences. No paragraphs.
- **Future component:** `<HudLabel>`
- **Safety/UX:** Never below 11px. Must be readable without hover. No information conveyed by color alone.

### Status Chip
- **Purpose:** Compact indicator showing phase status (complete, active, blocked, deferred).
- **Visual behavior:** Rounded pill shape, color-coded (green=complete, blue=active, amber=blocked, gray=deferred), with text label.
- **Content rules:** One word or short phrase. Always pair color with text — never color-only.
- **Future component:** `<StatusChip>`
- **Safety/UX:** Must include text label for accessibility. Color is supplementary, not primary.

### Orbit Node
- **Purpose:** Circular element representing a roadmap phase in the orbit map.
- **Visual behavior:** Circular or elliptical marker on an orbital ring, with phase label and status chip. Inner orbits = completed, outer = future.
- **Content rules:** Phase name, status, optional date range.
- **Future component:** `<OrbitNode>`
- **Safety/UX:** Blocked/deferred phases must be visually dimmed, not hidden. Honest representation of project state.

### Route Line
- **Purpose:** Visual connection between constellation nodes showing routing relationships.
- **Visual behavior:** Thin line (1-2px) with optional glow, connecting provider nodes through OmniRouter hub. Active routes brighter, dormant routes dimmed.
- **Content rules:** Lines only — no labels on lines. Labels belong on nodes.
- **Future component:** `<RouteLine>`
- **Safety/UX:** Must not animate to imply live data flow. Static lines only in prototype phase.

### Constellation Node
- **Purpose:** Represents an AI agent or provider in the agent constellation visualization.
- **Visual behavior:** Circular or hexagonal marker with agent icon/name, connected via route lines through OmniRouter. Size indicates role importance.
- **Content rules:** Agent name, role label, status chip.
- **Future component:** `<ConstellationNode>`
- **Safety/UX:** All agents shown as "supervised" — no node should appear autonomous. OmniRouter is the central hub connecting all nodes.

### Memory Card
- **Purpose:** Represents a shared context file or memory artifact.
- **Visual behavior:** Glass panel card with file name, description, and type label. Subtle icon indicating content type (contract, routing, roadmap, etc.).
- **Content rules:** File name, one-line description, type badge.
- **Future component:** `<MemoryCard>`
- **Safety/UX:** Must not display actual file contents — only metadata. No secrets, no keys, no real values.

### Safety Badge
- **Purpose:** Prominent indicator that safety constraints are active and verified.
- **Visual behavior:** Shield or lock icon with label ("No Secrets", "Static Preview", "Supervised Only"), green or cyan accent.
- **Content rules:** Short label only. No paragraphs.
- **Future component:** `<SafetyBadge>`
- **Safety/UX:** Must be accurate — never display a safety badge for a constraint that is not actually enforced.

### Roadmap Phase Marker
- **Purpose:** Detailed marker for a specific roadmap phase within the orbit map.
- **Visual behavior:** Combines orbit node with expandable detail panel. Shows phase name, status, key deliverables, and blocked/later state.
- **Content rules:** Phase name, status chip, 2-4 bullet deliverables, dependency notes.
- **Future component:** `<RoadmapPhaseMarker>`
- **Safety/UX:** Blocked and deferred phases are visible, not hidden. Honest roadmap representation.

### Static Preview Notice
- **Purpose:** Explicit notice that a section or the entire page is a static prototype.
- **Visual behavior:** Subtle banner or badge with "Static Preview" or "Prototype — No Live Data" text. Muted amber or lavender.
- **Content rules:** Short, clear statement. No ambiguity.
- **Future component:** `<StaticPreviewNotice>`
- **Safety/UX:** Must appear in hero and any section that could be misread as live. Non-dismissable.

### Section Header Cluster
- **Purpose:** Standardized section heading with title, subtitle, and optional HUD labels.
- **Visual behavior:** Large headline (left-aligned or centered), subtitle below, optional HUD label row above or beside.
- **Content rules:** Title (2-5 words), subtitle (1 sentence max), 1-3 HUD labels.
- **Future component:** `<SectionHeaderCluster>`
- **Safety/UX:** Subtitle should clarify section scope and static/dynamic status.

---

## 10. Surfaces and Panels

| Surface | Description | Content |
|---|---|---|
| **Glass Panel** | Primary content container with blur and border | Text, cards, HUD clusters, visualizations |
| **HUD Panel** | Compact technical panel with dense label layout | Status data, metadata, configuration summaries |
| **Card** | Individual content unit within a grid or list | Agent info, memory files, tool descriptions |
| **Orbit Node** | Circular roadmap phase marker on orbital ring | Phase name, status, deliverables |
| **Status Chip** | Compact color-coded status indicator | Phase/agent status: complete, active, blocked, deferred |
| **Command Bar** | Top navigation or action bar | Navigation links, project status, safety badges |
| **Route Panel** | Visualization panel for model/provider routing | Constellation diagram with OmniRouter as hub |
| **Safety Panel** | Dedicated panel for safety contract visibility | Contract rules, verification status, no-secrets confirmation |
| **Roadmap Node** | Expanded roadmap phase detail | Phase description, deliverables, dependencies |
| **Footer Status Panel** | Footer area showing project-wide status | Project phase, repo state summary, static preview confirmation |

---

## 11. Glassmorphism Rules

**When to use blur:**
- Glass panels containing primary content.
- Cards within a grid that need visual separation from the star field background.
- Navigation bar if it overlays content.

**When NOT to use blur:**
- Small elements (status chips, HUD labels, buttons) — blur adds no value at small scale.
- Text-heavy sections where blur reduces readability.
- Mobile viewports below 768px — prefer solid semi-transparent backgrounds over backdrop-blur for performance.

**Border intensity:**
- Glass panel borders: 15-20% opacity white/violet. Visible but not dominant.
- Card borders: 10-15% opacity. Subtle containment, not heavy framing.
- Never use fully opaque borders on glass elements — defeats the transparency effect.

**Shadow and glow limits:**
- Maximum one shadow per glass panel: subtle violet-tinted, 20-40px spread, 10-15% opacity.
- Maximum one glow per section hero element.
- Never stack shadow + glow on the same element unless it is the singular hero focal point.

**Text contrast requirements:**
- All text on glass panels must meet WCAG AA (4.5:1 for body, 3:1 for large text).
- Test contrast through the blur layer — the backdrop content affects perceived contrast.
- When in doubt, increase glass panel background opacity rather than increasing text weight.

**Accessibility limits:**
- Users with vestibular disorders may be affected by layered transparency. Provide a reduced-transparency option in future.
- Never rely on glass transparency to convey state — always pair with label or icon.

**Mobile performance caution:**
- `backdrop-filter: blur()` is expensive on mobile GPUs. On mobile, prefer solid semi-transparent backgrounds.
- Limit glass panels to 3-4 per viewport on mobile.

---

## 12. Neon Glow Rules

**When to use violet glow:**
- Hero element (orbital cube, main headline underline).
- Active orbit ring or selected constellation node.
- Primary CTA button hover/focus state.

**When to use blue glow:**
- Route lines between constellation nodes.
- Active routing path indicators (static, not animated).
- Secondary interactive element hover states.

**When to use cyan glow:**
- HUD label emphasis (sparingly).
- Status indicator accent.
- Constellation connector highlight on hover.

**Avoiding visual noise:**
- Maximum 2-3 glowing elements per viewport.
- Glow intensity: subtle (10-20% opacity, 20-40px spread). Never blinding.
- Never apply glow to body text, navigation links, or background elements.
- Glow must not replace readable contrast — text must be readable with glow disabled.

**Hover/focus guidance:**
- Hover glow should appear within 150ms, fade out within 300ms.
- Focus glow must be clearly visible for keyboard navigation.
- Glow on hover must not shift layout or cause reflow.

**Reduced motion fallback:**
- When `prefers-reduced-motion` is active, replace glow transitions with instant state changes.
- Glow itself is acceptable under reduced motion — only the transition animation is removed.

**Glow must not replace readable contrast:**
- Every element with glow must be fully readable if the glow is removed.
- Test readability with glow effects disabled globally.

---

## 13. Background / Starfield Guidance

**Black-space background:**
- Primary background is void black to deep space black. Not flat gray, not white, not gradient-heavy.
- The background should feel like looking into deep space — vast, calm, technical.

**Subtle star field:**
- Small, dim, scattered points of light. Not dense, not animated in prototype phase.
- Star density: sparse (50-100 visible points per 1920x1080 viewport).
- Star brightness: 10-30% white opacity. Never competing with foreground content.
- Implementation note: CSS radial-gradient or small canvas — avoid heavy particle systems.

**Orbital grid:**
- Optional faint grid overlay (5-8% opacity) in hero or orbit map sections.
- Grid lines should suggest structure and precision, not create visual noise.
- Grid fades at section edges — never hard-edged.

**Gradient nebula:**
- Soft radial gradients in nebula purple/orbital violet, placed behind glass panels.
- Limit to 1-2 nebula gradients per viewport.
- Nebula must not reduce glass panel text readability.

**Avoid heavy animated backgrounds:**
- No particle systems, no moving star fields, no animated nebula in prototype phase.
- Background is static-first. Motion is a future enhancement.

**Static-first:**
- All background elements render correctly without JavaScript.
- CSS-only backgrounds preferred for initial implementation.

**Future motion notes:**
- If animation is added later: slow parallax (0.5-2px per scroll unit), gentle star twinkle (opacity oscillation over 5-10s cycles), no fast movement.
- All background motion must respect `prefers-reduced-motion`.

---

## 14. Orbital Cube Guidance

**Hero role:**
- The orbital cube is the central visual metaphor in the hero section. It represents MellyCore AIOS as the shared coordination core — the object around which all agents, models, and products orbit.

**Symbolic meaning:**
- The cube represents structure, stability, and architectural foundation.
- "Orbital" implies that other elements (agents, providers, products) revolve around this core.
- It is not a product logo — it is a conceptual visualization of the shared context layer.

**Static fallback:**
- In prototype phase, the cube is a static 3D render or CSS illustration.
- It must look complete and intentional without animation.
- A static cube with subtle glow is the target — not a spinning, pulsing, or interactive cube.

**Animation later only:**
- Slow rotation (30-60s per revolution) may be added in future.
- Gentle glow pulse (5-10s cycle) may be added.
- No rapid spinning, no user-interaction-driven rotation in prototype.

**Not distracting from copy:**
- The cube is positioned alongside or behind the hero headline — not in front of it.
- Hero text must be readable even if the cube is removed entirely.
- The cube enhances atmosphere; it does not carry information.

**Relation to shared context / model routing:**
- The cube can be thought of as the `shared_context/` layer made visual — the persistent memory that all agents orbit around.
- OmniRouter constellation visualization can reference the cube as its central anchor point.

---

## 15. Iconography Direction

**Geometric icons:**
- Clean, geometric line icons with consistent stroke weight (1.5-2px).
- Rounded corners on geometric shapes (2-4px radius).
- Icons should feel technical and precise, not playful or cartoon-like.

**Small line icons:**
- 16-24px for inline icons, 32-48px for feature icons.
- Consistent optical sizing within each context.

**Agent nodes:**
- Each agent in the constellation may have a distinctive geometric icon or letterform monogram.
- Avoid using official brand logos in prototype — use placeholder geometric markers with agent initials.

**Routing paths:**
- Route lines use simple straight or gently curved paths. No complex bezier routing in prototype.
- Arrowheads optional — direction can be implied by glow gradient.

**Status and safety markers:**
- Shield icon for safety. Check circle for verified. Lock for no-secrets. Warning triangle for caution.
- All status icons paired with text labels — never icon-only.

**Avoid emoji-heavy UI:**
- No emoji as primary icons. Emoji may appear in copy text but not as UI elements.

**Avoid icons implying trading/broker actions:**
- No candlestick charts, no buy/sell arrows, no dollar signs, no portfolio/pie-chart icons.
- This is a coordination center, not a trading terminal.

---

## 16. Motion Principles

**Static first:**
- The entire homepage must function, look complete, and communicate all messages without any animation.
- CSS-only rendering is the baseline. JavaScript-driven motion is a progressive enhancement.

**Subtle orbit movement (future):**
- If orbit rings animate, they move slowly (30-60s per revolution).
- Orbit nodes may gently pulse opacity (5-10s cycle) to suggest latent activity.

**Slow fades:**
- Section entrance: gentle fade-in (400-800ms) on scroll.
- Panel hover: subtle opacity or border brightness change (200-300ms).

**No distracting animations:**
- No bouncing, no spinning loaders, no flashing elements.
- No auto-scrolling, no parallax that disorients.
- No animation that draws attention away from primary content.

**Reduced-motion support:**
- All animations must check `prefers-reduced-motion: reduce`.
- When reduced motion is active: all animations become instant transitions.
- No content is hidden behind animation — everything is accessible without motion.

**No forced motion:**
- No content requires animation to be understood.
- No information is revealed only through animation.
- Static state is the canonical state.

**No motion required to understand content:**
- Every section, every label, every status is fully legible and meaningful in a screenshot.

---

## 17. Accessibility Guardrails

1. **Color contrast:** All body text meets WCAG AA 4.5:1. All large text (18px+ bold or 24px+) meets 3:1. Test on glass panels with blur.
2. **Keyboard focus:** All interactive elements have visible focus indicators. Focus rings use signal cyan or orbital violet, 2px solid.
3. **Readable body text:** Minimum 16px body text. Line-height 1.6-1.8. Max 72 characters per line.
4. **No tiny HUD text on mobile:** HUD labels hidden or scaled up on mobile. Never below 11px on any viewport.
5. **No information by color only:** Every color-coded element has a text label, icon, or pattern supplement.
6. **Reduced motion:** Full support for `prefers-reduced-motion`. No content loss when motion is disabled.
7. **Responsive text scaling:** All text scales correctly up to 200% browser zoom without overflow or clipping.
8. **Hover-independent interactions:** Every hover effect has a focus equivalent. No information available only on hover.
9. **Clear status labels:** All status chips, safety badges, and state indicators include text — not color-only.
10. **Skip navigation:** Future implementation must include skip-to-content link.
11. **Semantic HTML:** Sections use `<section>`, `<header>`, `<nav>`, `<main>`, `<footer>`. Headings follow hierarchy.
12. **Alt text:** All decorative images have empty alt. All informational images have descriptive alt.

---

## 18. Responsive Principles

| Viewport | Layout | Key Adaptations |
|---|---|---|
| **Desktop 1280px+** | Full command center | Multi-column grids, full constellation, orbit map, HUD clusters |
| **Tablet 768-1279px** | Stacked panels | 2-column grids, simplified constellation, orbit map reduced |
| **Mobile 767px and below** | Single column | Stacked cards, constellation to agent card list, orbit to vertical timeline |

**Orbit maps to lists:** On mobile, the radial orbit map converts to a vertical list of phase markers with status chips. Same information, linear layout.

**Constellation to agent cards:** On mobile, the constellation visualization converts to individual agent cards in a vertical stack. Each card shows agent name, role, and status. OmniRouter is shown as the central routing card connecting them.

**HUD density reduced on mobile:** Secondary HUD labels hidden on mobile. Only primary status labels visible. Expandable detail panels for users who want more.

**No unreadable decorative text on small screens:** Any text that exists purely for atmosphere (HUD background text, technical annotations) is hidden below 768px if it becomes unreadable.

---

## 19. Future Implementation Notes

**Static-first frontend:**
- First implementation slice is pure HTML/CSS or a static site generator.
- No JavaScript required for content rendering.
- No framework lock-in — design system is framework-agnostic.

**Component candidates:**
- Each design primitive (Section 9) maps to a future component.
- Components should be built in isolation (Storybook or similar) before page assembly.

**Design tokens later:**
- Color language (Section 6) maps to future design tokens.
- Typography guidance (Section 7) maps to future type scale tokens.
- Spacing rhythm (Section 8) maps to future spacing tokens.
- Token implementation deferred until frontend framework is chosen.

**No provider calls in first landing slice:**
- The website makes zero API calls. No provider SDKs. No fetch requests.
- All data is static content authored in markup.

**No live API indicators:**
- No "connected" dots, no real-time counters, no live-data badges.
- All status indicators show project/documentation state, not runtime state.

**No "connect live" CTA:**
- No button or link suggests connecting to a live provider.
- Safe CTAs: "View Roadmap", "Review Context Packet", "Explore Design System".

**No provider-key forms:**
- No input fields for API keys, tokens, or credentials.
- No settings panel for provider configuration.

**No backend assumptions:**
- Design does not assume a backend exists.
- No loading states, no error states from API failures, no retry buttons.

---

## 20. Forbidden Design Patterns

The following patterns are **explicitly forbidden** in the MellyCore AIOS design system:

| Forbidden Pattern | Reason |
|---|---|
| **Fake trading terminal** | MellyCore is not a trading platform. No candlestick charts, order books, or trade history. |
| **Fake live provider status** | No "connected" indicators, green dots, or "online" badges for providers. |
| **Fake PnL / returns** | No profit/loss displays, no return percentages, no portfolio values. |
| **Buy/sell/execute controls** | No buttons that imply placing trades, executing orders, or triggering actions. |
| **Connect-live buttons** | No CTAs suggesting connection to live APIs, providers, or production systems. |
| **Overanimated crypto hype** | No flashy animations, coin spins, rocket emojis, or "to the moon" aesthetics. |
| **Unreadable neon text** | No text that relies on glow for readability. All text must be clear without effects. |
| **Copied GLM visuals** | No assets, code, or visual elements copied from the GLM/Z.ai reference workspace. Inspiration is fine; copying is forbidden. |
| **Secret/key UI** | No input fields, display fields, or configuration panels for API keys or secrets. |
| **Misleading production claims** | No text suggesting the system is live, production-ready, or currently operational. |
| **Dashboards implying autonomous execution** | No agent dashboards that suggest agents are running unsupervised or making autonomous decisions. |
| **MellyTrade runtime UI** | No trading-specific components from MellyTrade imported into MellyCore AIOS. |
| **Broker execution routes** | No routing visualizations that resemble broker order routing or trade execution paths. |
| **Retail trading app patterns** | No patterns borrowed from Robinhood, Binance, or similar retail trading interfaces. |

---

*This design system specification is a living document. It defines the visual and UX architecture for MellyCore AIOS as of the current prototype phase. It will evolve as the project moves toward runtime integration.*
