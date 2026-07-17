"""Tests for the guarded Context Gate write path (scripts/context_gate/store.py).

Every test uses a temporary directory as ``root`` and mocks git identity via
``unittest.mock.patch.object`` on the module-level ``current_head`` /
``is_clean_working_tree`` functions, exactly like ``test_loop_ops_persist.py``
mocks ``persist.py``'s git helpers. No test invokes a real git process or
touches this repository's real ``shared_context/context_provenance*``
directories.
"""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from context_gate_fixtures import decided_candidate, preview_record
from scripts.context_gate import store as store_module
from scripts.context_gate.models import deterministic_json_bytes

FAKE_HEAD = "a" * 40
OTHER_HEAD = "b" * 40


class StoreTestCase(unittest.TestCase):
    """Base providing an isolated root and mocked git identity."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

        self._head_patch = mock.patch.object(store_module, "current_head", return_value=FAKE_HEAD)
        self._clean_patch = mock.patch.object(store_module, "is_clean_working_tree", return_value=True)
        self._head_patch.start()
        self._clean_patch.start()
        self.addCleanup(self._head_patch.stop)
        self.addCleanup(self._clean_patch.stop)

    def write_preview(self, data, name=None):
        name = name or "{}.json".format(data["source_id"])
        path = self.root / store_module.PREVIEW_DIRNAME / name
        path.parent.mkdir(parents=True, exist_ok=True)
        readme = path.parent / "README.md"
        if not readme.exists():
            readme.write_text("# Preview store\n", encoding="utf-8")
        path.write_bytes(deterministic_json_bytes(data))
        return path

    def batch(self, items, batch_id="test-batch"):
        return {"batch_id": batch_id, "items": items}

    def apply(self, *, batch=None, migrate_preview=False, approval="operator-1", expected_head=FAKE_HEAD):
        return store_module.apply(
            root=self.root,
            operator_approval_id=approval,
            expected_head=expected_head,
            batch_manifest=batch,
            migrate_preview=migrate_preview,
        )

    def records_dir(self) -> Path:
        return self.root / store_module.RECORDS_DIRNAME

    def canonical_files(self):
        d = self.records_dir()
        return sorted(p.name for p in d.glob("*.json")) if d.exists() else []


# --- apply gating -------------------------------------------------------------


class ApplyGatingTests(StoreTestCase):
    def test_missing_approval_id_refuses_and_writes_nothing(self) -> None:
        with self.assertRaises(store_module.ApplyRefused) as ctx:
            self.apply(migrate_preview=True, approval="")
        self.assertEqual("MISSING_APPROVAL", ctx.exception.code)
        self.assertFalse((self.root / store_module.CANONICAL_DIRNAME).exists())

    def test_missing_expected_head_refuses(self) -> None:
        with self.assertRaises(store_module.ApplyRefused) as ctx:
            self.apply(migrate_preview=True, expected_head="")
        self.assertEqual("MISSING_EXPECTED_HEAD", ctx.exception.code)

    def test_expected_head_mismatch_refuses_and_writes_nothing(self) -> None:
        with self.assertRaises(store_module.ApplyRefused) as ctx:
            self.apply(migrate_preview=True, expected_head=OTHER_HEAD)
        self.assertEqual("HEAD_MISMATCH", ctx.exception.code)
        self.assertFalse((self.root / store_module.CANONICAL_DIRNAME).exists())

    def test_dirty_working_tree_refuses_and_writes_nothing(self) -> None:
        with mock.patch.object(store_module, "is_clean_working_tree", return_value=False):
            with self.assertRaises(store_module.ApplyRefused) as ctx:
                self.apply(migrate_preview=True)
        self.assertEqual("DIRTY_WORKING_TREE", ctx.exception.code)
        self.assertFalse((self.root / store_module.CANONICAL_DIRNAME).exists())

    def test_neither_batch_nor_migrate_is_invalid_input(self) -> None:
        from scripts.context_gate.models import InvalidInputError

        with self.assertRaises(InvalidInputError):
            self.apply()


# --- write-once record store ---------------------------------------------------


class WriteOnceTests(StoreTestCase):
    def test_invalid_source_id_is_refused(self) -> None:
        with self.assertRaises(store_module.ApplyRefused) as ctx:
            store_module.resolve_record_path("../etc/passwd", self.root)
        self.assertEqual("INVALID_SOURCE_ID", ctx.exception.code)

    def test_check_existing_record_absent(self) -> None:
        path = self.records_dir() / "ctx-2026-07-17-example.json"
        self.assertEqual("absent", store_module.check_existing_record(path, b"{}"))

    def test_check_existing_record_identical_is_noop(self) -> None:
        path = self.records_dir()
        path.mkdir(parents=True)
        target = path / "ctx-2026-07-17-example.json"
        target.write_bytes(b'{"a": 1}\n')
        self.assertEqual("identical", store_module.check_existing_record(target, b'{"a": 1}\n'))

    def test_check_existing_record_conflict_is_refused(self) -> None:
        path = self.records_dir()
        path.mkdir(parents=True)
        target = path / "ctx-2026-07-17-example.json"
        target.write_bytes(b'{"a": 1}\n')
        with self.assertRaises(store_module.ApplyRefused) as ctx:
            store_module.check_existing_record(target, b'{"a": 2}\n')
        self.assertEqual("RECORD_CONFLICT", ctx.exception.code)
        # The conflicting write must never have touched the existing file.
        self.assertEqual(b'{"a": 1}\n', target.read_bytes())

    def test_case_collision_is_refused(self) -> None:
        records_dir = self.records_dir()
        (records_dir).mkdir(parents=True)
        (records_dir / "Ctx-2026-07-17-Example.json").write_bytes(b"{}")
        with self.assertRaises(store_module.ApplyRefused) as ctx:
            store_module._check_case_collision(records_dir, "ctx-2026-07-17-example.json")
        self.assertEqual("CASE_COLLISION", ctx.exception.code)

    def test_symlinked_canonical_directory_is_refused(self) -> None:
        real_target = self.root / "elsewhere"
        real_target.mkdir(parents=True, exist_ok=True)
        symlink_path = self.root / "shared_context" / "context_provenance"
        symlink_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            symlink_path.symlink_to(real_target, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("symlink creation not permitted in this environment")
        # A path deeper than the symlinked ancestor, walking up to root --
        # exactly how the real call sites invoke this (record_path.parent, root).
        deep_path = symlink_path / "records" / "ctx-2026-07-17-example.json"
        with self.assertRaises(store_module.ApplyRefused) as ctx:
            store_module._check_no_symlink_ancestors(deep_path.parent, self.root)
        self.assertEqual("SYMLINK_IN_PATH", ctx.exception.code)


# --- refusal log: structural whitelist and append-only safety ------------------


class RefusalLogTests(StoreTestCase):
    def test_entry_rejects_unlisted_keys_at_construction(self) -> None:
        with self.assertRaises(TypeError):
            store_module.RefusalLogEntry(
                refused_at="2026-07-17",
                reason_code="trust_cap_violation",
                proposed_by="test",
                batch_id="test-batch",
                gate_spec_version="v1.0",
                source_identity="this must never be constructible",
            )

    def test_append_only_and_json_line_shape(self) -> None:
        entry = store_module.RefusalLogEntry(
            refused_at="2026-07-17",
            reason_code="trust_cap_violation",
            proposed_by="test-proposer",
            batch_id="test-batch",
            gate_spec_version="v1.0",
        )
        store_module.append_refusal_log(entry, self.root)
        lines = store_module.read_refusal_log(self.root)
        self.assertEqual(1, len(lines))
        self.assertEqual(set(entry.to_dict()), set(lines[0]))
        self.assertEqual(entry.to_dict(), lines[0])

    def test_second_append_preserves_first_line_byte_for_byte(self) -> None:
        path = self.root / store_module.REFUSAL_LOG_RELPATH
        first = store_module.RefusalLogEntry("2026-07-17", "trust_cap_violation", "a", "b1", "v1.0")
        store_module.append_refusal_log(first, self.root)
        raw_after_first = path.read_bytes()

        second = store_module.RefusalLogEntry("2026-07-18", "secret_content", "c", "b2", "v1.0")
        store_module.append_refusal_log(second, self.root)
        raw_after_second = path.read_bytes()

        self.assertTrue(raw_after_second.startswith(raw_after_first))
        lines = store_module.read_refusal_log(self.root)
        self.assertEqual(2, len(lines))
        self.assertEqual("trust_cap_violation", lines[0]["reason_code"])
        self.assertEqual("secret_content", lines[1]["reason_code"])


# --- apply_batch: writing new decided records -----------------------------------


class ApplyBatchTests(StoreTestCase):
    def test_admitted_item_is_written(self) -> None:
        item = decided_candidate(source_id="ctx-2026-07-17-batch-one")
        result = self.apply(batch=self.batch([item]))
        self.assertEqual(1, result["writes_performed"])
        self.assertEqual(["written"], [i["status"] for i in result["batch"]["items"]])
        self.assertIn("ctx-2026-07-17-batch-one.json", self.canonical_files())

    def test_identical_reapply_is_a_noop_not_a_second_write(self) -> None:
        item = decided_candidate(source_id="ctx-2026-07-17-batch-two")
        self.apply(batch=self.batch([item]))
        before = (self.records_dir() / "ctx-2026-07-17-batch-two.json").read_bytes()

        result = self.apply(batch=self.batch([item]))
        after = (self.records_dir() / "ctx-2026-07-17-batch-two.json").read_bytes()
        self.assertEqual(before, after)
        self.assertEqual(["identical"], [i["status"] for i in result["batch"]["items"]])
        self.assertEqual(0, result["writes_performed"])

    def test_missing_human_decision_is_skipped_not_written(self) -> None:
        item = decided_candidate(source_id="ctx-2026-07-17-no-decision", decision=None, reviewed_by=None)
        result = self.apply(batch=self.batch([item]))
        self.assertEqual(["skipped_no_decision"], [i["status"] for i in result["batch"]["items"]])
        self.assertEqual(0, result["writes_performed"])
        self.assertEqual([], self.canonical_files())

    def test_r1_violation_is_refused_even_when_flagged_as_previously_previewed(self) -> None:
        item = decided_candidate(
            source_id="ctx-2026-07-17-secret-item",
            sensitivity_level="secret",
            allowed_use="must_not_be_ingested",
            previously_previewed="ACCEPT",
        )
        result = self.apply(batch=self.batch([item]))
        applied = result["batch"]["items"][0]
        self.assertEqual("refused", applied["status"])
        self.assertEqual(["secret_content"], applied["reason_codes"])
        self.assertEqual([], self.canonical_files())
        logged = store_module.read_refusal_log(self.root)
        self.assertEqual(1, len(logged))
        self.assertEqual("secret_content", logged[0]["reason_code"])
        # Aggregate-safe: the refusal log never carries the claim or identity.
        self.assertNotIn("claim", logged[0])
        self.assertNotIn("source_identity", logged[0])

    def test_refused_item_does_not_block_the_rest_of_the_batch(self) -> None:
        refused_item = decided_candidate(
            source_id="ctx-2026-07-17-secret-item",
            sensitivity_level="secret",
            allowed_use="must_not_be_ingested",
        )
        good_item = decided_candidate(source_id="ctx-2026-07-17-good-item")
        result = self.apply(batch=self.batch([refused_item, good_item]))
        statuses = {i["source_id"]: i["status"] for i in result["batch"]["items"]}
        self.assertEqual("refused", statuses["ctx-2026-07-17-secret-item"])
        self.assertEqual("written", statuses["ctx-2026-07-17-good-item"])

    def test_write_gating_checked_once_covers_batch_too(self) -> None:
        item = decided_candidate(source_id="ctx-2026-07-17-gated")
        with self.assertRaises(store_module.ApplyRefused) as ctx:
            self.apply(batch=self.batch([item]), approval="")
        self.assertEqual("MISSING_APPROVAL", ctx.exception.code)
        self.assertEqual([], self.canonical_files())


# --- migration of the preview store ---------------------------------------------


class MigrationTests(StoreTestCase):
    def _six_preview_records(self):
        return [
            preview_record(source_id=source_id, claim="Claim number {}.".format(i))
            for i, source_id in enumerate(sorted(store_module.EXPECTED_PREVIEW_SOURCE_IDS))
        ]

    def test_no_preview_records_is_refused(self) -> None:
        with self.assertRaises(store_module.ApplyRefused) as ctx:
            self.apply(migrate_preview=True)
        self.assertEqual("NO_PREVIEW_RECORDS", ctx.exception.code)

    def test_migration_requires_exact_known_six_record_set(self) -> None:
        records = self._six_preview_records()
        for item in records[:-1]:
            self.write_preview(item)
        with self.assertRaises(store_module.MigrationAborted) as ctx:
            self.apply(migrate_preview=True)
        self.assertEqual("MIGRATION_RECORD_SET_MISMATCH", ctx.exception.code)
        self.assertEqual([], self.canonical_files())

    def test_successful_migration_writes_canonical_records_tombstones_preview_and_backfills_c7(self) -> None:
        for item in self._six_preview_records():
            self.write_preview(item)

        result = self.apply(migrate_preview=True)
        migration = result["migration"]
        self.assertEqual(6, migration["records_migrated"])
        self.assertTrue(migration["refusal_log_backfilled"])
        self.assertEqual(6, len(self.canonical_files()))

        # Preview store is tombstoned: original files gone, README replaced.
        preview_dir = self.root / store_module.PREVIEW_DIRNAME
        self.assertEqual([], sorted(preview_dir.glob("ctx-*.json")))
        readme_text = (preview_dir / "README.md").read_text(encoding="utf-8")
        self.assertIn("retired", readme_text.lower())

        # Canonical envelope is correct; ContextSource + gate_audit unchanged.
        one_name = sorted(store_module.EXPECTED_PREVIEW_SOURCE_IDS)[0] + ".json"
        one = json.loads((self.records_dir() / one_name).read_text(encoding="utf-8"))
        self.assertEqual("canonical", one["envelope"]["store"])
        self.assertIsNotNone(one["envelope"]["migrated_from"])
        self.assertIsNotNone(one["envelope"]["migrated_at"])
        self.assertNotIn("preview", one)
        self.assertNotIn("record_status", one)
        self.assertEqual("preview_hand_exercised", one["gate_audit"]["mode"])

        # MIGRATION_001.md and canonical README.md exist.
        self.assertTrue((self.root / store_module.MIGRATION_REPORT_RELPATH).exists())
        self.assertTrue((self.root / store_module.CANONICAL_README_RELPATH).exists())

        # C7 is backfilled as the first refusal-log line.
        logged = store_module.read_refusal_log(self.root)
        self.assertEqual(1, len(logged))
        self.assertEqual(store_module.C7_BACKFILL, logged[0])

    def test_second_migration_is_refused_not_repeated(self) -> None:
        for item in self._six_preview_records():
            self.write_preview(item)
        self.apply(migrate_preview=True)

        with self.assertRaises(store_module.ApplyRefused) as ctx:
            self.apply(migrate_preview=True)
        self.assertEqual("ALREADY_MIGRATED", ctx.exception.code)
        # No duplicate refusal-log backfill or record churn from the second attempt.
        self.assertEqual(1, len(store_module.read_refusal_log(self.root)))
        self.assertEqual(6, len(self.canonical_files()))

    def test_undecided_draft_aborts_migration_and_writes_nothing(self) -> None:
        records = self._six_preview_records()
        records[0]["decision"] = None
        records[0]["reviewed_by"] = None
        for item in records:
            self.write_preview(item)

        with self.assertRaises(store_module.MigrationAborted) as ctx:
            self.apply(migrate_preview=True)
        self.assertEqual("MIGRATION_NOT_ADMITTED", ctx.exception.code)
        self.assertEqual([], self.canonical_files())
        self.assertEqual(6, len(sorted((self.root / store_module.PREVIEW_DIRNAME).glob("ctx-*.json"))))

    def test_rejected_preview_record_is_not_migrated_as_one_of_the_six_admissions(self) -> None:
        records = self._six_preview_records()
        records[0]["decision"] = "rejected"
        for item in records:
            self.write_preview(item)
        with self.assertRaises(store_module.MigrationAborted) as ctx:
            self.apply(migrate_preview=True)
        self.assertEqual("MIGRATION_NOT_ADMITTED", ctx.exception.code)
        self.assertEqual([], self.canonical_files())

    def test_preexisting_canonical_record_is_never_overwritten_by_migration(self) -> None:
        records = self._six_preview_records()
        for item in records:
            self.write_preview(item)
        self.records_dir().mkdir(parents=True)
        conflict = self.records_dir() / (sorted(store_module.EXPECTED_PREVIEW_SOURCE_IDS)[0] + ".json")
        conflict.write_bytes(b"pre-existing bytes\n")
        with self.assertRaises(store_module.MigrationAborted) as ctx:
            self.apply(migrate_preview=True)
        self.assertEqual("MIGRATION_PARTIAL_STATE", ctx.exception.code)
        self.assertEqual(b"pre-existing bytes\n", conflict.read_bytes())

    def test_record_failing_gate_recheck_aborts_migration_loudly(self) -> None:
        records = self._six_preview_records()
        records[0]["sensitivity_level"] = "secret"
        records[0]["allowed_use"] = "must_not_be_ingested"
        for item in records:
            self.write_preview(item)

        with self.assertRaises(store_module.MigrationAborted) as ctx:
            self.apply(migrate_preview=True)
        self.assertEqual("MIGRATION_RECHECK_FAILED", ctx.exception.code)
        self.assertEqual([], self.canonical_files())
        self.assertEqual(6, len(sorted((self.root / store_module.PREVIEW_DIRNAME).glob("ctx-*.json"))))

    def test_tampered_field_identity_check_is_caught(self) -> None:
        preview_data = preview_record(source_id="ctx-2026-07-17-tamper-check")
        tampered_canonical = dict(preview_data)
        tampered_canonical["claim"] = "A different claim than the preview record made."
        with self.assertRaises(store_module.MigrationAborted) as ctx:
            store_module._verify_field_identity(preview_data, tampered_canonical, "ctx-2026-07-17-tamper-check")
        self.assertEqual("MIGRATION_FIELD_MISMATCH", ctx.exception.code)

    def test_field_identity_check_passes_for_a_genuine_relocation(self) -> None:
        preview_data = preview_record(source_id="ctx-2026-07-17-clean-relocation")
        relocated = {k: v for k, v in preview_data.items() if k not in ("preview", "record_status")}
        relocated["envelope"] = {"store": "canonical", "migrated_from": "x", "migrated_at": "2026-07-17"}
        # Must not raise.
        store_module._verify_field_identity(preview_data, relocated, "ctx-2026-07-17-clean-relocation")

    def test_partial_write_failure_leaves_preview_store_untouched(self) -> None:
        for item in self._six_preview_records():
            self.write_preview(item)

        call_count = {"n": 0}
        real_replace = store_module.os.replace

        def flaky_replace(src, dst):
            call_count["n"] += 1
            if call_count["n"] == 3:
                raise OSError("simulated disk failure partway through migration")
            return real_replace(src, dst)

        with mock.patch.object(store_module.os, "replace", side_effect=flaky_replace):
            with self.assertRaises(OSError):
                self.apply(migrate_preview=True)

        # Nothing was left half-migrated: no canonical files, preview intact.
        self.assertEqual([], self.canonical_files())
        self.assertEqual(6, len(sorted((self.root / store_module.PREVIEW_DIRNAME).glob("ctx-*.json"))))
        self.assertFalse((self.root / store_module.MIGRATION_REPORT_RELPATH).exists())

    def test_combined_migration_and_batch_in_one_apply(self) -> None:
        for item in self._six_preview_records():
            self.write_preview(item)
        new_item = decided_candidate(source_id="ctx-2026-07-17-seventh", decision="rejected")

        result = self.apply(migrate_preview=True, batch=self.batch([new_item]))
        self.assertEqual(6, result["migration"]["records_migrated"])
        self.assertEqual(1, result["batch"]["writes_performed"])
        self.assertEqual(7, len(self.canonical_files()))


if __name__ == "__main__":
    unittest.main()
