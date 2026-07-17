"""Tests for the cost estimator, worktree parser, redaction scanner, and audit.

The worktree tests parse fixture text and never invoke git or touch a real
worktree. The redaction tests build candidate strings at runtime by
concatenation so that no secret-shaped literal is ever committed to this file.
No test needs the network, a provider, or a credential.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

from scripts.loop_ops import persist as persist_module
from scripts.loop_ops.cost import BASIS, estimate_loop, estimate_realistic, estimate_scenario
from scripts.loop_ops.models import (
    TIER_CONFIGURED,
    TIER_EXERCISED,
    TIER_HUMAN_APPROVED,
    TIER_PRODUCTION_ENABLED,
    TIER_VALIDATED,
    InvalidInputError,
)
from scripts.loop_ops.readiness import audit_loop, audit_registry
from scripts.loop_ops.redaction import (
    CATEGORY_CONNECTION_STRING,
    CATEGORY_CREDENTIAL_PATTERN,
    CATEGORY_FIELD_NAME,
    CATEGORY_PRIVATE_KEY,
    scan_text,
)
from scripts.loop_ops.registry import parse_registry
from scripts.loop_ops.worktrees import (
    RISK_DIRTY,
    RISK_DUPLICATE_BRANCH,
    RISK_DUPLICATE_TASK,
    assess_risks,
    audit_report,
    parse_worktree_porcelain,
)
from tests.loop_ops_fixtures import make_budgets, make_loop, make_persistable_ledger, make_registry

FAKE_HEAD = "a" * 40
FAKE_BRANCH = "publish/mellycore-main-001"


def _persist_real_run(loop_id: str, root: Path, registry, run_id=None, **ledger_overrides) -> dict:
    """Test helper: persist a real, valid ledger via the actual persist-run apply
    path (with git identity mocked), so 'exercised' tests exercise the real
    integration between persist.py and readiness.py rather than a hand-built
    state file that merely claims a run happened.
    """
    import json as _json

    ledger = make_persistable_ledger(
        loop_id=loop_id, run_id=run_id, head_sha=FAKE_HEAD, branch=FAKE_BRANCH, **ledger_overrides
    )
    ledger_path = root / "incoming-ledger.json"
    ledger_path.write_text(_json.dumps(ledger), encoding="utf-8")
    with mock.patch.object(persist_module, "current_head", return_value=FAKE_HEAD), mock.patch.object(
        persist_module, "current_branch", return_value=FAKE_BRANCH
    ):
        return persist_module.apply(
            ledger_path,
            operator_approval_id="test-operator",
            expected_head=FAKE_HEAD,
            root=root,
            registry=registry,
        )

# --- cost --------------------------------------------------------------------


class CostEstimatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.budgets = make_budgets()

    def loop(self, **kw):
        return parse_registry(make_registry(loops=[make_loop(**kw)])).loops[0]

    def test_maker_checker_doubles_the_estimate(self) -> None:
        without = estimate_scenario(self.loop(verifier_required=False), self.budgets, "report")
        with_checker = estimate_scenario(self.loop(verifier_required=True), self.budgets, "report")
        self.assertEqual(without["estimated_tokens"] * 2, with_checker["estimated_tokens"])
        self.assertTrue(with_checker["multipliers"]["maker_checker_applied"])
        self.assertFalse(without["multipliers"]["maker_checker_applied"])

    def test_maker_checker_can_be_forced_on(self) -> None:
        loop = self.loop(verifier_required=False)
        forced = estimate_scenario(loop, self.budgets, "report", apply_maker_checker=True)
        natural = estimate_scenario(loop, self.budgets, "report")
        self.assertEqual(natural["estimated_tokens"] * 2, forced["estimated_tokens"])

    def test_maker_checker_can_be_forced_off(self) -> None:
        loop = self.loop(verifier_required=True)
        forced_off = estimate_scenario(loop, self.budgets, "report", apply_maker_checker=False)
        natural = estimate_scenario(loop, self.budgets, "report")
        self.assertEqual(natural["estimated_tokens"], forced_off["estimated_tokens"] * 2)

    def test_parallel_agents_multiplies_the_estimate(self) -> None:
        loop = self.loop(verifier_required=False)
        single = estimate_scenario(loop, self.budgets, "report", parallel_agents=1.0)
        triple = estimate_scenario(loop, self.budgets, "report", parallel_agents=3.0)
        self.assertEqual(single["estimated_tokens"] * 3, triple["estimated_tokens"])

    def test_retry_overhead_is_applied(self) -> None:
        # report base = 25000 + 3000 = 28000; retry 1.25 -> 35000
        result = estimate_scenario(self.loop(verifier_required=False), self.budgets, "report")
        self.assertEqual(28000, result["base_tokens"])
        self.assertEqual(35000, result["estimated_tokens"])

    def test_no_op_is_cheaper_than_report(self) -> None:
        loop = self.loop()
        self.assertLess(
            estimate_scenario(loop, self.budgets, "no_op")["estimated_tokens"],
            estimate_scenario(loop, self.budgets, "report")["estimated_tokens"],
        )

    def test_realistic_mix_sits_between_no_op_and_report(self) -> None:
        loop = self.loop(verifier_required=False)
        realistic = estimate_realistic(loop, self.budgets)["estimated_tokens"]
        no_op = estimate_scenario(loop, self.budgets, "no_op")["estimated_tokens"]
        report = estimate_scenario(loop, self.budgets, "report")["estimated_tokens"]
        self.assertGreater(realistic, no_op)
        self.assertLess(realistic, report)

    def test_every_estimate_is_labelled_as_an_estimate(self) -> None:
        report = estimate_loop(self.loop(), self.budgets)
        self.assertEqual(BASIS, report["basis"])
        self.assertEqual("ESTIMATE_NOT_MEASURED", report["basis"])
        for scenario in report["scenarios"]:
            self.assertEqual(BASIS, scenario["basis"])
        self.assertEqual(BASIS, report["realistic"]["basis"])

    def test_weights_must_sum_to_one(self) -> None:
        budgets = make_budgets()
        budgets["estimation_model"]["realistic_mix"]["weights"] = {"no_op": 0.5, "report": 0.2}
        with self.assertRaises(InvalidInputError):
            estimate_realistic(self.loop(), budgets)

    def test_unknown_scenario_is_refused(self) -> None:
        with self.assertRaises(InvalidInputError):
            estimate_scenario(self.loop(), self.budgets, "wishful_thinking")

    def test_zero_parallel_agents_is_refused(self) -> None:
        with self.assertRaises(InvalidInputError):
            estimate_scenario(self.loop(), self.budgets, "report", parallel_agents=0)

    def test_over_budget_scenario_is_flagged(self) -> None:
        loop = self.loop(per_run_token_budget=100)
        self.assertFalse(estimate_scenario(loop, self.budgets, "report")["within_per_run_budget"])


# --- worktrees ---------------------------------------------------------------

PORCELAIN_FIXTURE = """worktree C:/repo/main
HEAD 513e8e74d82f6c72010d11c5ef1b0a1527882270
branch refs/heads/publish/mellycore-main-001

worktree C:/repo/feature-a
HEAD 0c10e4ea768eaac9f988ebc137d87763487b9842
branch refs/heads/codex/mellycore-context-smoke-001

worktree C:/repo/detached
HEAD 7e70f9a04e5068971d8b633e7ec04d2329e34244
detached
"""

PORCELAIN_COLLISION = """worktree C:/repo/one
HEAD aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
branch refs/heads/codex/mellycore-task-001

worktree C:/repo/two
HEAD bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
branch refs/heads/agent/mellycore-task-001
"""


class WorktreeParserTests(unittest.TestCase):
    def test_parses_all_records(self) -> None:
        worktrees = parse_worktree_porcelain(PORCELAIN_FIXTURE)
        self.assertEqual(3, len(worktrees))

    def test_parses_path_branch_and_head(self) -> None:
        first = parse_worktree_porcelain(PORCELAIN_FIXTURE)[0]
        self.assertEqual("C:/repo/main", first.path)
        self.assertEqual("publish/mellycore-main-001", first.branch)
        self.assertEqual("513e8e74d82f6c72010d11c5ef1b0a1527882270", first.head)
        self.assertEqual("513e8e7", first.short_head)

    def test_strips_refs_heads_prefix(self) -> None:
        second = parse_worktree_porcelain(PORCELAIN_FIXTURE)[1]
        self.assertEqual("codex/mellycore-context-smoke-001", second.branch)

    def test_detached_head_is_detected(self) -> None:
        third = parse_worktree_porcelain(PORCELAIN_FIXTURE)[2]
        self.assertTrue(third.is_detached)
        self.assertIsNone(third.branch)

    def test_bare_worktree_is_detected(self) -> None:
        worktrees = parse_worktree_porcelain("worktree C:/repo/bare\nHEAD abc123\nbare\n")
        self.assertTrue(worktrees[0].is_bare)

    def test_empty_input_yields_nothing(self) -> None:
        self.assertEqual([], parse_worktree_porcelain(""))

    def test_records_without_blank_separator_are_parsed(self) -> None:
        text = "worktree C:/a\nHEAD aaa\nbranch refs/heads/x\nworktree C:/b\nHEAD bbb\nbranch refs/heads/y\n"
        worktrees = parse_worktree_porcelain(text)
        self.assertEqual(2, len(worktrees))
        self.assertEqual(["x", "y"], [w.branch for w in worktrees])

    def test_task_hint_strips_agent_prefix(self) -> None:
        worktrees = parse_worktree_porcelain(PORCELAIN_COLLISION)
        self.assertEqual("mellycore-task-001", worktrees[0].task_hint)
        self.assertEqual("mellycore-task-001", worktrees[1].task_hint)


class WorktreeRiskTests(unittest.TestCase):
    def test_duplicate_task_ownership_is_flagged(self) -> None:
        worktrees = assess_risks(parse_worktree_porcelain(PORCELAIN_COLLISION), known_paths_exist=False)
        for wt in worktrees:
            self.assertIn(RISK_DUPLICATE_TASK, wt.risks)

    def test_duplicate_branch_is_flagged(self) -> None:
        text = (
            "worktree C:/a\nHEAD aaa\nbranch refs/heads/same\n\n"
            "worktree C:/b\nHEAD bbb\nbranch refs/heads/same\n"
        )
        worktrees = assess_risks(parse_worktree_porcelain(text), known_paths_exist=False)
        self.assertIn(RISK_DUPLICATE_BRANCH, worktrees[0].risks)

    def test_dirty_worktree_is_flagged(self) -> None:
        worktrees = parse_worktree_porcelain(PORCELAIN_FIXTURE)
        worktrees[0].dirty = True
        assess_risks(worktrees, known_paths_exist=False)
        self.assertIn(RISK_DIRTY, worktrees[0].risks)

    def test_unknown_dirty_state_is_not_reported_as_clean(self) -> None:
        worktrees = parse_worktree_porcelain(PORCELAIN_FIXTURE)
        assess_risks(worktrees, known_paths_exist=False)
        self.assertIsNone(worktrees[0].dirty)
        self.assertNotIn(RISK_DIRTY, worktrees[0].risks)

    def test_no_collision_in_clean_fixture(self) -> None:
        worktrees = assess_risks(parse_worktree_porcelain(PORCELAIN_FIXTURE), known_paths_exist=False)
        self.assertNotIn(RISK_DUPLICATE_BRANCH, worktrees[0].risks)

    def test_report_declares_itself_read_only(self) -> None:
        report = audit_report(assess_risks(parse_worktree_porcelain(PORCELAIN_FIXTURE), False))
        self.assertTrue(report["read_only"])
        self.assertEqual(3, report["worktree_count"])


# --- redaction ---------------------------------------------------------------


class RedactionTests(unittest.TestCase):
    """Candidate strings are assembled at runtime so no secret-shaped literal is committed here."""

    def test_secret_bearing_field_name_is_detected(self) -> None:
        findings = scan_text('{"api' + '_key": "redacted"}', "state.json")
        self.assertEqual(1, len(findings))
        self.assertEqual(CATEGORY_FIELD_NAME, findings[0].category)

    def test_various_field_names_are_detected(self) -> None:
        for name in ("password", "secret", "token", "credential", "bearer", "account_id"):
            with self.subTest(name=name):
                findings = scan_text('"' + name + '": "x"', "state.json")
                self.assertTrue(findings, "expected {} to be flagged".format(name))

    def test_credential_shaped_value_is_detected(self) -> None:
        candidate = "value = " + "sk" + "-" + ("a" * 32)
        findings = scan_text(candidate, "ledger.json")
        self.assertTrue(any(f.category == CATEGORY_CREDENTIAL_PATTERN for f in findings))

    def test_private_key_block_is_detected(self) -> None:
        findings = scan_text("-----" + "BEGIN RSA PRIVATE KEY" + "-----", "state.json")
        self.assertTrue(any(f.category == CATEGORY_PRIVATE_KEY for f in findings))

    def test_connection_string_with_credentials_is_detected(self) -> None:
        candidate = "postgres" + "://user:" + "hunter2" + "@db.example.com/app"
        findings = scan_text(candidate, "state.json")
        self.assertTrue(any(f.category == CATEGORY_CONNECTION_STRING for f in findings))

    def test_finding_never_discloses_the_value(self) -> None:
        """The whole point: report the location, never the secret."""
        value = "sk" + "-" + ("z" * 40)
        findings = scan_text("key = " + value, "ledger.json")
        self.assertTrue(findings)
        for finding in findings:
            rendered = finding.render()
            payload = str(finding.to_dict())
            self.assertNotIn(value, rendered)
            self.assertNotIn(value, payload)
            self.assertNotIn("z" * 40, rendered)
            self.assertNotIn("z" * 40, payload)

    def test_finding_object_has_no_value_attribute(self) -> None:
        findings = scan_text('{"token": "x"}', "state.json")
        self.assertFalse(hasattr(findings[0], "value"))
        self.assertNotIn("value", findings[0].to_dict())

    def test_line_numbers_are_reported(self) -> None:
        text = "line one\nline two\n" + '"password": "x"'
        findings = scan_text(text, "state.json")
        self.assertEqual(3, findings[0].line)

    def test_clean_text_yields_no_findings(self) -> None:
        clean = '{"loop_id": "project-health", "status": "REPORT_ONLY", "consecutive_failures": 0}'
        self.assertEqual([], scan_text(clean, "state.json"))

    def test_scanning_does_not_modify_the_file(self) -> None:
        from scripts.loop_ops.redaction import scan_path

        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "state.json"
            original = '{"pass' + 'word": "x"}'
            target.write_text(original, encoding="utf-8")
            findings = scan_path(target, root=Path(tmp))
            self.assertTrue(findings)
            self.assertEqual(original, target.read_text(encoding="utf-8"))


# --- readiness audit ---------------------------------------------------------


class AuditTierTests(unittest.TestCase):
    """A registry entry proves configuration. It must never imply exercise."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def test_configured_does_not_imply_exercised(self) -> None:
        registry = parse_registry(make_registry())
        report = audit_loop(registry.loops[0], registry, root=self.root)
        self.assertTrue(report["capabilities"][TIER_CONFIGURED]["value"])
        self.assertTrue(report["capabilities"][TIER_VALIDATED]["value"])
        self.assertFalse(report["capabilities"][TIER_EXERCISED]["value"])
        self.assertFalse(report["capabilities"][TIER_HUMAN_APPROVED]["value"])
        self.assertFalse(report["capabilities"][TIER_PRODUCTION_ENABLED]["value"])
        self.assertEqual(TIER_VALIDATED, report["highest_earned_tier"])

    def test_state_file_without_runs_is_not_exercised(self) -> None:
        """An empty state file must not read as evidence of a run."""
        registry = parse_registry(make_registry(loops=[make_loop("sample-loop")]))
        state = self.root / "shared_context" / "loops" / "states" / "sample-loop.state.json"
        state.parent.mkdir(parents=True, exist_ok=True)
        state.write_text('{"loop_id": "sample-loop", "run_history": []}', encoding="utf-8")
        report = audit_loop(registry.loops[0], registry, root=self.root)
        self.assertFalse(report["capabilities"][TIER_EXERCISED]["value"])

    def test_recorded_run_counts_as_exercised(self) -> None:
        registry = parse_registry(make_registry(loops=[make_loop("sample-loop")]))
        _persist_real_run("sample-loop", self.root, registry)
        report = audit_loop(registry.loops[0], registry, root=self.root)
        self.assertTrue(report["capabilities"][TIER_EXERCISED]["value"])

    def test_run_history_entry_without_backing_evidence_is_not_exercised(self) -> None:
        """Closes D4: a run_history entry that merely claims a run_id and finished_at, with a
        ledger_ref that does not resolve to a real, validated evidence file, is an orphan claim,
        not exercised. Previously this state shape was (incorrectly) trusted at face value."""
        registry = parse_registry(make_registry(loops=[make_loop("sample-loop")]))
        state = self.root / "shared_context" / "loops" / "states" / "sample-loop.state.json"
        state.parent.mkdir(parents=True, exist_ok=True)
        state.write_text(
            '{"loop_id": "sample-loop", "run_history": ['
            '{"run_id": "r1", "finished_at": "2026-01-01T00:00:00Z", "outcome": "success", '
            '"ledger_ref": "shared_context/loops/runs/sample-loop/r1.json"}]}',
            encoding="utf-8",
        )
        report = audit_loop(registry.loops[0], registry, root=self.root)
        self.assertFalse(report["capabilities"][TIER_EXERCISED]["value"])

    def test_incomplete_run_entry_does_not_count(self) -> None:
        registry = parse_registry(make_registry(loops=[make_loop("sample-loop")]))
        state = self.root / "shared_context" / "loops" / "states" / "sample-loop.state.json"
        state.parent.mkdir(parents=True, exist_ok=True)
        state.write_text('{"run_history": [{"run_id": "r1"}]}', encoding="utf-8")
        report = audit_loop(registry.loops[0], registry, root=self.root)
        self.assertFalse(report["capabilities"][TIER_EXERCISED]["value"])

    def test_human_approval_requires_a_named_approver(self) -> None:
        registry = parse_registry(make_registry(loops=[make_loop("sample-loop")]))
        state = self.root / "shared_context" / "loops" / "states" / "sample-loop.state.json"
        state.parent.mkdir(parents=True, exist_ok=True)
        state.write_text('{"human_approval": {"granted": true}}', encoding="utf-8")
        report = audit_loop(registry.loops[0], registry, root=self.root)
        self.assertFalse(report["capabilities"][TIER_HUMAN_APPROVED]["value"])

    def test_production_enabled_is_unreachable_in_phase_1(self) -> None:
        """Even a fully approved, exercised, verifier-backed loop stays off in Phase 1."""
        import json as _json

        registry = parse_registry(make_registry(loops=[make_loop("sample-loop", verifier_required=True)]))
        _persist_real_run("sample-loop", self.root, registry)
        state_path = self.root / "shared_context" / "loops" / "states" / "sample-loop.state.json"
        state = _json.loads(state_path.read_text(encoding="utf-8"))
        state["human_approval"] = {"granted": True, "granted_by": "operator", "granted_at": None, "scope": None}
        state_path.write_text(_json.dumps(state), encoding="utf-8")
        report = audit_loop(registry.loops[0], registry, root=self.root)
        self.assertTrue(report["capabilities"][TIER_EXERCISED]["value"])
        self.assertTrue(report["capabilities"][TIER_HUMAN_APPROVED]["value"])
        self.assertFalse(report["capabilities"][TIER_PRODUCTION_ENABLED]["value"])
        self.assertIn("Phase 1", report["capabilities"][TIER_PRODUCTION_ENABLED]["evidence"])

    def test_failing_validation_is_reported_as_not_validated(self) -> None:
        registry = parse_registry(make_registry(loops=[make_loop(human_gates=[])]))
        report = audit_loop(registry.loops[0], registry, root=self.root)
        self.assertFalse(report["capabilities"][TIER_VALIDATED]["value"])
        self.assertIn("NO_HUMAN_GATE", report["capabilities"][TIER_VALIDATED]["evidence"])

    def test_registry_audit_reports_zero_exercised_honestly(self) -> None:
        registry = parse_registry(make_registry(loops=[make_loop("a"), make_loop("b")]))
        report = audit_registry(registry, root=self.root)
        self.assertEqual(0, report["summary"][TIER_EXERCISED])
        self.assertEqual(2, report["summary"][TIER_CONFIGURED])
        self.assertIn("No loop has been exercised", report["honest_assessment"])


class ShippedRegistryAuditTests(unittest.TestCase):
    def test_no_shipped_loop_is_production_enabled(self) -> None:
        """production_enabled must be structurally unreachable in Phase 1, regardless of how
        many loops have real persisted evidence. This does NOT assert exercised == 0: as of
        MELLYCORE-PROJECT-HEALTH-REGISTERED-RUN-001, the shipped project-health loop has one
        real, honestly-derived persisted run, and exercised is expected to be >= 1 from that
        point on. production_enabled staying 0 is the actual invariant this test protects."""
        from scripts.loop_ops.registry import load_registry

        report = audit_registry(load_registry())
        self.assertEqual(0, report["summary"][TIER_PRODUCTION_ENABLED])


if __name__ == "__main__":
    unittest.main()
