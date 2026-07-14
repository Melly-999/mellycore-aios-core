# Claude Prompt Notes

Use Claude for architecture, reasoning, docs, and review. Start by reading `CLAUDE.md` and the required `shared_context/` files.

## Loop Operations

When operating a MellyCore loop, use the canonical skills in `[[../loops/README]]`. They are tool-neutral and are not duplicated here — this wrapper points at them so the two cannot drift apart.

Read `[[../loops/mellycore-loop-constraints]]` first; every loop skill inherits it. Phase 1 is report-only: no loop writes, pushes, merges, deploys, comments, installs, or calls a provider.

Claude's review role maps naturally to `[[../loops/mellycore-loop-verifier]]`. Two rules there are absolute: the verifier never implements the fix it verifies, and the verdict defaults to REJECT until evidence observed first-hand supports every claim.

