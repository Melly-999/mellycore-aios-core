# MELLYCORE-M2-MOBILE-NAV-REMEDIATION-001

## RESULT

**PASS**

The acceptance-blocking 375 px header navigation and visible-focus defect
`M2-ACCEPT-01` is resolved by one focus-aware CSS declaration. This task does
not accept the Showcase or mark M2 complete; it makes the bounded remediation
eligible for a fresh independent acceptance rerun.

## OBSERVED

- Source baseline:
  `8be96f691691e4e527a666d019a994b00d526173`
  (`docs: record M2 showcase rejection`).
- Source branch/worktree:
  `docs/mellycore-m2-showcase-acceptance-001` at
  `C:\AI\MellyCore_Workspace\02_Worktrees\mellycore-m2-showcase-acceptance-001`.
- Task branch/worktree: `fix/mellycore-m2-mobile-nav-remediation-001` at
  `C:\AI\MellyCore_Workspace\02_Worktrees\mellycore-m2-mobile-nav-remediation-001`.
- Both worktrees were clean at preflight. The task worktree was created
  directly from the pinned baseline; the source worktree was not modified.
- At the unmodified 375 px baseline, the rail measured 327 px client width and
  437 px scroll width, with a valid 110 px maximum scroll position. The final
  `Static dashboard` link occupied x=325.59..428.80 while the rail occupied
  x=24..351. Keyboard focus reached the link but left `scrollLeft = 0`, so the
  label and its 2 px cyan outline with 2 px offset were clipped.
- Document client and scroll widths were both 375 px. The defect was local
  header/navigation containment, not body horizontal overflow.

## ROOT CAUSE

The existing mobile rail already provided 32 px of physical trailing padding
and enough range to reveal the final link fully. Manual end scrolling proved
the end state was valid. The rail did not declare focus-aware end scroll
padding, so Chromium did not advance the horizontal scroller when keyboard
focus landed on the partially visible final link.

## IMPLEMENTED

- `site/css/sections.css`: added
  `scroll-padding-inline-end: 32px` beside the existing 32 px rail end padding
  in the mobile `.command-bar nav` rule.
- Navigation markup, semantics, copy, styling tokens, JavaScript posture, and
  all accepted page surfaces remain unchanged.
- `shared_context/AGENT_HANDOFF.md`: recorded this meaningful remediation and
  the exact independent next gate.

## VERIFIED

- At 375 px, logical Tab order is: Skip to content, Command Center, Product
  evidence, Safety, Static dashboard.
- On the fifth Tab, `Static dashboard` is active, the rail advances to its
  110 px end position, and the link occupies x=215.59..318.80 within the
  x=24..351 rail. Its complete 2 px outline plus 2 px offset is visible.
- At 375 px, document client width and scroll width both remain 375 px.
- 1440, 1024, and 768 px retain their existing layout because the changed rule
  applies only below the existing 768 px breakpoint. Required 375 px rendering
  passes. The 720-CSS-pixel approximate 200% reflow remains usable with zero
  document overflow and visible final-link focus.
- Additional 320 and 360 px sanity checks keep the final link and outline fully
  visible on keyboard focus without document overflow. At the optional 390 and
  430 px sanity widths, the inherited rail still leaves part of the final link
  and its focus treatment outside the initial visible region. This was present
  at the pinned baseline, was not introduced by the fix, and was not broadened
  into the exact 375 px acceptance-blocker remediation.
- Reduced-motion emulation produces no active animations, limits transitions
  to 0.00001 seconds, and retains automatic root scrolling.
- Zero duplicate IDs; all six fragment links resolve; `dashboard.html` and
  page-owned CSS return HTTP 200; no JavaScript, external requests, buttons,
  forms, dependencies, or new console errors were introduced. The previously
  disclosed favicon 404 remains unchanged and out of scope.
- Exactly ten canonical AI Workspaces remain present in waves 4 / 3 / 3. The
  accepted H1 and product truth are unchanged.

## NOT CHANGED

- `shared_context/PROJECT_STATE.md`, `shared_context/ROADMAP.md`,
  `shared_context/TASK_INDEX.md`, and `shared_context/RUN_QUEUE.md`.
- Product Vision, milestone definitions, runtime/provider/agent/MCP/integration
  implementations, dependencies, assets, fonts, credentials, deployment, and
  release state.
- The tablet Shared Context orphan, unused `.card-grid--4`, favicon 404,
  skip-link focus transfer, mobile page depth, and roadmap terminology.

## REMAINING

- M2 remains not complete.
- Showcase Acceptance remains rejected until a fresh independent review passes.
- No push, merge, deployment, provider/runtime activation, workspace backend
  activation, or public release occurred.
- Recommend only `MELLYCORE-M2-SHOWCASE-ACCEPTANCE-002`; do not execute it as
  part of this remediation.
