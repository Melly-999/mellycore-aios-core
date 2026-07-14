# Codex Prompt Notes

Use Codex for implementation, validation, local git hygiene, and PR preparation when explicitly approved. Start by reading `AGENTS.md` and the required `shared_context/` files.

## Loop Operations

When operating a MellyCore loop, use the canonical skills in `[[../loops/README]]`. They are tool-neutral and are not duplicated here — this wrapper points at them so the two cannot drift apart.

Read `[[../loops/mellycore-loop-constraints]]` first; every loop skill inherits it. Phase 1 is report-only: no loop writes, pushes, merges, deploys, comments, installs, or calls a provider.

The deterministic circuit breaker (`py -3.9 -m scripts.loop_ops guard`) is binding. Codex must not retry past it, edit a ledger to change its verdict, or start a fresh run to reset counters.

