# MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001

**Status:** `IMPLEMENTED_LOCALLY_PENDING_REVIEW` / `DRAFT_PR_OPEN_PENDING_VISUAL_ACCEPTANCE`. Not merged.

## Purpose

Retire the obsolete NASA Images API runtime dependency from the MellyCore
AIOS Live Cockpit V2 / Source Arena static prototype, replacing it with a
deterministic local showcase dataset and local filtering, without beginning
the future hybrid Source Arena renderer implementation.

## Canonical base

Branch `fix/mellycore-source-arena-nasa-runtime-retirement-001` was created
from canonical `main` at `026809fbd6a6c980bcc40325c2a7d3f899997b81` (the
merge commit of PR #14, verified as an ancestor of `clean-origin/main`
before branching). Local and remote feature branches from the prior task
(`docs/mellycore-odc-post-merge-state-sync-001`) were left untouched.

## Files changed

Implementation:

- `site/dashboard.html` — renamed the `nasa-*` id/class namespace to
  `source-arena-*` (tab button/panel, media stage, stage dots, search
  form, queue and its children) per
  `docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md` Appendix A;
  replaced the 5 astronomy-themed demo presets with 8 MellyCore-aligned
  archive categories; removed the NASA search form's year-range and
  page/page-size fields and pagination controls (no local equivalent);
  updated all NASA-implying copy (announcement banner, arena head note,
  provider rail, provider preview text, footer bar, tab subtitles).
- `site/js/dashboard.js` — removed `NASA_API_ROOT`, `searchNasa()`,
  `buildNasaSearchURL()`, `normalizeNasaItem()`, `resolveManifest()`,
  `chooseManifestAsset()`, the NASA request `AbortController` state, and
  the boot-time automatic NASA fetch. Added `ARCHIVE_CATEGORIES` (8
  categories) and `ARCHIVE_RECORDS` (8 deterministic local records) plus
  synchronous local filter/render functions (`filterArchiveRecords`,
  `renderArchiveResults`, `renderArchiveQueue`, `renderArchiveDots`,
  `renderArchiveStage`, `selectArchiveItem`). Rewrote `MODEL_COPY` to
  describe the 8 new categories instead of Apollo/asteroid/aurora/etc.
- `site/css/dashboard.css` — renamed `nasa-*` selectors to
  `source-arena-*`/`.dash-panel--source-arena`; removed the now-dead
  `.data-origin--nasa` rule; added procedural swatch styling
  (`.stage-media--procedural`, `.stage-media-glyph`,
  `.source-arena-queue-thumb`, `.compare-source-thumb--procedural`) using
  a CSS custom property (`--swatch-hue`) instead of any image;
  `.mission-rail` changed from `overflow: hidden` to `overflow-y: auto`
  (8 category buttons exceed the rail's available height on common
  desktop viewports — confirmed by measurement, see Validation) and the
  `--horizontal` modifier of `.task-selector` changed from a fixed
  5-column to a 4-column grid (8 items wrap 2×4 instead of 5+3).

Documentation / state sync (minimum necessary):

- `README.md` — corrected the roadmap table row and "NASA Images
  Disposition" section, which otherwise would have (truthfully, for
  canonical `main` today, but not for this branch's own tree) continued
  to claim no NASA runtime retirement exists in the repository.
- `shared_context/PROJECT_STATE.md`, `shared_context/ROADMAP.md`,
  `shared_context/RUN_QUEUE.md`, `shared_context/AGENT_HANDOFF.md` —
  updated the specific bullets/entries describing NASA runtime status to
  reflect local implementation pending review; did not rewrite unrelated
  roadmap items or historical/completed task entries.
- This report.

`site/index.html` was not modified — confirmed by direct grep to contain
zero NASA references before this task began.

## NASA dependency inventory (before removal)

Executable runtime dependency, all in `site/js/dashboard.js`:

- `NASA_API_ROOT = "https://images-api.nasa.gov"` constant.
- `searchNasa()` — performed a live `fetch()` to that root; invoked
  automatically from `boot()` on `DOMContentLoaded` (`await
  searchNasa({ preserveTask: true })`), before any user interaction, and
  again on every subsequent search/task-select/page-change.
- `resolveManifest()` / `chooseManifestAsset()` — a second NASA endpoint
  (`${NASA_API_ROOT}/asset/:id`) called per selected item to resolve a
  playable media URL.
- NASA-specific UI: `readNasaForm()` (year range, media type, paging),
  `renderNasaQueue()`/`renderNasaDots()`/`renderNasaStage()`, loading copy
  ("NASA Images API · public request · no API key"), error copy ("Demo
  provider (NASA Images API) could not be reached"), `aria-label="Show
  NASA result N"`, `aria-label="Demo provider search results"`, a public
  `images.nasa.gov` share-link builder, and NASA preview `<img>` sources.

Historical references left untouched (not executable, explicitly
time-scoped or task-naming): `docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md`,
`docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md`, `docs/runbooks/MELLYCORE_LOCALHOST_QUICKSTART.md`,
and all prior `docs/tasks/*.md` reports describing why the NASA prototype
existed.

## Replacement design

No pre-approved replacement name existed elsewhere for a "Source Archive"
label, but `docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md`
Appendix A already specified the exact identifier/naming transition
(`nasa-*` → `source-arena-*`, "Local source fixture" terminology), so that
mapping was followed instead of inventing a separate scheme.

The 8 local records use MellyCore-aligned categories (context, workflow,
safety, observability, model, routing, memory, orchestration) rather than
an astronomy theme, each summarizing an already-documented, verifiable
piece of this repository's own committed state (Context Gate, Loop
Operations Registry, Safety Contract, Project-Health Evidence Ledger, AI
Operations Intelligence Spec, Operations Data Contract, Memory Freshness
Monitor, Source Arena Hybrid Renderer decision). No external image URL is
used; a deterministic per-category hue drives a CSS gradient swatch
instead.

## Local/offline semantics

- Zero `fetch()`/`XMLHttpRequest` calls related to the Source Arena
  remain; `loadLocalData()`'s existing same-origin reads of
  `shared_context/**` and `site/data/**` are unrelated pre-existing
  behavior, not part of this retirement's scope, and were left unchanged.
- Filtering is synchronous, operates over the embedded `ARCHIVE_RECORDS`
  array, is case-insensitive, handles an empty query (returns all
  records), and has a truthful no-results state ("No local records
  matched that filter…").
- No API key, no remote image URL, no external host is referenced by the
  Source Arena surface after this change.

## Validation

**Static/network:** repository-wide `grep -rniE "nasa"` re-run after the
change; every remaining match is either the `--cockpit-nasa` CSS custom
property (a generic danger-red color token reused by unrelated UI —
non-executable, not user-visible NASA branding) or historical/task-naming
text in `docs/`. No `images-api.nasa.gov`/`api.nasa.gov` string remains
anywhere in `site/`.

**Browser smoke (executed):** served the repository root locally
(`py -3 -m http.server <port>`) and loaded `site/dashboard.html` in the
Browser pane.
- Console: no errors on load or during interaction.
- Network: zero requests to any `nasa.gov` host, at boot or after
  repeated filtering — confirmed via the network request log across a
  cold load and multiple interactions.
- Filtering: typed-query filter (`"safety"` → exactly the Safety Contract
  record), category-select filter, mission-rail category-button filter
  (`memory` → exactly Memory Freshness Monitor), top search-bar
  auto-category-detection (`"orchestration"` → Source Arena Hybrid
  Renderer, rail button activated, model-lens panel updated), clear
  search (restores all 8 records), and a deliberate no-match query (shows
  the truthful empty state, 0 records) — all verified via DOM inspection
  after each interaction.
- No `<img>` tag exists anywhere on the page after the change (`0`
  confirmed via `document.querySelectorAll('img').length`); procedural
  swatches render an actual visible gradient (confirmed via computed
  `background-image`), not a blank/broken placeholder.
- Model Arena (compare) tab: 8 category buttons render, selecting a
  record shows a "Local source fixture" label (not "Real source"/"Demo
  provider").
- The only remaining `nasa`-matching text found in the live DOM is a
  `RUN_QUEUE.md`-sourced Roadmap-tab entry naming this task itself
  ("...remove active NASA API calls...") — expected, since that tab
  renders the run queue verbatim and this task's own entry describes
  what it does; not a UI label or executable behavior.
- Desktop responsive: 1440×900 and 2560×1440 checked — no horizontal
  overflow (`document.documentElement.scrollWidth` vs `window.innerWidth`)
  at either. At 1440×900 the 8-button category rail's `scrollHeight`
  (764px) exceeds its `clientHeight` (720px); the `overflow-y: auto` CSS
  change (see Files changed) was confirmed necessary and sufficient — the
  rail scrolls internally instead of clipping the "Pause feed" control
  that sits below it.
- Mobile responsive: 390×844 and 430×932 checked — no horizontal
  overflow at either; the pre-existing mobile layout (horizontal
  scroll-snap rail) accommodates 8 buttons the same way it accommodated
  5.
- Accessibility (partial, not a full audit): confirmed zero remaining
  `aria-label`/`aria-labelledby` values matching `/nasa/i`; search input,
  stage-navigation, and action buttons retain descriptive
  `aria-label`s under their new local-fixture wording; keyboard-driven
  tab switching (existing `ArrowLeft`/`ArrowRight` handling) was not
  modified. No WCAG certification is claimed.

A caching artifact of the specific preview-browser session (a previously
cached HTML/JS pair from an earlier, differently-named tab default) caused
one early load in this session to show stale content; this was diagnosed
and ruled out by loading the same files from a freshly bound, never-before-visited
port, which rendered correctly on first load with no manual intervention.
This was a browser-cache artifact of the test session, not a defect in
the committed files.

**Validators run:**

```
python scripts/validate_project_state.py   → PASS
git diff --check                            → clean (no output, exit 0)
```

## Known limitations

- `--cockpit-nasa` (CSS custom property name) was intentionally left
  unrenamed — it is reused by several unrelated UI states (danger/error
  color for metrics, decision tags, form errors, provider-preview
  "not-live" badge) and renaming it repository-wide would be a token-level
  rename beyond this task's narrow scope. It is not user-visible NASA
  branding and has no executable NASA behavior attached.
- `.queue-pagination`/`.queue-page-btn` CSS rules (for the now-removed
  NASA pagination controls) were left in `dashboard.css` as inert,
  unused selectors rather than deleted, to keep the diff narrow; they
  match no element in the current markup and have no visual or
  functional effect.
- No automated accessibility audit tool was run; accessibility checks
  above were manual/targeted, not exhaustive.
- Visual acceptance (does the Source Archive read as a deliberate design
  choice rather than a degraded placeholder) has not been performed by a
  human or a dedicated visual-QA pass — that is the explicit purpose of
  the next task below.

## Explicit boundaries (not implemented by this task)

ODC adapter: `NOT_IMPLEMENTED`. Backend execution: `NOT_IMPLEMENTED`.
Runtime-consumed ODC schema integration: `NOT_IMPLEMENTED`. Provider
integration: `NOT_IMPLEMENTED`. Source Arena hybrid renderer:
`NOT_IMPLEMENTED`. CSS/DOM fallback renderer: `NOT_IMPLEMENTED`
(unchanged by this task). Three.js: `NOT_VENDORED`. Deployment:
`NOT_PERFORMED`. Release: `NOT_PERFORMED`. No broker, trading, or
MellyTrade-related file was touched.

## Exact next task

`MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-VISUAL-ACCEPTANCE-001` —
recommended model Fable 5, high effort — desktop/mobile visual QA,
product-coherence review, interaction review, and confirmation that the
Source Archive does not look like a degraded placeholder, before any
merge is considered.
