# 3D

This repository currently plans two distinct, unrelated 3D concepts. Neither
has an accepted, canonical implementation on `main` as of this note.

1. **Source Arena Hybrid renderer** — an accepted WebGL-enhanced, CSS-complete-fallback
   renderer decision for the Source Arena model-lens hero (the primary product
   surface defined in `docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md`). The
   decision is recorded in `docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md`
   (status: **ACCEPTED**, 2026-07-20, decision/specification level only). It
   covers orbital/model-lens nodes, a procedural deep-space background, and a
   central model-lens core, always paired with a complete CSS/DOM fallback.
   Canonical `main` has no accepted implementation. Paused, open, unmerged
   PR #28 (`feat: add MellyCore 3D scene foundation`) implements this
   foundation (`site/js/mellycore-scene.js`, `THREE.WebGLRenderer`, vendored
   `site/vendor/three-r164.module.js`), but it remains non-canonical, unmerged,
   and blocked by physical Android Chromium Gate B (`OPEN / NOT EXECUTED`).
2. **Obsidian-style 3D Knowledge Graph page** — a separate, unrelated future
   concept for a spatial view of the Living Context Graph fixture
   (`docs/specs/MELLYCORE_OBSIDIAN_3D_PAGE_SPEC_001.md`,
   `docs/design/MELLYCORE_OBSIDIAN_3D_VISUAL_LANGUAGE_001.md`). Both of those
   documents explicitly disclaim any Three.js/WebGL implementation themselves;
   they describe direction notes only.

No orbital cube, constellation, star field, or provider-routing visual from
the Obsidian-style concept is implemented in this repository today. The
Source Arena Hybrid renderer foundation exists only on paused, unmerged
PR #28 (see above) and is not canonical or accepted.
