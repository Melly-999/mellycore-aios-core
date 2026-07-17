# MELLYCORE-LIVE-COCKPIT-V2-001

## Outcome

`PASS_LIVE_COCKPIT_V2_COMMITTED_NO_PUSH`

Live Cockpit V2 is implemented as a dependency-free, static-first local dashboard. It completes Context Gate dashboard Phase I4, adds a real keyless NASA Images API arena, and adds a deterministic simulated model-comparison surface without introducing a backend, secret, provider connection, database, scheduler, or dashboard write path.

## Baseline

- Repository: `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`
- Branch: `publish/mellycore-main-001`
- Starting HEAD and remote branch SHA: `def9000b67daa3c1fd87dcc104ced124a9a7d4a2`
- Worktree: clean before implementation
- Commit message: `feat(aios): add live cockpit v2 dashboard`
- Push: not performed

## Visual direction

The implementation follows two generated visual specifications:

- Desktop concept: `C:\Users\highe\.codex\generated_images\019f6e97-f49f-7a31-8e43-f78978bb36d2\exec-50925e1b-c2fd-4436-908a-b80132223141.png` (`1536x1024`)
- Mobile concept: `C:\Users\highe\.codex\generated_images\019f6e97-f49f-7a31-8e43-f78978bb36d2\exec-7645b04b-93d4-4fc9-abcb-758f517e92ed.png` (`390x844` target)

Extracted design system:

- true near-black command canvas;
- electric violet and cyber cyan navigation/state accents;
- restrained red reserved for the real NASA-data marker;
- open mission/search/media/model rails rather than a nested card grid;
- geometric heading typography plus compact mono controls;
- dominant vertical 9:14 media stage on desktop and media-first mobile flow;
- fine borders, restrained glass, visible keyboard focus, 44px mobile action targets;
- vertical NASA deck and horizontal comparison-rail interaction cues;
- reduced-motion fallback.

No generated concept image is shipped as UI or as a repository asset. All product text, controls, labels, states, and media rendering are code-native.

## Implementation

### Cockpit shell

`site/dashboard.html`, `site/css/dashboard.css`, and `site/js/dashboard.js` now provide seven tabs:

1. Overview
2. Context
3. NASA Arena
4. Compare
5. Loops
6. Evidence
7. Roadmap

The existing Overview, Loops, Evidence, and Roadmap capabilities remain local/read-only. Models and the old mock Live stream are replaced by the clearer Compare surface and its explicit real-source-versus-simulated-output boundary.

### Context tab / Phase I4

The tab consumes:

- `shared_context/context_provenance/INDEX.json` live at page load;
- `site/data/context_audit_snapshot.json`, a clearly dated frozen copy of `py -3.9 -m scripts.context_gate audit --json`.

The UI renders only the index allowlist and aggregate audit fields. It filters by `allowed_use` before rendering:

- admitted `public_display` and `internal_summary_display` records may appear as index metadata rows;
- `internal_reasoning_only` records are counted only;
- rejected records are aggregate-counted, not identity-rendered;
- no canonical record body, claim, notes field, source identity, private path, refusal-log line, or refused content is requested;
- refusal data appears only as aggregate reason-code counts;
- stale and expiring states are visibly labeled rather than hidden.

Browser verification returned five display-safe rows, one reasoning-only record counted, seven valid records, six admitted, one rejected, one expiring, zero stale, one refusal, and zero findings. The Context DOM contained neither the reasoning-only record ID nor the rejected C8 record ID.

### NASA Arena

The browser calls NASA's public API directly:

- `GET https://images-api.nasa.gov/search`
- `GET https://images-api.nasa.gov/asset/{nasa_id}` for the selected media manifest

Supported controls:

- `q`
- `media_type` (`image`, `video`, `audio`, or comma-separated all-media search)
- `year_start`
- `year_end`
- `page`
- `page_size`

Search results render in a media queue and a vertical stage. Selected media resolves a browser-ready manifest asset when available. Image, video, and audio paths were exercised against the live service; all three returned results and resolved manifests. Network errors, empty results, invalid year ranges, and manifest failures have visible fallback states while local cockpit data remains usable.

The first-version integration uses no NASA API key and stores no token. NASA data is labeled `REAL NASA DATA` at the media stage and `NASA public API` in the command bars.

### Model comparison

The comparison surface includes Fable 5, Opus, GPT, and GLM panels plus task choices for Apollo, asteroid, solar flare, aurora, and Mars. Task selection updates the real NASA query and deterministic local comparison copy. Pause/resume controls only the simulated feed pulse.

Every model panel says `SIMULATED MODEL OUTPUT`. No prompt is sent, no provider is connected, and no output is represented as real model execution or NASA-authored text.

## Browser and visual QA

Preview command:

```text
python -m http.server 8791 --bind 127.0.0.1
```

Preview URL:

`http://127.0.0.1:8791/site/dashboard.html`

Browser/IAB verification covered:

- live Apollo image search: 509 hits, selected image rendered, manifest resolved;
- video search: 71 hits, selected `<video>` rendered, manifest resolved;
- audio search: 44 hits, selected `<audio>` rendered, manifest resolved;
- Mars task switch: query, selected NASA media, and all four deterministic mock lenses updated;
- pause/resume: only the simulated comparison feed state changed;
- Context tab: current index, seven safe aggregate metrics, five permitted rows, no protected identities in the DOM;
- all local data files returned HTTP 200;
- no canonical record or refusal-log HTTP request occurred;
- desktop `1536x1024` layout;
- mobile `390x844` browser emulation: no page-level horizontal overflow, 366px-wide media stage, 44px task/search action targets;
- visible focus and selected states;
- reduced-motion CSS fallback.

QA render files inspected with `view_image`:

- `C:\Users\highe\.codex\visualizations\2026\07\17\019f6e97-f49f-7a31-8e43-f78978bb36d2\mellycore-live-cockpit-v2-desktop-final.png`
- `C:\Users\highe\.codex\visualizations\2026\07\17\019f6e97-f49f-7a31-8e43-f78978bb36d2\mellycore-live-cockpit-v2-mobile.png`

Chrome headless has a 500px minimum screenshot canvas on this Windows host; the exact `390x844` state was therefore verified in Browser device emulation, while the saved mobile file is the closest headless capture of the same mobile breakpoint.

### Fidelity ledger

| Check | Concept evidence | Browser evidence | Result |
| --- | --- | --- | --- |
| Primary composition | mission rail + controls + vertical NASA stage + model rail | same four-zone desktop layout at 1536x1024 | matched |
| Palette and type | true black, violet/cyan, red real-source marker, mono controls | sampled implementation uses the same roles and high contrast | matched |
| Real vs simulated | NASA source red; model panels explicitly simulated | `REAL NASA DATA` and four `SIMULATED MODEL OUTPUT` labels persist in the DOM | matched |
| Desktop media treatment | dominant rounded 9:14 editorial stage | live NASA media fills a 570px bounded stage with readable metadata overlay | matched |
| Mobile structure | media first, tasks, filters, horizontal comparisons | 390px emulation preserves that order with no page overflow | matched |
| Context safety | aggregate context health only | seven safe metrics, five allowed rows, protected identities absent | matched and hardened |
| Interaction | vertical deck, task selector, pause/resume | wheel/touch navigation, tasks, page controls, and feed control exercised | matched |

Material fixes made during QA:

- added a data-URI favicon to remove the only console 404;
- raised mobile form controls to 44px;
- changed the mobile context metric row from an uneven wrapped grid to seven equal compact cells;
- corrected the mobile selected-tab state to match the rendered NASA surface.

Above-the-fold copy matches the accepted concept and user requirements except for intentional safety clarifications (`Static-first cockpit`, `No provider calls`) and the use of the actual NASA result title instead of concept placeholder copy. No material visual mismatch remains.

## Validation

| Command | Result |
| --- | --- |
| `py -3.9 -m scripts.context_gate rebuild-index` | PASS — 7 records, index identical, 0 writes |
| `py -3.9 -m scripts.context_gate audit --json` | PASS — 7/7 valid, 6 admitted, 1 rejected, 1 expiring, 0 stale, 1 refusal, 0 findings, 0 writes |
| `py -3.9 -m scripts.loop_ops validate` | PASS — 9 loops, no findings |
| `py -3.9 -m unittest discover -s tests -p "test_loop_ops*.py"` | PASS — 150 tests |
| `py -3.9 -m unittest discover -s tests -p "test_context_gate*.py"` | PASS — 95 tests |
| `py -3.9 -m scripts.validate_project_state` | PASS |
| `node --check site/js/dashboard.js` | PASS |
| `git diff --check` | PASS; only expected Windows LF/CRLF notices |

## Files changed

- `site/dashboard.html`
- `site/css/dashboard.css`
- `site/js/dashboard.js`
- `site/data/dashboard_snapshot.json`
- `site/data/context_audit_snapshot.json`
- `shared_context/ROADMAP.md`
- `shared_context/RUN_QUEUE.md`
- `shared_context/PROJECT_STATE.md`
- `shared_context/AGENT_HANDOFF.md`
- `docs/tasks/MELLYCORE-LIVE-COCKPIT-V2-001.md`

## Safety confirmation

- static-first HTML/CSS/vanilla JavaScript;
- no backend or build dependency;
- no secret, `.env` value, provider token, account ID, or API key;
- NASA Images API only, public GET requests, no authentication;
- no provider/model request;
- no UI write action;
- no canonical ContextSource record, refusal log, migration manifest, or loop evidence mutation;
- no database, MCP, scheduler, workflow YAML, deploy, push, or MellyTrade change;
- local preview bound only to `127.0.0.1`.

## Next recommended task

`MELLYCORE-LIVE-COCKPIT-V2-REVIEW-001` — independent read-only review of the data boundary, NASA failure modes, accessibility, responsive behavior, and honest real-versus-simulated labels before any separately approved publish task.
