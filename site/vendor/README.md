# Three.js vendor provenance

- Upstream: `https://github.com/mrdoob/three.js`
- Release: `r164`
- Annotated tag object: `2747e290508e1d8ff71d4f6fd61d17f287a1f35d`
- Peeled immutable commit: `a2e9ee8204b67f9dca79f48cf620a34a05aa8126`
- Module source: `build/three.module.js`
- Local entrypoint: `three-r164.module.js`
- Local change: one indentation-only normalization at upstream line 46459 so
  the repository's staged whitespace gate passes; runtime code is unchanged.
- Module SHA-256:
  `07940AB8E640E3F29E4FE9A934ADB574315387CC5BB6CAD8226845CC6F6AE11F`
- Module size: `1,274,690` bytes
- License: MIT; preserved in `LICENSE.three-r164.txt`

The module is loaded dynamically and locally only after the semantic Source
Arena shell is usable, reduced motion is not requested, the viewport is above
the mobile breakpoint, low-power/data-saving signals are absent, and an actual
WebGL context can be created. It has no runtime CDN dependency and includes no
examples, controls, loaders, textures, or other external assets.

Update process:

1. Choose a tagged upstream release whose `build/three.module.js` is a
   self-contained ESM file.
2. Resolve the annotated tag and peeled commit with `git ls-remote`.
3. Download the module and license from the peeled immutable commit.
4. Re-run SHA-256, size, license, suspicious-code, offline-load, browser-network,
   fallback, and lifecycle checks.
5. Update this record and the import path in one reviewed task.

Rollback is CSS-only: remove the module load, force capability detection to
fall back, or use the local diagnostic query `?scene=css`. The semantic shell
and CSS/DOM source map remain complete.
