# MELLYCORE-HOLOGRAPHIC-UI-SPEC-REMEDIATION-001

Status: complete (docs-only). No UI implemented, no site/dashboard code touched,
no `ContextSource`/refusal-log/loop-evidence change, no release-facts change in
`PROJECT_STATE.md`, no push to `main`, no merge, PR #4 remains draft.
Model: Sonnet 5. Effort: Medium.

Purpose: remediate `docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md` so its
primary product composition matches the operator's authoritative TikTok/
Hyperagent social-cockpit target, resolving findings F1–F5 from
`MELLYCORE-HOLOGRAPHIC-UI-SPEC-REVIEW-001` (verdict: **NEEDS SPEC FIXES BEFORE
MERGE**).

## Preflight (confirmed before any edit)

- Repository identity: the only configured remote (`origin`) resolves via the
  session's local proxy to `Melly-999/mellycore-aios-core` — canonical, not the
  retired `Melly-999/mellycore-aios`.
- Branch `claude/mellycore-holographic-ui-spec-sqgfs3`, HEAD
  `8fa60840a641bae7307c31f0a75dd472b474c837`, matching the expected value.
- Working tree clean before edits.
- PR #4 confirmed via GitHub API: `state=open`, `draft=true`, `merged=false`,
  head SHA `8fa6084`, base `main` at `fff50d2`.
- Canonical `main` confirmed at `fff50d2a49f7ee9824d1ad1dc29da81e8085ca2e`.
- Linear ancestry confirmed: `fff50d2 → 31abbea → 33d24d7 → 8fa6084`.

No material difference from expected state was found; the run proceeded.

## How findings F1–F5 were resolved

**F1 (HIGH — wrong hero) → resolved.** Section 2.5 retitled "Secondary identity
composition: core, orbit, hull (Overview only)" and rewritten with five hard
rules: static/ultra-slow motion, background-level only, never inside the
Source Arena viewport, never the lead screenshot, never visually stronger than
the central social slide. Section 3.4 (Overview) rewritten so the three status
panels — not the core+orbit+hull composition — are the visually dominant
element; the composition is explicitly demoted to "a compact identity mark, not
the dominant element of this screen or of the product." Section 6.3's
screenshot order (E8) makes the Source Arena mobile model-lens slide screenshot
#1 and Overview screenshot #4.

**F2 (HIGH — comparison not in the central slide) → resolved.** New Section
3.1a "Model-lens slide (required feed slide type)" specifies a first-class feed
slide containing a pinned real-source header (`Real source` badge) plus four
stacked model panels (Fable 5, Opus, GPT, GLM), each with a `Simulated model
output` badge in its header. Section 3.1's layout is restructured to name this
as one of two interchangeable central-slide types, with the demo prompt/task
rail immediately above it. Section 3.2 (desktop) gives the same content a 2×2
arrangement in the right rail. Section 3.3 (Model Arena) is retitled as the
*expanded* version of this same slide type, not a disconnected experience.

**F3 (MEDIUM — pagination dots and prompt list unspecified) → resolved.**
Section 3.1 item 4 requires the existing `nasa-stage-dots` element under every
slide type; item 2 requires the prompt/demo-task chip rail. Section 3.1a
specifies the rail's exact honesty label (`Demo prompts / simulated comparison
tasks`) and five example prompts (asteroid visualization, 100-acre fitness
retreat site plan, Apollo control panel reconstruction from PDFs, World Cup
jersey supply-chain simulation, solar-flare/aurora effects), each with an
explicit "does not imply the described capability is implemented" disclaimer.
Section 3.2 requires the same rail on desktop.

**F4 (LOW — approximate mobile breakpoint) → resolved.** Section 4.9's mobile
flatten rule now reads `max-width: 768px` exactly, replacing "≤ ~700px."

**F5 (LOW — HTML insertion points not anchored) → resolved.** Section 5.1 now
names the exact anchor (`#tab-nasa` / `.dash-panel--nasa`) and requires reuse
of the existing NASA stage, provider rail, and `nasa-stage-dots` rather than
duplication; explicitly states the Context tab is out of scope. Section 5.3
repeats the reuse requirement for HTML structure changes specifically.

## Additional remediation beyond F1–F5 (per this task's explicit E1–E10 scope)

- **E5/E6 (mobile-first priority, desktop adaptation):** Section 5.6 rewritten
  to declare 390×844 "the primary reference viewport for this entire spec,"
  with explicit acceptance criteria (slide ~70–75% of first viewport, no
  orbit, no monumental hull, zero horizontal overflow, story visible without
  scroll, 44×44px controls, labels never occlude content). Section 3.2 caps
  desktop decorative tilt at ~4° and states desktop "must remain recognizably
  the same product as mobile."
- **E7 (containment hull re-scope):** Sections 2.4 and 4.4 rewritten so the
  hull is explicitly "a labeling device, not architecture," sized to wrap only
  specific simulated content (model-lens panels, Model Arena panel set, model
  rail, Overview's compact identity mark) — never the whole screen or app
  shell.
- **E9/E10 (implementation anchors and constraints):** Section 5.1/5.3 add the
  exact reuse/anchor guidance above. Section 5.9 expanded to explicitly restate
  every constraint category from this task's E10 list (no Three.js, no Canvas,
  no dependency, no build step, no backend/database/key/scheduler, no live
  GitHub ingestion, no autonomy, no `ContextSource` body/note/rationale/
  refusal-log/private-path access) in one place, so Sonnet's future
  implementation task report has a single restatement target.

## Self-verification (performed before commit, per this task's checklist)

- Source Arena is now the lead hero — confirmed (§3.1: "primary hero
  composition and required first screenshot").
- Model comparison exists inside the central slide — confirmed (§3.1a).
- Prompt/task list is visible — confirmed (§3.1 item 2, §3.1a rail spec).
- Pagination dots are required — confirmed (§3.1 item 4, reusing
  `nasa-stage-dots`).
- Orbit is secondary and Overview-only — confirmed (§2.5 title and hard rules,
  §3.1/§3.2 "does not render," §3.4 demoted dominance).
- Containment hull is a compact honesty frame — confirmed (§2.4, §4.4 "sized to
  its content, not its screen").
- 390×844 is the primary reference viewport — confirmed (§5.6 opening
  statement).
- No implementation capability is falsely claimed — confirmed (§3.1a's explicit
  disclaimer that prompt selection does not imply live capability).

## Files changed

- `docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md` — sections 2.4, 2.5, 3.1
  (+ new 3.1a), 3.2, 3.3, 3.4, 4.4, 4.9, 5.1, 5.3, 5.6, 5.9, 6.3 amended per
  E1–E10 above. Sections 1 (positioning), 2.1–2.3, 2.6–2.7, 3.5–3.6, 4.1–4.3,
  4.5–4.8, 4.10–4.11, 5.2, 5.4–5.5, 5.7–5.8, 6.1–6.2, 6.4–6.5, 7, 8 are
  unchanged — they were not implicated by the review findings.
- `shared_context/AGENT_HANDOFF.md`
- `shared_context/RUN_QUEUE.md`
- `docs/tasks/MELLYCORE-HOLOGRAPHIC-UI-SPEC-REMEDIATION-001.md` (this file, new)

`site/dashboard.html`, `site/css/*`, `site/js/*`, `ContextSource` records,
refusal logs, loop evidence, and `PROJECT_STATE.md`'s release facts were **not**
touched, per this task's explicit exclusions.

## Validation

- `python3 -m scripts.context_gate audit --json` → 0 findings
- `python3 -m scripts.loop_ops validate` → PASS
- `python3 -m scripts.validate_project_state` → PASS
- `python3 -m unittest discover` → 245/245 passing
- `git diff --check` → clean

## Safety confirmation

Docs-only. No site/dashboard code, `ContextSource` record, refusal log, loop
evidence, or `PROJECT_STATE.md` release fact was modified. No backend,
database, API key, secret, dependency, scheduler, or workflow YAML change. The
UI remains unimplemented — this task edits the specification only. PR #4 was
not merged, marked ready, or force-pushed. No release was created. Canonical
`main` remains unchanged at `fff50d2`. The retired repository
`Melly-999/mellycore-aios` was never contacted.

## Next recommended task

`MELLYCORE-PR4-MERGE-001` — merge draft PR #4 into `main` now that the spec
review's blocking findings (F1–F5) are remediated.
