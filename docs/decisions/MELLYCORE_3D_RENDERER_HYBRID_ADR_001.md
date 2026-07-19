# ADR: MellyCore Source Arena Hybrid Renderer (WebGL-Enhanced, CSS-Complete-Fallback)

**ADR ID:** `MELLYCORE_3D_RENDERER_HYBRID_ADR_001`
**Status:** PROPOSED. Not yet accepted, not yet integrated into canonical `main`. This document authorizes no implementation, no dependency download, and no site/runtime change by itself.
**Date:** 2026-07-19
**Decision owners:** Operator (sole acceptance authority). Drafted by Claude Code under task `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-001`. Independent spec-compatibility and Git review is required from GPT-5.6 Sol / Codex (`MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-001`) before this ADR may be treated as accepted.

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

| Source / Section | Disposition | Replacement rule |
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

## 11. Shared-state model

A single plain JavaScript state object (no framework): selected slide/source id, active model-lens id, per-node truthful-state label, reduced-motion flag, viewport size, active-renderer flag. Written only by existing DOM controls. Read by whichever renderer is mounted. Both renderers observe the same object; neither renderer is a second source of truth.

## 12. Truthful-state semantics

Every visual element's truthful-state label — the integrated AI Operations Intelligence spec's `IMPLEMENTED` / `LEGACY_PROTOTYPE` / `SPECIFIED` / `PLANNED` / `SIMULATED` / `UNAVAILABLE` / `DEGRADED` / `STALE` / `UNKNOWN` / `ERROR` taxonomy (§1.9 of that spec, integrated into canonical `main` via PR #7; its modules remain `SPECIFIED`, not runtime-implemented), plus the visible `Real source` / `Simulated model output` / `Planned` badge set — is carried by DOM text in both renderers. Canvas never carries a label alone.

## 13. Accessibility model

Canvas is `aria-hidden="true"`. Every interactive affordance (selecting a model lens, an orbit node) has a real DOM control of record. Keyboard and screen-reader users operate entirely through DOM. Pointer/tap-on-canvas, if implemented, is an alias that calls the same state-change function the DOM controls call — never an exclusive capability.

## 14. Reduced-motion policy

`prefers-reduced-motion: reduce` → WebGL is not mounted at all; the CSS frozen pose renders instead. Checked at initialization and re-checked on `change`.

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

## 23. Mobile and desktop performance budgets

Targets are set for ordinary consumer mobile and desktop hardware, not the operator's development machine: ≤50 draw calls per frame; ≤~20,000 triangles across the whole scene; device-pixel-ratio capped at 2 on desktop and ~1.5 on mobile; a 60fps desktop target and a 30fps sustained mobile target; zero ongoing GPU/CPU cost while hidden or while `prefers-reduced-motion` is active. These are conservative, ordinary-device budgets and must not be validated only against a high-end development GPU.

## 24. NASA runtime-retirement boundary

Active NASA Images search/fetch/runtime integration is to be **removed** from the active Source Arena surface during the future implementation phase — not indefinitely isolated. New Source Arena runtime identifiers introduced by that future task must not use the `nasa-*` namespace (current examples observed by read-only inspection of `site/dashboard.html`, listed for reference only and not modified by this task: `#tab-nasa`, `.dash-panel--nasa`, `#nasa-stage`, `#nasa-stage-dots`, `#nasa-search-form`, `#nasa-queue`, and related form-field ids). The future Hybrid renderer must not initialize from, call, or depend on any NASA API. Historical task reports and `v0.2.0` release evidence describing why the NASA prototype exists remain untouched by both this ADR and the future implementation task; only active runtime code and identifiers are in scope for retirement, not the historical record.

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

This ADR (`MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-001`) → independent review (`MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-001`) → NASA runtime retirement (`MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001`, which may be executed as the first tightly bounded slice of the foundation task if the accepting review prefers that grouping) → Hybrid renderer implementation (`MELLYCORE-3D-SCENE-FOUNDATION-001`) → accessibility/performance QA (`MELLYCORE-3D-SCENE-ACCESSIBILITY-PERFORMANCE-QA-001`) → independent integration review (`MELLYCORE-3D-SCENE-INTEGRATION-REVIEW-001`).

## 32. Review and acceptance gates

Independent spec-compatibility, supersession-scope, Git-diff, and acceptance-criteria review by GPT-5.6 Sol / Codex is required before this ADR is treated as accepted. Independent architecture, accessibility, and failure-mode review by Claude Code informed this draft. Operator acceptance is the final gate; acceptance of this ADR does not itself authorize the implementation task — that requires its own separate authorization and review gates.

## 33. Future reconsideration triggers

Reconsider this ADR if: the vendored file's provenance cannot be fully verified per Section 21; fresh-clone byte-identical reproducibility fails; the CSS fallback is found to lack functional or accessibility parity with the WebGL path; or a future need emerges for a build tool (a separate ADR, not a silent expansion of this one).

## 34. Approval boundary

This document, in its current PROPOSED state, authorizes no commit beyond its own creation, no dependency download, no vendoring, no site/runtime change, and no push, PR, merge, or deployment. Moving this ADR to ACCEPTED requires an explicit operator decision recorded after the independent review task above; this document does not assert that acceptance has occurred.
