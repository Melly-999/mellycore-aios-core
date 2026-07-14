"""Shared data models and constants for MellyCore loop operations.

Standard library only, Python 3.9 compatible. Nothing in this module performs
I/O, calls a model, or mutates state.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

# --- Contract versions -------------------------------------------------------

SUPPORTED_REGISTRY_MAJOR = "1"
SUPPORTED_LEDGER_MAJOR = "1"
SUPPORTED_STATE_MAJOR = "1"

# --- Exit codes --------------------------------------------------------------
# Deterministic and stable. Callers and CI may depend on these.

EXIT_OK = 0
EXIT_INVALID = 1
EXIT_ESCALATE = 2

# --- Lifecycle ---------------------------------------------------------------

LIFECYCLE_STATES = (
    "DRAFT",
    "REPORT_ONLY",
    "ASSISTED",
    "WAITING_HUMAN",
    "PAUSED",
    "BLOCKED",
    "COMPLETED",
    "DISABLED",
)

LEVELS = ("L0", "L1", "L2", "L3")

#: Levels that can change something. Never enabled in Phase 1.
ACTION_CAPABLE_LEVELS = ("L2", "L3")

#: Statuses meaning "this loop may run right now".
ENABLED_STATUSES = ("REPORT_ONLY", "ASSISTED")

#: Statuses forbidden outright in Phase 1. ASSISTED implies acting on the repo.
PHASE1_FORBIDDEN_STATUSES = ("ASSISTED",)

TRIGGER_TYPES = ("manual", "schedule", "event")

#: Allowed lifecycle transitions.
#:
#: Two rules are deliberately strict. DRAFT cannot jump straight to ASSISTED --
#: a loop earns action capability by first proving itself report-only. And
#: BLOCKED cannot return directly to running; it must pass through
#: WAITING_HUMAN, because a human decided it was blocked and a human decides it
#: is not.
ALLOWED_TRANSITIONS: Dict[str, tuple] = {
    "DRAFT": ("DRAFT", "REPORT_ONLY", "DISABLED"),
    "REPORT_ONLY": (
        "REPORT_ONLY",
        "WAITING_HUMAN",
        "PAUSED",
        "BLOCKED",
        "COMPLETED",
        "DISABLED",
        "ASSISTED",
    ),
    "ASSISTED": (
        "ASSISTED",
        "REPORT_ONLY",
        "WAITING_HUMAN",
        "PAUSED",
        "BLOCKED",
        "COMPLETED",
        "DISABLED",
    ),
    "WAITING_HUMAN": (
        "WAITING_HUMAN",
        "REPORT_ONLY",
        "ASSISTED",
        "PAUSED",
        "BLOCKED",
        "COMPLETED",
        "DISABLED",
    ),
    "PAUSED": ("PAUSED", "REPORT_ONLY", "ASSISTED", "WAITING_HUMAN", "BLOCKED", "DISABLED"),
    "BLOCKED": ("BLOCKED", "WAITING_HUMAN", "PAUSED", "DISABLED"),
    "COMPLETED": ("COMPLETED", "DISABLED", "DRAFT"),
    "DISABLED": ("DISABLED", "DRAFT", "REPORT_ONLY"),
}

# --- Guard decisions ---------------------------------------------------------

CONTINUE = "CONTINUE"
ESCALATE_HUMAN = "ESCALATE_HUMAN"
PAUSE_BUDGET = "PAUSE_BUDGET"
BLOCK_INVALID_STATE = "BLOCK_INVALID_STATE"

DECISION_EXIT_CODES = {
    CONTINUE: EXIT_OK,
    ESCALATE_HUMAN: EXIT_ESCALATE,
    PAUSE_BUDGET: EXIT_ESCALATE,
    BLOCK_INVALID_STATE: EXIT_INVALID,
}

# --- Capability tiers --------------------------------------------------------
#
# Ordered weakest to strongest. The distinction matters: a registry entry proves
# only that someone wrote a file. It says nothing about whether the loop works,
# has ever run, or is trusted. Each tier must be earned separately, and the
# audit never infers a stronger tier from a weaker one.

TIER_CONFIGURED = "configured"
TIER_VALIDATED = "validated"
TIER_EXERCISED = "exercised"
TIER_HUMAN_APPROVED = "human_approved"
TIER_PRODUCTION_ENABLED = "production_enabled"

CAPABILITY_TIERS = (
    TIER_CONFIGURED,
    TIER_VALIDATED,
    TIER_EXERCISED,
    TIER_HUMAN_APPROVED,
    TIER_PRODUCTION_ENABLED,
)

TIER_DEFINITIONS = {
    TIER_CONFIGURED: "A registry entry exists with the required fields. Proves authorship, nothing more.",
    TIER_VALIDATED: "The entry passes structural and safety validation.",
    TIER_EXERCISED: "At least one real run is recorded in a run ledger. Not satisfied by an example file.",
    TIER_HUMAN_APPROVED: "An operator recorded explicit approval in the loop state.",
    TIER_PRODUCTION_ENABLED: "Unattended operation. Requires every tier above plus an independent verifier and an approved enabling task. Not reachable in Phase 1.",
}


class LoopOpsError(Exception):
    """Base class for loop-ops failures that should exit non-zero cleanly."""


class InvalidInputError(LoopOpsError):
    """Input file is missing, unparseable, or violates its contract."""


@dataclass(frozen=True)
class Finding:
    """A single validation or audit finding.

    ``severity`` is ``error`` (fails validation) or ``warning`` (reported only).
    """

    severity: str
    code: str
    message: str
    loop_id: Optional[str] = None

    def render(self) -> str:
        where = " [{}]".format(self.loop_id) if self.loop_id else ""
        return "{} {}{}: {}".format(self.severity.upper(), self.code, where, self.message)


@dataclass(frozen=True)
class LoopSpec:
    """One loop entry from the registry."""

    id: str
    title: str
    purpose: str
    owner: str
    level: str
    status: str
    trigger_type: str
    suggested_cadence: str
    read_scope: List[str]
    allowed_write_scope: List[str]
    forbidden_paths: List[str]
    state_file: str
    verifier_required: bool
    max_attempts: int
    stagnation_threshold: int
    no_progress_threshold: int
    per_run_token_budget: int
    daily_token_budget: int
    human_gates: List[str]
    kill_switch: str
    success_condition: str
    escalation_condition: str
    state_file_is_template: bool = True
    raw: Dict[str, Any] = field(default_factory=dict)

    @property
    def is_action_capable(self) -> bool:
        """True if this loop's level or write scope means it could change something."""
        return self.level in ACTION_CAPABLE_LEVELS or bool(self.allowed_write_scope)

    @property
    def is_enabled(self) -> bool:
        return self.status in ENABLED_STATUSES


@dataclass(frozen=True)
class Registry:
    """The parsed loop registry."""

    schema_version: str
    registry_id: str
    phase: int
    global_kill_switch: Dict[str, Any]
    global_forbidden_paths: List[str]
    lifecycle_states: List[str]
    loops: List[LoopSpec]
    raw: Dict[str, Any] = field(default_factory=dict)

    def get(self, loop_id: str) -> Optional[LoopSpec]:
        for loop in self.loops:
            if loop.id == loop_id:
                return loop
        return None


@dataclass(frozen=True)
class Iteration:
    """One attempt inside a run ledger."""

    index: int
    started_at: str
    outcome: str
    error_signature: Optional[str] = None
    progress_marker: Optional[str] = None
    tokens_total: int = 0
    tokens_measured: bool = False
    verifier_verdict: str = "NOT_RUN"

    @property
    def failed(self) -> bool:
        return self.outcome == "failure"


@dataclass(frozen=True)
class RunLedger:
    """A parsed run ledger. The only input the circuit breaker trusts."""

    schema_version: str
    loop_id: str
    run_id: str
    started_at: str
    status_before: str
    status_after: str
    iterations: List[Iteration]
    daily_tokens_used: Optional[int] = None
    kill_switch_engaged: bool = False
    raw: Dict[str, Any] = field(default_factory=dict)

    @property
    def measured_run_tokens(self) -> int:
        """Total of MEASURED tokens only.

        Unmeasured values are ignored rather than counted, so an estimate can
        never trigger or satisfy a budget check.
        """
        return sum(i.tokens_total for i in self.iterations if i.tokens_measured)

    @property
    def has_unmeasured_tokens(self) -> bool:
        return any(i.tokens_total > 0 and not i.tokens_measured for i in self.iterations)


@dataclass(frozen=True)
class GuardDecision:
    """The circuit breaker's verdict."""

    decision: str
    reasons: List[str]
    checks: Dict[str, str]
    loop_id: Optional[str] = None
    run_id: Optional[str] = None

    @property
    def exit_code(self) -> int:
        return DECISION_EXIT_CODES[self.decision]
