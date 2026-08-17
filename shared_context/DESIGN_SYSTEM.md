# Design System

## Surface Ownership

MellyCore has two distinct primary visual surfaces. They are complementary, not
competing, and neither displaces the other.

| Surface | Primary direction | Behavioral owner |
|---|---|---|
| Homepage / commercial showcase hero (`site/index.html`) | **Source Arena** holographic metaphor | `docs/specs/MELLYCORE_HOMEPAGE_SPEC_001.md`, `docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md` |
| Command Center cockpit (`site/dashboard.html`) | **MellyCore Cockpit V3.1** dense AI operations workstation | `docs/specs/MELLYCORE_COMMAND_CENTER_COCKPIT_SPEC_001.md` |

Source Arena remains the leading cinematic metaphor for hero, showcase,
transition, and model/source visualization. The Cockpit is the primary product
composition for operational work. A rule written for one surface does not
silently govern the other; where a rule is surface-specific, it says so.

Recorded by `MELLYCORE-COCKPIT-V3-CANONICALIZATION-001` on Operator direction.
Neither direction is a claim that the surface is implemented.

## Leading Visual Metaphor

Source Arena is the leading holographic visual metaphor and intended first hero
experience. The accepted reference is a 390×844 mobile model-lens composition:
operator-selected evidence, visible model perspectives, provenance, and approval
state in a readable social-feed frame.

The accepted contract lives in
`docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md`. It is a specification, not a
claim that the complete holographic/3D experience is implemented.

An accepted Hybrid renderer decision, `docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md`
(status: **ACCEPTED**, 2026-07-20, decision/specification level only), lets
Source Arena's space/hologram layers be rendered by an enhanced WebGL
renderer (one pinned, vendored Three.js module) or by the CSS-only
description below, selected automatically by capability detection, with the
CSS path always complete and mandatory as fallback. The feed/content layer,
honesty labels, and layer ordering are identical under either renderer and
are not affected by this decision. Canonical `main` contains no accepted
WebGL renderer. Paused, open, unmerged PR #28 implements one
(`site/js/mellycore-scene.js`, `THREE.WebGLRenderer`, vendored
`site/vendor/three-r164.module.js`), but it remains non-canonical, unmerged,
and blocked by physical Android Chromium Gate B (`OPEN / NOT EXECUTED`); the
design system does not treat it as accepted.

## Visual Hierarchy

1. **Feed/content layer:** Source Arena evidence, model lenses, recommendations,
   provenance, and operator controls.
2. **Hologram/structure layer:** restrained HUD panels, glassmorphism, context
   state, and safety containment.
3. **Atmosphere layer:** black-space depth, sparse star field, purple/blue neon,
   and cinematic command-center tone.

Overview's core/orbit/hull, an orbital cube, roadmap orbit map, model-router
constellation, or OmniRouter provider hub may appear only as supporting motifs.
**On the homepage/hero surface** they must never displace Source Arena as the
lead image or reduce readability. This constraint is scoped to that surface; it
does not govern the Command Center cockpit, where the Knowledge & Operations
Graph is the intended dominant element (see "Surface Ownership" above and
"Command Center Cockpit" below).

NASA or other space media is not part of the current product identity. Any NASA
imagery still rendered by the legacy prototype is historical content behavior,
not design-system chrome or a roadmap pillar.

## Observatory Surfaces

Mission Control, Agent Activity, Context Pulse, Model Router, Unified Run Ledger,
Approval Queue, Memory & Recommendation Ledger, AI Estate Inventory, Skill Gap
Detector, and Memory Freshness Monitor are planned surfaces. Designs must label
them as planned until implemented evidence exists.

## Color Direction

- Near black and deep charcoal foundations
- Electric violet and soft lavender as primary structure
- Cyber blue as a secondary data accent
- Magenta for interaction emphasis
- Amber for safety/approval boundaries
- Green only for verified real/current state

Avoid gamer RGB, hue cycling, casino trading UI, fake PnL, broker execution UX,
unlabeled simulation, and ornamental effects that overpower operational evidence.

## Command Center Cockpit

Surface-scoped rules for `site/dashboard.html`. Full contract:
`docs/specs/MELLYCORE_COMMAND_CENTER_COCKPIT_SPEC_001.md`.

Composition and density:

- dense technical workstation; high but intentional information density;
- near-black technical canvas;
- cockpit gaps approximately 8–12px; panel padding approximately 12–16px;
- small radii; 1px restrained borders; subtle depth; restrained glow;
- central topology dominance — the Knowledge & Operations Graph is the
  dominant element and MellyCore Core is visually dominant within it;
- aligned panel grid; compact technical typography.

Colour, scoped to this surface only (it does not amend the global Color
Direction above, which continues to govern the homepage/hero):

- **cyan / blue** — core system, routing, architecture (primary cockpit accent)
- **violet** — governance and MellyCore identity
- **amber** — context, attention, artifacts
- **green / lime** — verified capability, tools, positive factual state
- **red** — critical only

Colour must never be the sole state indicator.

Prohibited on this surface: giant rounded cards, excessive glassmorphism, giant
hero typography, large empty marketing gaps, generic component-library admin
defaults, uniform purple gradient treatment, gaming-HUD styling,
crypto/trading-terminal aesthetics, decorative neon overload, and
generic SaaS card soup.

Also prohibited: fake-live telemetry of any kind. See the cockpit
specification's binding truthfulness rules and `shared_context/SAFETY_CONTRACT.md`.

Accessibility and reduced motion are mandatory, and the graph must never be the
only representation of important architecture or state.

## Interaction and Safety

- Readability and visible labels beat atmosphere.
- Real, simulated, legacy, and planned states must be explicit in text.
- Consequential actions require an operator approval state; no autonomous action
  should be implied by motion or copy.
- Mobile flattening, reduced motion, forced colors, keyboard focus, and meaningful
  no-JS states remain mandatory.
