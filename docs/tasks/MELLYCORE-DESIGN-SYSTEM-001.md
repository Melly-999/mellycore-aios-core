# Task Report: MELLYCORE-DESIGN-SYSTEM-001

**Task ID:** MELLYCORE-DESIGN-SYSTEM-001
**Purpose:** Define the complete visual and UX design system for the MellyCore AIOS command center website.
**Scope:** 20-section design system specification covering identity, color, typography, layout, primitives, surfaces, glassmorphism, neon glow, backgrounds, orbital cube, iconography, motion, accessibility, responsive, implementation notes, and forbidden patterns.
**Status:** Complete

---

## Changed Files

| File | Action | Description |
|---|---|---|
| `docs/design/MELLYCORE_DESIGN_SYSTEM_001.md` | Created | Complete 20-section design system specification |

## Design Decisions

1. **OmniRouter as central routing hub.** The constellation visualization positions OmniRouter at the center, with all agents and providers connecting through it — not directly to each other. This reflects the actual routing architecture defined in `shared_context/MODEL_ROUTING.md`.

2. **Static-first prototype honesty.** Every section of the design system explicitly forbids patterns that imply live connectivity. No pulsing dots, no "connected" indicators, no real-time counters. The design system is for a static preview first, runtime later.

3. **Safety as first-class visual layer.** Safety is not relegated to a footer or legal page. The design system defines safety badges, safety panels, and safety-first visual patterns that must appear prominently throughout the homepage.

4. **No GLM workspace copying.** The design system explicitly forbids copying any visual assets, code, or elements from the GLM/Z.ai reference workspace. Inspiration is acknowledged; wholesale import is forbidden. This is documented in the forbidden patterns section (Section 20) and reinforced throughout.

5. **Color language over CSS variables.** Color definitions use descriptive semantic names with intended use, emotional meaning, accessibility notes, and misuse warnings. No CSS variables are defined — this is a design specification, not a token implementation. Framework-specific tokens will be created when the frontend framework is chosen.

6. **Framework-agnostic primitives.** All 12 design primitives are defined with purpose, visual behavior, content rules, and future component names — but no framework-specific implementation. This allows the design system to be implemented in React, Vue, Svelte, Astro, or plain HTML/CSS.

7. **MellyTrade separation.** The design system explicitly forbids all trading-specific UI patterns (candlestick charts, buy/sell controls, PnL displays, broker routing). MellyCore AIOS and MellyTrade are separate products; MellyTrade consumes MellyCore's coordination but is not its frontend.

8. **MellyGenix unification.** MellyCore AIOS is positioned as the shared coordination layer for all MellyGenix AI products — not just MellyTrade. The design system communicates this broader scope.

## Safety Decisions

1. **No secrets in design artifacts.** The design system contains no API keys, tokens, provider credentials, or real configuration values. All examples are descriptive, not functional.

2. **No runtime code.** This task produces documentation only. No HTML, CSS, JavaScript, or component code was created. The design system specifies future implementation — it does not implement.

3. **No .env files.** No environment configuration files were created or referenced with real values.

4. **No provider keys.** No provider API keys appear in any design documentation. Provider references use names only (ChatGPT, Claude, etc.) without credentials.

5. **No GLM files copied.** No files from the GLM/Z.ai reference workspace (`C:\AI\MellyCore_Workspace\03_Assets\glm_workspace_reference`) were copied into this repository. The design system references the existing `shared_context/DESIGN_SYSTEM.md` which notes visual inspiration from the GLM orbital cube prototype.

6. **Static-first before runtime.** The design system mandates static-first implementation. Runtime features (provider connections, live routing, agent execution) are explicitly deferred and gated behind explicit human approval.

7. **Honest prototype communication.** The design system requires that every surface honestly communicates prototype status. No visual pattern may imply production readiness or live operation.

## Validation Checklist

- [x] Design system contains all 20 required sections.
- [x] OmniRouter documented as central routing hub.
- [x] No CSS variables defined (specification only).
- [x] No framework-specific code.
- [x] No runtime code, no frontend code.
- [x] All color definitions include accessibility notes.
- [x] All design primitives include safety/UX notes.
- [x] Forbidden patterns section includes GLM copying prohibition.
- [x] Safety-first visual patterns defined.
- [x] No secrets, keys, or real values in documentation.
- [x] No GLM workspace files copied.
- [x] Static-first implementation mandate documented.
- [x] Responsive principles cover desktop, tablet, mobile.
- [x] Accessibility guardrails meet WCAG AA baseline.
- [x] Motion principles include reduced-motion support.

## Completion Status

**COMPLETE.** The design system specification is implementation-ready for future frontend agents.

## Next Recommended Task

**MELLYCORE-DOCS-INTEGRATION-REVIEW-001** — Cross-reference the design system with the homepage spec, UI sections brief, and existing shared_context files to ensure consistency, identify gaps, and validate that all design decisions align with the safety contract and project state.
