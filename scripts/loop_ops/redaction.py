"""Secret-shape detection for loop state and ledger files.

State files and ledgers are committed to the repository, so anything written
into one is visible to every reader of this repo. This module reports where a
secret-shaped string appears so a human can remove it.

Two rules govern this module absolutely:

1. **It never prints a detected value.** Output is file, line number, and
   category only. A scanner that echoes the secret it found has published the
   secret to the terminal, the log, and the transcript.
2. **It never modifies a file.** It reports; a human decides.

Detection is heuristic. A finding is a candidate for human review, not a
verdict, and a clean scan is not proof that a file is free of secrets.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

from .models import InvalidInputError
from .registry import repo_root

CATEGORY_FIELD_NAME = "secret_bearing_field_name"
CATEGORY_CREDENTIAL_PATTERN = "credential_like_value"
CATEGORY_PRIVATE_KEY = "private_key_block"
CATEGORY_CONNECTION_STRING = "connection_string_with_credentials"

#: Field names that should never appear as keys in a committed state file or
#: ledger. Matching a name is enough to warrant review; the value is never read
#: out, only located.
_FIELD_NAME_WORDS = (
    "api[_-]?key",
    "apikey",
    "secret",
    "client[_-]?secret",
    "token",
    "auth[_-]?token",
    "access[_-]?key",
    "private[_-]?key",
    "password",
    "passwd",
    "credential",
    "session[_-]?cookie",
    "bearer",
    "account[_-]?id",
)

_FIELD_NAME_RE = re.compile(
    r"(?i)[\"']?(" + "|".join(_FIELD_NAME_WORDS) + r")[\"']?\s*(?::|=)"
)

#: Value shapes that look like real credentials regardless of field name.
_VALUE_PATTERNS = (
    (CATEGORY_CREDENTIAL_PATTERN, re.compile(r"sk" + r"-[A-Za-z0-9_\-]{16,}")),
    (CATEGORY_CREDENTIAL_PATTERN, re.compile(r"gh[pousr]" + r"_[A-Za-z0-9]{20,}")),
    (CATEGORY_CREDENTIAL_PATTERN, re.compile(r"xox[baprs]" + r"-[A-Za-z0-9\-]{10,}")),
    (CATEGORY_CREDENTIAL_PATTERN, re.compile(r"AKIA" + r"[0-9A-Z]{16}")),
    (CATEGORY_CREDENTIAL_PATTERN, re.compile(r"npg" + r"_[A-Za-z0-9]{20,}")),
    (CATEGORY_CREDENTIAL_PATTERN, re.compile(r"eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.")),
    (CATEGORY_PRIVATE_KEY, re.compile(r"BEGIN [A-Z ]*PRIVATE KEY")),
    (
        CATEGORY_CONNECTION_STRING,
        re.compile(r"(?i)\b(?:postgres|postgresql|mysql|mongodb|redis|amqp)(?:\+\w+)?://[^\s:@/]+:[^\s:@/]+@"),
    ),
)

DEFAULT_SUFFIXES = (".json", ".md", ".txt", ".log")


class RedactionFinding:
    """One secret-shaped location.

    Carries no value field by construction, so a value cannot leak through this
    object even by accident.
    """

    __slots__ = ("path", "line", "category", "detail")

    def __init__(self, path: str, line: int, category: str, detail: str) -> None:
        self.path = path
        self.line = line
        self.category = category
        self.detail = detail

    def to_dict(self) -> Dict[str, Any]:
        return {
            "file": self.path,
            "line": self.line,
            "category": self.category,
            "detail": self.detail,
        }

    def render(self) -> str:
        return "{}:{}: {} ({})".format(self.path, self.line, self.category, self.detail)


def scan_text(text: str, path_label: str) -> List[RedactionFinding]:
    """Scan text and report secret-shaped locations.

    Never includes matched text in a finding: only the category and the field
    name that triggered it.
    """
    findings: List[RedactionFinding] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        match = _FIELD_NAME_RE.search(line)
        if match:
            findings.append(
                RedactionFinding(
                    path=path_label,
                    line=lineno,
                    category=CATEGORY_FIELD_NAME,
                    detail="field name {!r} suggests a credential-bearing key".format(
                        match.group(1).lower()
                    ),
                )
            )
        for category, pattern in _VALUE_PATTERNS:
            if pattern.search(line):
                findings.append(
                    RedactionFinding(
                        path=path_label,
                        line=lineno,
                        category=category,
                        detail="a value on this line matches a known credential shape; value withheld",
                    )
                )
                break
    return findings


def iter_target_files(
    target: Path,
    suffixes: Iterable[str] = DEFAULT_SUFFIXES,
) -> List[Path]:
    """List files to scan under ``target``."""
    if target.is_file():
        return [target]
    if not target.exists():
        raise InvalidInputError("path not found: {}".format(target))
    allowed = tuple(suffixes)
    found = [p for p in sorted(target.rglob("*")) if p.is_file() and p.suffix in allowed]
    return found


def scan_path(
    target: Any,
    root: Optional[Path] = None,
    suffixes: Iterable[str] = DEFAULT_SUFFIXES,
) -> List[RedactionFinding]:
    """Scan a file or directory. Read-only; nothing is written or rewritten."""
    root = root or repo_root()
    path = Path(str(target))
    if not path.is_absolute():
        path = root / path

    findings: List[RedactionFinding] = []
    for file_path in iter_target_files(path, suffixes):
        try:
            text = file_path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            raise InvalidInputError("cannot read {}: {}".format(file_path, exc)) from exc
        try:
            label = str(file_path.relative_to(root))
        except ValueError:
            label = str(file_path)
        findings.extend(scan_text(text, label.replace("\\", "/")))
    return findings
