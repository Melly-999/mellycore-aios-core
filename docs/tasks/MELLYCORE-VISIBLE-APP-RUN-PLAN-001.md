# MELLYCORE-VISIBLE-APP-RUN-PLAN-001

Status: complete (docs-only planning task — no UI implemented, no site/dashboard
code changed, no push, no merge, no release).
Model: Sonnet-class run plan produced in-session. Effort: Medium/High.

Purpose: a practical run plan that gets MellyCore AIOS visually usable,
impressive, and portfolio-ready as fast as possible while preserving the safety
posture (no backend, no keys, no database, no autonomous actions).

Preflight evidence (this session):

- Repo root confirmed; working tree clean before this doc.
- Only the canonical remote is configured in this clone; the old origin is not
  present and was not contacted. Fetch was canonical-remote-only.
- `main` tip = `fff50d2a49f7ee9824d1ad1dc29da81e8085ca2e` — the PR #3 merge
  commit is on main (verified with `merge-base --is-ancestor`).
- PR #4 exists, is **open and draft**, mergeable-state clean, and contains only
  commit `31abbea` (the HSSC spec `docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md`,
  its task report, and AGENT_HANDOFF/RUN_QUEUE sync). Not merged by this task.
- Inspected: `README.md`, `site/dashboard.html`, `site/css/dashboard.css`,
  `site/js/dashboard.js`, `shared_context/ROADMAP.md`, `RUN_QUEUE.md`,
  `PROJECT_STATE.md`, `AGENT_HANDOFF.md`, and the HSSC spec (present locally on
  the PR #4 branch).

---

## 1. Current State Snapshot

**On `main` (fff50d2):**

- `v0.2.0` Live Cockpit V2 / Social Source Arena: purple/black vertical social
  cockpit at `site/dashboard.html` (7 tabs), phone-frame media stage, right-side
  action rail with `Demo counts`, provider chip rail (1 live demo + 9 planned),
  top search pill, caption/hashtag block.
- Real keyless NASA Images API search (image/video/audio) — the only external
  data path. Simulated Fable 5/Opus/GPT/GLM model lenses, labeled per card.
- GitHub Repository planned/demo provider card (PR #3), `/roadmap` operator
  command docs (PR #3).
- Full trust stack: Context Gate I1–I4 (95 tests), Loop Ops (150 tests),
  245 total tests, three validators, seven canonical provenance records.

**Only in PR #4 (branch `claude/mellycore-holographic-ui-spec-sqgfs3`):**

- `docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md` — positioning + HSSC visual
  language + screen concepts + CSS-only 3D spec + Sonnet hand-off task +
  README guidance + 10-task roadmap. Docs only; authorizes nothing.

**Visible in the dashboard now:** the social source arena works and looks
intentional (deep black/violet, magenta highlights), NASA search is genuinely
live, honesty labels are present. It reads as a solid v0.2.0 — but there is no
hero identity (no MellyCore core / provider orbit / containment hull), the
Overview tab is informational rather than cinematic, and desktop framing is
functional rather than holographic.

**Missing for a strong public showcase:**

1. README leads with the older "Living Context Graph" story, not the cockpit /
   providers / provenance / model-arena story; no screenshots; no "open this,
   look at this" walkthrough; validation section lists only one of the four
   validator commands.
2. No hero visual (the HSSC core+orbit+hull) — nothing screenshot-iconic yet.
3. No screenshot/GIF showcase pack captured for the current UI.
4. **`PROJECT_STATE.md` is stale**: it still claims branch
   `publish/mellycore-main-001`, HEAD `6e804e3d`, and "Cockpit V2 remains a
   local static preview until a separate push/deploy task" — all pre-release
   claims contradicted by the shipped `v0.2.0` and the PR #3 merge. Its "Next
   tasks" list is also outdated.
5. `ROADMAP.md` is close to current (through PR #3 content) but does not record
   the PR #3 merge commit or PR #4's existence. `AGENT_HANDOFF`/`RUN_QUEUE` are
   current only on the PR #4 branch, not on main.

## 2. Fastest Visible Path

**Must do before screenshots** (in order):

1. PR #3 closeout docs — kill the stale PROJECT_STATE claims so every later
   artifact is written against true state.
2. PR #4 spec review → merge — the UI pass implements the merged spec, not a
   draft.
3. README positioning refresh — the "what to look at" walkthrough must exist
   before traffic arrives.
4. Provider honesty polish — labels must be screenshot-correct *before* they
   are photographed.
5. Hyperagent Social Cockpit UI pass (HSSC implementation) + mobile QA — the
   hero and the polish the screenshots exist to capture.

**Must do before v0.3.0:** Fable UI review, showcase pack, release review/tag.

**Can wait (post-v0.3.0):** provider abstraction spec; a second live keyless
provider (non-space, e.g. Wikimedia — breaks the NASA monoculture); the 3D
graph page concepts; GitHub Pages/deploy decisions; any live-model-comparison
exploration (needs its own safety spec).

## 3. Task Queue (run in this exact order)

### T1 — `MELLYCORE-PR3-CLOSEOUT-DOCS-001` — PR #3 merge closeout

- Goal: record the PR #3 merge (`fff50d2`) and `v0.2.0`-released reality in
  shared state; fix `PROJECT_STATE.md`'s stale branch/HEAD/"not pushed" claims
  and stale Next-tasks list; note PR #4 as open/draft.
- Model: Sonnet 5 · Effort: Low · Type: docs
- Files: `shared_context/PROJECT_STATE.md`, `ROADMAP.md`, `RUN_QUEUE.md`,
  `AGENT_HANDOFF.md`, `docs/tasks/MELLYCORE-PR3-CLOSEOUT-DOCS-001.md` (new)
- Validation: 3 validators + `unittest discover` + `git diff --check`
- One session: yes · Risk: low · Depends on: — 
- Artifact: clean, non-contradictory shared state on a branch off `main`.

### T2 — `MELLYCORE-HOLOGRAPHIC-UI-SPEC-REVIEW-001` — PR #4 spec review

- Goal: independent review of the HSSC spec: honesty-label completeness per
  screen, a11y/reduced-motion/no-JS soundness, CSS-only feasibility,
  purple-not-blue rule, no-NASA-dominance rule; small spec hardening only.
- Model: Fable 5 · Effort: Medium · Type: review
- Files: `docs/tasks/MELLYCORE-HOLOGRAPHIC-UI-SPEC-REVIEW-001.md` (new);
  possibly small edits to the spec on the PR #4 branch
- Validation: 3 validators (+ unittest/diff-check if docs edited)
- One session: yes · Risk: low · Depends on: — (parallel-safe with T1)
- Artifact: review report + approve/revise verdict for PR #4.

### T3 — `MELLYCORE-PR4-MERGE-001` — merge PR #4 (only if approved)

- Goal: with T2 approval and explicit operator approval, mark PR #4 ready and
  merge to `main` via normal merge commit; verify main afterward.
- Model: Sonnet 5 · Effort: Low · Type: release/ops (operator-gated)
- Files: none (merge only)
- Validation: fresh `main` checkout → 3 validators + `unittest discover`
- One session: yes · Risk: low (docs-only diff) · Depends on: T2 + operator OK
- Artifact: HSSC spec on `main`; PR #4 closed-merged.

### T4 — `MELLYCORE-POSITIONING-REFRESH-001` — README repositioning

- Goal: rewrite the README top per spec §6.2: cockpit one-liner, honesty-badge
  row, above-the-fold "real vs. simulated" table, 60-second local preview, a
  literal "what to look at" walkthrough (open dashboard → Source Arena →
  Model Arena → Context), all four validator commands; keep the graph story as
  a later section, not the lede.
- Model: Sonnet 5 · Effort: Medium · Type: docs
- Files: `README.md`, task report, handoff/run-queue sync
- Validation: 3 validators + unittest + `git diff --check`
- One session: yes · Risk: low · Depends on: T1 (true state), ideally T3
- Artifact: portfolio-ready README (screenshot links added later by T9).

### T5 — `MELLYCORE-PROVIDER-HONESTY-POLISH-001` — label sweep + fix

- Goal: sweep every visible provider/model/count label against spec §2.6/§3;
  fold in the still-open GitHub-card read-only review; fix copy only (no
  layout): `Demo provider`, `Planned`, `Simulated model output`, `Demo counts`,
  `Real source` complete and consistent on every tab at mobile and desktop.
- Model: Sonnet 5 · Effort: Low–Medium · Type: review + UI copy
- Files: `site/dashboard.html` (copy/badges only), possibly minor
  `dashboard.css` badge styles, task report, shared-state sync
- Validation: 3 validators + unittest + diff-check + browser QA (all tabs,
  390×844 + 1280×800, zero console errors)
- One session: yes · Risk: low–medium (touches site) · Depends on: T3
- Artifact: screenshot-correct labels everywhere.

### T6 — `MELLYCORE-HOLOGRAPHIC-UI-SPEC-001` — Hyperagent Social Cockpit UI pass

- Goal: implement HSSC per spec §5: `--holo-*` tokens, three-layer scene,
  Overview hero (core + provider orbit ring + amber containment hull), hull
  wrappers on Model Arena/Context, layered cards, depth/glow, `holo-pose`
  frozen state, reduced-motion / mobile-flatten / forced-colors / no-JS
  fallbacks. CSS-first, additive HTML only, ~zero JS, no dependencies.
- Model: Sonnet 5 · Effort: High · Type: UI
- Files: `site/css/dashboard.css` (or new `site/css/holo.css`),
  `site/dashboard.html`, task report, shared-state sync,
  `shared_context/DESIGN_SYSTEM.md` (HSSC summary)
- Validation: full spec §5.7 QA checklist + 3 validators + unittest +
  diff-check + network-diff zero (no new origins)
- One session: yes (large but bounded) · Risk: medium · Depends on: T3, T5
- Artifact: the showable holographic cockpit.

### T7 — `MELLYCORE-COCKPIT-MOBILE-QA-001` — mobile 390×844 QA

- Goal: dedicated mobile pass: no horizontal overflow, stage ≥75% viewport,
  flattened-scene check, badge visibility without hover, 44px tap targets,
  reduced-motion emulation, JS-off fallback render; fix only what QA finds.
- Model: Sonnet 5 · Effort: Low–Medium · Type: review/QA
- Files: QA report (new); site files only for QA-found fixes
- Validation: 3 validators + unittest + diff-check (if fixes) + re-QA
- One session: yes · Risk: low · Depends on: T6
- Artifact: mobile QA report with pass evidence.

### T8 — `MELLYCORE-HOLOGRAPHIC-UI-REVIEW-001` — independent UI review

- Goal: Fable review of T6/T7: spec conformance, label survival after restyle,
  purple-not-blue and no-NASA-dominance verdicts, a11y/fallback verification,
  performance guardrails; small hardening only.
- Model: Fable 5 · Effort: Medium · Type: review
- Files: review report (new); minor hardening edits at most
- Validation: 3 validators + unittest + diff-check
- One session: yes · Risk: low · Depends on: T7
- Artifact: review report; go/no-go for release prep.

### T9 — `MELLYCORE-SHOWCASE-PACK-002` — screenshot/showcase pack

- Goal: capture spec §6.3 set (Overview hero in `holo-pose` 1920×1080; Source
  Arena mobile 390×844; Model Arena desktop with `Simulated` badges legible;
  Context tab; ≤8s vertical-scroll GIF); evidence stored outside the repo per
  policy; wire links/references into README and showcase doc.
- Model: Sonnet 5 · Effort: Low · Type: docs
- Files: `docs/showcase/` pack doc (new), `README.md` (image/evidence links),
  shared-state sync
- Validation: 3 validators + unittest + diff-check
- One session: yes · Risk: low · Depends on: T8
- Artifact: the visual proof pack the README points at.

### T10 — `MELLYCORE-V0.3.0-RELEASE-REVIEW-001` — v0.3.0 release

- Goal: fresh-clone validation at the release candidate on `main`; tag and
  publish **`v0.3.0` — Holographic Social Cockpit**; release notes led by the
  real-vs-simulated table; record release in shared state.
- Model: Fable 5 · Effort: Medium · Type: release (operator-gated)
- Files: release notes, shared-state sync, task report
- Validation: fresh clone → `context_gate audit --json` 0 findings,
  `loop_ops validate` PASS, `validate_project_state` PASS, full unittest pass
- One session: yes · Risk: low–medium (public artifact) · Depends on: T9 +
  operator approval
- Artifact: published `v0.3.0` release.

## 4. Recommended RUN_QUEUE update (draft — not applied by this task)

This task deliberately does **not** edit `shared_context/RUN_QUEUE.md`: its
commit stays local and unpushed on the PR #4 branch, and registering queue
state that main can't see would recreate the stale-claim contradictions this
repo polices. T1 applies the following text (renumber as needed):

> 61. `MELLYCORE-VISIBLE-APP-RUN-PLAN-001` — complete (docs-only). Produced the
> visible-app run plan at `docs/tasks/MELLYCORE-VISIBLE-APP-RUN-PLAN-001.md`:
> current-state snapshot (v0.2.0 + PR #3 on main; HSSC spec only in draft
> PR #4; PROJECT_STATE stale on branch/HEAD/push claims), fastest visible path,
> and a 10-task ordered queue T1–T10 (PR #3 closeout docs → PR #4 spec review →
> PR #4 merge if approved → README positioning refresh → provider honesty
> polish → Hyperagent Social Cockpit UI pass → mobile 390×844 QA → Fable UI
> review → showcase pack → `v0.3.0 — Holographic Social Cockpit` release), with
> model routing (Fable 5 = reviews/release gates; Sonnet 5 = docs sync, UI
> implementation, QA, showcase), a UI target summary, and release
> must-ship/must-not-ship boundaries. No UI implemented; no site code changed;
> no push, merge, or release performed; old origin untouched. Recommended
> next: `MELLYCORE-PR3-CLOSEOUT-DOCS-001`.

## 5. Recommended AGENT_HANDOFF update (draft — not applied by this task)

T1 applies this as the new latest entry:

> Latest completed task: `MELLYCORE-VISIBLE-APP-RUN-PLAN-001`
>
> - Outcome: docs-only run plan (`docs/tasks/MELLYCORE-VISIBLE-APP-RUN-PLAN-001.md`)
>   defining the fastest path to a visible, polished, portfolio-ready cockpit:
>   task queue T1–T10 ending in `v0.3.0 — Holographic Social Cockpit`.
> - Current state: `main` = `fff50d2` (PR #3 merged; v0.2.0 released). Draft
>   PR #4 (open, docs-only) carries `MELLYCORE_HOLOGRAPHIC_UI_SPEC_001` and is
>   NOT merged. No UI work has started on the HSSC spec.
> - Warnings: `PROJECT_STATE.md` contains stale pre-release claims (branch
>   `publish/mellycore-main-001`, HEAD `6e804e3d`, "not pushed" cockpit) —
>   fixed by T1; do not trust those lines until T1 lands. README still leads
>   with the graph story until T4.
> - Old origin: untouched; only the canonical remote was fetched.
> - Next task: `MELLYCORE-PR3-CLOSEOUT-DOCS-001`, then
>   `MELLYCORE-HOLOGRAPHIC-UI-SPEC-REVIEW-001` →
>   `MELLYCORE-PR4-MERGE-001` (operator-gated) →
>   `MELLYCORE-POSITIONING-REFRESH-001`.
> - Intended v0.3.0 path: T1→T10 above; v0.3.0 is presentational + docs only —
>   no new capability surface, no backend, no keys, no autonomy.

## 6. Model routing

- **Fable 5 for:** the two independent reviews (T2 spec review, T8 UI review),
  the v0.3.0 release review/tag decision (T10), and any safety-posture or
  positioning-claim judgment call. High-leverage, low-volume gates.
- **Sonnet 5 for:** everything that executes against an approved spec — docs
  sync (T1), merge mechanics (T3), README rewrite (T4), label polish (T5), the
  HSSC UI implementation (T6), mobile QA (T7), showcase pack (T9).
- **Do not spend Fable 5 on:** mechanical shared-state bookkeeping, run-queue
  renumbering, screenshot capture, badge copy edits, or QA click-throughs —
  Sonnet handles all of it inside guardrails the specs already define.

## 7. Visual/UI target (implementation language)

Black TikTok-style mobile-first vertical feed: full-bleed media stage ≥75% of
the mobile viewport, one source per screen. Top: `Find related sources` search
pill + provider chip rail. Right edge: floating glass action rail
(like/inspect/save/share) with `Demo counts` label attached. Bottom: caption
block — provider handle, source title, provenance badge row, hashtags. Desktop:
the phone-proportioned stage centered like an instrument between tilted glass
side rails, faint orbit arc + violet nebula behind it. Model Arena: pinned
`Real source` card above four equal sibling cards with bold model names —
**Fable 5 / Opus / GPT / GLM** — each with `Simulated model output` in the card
header. Overview: MellyCore core at center, provider orbit ring around it
(NASA = the one green `Live demo` chip; GitHub = violet `Planned / demo` chip;
nine dimmed planned chips), amber safety containment hull around the whole
composition captioned `Zero-autonomy containment · static · keyless ·
read-only`. Purple/black holographic depth throughout (violet/magenta/lavender;
cyan tertiary only; no gamer RGB, no hue animation). NASA imagery appears only
inside the media stage — never in the chrome, never in the center. All labels
honest and visible in every screenshot.

## 8. Release target — `v0.3.0 — Holographic Social Cockpit`

**Must ship:** merged HSSC spec; HSSC UI implemented and Fable-reviewed;
refreshed README positioning with real-vs-simulated table and walkthrough;
honesty-polished labels; mobile 390×844 QA pass; showcase screenshot/GIF pack
(evidence outside repo); all validators + 245+ tests green from a fresh clone;
release notes stating what is real, simulated, and planned.

**Must not ship:** any backend, database, API key, secret, dependency, build
step, scheduler, workflow YAML, autonomous behavior, new live provider, live
model call, deploy/hosting claim, or MellyTrade linkage. No capability surface
changes at all — v0.3.0 is presentational + docs by definition.

**Release name:** `v0.3.0 — Holographic Social Cockpit`.

## 9. Final recommendation

- **Run immediately:** `MELLYCORE-PR3-CLOSEOUT-DOCS-001` (T1). It is the
  cheapest task in the queue and unblocks honest writing everywhere else —
  PROJECT_STATE currently contradicts shipped reality.
- **Next three:** T2 spec review (Fable) → T3 PR #4 merge (operator-gated) →
  T4 README positioning refresh.
- **Push/merge anything now?** No. This task pushes nothing and merges
  nothing. PR #4 merges only after T2 approval plus explicit operator
  approval. All T1+ work lands via normal reviewed branches/PRs.
- **Avoid:** starting the HSSC UI pass before the spec review and honesty
  polish land (you would restyle copy that is about to change and implement an
  unreviewed spec); Three.js/Canvas/dependency temptation; adding a second
  provider or any new capability before v0.3.0; letting NASA imagery into the
  hero or chrome; screenshots cropped so `Simulated`/`Demo` labels fall out of
  frame.

---

## Validation results (this task)

- `context_gate audit --json`: 0 findings
- `loop_ops validate`: PASS (9 loops)
- `validate_project_state`: PASS
- `unittest discover` and `git diff --check`: run at commit time (docs edited)

Safety confirmation: no push, no merge, no release, no site/dashboard code
change, no `ContextSource`/refusal-log/loop-evidence mutation, no dependency,
no backend/keys/database/scheduler/autonomy. Old origin untouched (not even
configured in this clone); only the canonical remote was fetched.
