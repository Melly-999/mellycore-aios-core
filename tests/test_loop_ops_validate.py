"""Tests for loop registry parsing and Phase 1 policy validation.

No network, no provider access, no secrets, no real worktree mutation.
"""

from __future__ import annotations

import unittest

from scripts.loop_ops.models import InvalidInputError
from scripts.loop_ops.registry import parse_registry
from scripts.loop_ops.validators import has_errors, validate
from tests.loop_ops_fixtures import make_loop, make_registry


def codes(findings) -> list:
    return [f.code for f in findings]


class ValidRegistryTests(unittest.TestCase):
    def test_minimal_registry_is_valid(self) -> None:
        registry = parse_registry(make_registry())
        findings = validate(registry)
        self.assertEqual([], codes(findings))
        self.assertFalse(has_errors(findings))

    def test_registry_reports_parsed_loops(self) -> None:
        registry = parse_registry(make_registry(loops=[make_loop("alpha"), make_loop("beta")]))
        self.assertEqual(["alpha", "beta"], [loop.id for loop in registry.loops])
        self.assertIsNotNone(registry.get("alpha"))
        self.assertIsNone(registry.get("does-not-exist"))

    def test_unsupported_schema_version_is_refused(self) -> None:
        with self.assertRaises(InvalidInputError):
            parse_registry(make_registry(schema_version="2.0"))

    def test_missing_required_field_is_refused(self) -> None:
        loop = make_loop()
        del loop["human_gates"]
        with self.assertRaises(InvalidInputError):
            parse_registry(make_registry(loops=[loop]))


class DuplicateIdTests(unittest.TestCase):
    def test_duplicate_loop_id_is_an_error(self) -> None:
        registry = parse_registry(make_registry(loops=[make_loop("same"), make_loop("same")]))
        findings = validate(registry)
        self.assertIn("DUPLICATE_LOOP_ID", codes(findings))
        self.assertTrue(has_errors(findings))


class LifecycleTests(unittest.TestCase):
    def test_invalid_lifecycle_state_is_an_error(self) -> None:
        registry = parse_registry(make_registry(loops=[make_loop(status="RUNNING_WILD")]))
        findings = validate(registry)
        self.assertIn("INVALID_STATUS", codes(findings))
        self.assertTrue(has_errors(findings))

    def test_invalid_level_is_an_error(self) -> None:
        registry = parse_registry(make_registry(loops=[make_loop(level="L9")]))
        self.assertIn("INVALID_LEVEL", codes(validate(registry)))

    def test_registry_lifecycle_set_must_match_implementation(self) -> None:
        registry = parse_registry(make_registry(lifecycle_states=["DRAFT", "REPORT_ONLY"]))
        self.assertIn("LIFECYCLE_SET_MISMATCH", codes(validate(registry)))


class Phase1GateTests(unittest.TestCase):
    """The gates that keep Phase 1 report-only."""

    def test_enabled_loop_with_write_scope_is_rejected(self) -> None:
        registry = parse_registry(
            make_registry(loops=[make_loop(status="REPORT_ONLY", allowed_write_scope=["src/**"])])
        )
        findings = validate(registry)
        self.assertIn("PHASE1_ENABLED_ACTION_LOOP", codes(findings))
        self.assertTrue(has_errors(findings))

    def test_enabled_loop_at_action_capable_level_is_rejected(self) -> None:
        registry = parse_registry(make_registry(loops=[make_loop(level="L2", status="REPORT_ONLY")]))
        self.assertIn("PHASE1_ENABLED_ACTION_LEVEL", codes(validate(registry)))

    def test_assisted_status_is_forbidden_in_phase_1(self) -> None:
        registry = parse_registry(make_registry(loops=[make_loop(status="ASSISTED")]))
        self.assertIn("PHASE1_STATUS_FORBIDDEN", codes(validate(registry)))

    def test_disabled_action_loop_is_allowed(self) -> None:
        """A DISABLED L2 loop with a stated reason is the sanctioned way to record future intent."""
        registry = parse_registry(
            make_registry(
                loops=[
                    make_loop(
                        level="L2",
                        status="DISABLED",
                        allowed_write_scope=["FUTURE_ONLY: tbd"],
                        disabled_reason="Out of scope for Phase 1.",
                    )
                ]
            )
        )
        self.assertEqual([], codes(validate(registry)))

    def test_disabled_loop_without_reason_is_an_error(self) -> None:
        registry = parse_registry(make_registry(loops=[make_loop(status="DISABLED")]))
        self.assertIn("DISABLED_WITHOUT_REASON", codes(validate(registry)))


class BudgetValidationTests(unittest.TestCase):
    def test_zero_budget_is_an_error(self) -> None:
        registry = parse_registry(make_registry(loops=[make_loop(per_run_token_budget=0)]))
        self.assertIn("BUDGET_NOT_POSITIVE", codes(validate(registry)))

    def test_negative_max_attempts_is_an_error(self) -> None:
        registry = parse_registry(make_registry(loops=[make_loop(max_attempts=-1)]))
        self.assertIn("BUDGET_NOT_POSITIVE", codes(validate(registry)))

    def test_daily_budget_below_per_run_budget_is_an_error(self) -> None:
        registry = parse_registry(
            make_registry(loops=[make_loop(per_run_token_budget=50000, daily_token_budget=1000)])
        )
        self.assertIn("BUDGET_INCOHERENT", codes(validate(registry)))


class ForbiddenPathTests(unittest.TestCase):
    def test_empty_forbidden_paths_is_an_error(self) -> None:
        registry = parse_registry(make_registry(loops=[make_loop(forbidden_paths=[])]))
        self.assertIn("FORBIDDEN_PATHS_EMPTY", codes(validate(registry)))

    def test_loop_missing_a_global_forbidden_path_is_an_error(self) -> None:
        registry = parse_registry(make_registry(loops=[make_loop(forbidden_paths=[".env"])]))
        findings = validate(registry)
        self.assertIn("FORBIDDEN_PATHS_INCOMPLETE", codes(findings))

    def test_loop_cannot_opt_out_of_the_global_kill_switch(self) -> None:
        registry = parse_registry(make_registry(loops=[make_loop(kill_switch="some/other/switch")]))
        self.assertIn("KILL_SWITCH_MISMATCH", codes(validate(registry)))


class HumanGateTests(unittest.TestCase):
    def test_loop_without_human_gate_is_an_error(self) -> None:
        registry = parse_registry(make_registry(loops=[make_loop(human_gates=[])]))
        self.assertIn("NO_HUMAN_GATE", codes(validate(registry)))


class StateFileTests(unittest.TestCase):
    def test_missing_non_template_state_file_is_an_error(self) -> None:
        registry = parse_registry(
            make_registry(
                loops=[
                    make_loop(
                        state_file="shared_context/loops/states/definitely-absent.state.json",
                        state_file_is_template=False,
                    )
                ]
            )
        )
        self.assertIn("STATE_FILE_MISSING", codes(validate(registry)))

    def test_template_state_file_may_be_absent(self) -> None:
        registry = parse_registry(
            make_registry(
                loops=[
                    make_loop(
                        state_file="shared_context/loops/states/definitely-absent.state.json",
                        state_file_is_template=True,
                    )
                ]
            )
        )
        self.assertEqual([], codes(validate(registry)))


class RealRegistryTests(unittest.TestCase):
    """The registry actually shipped in this repo must pass its own rules."""

    def test_shipped_registry_validates(self) -> None:
        from scripts.loop_ops.registry import load_registry

        registry = load_registry()
        findings = validate(registry)
        self.assertFalse(
            has_errors(findings),
            "shipped LOOP_REGISTRY.json has validation errors: {}".format(
                [f.render() for f in findings if f.severity == "error"]
            ),
        )

    def test_shipped_registry_has_no_enabled_action_loop(self) -> None:
        from scripts.loop_ops.registry import load_registry

        for loop in load_registry().loops:
            if loop.is_enabled:
                self.assertEqual(
                    [], loop.allowed_write_scope, "enabled loop {} declares a write scope".format(loop.id)
                )


if __name__ == "__main__":
    unittest.main()
