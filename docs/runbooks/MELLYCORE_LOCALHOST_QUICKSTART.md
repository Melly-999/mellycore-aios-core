# MellyCore Localhost Quickstart

**Status:** Verified working (this task, `MELLYCORE-PROJECT-HISTORY-AND-LOCALHOST-BOOT-001`). Local preview only. No backend, no runtime, no provider connections.

## What this serves

The existing static `site/` scaffold — pure HTML/CSS, no JavaScript, no build step, no `package.json`, no dependencies. This is the fastest existing runnable application surface in the repository.

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

Loads `site/index.html`. CSS assets (`tokens.css`, `base.css`, `components.css`, `sections.css`) are served alongside it; no `/api/` calls and no external network requests occur.

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

## Forward-looking note: proposed Hybrid Source Arena renderer

`docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md` (status: PROPOSED, not
accepted) proposes a WebGL-enhanced Source Arena renderer using exactly one
pinned, vendored Three.js ESM module served from `site/vendor/`. If that ADR is
accepted and later implemented, this quickstart's guarantees are designed to
remain unchanged: no `package.json`, no build step, and no external runtime
network request — the vendored file would be served as a static asset from
this same `--directory site` root, not fetched from a CDN. As of this note, no
such file exists in the repository and this command continues to serve only
the current static scaffold described above.

## Related documents

- `[[../../README]]`
- `[[../showcase/static_preview_evidence_pack_001]]`
- `[[../tasks/MELLYCORE-PROJECT-HISTORY-AND-LOCALHOST-BOOT-001]]`
- `[[../decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001]]`
