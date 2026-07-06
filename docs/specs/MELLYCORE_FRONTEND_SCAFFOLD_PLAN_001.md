# MellyCore AIOS — Frontend Scaffold Plan

**Task ID:** MELLYCORE-FRONTEND-SCAFFOLD-001
**Version:** 1.0
**Status:** Complete (planning artifact)
**Scope:** Implementation-ready scaffold plan for the MellyCore AIOS homepage. Planning only — no frontend code exists or is created by this task.

---

## 1. Purpose

This document is a **frontend scaffold plan only**. It translates the completed design system and homepage specification into a concrete, step-by-step implementation blueprint that a future, separately approved coding task (`MELLYCORE-FRONTEND-STATIC-SCAFFOLD-IMPLEMENTATION-001`) can execute without re-deriving decisions.

This task does **not**:

- create any frontend, backend, or runtime code;
- add packages, lockfiles, build tooling, or workflow YAML;
- integrate any provider, API, or runtime state;
- authorize implementation — that requires separate explicit approval.

---

## 2. Source of Truth

This plan is derived exclusively from the following repository documents, all validated as of commit `6dedbefd07567400969f9c5fdc3f5c1c86a32a37` on branch `docs/mellycore-design-system-homepage-spec`:

| Document | Role |
|---|---|
| `docs/design/MELLYCORE_DESIGN_SYSTEM_001.md` | Visual language, color tokens, typography, primitives, glassmorphism/glow/motion rules, forbidden patterns |
| `docs/specs/MELLYCORE_HOMEPAGE_SPEC_001.md` | Section-by-section homepage content, copy direction, acceptance criteria |
| `docs/specs/MELLYCORE_UI_SECTIONS.md` | Section registry, build order, minimum viable homepage, visual QA checklist |
| `shared_context/PROJECT_STATE.md` | Current project status and next-task sequencing |
| `shared_context/AGENT_HANDOFF.md` | Handoff state and gating conditions |
| `shared_context/RUN_QUEUE.md` | Task queue and sequencing |
| `shared_context/SAFETY_CONTRACT.md` | Binding safety rules |
| `PROJECT_RULES.md`, `AGENTS.md`, `CLAUDE.md`, `README.md` | Repo-wide agent rules and docs-first posture |

If any of these documents conflict with this plan, the source documents win and implementation must stop (see Section 12).

---

## 3. Page Architecture

### Route / page structure

One page, no router, no framework:

```
site/
  index.html          — the complete homepage (single static document)
  css/
    tokens.css        — design tokens (CSS custom properties only)
    base.css          — reset, typography, background/starfield, layout shell
    components.css    — reusable primitives (panels, chips, badges, nodes, labels)
    sections.css      — per-section layout (hero, constellation, orbit map, etc.)
  assets/
    (static SVG/PNG only; geometric placeholder icons; no external fetches)
```

- Pure HTML/CSS. **Zero JavaScript in the first slice.** No package.json, no node_modules, no build step, no framework. The page opens directly from the filesystem.
- All content is authored in markup. No data fetching of any kind.
- The `site/` directory name is a proposal; the implementation task may use `website/` or `frontend/` if the operator prefers, but must not scatter files at repo root.

### Section order (per `MELLYCORE_HOMEPAGE_SPEC_001.md`)

Document order on the page, top to bottom, each as a `<section>` with the spec's section ID as its `id` attribute (anchor targets):

1. `hero-command-center` — Hero: identity, prototype tag, safety badges, safe CTAs
2. `agent-constellation` — Supervised agent fleet, OmniRouter hub
3. `model-router-panel` — Architectural routing preview, placeholder providers
4. `shared-context-memory` — Memory-card grid of the 10 shared_context files
5. `roadmap-orbit-map` — Six phases as concentric orbits, honest statuses
6. `safety-control-layer` — First-class safety checklist and badges
7. `tooling-layer` — Eight controlled tool surfaces
8. `next-actions` — Safe anchor-link CTA group
9. `footer-status` — Honest project status footer

**Build order** follows `MELLYCORE_UI_SECTIONS.md`: hero → safety → shared-context → roadmap → constellation → router → tooling → next-actions → footer. The five-section minimum viable homepage (hero, safety, shared-context, roadmap, footer) is an acceptable first checkpoint.

### Static-first assumptions

- The page must render completely and communicate every message with JavaScript disabled.
- No loading states, error states, retry buttons, or backend assumptions.
- All status indicators describe **project/documentation state**, never runtime state.
- Prototype status ("Static Prototype — Docs & Spec Phase") is visible in the hero before any CTA and again in the footer.

---

## 4. Component Inventory

Names only — no code. Each maps to design-system primitives (design system §9) and homepage spec components. "Props/data shape" describes the static authored content each component instance carries.

### HeroShell
- **Purpose:** Full-viewport hero container; frames headline, subtitle, prototype tag, safety badges, orbital cube visual, and CTA group. Realizes `CommandCenterShell` + `HeroSection`.
- **Props/data shape:** headline text, subtitle text, prototype tag label, one-liner, optional description paragraph, list of safety badge labels, list of CTA {label, anchor target}.
- **Safety constraints:** prototype tag rendered before any CTA; no forbidden CTAs (no "Connect Live", "Add API Key", "Execute", "Deploy Now", "Launch", "Start Trading", "Go Live"); no pulsing/live indicators; orbital cube is static CSS/image, no 3D library.
- **Responsive:** desktop headline-beside-cube; tablet headline centered, cube scaled below; mobile cube hidden or minimal, CTAs stack vertically.

### GlassPanel
- **Purpose:** Primary content container: semi-transparent surface, backdrop blur, subtle border. Used by nearly every section.
- **Props/data shape:** slot content; optional accent-border variant (safety section); optional padding scale.
- **Safety constraints:** text on panel must meet WCAG AA through the blur layer; never conveys state by transparency alone.
- **Responsive:** below 768px, swaps `backdrop-filter` for a solid semi-transparent background (performance rule, design system §11); max 3–4 glass panels per mobile viewport.

### ConstellationNode
- **Purpose:** One agent/provider/tool marker in the constellation and router sections.
- **Props/data shape:** name, 2–3 word role label, status label ("supervised" or "placeholder"), size variant (hub vs. satellite), geometric placeholder icon/initials.
- **Safety constraints:** every agent node shows "supervised"; provider nodes show "placeholder" in dormant gray; no "connected"/"online"/"running" states; no brand logos; OmniRouter is always the visually central hub.
- **Responsive:** radial positioning on desktop; on mobile the constellation collapses to a stacked card list with the OmniRouter card first.

### OrbitNode
- **Purpose:** One roadmap phase marker on an orbital ring.
- **Props/data shape:** phase name, status (complete | active | planned | blocked/later), 2–4 deliverable bullets, optional dependency note.
- **Safety constraints:** blocked/later phases dimmed but visible — never hidden; the runtime phase must carry the literal note "requires explicit approval"; no implied progress beyond documented state (cross-agent smoke stays **pending**).
- **Responsive:** positioned on concentric rings on desktop/tablet; converts to a vertical timeline list item on mobile.

### StatusChip
- **Purpose:** Compact pill indicator for phase/agent/tool status.
- **Props/data shape:** text label, status variant (complete=green, active=blue, blocked=amber, deferred/placeholder=gray, supervised/controlled=cyan-neutral).
- **Safety constraints:** always text + color, never color-only; only honest states — no "live", "connected", or "online" variants exist in the palette.
- **Responsive:** minimum 10–12px text; never wraps; unchanged across breakpoints.

### SafetyBadge
- **Purpose:** Prominent shield/lock-style indicator for enforced safety constraints ("No Secrets Loaded", "Static Preview", "Supervised Only", "No Copied Workspace").
- **Props/data shape:** icon variant (shield | lock | check), short label.
- **Safety constraints:** a badge may only be rendered for a constraint that is actually enforced in the repo; icon always paired with text.
- **Responsive:** horizontal row on desktop; wraps to grid on tablet; vertical stack on mobile.

### RoadmapOrbitMap
- **Purpose:** Section-level composition: concentric CSS rings hosting the six OrbitNodes with status color coding (inner=complete/green, mid=active/blue, outer=planned/lavender, outermost=blocked/gray+amber "later" badge).
- **Props/data shape:** ordered list of phase objects (see OrbitNode) plus the HUD label "STATIC ROADMAP — UPDATED MANUALLY".
- **Safety constraints:** no timeline animation; no GitHub/project-board integration; honest phase states only.
- **Responsive:** full radial map ≥1280px; simplified/semi-circular 768–1279px; vertical timeline list <768px.

### AgentRosterPanel
- **Purpose:** Section-level composition for the agent constellation: OmniRouter hub, 10 ConstellationNodes, static RouteLines from each node to the hub. Also the mobile card-list fallback.
- **Props/data shape:** hub descriptor + list of agent/tool objects {name, role, status}; route pairs are implicit (every node → hub).
- **Safety constraints:** route lines are static (no animated data-flow); nodes connect only through OmniRouter, never directly to each other; no autonomy implied.
- **Responsive:** radial diagram desktop; reduced node layout tablet; stacked AgentCardList mobile.

### CommandSurfacePreview
- **Purpose:** Section-level composition for the model-router panel: control-panel layout with OmniRouter center and five dormant provider placeholder cards, plus the HUD label "ARCHITECTURE PREVIEW — NO LIVE ROUTING".
- **Props/data shape:** hub note text ("Provider API keys stay outside the repo"), list of provider placeholders {name, routing role, status: "placeholder"}.
- **Safety constraints:** no key inputs, no connection forms, no "add provider" buttons, no provider health indicators; dormant-gray styling on all provider cards; the no-live-routing notice is mandatory and non-dismissable.
- **Responsive:** radial/horizontal desktop; 2-column with hub spanning top on tablet; vertical stack with hub card first on mobile.

### FooterSafetyNote
- **Purpose:** Footer status panel: project name, "Prototype — Docs & Spec Phase" chip, five status confirmations (no live provider connections; no secrets or API keys loaded; no runtime code; GLM reference workspace not copied; static preview planned — not yet published), doc links, attribution.
- **Props/data shape:** status label, confirmation list, link list {label, href to repo docs or page anchors}, attribution line.
- **Safety constraints:** honest phase statement; explicit "GLM reference not copied" line; no production claims; no dynamic git data.
- **Responsive:** 2-column desktop (status left, links right); stacked tablet; compact single column mobile.

### Supporting primitives (from design system §9, reused across sections)
- **HudLabel** — uppercase letter-spaced technical label; max 2–3 words; ≥11px always; may be hidden on mobile if unreadable.
- **RouteLine** — static 1–2px SVG/CSS connector; no animation; no labels on lines.
- **MemoryCard** — shared-context file card: file name, one-line description, type badge; **metadata only, never file contents**; also reused as ToolCard for the tooling layer with a "controlled" chip.
- **StaticPreviewNotice** — non-dismissable "Static Preview / Prototype — No Live Data" banner; required in hero and any section that could be misread as live.
- **SectionHeaderCluster** — title (2–5 words) + one-sentence subtitle + 0–3 HudLabels; opens every section.
- **NextActionsCtaGroup** — anchor-link button group; allowed CTAs only ("View Roadmap", "Review Context Packet", "Explore Design System", "Review Safety Contract", "View Agent Constellation"); zero form elements.

---

## 5. Data Model / Fixture Plan

All "data" is static authored content. In the pure HTML/CSS first slice it lives directly in markup; the fixture names below define the canonical content groupings so a later componentized pass can extract them without redesign.

| Fixture name | Contents | Source section |
|---|---|---|
| `heroContent` | Headline, subtitle, prototype tag, one-liner, description, CTA anchors, safety badge labels | Spec §1 |
| `agentRoster` | 10 agent/tool entries: name, role label, status "supervised" | Spec §2 |
| `providerPlaceholders` | 5 entries: name, routing role, status "placeholder" | Spec §3 |
| `contextFileList` | 10 shared_context file cards: name, description, type badge | Spec §4 |
| `roadmapPhases` | 6 phases with status, orbit position, deliverables, approval note on runtime phase | Spec §5 |
| `safetyRules` | 13 checklist rules + 4 badge labels + GLM reference note | Spec §6 |
| `toolSurfaces` | 8 tool cards: name, role description, status "controlled" | Spec §7 |
| `nextActionCtas` | 5 allowed CTA labels + anchor targets | Spec §8 |
| `footerStatus` | Status label, 5 confirmations, links, attribution | Spec §9 |

Hard constraints on all fixtures:

- **No API calls, no fetch, no provider SDKs, no env variables, no live state, no runtime reads.**
- No secrets, keys, tokens, account IDs, or real config values anywhere in fixture content.
- Roadmap fixture must mirror the honest states in the spec (cross-agent smoke = pending; runtime integrations = blocked/later, approval-gated).
- Fixture content changes require re-checking the acceptance criteria in the homepage spec.

---

## 6. CSS / Design Token Plan

`css/tokens.css` defines CSS custom properties mapping 1:1 to design system §6–§8. Proposed naming (implementation may adjust prefixes but must keep the 1:1 mapping documented):

### Color tokens (design system §6)
| Token | Maps to |
|---|---|
| `--color-void-black` | Void Black (#050508 range) — page background |
| `--color-deep-space` | Deep Space Black (#0A0B14 range) — panel backgrounds |
| `--color-orbital-violet` | Orbital Violet (#7C3AED range) — primary accent |
| `--color-plasma-blue` | Plasma Blue (#3B82F6 range) — secondary accent, route lines |
| `--color-signal-cyan` | Signal Cyan (#06B6D4 range) — HUD labels, status |
| `--gradient-nebula` | Nebula Purple gradient (#4C1D95 → #7C3AED) |
| `--color-cold-white` | Cold White (#E2E8F0 range) — body text |
| `--color-muted-lavender` | Muted Lavender (#C4B5FD range) — secondary text |
| `--color-warning-amber` | Soft Warning Amber (#F59E0B range) — blocked/"later" |
| `--color-safe-green` | Safe Status Green (#10B981 range) — complete states |
| `--surface-glass` | Glass Panel Surface (8–12% white) |
| `--border-command` | Command Center Border (15–20% violet-white) |
| `--glow-nebula` | Soft Nebula Glow radial gradient |
| `--color-dormant-gray` | Dormant Node Gray (#6B7280 range) — placeholders |
| `--color-active-route` | Active Route Blue (#2563EB range) |

### Type and spacing tokens (design system §7–§8)
- Type scale: `--text-hero`, `--text-h2`, `--text-body` (16–18px base), `--text-hud` (11–13px, never below 11px), `--text-caption`; line-height 1.6–1.8 body; system font stack with Inter/Space Grotesk/JetBrains Mono listed as preferred families — **no font files committed, no external font CDN fetches in first slice** (system fallbacks acceptable).
- Spacing scale on an 8px base: `--space-1` (8) through `--space-20` (160), used for the 120–160px desktop / 80–120px tablet / 64–80px mobile section rhythm.
- Layout: `--max-content-width: 1280px`.

### Component class plan (`components.css`)
- `.glass-panel` (+ `.glass-panel--accent` for safety section) — blur, border, shadow per §11 limits (one shadow max, 15–20% border opacity).
- `.hud-label`, `.status-chip` (+ `--complete/--active/--blocked/--deferred/--supervised` modifiers), `.safety-badge`, `.memory-card`, `.orbit-ring`, `.orbit-node`, `.constellation-node` (+ `--hub`), `.route-line`, `.static-preview-notice`, `.cta-anchor`.
- Starfield/nebula: CSS radial-gradients on `body`/hero pseudo-elements — sparse (50–100 points equivalent), 10–30% opacity, **no canvas, no particle system, no animation**.

### Glassmorphism, glow, and premium cinematic feel
- Glassmorphism per §11: blur only on primary panels; never on chips/labels/buttons; solid semi-transparent fallback below 768px.
- Glow per §12: max 2–3 glowing elements per viewport; violet glow reserved for hero cube/headline and primary CTA focus; blue for route lines; cyan sparingly for HUD emphasis; glow never substitutes for contrast.
- Cinematic feel comes from the void-black canvas, nebula gradients (max 1–2 per viewport), generous spacing rhythm, and restraint — not from motion.

### Motion constraints and reduced motion
- **First slice is static: no keyframe animations, no scroll-triggered effects, no cube rotation.** Only hover/focus transitions (150–300ms opacity/border changes) are permitted.
- A single global `@media (prefers-reduced-motion: reduce)` block makes all transitions instant. No content or meaning depends on motion.

---

## 7. Accessibility Plan

- **Keyboard/focus:** every interactive element (anchor CTAs, footer links) gets a visible 2px solid focus ring in signal cyan or orbital violet; a skip-to-content link is the first focusable element; logical tab order follows document order.
- **Contrast:** all body text ≥4.5:1, large text ≥3:1 (WCAG AA), verified **through the blur layer** on glass panels; if a panel fails, increase panel background opacity rather than adding glow.
- **Reduced motion:** full `prefers-reduced-motion` support; static state is the canonical state; nothing is revealed only by animation.
- **Readable hierarchy:** one `<h1>` (hero headline), sequential `<h2>` per section, no skipped levels; body text 16px+ (16px+ on mobile), max 72ch line length; HUD labels never below 11px and hidden on mobile if decorative.
- **Semantic structure:** `<header>`, `<nav>` (if a command bar is included), `<main>` with nine `<section id="…">` landmarks matching the spec section IDs, `<footer>`; status conveyed by text labels, never color alone; decorative visuals (cube, starfield, route lines) marked `aria-hidden="true"` with empty alt where applicable; informational SVGs get accessible names.
- **Zoom:** layout survives 200% browser zoom without clipping or horizontal overflow.

---

## 8. Responsive Plan

| Breakpoint | Layout | Key adaptations |
|---|---|---|
| **Desktop ≥1280px** | Full command center, max content 1280px centered | Full radial constellation and orbit map; 2–4 column card grids; HUD clusters visible |
| **Tablet 768–1279px** | Stacked panels, 2-column grids | Constellation simplified; orbit map reduced/semi-circular; section spacing 80–120px; larger touch targets |
| **Mobile ≤767px** | Single column | Orbit map → vertical timeline list; constellation → stacked agent cards (OmniRouter first); cube hidden/minimal; HUD density reduced; solid panels instead of backdrop blur; section spacing 64–80px |

Hard requirements:

- **No horizontal overflow at any width** — verified at 375px, 768px, 1024px, 1280px, 1920px.
- **No content hidden behind cinematic effects:** nebula/starfield/glow layers sit behind content with pointer-events none conceptually; text remains readable if every decorative layer is removed.
- Decorative-only text is hidden below 768px rather than rendered unreadably small.
- Radial visualizations always have a linear equivalent carrying the same information.

---

## 9. Safety UX Plan

### Communicating static/demo-only status
- Hero prototype tag ("Static Prototype — Docs & Spec Phase") rendered before any CTA.
- Non-dismissable StaticPreviewNotice in hero; per-section HUD notices: "ARCHITECTURE PREVIEW — NO LIVE ROUTING", "STATIC FILE LIST — NO RUNTIME ACCESS", "STATIC ROADMAP — UPDATED MANUALLY", "CONTROLLED SURFACES — NO AUTONOMOUS EXECUTION".
- Footer repeats the five honest status confirmations, including "no runtime code" and "GLM reference workspace not copied".

### Avoiding connect-live implications
- No pulsing dots, no green "online" indicators, no real-time counters, no simulated data streams, no animated route lines.
- Provider cards are dormant gray with "placeholder" chips; copy states keys stay outside the repo.
- All agents/tools labeled "supervised"/"controlled"; no autonomy or background execution implied.
- Status vocabulary is closed: complete, active, planned, blocked/later, pending, placeholder, supervised, controlled. No "live", "connected", "online", "running".

### Forbidden CTA list (must not appear anywhere)
"Connect Live", "Add API Key", "Execute", "Deploy Now", "Launch", "Start Trading", "Go Live", "Sign Up", "Get Started Free", "Add Provider", "Open in [tool]", plus any form submission or external service redirect.

### Forbidden trading/broker UI list (must not appear anywhere)
Buy/sell/execute/order controls; order books; candlestick charts; PnL/returns/portfolio displays; broker connectivity or account UI; trade history; broker-style order routing visualizations; retail trading app patterns; any MellyTrade runtime component. Also forbidden per design system §20: key/secret input or display fields, fake safety badges, copied GLM visuals/assets, production-readiness claims.

---

## 10. Implementation Sequence for the Future Coding Task

For `MELLYCORE-FRONTEND-STATIC-SCAFFOLD-IMPLEMENTATION-001` (requires separate explicit approval; do **not** execute now):

1. **Preflight:** confirm clean working tree on the approved branch; re-read this plan, the design system, homepage spec, UI sections brief, and `SAFETY_CONTRACT.md`; verify no stop condition (Section 12) applies.
2. **Scaffold directories:** create `site/` with `css/` and `assets/` as in Section 3. No package manager, no build tooling.
3. **Tokens first:** author `css/tokens.css` with the full token set from Section 6; commit-sized checkpoint.
4. **Base layer:** `css/base.css` — reset, typography scale, void-black background, CSS starfield, layout shell, skip link, focus ring, reduced-motion block.
5. **Semantic skeleton:** `index.html` with `<main>` and all nine empty `<section id>` landmarks in spec order, plus heading hierarchy — validating anchors before styling.
6. **Build sections in the UI-brief order:** hero → safety → shared-context → roadmap → constellation → router → tooling → next-actions → footer. For each section: author content from the fixture definitions (Section 5), apply component classes, check that section's acceptance criteria from the homepage spec before moving on.
7. **Component pass:** consolidate repeated patterns into the shared classes in `components.css`; remove duplication.
8. **Responsive pass:** implement the three breakpoints (Section 8); verify no horizontal overflow at 375/768/1024/1280/1920px.
9. **Accessibility pass:** run the checks in Section 7 (headings, contrast through blur, focus visibility, zoom 200%, reduced motion).
10. **Safety scan:** run the static scan and safety checklist from Section 11; fix any hit before committing.
11. **Validation and report:** run the full Section 11 validation, capture responsive screenshots, write the task report under `docs/tasks/`, update `shared_context/` handoff files, commit docs+site changes. **No push, no publish, no deployment.**

Each step is small enough for a single Codex/Claude Code working session; steps 6–10 may be split across commits per section.

---

## 11. Validation Plan for the Future Coding Task

### Commands
No build/typecheck/lint toolchain exists (and none may be added), so validation is:

- `git status --short` and `git diff --check` — clean, whitespace-sane changes.
- `python scripts/validate_project_state.py` — repo state validation (script exists at `scripts/validate_project_state.py`).
- Optional stdlib-only serve for manual review: `python -m http.server` from `site/` (local only; not a deployment).
- HTML validity: W3C validator offline check or careful manual review — no npm-based linters.

### Visual QA checklist
Use the full checklist in `MELLYCORE_UI_SECTIONS.md` ("Visual QA Checklist") verbatim. Highlights: renders without JavaScript; no live-connectivity implication; WCAG AA contrast; no horizontal scroll at 375px; safety section prominent; prototype status in hero and footer; GLM note present; OmniRouter central; supervised agents; dimmed-but-visible blocked phases; readable at 200% zoom; reduced motion honored; no emoji icons; no trading/broker patterns.

### Static scan checklist
Grep the changed files for and classify every hit:
`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `sk-ant`, `sk-proj`, `.env`, `GLM`, `buy`, `sell`, `order` (word-boundary; CSS `order:` property and words like "border"/"coordination" are benign), `execute`, `broker`, `live`, `deploy`, `workflow`, `provider key`, `fetch(`, `XMLHttpRequest`, `<script`, `<form`, `<input`, `api.`, `http://`, `https://` (external references), `@import` (external CSS).

Classification: prohibition/notice copy is OK; benign substrings are OK; any actual secret, external fetch, form element, or live/trading UX is a **blocker**.

### Safety checklist
- Zero forbidden CTAs (Section 9 list) and zero trading/broker UI.
- Zero form/input elements; zero script tags in first slice.
- Zero external network references (fonts, CDNs, analytics, images).
- Safety badges correspond only to actually enforced constraints.
- shared_context handoff files updated honestly — no overstated progress.

### Responsive screenshots (required evidence)
Capture and attach to the task report: 375px (mobile), 768px (tablet), 1280px (desktop), 1920px (wide desktop) — full-page, plus a reduced-motion/no-JS verification note.

---

## 12. Stop Conditions for the Future Coding Task

The implementation task must **stop immediately and report** (not work around) if:

1. **Package changes are required** — any need for package.json, lockfiles, npm/pnpm/yarn, bundlers, or framework installation.
2. **Route structure is unclear** — anything beyond the single static page seems needed, or the target directory conflicts with existing files.
3. **Runtime/provider/API integration is needed** — any fetch, SDK, endpoint, or dynamic data requirement.
4. **Any live/broker/trading UX appears** — in requirements, copy, or generated output, including anything from the Section 9 forbidden lists.
5. **Secrets/env are needed** — any key, token, credential, or `.env` value would be required or displayed.
6. **Design docs conflict** — this plan, the design system, the homepage spec, or the UI sections brief disagree on something material; resolve via a docs task first.
7. **Safety contract or handoff files disagree with the task premise** — e.g., the frontend gate is marked blocked again in `shared_context/`.
8. **Any destructive git operation, push, merge, rebase, or publish step** would be required to proceed.

---

## 13. Next Recommended Task

If this planning document is accepted as valid:

> **`MELLYCORE-FRONTEND-STATIC-SCAFFOLD-IMPLEMENTATION-001`** — build the static HTML/CSS homepage scaffold exactly per Sections 3–12 of this plan.

**Implementation is not authorized by this document.** It must be separately and explicitly approved by the operator before any frontend code is created. Until then, the repository remains docs-only.

---

*This plan is a docs-only artifact of MELLYCORE-FRONTEND-SCAFFOLD-001. It creates no code, changes no runtime behavior, and preserves the static-first, safety-first posture defined in the shared context.*
