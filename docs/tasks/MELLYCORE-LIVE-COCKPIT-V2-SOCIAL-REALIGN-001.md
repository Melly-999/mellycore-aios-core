# MELLYCORE-LIVE-COCKPIT-V2-SOCIAL-REALIGN-001

## Outcome

`PASS_SOCIAL_SOURCE_ARENA_COMMITTED_NO_PUSH`

Live Cockpit V2 is visually and product-wise realigned into a vertical, social-video-style source cockpit with a deeper black/violet MellyCore identity. NASA is repositioned from "the product" to one demo provider proving real external-source ingestion. No backend, database, API key, provider secret, scheduler, deploy, or push was introduced.

## Baseline

- Repository: `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`
- Branch: `publish/mellycore-main-001`
- Starting HEAD: `6e804e3dcec24c1c7ae462136489428f7d245be9`
- Worktree: clean before implementation
- Commit message: `feat(aios): realign cockpit as social source arena`
- Push: not performed

## Visual direction

Pattern reference: TikTok/Hyperagent-style vertical social cockpits (pattern only — no TikTok branding, glyphs, or copy was reproduced). Applied direction:

- deep black canvas with a violet cast (`#05030a`) and layered purple radial gradients;
- violet identity dominant, magenta/pink (`#ff4fd8`) reserved for interaction highlights (hover, pressed actions, active dots, clamp toggles), cyan demoted to a secondary accent;
- subtle purple glow on surfaces, buttons, and the media stage;
- full-bleed vertical media stage (phone frame) as the visual centerpiece;
- right-side social action rail overlaid on the stage (like / inspect / save / share);
- bottom-left caption block over the media (provider handle, title, product explanation, hashtags);
- top "Find related sources" search pill plus a provider/related-source chip rail;
- bold white text over dark media, minimal chrome, intentional breathing room;
- mobile-first vertical feed at 390x844; desktop as a centered phone preview flanked by cockpit side panels.

## Product repositioning

- Tab "NASA Arena" → **"Source Arena"**; in-panel framing → **"External Data Arena"** / **"Live Source Arena"**.
- NASA → **"Demo provider: NASA Images API"** everywhere (announcement bar, arena rails, stage labels, compare card, footer).
- Apollo/Asteroid/Solar flare/Aurora/Mars → **"Demo presets"**.
- Model outputs → **"Simulated model lenses over one real source"**; every lens card keeps its persistent `Simulated model output` label.
- Real-vs-simulated labels remain explicit at point of use: `Real source`, `Demo provider`, `Simulated`, plus the existing `Committed local data` / `Audit snapshot` origins.
- Extensibility copy (visible in the provider chip rail and the stage caption): MellyCore can later ingest GitHub repositories, PDFs/docs, websites, changelogs, issues, CVs/job offers, research sources, marketplace/e-commerce data, and local project files. All are labeled **planned**; only the NASA Images API demo provider is live.

## Implementation

### `site/dashboard.html`

- Renamed tabs: `NASA Arena` → `Source Arena`, `Compare` → `Model Arena` (internal ids unchanged).
- New arena top bar: "External Data Arena" head, a `Find related sources` search pill (`#arena-search-form`), and a horizontally scrollable provider chip rail (1 live demo provider + 9 planned source types).
- Arena rails renamed and reframed (`Arena rail`, `Demo presets`, `Provider query` with a keyless-demo-provider note, `Model lenses`, `Lens feed`).
- Model Arena: replaced the debug-looking `compare-source-strip` with a proper selected-source card (`#compare-source-card`) carrying the real thumbnail, provider labels, title, and en-US date.
- Announcement/footer strips: `Demo provider: NASA Images API`, `No API key`, `No model calls`.

### `site/js/dashboard.js`

- **Social action rail** rendered onto the stage: like/save toggles with deterministic, seeded demo counts (labeled `Demo counts` in-UI and `not real engagement` in the ARIA label), an inspect toggle revealing the real NASA description excerpt (labeled `Real source description`), and share, which copies the public `images.nasa.gov/details/{nasa_id}` URL to the local clipboard (fallback: shows the URL inline). Nothing is posted or published anywhere.
- **Caption block**: provider handle (`@nasa-images-api · demo provider`), media title, short product explanation, future-source list, `#MellyCore #ExternalData #ModelArena #AIOS` tags, and a fine-print line (center · date · ID · manifest state).
- **Top search bar** wiring: syncs with the advanced `q` field, resets the year range and page (fixes a bug found in QA where preset year filters silently zeroed unrelated queries).
- **Formatting pinned to en-US/ISO-style**: manual zero-padded 24h clock/timestamps, `toLocaleDateString("en-US", …)`, `toLocaleString("en-US")` for hit counts.
- **Roadmap/RUN_QUEUE clamping**: entries longer than 200 characters render clamped to 3 lines with an accessible `Show more` / `Show less` toggle (`aria-expanded` tracked).
- Compare source card renderer; share/inspect state reset on media change; demo-provider phrasing in loading/error/status strings.

### `site/css/dashboard.css`

- Retuned tokens: purple-cast blacks and panels, `--cockpit-pink` interaction color, stronger `--cockpit-line-strong`, violet glow shadows.
- Layered purple radial gradients on the body; violet-glow surfaces; violet→magenta primary buttons.
- New components: arena top bar/search pill/provider chips, stage action rail, caption block, compare source card, clamp toggles.
- Stage: stronger violet border/glow; pagination dots moved to the left edge (action rail owns the right edge); pink active dot.
- Desktop arena grid rebalanced (`170px 250px minmax(370px,1fr) 410px`, breakpoint moved 1320→1240) so the phone stage is horizontally centered at 1280 wide (measured center 655 vs viewport center 640).
- Mobile (≤760px): scroll-fade masks on the announcement bar, preset rail, provider rail, lens feed, and compare rail; taller stage (9/14, 9/13.5 under 420px); caption clamped (title 2 lines, caption 3 lines) so the media stays dominant (caption overlay reduced from 65% to ~40% of stage height excluding gradient padding); compact 42px action buttons.
- Reduced-motion and forced-colors blocks retained.

## What was kept

- Safe Context tab — untouched read boundary: content-free `INDEX.json` + dated aggregate audit snapshot; no record bodies, notes, private paths, or refusal-log lines fetched.
- Real NASA Images API search (`/search`, `/asset/{nasa_id}`) with all filters (`q`, `media_type`, `year_start`, `year_end`, `page`, `page_size`).
- Simulated Fable 5/Opus/GPT/GLM comparison with pause/resume.
- Overview/Loops/Evidence/Roadmap local read-only surfaces.
- Static HTML/CSS/vanilla JS; no backend, no database, no API keys, no provider secrets, no push.

## Browser QA (127.0.0.1:8791, served from repo root)

- **Mobile 390x844**: vertical social cockpit confirmed — full-bleed media, right action rail inside the stage, bottom caption + hashtags, top search pill, provider chips with fade affordance; `scrollWidth == 390` (no horizontal overflow).
- **Desktop 1280x800**: centered phone stage (center offset 15px) flanked by preset/query rails left and the model-lens rail right; `scrollWidth 1265 < 1280`.
- **Real search**: Apollo 11 preset → 509 hits with media, manifest resolution, queue, and dots; top-bar search `aurora` → 803 hits (after the year-reset fix).
- **Interactions verified**: like toggle (`aria-pressed` flips, demo count increments), inspect (real description with `Real source description` label), clamp toggles on 18 long Roadmap/RUN_QUEUE entries (expand/collapse verified), preset selection, tab switching.
- **Labels**: `Simulated model output` on every lens card (8 instances across both surfaces), `Real source` / `Demo provider` on stage and compare card, `Demo counts` note on the action rail.
- **Leak check**: full-DOM scan found no filesystem paths, usernames, workspace paths, reasoning-only record ids, or rejected-record ids. The only "MellyTrade" match is committed loop-registry purpose text describing the separation boundary.
- **Console**: zero errors/warnings across all seven tabs.

## Validation

All commands run at implementation HEAD, all passing:

- `py -3.9 -m scripts.context_gate rebuild-index` → status `identical`, `writes_performed: 0`
- `py -3.9 -m scripts.context_gate audit --json` → 7 valid records, 1 aggregate refusal, 0 findings, 0 writes
- `py -3.9 -m scripts.loop_ops validate` → PASS (9 loops, Phase 1)
- `py -3.9 -m unittest discover -s tests -p "test_loop_ops*.py"` → 150 tests OK
- `py -3.9 -m unittest discover -s tests -p "test_context_gate*.py"` → 95 tests OK
- `py -3.9 -m scripts.validate_project_state` → PASS

## Safety posture

Unchanged: read-only cockpit; the keyless public NASA Images API remains the sole external data request; social counts are deterministic local mock numbers labeled as demo; share copies a public URL to the local clipboard only; no write path, provider call, secret, deploy, or push. The preview server bound to `127.0.0.1` only.

## Recommended next task

`MELLYCORE-LIVE-COCKPIT-V2-SOCIAL-REALIGN-REVIEW-001` — an independent read-only review of the social realignment: label honesty (real vs demo vs simulated), responsive QA on real narrow devices, and copy audit before any later publish/deploy task.
