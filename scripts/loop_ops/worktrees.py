"""Read-only git worktree audit.

This module runs exactly one git command, ``git worktree list --porcelain``, and
one optional ``git status --porcelain`` per worktree. It never removes, prunes,
unlocks, resets, cleans, or otherwise modifies a worktree or branch. There is no
code path here that mutates anything, and there must never be one: cleanup is an
operator decision.

Parsing is a pure function over text so that tests exercise it with fixtures and
never touch a real repository.
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional

from .models import InvalidInputError
from .registry import repo_root

RISK_DUPLICATE_BRANCH = "duplicate_branch"
RISK_DUPLICATE_TASK = "duplicate_task_ownership"
RISK_DIRTY = "dirty_worktree"
RISK_DETACHED = "detached_head"
RISK_STALE = "possibly_stale"
RISK_MISSING_PATH = "path_missing"


class Worktree:
    """One linked worktree as reported by git."""

    __slots__ = ("path", "branch", "head", "is_bare", "is_detached", "dirty", "risks")

    def __init__(
        self,
        path: str,
        branch: Optional[str],
        head: Optional[str],
        is_bare: bool = False,
        is_detached: bool = False,
    ) -> None:
        self.path = path
        self.branch = branch
        self.head = head
        self.is_bare = is_bare
        self.is_detached = is_detached
        self.dirty: Optional[bool] = None  # None means not safely determinable
        self.risks: List[str] = []

    @property
    def short_head(self) -> str:
        return (self.head or "")[:7]

    @property
    def task_hint(self) -> Optional[str]:
        """Best-effort task identity from the branch name.

        Branches here look like ``codex/mellycore-context-smoke-001`` or
        ``agent/mellycore-public-polish-001``. The segment after the agent
        prefix is the task. Two worktrees claiming the same task is a collision
        risk worth reporting.
        """
        if not self.branch:
            return None
        parts = self.branch.split("/", 1)
        return parts[1] if len(parts) == 2 else self.branch

    def to_dict(self) -> Dict[str, Any]:
        return {
            "path": self.path,
            "branch": self.branch,
            "head": self.head,
            "short_head": self.short_head,
            "is_bare": self.is_bare,
            "is_detached": self.is_detached,
            "dirty": self.dirty,
            "task_hint": self.task_hint,
            "risks": list(self.risks),
        }


def parse_worktree_porcelain(text: str) -> List[Worktree]:
    """Parse the output of ``git worktree list --porcelain``.

    Records are separated by a blank line. Each begins with ``worktree <path>``,
    followed by ``HEAD <sha>``, and then either ``branch refs/heads/<name>``,
    ``detached``, or ``bare``.
    """
    worktrees: List[Worktree] = []
    path: Optional[str] = None
    head: Optional[str] = None
    branch: Optional[str] = None
    is_bare = False
    is_detached = False

    def flush() -> None:
        if path is not None:
            worktrees.append(
                Worktree(path=path, branch=branch, head=head, is_bare=is_bare, is_detached=is_detached)
            )

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            flush()
            path, head, branch, is_bare, is_detached = None, None, None, False, False
            continue
        if line.startswith("worktree "):
            # A new record without a blank separator; flush the previous one.
            if path is not None:
                flush()
                head, branch, is_bare, is_detached = None, None, False, False
            path = line[len("worktree ") :].strip()
        elif line.startswith("HEAD "):
            head = line[len("HEAD ") :].strip()
        elif line.startswith("branch "):
            ref = line[len("branch ") :].strip()
            branch = ref[len("refs/heads/") :] if ref.startswith("refs/heads/") else ref
        elif line == "bare":
            is_bare = True
        elif line == "detached":
            is_detached = True

    flush()
    return worktrees


def assess_risks(worktrees: List[Worktree], known_paths_exist: bool = True) -> List[Worktree]:
    """Annotate worktrees with collision and hygiene risks. Pure; mutates only the objects passed in."""
    branch_counts: Dict[str, int] = {}
    task_counts: Dict[str, int] = {}
    for wt in worktrees:
        if wt.branch:
            branch_counts[wt.branch] = branch_counts.get(wt.branch, 0) + 1
        hint = wt.task_hint
        if hint:
            task_counts[hint] = task_counts.get(hint, 0) + 1

    for wt in worktrees:
        if wt.branch and branch_counts.get(wt.branch, 0) > 1:
            wt.risks.append(RISK_DUPLICATE_BRANCH)
        hint = wt.task_hint
        if hint and task_counts.get(hint, 0) > 1 and RISK_DUPLICATE_BRANCH not in wt.risks:
            wt.risks.append(RISK_DUPLICATE_TASK)
        if wt.is_detached:
            wt.risks.append(RISK_DETACHED)
        if wt.dirty is True:
            wt.risks.append(RISK_DIRTY)
        if known_paths_exist and wt.path and not Path(wt.path).exists():
            wt.risks.append(RISK_MISSING_PATH)
            wt.risks.append(RISK_STALE)
    return worktrees


def _run_git(args: List[str], cwd: Path) -> str:
    """Run a read-only git command and return stdout."""
    try:
        completed = subprocess.run(
            ["git"] + args,
            cwd=str(cwd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=30,
        )
    except FileNotFoundError as exc:
        raise InvalidInputError("git executable not found") from exc
    except subprocess.TimeoutExpired as exc:
        raise InvalidInputError("git command timed out: git {}".format(" ".join(args))) from exc
    if completed.returncode != 0:
        raise InvalidInputError(
            "git {} failed: {}".format(" ".join(args), completed.stderr.decode("utf-8", "replace").strip())
        )
    return completed.stdout.decode("utf-8", "replace")


def collect_worktrees(root: Optional[Path] = None, check_dirty: bool = True) -> List[Worktree]:
    """List worktrees via read-only git inspection.

    ``dirty`` stays None when it cannot be determined safely, which is reported
    as "unknown" rather than guessed as clean.
    """
    root = root or repo_root()
    text = _run_git(["worktree", "list", "--porcelain"], cwd=root)
    worktrees = parse_worktree_porcelain(text)

    if check_dirty:
        for wt in worktrees:
            if wt.is_bare or not wt.path:
                continue
            wt_path = Path(wt.path)
            if not wt_path.exists():
                continue
            try:
                status = _run_git(["status", "--porcelain"], cwd=wt_path)
            except InvalidInputError:
                wt.dirty = None
                continue
            wt.dirty = bool(status.strip())

    return assess_risks(worktrees)


def audit_report(worktrees: List[Worktree]) -> Dict[str, Any]:
    """Build a machine-readable worktree audit report."""
    return {
        "read_only": True,
        "read_only_note": (
            "This audit only reads. It never removes, prunes, unlocks, resets, or cleans a worktree. "
            "Any cleanup is an operator decision."
        ),
        "worktree_count": len(worktrees),
        "worktrees": [wt.to_dict() for wt in worktrees],
        "risk_summary": {
            risk: sum(1 for wt in worktrees if risk in wt.risks)
            for risk in (
                RISK_DUPLICATE_BRANCH,
                RISK_DUPLICATE_TASK,
                RISK_DIRTY,
                RISK_DETACHED,
                RISK_STALE,
                RISK_MISSING_PATH,
            )
        },
    }
