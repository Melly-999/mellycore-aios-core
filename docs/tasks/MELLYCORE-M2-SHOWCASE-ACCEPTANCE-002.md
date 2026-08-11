# MELLYCORE-M2-SHOWCASE-ACCEPTANCE-002

## OBSERVED

- Candidate:
  `24312daa8f9c204faa42f9d5ca357834c1b10e81`
  (`fix: correct M2 mobile navigation containment`).
- Parent:
  `8be96f691691e4e527a666d019a994b00d526173`
  (`docs: record M2 showcase rejection`).
- Review branch/worktree: `review/mellycore-m2-showcase-acceptance-002` at
  `C:\AI\MellyCore_Workspace\02_Worktrees\mellycore-m2-showcase-acceptance-002`.
- The candidate, parent, subject, one-parent relationship, and clean isolated
  review state were verified before browser testing.
- The candidate delta contains one implementation declaration in
  `site/css/sections.css`, the remediation task record, and the required prior
  handoff update. No other implementation file differs from the rejection
  parent.
- Chromium `151.0.7922.76` rendered fresh evidence through a controlled local
  HTTP server. No screenshot or measurement from the remediation run was used
  as acceptance evidence.

## VERIFIED

### M2-ACCEPT-01 at 375 px

- Viewport, document client width, and document scroll width were all 375 px.
- The nav measured 327 px client width and 437 px scroll width, with a 110 px
  maximum scroll position.
- From an untouched page load, keyboard order was Skip to content, Command
  Center, Product evidence, Safety, Static dashboard.
- On the fifth Tab, the rail advanced from `scrollLeft = 0` to 110. The final
  link moved from x=325.59..428.80 to x=215.59..318.80 inside the x=24..351
  rail.
- The focused link used a 2 px solid cyan outline with a 2 px offset. The link
  and complete focus indicator were visible inside both rail and viewport.
- No body or document horizontal overflow existed.

`M2-ACCEPT-01` is **RESOLVED**.

### Required responsive and visual contract

- Fresh full-page evidence was rendered and inspected at 1440 x 900,
  1024 x 900, 768 x 1024, and 375 x 812. The prior 200% acceptance method was
  repeated at 720 CSS pixels.
- At every required width, document client width equaled document scroll
  width. All major sections stayed within the viewport, CTAs remained visible,
  and no materially broken stacking or non-decorative clipping was found.
- Hero, Source Arena, Command Center, Runtime Constellation, exact ten-workspace
  ecosystem, Shared Context, Knowledge & Operations Graph, roadmap, safety,
  tooling, and Operator Channel remained coherent and readable.
- The accepted H1 remains `One command center. Every AI plane under operator
  control.` Exactly two top-level product layers remain represented. Exactly
  ten canonical workspaces render in waves 4 / 3 / 3.
- Point-of-use labels retain static, representative, planned, derived,
  no-live-ingestion, no-provider-call, no-workspace-backend, and
  no-autonomous-action boundaries. No false live or authorized capability was
  introduced.
- Reduced-motion emulation matched the media query, produced no animation
  names, reduced transitions to 0.00001 seconds, used automatic root scrolling,
  and left zero critical headings/paragraphs hidden.

### Technical contract

- Fresh page loads requested only `site/index.html` and four local CSS files;
  all page-owned requests succeeded and no external request occurred.
- The known `/favicon.ico` console 404 remains inherited and non-blocking.
- Script, button, form, and input counts were zero. Duplicate ID count was
  zero. All six fragment links resolved, and all five unique authored local
  targets returned HTTP 200.
- The skip link became visibly focused and navigated to `#main-content`, while
  focus returned to `body`; this matches the previously disclosed non-blocking
  limitation and did not worsen.

## ACCEPTANCE FINDINGS

### Resolved

**M2-ACCEPT-01 — 375 px final navigation link and focus containment.**

The exact rejected viewport now passes ordinary keyboard traversal, link
visibility, full focus-indicator visibility, and document-overflow checks.

### Blocking

**M2-ACCEPT-02 — 390/430 px focused final navigation target remains clipped.**

At 390 px, the rail occupies x=24..366 and has a 95 px end-scroll range.
Ordinary fifth-Tab focus leaves `scrollLeft = 0`, with the final link at
x=325.59..428.80; the label and complete focus indicator are not visible.
At 430 px, the rail occupies x=24..406 and has a 55 px end-scroll range, but
focus again leaves `scrollLeft = 0` and the same final-link geometry clipped.
Manual end scrolling fully contains focus at both widths.

The candidate's only implementation change is
`scroll-padding-inline-end: 32px`. Disabling that declaration reproduces the
same 390/430 behavior, so the finding is not a regression introduced by the
remediation. It is nevertheless acceptance-blocking because the existing
canonical homepage specification requires deliberate mobile horizontal rails
to be keyboard accessible and requires viable visible-focus paths. The
sanity-width review did not invent a requirement for every item to be initially
visible; the failure occurs after ordinary keyboard focus lands on the target.

## LIMITATIONS

The following previously disclosed items remain non-blocking and unchanged:

1. The ninth Shared Context card remains an intentional lone row at 768 px.
2. `.card-grid--4` remains unused.
3. `/favicon.ico` returns 404.
4. Skip-link navigation does not transfer DOM focus to `main`.
5. The 375 px page remains long and label-dense.
6. `MVP demo — Planned` remains ambiguously related to canonical M0–M5 terms
   without implying live or connected state.

## FINAL DECISION

`REJECTED`

The First Commercial Design Showcase is not accepted. M2 remains incomplete.
The successful 375 px remediation and otherwise passing Showcase do not
override the independently reproduced mobile visible-focus failure at 390 and
430 px.

## CANONICAL STATE EFFECT

- `shared_context/AGENT_HANDOFF.md`: updated because repository rules require a
  handoff after meaningful work and the rejected gate must remain durable.
- `docs/tasks/MELLYCORE-M2-SHOWCASE-ACCEPTANCE-002.md`: created as this
  independent acceptance record.
- `shared_context/PROJECT_STATE.md`, `shared_context/ROADMAP.md`,
  `shared_context/TASK_INDEX.md`, and `shared_context/RUN_QUEUE.md`: unchanged.
  No completion or accepted milestone exists to promote, and the independent
  repository-wide Global Pointer remains untouched.
- `site/**`: unchanged by this acceptance task.
- No push, merge, deployment, public release, provider/runtime activation,
  workspace backend activation, dependency, credential, or external operation
  occurred.

## NEXT STEP

Recommend only:

`MELLYCORE-M2-MOBILE-NAV-REMEDIATION-002`

Bound it to a range-safe focus-containment correction for the existing mobile
horizontal rail, including ordinary keyboard-focus checks at 360, 375, 390,
and 430 px. Then perform a fresh independent Showcase Acceptance rerun. This
record authorizes and executes neither task.
