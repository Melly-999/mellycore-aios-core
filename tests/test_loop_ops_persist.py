"""Tests for guarded loop-evidence persistence (scripts/loop_ops/persist.py).

Every test uses a temporary directory as ``root`` and mocks git identity via
``unittest.mock.patch.object`` on the module-level ``current_head`` /
``current_branch`` functions. Nothing here ever touches this repository's
real ``shared_context/loops/runs`` or ``shared_context/loops/states``
directories, and no test invokes a real git process.
"""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from scripts.loop_ops import persist as persist_module
from scripts.loop_ops.models import InvalidInputError
from scripts.loop_ops.readiness import audit_loop
from scripts.loop_ops.registry import parse_registry
from tests.loop_ops_fixtures import make_iteration, make_loop, make_persistable_ledger, make_registry, make_run_id

FAKE_HEAD = "a" * 40
OTHER_HEAD = "b" * 40
FAKE_BRANCH = "publish/mellycore-main-001"


class PersistTestCase(unittest.TestCase):
    """Base providing an isolated root and mocked git identity."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)
        self.registry = parse_registry(make_registry(loops=[make_loop("sample-loop")]))

        self._head_patch = mock.patch.object(persist_module, "current_head", return_value=FAKE_HEAD)
        self._branch_patch = mock.patch.object(persist_module, "current_branch", return_value=FAKE_BRANCH)
        self._head_patch.start()
        self._branch_patch.start()
        self.addCleanup(self._head_patch.stop)
        self.addCleanup(self._branch_patch.stop)

    def write_ledger(self, data: dict, name: str = "ledger.json") -> Path:
        path = self.root / name
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def dry_run(self, data: dict):
        return persist_module.dry_run(self.write_ledger(data), root=self.root, registry=self.registry)

    def apply(self, data: dict, approval="operator-1", expected_head=FAKE_HEAD):
        return persist_module.apply(
            self.write_ledger(data),
            operator_approval_id=approval,
            expected_head=expected_head,
            root=self.root,
            registry=self.registry,
        )


def good_ledger(**overrides):
    defaults = {"loop_id": "sample-loop", "head_sha": FAKE_HEAD, "branch": FAKE_BRANCH}
    defaults.update(overrides)
    return make_persistable_ledger(**defaults)


# --- run id / loop id format -------------------------------------------------


class RunIdFormatTests(PersistTestCase):
    def test_unknown_loop_id_is_refused(self) -> None:
        ledger = good_ledger(loop_id="never-registered", run_id=make_run_id("never-registered"))
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.dry_run(ledger)
        self.assertEqual("UNKNOWN_LOOP", ctx.exception.code)

    def test_malformed_run_id_is_refused(self) -> None:
        ledger = good_ledger(run_id="not-a-canonical-run-id")
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.dry_run(ledger)
        self.assertEqual("INVALID_RUN_ID", ctx.exception.code)

    def test_run_id_traversal_is_refused(self) -> None:
        ledger = good_ledger(run_id="../../../etc/passwd")
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.dry_run(ledger)
        self.assertEqual("INVALID_RUN_ID", ctx.exception.code)

    def test_run_id_absolute_path_attempt_is_refused(self) -> None:
        ledger = good_ledger(run_id="/etc/passwd--20260101T000000Z--a1b2c3d4e5f6")
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.dry_run(ledger)
        self.assertEqual("INVALID_RUN_ID", ctx.exception.code)

    def test_run_id_not_matching_its_own_loop_id_is_refused(self) -> None:
        ledger = good_ledger(run_id=make_run_id("a-different-loop"))
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.dry_run(ledger)
        self.assertIn(ctx.exception.code, ("INVALID_RUN_ID", "RUN_ID_LOOP_MISMATCH"))

    def test_resolve_run_path_lands_under_the_canonical_runs_directory(self) -> None:
        # A well-formed id resolves cleanly under the canonical runs root; the
        # containment check (target.resolve().relative_to(runs_root.resolve()))
        # is defense in depth against any future relaxation of the id patterns.
        path = persist_module.resolve_run_path(
            "sample-loop", "sample-loop--20260101T000000Z--" + "0" * 12, self.root
        )
        self.assertTrue(
            str(path)
            .replace("\\", "/")
            .endswith("shared_context/loops/runs/sample-loop/sample-loop--20260101T000000Z--000000000000.json")
        )


# --- repository identity ------------------------------------------------------


class RepositoryIdentityTests(PersistTestCase):
    def test_repository_head_mismatch_is_recorded_not_blocking(self) -> None:
        ledger = good_ledger(head_sha="c" * 40)
        plan = self.dry_run(ledger)
        self.assertTrue(any("head_sha mismatch" in w for w in plan.warnings))

    def test_repository_branch_mismatch_is_recorded_not_blocking(self) -> None:
        ledger = good_ledger(branch="some/other/branch")
        plan = self.dry_run(ledger)
        self.assertTrue(any("branch mismatch" in w for w in plan.warnings))

    def test_expected_head_mismatch_refuses_apply(self) -> None:
        ledger = good_ledger()
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.apply(ledger, expected_head=OTHER_HEAD)
        self.assertEqual("HEAD_MISMATCH", ctx.exception.code)


# --- approval / expected-head gating ------------------------------------------


class ApplyGatingTests(PersistTestCase):
    def test_missing_operator_approval_refuses_apply(self) -> None:
        ledger = good_ledger()
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.apply(ledger, approval=None)
        self.assertEqual("MISSING_APPROVAL", ctx.exception.code)
        self.assertFalse((self.root / persist_module.RUNS_DIRNAME).exists())

    def test_blank_operator_approval_refuses_apply(self) -> None:
        ledger = good_ledger()
        with self.assertRaises(persist_module.PersistenceRefused):
            self.apply(ledger, approval="   ")

    def test_missing_expected_head_refuses_apply(self) -> None:
        ledger = good_ledger()
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.apply(ledger, expected_head=None)
        self.assertEqual("MISSING_EXPECTED_HEAD", ctx.exception.code)
        self.assertFalse((self.root / persist_module.RUNS_DIRNAME).exists())


# --- dry run vs apply ----------------------------------------------------------


class DryRunTests(PersistTestCase):
    def test_dry_run_writes_nothing(self) -> None:
        ledger = good_ledger()
        self.dry_run(ledger)
        self.assertFalse((self.root / persist_module.RUNS_DIRNAME).exists())
        self.assertFalse((self.root / persist_module.STATES_DIRNAME).exists())

    def test_dry_run_proposes_correct_destinations(self) -> None:
        run_id = make_run_id("sample-loop")
        ledger = good_ledger(run_id=run_id)
        plan = self.dry_run(ledger)
        self.assertEqual("shared_context/loops/runs/sample-loop/{}.json".format(run_id), plan.evidence_relpath)
        self.assertEqual("shared_context/loops/states/sample-loop.state.json", plan.state_relpath)


class ApplyTests(PersistTestCase):
    def test_valid_apply_writes_evidence_and_state(self) -> None:
        ledger = good_ledger()
        result = self.apply(ledger)
        self.assertTrue(Path(self.root / result["evidence_path"]).exists())
        self.assertTrue(Path(self.root / result["state_path"]).exists())
        self.assertEqual("absent", result["evidence_status"])
        self.assertTrue(result["evidence_written"])

    def test_persisted_evidence_records_guard_decision_and_exit_code(self) -> None:
        ledger = good_ledger()
        result = self.apply(ledger)
        record = json.loads((self.root / result["evidence_path"]).read_text(encoding="utf-8"))
        self.assertIn(record["guard_evaluation"]["decision"], ("CONTINUE", "ESCALATE_HUMAN", "PAUSE_BUDGET"))
        self.assertEqual(result["guard_decision"], record["guard_evaluation"]["decision"])
        self.assertIn("exit_code", record["guard_evaluation"])
        self.assertEqual("PERSISTED", record["final_classification"])

    def test_operator_approval_id_is_recorded_as_audit_metadata(self) -> None:
        ledger = good_ledger()
        result = self.apply(ledger, approval="mateusz-2026-07-15")
        record = json.loads((self.root / result["evidence_path"]).read_text(encoding="utf-8"))
        self.assertEqual("mateusz-2026-07-15", record["persisted_by"]["operator_approval_id"])
        self.assertIn("not cryptographic proof", record["persisted_by"]["note"])

    def test_duplicate_conflicting_run_id_is_refused(self) -> None:
        run_id = make_run_id("sample-loop")
        self.apply(good_ledger(run_id=run_id, outcome="success"))
        original_bytes = (self.root / persist_module.RUNS_DIRNAME / "sample-loop" / (run_id + ".json")).read_bytes()
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.apply(good_ledger(run_id=run_id, outcome="failure"))
        self.assertEqual("EVIDENCE_CONFLICT", ctx.exception.code)
        after_bytes = (self.root / persist_module.RUNS_DIRNAME / "sample-loop" / (run_id + ".json")).read_bytes()
        self.assertEqual(original_bytes, after_bytes)

    def test_identical_evidence_can_recover_a_missing_state(self) -> None:
        run_id = make_run_id("sample-loop")
        ledger = good_ledger(run_id=run_id)
        first = self.apply(ledger)
        # Simulate an interrupted first attempt: evidence exists, state does not.
        (self.root / first["state_path"]).unlink()
        result = self.apply(ledger)
        self.assertEqual("identical", result["evidence_status"])
        self.assertFalse(result["evidence_written"])
        self.assertTrue((self.root / result["state_path"]).exists())

    def test_never_writes_without_explicit_approver_even_if_head_matches(self) -> None:
        ledger = good_ledger()
        with self.assertRaises(persist_module.PersistenceRefused):
            self.apply(ledger, approval="")
        self.assertFalse((self.root / persist_module.RUNS_DIRNAME).exists())


# --- Phase 1 REPORT_ONLY invariants -------------------------------------------


class ReportOnlyInvariantTests(PersistTestCase):
    def test_nonzero_mutation_count_is_refused(self) -> None:
        ledger = good_ledger(repository_mutation_count=1)
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.dry_run(ledger)
        self.assertEqual("NONZERO_MUTATION_COUNT", ctx.exception.code)

    def test_nonzero_remote_action_count_is_refused(self) -> None:
        ledger = good_ledger(remote_action_count=1)
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.dry_run(ledger)
        self.assertEqual("NONZERO_REMOTE_ACTION_COUNT", ctx.exception.code)

    def test_lifecycle_promotion_beyond_report_only_is_refused(self) -> None:
        ledger = good_ledger(status_after="ASSISTED")
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.dry_run(ledger)
        self.assertEqual("LIFECYCLE_PROMOTION_FORBIDDEN", ctx.exception.code)

    def test_invalid_lifecycle_transition_is_refused(self) -> None:
        ledger = good_ledger(status_before="BLOCKED", status_after="REPORT_ONLY")
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.dry_run(ledger)
        self.assertEqual("INVALID_TRANSITION", ctx.exception.code)


# --- timestamps ----------------------------------------------------------------


class TimestampTests(PersistTestCase):
    def test_future_timestamp_is_refused(self) -> None:
        ledger = good_ledger(started_at="2099-01-01T00:00:00Z", completed_at="2099-01-01T00:05:00Z")
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.dry_run(ledger)
        self.assertEqual("FUTURE_TIMESTAMP", ctx.exception.code)

    def test_completed_before_started_is_refused(self) -> None:
        ledger = good_ledger(started_at="2026-01-01T00:05:00Z", completed_at="2026-01-01T00:00:00Z")
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.dry_run(ledger)
        self.assertEqual("FINISHED_BEFORE_STARTED", ctx.exception.code)


# --- redaction -----------------------------------------------------------------


class RedactionGateTests(PersistTestCase):
    def test_secret_shaped_content_blocks_persistence(self) -> None:
        candidate_key = "sk" + "-" + ("a" * 32)
        ledger = good_ledger()
        ledger["notes"] = "leaked value = " + candidate_key
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.dry_run(ledger)
        self.assertEqual("REDACTION_FINDING", ctx.exception.code)
        self.assertFalse((self.root / persist_module.RUNS_DIRNAME).exists())


# --- required fields -----------------------------------------------------------


class RequiredFieldTests(PersistTestCase):
    def test_missing_persist_only_field_is_refused(self) -> None:
        ledger = good_ledger()
        del ledger["repository"]
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.dry_run(ledger)
        self.assertEqual("MISSING_PERSIST_FIELDS", ctx.exception.code)

    def test_invalid_outcome_is_refused(self) -> None:
        ledger = good_ledger(outcome="maybe")
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.dry_run(ledger)
        self.assertEqual("INVALID_OUTCOME", ctx.exception.code)

    def test_negative_mutation_count_is_refused(self) -> None:
        ledger = good_ledger(repository_mutation_count=-1)
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.dry_run(ledger)
        self.assertEqual("INVALID_COUNT", ctx.exception.code)

    def test_base_ledger_invariants_still_apply(self) -> None:
        """persist-run reuses registry.parse_ledger, so the corrected token
        contract and every other base invariant apply here too."""
        ledger = good_ledger(iterations=[make_iteration(1, tokens_total=5, measured=False)])
        with self.assertRaises(InvalidInputError):
            self.dry_run(ledger)


# --- symlink and case-collision safety -----------------------------------------


class PathSafetyTests(PersistTestCase):
    def test_symlinked_loop_directory_is_refused(self) -> None:
        runs_root = self.root / persist_module.RUNS_DIRNAME
        runs_root.mkdir(parents=True, exist_ok=True)
        real_target = self.root / "elsewhere"
        real_target.mkdir(parents=True, exist_ok=True)
        symlink_path = runs_root / "sample-loop"
        try:
            symlink_path.symlink_to(real_target, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("symlink creation not permitted in this environment")
        ledger = good_ledger()
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.dry_run(ledger)
        # A symlinked loop directory pointing outside runs_root is refused
        # either by the explicit symlink check or by the path-containment
        # check (since resolve() follows the symlink) -- both are valid,
        # fail-closed outcomes for this scenario.
        self.assertIn(ctx.exception.code, ("SYMLINK_IN_PATH", "PATH_ESCAPE"))
        self.assertFalse((self.root / persist_module.STATES_DIRNAME).exists())

    def test_case_collision_on_loop_directory_is_refused(self) -> None:
        runs_root = self.root / persist_module.RUNS_DIRNAME
        (runs_root / "Sample-Loop").mkdir(parents=True, exist_ok=True)
        ledger = good_ledger()
        with self.assertRaises(persist_module.PersistenceRefused) as ctx:
            self.dry_run(ledger)
        self.assertEqual("CASE_COLLISION", ctx.exception.code)


# --- audit integration (D4 closure) ---------------------------------------------


class AuditIntegrationTests(PersistTestCase):
    def test_orphan_evidence_without_state_pointer_is_not_exercised(self) -> None:
        """An evidence file existing on disk with no state entry pointing to it must not, by
        itself, make the audit report the loop as exercised -- the audit only ever reads
        run_history in state, never scans the runs/ directory directly."""
        ledger = good_ledger()
        ledger_path = self.write_ledger(ledger)
        # Validate-only: write the evidence file by hand, without ever calling apply(), so no
        # state file is created at all.
        plan = persist_module.dry_run(ledger_path, root=self.root, registry=self.registry)
        record = {
            "schema_version": "1.0",
            "ledger": plan.ledger_raw,
            "final_classification": "PERSISTED",
        }
        plan.evidence_path.parent.mkdir(parents=True, exist_ok=True)
        plan.evidence_path.write_text(json.dumps(record), encoding="utf-8")

        report = audit_loop(self.registry.loops[0], self.registry, root=self.root)
        self.assertFalse(report["capabilities"]["exercised"]["value"])

    def test_human_approval_is_never_set_by_persisting_a_run(self) -> None:
        result = self.apply(good_ledger())
        self.assertFalse(result["state"]["human_approval"]["granted"])

    def test_production_enablement_is_never_inferred_from_persisting_a_run(self) -> None:
        self.apply(good_ledger())
        report = audit_loop(self.registry.loops[0], self.registry, root=self.root)
        self.assertFalse(report["capabilities"]["production_enabled"]["value"])

    def test_state_is_reconstructible_from_evidence_alone(self) -> None:
        """Rebuilding state fresh from the persisted evidence set alone reproduces exactly the
        state the incremental persist actions already wrote."""
        first_run = make_run_id("sample-loop", timestamp="20260101T000000Z", suffix="1" * 12)
        second_run = make_run_id("sample-loop", timestamp="20260102T000000Z", suffix="2" * 12)
        self.apply(good_ledger(run_id=first_run, completed_at="2026-01-01T00:05:00Z"))
        result = self.apply(good_ledger(run_id=second_run, completed_at="2026-01-02T00:05:00Z"))

        records = persist_module.list_persisted_ledgers("sample-loop", self.root)
        self.assertEqual(2, len(records))
        rebuilt = persist_module.derive_state("sample-loop", records, existing_state=None)

        on_disk = json.loads((self.root / result["state_path"]).read_text(encoding="utf-8"))
        self.assertEqual(
            [entry["run_id"] for entry in rebuilt["run_history"]],
            [entry["run_id"] for entry in on_disk["run_history"]],
        )
        self.assertEqual(rebuilt["status"], on_disk["status"])


if __name__ == "__main__":
    unittest.main()
