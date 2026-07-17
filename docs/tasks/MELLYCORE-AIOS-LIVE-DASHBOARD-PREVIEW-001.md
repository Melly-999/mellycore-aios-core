# MELLYCORE-AIOS-LIVE-DASHBOARD-PREVIEW-001

## Task ID

`MELLYCORE-AIOS-LIVE-DASHBOARD-PREVIEW-001`

## Outcome

`PASS_LOCAL_DASHBOARD_PREVIEW_COMMITTED`

## Scope

Build the first local, interactive MellyCore AIOS dashboard preview: a cinematic cockpit UI reading real local project files where safely available, with mock data clearly labeled and no live provider calls, secrets, write actions, or trading surfaces of any kind.

This is a **read-only local preview**, not a runtime application. It is the first page in `site/` that uses JavaScript; the existing architectural homepage (`site/index.html`) remains pure HTML/CSS per its own documented scope — see the note added to `shared_context/PROJECT_STATE.md`.

## 1. Preflight

- Repo root: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios`
- Branch: `publish/mellycore-main-001`
- Starting HEAD: `87077b91468acaf9fb3d27879acc4f7070c11321`
- Worktree: clean before starting

## 2. Files added / changed

| File | Change |
| --- | --- |
| `site/dashboard.html` | New page: 6 tabs (Overview, Loops, Models, Evidence, Roadmap, Live), 3-column desktop grid, bottom status bar |
| `site/css/dashboard.css` | New stylesheet: tabs, badges (Ready/Running/Warning/Blocked), system map, expandable `<details>` cards, model cards, event log, responsive grid (stacks below 1024px) |
| `site/css/tokens.css` | Added two tokens: `--color-blocked-red` (reserved for Blocked state only) and `--color-teal-active` (Exercised state) |
| `site/js/dashboard.js` | New vanilla JS (no dependencies, no build step): tab switching, real-data fetch/render, mock live event stream, model-card selection |
| `site/data/dashboard_snapshot.json` | New frozen snapshot of real CLI output (`validate`, `audit --json`, test suite), captured once during this task |
| `site/index.html` | Two small additions: a nav link and a CTA anchor to `dashboard.html`. No other changes. |
| `.claude/launch.json` | New: local static-file-server dev config bound to `127.0.0.1` only |
| `shared_context/PROJECT_STATE.md` | One paragraph added noting the new interactive dashboard page and its safety posture |
| `shared_context/RUN_QUEUE.md` | Entry 44 added recording this task |

No Python, loop registry, state, or evidence files were modified. No `.env`, secret, or credential file was read or written.

## 3. Real data vs. mock data

**Real, fetched live at page load** (edit the file, reload the page, dashboard reflects it):
- `shared_context/ROADMAP.md` — current milestone, next-task bullet, Roadmap tab
- `shared_context/RUN_QUEUE.md` — task queue tail
- `shared_context/loops/LOOP_REGISTRY.json` — all 9 loop entries, Loops tab, system map nodes
- `shared_context/loops/states/project-health.state.json` — latest run pointer
- `shared_context/loops/runs/project-health/<latest>.json` — full run ledger (Evidence tab); the dashboard discovers the latest file by listing the directory, it does not hardcode a filename
- `shared_context/MODEL_ROUTING.md` — Models tab cards and Overview router preview
- `shared_context/SAFETY_CONTRACT.md` — Overview safety list

**Real, but a frozen snapshot** (captured once by actually running the commands; will not update on its own — see `site/data/dashboard_snapshot.json`):
- `py -3.9 -m scripts.loop_ops validate` → PASS, 9 loops, 0 findings
- `py -3.9 -m scripts.loop_ops audit --json` → `configured: 9, validated: 9, exercised: 1, human_approved: 0, production_enabled: 0`
- `py -3.9 -m unittest discover -s tests -p "test_loop_ops*.py"` → 150 passed, 0 failed

Loop-tier badges (Ready / Exercised / Blocked) on the Loops tab and system map use this snapshot for the tier classification, combined with the live-fetched registry for everything else. This is labeled in the UI as "snapshot, not live."

**Mock, explicitly labeled in the UI:**
- The Live tab's event stream — a client-side `setInterval` cycling through fixed sample strings prefixed `[MOCK]`. No backend, scheduler, or provider exists.
- The "Pause/Resume stream" control — toggles the mock interval only.
- Clicking a model-route card shows a "preview only — no request sent" panel using the documented role text from `MODEL_ROUTING.md`; no network request is made to any provider.

## 4. Validation

| Command | Result |
| --- | --- |
| `py -3.9 -m unittest discover -s tests -p "test_loop_ops*.py"` | 150 tests, OK (re-confirmed after this task's changes; no Python files were touched) |
| Local static server: `python -m http.server <port> --bind 127.0.0.1` | Started successfully; bound to `127.0.0.1` only per `shared_context/PROJECT_STATE.md`'s local-preview rule |
| Browser check (Overview, Loops, Models, Evidence, Roadmap, Live tabs) | All real-data fields render correctly; verified via DOM inspection (`document.querySelectorAll`, `getComputedStyle`) rather than relying solely on screenshots, because the session's screenshot tool downscaled/cropped desktop-width captures in this environment. `console` had zero errors throughout. |
| Tab switching, expandable loop cards (`<details>`), model-card selection (`aria-pressed` toggling), Evidence tab real-field rendering, Live tab pause/resume, mobile layout at 375px (no horizontal overflow, single-column stack) | All confirmed working |
| Build/lint | Not applicable — no JS bundler, linter, or `package.json` exists in this repository; the page is dependency-free vanilla HTML/CSS/JS by design, consistent with "keep implementation lightweight" |

No live backend integration is claimed. No provider was contacted. No repository mutation occurred from the dashboard UI itself (it is fetch-only, GET requests against local static files).

## 5. Local URL

`http://127.0.0.1:<port>/site/dashboard.html` — serve from the repository root with:

```
python -m http.server <port> --bind 127.0.0.1
```

(A `.claude/launch.json` entry named `mellycore-dashboard` is included for editors/tools that read that file, on port 8000. Port 8000 was unavailable on the machine used for this task, so validation used an alternate port; either works identically.)

## 6. Safety posture confirmed

- No secrets, `.env` values, or API keys added or read.
- No broker, trading, order, buy/sell/execute UX anywhere.
- No write actions from the UI; every fetch is a GET against local static files.
- No destructive git command run; no push.
- Server binds to `127.0.0.1` only, never LAN/internet, per the existing local-preview rule in `shared_context/PROJECT_STATE.md`.

## 7. Next task to bind real live data

Any future move from "frozen snapshot" to genuinely live loop-audit/test data would require a small local backend (or a build step that regenerates `dashboard_snapshot.json` on each loop run/test run) — out of scope here per "no real provider calls" and "keep implementation lightweight." The next natural step is the roadmap's own next item: the **weekly L1 pilot** (a recurring `project-health` run, persisted via `persist-run --apply` each time), after which this dashboard's Evidence/Loops tabs would show more than one real run without any code change, since they already read `shared_context/loops/runs/project-health/` dynamically.
