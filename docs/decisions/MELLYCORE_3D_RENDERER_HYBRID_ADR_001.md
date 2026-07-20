# ADR: MellyCore Source Arena Hybrid Renderer (WebGL-Enhanced, CSS-Complete-Fallback)

**ADR ID:** `MELLYCORE_3D_RENDERER_HYBRID_ADR_001`
**Status:** ACCEPTED (2026-07-20). Accepted by the Operator on branch `docs/mellycore-3d-renderer-hybrid-adr-001` at reviewed baseline commit `b95a741231d18ef712379837c7167aa22b37d42f`, following `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-003`'s `PASS_HYBRID_RENDERER_ADR_REVIEW_003_COMPLETE` outcome. Acceptance is a decision/specification-level authorization only — see the acceptance record below and Section 34. Integrated into canonical `main` via merge commit `f93be7018a1da3bba50eb66346b1f9e627a46dd2` (PR #8, `docs/mellycore-3d-renderer-hybrid-adr-001` → `main`) — see the canonical integration record below. This document still authorizes no dependency download, no vendoring, no site/runtime change, and no release or deployment by itself.
**Date:** 2026-07-19 (original decision); accepted 2026-07-20.
**Decision owners:** Operator (sole acceptance authority — exercised 2026-07-20; see acceptance record below). Drafted by Claude Code under task `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-001`. Independent spec-compatibility and Git review (`MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-001` through `-REVIEW-003`) is complete; `-REVIEW-003` returned `PASS_HYBRID_RENDERER_ADR_REVIEW_003_COMPLETE`, the gate this ADR required before operator acceptance.

> **Remediation note (2026-07-20):** Independent review
> `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-001` returned
> `NEEDS_FIXES` (findings HR-01 through HR-06). This document was amended by
> `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REMEDIATION-001` to close those
> findings: Section 7's supersession table is now marked explicitly
> not-yet-operative (HR-03); Section 11 splits DOM-owned, environment, and
> renderer-lifecycle state, and Section 14 specifies the exact reduced-motion
> transition ordering (HR-06); Section 23 replaces approximate performance
> language with an exact, reproducible measurement contract (HR-05); Section 24
> and new Appendix A define a complete, conditional NASA-transition
> supersession map (HR-01). This ADR's status remains **PROPOSED**; none of
> these amendments move it to ACCEPTED or authorize implementation. The exact
> next task is `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-002`.

> **Remediation note (2026-07-20, second pass):** Independent review
> `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-002` returned
> `NEEDS_FIXES` on two residual findings (RF-01, RF-02), not on HR-01 through
> HR-06, which it confirmed closed. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REMEDIATION-002`
> closed both: RF-02 by adding a row to Appendix A §A.1 mapping the
> Holographic UI Spec §6.2.4 planned README truthfulness-table entry (`NASA
> Images API — real, live, keyless`) to its future provider-neutral
> replacement, conditional on the same acceptance and implementation gates as
> every other Appendix A row; RF-01 by correcting
> `docs/runbooks/MELLYCORE_LOCALHOST_QUICKSTART.md`'s "What this serves"
> section, which previously described the entire `site/` scaffold as having
> no JavaScript even though `site/dashboard.html` in that same scaffold loads
> `dashboard.js` and makes live NASA Images API calls. This ADR's status
> remains **PROPOSED**; neither correction moves it to ACCEPTED or authorizes
> implementation. The exact next task is
> `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-003`.

> **Acceptance record (2026-07-20):** Independent review
> `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-003` returned
> `PASS_HYBRID_RENDERER_ADR_REVIEW_003_COMPLETE`, confirming HR-01 through
> HR-06, RF-01, and RF-02 all closed against reviewed baseline
> `b95a741231d18ef712379837c7167aa22b37d42f`. The operator then explicitly
> accepted this ADR at that exact baseline, on this exact branch, authorizing
> only the recording of that acceptance in one new signed local commit
> (`MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-ACCEPTANCE-001`) — no push, no
> PR, no merge, no Three.js implementation, no site/runtime change, and no
> NASA removal. This ADR's status is now **ACCEPTED**. Acceptance makes the
> decision-level supersession in Section 7 authoritative and makes NASA
> runtime retirement (Section 24, Appendix A) an accepted future requirement
> — it does not execute that retirement, vendor Three.js, or implement any
> renderer. The complete CSS/DOM fallback (Section 10) remains mandatory; the
> no-build-step and zero-external-runtime-network guarantees (Section 22)
> remain binding; DOM remains the sole authoritative carrier of labels,
> controls, navigation, and safety/approval state (Sections 11–13),
> unconditionally. The current legacy NASA runtime
> (`site/js/dashboard.js`, verified in
> `docs/runbooks/MELLYCORE_LOCALHOST_QUICKSTART.md`'s "Current network
> behavior, by page" section) remains present and unretired until a
> separately-authorized implementation task
> (`MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001`) removes it. No
> Three.js file has been downloaded or vendored; no renderer implementation
> exists. This acceptance authorizes no push, PR creation, merge, or
> deployment. Exact status tokens as of this record: decision status
> `ACCEPTED`; renderer implementation status `NOT_IMPLEMENTED`; Three.js
> dependency status `NOT_VENDORED`; NASA runtime-retirement status
> `ACCEPTED_REQUIREMENT_NOT_EXECUTED`; Git publication status
> `LOCAL_ONLY_NOT_PUSHED`. Exact next task:
> `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-ACCEPTANCE-REVIEW-001`.

> **Canonical integration record (2026-07-20):** Following
> `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-ACCEPTANCE-REVIEW-001`
> (`NEEDS_FIXES`, two persisted Section 7 / Appendix A gating-text
> contradictions), `-ACCEPTANCE-REMEDIATION-001` (closed both), and
> `-ACCEPTANCE-REVIEW-002` (`PASS_HYBRID_RENDERER_ADR_ACCEPTANCE_REVIEW_002_COMPLETE`),
> the operator separately authorized `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-PR-001`
> to push this branch to canonical `clean-origin` and open draft PR #8; then
> `-PR-REVIEW-001` (`PASS`), `-PR-READY-001` (marked ready; Sourcery's
> ready-state check did not trigger a fresh run because it had exhausted its
> own external weekly diff-character quota — waived by the operator as
> `WAIVED_UNAVAILABLE_BY_OPERATOR` / `EXTERNAL_WEEKLY_RATE_LIMIT_NOT_CODE_FAILURE`,
> not reported as a passing check — and this repository has no branch
> protection or required status checks on `main`), and finally
> `-PR-MERGE-001` merged PR #8 into canonical `main` via merge commit
> `f93be7018a1da3bba50eb66346b1f9e627a46dd2` (parents
> `06a7a421a06abbe38450d276af94985da8ddeba0` and
> `dcfcd8db2089e6f27b5aea59446244bf964f4aea`), confirmed by independent
> pre- and post-merge fresh clones (245/245 tests, all validators passing,
> all five commit signatures verified, all five commits confirmed ancestors
> of the new `main`). This ADR is now present in canonical `main`. None of
> this integration implements the renderer, vendors Three.js, retires NASA,
> or performs any release/deployment. Exact status tokens as of this record:
> decision status `ACCEPTED_CANONICAL_MAIN`; renderer implementation status
> `NOT_IMPLEMENTED`; CSS fallback status `NOT_IMPLEMENTED`; Three.js
> dependency status `NOT_VENDORED`; NASA runtime-retirement status
> `ACCEPTED_REQUIREMENT_NOT_EXECUTED`; Git publication status
> `MERGED_CANONICAL_MAIN` (PR #8); release/deployment status
> `NOT_PERFORMED`. Exact next task:
> `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-POST-MERGE-STATE-SYNC-REVIEW-001`.

---

## 1. Context

`docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md` is this repository's accepted, currently-binding visual contract for Source Arena — a 390×844 mobile-first model-lens hero. Its Section 4 defines the visual language entirely in CSS, with an absolute constraint against Three.js, WebGL, Canvas, or any new dependency. That CSS-only Source Arena has not been implemented; it remains a specification.

The operator has separately decided that Source Arena's next evolution should use a real-time WebGL 3D renderer as a progressive enhancement layered over a complete CSS/DOM baseline, with a single vendored, pinned Three.js ESM distribution as the only new dependency. This ADR is the written record of that decision and its exact boundary.

## 2. Problem statement

The repository's own accepted specification forbids the exact rendering technology the operator has chosen for Source Arena. Proceeding to a future implementation task without a written, narrowly-scoped decision would either silently violate an accepted spec or silently block a legitimate, already-decided product direction. This ADR resolves that conflict once, in writing, with an exact and minimal scope.

## 3. Existing conflicting constraints (quoted for the record)

- Holographic UI Spec §4: *"Constraints (absolute): no Three.js, no WebGL, no Canvas, no SVG animation libraries, no new dependency, no build step... Everything below is achievable with hand-written CSS."*
- Holographic UI Spec §5.4: *"Default: zero JS changes... If the task cannot be done within this, stop and report."*
- Holographic UI Spec §5.9: *"Static HTML/CSS/vanilla-JS only; no Three.js, no Canvas engine, no new dependency, no build step..."*
- Holographic UI Spec §8: *"any Three.js/WebGL temptation (it breaks the no-dependency story that makes this repo credible)."*
- `README.md`'s architecture-of-trust framing echoes the same "no Three.js/WebGL" language conceptually.

## 4. Operator-selected Hybrid direction

The operator has selected: Three.js/WebGL as the enhanced Source Arena visual renderer; a complete CSS/DOM fallback as the mandatory, always-available baseline; DOM as the sole authoritative carrier of content, controls, navigation, accessibility, and truthful-state labels; WebGL never owning safety, approval, or navigation state; canvas remaining decorative and `aria-hidden="true"`; a single vendored, pinned Three.js ESM distribution (`VENDORED_PINNED_THREE_ESM`) as the only acceptable dependency-acquisition method; zero build step; zero external runtime network requests; active NASA Images runtime functionality to be removed from the Source Arena surface during the future implementation phase, with historical evidence preserved untouched.

## 5. Decision drivers

- Genuine 3D depth and interactivity require a real GPU renderer; CSS 3D transforms cap out at flat-card illusions and cannot deliver the operator's intended experience.
- This repository's credibility mechanism is provable, reproducible, offline honesty — not literally zero dependencies as an end in itself. One pinned, checksummed, offline-verifiable dependency, fully disclosed with recorded provenance, preserves that mechanism without contradicting it.
- A complete, mandatory CSS fallback preserves every existing accessibility, no-JS, and reduced-motion guarantee unconditionally, regardless of WebGL availability.
- NASA Images has never been the product's identity (per `README.md`'s "NASA Images Disposition" and `shared_context/DESIGN_SYSTEM.md`); continuing to route the primary hero through NASA-named runtime identifiers and live NASA calls is inconsistent with the product's own stated positioning, independent of the renderer question.

## 6. Chosen architecture

A dual-renderer Source Arena: one shared, plain-JavaScript state object; two interchangeable presentation layers for the "space" and "hologram" visual layers (WebGL-enhanced or CSS-only); the "feed" layer (content, labels, controls) stays DOM in both cases, unconditionally.

## 7. Exact supersession map

**This table's decision-level supersessions are authoritative as of operator
acceptance (2026-07-20; see the acceptance record above).** Each
"Disposition" cell describes a specification-level supersession — which
constraint text no longer blocks the operator-selected direction — not an
implementation event. No renderer code, dependency, or site/runtime file has
been added or changed by acceptance itself; implementing the WebGL renderer
still requires its own separately-authorized task (Section 31).

| Source / Section | Disposition (accepted and operative at the decision/specification level as of 2026-07-20; implementation remains separately gated and unexecuted) | Replacement rule |
|---|---|---|
| Holographic UI Spec §4 (dependency/build-step clause) | **Narrowly superseded** | WebGL, Canvas, and exactly one vendored Three.js ESM dependency are permitted, but only as the enhanced renderer of Source Arena's central stage, and only when a complete CSS/DOM fallback exists and is authoritative whenever WebGL is unavailable |
| Holographic UI Spec §4.1–4.11 (CSS techniques) | **Preserved as the mandatory fallback spec** | Every technique becomes the required CSS/DOM baseline implementation, not diminished |
| Holographic UI Spec §5.4 (zero-JS ceiling) | **Narrowly superseded** | A renderer module and shared-state module are permitted, scoped to Source Arena capability-detection, WebGL lifecycle, and state already driven by existing DOM controls; no new fetches, no new endpoints, no behavior change to search/tabs/provenance reads |
| Holographic UI Spec §5.9 (dependency clause only) | **Narrowly superseded** | Per §4 above |
| Holographic UI Spec §5.9 (every other clause: no backend/database/key/scheduler/workflow-YAML/deploy/push, no live GitHub ingestion, no autonomy, no `ContextSource` body/note/refusal-log access) | **Preserved, fully binding** | Unaffected by this ADR |
| Holographic UI Spec §5.9 ("the keyless NASA Images API remains the sole external data path") | **Narrowly superseded** | Replaced per Section 15 (NASA runtime-retirement boundary) below — the future Source Arena makes no NASA API request at all |
| Holographic UI Spec §8 (no-dependency credibility narrative) | **Clarified** | Credibility rests on provable, reproducible, offline honesty, not on a literal zero-dependency count. A single vendored, checksummed, offline dependency with a complete fallback preserves that honesty differently but no less rigorously |
| `README.md` architecture-of-trust paragraph | **Clarified** | Same reasoning as §8 |
| `docs/runbooks/MELLYCORE_LOCALHOST_QUICKSTART.md` build/network guarantee | **Preserved exactly**, with a future factual addition once implemented | Zero build step and zero external runtime network requests both remain true under `VENDORED_PINNED_THREE_ESM`; a vendored file served from the same static root is not an external request |
| `shared_context/DESIGN_SYSTEM.md` "Leading Visual Metaphor" | **Clarified** | Space/hologram layers may be rendered by WebGL or by the CSS description; content/feed layer, honesty labels, and layer ordering are unchanged |
| Mobile composition (§5.6) | **Preserved** | Applies identically to both renderers |
| Desktop composition (§3.2) | **Preserved** | Applies identically to both renderers |
| Screenshot order (§6.3) | **Preserved** | Source Arena mobile model-lens remains required screenshot #1; Overview remains #4, supporting only |
| Truthful labels (§1.9 of the integrated AI Operations Intelligence spec; §2.6/§3.x of the Holographic UI Spec) | **Preserved, strengthened** | DOM remains the sole authoritative carrier of every label in both renderers |
| Source Arena / Overview / Model Arena relationship (§2.5, §3.1–3.4) | **Preserved** | Unchanged; WebGL scope is Source Arena's central stage only |
| Reduced motion (§4.9) | **Preserved, extended** | Extended so that `prefers-reduced-motion: reduce` also prevents WebGL from mounting at all |
| Accessibility (§5.5) | **Preserved, extended** | Canvas is `aria-hidden="true"`; every interactive affordance has a real DOM control; no canvas-exclusive capability |
| Repository dependency policy | **Narrowly superseded** (dependency count only) | Exactly one dependency permitted: a pinned, checksummed, vendored Three.js ESM build with a recorded provenance file; every other safety-contract item (no secrets, no keys, no runtime state) is unaffected |

## 8. Preserved requirements

Every honesty label; the 390×844 mobile-first primacy and its exact acceptance figures (E5/E6 in `MELLYCORE-HOLOGRAPHIC-UI-SPEC-REMEDIATION-001.md`); the screenshot order (E8); the containment-hull re-scoping (E7); Source Arena as the primary hero and Model Arena as its expanded relationship; Overview's core/orbit/hull as background-level, supporting-only, never inside the Source Arena viewport; the zero-build-step guarantee; the zero-external-runtime-network guarantee; every non-dependency clause in E10 and `shared_context/SAFETY_CONTRACT.md` (no backend, no database, no provider key, no scheduler, no workflow YAML, no live GitHub ingestion, no autonomy, no `ContextSource`/refusal-log/private-path access).

## 9. WebGL enhanced-renderer boundary

Owns: procedural deep-space background, the central Source Arena model-lens core, bounded orbital/model-lens nodes — mounted only inside the future renamed Source Arena stage element's bounds (current identifier `#nasa-stage`, to be renamed off the `nasa-*` namespace per Section 15). Does not own: text, labels, badges, navigation, tab state, or any state not mirrored in the DOM.

## 10. CSS/DOM fallback boundary

The complete Holographic UI Spec §4.1–4.11 CSS-only technique set (perspective scene, orbit ring, core, hull, layered cards, shadows, frozen pose), rendered unconditionally first, in the DOM, structurally present without JavaScript (§4.10's no-JS contract preserved).

## 11. State model (three explicit categories)

The prior draft's single "shared-state object" conflated three different kinds
of state with three different owners and lifetimes. This ADR replaces that
single model with three explicit, separately owned categories. All three are
read by whichever renderer (WebGL or CSS) is mounted; neither renderer is a
second source of truth for any of them.

### 11.1 DOM-owned interaction state

Written only through existing DOM/controller actions (a click, a tap, a form
submit already wired to `dashboard.js`): selected source/slide id, selected
model-lens id, user-controlled filters, and every truthful-state label value
(`Real source` / `Simulated model output` / `Planned` / etc.) whose source of
truth is DOM content. The renderer never writes to this category; it only
reads it.

### 11.2 Environment state

Written only by the browser/media/visibility platform, never chosen by
application code: viewport dimensions, device pixel ratio,
`document.visibilityState`, the Source Arena panel's own active/hidden state
(the existing `activateTab`/`panel.hidden` mechanism), the
`prefers-reduced-motion` media-query result, and the outcome of WebGL
capability detection (Section 15). Both the DOM controller and the renderer
read this category; neither one sets its values — the platform does.

### 11.3 Renderer lifecycle state

Written only internally by the renderer's own lifecycle manager, and exposed
**read-only** to DOM diagnostics — DOM/controller code may read it (e.g. to
show a non-blocking degraded-state note per Section 26) but never assigns to
it: lifecycle phase (uninitialized / initializing / running / suspended /
disposed / failed), which renderer is active (WebGL or CSS), WebGL context
state, first-frame-rendered status, suspended-vs-running status, and the last
recorded failure reason, if any.

The requirement that "WebGL never owns safety, approval, or navigation state"
(Section 4) is satisfied structurally: 11.1 and 11.2 — never 11.3 — are the
only categories a safety, approval, or navigation decision may read from.

## 12. Truthful-state semantics

Every visual element's truthful-state label — the integrated AI Operations Intelligence spec's `IMPLEMENTED` / `LEGACY_PROTOTYPE` / `SPECIFIED` / `PLANNED` / `SIMULATED` / `UNAVAILABLE` / `DEGRADED` / `STALE` / `UNKNOWN` / `ERROR` taxonomy (§1.9 of that spec, integrated into canonical `main` via PR #7; its modules remain `SPECIFIED`, not runtime-implemented), plus the visible `Real source` / `Simulated model output` / `Planned` badge set — is carried by DOM text in both renderers. Canvas never carries a label alone.

## 13. Accessibility model

Canvas is `aria-hidden="true"`. Every interactive affordance (selecting a model lens, an orbit node) has a real DOM control of record. Keyboard and screen-reader users operate entirely through DOM. Pointer/tap-on-canvas, if implemented, is an alias that calls the same state-change function the DOM controls call — never an exclusive capability.

## 14. Reduced-motion policy and exact transition ordering

`prefers-reduced-motion: reduce`, evaluated at initialization and re-evaluated
on the media query's `change` event (Section 11.2, environment state), gates
WebGL mounting entirely. The transition in each direction must follow this
exact, idempotent step order — repeating any step, or invoking it out of
order, must not throw, double-register a listener, or leak a resource (Section
19).

### 14.1 Transition: no-preference → reduce

1. Synchronously make the complete CSS fallback layer (Section 10) visible.
2. Mark WebGL promotion as disabled for the remainder of this preference state.
3. Cancel/suspend the renderer's `requestAnimationFrame` loop.
4. Stop renderer-owned animation and pointer/tap-on-canvas input aliases
   (Section 13); DOM controls remain fully functional throughout.
5. Release or dispose GPU resources per the permanent reduced-motion lifecycle
   policy (Section 19 governs exactly which resources this includes).
6. Leave all DOM controls, labels, focus state, and selection state (Section
   11.1) untouched by this transition.
7. Set renderer lifecycle state (Section 11.3) to `css-fallback / reduced-motion`.
8. At no point during or after this transition is a frozen or black canvas left
   visible — the CSS layer is authoritative and on-screen before any WebGL
   teardown step begins.

### 14.2 Transition: reduce → no-preference

1. Keep the CSS fallback visible and fully functional throughout; it is never
   hidden speculatively.
2. Re-run guarded capability detection (Section 15) from scratch.
3. Initialize WebGL only if capability detection passes.
4. Render and verify the first successful frame before any visual change
   (Section 16's first-frame rule applies identically here).
5. Only after that first frame succeeds, hide the decorative CSS visual layer
   (never the DOM labels/controls layer, which is never hidden by either
   renderer, per Section 4).
6. Preserve DOM labels, controls, focus, and selection state (Section 11.1)
   unchanged across this transition.
7. On any failure at steps 2–4, retain the CSS layer as the rendered result and
   record a non-blocking degraded state in renderer lifecycle state (Section
   11.3) — never surfaced as a blocking error to the user (Section 26).

Initialization, suspension, resumption, and disposal remain idempotent
(Section 19) regardless of how many times reduced-motion toggles back and
forth in a single session.

## 15. Capability detection

Capability detection is a guarded, actual context-creation attempt — not a mere feature check. Order: (1) evaluate `prefers-reduced-motion`; if reduced motion is set, do not attempt WebGL at all. (2) Otherwise, attempt `canvas.getContext('webgl2')` or `canvas.getContext('webgl')` inside a `try`/`catch`; a returned `null` or a thrown exception is treated identically as "WebGL unavailable," not as an error to surface to the user. The mere existence of `window.WebGLRenderingContext` is never treated as sufficient evidence that a context can actually be created.

## 16. CSS-first and first-frame fallback rule

The CSS fallback layer renders first, always, unconditionally. WebGL mount is attempted only after. The CSS layer is hidden only once WebGL's first frame has actually rendered without error. Any exception at any point during capability detection or first-frame rendering leaves the CSS layer visible and does not remove it speculatively.

## 17. Context-loss behavior

`webglcontextlost` → `preventDefault()` (to permit later recovery), suspend the render loop, immediately re-show the CSS layer. `webglcontextrestored` → reinitialize buffers/textures and re-attempt mount. If context loss recurs repeatedly within a session (implementation must define and record an exact threshold, e.g. more than once), the renderer permanently falls back to CSS for the remainder of that session rather than retrying indefinitely. The CSS layer is the permanent safety net, not a one-time fallback.

## 18. Visibility and tab lifecycle

Rendering is suspended (RAF loop paused, no per-frame GPU work) when `document.visibilitychange` reports hidden, or when the existing `activateTab`/`panel.hidden` mechanism marks the Source Arena panel as not active. Suspension is not the same as disposal: for ordinary, temporary tab switching, safe, reusable renderer resources (scene graph, geometries, textures, the WebGL context itself) MAY be preserved and simply not rendered, so that resuming does not require full reinitialization. This is a deliberate, corrected boundary — the read-only draft's requirement to fully dispose on every tab switch is replaced by this suspend/resume model for the ordinary case.

## 19. Resource cleanup and disposal

Full disposal (releasing geometries, materials, textures, the WebGL context, and all listeners) is required only on: permanent teardown of the page, page unload, an unrecoverable initialization failure, or repeated context-loss failure exceeding the implementation's defined threshold. Initialization, suspension, resumption, and disposal must each be idempotent — calling any of them more than once, or in any order relative to the others, must not throw, double-register a listener, or leak a resource. Validation for the later implementation task must demonstrate, across many repeated ordinary tab-switch cycles, that no listener, RAF handle, or GPU resource accumulates (e.g., via a heap-snapshot diff or an explicit resource-count assertion), distinct from and in addition to a separate test proving full disposal actually occurs at permanent teardown.

## 20. Dependency acquisition decision

`VENDORED_PINNED_THREE_ESM`. One pinned Three.js ESM distribution, committed under `site/vendor/` in the future implementation task. No CDN. No npm. No `package.json`. No build step, for this foundation slice.

## 21. Dependency provenance requirements

Before any vendoring occurs, the implementation task must verify and record, with evidence — not assumption: the official upstream source; the exact release version; an immutable download source (a tagged release asset or a commit-pinned URL, never a "latest" pointer); the license text and required attribution; the file's SHA-256; its byte size; its expected filename and ESM entrypoint; confirmation the vendored file contains only the module needed for Source Arena (core renderer/scene/camera/geometry), not unrelated bundled examples or assets; a secret/malware scan of the file before commit; an offline load test (server started with network disabled, page still renders); a fresh-clone reproducibility check (checksum matches after a clean clone); a network-panel confirmation of zero runtime CDN requests; a documented update process for future version bumps; a documented rollback process to a prior pinned version or to CSS-only. **None of these values are established, invented, or asserted by this ADR.** They are mandatory future verification fields for the implementation task.

## 22. Zero-build and offline guarantees

`docs/runbooks/MELLYCORE_LOCALHOST_QUICKSTART.md`'s `py -3.9 -m http.server` workflow is unchanged. No `package.json`, `node_modules`, or build command is introduced. Zero runtime network requests occur beyond the same-origin static server once the vendored file is in place.

## 23. Performance contract (exact, reproducible — future acceptance criteria)

The prior draft's approximate language (`≤~20,000`, `~1.5`, "ordinary consumer
hardware", unqualified "sustained") is replaced by the exact, testable contract
below. **Nothing in this section has been measured yet.** These are acceptance
criteria for the future implementation task
(`MELLYCORE-3D-SCENE-FOUNDATION-001`) and its QA task
(`MELLYCORE-3D-SCENE-ACCESSIBILITY-PERFORMANCE-QA-001`), not results claimed by
this ADR.

### 23.1 Geometry and renderer limits (hold for every sampled frame)

- Maximum draw calls per rendered frame: **50**.
- Maximum rendered triangles per frame: **20,000**.
- Maximum device pixel ratio: **1.5 on mobile**, **2.0 on desktop**.
- Exactly one active renderer canvas at any time.
- Zero renderer `requestAnimationFrame` callbacks while hidden, after the
  suspension grace period defined in 23.4.

### 23.2 Reference viewports and browsers

- Mobile reference viewport: **390×844 CSS pixels**.
- Desktop reference viewport: **1920×1080 CSS pixels**.
- Desktop reference browser: current stable Chromium-based desktop browser at
  test time, with the exact version recorded in the future task's evidence.
- Mobile reference browser: current stable Android Chromium browser on the
  named physical reference device below, exact version recorded in evidence.
- If no physical mobile device is available at test time, emulation results
  must be labeled **provisional** in that evidence and cannot alone produce a
  final physical-mobile PASS.

### 23.3 Reference mobile device

One reproducible physical baseline device, explicitly named in the future
task's evidence — for example a Google Pixel 6 or another explicitly named
device of comparable or lower capability. The future task must not claim
operator ownership of the device, and if the named device is unavailable at
test time, the physical-mobile gate must be reported as **unavailable**, never
as passed.

### 23.4 Measurement protocol

- 5-second warm-up after the first successful WebGL frame, excluded from the
  sample.
- 30-second active-animation sample window, no user interaction during the
  sample.
- Exact scene/slide and object count recorded alongside every sample.
- Desktop: average FPS ≥ **55**; p95 frame time ≤ **20 ms**.
- Mobile: average FPS ≥ **30**; p95 frame time ≤ **33.3 ms**.
- Draw-call and triangle limits (23.1) must hold for every sampled frame, not
  only on average.
- Zero uncaught console errors during the sample.
- Zero WebGL context loss events during the sample.

### 23.5 Hidden-idle test

- Hide the Source Arena tab or document.
- Allow a maximum **1-second** suspension grace period.
- Observe for 10 seconds.
- Renderer-owned RAF callback count must be exactly **0**.
- Renderer draw-call count must be exactly **0**.

### 23.6 Lifecycle / leak test

- Perform 20 Source Arena hide/show cycles.
- Exactly one canvas remains afterward.
- Exactly one active renderer lifecycle instance remains.
- No duplicate listeners or RAF loops.
- Post-GC heap must not show monotonically increasing retained renderer
  instances across the 20 cycles; if precise heap measurement is unavailable
  in the test environment, the future task must report that limitation
  honestly rather than claim this portion PASS.

### 23.7 Required evidence fields (future task, not this ADR)

Device, OS, browser and version, viewport, device pixel ratio, scene
description, sample duration, average FPS, p95 frame time, draw calls,
triangles, hidden-idle RAF result, and lifecycle/leak result — recorded for
every completed measurement run.

These targets apply regardless of the development machine used to author this
ADR or the future implementation; they must not be validated only against a
single high-end development GPU.

## 24. NASA runtime-retirement boundary (conditional, not yet operative)

**Nothing in this section has been executed.** Gate (a) — explicit operator
acceptance of this ADR — is now met (2026-07-20; see the acceptance record
above). Gate (b) — the future NASA runtime-retirement task's own separate
authorization, implementation, and review — is not met. This section records
what that future task would do once gate (b) is also met; it is not
performed by this ADR or by its acceptance. As of this acceptance, `site/`,
`docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md`'s binding requirements, and
every `nasa-*` identifier remain unmodified and fully in force.

If and when both gates above are met: active NASA Images search/fetch/runtime
integration would be removed from the active Source Arena surface — not
indefinitely isolated. New Source Arena runtime identifiers introduced by that
future task would not use the `nasa-*` namespace. The future Hybrid renderer
would not initialize from, call, or depend on any NASA API. Historical task
reports and `v0.2.0` release evidence describing why the NASA prototype exists
would remain untouched by both this ADR and the future implementation task;
only active runtime code and identifiers are ever in scope for retirement, not
the historical record.

**Appendix A** (end of this document) is the complete, exact conditional
supersession map and provider-neutral replacement contract for every
currently-verified `nasa-*` identifier, label, and behavior — closing the gap
left by this section's prior, partial identifier list.

## 25. Security considerations

A single vendored dependency, reviewed for provenance before inclusion (Section 21); no dynamic `eval` or remote script injection; canvas content has no privileged bridge to DOM state (no `postMessage` channel is needed or introduced); no new attack surface beyond parsing one additional static JS file already served by the existing static file server.

## 26. Failure behavior

Any WebGL failure — no context, an initialization exception, a shader compile failure, or repeated context loss — degrades to the CSS layer from the user's perspective, with at most one quiet, non-blocking note. Never a blank stage, never a broken canvas, never a lost navigation, label, or control.

## 27. Explicit non-goals

No backend, database, provider key, live model execution, autonomous operation, scheduler, merge, deployment, or approval-execution surface. No expansion into the full seven-module Cockpit. No change to the Context tab, Loop Operations, or Context Gate. No live GitHub ingestion. No build-tool introduction (a separate, future ADR would be required if that is ever proposed). No implementation of any kind is authorized by this ADR document itself.

## 28. Consequences and tradeoffs

Gains genuine 3D depth and interactivity for Source Arena. Costs: one real dependency (a JS payload step-change, on the order of 150–600KB depending on the exact module set vendored) that must be manually re-vendored and re-verified on updates; two renderer code paths that must be kept in parity; a documented, narrow exception to previously-absolute no-dependency language in three separate documents, each requiring careful, honest amendment rather than silent rewriting.

## 29. Rejected alternatives

- **CSS-only** — rejected as the sole path because it cannot deliver genuine 3D depth/interactivity; retained as the mandatory fallback, not discarded.
- **CDN import map** — rejected because it introduces a live third-party runtime network dependency, breaking the Localhost Quickstart's documented zero-external-network guarantee and fresh-clone offline reproducibility.
- **npm/bundler** — rejected for this foundation slice as the largest one-time architecture change this repository has faced (its first `package.json`/build step); may be reconsidered later under a separate ADR if JS tooling needs grow beyond this slice.
- **WebGL-only (no fallback)** — rejected outright; violates the explicit requirement that WebGL never be a prerequisite for safety, approval, audit, navigation, or truthful-state visibility.

## 30. Rollback strategy

At any time, forcing WebGL off — via capability-detection failure, a debug flag, or removal of the vendored file — must leave a fully functional, fully labeled, fully accessible Source Arena via the CSS layer alone. This is both the acceptance bar for the implementation task and the rollback path if the vendored dependency is ever rejected after the fact.

## 31. Implementation sequencing

**Completed decision/integration path** (every step below is done; none of it implements the renderer): ADR authored (`-ADR-001`) → independent review found defects (`-REVIEW-001`, `NEEDS_FIXES`) → remediated (`-REMEDIATION-001`) → residual defects found (`-REVIEW-002`, `NEEDS_FIXES`) → remediated (`-REMEDIATION-002`) → final ADR review passed (`-REVIEW-003`, `PASS`) → explicit operator acceptance (`-ACCEPTANCE-001`) → acceptance re-review found a narrow gating-text contradiction (`-ACCEPTANCE-REVIEW-001`, `NEEDS_FIXES`) → remediated (`-ACCEPTANCE-REMEDIATION-001`) → final acceptance review passed (`-ACCEPTANCE-REVIEW-002`, `PASS`) → branch pushed and draft PR #8 opened (`-PR-001`) → PR review passed (`-PR-REVIEW-001`, `PASS`) → PR marked ready, Sourcery's check waived as unavailable rather than passed (`-PR-READY-001`) → merged into canonical `main` via merge commit `f93be7018a1da3bba50eb66346b1f9e627a46dd2` (`-PR-MERGE-001`) → this documentation-state sync (`-POST-MERGE-STATE-SYNC-001`).

**Remaining runtime path** (every step below is not started and each requires its own separate authorization and review gate): NASA runtime retirement (`MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001`; may run as the first tightly bounded slice of the foundation task if the accepting review prefers that grouping) → Three.js provenance verification and vendoring inside the authorized foundation task → CSS/DOM fallback implementation → Hybrid WebGL Source Arena implementation (together, `MELLYCORE-3D-SCENE-FOUNDATION-001`) → accessibility/performance QA (`MELLYCORE-3D-SCENE-ACCESSIBILITY-PERFORMANCE-QA-001`) → independent integration review (`MELLYCORE-3D-SCENE-INTEGRATION-REVIEW-001`) → a separate implementation PR and its own merge → optional public deployment, itself requiring separate authorization.

The Operations Data Contract (`MELLYCORE-OPERATIONS-DATA-CONTRACT-001`) integration has **no ordering relationship** with the runtime path above: it is not a prerequisite, gate, blocker, dependency, sequencing step, or required prior task for this Source Arena renderer track or for `MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001`, and it does not supersede this track. Consistent with `shared_context/RUN_QUEUE.md`, renderer-track work may be independently authorized and reviewed on its own gates regardless of whether Operations Data Contract integration is pending, in progress, or complete. The Operations Data Contract remains `NOT_PRESENT_PENDING_INTEGRATION` as a separately-authorized, parallel roadmap track; if both tracks are ever active they proceed independently, each keeping its own authorization and review gates.

## 32. Review and acceptance gates

Independent spec-compatibility, supersession-scope, Git-diff, and acceptance-criteria review (`MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-001` through `-REVIEW-003`) was required before this ADR could be treated as accepted, and is now complete — `-REVIEW-003` returned `PASS_HYBRID_RENDERER_ADR_REVIEW_003_COMPLETE`. Independent architecture, accessibility, and failure-mode review by Claude Code informed this draft. Operator acceptance was the final gate and has now been exercised (2026-07-20; see the acceptance record above); acceptance of this ADR does not itself authorize the implementation task — that requires its own separate authorization and review gates.

## 33. Future reconsideration triggers

Reconsider this ADR if: the vendored file's provenance cannot be fully verified per Section 21; fresh-clone byte-identical reproducibility fails; the CSS fallback is found to lack functional or accessibility parity with the WebGL path; or a future need emerges for a build tool (a separate ADR, not a silent expansion of this one).

## 34. Approval boundary

This document is now **ACCEPTED** (2026-07-20; see the acceptance record above and `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-ACCEPTANCE-001`). Acceptance itself authorizes no dependency download, no vendoring, no site/runtime change, no NASA removal, and no push, PR, merge, or deployment — only the decision-level specification supersession in Section 7. Any future implementation, dependency acquisition, or NASA retirement task requires its own separate authorization and review gates, as Sections 20, 21, 24, and 31 already require.

---

## Appendix A: NASA transition supersession map (conditional, not yet operative)

This appendix is the complete, exact conditional map required to close
independent-review finding HR-01, extended by
`MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REMEDIATION-002` to also close
residual finding RF-02 (the §A.1 README truthfulness-table row below).
**None of this table is executed yet.** This ADR is now accepted (2026-07-20),
satisfying the first of the two gates every row requires. Every row's "Future
disposition" and "Provider-neutral replacement" still additionally require
the separately-authorized NASA runtime-retirement task
(`MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001`) to itself be
authorized, implemented, and reviewed before it takes effect. Until then,
every current identifier below remains exactly as verified in the repository
(read-only inspection of `site/dashboard.html`, `site/js/dashboard.js`,
`site/css/dashboard.css`), unrenamed and fully functional.

### A.1 Identifier map

| Category | Current identifier (verified in-repo) | Future disposition | Provider-neutral replacement |
|---|---|---|---|
| Active nav tab button | `#tab-btn-nasa`, `data-tab="nasa"` | Conditionally renamed | `#tab-btn-source-arena`, `data-tab="source-arena"` |
| Tab panel id | `#tab-nasa` (`aria-controls` target of the tab button) | Conditionally renamed | `#tab-source-arena` |
| Panel identifier (class) | `.dash-panel--nasa` | Conditionally renamed | `.dash-panel--source-arena` |
| Central-stage identifier | `#nasa-stage` (`.media-stage`) | Conditionally renamed | `#source-arena-stage` |
| Pagination-dot container | `#nasa-stage-dots` (`.stage-pagination`) | Conditionally renamed | `#source-arena-stage-dots` |
| Pagination-dot buttons | `.stage-dot` (class already provider-neutral) | Preserved unchanged | `.stage-dot` (no rename; see the `aria-label` row below for the text each dot carries) |
| Search-form identifiers | `#nasa-search-form` / `.nasa-search-form` (and its `input`/`select` children) | Conditionally renamed | `#source-arena-search-form` / `.source-arena-search-form` |
| Query-control / results-queue identifiers | `#nasa-queue` / `.nasa-queue`, `.nasa-queue-item`, `.nasa-queue-button`, `.nasa-queue-thumb`, `.nasa-queue-copy` | Conditionally renamed | `#source-arena-queue` / `.source-arena-queue`, `.source-arena-queue-item`, `.source-arena-queue-button`, `.source-arena-queue-thumb`, `.source-arena-queue-copy` |
| NASA API root / boot-time fetch behavior | `NASA_API_ROOT = "https://images-api.nasa.gov"` (`site/js/dashboard.js`); `searchNasa()` is invoked automatically from `boot()` on `DOMContentLoaded`, performing a live `fetch()` to that root before the user takes any action | Retired | No provider API root constant of any kind in the foundation slice; `searchNasa()`'s network call is replaced by a local-fixture loader (e.g. `loadSourceArenaFixture()`) that performs **zero** network requests; `boot()` calls the loader directly, not an async remote fetch |
| Loading-state copy naming NASA | `"NASA Images API · public request · no API key"` (loading string in `dashboard.js`) | Retired | Loader string names the local fixture, not any external provider |
| Result-count `aria-label` | `aria-label="Demo provider search results"` on `.nasa-queue` | Conditionally renamed | `aria-label="Local source fixture results"` |
| Per-dot `aria-label` | `aria-label="Show NASA result ${index + 1}"` | Conditionally renamed | `aria-label="Show source result ${index + 1}"` |
| Must-visible label: `Demo provider: NASA Images API` (Holographic UI Spec §3.1) | Spec text | Retired | Replaced by `Local source fixture`, from this ADR's truthful-label set (A.2 below) |
| `Real source` badge on a NASA-sourced item (Holographic UI Spec §3.1, §3.1a) | Spec text — currently accurate, since the source is genuinely live NASA data | Conditionally re-scoped | `Real source` remains usable post-retirement **only** where an actual bundled fixture record has verifiable, recorded provenance; otherwise the item must carry `Local source fixture` or `Planned`, never `Real source` by default |
| "NASA id" field in the pinned-source header (Holographic UI Spec §3.1a) | Spec text | Conditionally renamed | Generic fixture record id (e.g. `source id`), no provider-specific field name |
| No-JS fallback copy (Holographic UI Spec §4.10: "a static glass panel stating that live search requires JavaScript and linking the NASA API docs") | Spec text; **not yet implemented in `site/` today** | Conditionally renamed | Provider-neutral no-JS fallback copy stating the Source Arena fixture requires JavaScript to render, with no NASA-specific wording and no NASA API doc link |
| Mobile/desktop composition (Holographic UI Spec §3.1/§3.2) referencing "NASA media"/"NASA source" as example content | Spec text | Preserved structurally; content genericized | Layout, proportions, and composition rules (Sections 8–10 above) are unchanged; "NASA media" as an example content type is replaced by "bundled Source Arena fixture media" |
| QA selector: "NASA search still works end-to-end" (Holographic UI Spec §5.7) | Spec text | Retired, replaced | Future QA criterion: "Source Arena fixture renders end-to-end (image/video/audio fixture types) with zero network requests in the request log" |
| Screenshot requirement content (Holographic UI Spec §6.3) referencing NASA imagery as the pictured content | Spec text | Preserved structurally; content genericized | Exact screenshot composition, order, and required-labels rules (Section 7's "Screenshot order" row) are unchanged; "NASA imagery" as pictured content is replaced by "bundled Source Arena fixture imagery" |
| README "what is real vs. simulated" truthfulness-table row (Holographic UI Spec §6.2.4: the first of four planned rows reads `NASA Images API (real, live, keyless)`; this table is a planned README section and **does not exist in `README.md` today**) | Spec text describing an unimplemented future README section; currently fully binding as written, exactly like every other unimplemented clause of this spec | Conditionally replaced | This one row becomes `Local source fixture` — bundled locally, zero external runtime request, no backend/provider key/database/scheduler — labeled `Local source fixture` by default; `Real source` is used in its place only where the bundled record has verifiable, recorded provenance (see the `Real source` row above). §6.2.4's other three planned rows (`provenance index + audit`, `model lenses`, `GitHub provider`) do not describe NASA and are unaffected by this replacement. Like every row in this appendix: gate (a) — explicit operator acceptance of this ADR — was satisfied on 2026-07-20 at reviewed baseline `b95a741231d18ef712379837c7167aa22b37d42f`; §6.2.4 as currently written stays binding and the current NASA runtime remains present and unretired until gate (b) is also met. This replacement is not implemented yet and becomes operative only once the separately-authorized NASA runtime-retirement task is itself later implemented and reviewed. No historical README, task, or evidence statement describing why the NASA prototype exists is altered by this row |
| No-rename clause (Holographic UI Spec §5.3: "no removal or renaming of existing ids, classes, tab roles, or aria wiring") | Spec text, currently fully binding | Narrowly and conditionally excepted | This appendix is the ADR's sole, narrow, conditional exception to that clause, limited exactly to the `nasa-*` identifiers enumerated above, and only takes effect if/when both this ADR and the future NASA-retirement task are separately authorized and implemented |
| "NASA search must work" requirement (Holographic UI Spec §3.1 "Real:" row, §5.7) | Spec text | Retired | Superseded by: local-fixture search/filter must work identically over bundled deterministic data, with zero external requests |
| Historical evidence: `v0.2.0` release notes and NASA-referencing completed task reports under `docs/tasks/` | Existing files | **Untouched** | Not modified by this ADR or by any future task in this sequence; remains the historical record of why the NASA prototype exists |

### A.2 Future data contract (conditional; establishes no current behavior)

If and when the conditions above are met, the future foundation renderer:

- Uses deterministic, locally bundled Source Arena showcase data.
- Performs no external provider/API request of any kind.
- Requires no backend, database, provider key, or scheduler.
- Never claims simulated or fixture content is a real external source.
- Uses truthful visible labels drawn from this set: `Local source fixture`,
  `Simulated model output`, `Planned`. `Real source` is used only where an
  actual bundled source record has verifiable, recorded provenance (A.1's
  `Real source` row).
- Keeps DOM as the sole authoritative carrier of every label (Section 12,
  Section 11.1 above) — canvas never carries a label alone (Section 13).
- Leaves historical NASA evidence and task reports unchanged (A.1's last row).

### A.3 Preserved visual/product requirements (unaffected by this appendix)

Source Arena remains the lead hero; 390×844 remains the primary reference
viewport; Source Arena remains required screenshot #1; Overview remains
screenshot #4, supporting-only; Model Arena remains the expanded model-lens
relationship; pagination dots remain required, using the provider-neutral
successor identifier in A.1 once (and only once) the conditions above are met;
every accessibility and reduced-motion requirement in Sections 11–14 above
remains binding regardless of this appendix's status.
