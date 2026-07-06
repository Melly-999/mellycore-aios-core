# Task Report: MELLYCORE-HOMEPAGE-SPEC-001

**Task ID:** MELLYCORE-HOMEPAGE-SPEC-001
**Purpose:** Define the complete homepage specification for the MellyCore AIOS command center website — section-by-section architecture, UI implementation brief, and visual QA guidance.
**Scope:** 9-section homepage specification with acceptance criteria, plus a compact UI sections implementation brief with build order, minimum viable homepage, and blocked runtime features.
**Status:** Complete

---

## Changed Files

| File | Action | Description |
|---|---|---|
| `docs/specs/MELLYCORE_HOMEPAGE_SPEC_001.md` | Created | Complete 9-section homepage specification |
| `docs/specs/MELLYCORE_UI_SECTIONS.md` | Created | Compact UI sections implementation brief for frontend agents |

## Homepage Decisions

1. **9 sections, ordered by narrative flow.** Hero (identity) → Agent Constellation (agents) → Model Router (routing) → Shared Context (memory) → Roadmap (phases) → Safety (constraints) → Tooling (tools) → CTAs (next actions) → Footer (status). Each section builds on the previous, creating a coherent architectural story.

2. **OmniRouter as central hub in constellation and router sections.** Both the Agent Constellation (Section 2) and Model Router Panel (Section 3) position OmniRouter as the central routing element. All agents connect through OmniRouter — not directly to each other. This matches the routing architecture in `shared_context/MODEL_ROUTING.md`.

3. **Safe CTAs only.** Every CTA across the homepage is an anchor link or documentation link. Forbidden CTAs are explicitly listed: "Connect Live", "Add API Key", "Execute", "Deploy Now", "Launch", "Start Trading", "Sign Up", "Get Started Free".

4. **Prototype status in hero and footer.** The hero section establishes "Static Prototype — Docs & Spec Phase" immediately. The footer reinforces it with 5 explicit status confirmations. No section in between implies live operation.

5. **Safety as Section 6, not a sidebar.** Safety gets its own full section with 13 documented rules, 4 safety badges, and a GLM reference notice. It is architecturally central, not an afterthought.

6. **GLM reference explicitly addressed.** Section 6 (Safety) includes a specific note: "The GLM/Z.ai workspace is reference only. No GLM files have been copied into this repository." The footer (Section 9) confirms: "GLM reference workspace not copied."

7. **Roadmap shows blocked/later phases honestly.** The Runtime/Provider Integrations phase is visible but dimmed, labeled "later — requires explicit approval." This is honest project state communication, not aspirational marketing.

8. **Minimum viable homepage is 5 sections.** For the first deployable slice: hero, safety, shared context, roadmap, and footer. These 5 sections form a complete narrative arc. The remaining 4 sections (constellation, router, tooling, CTAs) enhance but are not required for minimum viability.

9. **Build order prioritized for pattern reuse.** The UI sections brief recommends building hero first (establishes patterns), then safety (trust patterns), then shared context (card patterns), then roadmap (orbital patterns). Later sections reuse patterns from earlier ones.

10. **Mobile-first responsive conversions defined.** Every section specifies how it adapts: constellation → card list, orbit map → vertical timeline, card grids → single column, HUD labels → hidden or scaled.

## Safety Decisions

1. **No secrets in any specification.** All 3 files (homepage spec, UI sections, this task report) contain zero API keys, tokens, credentials, or real configuration values.

2. **No runtime code.** This task produces documentation only. No HTML, CSS, JavaScript, component code, package.json, or any executable files were created.

3. **No .env files.** No environment configuration files were created. The .env.example already in the repo was not modified.

4. **No provider keys.** Provider references use names only (ChatGPT, Claude, Codex, GLM 5.2, Grok, OmniRouter) without credentials, endpoints, or real configuration.

5. **No GLM files copied.** No files from the GLM/Z.ai reference workspace were copied. The homepage spec references existing shared_context files by name only.

6. **Static-first before runtime.** Every section in the homepage spec is explicitly "static only." Blocked runtime features are documented in the UI sections brief. Runtime integration requires explicit human approval.

7. **No fake live status.** Every section includes safety notes prohibiting live-data indicators, connected-status badges, real-time counters, or any visual pattern implying active provider connections.

8. **Honest validation.** The visual QA checklist in the UI sections brief includes 20 verification items, several of which are safety-specific (no forbidden CTAs, no live status, safety section prominent, GLM note accurate, OmniRouter central, all agents supervised).

## Validation Checklist

- [x] Homepage spec contains all 9 required sections.
- [x] Each section includes: purpose, user message, content direction, visual behavior, UI components, interaction notes, responsive behavior, safety notes, static/dynamic guidance, future components, acceptance criteria.
- [x] OmniRouter positioned as central routing hub in constellation and router sections.
- [x] All CTAs are safe (anchor links or documentation links).
- [x] Forbidden CTAs explicitly listed and absent from all sections.
- [x] Prototype status visible in hero and footer.
- [x] Safety section contains all 13 rules from safety contract.
- [x] GLM reference note present in safety section and footer.
- [x] Roadmap shows blocked/later phases honestly.
- [x] Runtime phase explicitly gated ("requires explicit approval").
- [x] UI sections brief covers all 9 section IDs.
- [x] Build order, minimum viable homepage, and blocked features documented.
- [x] Visual QA checklist contains 20 verification items.
- [x] No secrets, keys, or real values in any file.
- [x] No GLM workspace files copied.
- [x] No runtime code, no frontend code, no CSS, no package files.
- [x] Static-first mandate enforced across all sections.

## Completion Status

**COMPLETE.** The homepage specification and UI sections brief are implementation-ready for future frontend agents.

## Next Recommended Task

**MELLYCORE-DOCS-INTEGRATION-REVIEW-001** — Cross-reference the homepage spec, UI sections brief, and design system with existing shared_context files to ensure consistency, identify gaps, and validate that all specifications align with the safety contract, project state, and model routing architecture.
