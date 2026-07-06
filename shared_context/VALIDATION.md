# Validation

Baseline validation commands:

```powershell
python scripts/validate_project_state.py
git diff --check
git status --short
```

Validation should confirm required scaffold files, shared context files, safety placeholders, absence of `.env`, and no obvious provider key patterns in tracked markdown/example files.

