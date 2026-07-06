from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "PROJECT_RULES.md",
    ".gitignore",
    ".env.example",
    "docs/references/glm_workspace_inventory.md",
    "docs/design/glm_css_effects_reference.md",
]

SHARED_CONTEXT_FILES = [
    "shared_context/PROJECT_STATE.md",
    "shared_context/AGENT_HANDOFF.md",
    "shared_context/RUN_QUEUE.md",
    "shared_context/DECISIONS.md",
    "shared_context/VALIDATION.md",
    "shared_context/MODEL_ROUTING.md",
    "shared_context/PROVIDER_SETUP.md",
    "shared_context/TOOLING.md",
    "shared_context/CROSS_AGENT_CONTEXT.md",
    "shared_context/SAFETY_CONTRACT.md",
    "shared_context/DESIGN_SYSTEM.md",
    "shared_context/ROADMAP.md",
]

AGENT_PROMPTS = [
    "agent_prompts/codex/README.md",
    "agent_prompts/claude/README.md",
    "agent_prompts/glm/README.md",
    "agent_prompts/grok/README.md",
    "agent_prompts/warp/README.md",
    "agent_prompts/zed/README.md",
    "agent_prompts/chatgpt/README.md",
]

DOC_READMES = [
    "docs/architecture/README.md",
    "docs/design/README.md",
    "docs/roadmap/README.md",
    "docs/website/README.md",
    "docs/3d/README.md",
    "docs/evidence/README.md",
    "docs/references/README.md",
]

WARP_AND_EDITOR_FILES = [
    ".warp/workflows/safe_status.md",
    ".warp/workflows/validate_project.md",
    ".warp/workflows/update_handoff.md",
    ".warp/rules/mellycore_rules.md",
    ".warp/prompts/operator_prompt.md",
    ".zed/settings.example.json",
    ".vscode/settings.example.json",
]

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"sk-proj-[A-Za-z0-9_-]{20,}"),
    re.compile(r"npg_[A-Za-z0-9]{20,}"),
    re.compile(r"(?i)(api[_-]?key|token|secret)[ \t]*[:=][ \t]*['\"]?[A-Za-z0-9_\-]{16,}"),
]


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)
    print(f"FAIL {message}")


def check_exists(paths: list[str], failures: list[str]) -> None:
    for rel_path in paths:
        if not (ROOT / rel_path).exists():
            fail(f"missing required file: {rel_path}", failures)


def tracked_text_files() -> list[Path]:
    include_suffixes = {".md", ".example", ".json", ".py", ".txt"}
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.name == ".env":
            continue
        if path.suffix in include_suffixes or path.name == ".env.example":
            files.append(path)
    return files


def main() -> int:
    failures: list[str] = []

    check_exists(REQUIRED_FILES, failures)
    check_exists(SHARED_CONTEXT_FILES, failures)
    check_exists(AGENT_PROMPTS, failures)
    check_exists(DOC_READMES, failures)
    check_exists(WARP_AND_EDITOR_FILES, failures)

    if (ROOT / ".env").exists():
        fail(".env must not be present in repo", failures)

    if not (ROOT / ".env.example").exists():
        fail(".env.example is required", failures)

    for path in tracked_text_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(f"possible secret pattern in {path.relative_to(ROOT)}", failures)
                break

    design = (ROOT / "shared_context/DESIGN_SYSTEM.md").read_text(encoding="utf-8", errors="replace").lower()
    for word in ["purple", "blue", "orbital", "cube"]:
        if word not in design:
            fail(f"DESIGN_SYSTEM.md must mention {word}", failures)

    routing = (ROOT / "shared_context/MODEL_ROUTING.md").read_text(encoding="utf-8", errors="replace").lower()
    for word in ["glm", "grok", "omnirouter", "codex", "claude", "chatgpt"]:
        if word not in routing:
            fail(f"MODEL_ROUTING.md must mention {word}", failures)

    if failures:
        print(f"FAIL validation failed with {len(failures)} issue(s)")
        return 1

    print("PASS MellyCore project scaffold validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
