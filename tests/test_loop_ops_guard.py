"""Tests for the deterministic loop circuit breaker.

The guard must never call a model or the network, and must fail closed. These
tests use in-memory ledgers and a temporary directory for the kill switch, so no
real repository state is touched.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.loop_ops.guard import evaluate, normalize_error, transition_allowed
from scripts.loop_ops.models import (
    BLOCK_INVALID_STATE,
    CONTINUE,
    ESCALATE_HUMAN,
    EXIT_ESCALATE,
    EXIT_INVALID,
    EXIT_OK,
    PAUSE_BUDGET,
    InvalidInputError,
)
from scripts.loop_ops.registry import parse_ledger, parse_registry
from tests.loop_ops_fixtures import make_iteration, make_ledger, make_loop, make_registry


class GuardTestCase(unittest.TestCase):
    """Base providing an isolated root so the kill switch file is never real."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def decide(self, ledger_data, registry_data=None):
        registry = parse_registry(registry_data or make_registry())
        ledger = parse_ledger(ledger_data)
        return evaluate(ledger, registry, root=self.root)


class ContinueTests(GuardTestCase):
    def test_healthy_run_continues(self) -> None:
        decision = self.decide(make_ledger(iterations=[make_iteration(1, outcome="success")]))
        self.assertEqual(CONTINUE, decision.decision)
        self.assertEqual(EXIT_OK, decision.exit_code)

    def test_guard_is_deterministic(self) -> None:
        ledger = make_ledger(iterations=[make_iteration(1, outcome="failure", error_signature="e1")])
        first = self.decide(ledger)
        second = self.decide(ledger)
        self.assertEqual(first.decision, second.decision)
        self.assertEqual(first.reasons, second.reasons)


class MaxAttemptsTests(GuardTestCase):
    def test_reaching_max_attempts_escalates(self) -> None:
        loop = make_loop(max_attempts=3, stagnation_threshold=99, no_progress_threshold=99)
        iterations = [
            make_iteration(1, outcome="failure", error_signature="a", progress_marker="p1"),
            make_iteration(2, outcome="failure", error_signature="b", progress_marker="p2"),
            make_iteration(3, outcome="failure", error_signature="c", progress_marker="p3"),
        ]
        decision = self.decide(
            make_ledger(iterations=iterations), make_registry(loops=[loop])
        )
        self.assertEqual(ESCALATE_HUMAN, decision.decision)
        self.assertEqual(EXIT_ESCALATE, decision.exit_code)
        self.assertEqual("fail", decision.checks["max_attempts"])

    def test_below_max_attempts_continues(self) -> None:
        loop = make_loop(max_attempts=5, stagnation_threshold=99, no_progress_threshold=99)
        decision = self.decide(
            make_ledger(iterations=[make_iteration(1, outcome="success", progress_marker="p1")]),
            make_registry(loops=[loop]),
        )
        self.assertEqual(CONTINUE, decision.decision)


class StagnationTests(GuardTestCase):
    def test_same_error_repeated_escalates(self) -> None:
        loop = make_loop(max_attempts=10, stagnation_threshold=2, no_progress_threshold=99)
        iterations = [
            make_iteration(1, outcome="failure", error_signature="import_error", progress_marker="p1"),
            make_iteration(2, outcome="failure", error_signature="import_error", progress_marker="p2"),
        ]
        decision = self.decide(make_ledger(iterations=iterations), make_registry(loops=[loop]))
        self.assertEqual(ESCALATE_HUMAN, decision.decision)
        self.assertEqual("fail", decision.checks["stagnation"])

    def test_error_signatures_are_normalized_before_comparison(self) -> None:
        loop = make_loop(max_attempts=10, stagnation_threshold=2, no_progress_threshold=99)
        iterations = [
            make_iteration(1, outcome="failure", error_signature="Import  Error", progress_marker="p1"),
            make_iteration(2, outcome="failure", error_signature="import error", progress_marker="p2"),
        ]
        decision = self.decide(make_ledger(iterations=iterations), make_registry(loops=[loop]))
        self.assertEqual(ESCALATE_HUMAN, decision.decision)

    def test_different_errors_do_not_trigger_stagnation(self) -> None:
        loop = make_loop(max_attempts=10, stagnation_threshold=2, no_progress_threshold=99)
        iterations = [
            make_iteration(1, outcome="failure", error_signature="error_one", progress_marker="p1"),
            make_iteration(2, outcome="failure", error_signature="error_two", progress_marker="p2"),
        ]
        decision = self.decide(make_ledger(iterations=iterations), make_registry(loops=[loop]))
        self.assertEqual(CONTINUE, decision.decision)

    def test_normalize_error_handles_none(self) -> None:
        self.assertEqual("", normalize_error(None))


class NoProgressTests(GuardTestCase):
    def test_unchanged_progress_marker_escalates(self) -> None:
        loop = make_loop(max_attempts=10, stagnation_threshold=99, no_progress_threshold=2)
        iterations = [
            make_iteration(1, outcome="success", progress_marker="stuck"),
            make_iteration(2, outcome="success", progress_marker="stuck"),
        ]
        decision = self.decide(make_ledger(iterations=iterations), make_registry(loops=[loop]))
        self.assertEqual(ESCALATE_HUMAN, decision.decision)
        self.assertEqual("fail", decision.checks["no_progress"])

    def test_changing_progress_marker_continues(self) -> None:
        loop = make_loop(max_attempts=10, stagnation_threshold=99, no_progress_threshold=2)
        iterations = [
            make_iteration(1, outcome="success", progress_marker="step-a"),
            make_iteration(2, outcome="success", progress_marker="step-b"),
        ]
        decision = self.decide(make_ledger(iterations=iterations), make_registry(loops=[loop]))
        self.assertEqual(CONTINUE, decision.decision)

    def test_single_attempt_cannot_show_no_progress(self) -> None:
        loop = make_loop(max_attempts=10, stagnation_threshold=99, no_progress_threshold=1)
        decision = self.decide(
            make_ledger(iterations=[make_iteration(1, outcome="success", progress_marker="only")]),
            make_registry(loops=[loop]),
        )
        self.assertEqual(CONTINUE, decision.decision)


class ConsecutiveFailureTests(GuardTestCase):
    def test_consecutive_failures_escalate(self) -> None:
        loop = make_loop(max_attempts=2, stagnation_threshold=99, no_progress_threshold=99)
        iterations = [
            make_iteration(1, outcome="failure", error_signature="x", progress_marker="p1"),
            make_iteration(2, outcome="failure", error_signature="y", progress_marker="p2"),
        ]
        decision = self.decide(make_ledger(iterations=iterations), make_registry(loops=[loop]))
        self.assertEqual(ESCALATE_HUMAN, decision.decision)
        self.assertEqual("fail", decision.checks["consecutive_failures"])


class BudgetTests(GuardTestCase):
    def test_measured_tokens_over_per_run_budget_pauses(self) -> None:
        loop = make_loop(per_run_token_budget=1000, daily_token_budget=10000)
        iterations = [make_iteration(1, outcome="success", tokens_total=5000, measured=True)]
        decision = self.decide(make_ledger(iterations=iterations), make_registry(loops=[loop]))
        self.assertEqual(PAUSE_BUDGET, decision.decision)
        self.assertEqual(EXIT_ESCALATE, decision.exit_code)
        self.assertEqual("fail", decision.checks["per_run_budget"])

    def test_measured_daily_tokens_over_budget_pauses(self) -> None:
        loop = make_loop(per_run_token_budget=50000, daily_token_budget=10000)
        decision = self.decide(
            make_ledger(iterations=[make_iteration(1, outcome="success")], daily_tokens_used=99999),
            make_registry(loops=[loop]),
        )
        self.assertEqual(PAUSE_BUDGET, decision.decision)
        self.assertEqual("fail", decision.checks["daily_budget"])

    def test_unmeasured_tokens_never_trigger_a_budget_pause(self) -> None:
        """An estimate must not be enforceable. Over-budget-looking but unmeasured stays CONTINUE."""
        loop = make_loop(per_run_token_budget=1000, daily_token_budget=10000)
        iterations = [make_iteration(1, outcome="success", tokens_total=999999, measured=False)]
        decision = self.decide(make_ledger(iterations=iterations), make_registry(loops=[loop]))
        self.assertEqual(CONTINUE, decision.decision)
        self.assertEqual("unenforceable", decision.checks["per_run_budget"])

    def test_absent_daily_total_is_unenforceable_not_pass(self) -> None:
        decision = self.decide(make_ledger(daily_tokens_used=None))
        self.assertEqual("unenforceable", decision.checks["daily_budget"])


class KillSwitchTests(GuardTestCase):
    def test_kill_switch_file_halts_everything(self) -> None:
        switch = self.root / "shared_context" / "loops" / "KILL_SWITCH"
        switch.parent.mkdir(parents=True, exist_ok=True)
        switch.write_text("halt", encoding="utf-8")
        decision = self.decide(make_ledger())
        self.assertEqual(ESCALATE_HUMAN, decision.decision)
        self.assertEqual("fail", decision.checks["kill_switch"])

    def test_kill_switch_flag_in_ledger_halts_everything(self) -> None:
        decision = self.decide(make_ledger(kill_switch_engaged=True))
        self.assertEqual(ESCALATE_HUMAN, decision.decision)

    def test_kill_switch_outranks_budget(self) -> None:
        """Kill switch is checked before budgets, so the reported reason is the halt."""
        switch = self.root / "shared_context" / "loops" / "KILL_SWITCH"
        switch.parent.mkdir(parents=True, exist_ok=True)
        switch.write_text("halt", encoding="utf-8")
        loop = make_loop(per_run_token_budget=1)
        decision = self.decide(
            make_ledger(iterations=[make_iteration(1, tokens_total=9999, measured=True)]),
            make_registry(loops=[loop]),
        )
        self.assertEqual(ESCALATE_HUMAN, decision.decision)
        self.assertIn("kill switch", " ".join(decision.reasons).lower())

    def test_absent_kill_switch_passes(self) -> None:
        decision = self.decide(make_ledger())
        self.assertEqual("pass", decision.checks["kill_switch"])


class InvalidStateTests(GuardTestCase):
    def test_forbidden_transition_blocks(self) -> None:
        decision = self.decide(make_ledger(status_before="DRAFT", status_after="ASSISTED"))
        self.assertEqual(BLOCK_INVALID_STATE, decision.decision)
        self.assertEqual(EXIT_INVALID, decision.exit_code)
        self.assertEqual("fail", decision.checks["lifecycle_transition"])

    def test_blocked_cannot_resume_directly(self) -> None:
        decision = self.decide(make_ledger(status_before="BLOCKED", status_after="REPORT_ONLY"))
        self.assertEqual(BLOCK_INVALID_STATE, decision.decision)

    def test_blocked_may_move_to_waiting_human(self) -> None:
        self.assertTrue(transition_allowed("BLOCKED", "WAITING_HUMAN"))

    def test_unknown_loop_blocks(self) -> None:
        decision = self.decide(make_ledger(loop_id="never-heard-of-it"))
        self.assertEqual(BLOCK_INVALID_STATE, decision.decision)

    def test_disabled_loop_blocks(self) -> None:
        loop = make_loop(status="DISABLED", disabled_reason="off for tests")
        decision = self.decide(
            make_ledger(status_before="DISABLED", status_after="DISABLED"),
            make_registry(loops=[loop]),
        )
        self.assertEqual(BLOCK_INVALID_STATE, decision.decision)

    def test_unknown_state_name_blocks(self) -> None:
        decision = self.decide(make_ledger(status_before="MADE_UP", status_after="REPORT_ONLY"))
        self.assertEqual(BLOCK_INVALID_STATE, decision.decision)


class VerifierTests(GuardTestCase):
    def test_verifier_reject_escalates(self) -> None:
        loop = make_loop(verifier_required=True, max_attempts=10, stagnation_threshold=99)
        iterations = [make_iteration(1, outcome="success", verdict="REJECT", progress_marker="p1")]
        decision = self.decide(make_ledger(iterations=iterations), make_registry(loops=[loop]))
        self.assertEqual(ESCALATE_HUMAN, decision.decision)
        self.assertEqual("fail", decision.checks["verifier"])

    def test_verifier_accept_continues(self) -> None:
        loop = make_loop(verifier_required=True, max_attempts=10, stagnation_threshold=99)
        iterations = [make_iteration(1, outcome="success", verdict="ACCEPT", progress_marker="p1")]
        decision = self.decide(make_ledger(iterations=iterations), make_registry(loops=[loop]))
        self.assertEqual(CONTINUE, decision.decision)


class LedgerIntegrityTests(unittest.TestCase):
    def test_failed_iteration_without_error_signature_is_refused(self) -> None:
        """Without a signature, stagnation detection would silently stop working."""
        bad = make_ledger(iterations=[make_iteration(1, outcome="failure")])
        bad["iterations"][0]["error_signature"] = None
        with self.assertRaises(InvalidInputError):
            parse_ledger(bad)

    def test_duplicate_iteration_index_is_refused(self) -> None:
        bad = make_ledger(iterations=[make_iteration(1), make_iteration(1)])
        with self.assertRaises(InvalidInputError):
            parse_ledger(bad)

    def test_out_of_order_iteration_index_is_refused(self) -> None:
        bad = make_ledger(iterations=[make_iteration(2), make_iteration(1)])
        with self.assertRaises(InvalidInputError):
            parse_ledger(bad)

    def test_unsupported_ledger_version_is_refused(self) -> None:
        with self.assertRaises(InvalidInputError):
            parse_ledger(make_ledger(schema_version="9.0"))

    def test_invalid_outcome_is_refused(self) -> None:
        bad = make_ledger()
        bad["iterations"][0]["outcome"] = "maybe"
        with self.assertRaises(InvalidInputError):
            parse_ledger(bad)


if __name__ == "__main__":
    unittest.main()
