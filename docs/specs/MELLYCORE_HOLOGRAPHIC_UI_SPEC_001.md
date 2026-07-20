# MellyCore AIOS — Positioning and Holographic UI Specification

Spec ID: `MELLYCORE_HOLOGRAPHIC_UI_SPEC_001`
Produced by task: `MELLYCORE-POSITIONING-AND-HOLOGRAPHIC-UI-SPEC-FABLE-001`
Status: specification only. This document authorizes nothing by itself. It contains no
implementation, no code, and no site changes. A later, separately approved task
(Section 5) implements it.

> **Current-positioning notice (2026-07-18):**
> `MELLYCORE-POSITIONING-REFRESH-001` supersedes this document's NASA-era
> product-positioning and roadmap statements, including the word "canonical" in
> Section 1.1. NASA references below are retained as implementation/historical
> evidence for the existing legacy prototype, not as current product direction.
> The accepted visual contract is unchanged: Source Arena remains the leading
> 390×844 mobile model-lens hero; Overview/core/orbit/hull remains supporting
> imagery; no holographic/3D implementation is claimed. Current positioning and
> sequencing live in `README.md`, `shared_context/ROADMAP.md`, and
> `docs/tasks/MELLYCORE-POSITIONING-REFRESH-001.md`.

> **Renderer amendment notice (2026-07-19; conditional wording corrected
> 2026-07-20; acceptance recorded 2026-07-20):**
> `docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md` is now status:
> **ACCEPTED**. The operator explicitly accepted it on 2026-07-20, on branch
> `docs/mellycore-3d-renderer-hybrid-adr-001` at reviewed baseline commit
> `b95a741231d18ef712379837c7167aa22b37d42f`, following
> `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-003`'s
> `PASS_HYBRID_RENDERER_ADR_REVIEW_003_COMPLETE` outcome (task
> `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-ACCEPTANCE-001`). Acceptance
> makes the ADR's narrow supersession of this document's Section 4, Section
> 5.4, Section 5.9, and Section 8 dependency/build-step/renderer-technology
> clauses authoritative — **only** for Source Arena's central-stage enhanced
> renderer, and **only** the exact clauses the ADR enumerates (ADR Section 7).
> It permits exactly one pinned, checksummed, vendored Three.js ESM module as
> progressive enhancement over a mandatory, complete CSS/DOM fallback that
> implements this document's Section 4 in full. The zero-build-step guarantee
> remains binding; a zero-external-runtime-network guarantee for the future
> post-retirement Source Arena is accepted as a requirement but not yet
> implemented — this notice makes no claim about the **current** dashboard's
> network behavior; see `docs/runbooks/MELLYCORE_LOCALHOST_QUICKSTART.md` for
> the current, verified network behavior of `site/index.html` versus
> `site/dashboard.html`. Every other requirement in this document remains
> fully binding and unchanged: Source Arena as the 390×844 primary hero and
> required first screenshot (Section 3.1, Section 6.3); Overview's
> core/orbit/hull as supporting-only, background-level imagery, never inside
> the Source Arena viewport (Section 2.5); Model Arena as the expanded
> model-lens relationship (Section 3.3); every `Real source` /
> `Simulated model output` / `Planned` label and the truthful-state taxonomy of
> the integrated AI Operations Intelligence specification (integrated into
> canonical `main` via PR #7); DOM as the sole authoritative carrier of every
> label and control in both renderers; every accessibility requirement in
> Section 5.5, now extended so the enhanced-renderer canvas is
> `aria-hidden="true"` and never carries an exclusive interaction; and
> reduced-motion (Section 4.9), now extended so `prefers-reduced-motion:
> reduce` prevents the WebGL renderer from mounting at all, leaving the CSS
> frozen pose as the rendered result. Section 5.9's "the keyless NASA Images
> API remains the sole external data path" is accepted as a future
> requirement to be superseded by the ADR's NASA runtime-retirement boundary
> (ADR Section 24 and Appendix A give the complete, exact, conditional
> identifier map) — **but that retirement has not been executed**: it requires
> its own separately-authorized implementation task
> (`MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001`), which has not begun.
> The current legacy dashboard's NASA API calls and `nasa`-named runtime
> identifiers remain present and unchanged today; historical task reports and
> release evidence remain untouched regardless. **No CSS-only implementation,
> no Hybrid implementation, and no vendored Three.js file exist in the
> repository as of this notice.** Acceptance of the ADR does not itself
> authorize that implementation, dependency acquisition, NASA retirement,
> push, PR, merge, or deployment — those require their own separate
> authorization and review gates. See the ADR for the complete rationale,
> supersession map, and implementation sequencing.

Ground truth this spec is written against (verified in-repo at authoring time):

- Current release: `v0.2.0` — Live Cockpit V2 / Social Source Arena.
- PR #3 (GitHub Repository provider demo + `/roadmap` docs) merged to `main` at `fff50d2`.
- NASA Images API is the only real, live, no-key provider (browser-side GET only).
- GitHub Repository is a planned/demo provider — never live ingestion.
- No backend, no database, no provider keys, no autonomous actions, no scheduler.
- Fable 5 / Opus / GPT / GLM comparison text is deterministic local mock copy,
  labeled `Simulated model output`.
- Existing surface: `site/dashboard.html` (380 lines), `site/css/dashboard.css`
  (992 lines, `--cockpit-*` custom properties), `site/js/dashboard.js` (790 lines,
  vanilla JS), plus the JS-free `site/index.html` homepage.

---

## 1. Product positioning

### 1.1 One-paragraph public description (canonical)

> **MellyCore AIOS is a safety-first AI operations cockpit.** It demonstrates how an
> operator can pull external sources into one auditable surface, see exactly where
> every piece of context came from, and compare how different AI models would read
> the same source — without granting any model the ability to act. The entire product
> is static and zero-autonomy **by design**: no backend, no database, no stored API
> keys, no write actions, no scheduled or autonomous behavior. Every claim on screen
> is labeled as real, simulated, or planned. The current live demo provider is the
> public, keyless NASA Images API; a GitHub Repository provider is shown as a
> planned/demo card; every other source type is explicitly labeled planned.

### 1.2 The five claims MellyCore is allowed to make (all true today)

1. **Provider model.** External data enters through swappable providers. One provider
   (NASA Images API) is live today with real browser-side GETs and no key; one
   (GitHub Repository) is a planned/demo card; nine further source types are listed
   as planned. NASA is a demonstration provider, not the product.
2. **Provenance model.** A working, tested Context Gate (Python stdlib CLI, phases
   I1–I4 complete, 95 focused tests) admits context only through human review, keeps
   records write-once, logs refusals aggregate-safely, and exposes only a
   content-free index to the UI.
3. **Operator gating.** Every state-changing operation in the repository — loop run
   persistence, context admission — requires an explicit operator approval id and an
   expected-HEAD match. Nothing runs unattended; there is no scheduler.
4. **Honest model comparison.** The Model Arena shows four model lenses (Fable 5,
   Opus, GPT, GLM) over one real external source. The lens copy is deterministic
   local simulation, and each card says so. The comparison *pattern* is real; the
   model output is not, and the UI never pretends otherwise.
5. **Auditability.** Validators (`context_gate audit`, `loop_ops validate`,
   `validate_project_state`, 245 unit tests) pass from a fresh clone. The evidence
   trail is in the repository, not in a claim.

### 1.3 Claims MellyCore must never make

- That any model is connected, called, or compared live.
- That NASA is "integrated" beyond public keyless GETs from the visitor's browser.
- That GitHub ingestion exists (it is a planned/demo card with link-only references).
- That social counts are real engagement (they are labeled `Demo counts`).
- That the system runs, monitors, schedules, or acts autonomously in any form.
- Anything implying trading capability or MellyTrade linkage.

### 1.4 Why "static and zero-autonomy" is the feature, not the caveat

The positioning sentence to use whenever this comes up:

> "Most AI-ops demos ask you to trust a black box. MellyCore inverts that: the
> product is the audit trail. It is static so every behavior is inspectable in the
> repo; it is zero-autonomy so the safety story is enforced by architecture, not by
> promises. Capabilities are added in the order *spec → review → gated
> implementation → release*, and the UI labels real/simulated/planned at every
> panel, so the demo can never claim more than the code does."

---

## 2. Visual direction — "Holographic Social Source Cockpit" (HSSC)

### 2.1 Name and one-line definition

**Holographic Social Source Cockpit (HSSC-1).** A black, mobile-first vertical
social feed suspended inside a purple-black holographic command deck: sources
stream like social media, provenance and safety read like avionics.

### 2.2 The three-layer metaphor

Every screen is composed of exactly three visual layers, back to front:

1. **Space layer (background):** near-black canvas, violet nebula depth washes,
   sparse starfield texture. This layer is atmosphere only — it never carries
   information and never exceeds ~10% perceived brightness.
2. **Hologram layer (structure):** the MellyCore core, the provider orbit ring, the
   safety containment hull, and depth-tilted glass panels. This layer carries
   *system state* (what is live, planned, gated).
3. **Feed layer (content):** the vertical social media stage, captions, action
   rail, provenance badges, model lens cards. This layer carries *content* and is
   always the flattest, sharpest, most readable layer.

Rule: readability beats atmosphere. Any conflict between a holographic effect and
text legibility is resolved by flattening the effect, never by boosting glow.

### 2.3 Color system (more purple, less blue)

Extends the existing `--cockpit-*` tokens; new tokens use a `--holo-*` prefix.

| Role | Token (proposed) | Value direction | Notes |
| --- | --- | --- | --- |
| Canvas | `--holo-void` | `#050308` near-black with violet cast | replaces pure black |
| Nebula deep | `--holo-nebula-1` | deep violet `#2a1057`-range at low alpha | radial washes only |
| Nebula bright | `--holo-nebula-2` | electric violet `#7c3aed`-range at low alpha | max 0.22 alpha |
| Primary accent | `--holo-violet` | `#a86cff` (keep existing) | borders, active states |
| Interaction | `--holo-magenta` | `#ff4fd8` (keep existing) | likes, highlights, CTAs |
| Lavender copy | `--holo-lavender` | soft lavender `#cbb8ef`-range | secondary text |
| Hull warning | `--holo-amber` | `#ffc34d` (keep existing) | safety/containment only |
| Live signal | `--holo-green` | `#58e68a` (keep existing) | "live/real" badges only |
| Cyan | `--cockpit-cyan` | demote further | data-table accents only, never structural |

Hard rules:

- Violet/magenta/lavender dominate; cyan appears only as a tertiary data accent.
  If a screenshot reads "blue," it fails review.
- No hue-cycling, no rainbow gradients, no per-frame color animation — this is the
  anti-"gamer RGB" rule. Accent hues are fixed; only opacity and position animate.
- `--holo-green` is reserved exclusively for *real/live* markers, `--holo-amber`
  exclusively for safety/containment. Neither is ever decorative, so color alone
  carries an honesty signal (always duplicated in text for accessibility).

### 2.4 Materials

- **Glass cockpit panel:** existing `dash-surface` treatment, hardened — 1px violet
  line, panel fill ≥ 0.9 alpha behind text (readability rule), backdrop blur where
  supported, inner top-edge highlight suggesting curved glass.
- **Hologram edge:** thin double-border (1px solid violet line + 1px blurred violet
  glow) on hologram-layer elements only. Feed-layer cards get the plain glass edge.
- **Starfield/media texture:** the existing CSS radial-dot starfield, kept sparse.
  Media itself (NASA imagery) supplies the cinematic texture; the UI never competes
  with it.
- **Containment hull:** a compact rounded-rectangle frame with amber corner ticks
  and a short amber caption — **a labeling device, not architecture.** It wraps
  specific simulated/autonomous-looking content (model-lens panels on the central
  feed slide, the Model Arena panel set, the model rail on desktop, loop status on
  Overview) at the size of that content, never the whole application shell or an
  entire screen. Caption text: `Simulated · read-only · zero-autonomy` for
  model-lens content, or the existing `Read-only · No autonomous actions` /
  `Zero-autonomy containment · static · keyless · read-only` variants elsewhere.
  The hull is the signature honest-UI element: decoration that states policy — its
  job is legibility of the constraint, not visual weight.

### 2.5 Secondary identity composition: core, orbit, hull (Overview only)

**This is a secondary identity composition, not the product hero.** The primary
hero of HSSC is the Source Arena social-feed composition (Sections 3.1/3.2). The
core+orbit+hull composition below appears only on the Overview tab, as a compact,
background-level identity mark:

- **MellyCore core:** a small central emblem (layered concentric violet rings around
  the wordmark), softly pulsing glow, the only element allowed a slow idle animation.
- **Provider orbit ring:** provider chips positioned on an elliptical ring around
  the core. NASA chip carries `Live demo` (green); GitHub chip carries `Planned /
  demo` (violet outline); remaining chips are dimmed `Planned`. The ring states the
  product thesis at a glance: many providers, one core, exactly one live today.
- **Safety containment hull:** the amber-ticked frame drawn around core + ring, with
  the caption `Zero-autonomy containment · static · keyless · read-only`.

Hard rules for this composition:

- The orbit is **static or ultra-slow** (existing 60s+ period keyframe, or reduced
  further); it never reads as active motion competing for attention.
- **Background-level only** — it renders behind the Overview status panels, never
  as full-bleed foreground content.
- **Never inside the Source Arena viewport.** The orbit ring does not render on
  the Source Arena mobile or desktop screens (Sections 3.1/3.2).
- **Never the lead screenshot.** See Section 6.3's screenshot order — Overview is
  screenshot #4, not #1.
- **Never visually stronger than the central social slide.** Its glow, size, and
  contrast budget stay below the Source Arena stage's on every viewport where both
  could theoretically be compared.

NASA must never sit in the center. The center is always MellyCore.

### 2.6 Typography and badges

- Keep the existing type stack; introduce no new fonts (no dependency rule).
- Label badge system (already partially shipped) becomes a formal component set:
  `Real source` (green), `Live demo provider` (green outline), `Simulated model
  output` (magenta outline), `Planned provider` / `Planned` (violet outline, dimmed),
  `Demo counts` (lavender), `Provenance required` (violet), `Read-only` (amber).
  Badges are text-first, colored second; minimum contrast 4.5:1 against panel fill.

### 2.7 Explicit avoid-list

- Gamer RGB: no hue rotation, no saturated red/green/blue triads, no pulsing neon.
- Generic dashboard: no white cards, no chart-grid-first layouts, no KPI tile walls.
- NASA dominance: no NASA logos as chrome, no rocket/space-agency iconography in
  UI chrome; space imagery appears only *inside* the media stage as content.
- Skeuomorphic sci-fi noise: no scanlines-over-text, no glitch text, no lens flares.

---

## 3. Screen concepts

Labels legend used below — **Real**: live data or real repo files read at load.
**Simulated**: deterministic local demo content, must carry its label. **Planned**:
described but not built, must carry `Planned`.

### 3.1 Source Arena — mobile (portrait, ≤ 480px)

**This is the product's primary hero composition and required first screenshot
(Section 6.3).**

- **Layout:** full-bleed vertical stage (existing phone-frame pattern promoted to
  the whole viewport), composed top to bottom:
  1. **Top control row:** search pill + provider chip rail (horizontal scroll,
     scroll-fade).
  2. **Prompt/demo-task chip rail:** a second horizontal-scroll row directly below
     the provider rail, listing demo prompts (Section 3.1a). Always visible, never
     hidden behind a menu.
  3. **Central slide:** one slide per viewport, vertical swipe/scroll between
     slides. Two slide types exist and are interchangeable in the same feed
     (Section 3.1a): a **media slide** (real NASA source, existing behavior) and a
     **model-lens slide** (selected real source + four model-comparison panels,
     new — required, not optional).
  4. **Pagination dots:** the existing `nasa-stage-dots` element, rendered directly
     below the central slide for every slide type (media and model-lens alike).
  5. **Right edge:** social action rail (like / inspect / save / share) as floating
     glass buttons, docked to the slide, not the viewport — it stays adjacent to
     whichever slide is active.
  6. **Bottom:** creator/caption/metadata block — provider handle, source/slide
     title, provenance badge row, hashtags. Tab bar below.
  All real/demo/simulated badges for the active slide are visible in this layout
  without opening another tab — Model Arena remains available separately as the
  *expanded* comparison view (Section 3.3), not as the only place the comparison
  is visible.
- **Real:** NASA Images API search results and media (image/video/audio) fetched
  browser-side, keyless; source titles, dates, NASA ids; on a model-lens slide, the
  pinned selected-source thumbnail and its metadata.
- **Simulated:** action-rail counts (`Demo counts` label stays attached to the rail,
  not hidden in a tooltip); preset "missions" are demo presets; demo prompt/task
  labels (Section 3.1a); on a model-lens slide, all four model panels' text.
- **Planned:** all non-NASA provider chips; the GitHub chip opens the existing
  planned-provider card.
- **Must-visible labels:** `Demo provider: NASA Images API`, `Real source` on the
  caption and on the model-lens slide's pinned source, `Demo counts` on the rail,
  `Planned` on every inactive chip, `Simulated model output` in every model-panel
  header on a model-lens slide, the prompt rail's `Demo prompts / simulated
  comparison tasks` label (Section 3.1a).
- **Visually dominant:** the central slide (media or model-lens). The slide gets
  ~70–75% of the first viewport's height (Section 5.6 sets the exact figure).
- **Reduced/hidden:** hologram-layer effects flatten to 2D on mobile (Section 4.9);
  the provider orbit ring does not render anywhere on this screen; nebula washes
  reduce to a single gradient; the Overview secondary identity composition
  (Section 2.5) is not present here at all.

#### 3.1a Model-lens slide (required feed slide type)

A model-lens slide is a first-class slide in the same vertical feed as media
slides — not a separate screen. Contents, top to bottom within the slide frame:

- **Pinned source header:** the selected real source's thumbnail, provider name,
  and provenance metadata (capture date, NASA id or equivalent), with a `Real
  source` badge. This is what makes the comparison honestly "over one real
  source" rather than a floating claim.
- **Four model panels**, stacked vertically on mobile: **Fable 5**, **Opus**,
  **GPT**, **GLM**, in that order. Each panel: bold model name, a one-line role tag
  (from `MODEL_ROUTING.md`), 2–3 lines of lens text, and a `Simulated model
  output` badge in the panel **header** (not the footer — consistent with Model
  Arena, Section 3.3).
- No panel receives a "winner" treatment; Fable 5's panel may use the primary
  violet edge (house model) but gains no size or glow advantage, matching Section
  3.3's rule for the expanded view.

**Demo prompt/task rail (Section 3.1's item 2):** a horizontal-scroll chip rail
sourced from the existing demo presets, always labeled `Demo prompts / simulated
comparison tasks` (never bare "Prompts" or "Tasks" without the qualifier — this is
a hard honesty requirement, not styling). Example labels (illustrative set, reuse
or extend the existing preset copy):

- "Visualize every asteroid in the solar system from NASA data"
- "Design a site plan for a 100-acre fitness retreat"
- "Reconstruct Apollo control panels from technical PDFs"
- "Simulate World Cup jersey supply chains by match outcome"
- "Show how solar flares affect the auroras"

Selecting a chip does not imply the described capability is implemented — only
that it is one of the deterministic local demo comparisons available today. The
rail must never be styled or worded in a way that implies every listed source
type (PDFs, supply-chain data, site-plan generation, etc.) is a live, implemented
capability; it remains explicitly a **demo prompt list over the one real NASA
source and the four simulated model lenses**, not a general task-execution
surface.

### 3.2 Source Arena — desktop (≥ 1024px)

**Desktop adaptation of the same primary hero composition (Section 3.1) — not a
different product.**

- **Layout:** three-column social cockpit. Center: the phone-proportioned vertical
  stage (existing centered phone-stage pattern kept — the mobile feed *is* the
  product and desktop frames it like an instrument), including the prompt/demo-task
  chip rail, both slide types (media and model-lens, Sections 3.1/3.1a), and
  `nasa-stage-dots` pagination below the stage. Left rail: prompt/mission rail
  (existing `mission-rail`/`search-rail`) restyled as tilted glass panels, maximum
  decorative tilt **~4°** toward center (Section 4.5 sets the ceiling; reduce
  further if legibility suffers). Right rail: model/source rail — on a model-lens
  slide this rail may expand the same four panels into a **2×2 arrangement**
  echoing the slide's own layout; plus the action rail docked to the stage edge.
  Holographic depth here is limited to these subtle card transforms — no orbit
  ring, no nebula arc, nothing behind the center stage competing with it.
- **Real / Simulated / Planned:** identical to mobile — layout changes, honesty
  labels do not.
- **Must-visible labels:** same set as mobile (Section 3.1), including `Simulated
  model output` on every model panel; the compact containment-hull frame (Section
  2.4/4.4) wraps the model rail / model-lens panel set with the caption
  `Simulated · read-only · zero-autonomy`.
- **Visually dominant:** the center stage — same as mobile. Desktop must remain
  recognizably the same product as mobile, not a separate dashboard.
- **Reduced/hidden:** side rails dim (opacity ~0.85) when the stage is interacted
  with. **The provider orbit ring and the Overview secondary identity composition
  (Section 2.5) do not render anywhere on this screen** — the orbit is
  Overview-only per Section 2.5's hard rules.

### 3.3 Model Arena — comparison view

This tab is the **expanded** version of the model-lens slide introduced in
Section 3.1a — the central feed already contains a compact model-lens slide;
this tab shows the same four panels at full size with no other feed chrome
(no action rail, no caption block, no pagination dots).

- **Layout:** top: compact selected-source card (thumbnail, title, `Real source`
  badge) — the single shared input, visually pinned so it is unmistakable that all
  lenses read the *same* source. Below: 2×2 grid (desktop) / vertical stack
  (mobile) of model lens cards: **Fable 5, Opus, GPT, GLM**. Each card: model name
  + role line (from `MODEL_ROUTING.md` roles), lens text, and a persistent
  `Simulated model output` badge in the card header — not the footer, the header.
  Hyperagent-style: cards are siblings of equal size; no "winner" styling.
- **Real:** the selected source metadata and thumbnail.
- **Simulated:** every word of lens text; the per-card badge is non-negotiable and
  must survive any future restyle.
- **Planned:** a dimmed footer row: `Planned: live model comparison via gated
  provider keys — not implemented`, so visitors see the roadmap without inferring
  a live capability.
- **Must-visible labels:** `Simulated model output` ×4, `Real source` ×1, the
  planned-footer sentence.
- **Visually dominant:** the four cards, equally. Fable 5's card may use the
  primary violet edge (house model) but gains no size or glow advantage.
- **Reduced/hidden:** no social action rail here; no engagement counts; nebula
  reduced so card text dominates.

### 3.4 Overview — secondary identity / cockpit status

- **Layout:** top: the compact secondary identity composition (core + provider
  orbit ring + containment hull, Section 2.5) with the one-paragraph positioning
  line beneath it — sized and weighted as a status-panel header, not a full-bleed
  hero. Below: three glass status panels — **Providers** (1 live demo / 1 planned
  demo / 9 planned), **Provenance** (admitted records, refusals, index freshness —
  from the content-free index and dated audit snapshot), **Operations** (loops
  configured/exercised, release tag, validation state — from the dashboard
  snapshot).
- **Real:** provenance counts (content-free `INDEX.json` read live), loop registry
  and run counts, release/version strings, validation snapshot (dated, labeled as
  a frozen snapshot).
- **Simulated:** nothing on this screen. Overview is the all-real screen; keep it
  that way.
- **Planned:** provider ring's planned chips.
- **Must-visible labels:** `v0.2.0` release marker, snapshot date on any frozen
  data, `Zero-autonomy containment` hull caption, `Planned` on planned chips.
- **Visually dominant:** the three status panels. The core+orbit+hull composition
  above them is a compact identity mark, not the dominant element of this screen
  or of the product — the Source Arena social feed (Sections 3.1/3.2) is the
  product's primary hero and required lead screenshot (Section 6.3).
- **Reduced/hidden:** no feeds, no media, no model copy; starfield at its sparsest
  so the hologram reads clean; the orbit composition itself stays visually quiet
  (static/ultra-slow, background-level, per Section 2.5's hard rules).

### 3.5 Context — provenance view

- **Layout:** header stating the contract in one line: `Reads the content-free
  index and a dated aggregate audit snapshot. Record bodies, notes, and refusal
  contents are never fetched.` Below: layered card stack per admitted record —
  front card: source id, type, trust, sensitivity, freshness badges; a subtle
  second card edge behind it (2–3px offset) suggesting the sealed immutable record
  beneath, which is deliberately *not* openable. Side rail: aggregate audit panel
  (counts by decision/trust/freshness, refusal count as a number only) inside a
  containment hull captioned `Aggregate-safe · write-once · human-gated`.
- **Real:** everything shown — index metadata and the dated audit aggregates.
- **Simulated:** nothing.
- **Planned:** a dimmed note that gate `apply` runs only as an operator-invoked
  CLI; no UI write path exists or is planned for the static site.
- **Must-visible labels:** the header contract line, the snapshot date, freshness
  badges (`stale` is badged, never hidden), `allowed_use`-filtered note.
- **Visually dominant:** the trust/sensitivity/freshness badge rows.
- **Reduced/hidden:** holographic depth is at its most restrained here — this is
  the audit room, not the show floor. No orbit, minimal nebula.

### 3.6 Roadmap / status view

- **Layout:** vertical milestone rail (Milestone A closed → Milestone B in
  progress → v0.3.0 target) rendered as stations along a violet orbit path — the
  orbit-map idea from the design system, flattened to a readable vertical spine.
  Each station: task id, one-line goal, state chip (`complete` green /
  `in progress` violet / `planned` dimmed). A `/roadmap` operator-command card
  links `docs/runbooks/MELLYCORE_ROADMAP_COMMAND.md`.
- **Real:** entries parsed from `ROADMAP.md` / `RUN_QUEUE.md` at load (existing
  behavior, kept — including Show more/Show less clamping).
- **Simulated:** nothing.
- **Planned:** future stations past v0.3.0, dimmed.
- **Must-visible labels:** state chips on every station; the release tag on the
  current station.
- **Visually dominant:** the spine and current-station marker.
- **Reduced/hidden:** long entry bodies stay clamped by default.

---

## 4. CSS-only 3D / holographic effect specification

Constraints (absolute): no Three.js, no WebGL, no Canvas, no SVG animation
libraries, no new dependency, no build step, no new fonts, no images added to the
repo for chrome purposes. Everything below is achievable with hand-written CSS
(custom properties, gradients, transforms, keyframes) on semantic HTML. New JS is
allowed only where Section 5.4 explicitly says so.

### 4.1 Scene depth model

- A single `perspective` value (~1100px) is set on each hologram-layer container
  (`.holo-scene`), with `perspective-origin` centered above the fold. Children that
  need real depth use `transform-style: preserve-3d`.
- Exactly three Z-planes exist, expressed as custom properties
  (`--z-space: -120px`, `--z-holo: 0`, `--z-feed: 40px` indicative). No element
  invents intermediate depths; this keeps the parallax coherent and cheap.
- Depth is communicated redundantly by: translateZ/scale, shadow softness
  (space layer: large soft violet shadows; feed layer: tight dark shadows), and
  border alpha (nearer = stronger line). If transforms are unsupported, the
  shadow/border cues alone still convey layering.

### 4.2 Orbiting provider ring

- Markup: an ordered list of provider chips inside a `.holo-orbit` container.
- Technique: the ring itself is a bordered ellipse (a rotated, scaled circle via
  `transform: rotateX(~68deg)`) with a faint conic-gradient sweep for the "traced
  orbit" look. Chips are absolutely positioned at fixed angles (precomputed
  per-chip `--angle` custom property; positions derived with CSS `sin()`/`cos()`
  where available, with a static hand-positioned fallback for older engines).
- Motion: one slow keyframe rotation of the ring container (period ≥ 60s), with
  chips counter-rotated so their text stays upright and readable at all times.
  Chips never blur or shrink below readable size; the NASA and GitHub chips also
  exist in the DOM as a plain visible list for a11y/no-JS (Section 4.10).
- The live NASA chip carries the only bright accent on the ring.

### 4.3 Central MellyCore core

- Concentric ring stack: 3–4 nested rounded elements with violet borders at
  decreasing alpha, plus a radial-gradient inner glow. Idle animation: a single
  slow opacity "breath" (period ~6s, opacity range ≤ 0.15) — the only permitted
  idle pulse in the whole UI.
- The wordmark stays HTML text (not an image), so it scales and stays selectable.

### 4.4 Safety containment hull

- A frame element using four corner ticks (border-image-free technique: corner
  pseudo-elements with two-sided borders) in `--holo-amber`, a 1px amber-tinted
  outline at low alpha, and a caption tab (small uppercase text on a dark chip)
  anchored top-left.
- **Sized to its content, not its screen.** On the central feed's model-lens slide
  and in Model Arena, the hull wraps the four-panel set at that set's own bounds.
  On Overview it wraps the compact core+orbit composition (Section 2.5), not the
  page. It never becomes a full-screen or full-viewport frame.
- The hull never animates. Stillness is the point: safety chrome is inert.

### 4.5 Floating source cards

- Feed-layer cards may hover-lift: translateY(-2px) + shadow deepen on
  hover/focus-visible, 150–200ms ease-out. On pointerless devices this state
  simply never fires; no JS needed.
- Desktop side rails get a static tilt (`rotateY(±4deg)` toward center) — a pose,
  not an animation. Text inside remains within readable skew tolerance; if any
  reviewer squints, reduce to ±2° or 0°.

### 4.6 Layered provenance / model cards

- The "sealed record beneath" effect (Section 3.5): each record card gets one
  pseudo-element offset 3px down-right, same radius, darker fill, 1px violet line
  at ~40% of the front card's alpha. Two layers maximum — a deck hint, not a
  skeuomorphic stack.
- Model lens cards in Model Arena use the same treatment with the magenta
  `Simulated` edge on the *front* layer only.

### 4.7 Depth shadows and glow

- Two shadow tokens only: `--holo-shadow-far` (large, soft, violet-tinted, for
  hologram-layer elements) and `--holo-shadow-near` (small, dark, for feed cards).
- Glow is always an outer box-shadow or a blurred pseudo-element behind the
  element — never `filter: blur()` on content, never text-shadow stacks on body
  copy. Glow alpha caps at 0.35.

### 4.8 Frozen screenshot pose

- A `holo-pose` class on the scene root pauses all animation
  (`animation-play-state: paused` scoped to the scene) and pins the orbit at its
  designed hero angle (the same angle used in keyframe 0%, so pausing is
  deterministic). Purpose: pixel-identical screenshots for the README/showcase
  pack and for visual QA diffing. Toggled by adding the class in devtools or via
  a URL hash handled by one line in existing JS (optional; class alone suffices).

### 4.9 Reduced-motion and mobile fallbacks

- `prefers-reduced-motion: reduce`: all animation (orbit, core breath, hover
  transitions beyond opacity) is disabled; the scene renders in the frozen pose.
  This is a hard requirement, not an enhancement.
- Mobile flatten (`max-width: 768px`): `perspective` removed, tilts zeroed; on
  Overview (the only screen where the orbit composition appears, Section 2.5) the
  orbit ring flattens to the plain provider chip rail; nebula reduced to one
  gradient, shadows simplified. The phone experience is intentionally the flat,
  fast, readable one — holographic depth is additive polish, never load-bearing
  for comprehension on any screen size.
- `prefers-contrast: more` / forced-colors: glow and glass alpha effects drop;
  borders go solid; badges rely on their text (they already carry words).

### 4.10 No-JS meaningful fallback

- `site/index.html` remains fully JS-free; any HSSC restyling of the homepage is
  pure HTML/CSS.
- On `dashboard.html`, all hologram-layer structure (core, orbit chips as a list,
  hull, panels, badges, positioning copy) must be static HTML styled by CSS —
  visible and correct with JS disabled. With JS off, the NASA stage shows a static
  glass panel stating that live search requires JavaScript and linking the NASA
  API docs; provenance/roadmap panels show their headers plus a "requires
  JavaScript to read local files" note. No blank screens, no unlabeled skeletons.

### 4.11 Performance guardrails

- Animate only `transform` and `opacity`. No animated box-shadows, no animated
  gradients, no `filter` animations.
- At most two simultaneously running animations per screen (orbit + core breath on
  Overview; zero to one elsewhere).
- Backdrop blur limited to topbar and ≤ 3 panels per screen; every blur has an
  opaque-enough fallback fill for engines without `backdrop-filter`.
- Target: no visible jank at 60Hz on a mid-range phone; if in doubt, cut the
  effect, keep the layout.

---

## 5. Implementation-ready task for Sonnet — `MELLYCORE-HOLOGRAPHIC-UI-SPEC-001`

Copy-paste task definition for the implementing agent (Sonnet 5 recommended).

**Task ID:** `MELLYCORE-HOLOGRAPHIC-UI-SPEC-001`
**Type:** UI implementation (CSS-first restyle of existing surfaces)
**Input spec:** this document, Sections 2–4. Product copy/labels in Section 3 are
requirements, not suggestions.

### 5.1 Files likely touched

- `site/css/dashboard.css` — primary work surface: add `--holo-*` tokens, the
  three-layer scene styles, orbit/core/hull components, card layering, fallbacks.
  Consider splitting new work into `site/css/holo.css` linked after `dashboard.css`
  if the file would exceed ~1600 lines; do not restructure existing selectors.
- `site/dashboard.html` — add the model-lens slide type and prompt/demo-task rail
  **inside the existing Source Arena panel** (`#tab-nasa` / `.dash-panel--nasa`),
  reusing the existing NASA media stage, provider chip rail, and `nasa-stage-dots`
  pagination element rather than duplicating them; add the compact secondary
  identity composition (core, orbit chip list, re-scoped hull) to the Overview
  panel only; add the re-scoped hull wrapper around the Model Arena panel set and
  the desktop model rail; badge markup upgrades; no-JS fallback panels. **Preserve
  every existing tab id, `role="tab"`/`role="tabpanel"` wiring, and navigation
  behavior exactly** — `dashboard.js` depends on them. **Do not replace or
  duplicate the existing safe Context tab implementation** (content-free index +
  dated audit snapshot only) — it is out of scope for this spec entirely.
- `site/css/*.css` for `index.html` **only if** the homepage hero is restyled to
  HSSC in the same task; otherwise leave `index.html` untouched and note it.
- `docs/tasks/MELLYCORE-HOLOGRAPHIC-UI-SPEC-001.md` — task report (required).
- `shared_context/AGENT_HANDOFF.md`, `shared_context/RUN_QUEUE.md`,
  `shared_context/PROJECT_STATE.md`, `shared_context/DESIGN_SYSTEM.md` — state
  sync; DESIGN_SYSTEM gains the HSSC summary (purple-first rule, three layers,
  containment hull, avoid-list).

### 5.2 CSS components to add

`.holo-scene` (perspective root), `.holo-layer--space/–holo/–feed`, `.holo-core`,
`.holo-orbit` + `.holo-orbit-chip`, `.holo-hull` + `.holo-hull-caption`,
`.holo-card--layered`, `.holo-badge` variants (real / live-demo / simulated /
planned / demo-counts / provenance / read-only), `.holo-pose`, shadow/z tokens,
reduced-motion block, mobile flatten block, forced-colors block.

### 5.3 HTML structure changes

Only additive: new sections/wrappers/badges as in Section 3, inserted inside the
existing Source Arena panel structure (reuse the NASA stage, provider rail, and
`nasa-stage-dots` — do not fork or duplicate them for the model-lens slide type);
no removal or renaming of existing ids, classes, tab roles, or aria wiring; native
elements first (`ol/li` for orbit chips, `details` stays for the GitHub card). The
Context tab's existing markup and data flow are untouched by this spec.

### 5.4 JS changes (only if absolutely needed)

Default: **zero JS changes.** Permitted maximum: (a) one hash/keydown toggle for
`holo-pose`, (b) class hooks if a new badge needs data already fetched. No new
fetches, no new endpoints, no new libraries, no behavior changes to search, tabs,
or provenance reads. If the task cannot be done within this, stop and report.

### 5.5 Accessibility requirements

- All information conveyed by color/glow is also conveyed by visible text.
- Contrast ≥ 4.5:1 for body/label text on its actual panel fill (measure over the
  most transparent state).
- `prefers-reduced-motion` fully honored (Section 4.9); `prefers-contrast` and
  `forced-colors` degrade gracefully.
- Focus-visible outlines on every interactive element, unclipped by transforms.
- Orbit chips: readable upright text at all animation phases; the same provider
  list must be reachable in DOM order for screen readers without depending on
  visual position.
- No content in pseudo-elements that isn't decorative.

### 5.6 Mobile requirements

**390×844 is the primary reference viewport for this entire spec** (360×800 is
checked as a secondary safety margin, not the design target).

At 390×844:

- Central slide (media or model-lens, Sections 3.1/3.1a) occupies **~70–75%** of
  the first viewport's height.
- No provider orbit ring anywhere on the Source Arena screen (Overview-only,
  Section 2.5).
- No monumental containment hull — only the compact re-scoped frame (Section
  2.4/4.4) around model-lens content, sized to fit inside the slide, never
  covering the whole screen.
- Zero horizontal page overflow at any scroll position.
- The core product story (real source + simulated model comparison + honesty
  labels) is legible within the first viewport without scrolling.
- All interactive controls ≥ 44×44px (existing `--cockpit-control`).
- Social/status labels and badges never occlude critical media or model-panel
  text — badges dock to card edges/headers, not as overlays crossing body copy.
- All badges visible without hover/long-press.

At 360×800: no horizontal overflow (secondary safety check only).

### 5.7 Browser QA checklist

- Chromium + Firefox (minimum; WebKit if available): every tab, desktop 1280×800
  and 1920×1080, mobile 390×844 emulation.
- JS disabled: dashboard renders the Section 4.10 fallbacks; no blank regions.
- `prefers-reduced-motion` emulated: zero running animations.
- `holo-pose` applied: identical screenshot two loads in a row.
- Zero console errors on all tabs; NASA search still works end-to-end
  (image/video/audio); Context tab still fetches only `INDEX.json` + the audit
  snapshot (verify in the network panel — this is a safety check, not a nicety).
- Verify no new network requests of any kind were introduced (fonts, images,
  CDNs). The request list before and after must differ by zero origins.

### 5.8 Validation commands (all must pass, from repo root)

- `python3 -m scripts.context_gate audit --json` → 0 findings (on Windows:
  `py -3.9`)
- `python3 -m scripts.context_gate rebuild-index` → byte-identical, 0 writes
- `python3 -m scripts.loop_ops validate` → PASS
- `python3 scripts/validate_project_state.py` → PASS
- `python3 -m unittest discover` → 245/245 (or current count) passing
- `git diff --check` → clean

### 5.9 Safety constraints (restate in the task report)

Static HTML/CSS/vanilla-JS only; no Three.js, no Canvas engine, no new
dependency, no build step; no backend, database, API key, secret, scheduler,
workflow YAML, deploy, push (commit only — push/PR is a separate approved step per
repo policy), or MellyTrade change; no live GitHub ingestion (GitHub Repository
stays a planned/demo card — implementing this spec does not authorize a live
fetch); no autonomous action of any kind. The keyless NASA Images API remains the
sole external data path. Every honesty label in Section 3 is present after the
restyle. No `ContextSource` record body, note, rationale, or refusal-log content
is ever fetched or rendered — the Context tab's existing content-free
index-and-snapshot-only contract (Section 3.5) is unchanged and untouched by this
spec. No canonical provenance record, refusal log, loop evidence file, or private
path is touched. Local preview binds to `127.0.0.1` only.

---

## 6. README / portfolio usage

### 6.1 Best one-liner

> **MellyCore AIOS — a safety-first AI operations cockpit: external sources in, provenance on everything, models compared side-by-side, zero autonomy by design.**

Alternate (more technical): *"A static, auditable AI-ops cockpit: swappable source
providers, a human-gated provenance store, and honest model-lens comparison — no
backend, no keys, no autonomous actions."*

### 6.2 GitHub README top section (structure to adopt)

1. Wordmark line + the one-liner.
2. One hero screenshot: Source Arena — 390×844 mobile model-lens hero matching Section 6.3. Overview (core + orbit + hull) may appear only as supporting imagery and must not be presented as the primary hero.
3. A three-badge honesty row rendered as plain text/shields: `static · no backend`,
   `zero-autonomy by design`, `v0.3.0`.
4. "What is real vs. simulated" table — four rows: NASA Images API (real, live,
   keyless) / provenance index + audit (real, repo data) / model lenses (simulated,
   labeled) / GitHub provider (planned, demo card). This table is the trust anchor
   of the whole README; keep it above the fold.
5. 60-second local preview instructions (`python -m http.server … --bind 127.0.0.1`).
6. Architecture-of-trust paragraph (Section 1.4 text).
7. Validation section: the exact commands from 5.8 with expected results.

### 6.3 Screenshots / GIFs to capture (in `holo-pose` unless noted)

1. **Hero — required first screenshot:** Source Arena mobile 390×844, on a
   **model-lens slide**: real selected source, four `Simulated model output`
   panels, the demo prompt rail, provenance/social badges, all legible in one
   frame. This is the lead image everywhere (README, showcase doc, portfolio) —
   it must visibly contain real source + simulated model labels + prompt/task
   context + social cockpit framing together.
2. **Desktop social-cockpit adaptation** — the same composition per Section 3.2,
   1920×1080 or 1280×800: center stage, prompt rail, model rail, action rail.
3. **Expanded Model Arena** — all four lens cards at full size with `Simulated
   model output` badges clearly readable (this screenshot *is* the honesty pitch).
4. **Overview** — the secondary identity composition (core, orbit ring, compact
   containment hull) plus the three status panels; captured as a supporting shot,
   not the hero.
5. **Context tab** — badge rows + aggregate audit hull.
6. One short GIF (≤ 8s, not posed): vertical source-feed scroll on mobile
   emulation, showing at least one media slide and one model-lens slide.
   Screenshots live outside the repo per existing evidence-pack policy, linked from
   the showcase doc.

### 6.4 What not to claim

Never in README/posts: "AI-powered", "autonomous agents", "real-time model
comparison", "integrated with NASA", "production", "platform". Never imply the
social counts are engagement. Never show the Model Arena cropped so the
`Simulated` badges are out of frame — treat that as a dishonest screenshot.

### 6.5 How to explain "static and zero-autonomy by design"

Short form for interviews/posts: *"It's not a stripped-down app — the constraint is
the thesis. Every capability an AI-ops product would need is here in its safest
possible form: providers behind provenance, models behind labels, operations behind
human approvals. The repo proves the discipline (write-once evidence, gated CLIs,
245 tests, honest labels), and the roadmap adds power only through spec → review →
gated implementation. That order — trust first, capability second — is the
product."*

---

## 7. Roadmap — next 10 tasks in order

| # | Task ID | Goal | Model | Effort | Type | Depends on | Before v0.3.0? |
|---|---------|------|-------|--------|------|------------|----------------|
| 1 | `MELLYCORE-PR3-CLOSEOUT-DOCS-001` | Record PR #3 merge (`fff50d2`) in PROJECT_STATE/ROADMAP/RUN_QUEUE; clear the two stale "review pending" claims; sync release posture | Sonnet 5 | Low | docs | — | Yes |
| 2 | `MELLYCORE-POSITIONING-REFRESH-001` | Apply Section 1 canonically: README top section per 6.2, homepage/dashboard copy aligned to the five claims + never-claims | Sonnet 5 | Medium | docs | 1 | Yes |
| 3 | `MELLYCORE-PROVIDER-HONESTY-POLISH-001` | Read-only sweep then fix pass on every provider/model/count label (the open GitHub-card review folds in here); verify badge set matches 2.6 | Sonnet 5 | Low–Med | review + UI copy | 2 | Yes |
| 4 | `MELLYCORE-HOLOGRAPHIC-UI-SPEC-REVIEW-001` | Independent review of THIS spec: honesty-label completeness, a11y/fallback soundness, CSS feasibility, purple-not-blue rule | Fable 5 | Medium | review | — | Yes |
| 5 | `MELLYCORE-HOLOGRAPHIC-UI-SPEC-001` | Implement HSSC per Section 5 (CSS-only 3D, additive HTML, ~zero JS) | Sonnet 5 | High | UI | 3, 4 | Yes |
| 6 | `MELLYCORE-HOLOGRAPHIC-UI-REVIEW-001` | Independent review of the implementation: QA checklist 5.7, reduced-motion/no-JS/mobile fallbacks, label survival, network-diff zero | Fable 5 | Medium | review | 5 | Yes |
| 7 | `MELLYCORE-SHOWCASE-PACK-002` | Capture the 6.3 screenshot/GIF set (evidence outside repo), update showcase doc + README image links | Sonnet 5 | Low | docs | 6 | Yes |
| 8 | `MELLYCORE-V0.3.0-RELEASE-REVIEW-001` | Fresh-clone validation at release candidate; tag `v0.3.0` — "Holographic Social Source Cockpit"; release notes with real-vs-simulated table | Fable 5 | Medium | release | 7 | Is v0.3.0 |
| 9 | `MELLYCORE-PROVIDER-ABSTRACTION-SPEC-001` | Docs-only: define the provider interface (metadata, capability flags, provenance hooks) so a second *live* keyless provider can slot in later | Fable 5 | Medium | docs | 8 | No |
| 10 | `MELLYCORE-SECOND-LIVE-PROVIDER-001` | Implement one more real keyless public provider (candidate: Wikimedia/Wikipedia API — public, keyless, non-space, breaks the NASA monoculture) | Sonnet 5 | Medium | UI | 9 | No |

Push/PR/merge for each remains a separate operator-approved step per repo policy.

---

## 8. Hard recommendation

**Do immediately:** Tasks 1–3 (closeout, positioning, honesty polish) — cheap,
docs-first, and they make every later screenshot honest by construction. Then run
the spec review (4) before any pixel work.

**Avoid:** starting the holographic implementation before the honesty polish
lands (you would restyle labels that are about to change); any Three.js/WebGL
temptation (it breaks the no-dependency story that makes this repo credible);
adding a second provider before v0.3.0 (scope creep that delays the visual
milestone); letting the Overview hero feature NASA imagery (the hero is MellyCore,
providers are chips).

**v0.3.0 is:** the Holographic Social Source Cockpit release — HSSC visual
language implemented, positioning refreshed, labels polished, showcase pack
captured, fresh-clone validation green. Purely presentational + docs; zero new
capability surface, which keeps the release safe and reviewable.

**Wait for after v0.3.0:** provider abstraction spec, the second live provider,
any live-model-comparison exploration (that one needs its own safety spec: keys
stay outside the repo, operator-gated, likely never in the static site at all),
GitHub Pages/deploy decisions, and the 3D graph page concepts.

**Do the cosmic/NASA visuals help or hurt?** They help — with one condition
already built into this spec. The nebula/starfield atmosphere is the memorable
signature that separates MellyCore from generic dashboards, and NASA media gives
the feed real, beautiful, legally clean content. The risk was never the aesthetic;
it was *narrative capture* — visitors reading it as "a NASA app." The spec
neutralizes that structurally: MellyCore sits in the center, NASA is one chip on
an orbit of many, space imagery is confined to the content stage, and the planned
second provider (task 10) is deliberately non-space. Keep the cosmos as the stage,
never as the star.
