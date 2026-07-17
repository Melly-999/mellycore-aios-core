"""Focused Phase I3 tests for the derived index and read-only audit."""

from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest import mock

from context_gate_fixtures import canonical_record
from scripts.context_gate import audit as audit_module
from scripts.context_gate import cli as cli_module
from scripts.context_gate import index as index_module
from scripts.context_gate.models import EXIT_INVALID, EXIT_OK, InvalidInputError, deterministic_json_bytes
from scripts.context_gate.store import REFUSAL_LOG_RELPATH

ROOT = Path(__file__).resolve().parents[1]


class IndexAuditTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)
        self.records_dir = self.root / "shared_context" / "context_provenance" / "records"
        self.records_dir.mkdir(parents=True)
        self.refusal_log = self.root / REFUSAL_LOG_RELPATH
        self.refusal_log.parent.mkdir(parents=True)
        self.refusal_log.write_text("", encoding="utf-8")

    def write_record(self, source_id: str, **overrides):
        data = canonical_record(
            source_id=source_id,
            reviewed_by="Test Operator",
            reviewed_at="2026-07-17",
            decision="admitted",
            decision_at="2026-07-17",
            decision_rationale="Decision verified for the synthetic test fixture.",
        )
        data.update(overrides)
        path = self.records_dir / (source_id + ".json")
        path.write_bytes(deterministic_json_bytes(data))
        return path

    def append_refusal(self, reason_code: str) -> None:
        entry = {
            "refused_at": "2026-07-17",
            "reason_code": reason_code,
            "proposed_by": "TEST-PROPOSER",
            "batch_id": "TEST-BATCH",
            "gate_spec_version": "MELLYCORE_CONTEXT_INGESTION_GATE_SPEC_001 v1.0",
        }
        with self.refusal_log.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(json.dumps(entry, sort_keys=True) + "\n")

    def snapshot(self):
        return {
            str(path.relative_to(self.root)): path.read_bytes()
            for path in sorted(self.root.rglob("*"))
            if path.is_file()
        }


class RebuildIndexTests(IndexAuditTestCase):
    def test_rebuild_is_deterministic_and_second_run_is_identical(self) -> None:
        self.write_record("ctx-2026-07-17-index-a")
        self.write_record("ctx-2026-07-17-index-b")
        first = index_module.rebuild_index(self.root)
        first_bytes = (self.root / index_module.INDEX_RELPATH).read_bytes()
        second = index_module.rebuild_index(self.root)
        second_bytes = (self.root / index_module.INDEX_RELPATH).read_bytes()
        self.assertEqual("written", first.status)
        self.assertEqual("identical", second.status)
        self.assertEqual(1, first.writes_performed)
        self.assertEqual(0, second.writes_performed)
        self.assertEqual(first_bytes, second_bytes)

    def test_index_contains_only_the_content_free_allowlist(self) -> None:
        marker = "CONTENT_MARKER_MUST_NOT_ENTER_INDEX"
        self.write_record(
            "ctx-2026-07-17-content-free",
            source_identity="operator-specific source description",
            claim=marker,
            notes="Reviewer note " + marker,
        )
        index_module.rebuild_index(self.root)
        raw = (self.root / index_module.INDEX_RELPATH).read_bytes()
        payload = json.loads(raw.decode("utf-8"))
        entry = payload["records"][0]
        expected = set(index_module.INDEX_ENTRY_FIELDS) | {"file", "validation_outcome"}
        self.assertEqual(expected, set(entry))
        self.assertNotIn(marker.encode("utf-8"), raw)
        self.assertNotIn(b"source_identity", raw)
        self.assertNotIn(b"claim", raw)
        self.assertNotIn(b"notes", raw)

    def test_invalid_canonical_record_blocks_rebuild_without_index_write(self) -> None:
        path = self.write_record("ctx-2026-07-17-invalid")
        data = json.loads(path.read_text(encoding="utf-8"))
        del data["decision_rationale"]
        path.write_bytes(deterministic_json_bytes(data))
        with self.assertRaises(InvalidInputError):
            index_module.rebuild_index(self.root)
        self.assertFalse((self.root / index_module.INDEX_RELPATH).exists())

    def test_rebuild_changes_only_derived_index(self) -> None:
        self.write_record("ctx-2026-07-17-only-index-write")
        self.append_refusal("trust_cap_violation")
        records_before = {path.name: path.read_bytes() for path in self.records_dir.glob("*.json")}
        refusal_before = self.refusal_log.read_bytes()
        index_module.rebuild_index(self.root)
        self.assertEqual(records_before, {path.name: path.read_bytes() for path in self.records_dir.glob("*.json")})
        self.assertEqual(refusal_before, self.refusal_log.read_bytes())
        self.assertTrue((self.root / index_module.INDEX_RELPATH).is_file())


class AuditTests(IndexAuditTestCase):
    def populate_audit_store(self) -> None:
        self.write_record("ctx-2026-07-17-current-historical")
        self.write_record(
            "ctx-2026-07-17-stale",
            staleness_policy="volatile",
            review_after="2026-07-16",
        )
        self.write_record(
            "ctx-2026-07-17-expiring",
            source_type="generated",
            trust_level="medium",
            staleness_policy="periodic_review",
            review_after="2026-07-20",
        )
        self.write_record(
            "ctx-2026-07-17-fresh-rejected",
            source_type="user_provided",
            decision="rejected",
            staleness_policy="periodic_review",
            review_after="2026-09-01",
        )
        self.write_record(
            "ctx-2026-07-17-superseded",
            staleness_policy="volatile",
            review_after="2026-07-10",
            superseded_by="ctx-2026-07-17-current-historical",
        )
        self.append_refusal("trust_cap_violation")
        self.append_refusal("trust_cap_violation")
        self.append_refusal("secret_content")
        index_module.rebuild_index(self.root)

    def test_audit_counts_freshness_decisions_trust_sensitivity_and_refusals(self) -> None:
        self.populate_audit_store()
        before = self.snapshot()
        result = audit_module.audit_store(self.root, as_of=date(2026, 7, 17))
        after = self.snapshot()

        self.assertEqual(before, after, "audit must never write")
        self.assertEqual(5, result["counts"]["record_files"])
        self.assertEqual(5, result["counts"]["valid_records"])
        self.assertEqual(4, result["counts"]["by_decision"]["admitted"])
        self.assertEqual(1, result["counts"]["by_decision"]["rejected"])
        self.assertEqual(4, result["counts"]["by_trust"]["high"])
        self.assertEqual(1, result["counts"]["by_trust"]["medium"])
        self.assertEqual(5, result["counts"]["by_sensitivity"]["internal"])
        self.assertEqual(
            {"immutable": 1, "fresh": 1, "expiring": 1, "stale": 1, "superseded": 1},
            result["counts"]["by_freshness"],
        )
        self.assertEqual(1, result["stale_implicated_count"])
        self.assertEqual({"secret_content": 1, "trust_cap_violation": 2}, result["refusal_counts"])
        self.assertEqual(3, result["refusal_entries"])
        self.assertEqual("current", result["index_status"])
        self.assertEqual(0, result["finding_count"])
        self.assertEqual(0, result["writes_performed"])
        self.assertEqual(
            [["ctx-2026-07-17-superseded", "ctx-2026-07-17-current-historical"]],
            result["superseded_chains"],
        )

    def test_orphaned_supersession_is_a_finding(self) -> None:
        self.write_record(
            "ctx-2026-07-17-orphan",
            staleness_policy="volatile",
            review_after="2026-07-16",
            superseded_by="ctx-2026-07-17-missing-target",
        )
        index_module.rebuild_index(self.root)
        result = audit_module.audit_store(self.root, as_of=date(2026, 7, 17))
        self.assertIn("orphaned_superseded_by", {item["code"] for item in result["findings"]})
        self.assertEqual(1, result["stale_implicated_count"])

    def test_index_drift_is_reported_without_repairing_it(self) -> None:
        self.write_record("ctx-2026-07-17-drift")
        index_module.rebuild_index(self.root)
        index_path = self.root / index_module.INDEX_RELPATH
        index_path.write_bytes(b"{}\n")
        before = index_path.read_bytes()
        result = audit_module.audit_store(self.root, as_of=date(2026, 7, 17))
        self.assertEqual("drifted", result["index_status"])
        self.assertIn("index_drift", {item["code"] for item in result["findings"]})
        self.assertEqual(before, index_path.read_bytes())

    def test_invalid_refusal_entry_never_echoes_its_value(self) -> None:
        self.write_record("ctx-2026-07-17-safe-refusal-audit")
        index_module.rebuild_index(self.root)
        marker = "CONTENT_MUST_NOT_BE_ECHOED"
        self.refusal_log.write_text(
            json.dumps(
                {
                    "refused_at": "2026-07-17",
                    "reason_code": marker,
                    "proposed_by": "TEST",
                    "batch_id": "TEST",
                    "gate_spec_version": "v1",
                }
            )
            + "\n",
            encoding="utf-8",
        )
        result = audit_module.audit_store(self.root, as_of=date(2026, 7, 17))
        rendered = json.dumps(result, sort_keys=True)
        self.assertNotIn(marker, rendered)
        self.assertEqual({}, result["refusal_counts"])
        self.assertIn("invalid_refusal_log_entry", {item["code"] for item in result["findings"]})

    def test_audit_never_emits_record_content_fields_or_values(self) -> None:
        marker = "RECORD_CONTENT_MUST_NOT_BE_RENDERED"
        self.write_record(
            "ctx-2026-07-17-content-free-audit",
            source_identity="operator-only source description",
            claim=marker,
            notes="Reviewer note " + marker,
        )
        index_module.rebuild_index(self.root)
        rendered = json.dumps(
            audit_module.audit_store(self.root, as_of=date(2026, 7, 17)), sort_keys=True
        )
        self.assertNotIn(marker, rendered)
        self.assertNotIn('"claim"', rendered)
        self.assertNotIn('"notes"', rendered)
        self.assertNotIn('"source_identity"', rendered)

    def test_cli_audit_json_is_read_only_and_deterministic_for_same_day(self) -> None:
        self.write_record("ctx-2026-07-17-cli-audit")
        index_module.rebuild_index(self.root)
        before = self.snapshot()
        outputs = []
        with mock.patch.object(cli_module, "repo_root", return_value=self.root):
            with mock.patch.object(audit_module, "date") as date_type:
                date_type.today.return_value = date(2026, 7, 17)
                for _ in range(2):
                    out = io.StringIO()
                    with contextlib.redirect_stdout(out):
                        self.assertEqual(EXIT_OK, cli_module.main(["audit", "--json"]))
                    outputs.append(out.getvalue())
        self.assertEqual(outputs[0], outputs[1])
        self.assertEqual(before, self.snapshot())

    def test_cli_audit_returns_nonzero_for_consistency_findings(self) -> None:
        self.write_record("ctx-2026-07-17-cli-finding")
        index_module.rebuild_index(self.root)
        (self.root / index_module.INDEX_RELPATH).write_bytes(b"{}\n")
        out = io.StringIO()
        with mock.patch.object(cli_module, "repo_root", return_value=self.root):
            with contextlib.redirect_stdout(out):
                self.assertEqual(EXIT_INVALID, cli_module.main(["audit", "--json"]))
        self.assertEqual("drifted", json.loads(out.getvalue())["index_status"])


class ShippedI3ArtifactsTests(unittest.TestCase):
    def test_shipped_index_matches_validated_canonical_records(self) -> None:
        index_path = ROOT / index_module.INDEX_RELPATH
        self.assertTrue(index_path.is_file())
        self.assertEqual(index_module.expected_index_bytes(ROOT), index_path.read_bytes())

    def test_shipped_audit_is_read_only_and_index_is_current(self) -> None:
        provenance = ROOT / "shared_context" / "context_provenance"
        before = {
            str(path.relative_to(provenance)): path.read_bytes()
            for path in provenance.rglob("*")
            if path.is_file()
        }
        result = audit_module.audit_store(ROOT)
        after = {
            str(path.relative_to(provenance)): path.read_bytes()
            for path in provenance.rglob("*")
            if path.is_file()
        }
        self.assertEqual(before, after)
        self.assertEqual("current", result["index_status"])
        self.assertEqual(7, result["counts"]["valid_records"])
        self.assertEqual(0, result["writes_performed"])


if __name__ == "__main__":
    unittest.main()
