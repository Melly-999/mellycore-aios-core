# MELLYCORE-STATIC-VISUAL-QA-001 — Static Homepage Visual QA Report

**Task ID:** MELLYCORE-STATIC-VISUAL-QA-001
**Version:** 1.0
**Status:** Complete

---

## 1. Outcome

**PASS** — all visual, safety, and accessibility checks passed at every tested viewport. No blockers, no site changes were needed or made.

## 2. Commit Under Test

- `484e5ee648ba9c7fdead7078a2b7cf1ad48c9616` — `feat(static): scaffold MellyCore homepage`
- Files under test: `site/index.html`, `site/css/tokens.css`, `site/css/base.css`, `site/css/components.css`, `site/css/sections.css`
- QA method: served locally via Python stdlib `http.server` (local only, not a hosting setup); inspected in Chromium with device-emulated viewports; DOM/layout measurements via scripted read-only checks; full-page screenshots captured per viewport.

## 3. Screenshot Evidence (local-only, not committed)

Saved under the local evidence folder (outside this repository, binaries intentionally not committed):

`C:\AI\MellyCore_Workspace\04_QA_Evidence\MELLYCORE-STATIC-VISUAL-QA-001\`

| File | Viewport |
|---|---|
| `qa-375-mobile-full.png` | 375×812, DPR 2, mobile emulation, full page |
| `qa-768-tablet-full.png` | 768×1024, full page |
| `qa-1024-small-desktop-full.png` | 1024×768, full page |
| `qa-1280-desktop-full.png` | 1280×900, full page |
| `qa-1920-wide-full.png` | 1920×1080, full page |

## 4. Viewport Results

| Check | 375 | 768 | 1024 | 1280 | 1920 |
|---|---|---|---|---|---|
| No horizontal overflow (scrollWidth ≤ clientWidth) | PASS | PASS | PASS | PASS | PASS |
| No element extends past viewport edges | PASS | PASS | PASS | PASS | PASS |
| Header readable, not clipped | PASS | PASS | PASS | PASS | PASS |
| Hero readable; prototype tag + static notice before CTAs | PASS | PASS | PASS | PASS | PASS |
| Layout mode | single column, timeline, card list, cube hidden, solid panels (no blur) | 2-col grids, blur on, timeline | 2-col grids, timeline | full radial constellation + orbit map, 2-col hero | same as 1280, content capped at 1280px and centered |

Additional viewport findings:

- **375:** body text 17px; HUD labels 12px (≥11px floor); glass panels use solid semi-transparent background (`backdrop-filter: none`) per the mobile performance rule.
- **768:** `backdrop-filter: blur(14px)` active; constellation 2-column with hub card spanning; memory grid 2-column.
- **1280:** radial constellation (10 nodes) — 0 overlapping cards, 0 cards outside the stage; orbit map (6 phases on 4 rings) — 0 overlaps, 0 out-of-stage; timeline list hidden in favor of the orbit map.
- **1920:** container capped at 1280px and centered; hero paragraph measures 660px (~72ch max respected) — no unreadable stretching.

## 5. Visual QA Findings

All 15 checklist items pass:

1. No horizontal overflow at any tested width.
2. Command bar readable at all widths; nav wraps cleanly on mobile.
3. Hero headline, subtitle, one-liner, and description all legible over the starfield.
4. "Static prototype — docs & spec phase" HUD tag and the amber static-preview notice render **before** any CTA in document and visual order (verified via DOM position comparison).
5. Glass panels maintain text contrast (see §7 contrast table) — no text obscured by blur or transparency.
6. Constellation: no overlapping content at any viewport (radial at 1280+, cards below).
7. Roadmap: orbit map clean at 1280+; vertical timeline below — no overlaps either mode.
8. Safety section is a first-class page section with accent border, 4 badges, 13-rule checklist, GLM note, and MellyTrade separation note.
9. Provider cards use dormant gray styling with "Placeholder" chips; agents/tools show "Supervised"/"Controlled" — nothing looks live.
10. Footer shows all 5 honest status confirmations plus documentation links.
11. Decorative layers (starfield, nebula, cube, spokes, rings) sit behind content; no content hidden behind effects.
12. Mobile stacks cleanly in a single column.
13. Tablet has no overflow.
14. Wide layout stays readable (1280px cap, 72ch text).
15. Visual style matches the design system: void-black canvas, violet/blue/cyan accents, glassmorphism, HUD labels, restrained glow.

**Minor notes (non-blocking):** none affecting readability, safety, or layout were found.

## 6. Safety QA Findings

Rendered-text and source scans:

- Forbidden CTA terms ("Connect Live", "Execute", "Run Agent", "Place Order", "Buy", "Sell", "Trade Now", "Link Broker", "Deploy Now", "Go Live", "Start Trading", "Sign Up", "Get Started Free"): **zero occurrences** in rendered text; `buy`/`sell` as words: zero.
- "live" appears only in prohibition text (e.g. "No live provider connections", "NO LIVE ROUTING").
- "connected" (×2) and "running" (×1) appear only in explicit negations ("Nothing on this page is connected", "no providers are connected in this preview", "not a running system").
- `<script>` tags: 0. Forms/inputs/selects/textareas/buttons: 0. Fetch/XHR: none.
- External references (CDN, fonts, images, links to http/https): **none** — every `href`/`src` is an in-page anchor, relative stylesheet, or relative repo-doc path.
- No provider keys, no `.env` references, no fake live/connected/online status, no broker connectivity claims, no trading execution UX.
- GLM: appears only as agent/tool names (per spec) and in the "no GLM files copied" notices.

## 7. Accessibility QA Findings

- **Headings:** exactly one `h1`; all section headings are `h2` — no skipped levels.
- **Skip link:** present and is the first anchor in `body`; targets `#main-content`.
- **Focus states:** programmatic focus on a CTA shows `outline: 2px solid rgb(6,182,212)` (signal cyan) — visible on the dark canvas.
- **Contrast spot checks (WCAG AA requires 4.5:1 body / 3:1 large):**

  | Sample | Ratio |
  |---|---|
  | Body text on void black | 16.51 |
  | Lavender subtitle on panel | 10.17 |
  | Cyan HUD label | 9.48 |
  | Amber HUD label | 9.48 |
  | Green safety badge | 8.02 |
  | Footer attribution | 8.02 |
  | "Complete" chip on panel | 7.40 |
  | Dormant "Placeholder" chip on panel (lowest) | 7.39 |

- **Reduced motion:** `@media (prefers-reduced-motion: reduce)` rule present, neutralizing all transitions and smooth scroll; page has no keyframe animations at all.
- **Decorative visuals:** cube stage, constellation spokes, orbit rings/core, and all glyph monograms carry `aria-hidden="true"`.
- **Links:** zero links with empty accessible text.
- **Landmarks:** `header`, `main` (8 sections), `footer` — all present.
- **Mobile readability:** 17px body text, single column, no clipped content at 375px.
- **Console:** zero console messages/errors during the session.

## 8. External Preview Artifact Status

Both preview-helper artifacts outside this repo were **removed after QA**:

- `C:\AI\MellyTrade_Workspace\.claude\mellycore-site` (directory junction) — deleted; the junction target `site/` in this repo verified intact.
- `mellycore-static` entry in `C:\AI\MellyTrade_Workspace\.claude\launch.json` — removed; the file's other entries were left untouched.
- No MellyTrade repo source files were modified.

## 9. Blockers

None.

## 10. Next Recommended Task

`MELLYCORE-GITHUB-REMOTE-SETUP-001` (per `shared_context/RUN_QUEUE.md` sequencing) — prepare GitHub remote setup **without pushing**; pushing requires explicit operator approval. Alternative next steps if the operator prefers: MVP-demo polish planning, or the deferred `MELLYCORE-CROSS-AGENT-CONTEXT-SMOKE-001` from a clean `main` worktree.

---

*QA performed read-only: no site HTML/CSS changes were made during this task.*
