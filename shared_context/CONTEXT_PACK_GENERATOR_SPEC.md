# Context Pack Generator Spec

**Task ID:** MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001
**Version:** 1.0
**Status:** Draft specification (docs-only)
**Scope:** Gitingest-inspired, safe, read-only repo digest for feeding future ingest passes and agent context

---

## 1. Purpose

This document specifies a **future, separately implemented** tool concept — a "context pack generator" — that would produce a bounded, read-only digest of this repository for use as LLM context or as raw material for `[[SOURCE_INGEST_WORKFLOW]]`. It is inspired by the Gitingest repo-digest pattern (`[[../docs/research/external_inspiration_llm_wiki_graph_001]]`, Section 2.3), adapted to MellyCore's safety posture.

**This document authorizes no implementation.** No script, CLI, or automation is created by this task. This is a specification for a future, separately approved coding task.

---

## 2. Read-Only Repo Digest

The context pack generator, when implemented, must:

- Operate strictly read-only against the local working tree. It must never write, move, delete, or modify any repository file.
- Never invoke `git push`, `git fetch`, `git pull`, or any remote operation. It reads local file state only.
- Never require or use network access. It is a local, offline tool.
- Produce a single output artifact (e.g., a Markdown or JSON digest file) that is itself treated as a normal repo file — reviewed and committed like any other docs artifact, never auto-published.

---

## 3. File Allowlist / Blocklist

### Allowlist (may be included in a digest)
- `docs/**/*.md`
- `shared_context/**/*.md`
- `agent_prompts/**/*.md`
- `README.md`, `PROJECT_RULES.md`, `AGENTS.md`, `CLAUDE.md`
- `site/**/*.html`, `site/**/*.css` (metadata/summary only — see Section 4 on token budget; full contents may be included since this is static, secret-free markup)

### Blocklist (must never be included, referenced by content, or listed by path)
- Any `.env`, `.env.*` file.
- Any file matching `*secret*`, `*credential*`, `*token*`, `*apikey*`, `*api_key*` (case-insensitive) in its filename.
- Any `db/*.db`, `*.sqlite`, `*.sqlite3` file.
- Any directory under `.git/` internals beyond standard metadata already exposed by `git status`/`git log` (no raw object inspection).
- Any file under a `node_modules/`, `vendor/`, or similar dependency directory (out of scope; this repo currently has none, but the rule stands for future-proofing).
- Any path outside the repository root (no `../` traversal).
- Any file the repository's own `.gitignore` excludes, treated as a signal the operator already wants it kept out of any generated artifact, not just out of git.

**Rule of composition:** blocklist always wins over allowlist. A blocklisted pattern excludes a file even if it would otherwise match an allowlist pattern.

---

## 4. Token Budget

- The generator must estimate and report a total token count for the digest (a simple character-count-based estimate is acceptable; no external tokenizer API call).
- A configurable maximum token budget (proposed default: 50,000 tokens) caps the digest; if the full allowlisted corpus exceeds the budget, the generator truncates by **omitting lowest-priority files first** (priority order: `shared_context/SAFETY_CONTRACT.md` and `shared_context/PROJECT_STATE.md` highest, then other `shared_context/*.md`, then `docs/specs` and `docs/design`, then `docs/tasks`, then everything else) rather than truncating file contents mid-file, which could create misleading partial claims.
- The digest output must state its own token estimate and whether truncation occurred, and if so, which files were omitted — an honest, self-describing artifact, not a silent truncation.

---

## 5. Changed-Files Summary

- The generator may include a summary of `git status --short` and `git diff --stat` output (file paths and change-type only, e.g., "modified," "added" — never full diff content of blocklisted files, and full diff content of allowlisted files only within the token budget).
- This summary exists to help a future ingest pass or reviewing agent quickly see what changed since the last snapshot, consistent with the Neon-inspired "snapshot" metaphor (`[[../docs/research/external_inspiration_llm_wiki_graph_001]]`, Section 2.5) applied to flat files.

---

## 6. Safety Summary

- The digest must include a fixed safety-summary section, always present, restating the core rules from `[[SAFETY_CONTRACT]]`: no secrets, no real API keys, no provider tokens, no `.env` values, no account IDs, no destructive git without approval, no deploy without approval, no MellyTrade mutation, no wholesale GLM workspace import.
- The digest must include a self-scan confirmation line: whether the blocklist scan (Section 3) found any blocklisted-pattern file present in the repo (a repo hygiene signal, not a content dump) — e.g., "Blocklist scan: 0 matches" or "Blocklist scan: 1 match found at `<path>` — review before proceeding," without printing the matched file's contents.

---

## 7. Task Queue Reference

- The digest may include a compact rendering of `shared_context/RUN_QUEUE.md`'s current task list (task IDs and one-line status only), so a reviewing agent has immediate situational awareness without opening a separate file.
- This is a read-only reflection of the existing queue file — the generator never edits `RUN_QUEUE.md`.

---

## 8. Hard Constraints (Restated for Emphasis)

- **No secrets.** Never included, never referenced by content, never partially quoted.
- **No PAT (personal access token) usage.** The generator does not authenticate to GitHub or any remote service.
- **No private/authenticated API calls of any kind.** Fully local and offline.
- **No automatic mutation.** The generator only reads and produces one output artifact; it never edits source files, never auto-commits, never auto-publishes anything into `docs/` or `shared_context/` without a human explicitly reviewing and committing the output, consistent with `[[SOURCE_INGEST_WORKFLOW]]` Step 9-10.

---

## 9. Relationship to the Knowledge Graph Console

A context pack produced under this spec is a candidate **input** to `[[SOURCE_INGEST_WORKFLOW]]` Step 1 (Collect Source) — it is not itself a `[[CONTEXT_GRAPH_SCHEMA]]` fixture. Turning a context pack's contents into graph nodes/edges still requires the full ingest workflow, including human review, before anything is published as a graph fixture.

---

*This specification is a docs-only artifact of `MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001`. It describes a future tool concept and authorizes no script, CLI, or automation implementation.*
