# MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-001

**Status:** `IMPLEMENTED_ON_BRANCH_DRAFT_PR_OPEN`. Not merged. First static
CSS/DOM renderer slice for the Source Arena stage.

## Purpose

Transform the Source Arena central stage from a single-record vertical media
card (which read as a social/TikTok-style feed: a large centered media post,
a vertical ♥/save/share engagement rail with demo counts, an
`@mellycore-source-archive` handle, `#hashtags`, and swipe/wheel/touch
"swipe or scroll to browse" navigation) into a **static holographic source
map** — an AI operations command surface: a central source core, orbital
source nodes (one per filtered local record), a connecting line to the active
node, an orbit ring, and a command inspector panel. This is a CSS/DOM-only
slice; no Three.js, WebGL, Canvas, dependency, network, or backend.

## Base

Branch `feat/mellycore-source-arena-renderer-static-slice-001`, created from
canonical `clean-origin/main` at
`9a5d1bb0bac80b567608f115f10cbd211b327aba` (the PR #16 merge commit).

## Files changed

- `site/js/dashboard.js` — replaced the stage's media/actions/caption markup
  and the wheel/touch swipe-feed handlers with a command-map renderer
  (`arenaNodesMarkup`, `arenaInspectorMarkup`, rewritten `renderArchiveStage`).
  Removed the now-dead social state (`likedIds`, `savedIds`, `inspectOpen`,
  `shareState`) and the demo-engagement helpers (`demoCount`, `shortCount`).
  Selection remains driven by the existing local Source Archive state — node
  click, the source queue, the dot selector, and the prev/next stepper — with
  no swipe-to-next-feed interaction.
- `site/css/dashboard.css` — removed the social action-rail, handle, hashtag,
  and share-note rules; added the `.arena-*` command-map styles (orbit, link,
  core, orbital nodes, inspector), a mobile flatten to a stacked command-panel
  list, and reduced-motion / forced-colors handling for the new elements.
- `site/dashboard.html` — added the `arena-stage-map` class to
  `#source-arena-stage`; replaced feed-grammar copy ("Opening the External
  Data Arena…", "Swipe or scroll to browse") with command language
  ("Initializing holographic source stage…", "Select a source node").

`site/index.html` was not touched. No dashboard IDs, tab roles, aria wiring,
search behavior, or other tabs were changed. Dataset records, category values,
and IDs are unchanged.

## Anti-social-feed confirmation

Removed: the vertical media-post composition, the ♥/save/share engagement
rail, demo like/save counts, the `@mellycore-source-archive` handle, the
`#hashtag` line, and the swipe/wheel/touch "next feed" navigation. The stage
now presents source nodes on an orbital map with a command inspector — a
map/table composition, not a content feed. No like/comment/share/follower
controls, no story/reel dots as the primary pattern, no swipe-to-next.

## Renderer boundary (unchanged truthful states)

- This slice is a **static CSS/DOM presentation** of the local Source Archive.
- WebGL hybrid renderer (per `docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md`):
  `NOT_IMPLEMENTED`.
- CSS-complete fallback renderer (the ADR's full §4.1–4.11 technique set):
  `NOT_IMPLEMENTED` (this is a narrow first slice, not that spec).
- Three.js: `NOT_VENDORED`. Canvas/WebGL: `NOT_USED`.
- Source Archive: local deterministic showcase data; external network
  `NOT_USED`; not live, not synchronized, not production-backed.
- Backend / provider integration: `NOT_IMPLEMENTED`. Deploy / release:
  `NOT_PERFORMED`.

## Validation

- `node --check site/js/dashboard.js` — PASS
- `python scripts/validate_project_state.py` — PASS
- `git diff --check` — clean
- No `images-api.nasa.gov` / `api.nasa.gov` in `site/`; no Three.js/WebGL/
  Canvas usage introduced (the only "WebGL" string is truthful record copy
  labelled "not yet implemented"); no external API or dependency added; no
  `site/index.html` change; no live/external or social-feed wording.
- Browser smoke test (served locally, `127.0.0.1`): zero console errors; 8
  source nodes render; node click, category filter, query search, empty
  state, and clear/reset all verified; compare-source card and model lenses
  stay synced to the active node.
- Visual: desktop 2560×1440 and 1440×900 show the orbital source map with no
  horizontal overflow; mobile 390×844 and 430×932 flatten to a stacked
  command-panel list with no horizontal overflow. Reduced-motion freezes the
  orbit sweep and core breath to a stable pose.

## Deferred / not in this slice

The ADR's full CSS-complete fallback spec, the WebGL enhanced renderer, and
Three.js vendoring remain the separately-authorized
`MELLYCORE-3D-SCENE-FOUNDATION-001` track — not started. VA-03 through VA-09
Source Arena polish items remain non-blocking backlog.

## Exact next task

`MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-REVIEW-001` — independent visual
and technical review of this draft PR (command-center vs social-feed
confirmation, accessibility, truthful-state boundary), then a
draft→ready→merge-gate sequence if clean. Do not begin the WebGL/Three.js
foundation track until this slice is reviewed and merged.
