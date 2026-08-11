# MELLYCORE-M2-SHOWCASE-ACCEPTANCE-001

## OBSERVED

- Review baseline:
  `751556faf30622733aa5548cfcf4e43cdda2a225`
  (`docs: reconcile M2 pre-acceptance state`).
- Review branch: `docs/mellycore-m2-showcase-acceptance-001`.
- Review worktree:
  `C:\AI\MellyCore_Workspace\02_Worktrees\mellycore-m2-showcase-acceptance-001`.
- Chromium `151.0.7922.76` rendered the complete homepage through a controlled
  local HTTP server at 1440 x 900, 1024 x 900, 768 x 1024, and 375 x 812.
  Full-page evidence at 1440, 1024, 768, and 375 and detailed section captures
  were generated and inspected outside Git.
- The page is visually credible, distinctive, technically legible, and strong
  enough in most sections for client/recruiter review. Hero, Source Arena,
  Command Center, Runtime Constellation, Workspace ecosystem, Knowledge &
  Operations Graph, Safety, Tooling, and Operator Channel form a coherent
  static product story.
- At 375 px the header navigation extends beyond the viewport. The final
  `Static dashboard` link occupies x=326..429, leaving roughly half its text
  clipped by the viewport/header containment. The document width remains
  375 px, so there is no horizontal mechanism by which a visitor can reveal
  the rest of that header link.

## VERIFIED

- All seven pinned commits exist with the expected subjects and form the
  claimed direct-parent chain from Foundation through Pre-Acceptance State
  Reconciliation.
- Exactly two top-level product layers remain: Command Center and AI
  Workspaces.
- Exactly ten canonical workspace identities render in waves 4 / 3 / 3; no
  eleventh workspace exists.
- At 1440, 1024, and 768, document width equals viewport width and no off-screen
  non-decorative content or panel collisions were detected. At 375, document
  width also equals viewport width, but programmatic geometry found the mobile
  header list and final link beyond the right edge.
- The approximate 200% check used a 720 CSS-pixel viewport as the reflow
  equivalent of a 1440-pixel physical viewport at 200%. Document width stayed
  720 px, calibration rows reflowed without clipping, and Graph/Runtime content
  remained readable.
- Keyboard traversal followed the expected link order and exposed cyan focus
  outlines. At 375, focus reached `Static dashboard` while that link and its
  outline remained clipped. The skip link became visible and changed the hash
  to `#main-content`, but focus returned to `body` rather than transferring to
  the main landmark.
- Reduced-motion emulation matched
  `(prefers-reduced-motion: reduce)`: no animation name ran, maximum transition
  duration was 0.00001 seconds, and root scroll behavior changed from `smooth`
  to `auto`.
- Fresh load requested only `site/index.html` and four local CSS files, all
  HTTP 200. No JavaScript, CDN, external font, external image, provider,
  runtime, or other external request occurred. Chromium separately reported a
  console 404 for `/favicon.ico`.
- HTML parsed, duplicate ID count was zero, all six in-page anchors resolved,
  five unique local document/dashboard targets returned HTTP 200, and no fake
  button, form, or input was present. Complex CSS visuals include readable
  text alternatives and explicit ARIA labels.
- Static/planned/representative/derived boundaries are explicit at point of
  use. No material false live, connected, running, supported, authorized,
  sending, downloading, generation, inference, or execution claim was found.
- `site/**` remained byte-for-byte outside the acceptance diff.

## ACCEPTANCE FINDINGS

### Blocking

**M2-ACCEPT-01 — 375 px header link and visible focus are clipped.**

The canonical homepage specification requires an intentionally composed
mobile page and viable keyboard/visible-focus paths. At the required 375 px
viewport, the navigation row does not wrap, collapse, or provide an intentional
local scroller. Its final link extends 54 px past the viewport, only `Sta` is
visibly retained in the captured header, and keyboard focus does not make the
complete link or outline visible. This is a user-visible responsive and
accessibility failure on a mandatory acceptance viewport, so the current page
does not yet qualify as the First Commercial Design Showcase.

### Satisfied areas

- Hero communicates MellyCore AIOS, local-first identity, operator control,
  static truth, the accepted H1, and useful next navigation.
- Source Arena is evidence-led, operator-controlled, fail-closed, provenance
  bearing, and explicitly simulated/representative.
- Command Center, System Calibration, and Routing Invariants communicate an
  observatory/product projection without fake operational controls.
- Knowledge & Operations Graph remains derived, source-subordinate,
  provenance-bearing, approval-aware, readable on mobile, and explicitly not
  live ingestion.
- Runtime Constellation preserves orbital identity on desktop, an ordered
  mobile fallback, framework-neutral MellyCore ownership, and explicit
  reference/planned state semantics.
- Workspace truth is intact for all ten products, including Email approval,
  Voice non-authority/no-input, Video no-media/no-inference, Image no-generation,
  Downloader no-download, Ollama no-presence assertion, and Studio no editor or
  execution control.
- Safety, Tooling, and Operator Channel remain truthful and non-executing. The
  absent live contact endpoint does not block a milestone defined as a static
  design showcase.

## LIMITATIONS

The following are non-blocking relative to the rejection decision:

1. At 768 px, the ninth Shared Context card is an intentional lone final-row
   orphan; it is readable and does not break hierarchy.
2. `.card-grid--4` remains unused CSS with no rendered correctness effect.
3. `/favicon.ico` returns 404 on a fresh browser load and produces one console
   error, but all page-owned HTML/CSS resources succeed.
4. The skip link scrolls to `#main-content` without transferring DOM focus to
   the main landmark.
5. The mobile page is long (21,672 px at 375) and label-dense, creating some
   vertical fatigue, but content remains coherent and readable.
6. The rendered `MVP demo — Planned` roadmap label is not mapped explicitly to
   canonical M0–M5 terminology. It is ambiguous, but the roadmap otherwise
   distinguishes complete/current/planned/deferred states and does not promote
   a live, connected, or authorized capability.

## FINAL DECISION

`REJECTED`

M2 First Commercial Design Showcase is **not accepted**. `SHOWCASE_READY`
remains **NO**. M2 remains **not complete**. The otherwise strong showcase does
not override a visible responsive/focus defect at a required viewport.

## CANONICAL STATE EFFECT

- `PROJECT_STATE.md`: not changed; it already records M2 as ready for formal
  acceptance rather than accepted.
- `TASK_INDEX.md`: not changed; no completed/accepted status is asserted.
- `RUN_QUEUE.md`: not changed; unrelated global authority is preserved.
- `AGENT_HANDOFF.md`: updated because repository rules require a handoff after
  every meaningful task and because the rejected gate must not be lost.
- `ROADMAP.md`: unchanged.
- `site/**`: unchanged; acceptance did not repair its own evidence.
- Workspace backends, provider/runtime integrations, public release, push,
  merge, and deployment remain not done.

## NEXT STEP

Recommend only:

`MELLYCORE-M2-MOBILE-NAV-REMEDIATION-001`

Bound its implementation to the 375 px header/navigation containment and
visible-focus defect. After that bounded remediation is reviewed, rerun
`MELLYCORE-M2-SHOWCASE-ACCEPTANCE-001` independently. This record does not
authorize or execute either task.
