# MellyCore Localhost Quickstart

**Status:** Verified working (this task, `MELLYCORE-PROJECT-HISTORY-AND-LOCALHOST-BOOT-001`). Local preview only. No backend, no runtime, no provider connections.

## What this serves

The command below exposes the static files under `site/` — no `package.json`, no build step, and no package installation for either page described below. This is the fastest existing runnable application surface in the repository. The two pages served from this root differ in what they do once loaded:

- `site/index.html` — the entrypoint — is pure HTML/CSS with **zero JavaScript**: no `<script>` tag, no `fetch()` call, no external request of any kind.
- `site/dashboard.html` — the current legacy Live Cockpit V2 / Social Source Arena dashboard, also served from this same root — loads `site/js/dashboard.js`, which renders a small, deterministic local Source Archive with zero external network requests. `MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001` (merged into canonical `main` via PR #15) removed the prior live NASA Images API calls this page used to make.

See "Current network behavior, by page" below for the exact, verified per-page detail (constants, call sites, and what remains true once the accepted Hybrid renderer ADR is eventually implemented).

- Static root: `site/`
- Entrypoint: `site/index.html`
- Supporting assets: `site/css/tokens.css`, `site/css/base.css`, `site/css/components.css`, `site/css/sections.css`

## Prerequisites already present

- Python 3.9 (invoked as `py -3.9`), standard library only (`http.server`). No `pip install`, no `npm install`, and none is required.

## Exact start command (Windows PowerShell)

Run from the repository root (`C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`):

```powershell
py -3.9 -m http.server 4173 --bind 127.0.0.1 --directory site
```

## Expected URL

```
http://127.0.0.1:4173/
```

Loads `site/index.html`. CSS assets (`tokens.css`, `base.css`, `components.css`, `sections.css`) are served alongside it; no `/api/` calls and no external network requests occur. **This guarantee covers `site/index.html` only** — see "Current network behavior, by page" below before opening `site/dashboard.html` from the same server.

## Current network behavior, by page (updated after NASA runtime retirement, PR #15)

Both pages served from this root are zero-external-network on canonical
`main` as of this note. Verified by read-only inspection of
`site/index.html`, `site/dashboard.html`, and `site/js/dashboard.js`:

- **`site/index.html` (the static landing/scaffold page):** contains no
  `<script>` tag, no `fetch()` call, and no external URL. Serving and loading
  it makes **zero** external network requests.
- **`site/dashboard.html` (the current legacy Live Cockpit V2 / Social Source
  Arena dashboard):** loads `site/js/dashboard.js`, which renders a small,
  deterministic local Source Archive — no `NASA_API_ROOT`, no `searchNasa()`,
  no external request of any kind, no API key. `MELLYCORE-SOURCE-ARENA-NASA-
  RUNTIME-RETIREMENT-001` (merged into canonical `main` via PR #15, merge
  commit `e0cbc332ff90f8787d981c9d86be717633f22d4d`) removed the prior live
  `https://images-api.nasa.gov` calls this page used to make on load and on
  every search; that prior behavior is historical evidence only, not current.
- **The paused, non-canonical WebGL Source Arena renderer** (see
  `docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md`, status
  **ACCEPTED** at the decision/specification level only): implementation
  exists solely on paused, open, unmerged PR #28 (`feat: add MellyCore 3D
  scene foundation`), blocked by physical Android Chromium Gate B
  (`OPEN / NOT EXECUTED`). Canonical `main` has no accepted implementation of
  this renderer today, and this quickstart's command does not serve it.
- **The vendored Three.js module** (`site/vendor/three-r164.module.js`):
  exists only on paused, open, unmerged PR #28. It is absent from canonical
  `main` and is not served by the command in this runbook today.

Do not read the "no external network requests" line under "Expected URL" above
as covering `index.html` only — both pages served by this command are now
zero-network on canonical `main`.

## How to stop the server

Press `Ctrl+C` in the terminal running the command above. If it was started in the background and the terminal is no longer available, find and stop it explicitly rather than leaving it running:

```powershell
Get-NetTCPConnection -LocalPort 4173 -State Listen | Select-Object -ExpandProperty OwningProcess | ForEach-Object { Stop-Process -Id $_ -Force }
```

Confirm the port is released:

```powershell
Get-NetTCPConnection -LocalPort 4173 -State Listen -ErrorAction SilentlyContinue
```

No output means the port is free.

## Confirmation: no backend involved

- No API routes, no database, no server-side logic — `http.server` only serves static files byte-for-byte.
- No provider API keys, secrets, or environment variables are required or read.
- No MCP, scheduler, or workflow automation is invoked by this command.
- Starting and stopping the server does not modify any tracked file in the repository.

## Known limitations

- This is a local preview mechanism only. It is not a deployment, and no live/public URL is enabled anywhere in this repository.
- The page is a static architectural blueprint (per its own on-page copy): "No live data, no provider connections, no execution capability." Interactive elements are limited to what plain HTML/CSS can do (links, `:hover`/`:focus` states, in-page anchors) — there is no JavaScript-driven interactivity.
- Automated screenshot capture was not available in the verification environment during this task's run; verification instead used HTTP status checks, full-page text extraction, browser console inspection, and network request inspection at both viewport sizes. Page content, structure, and asset loading were all confirmed with no errors at either viewport.

## Troubleshooting

**Port 4173 already in use:**

```powershell
Get-NetTCPConnection -LocalPort 4173 -State Listen -ErrorAction SilentlyContinue
```

If a process is listed, either stop it (see "How to stop the server" above) or start this server on a different port, e.g.:

```powershell
py -3.9 -m http.server 4174 --bind 127.0.0.1 --directory site
```

**`py -3.9` not found:** confirm the Python 3.9 launcher is installed and on `PATH`. This runbook intentionally avoids any other interpreter version or virtual environment requirement — the command uses only the Python standard library.

**Page loads but assets 404:** confirm the command is run with `--directory site` from the repository root (`C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`), not from inside `site/` itself (which would require dropping `--directory site`) or from any other working directory.

**Windows stale-checkout CRLF artifact:** if `py -3.9 -m scripts.context_gate audit --json` reports `non_deterministic_serialization` findings after a `.gitattributes` change to `shared_context/context_provenance/`, this is very likely a stale local working tree that predates the attribute being added, not a real regression — `.gitattributes` does not retroactively rewrite files already checked out with the wrong line ending. Before treating it as a real defect: validate against a fresh clone of the same commit, or run `git add --renormalize -- shared_context/context_provenance` in the existing checkout and re-run the audit. This does not change any provenance record content, only the working-tree line endings.

## Safety note

This server binds only to `127.0.0.1` (loopback) via `--bind 127.0.0.1`. It is not reachable from the local network or the internet. Do not remove or change the `--bind 127.0.0.1` flag, and do not port-forward or otherwise expose this server beyond the local machine.

## Forward-looking note: accepted Hybrid Source Arena renderer decision

`docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md` is now status:
**ACCEPTED** (2026-07-20, decision/specification level only) — it decides that
a WebGL-enhanced Source Arena renderer using exactly one pinned, vendored
Three.js ESM module served from `site/vendor/` is permitted, subject to its
own separately-authorized implementation task. The NASA runtime-retirement
task recorded in the ADR's Section 24 is complete and canonical on `main`
(merged via PR #15; see "Current network behavior, by page" above). The
renderer and vendored Three.js module (`site/vendor/three-r164.module.js`)
are implemented, but only on paused, open, unmerged PR #28 — not on canonical
`main`, and blocked by physical Android Chromium Gate B
(`OPEN / NOT EXECUTED`). This quickstart's command serves canonical `main`
only: as of this note it does not serve the renderer or the vendored Three.js
file, and continues to serve only the current static scaffold and legacy
dashboard described above. Once PR #28 is reviewed, accepted, and merged, this
quickstart's guarantees are designed to remain unchanged for the resulting
Source Arena page: no `package.json`, no build step, and no external runtime
network request — the vendored Three.js file would be served as a static
asset from this same `--directory site` root, not fetched from a CDN. The
ADR's acceptance authorizes none of that merge or implementation by itself.

## Related documents

- `[[../../README]]`
- `[[../showcase/static_preview_evidence_pack_001]]`
- `[[../tasks/MELLYCORE-PROJECT-HISTORY-AND-LOCALHOST-BOOT-001]]`
- `[[../decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001]]`
