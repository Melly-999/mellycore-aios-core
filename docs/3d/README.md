# 3D

This repository currently plans two distinct, unrelated 3D concepts. Neither is
implemented as of this note.

1. **Source Arena Hybrid renderer** — a proposed WebGL-enhanced, CSS-complete-fallback
   renderer for the Source Arena model-lens hero (the primary product surface
   defined in `docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md`). The decision is
   drafted in `docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md` (status:
   PROPOSED, not accepted). It covers orbital/model-lens nodes, a procedural
   deep-space background, and a central model-lens core, always paired with a
   complete CSS/DOM fallback.
2. **Obsidian-style 3D Knowledge Graph page** — a separate, unrelated future
   concept for a spatial view of the Living Context Graph fixture
   (`docs/specs/MELLYCORE_OBSIDIAN_3D_PAGE_SPEC_001.md`,
   `docs/design/MELLYCORE_OBSIDIAN_3D_VISUAL_LANGUAGE_001.md`). Both of those
   documents explicitly disclaim any Three.js/WebGL implementation themselves;
   they describe direction notes only.

No orbital cube, constellation, star field, or provider-routing visual from
either concept is implemented in this repository today.
