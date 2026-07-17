# MELLYCORE-GITHUB-SOURCE-PROVIDER-DEMO-001

## Task ID

`MELLYCORE-GITHUB-SOURCE-PROVIDER-DEMO-001`

## Outcome

`PASS_GITHUB_PROVIDER_DEMO_COMMITTED_NO_PUSH`

## Scope

A product-positioning task, not a backend integration task: add a GitHub Repository provider-demo card to External Data Arena, showing that the arena is broader than NASA. NASA remains the current real, no-key media API demo provider; GitHub Repository becomes the next MellyCore-aligned planned/demo provider, positioned for architecture intelligence, repo analysis, docs analysis, system design review, and model-lens comparison. No chapter content from the reference repository was copied, scraped, or ingested; no backend, auth, API key, secret, database, scheduler, or provider runtime was added; no live GitHub fetch was implemented.

## 1. Preflight

- Repo root: `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios` (confirmed)
- HEAD: `d500ba29677187102c76552397a673fe9632101a` (confirmed, matching `clean-origin/main`)
- Working tree: clean before any edit
- Note: local `git` reports the ref as detached `HEAD` rather than a branch literally named `main` — this is carried over from the prior release-review task, where the stale, untracked local `main` branch (unrelated history, no upstream) was deliberately left untouched rather than force-reset. The commit content is byte-identical to `clean-origin/main`. This was flagged in the prior task's final report; the substantive checks (HEAD hash, `clean-origin/main` match, clean working tree) all passed.
- `clean-origin/main`: confirmed at `d500ba2`, matching local HEAD
- Old `origin` remote: present but not fetched, read, or pushed

## 2. What changed in Source Arena

Added to `site/dashboard.html` inside the External Data Arena topbar:

- Updated the arena head note and the provider-rail chip labels (`GitHub Repository · planned`, `Marketplace / e-commerce data · planned`) so the product story is legible at a glance.
- A new collapsed-by-default `<details class="dash-details provider-preview">` panel — no JavaScript required, the native disclosure widget handles expand/collapse — containing:
  - An intro sentence distinguishing NASA (current, real, proving live ingestion) from GitHub Repository (next planned/demo provider).
  - An honesty badge row: `Planned provider`, `External repository`, `Public source`, `Provenance required`, `Not live ingestion`.
  - A facts table (`context-rule-list`): Provider, Example source (linked), Source type, Purpose, Status, Real ingestion.
  - 26 short, original topic-title chips (exactly the topic names supplied in the task instructions — no chapter body text).
  - Six planned model-lens use cases (architecture summary, bottleneck detection, tradeoff extraction, scaling risk review, implementation task generation, provenance-aware source comparison).
  - A closing footnote restating that this is a positioning preview, not live ingestion, and naming the other planned-but-unimplemented source types.
- Added matching CSS in `site/css/dashboard.css` (`.provider-preview*`, `.provider-chip--next`, `.provider-topic-list`, `.provider-lens-list`) styled to match the existing purple/violet cockpit surfaces and chip conventions — no new colors or design language introduced beyond the existing `--cockpit-*` token palette.

No `site/js/dashboard.js` change was needed or made.

## 3. GitHub Repository labeling

Labeled consistently as **planned provider / demo source**, never live:

| Fact | Value |
| --- | --- |
| Provider | GitHub Repository |
| Example source | [`liquidslr/system-design-notes`](https://github.com/liquidslr/system-design-notes) (link only) |
| Source type | Public GitHub repository |
| Purpose | System design knowledge benchmark |
| Status | Planned / demo provider |
| Real ingestion | Not live — no frontend fetch is implemented |

## 4. Live GitHub fetch

**Not implemented.** No `fetch()` call to any GitHub API or the reference repository was added. The card is a static, product-positioning preview — consistent with "Not live ingestion unless you actually implement live frontend-only fetch safely," which this task deliberately does not attempt.

## 5. Copyright / provenance safety notes

- Only the reference URL (`https://github.com/liquidslr/system-design-notes`) is linked — never fetched, cloned, or scraped by this task or by any code added.
- The 26 topic labels are the exact short topic names supplied in the task instructions, used as plain original short labels (e.g. "Rate limiter", "Consistent hashing") — no chapter prose, explanations, diagrams, or any other body content from the reference repository was reproduced anywhere.
- No `ContextSource` record was created, edited, or referenced for this external source; no provenance metadata was fabricated.
- No private paths, refused content, raw claims, notes, or rationales were exposed.

## 6. Validation

| Check | Result |
| --- | --- |
| `py -3.9 -m scripts.context_gate audit --json` | see report below |
| `py -3.9 -m scripts.loop_ops validate` | see report below |
| `py -3.9 -m scripts.validate_project_state` | see report below |
| `py -3.9 -m unittest discover` | see report below |
| `git diff --check` | see report below |

(Filled in after the validation run in the same session; see the final chat report for actual figures.)

## 7. Browser QA

Verified against `python -m http.server 8791 --bind 127.0.0.1` serving `site/dashboard.html`, per the 11-point checklist in the task instructions (all seven tabs, Source Arena, NASA labeling, GitHub Repository planned-provider card, example source visible, no copied chapter content in the DOM, honest labels, mobile 390×844 no overflow, desktop 1280×800 no console errors, Context tab safety, purple visual identity). See the final chat report for the actual results.

## 8. Safety confirmation

- No backend, auth, API key, secret, database, scheduler, or provider runtime was added.
- No paid/provider API was called.
- Old `origin` remote was not fetched, read, or pushed.
- No `ContextSource` record was edited.
- No private paths, refused content, raw claims, notes, or rationales were exposed.
- Purple TikTok/Hyperagent-inspired Social Source Arena visual identity preserved; all pre-existing honesty labels preserved.
- This task's commit was **not pushed** (per instruction).

## 9. Next recommended task

An independent read-only review of this GitHub Repository provider-demo card (label honesty, responsive behavior, confirm no scraped content) before any further provider work.
