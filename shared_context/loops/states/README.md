# Loop States

**Task ID:** MELLYCORE-LOOP-OPERATIONS-FOUNDATION-001
**Status:** Phase 1 — no state files exist yet

---

## 1. Purpose

A loop's state lives here, as a file, on purpose. Conversations end, context windows fill, and sessions get cleared. If a loop's memory lives only in a conversation, the loop has no memory.

Each state file answers, for a fresh reader with no prior context: what is this loop's lifecycle state, what did it last achieve, is it waiting on a human, and has an operator actually approved anything.

## 2. Why This Directory Is Empty

Every loop in `../LOOP_REGISTRY.json` sets `state_file_is_template: true`, meaning its state file **need not exist yet**. None do, because no loop has been run.

This is deliberate. A state file is created by an actual run, and no run has happened. Pre-creating them would manufacture the appearance of history and would make the `audit` command's "exercised" signal meaningless — an empty file would look like evidence.

The `validate` command permits a missing state file only while `state_file_is_template` is true. Setting it to false makes the file's existence mandatory, which is the right setting once a loop is genuinely in service.

## 3. Shape

State files follow `../LOOP_STATE_SCHEMA.json` and are named `<loop-id>.state.json`, matching the `state_file` field of the loop's registry entry.

## 4. Rules

- **Never hand-write a state file to make a loop look exercised.** The point of this directory is honest history.
- **Never put a secret in one.** These files are committed. Report file, line, and category — never a value. See `../LOOP_CONSTRAINTS.md` section 7.
- **`human_approval.granted` means a real human really approved.** It is not a default, an inference, or a convenience.
- **Do not delete a state file to clear a blocked loop.** A blocked loop is information. Escalate instead.

## 5. Checking

```powershell
py -3.9 -m scripts.loop_ops redact-check --path shared_context/loops/states
```

Reports secret-shaped field names and credential patterns without printing any value and without modifying any file.
