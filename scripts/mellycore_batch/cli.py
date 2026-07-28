"""Command-line interface for the MellyCore OpenAI Batch API foundation.

Commands:
    build       Validate a manifest and write its deterministic JSONL input file.
    validate    Validate a manifest, or stream-validate an existing JSONL file.
    inspect     Report facts about an existing JSONL file (count, size, sha256).
    summarize   Parse downloaded result/error files into a Run Ledger-compatible summary.
    plan-live   Show what a future submission would do, without doing it.
    submit      BLOCKED while migration trigger #5 is active. See policy.py.
    status      BLOCKED while migration trigger #5 is active. See policy.py.
    list        BLOCKED while migration trigger #5 is active. See policy.py.
    download    BLOCKED while migration trigger #5 is active. See policy.py.
    cancel      BLOCKED while migration trigger #5 is active. See policy.py.

Exit codes:
    0   success (EXIT_OK)
    1   invalid input or configuration (EXIT_INVALID)
    78  a command required a live provider connection, refused because
        migration trigger #5 is blocking (EXIT_LIVE_BLOCKED)

``build``, ``validate``, ``inspect``, ``summarize``, and ``plan-live`` are the
only commands that do anything; none of them constructs a provider client or
reaches the network. ``submit``, ``status``, ``list``, ``download``, and
``cancel`` always fail with exit code 78 right now -- see
:mod:`scripts.mellycore_batch.policy`.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from .jsonl import build_jsonl, iter_validate_jsonl_file, sha256_of_file
from .manifest import load_manifest_file, validate_manifest
from .models import (
    COMPLETION_WINDOW,
    EXIT_INVALID,
    EXIT_LIVE_BLOCKED,
    EXIT_OK,
    UPLOAD_PURPOSE,
    BatchOpsError,
    InvalidInputError,
    LiveConnectionBlockedError,
)
from .policy import credential_material_present, enforce_live_connection_allowed, get_active_policy
from .results import parse_result_files
from .summary import build_ledger_summary

PROG = "py -3.9 -m scripts.mellycore_batch"


def _emit_json(payload: Any) -> None:
    print(json.dumps(payload, indent=2, sort_keys=False))


# --- build --------------------------------------------------------------------


def cmd_build(args: argparse.Namespace) -> int:
    manifest = load_manifest_file(Path(args.manifest))
    if args.overwrite:
        manifest = _with_overwrite(manifest, True)
    output_path = Path(args.output) if args.output else None
    summary = build_jsonl(manifest, output_path=output_path)

    if args.json:
        _emit_json({"command": "build", **summary.to_dict()})
        return EXIT_OK

    print("MellyCore Batch build (local only, no network)")
    print("  task_id:            {}".format(manifest.task_id))
    print("  endpoint:           {}".format(summary.endpoint))
    print("  completion_window:  {}".format(summary.completion_window))
    print("  models:             {}".format(", ".join(summary.models) or "(none)"))
    print("  request_count:      {}".format(summary.request_count))
    print("  byte_size:          {}".format(summary.byte_size))
    print("  sha256:             {}".format(summary.sha256))
    print("  path:               {}".format(summary.path))
    return EXIT_OK


def _with_overwrite(manifest, overwrite: bool):
    # BatchManifest is frozen; rebuild rather than mutate.
    from dataclasses import replace

    return replace(manifest, overwrite=overwrite)


# --- validate -----------------------------------------------------------------


def cmd_validate(args: argparse.Namespace) -> int:
    if args.manifest:
        manifest = load_manifest_file(Path(args.manifest))
        validate_manifest(manifest)
        if args.json:
            _emit_json(
                {
                    "command": "validate",
                    "target": "manifest",
                    "manifest": args.manifest,
                    "task_id": manifest.task_id,
                    "request_count": len(manifest.requests),
                    "valid": True,
                }
            )
            return EXIT_OK
        print("MellyCore Batch validate (local only, no network)")
        print("  manifest: {}".format(args.manifest))
        print("  PASS manifest is valid: {} request(s)".format(len(manifest.requests)))
        return EXIT_OK

    if args.jsonl:
        findings = list(iter_validate_jsonl_file(Path(args.jsonl)))
        if args.json:
            _emit_json(
                {
                    "command": "validate",
                    "target": "jsonl",
                    "path": args.jsonl,
                    "valid": not findings,
                    "findings": findings,
                }
            )
            return EXIT_INVALID if findings else EXIT_OK
        print("MellyCore Batch validate (local only, no network)")
        print("  jsonl: {}".format(args.jsonl))
        if not findings:
            print("  PASS no findings")
            return EXIT_OK
        for finding in findings:
            print("  line {}: {} - {}".format(finding["line"], finding["code"], finding["message"]))
        print("  FAIL {} finding(s)".format(len(findings)))
        return EXIT_INVALID

    raise InvalidInputError("validate requires either --manifest or --jsonl")


# --- inspect ------------------------------------------------------------------


def cmd_inspect(args: argparse.Namespace) -> int:
    path = Path(args.jsonl)
    findings = list(iter_validate_jsonl_file(path))
    digest = sha256_of_file(path)
    byte_size = path.stat().st_size

    payload = {
        "command": "inspect",
        "path": str(path),
        "byte_size": byte_size,
        "sha256": digest,
        "finding_count": len(findings),
        "valid": not findings,
    }
    if args.json:
        _emit_json({**payload, "findings": findings})
        return EXIT_OK

    print("MellyCore Batch inspect (local only, streaming, no network)")
    print("  path:       {}".format(path))
    print("  byte_size:  {}".format(byte_size))
    print("  sha256:     {}".format(digest))
    print("  findings:   {}".format(len(findings)))
    return EXIT_OK


# --- summarize ------------------------------------------------------------------


def cmd_summarize(args: argparse.Namespace) -> int:
    expected_ids = None
    if args.expected_custom_ids:
        expected_ids = set(_read_lines(Path(args.expected_custom_ids)))

    result_set = parse_result_files(
        output_path=Path(args.output_file) if args.output_file else None,
        error_path=Path(args.error_file) if args.error_file else None,
        expected_custom_ids=expected_ids,
    )

    request_count = (
        len(expected_ids)
        if expected_ids is not None
        else result_set.completed_count + result_set.failed_count
    )

    summary = build_ledger_summary(
        task_id=args.task_id,
        endpoint=args.endpoint,
        completion_window=args.completion_window,
        models=args.model or [],
        request_count=request_count,
        status=args.status,
        batch_id=args.batch_id,
        result_set=result_set,
    )

    payload = summary.to_dict()
    if args.json:
        _emit_json({"command": "summarize", **payload})
        return EXIT_OK

    print("MellyCore Batch summarize (local only, parses local files, no network)")
    print("  task_id:          {}".format(payload["task_id"]))
    print("  status:           {}".format(payload["status"]))
    print("  completed_count:  {}".format(payload["completed_count"]))
    print("  failed_count:     {}".format(payload["failed_count"]))
    print("  missing_count:    {}".format(payload["missing_count"]))
    print("  duplicate_count:  {}".format(payload["duplicate_count"]))
    if result_set.malformed_lines:
        print("  malformed_lines:  {}".format(len(result_set.malformed_lines)))
        for line in result_set.malformed_lines:
            print("    {}:{} {}".format(line.source, line.line_number, line.reason))
    return EXIT_OK


def _read_lines(path: Path) -> List[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


# --- plan-live ------------------------------------------------------------------


def cmd_plan_live(args: argparse.Namespace) -> int:
    manifest = load_manifest_file(Path(args.manifest))
    validate_manifest(manifest)
    policy = get_active_policy()

    jsonl_path = Path(args.jsonl) if args.jsonl else None
    file_size: Optional[int] = None
    digest: Optional[str] = None
    if jsonl_path is not None and jsonl_path.exists():
        file_size = jsonl_path.stat().st_size
        digest = sha256_of_file(jsonl_path)

    plan: Dict[str, Any] = {
        "command": "plan-live",
        "task_id": manifest.task_id,
        "endpoint": manifest.endpoint,
        "completion_window": manifest.completion_window,
        "request_count": len(manifest.requests),
        "models": list(manifest.models),
        "input_path": str(jsonl_path) if jsonl_path else None,
        "input_file_size": file_size,
        "input_file_sha256": digest,
        "expected_upload_purpose": UPLOAD_PURPOSE,
        "live_connection_policy": policy.to_dict(),
        "credentials_detected": credential_material_present(),
        "execution_allowed": policy.allowed,
    }

    if args.json:
        _emit_json(plan)
        return EXIT_OK

    print("MellyCore Batch plan-live -- PLANNING ONLY, nothing is submitted")
    print("  task_id:               {}".format(plan["task_id"]))
    print("  endpoint:              {}".format(plan["endpoint"]))
    print("  completion_window:     {}".format(plan["completion_window"]))
    print("  request_count:         {}".format(plan["request_count"]))
    print("  models:                {}".format(", ".join(plan["models"]) or "(none)"))
    print("  input_path:            {}".format(plan["input_path"]))
    print("  input_file_size:       {}".format(plan["input_file_size"]))
    print("  input_file_sha256:     {}".format(plan["input_file_sha256"]))
    print("  expected_upload_purpose: {}".format(plan["expected_upload_purpose"]))
    print("  credentials_detected:  {} (value never shown)".format(plan["credentials_detected"]))
    print("  blocking_trigger:      {}".format(policy.blocking_trigger))
    print("  execution_allowed:     {}".format(plan["execution_allowed"]))
    return EXIT_OK


# --- provider-backed commands (always blocked right now) ----------------------


#: The submit/status/list/download/cancel command bodies below call
#: ``enforce_live_connection_allowed`` as their first and only action. That
#: call always raises :class:`LiveConnectionBlockedError` while migration
#: trigger #5 is active, so nothing after it in any of these functions can
#: currently execute. The actual provider-calling logic is deliberately not
#: written yet: it belongs to the separately authorized
#: ``MELLYCORE-OPENAI-BATCH-API-LIVE-SMOKE-001`` task, after Model B
#: reconsideration, not to this foundation task.


def cmd_submit(args: argparse.Namespace) -> int:
    enforce_live_connection_allowed("submit")
    raise NotImplementedError("live submission is out of scope for this foundation task")


def cmd_status(args: argparse.Namespace) -> int:
    enforce_live_connection_allowed("status")
    raise NotImplementedError("live status polling is out of scope for this foundation task")


def cmd_list(args: argparse.Namespace) -> int:
    enforce_live_connection_allowed("list")
    raise NotImplementedError("live listing is out of scope for this foundation task")


def cmd_download(args: argparse.Namespace) -> int:
    enforce_live_connection_allowed("download")
    raise NotImplementedError("live download is out of scope for this foundation task")


def cmd_cancel(args: argparse.Namespace) -> int:
    enforce_live_connection_allowed("cancel")
    raise NotImplementedError("live cancellation is out of scope for this foundation task")


# --- parser ---------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=PROG,
        description=(
            "MellyCore local OpenAI Batch API foundation. build/validate/inspect/summarize/"
            "plan-live are local-only and never reach the network. submit/status/list/download/"
            "cancel are hard-blocked while migration trigger #5 (first live provider connection) "
            "is active, regardless of any flag or environment variable."
        ),
    )
    sub = parser.add_subparsers(dest="command")

    p_build = sub.add_parser("build", help="Validate a manifest and write its deterministic JSONL file")
    p_build.add_argument("--manifest", required=True, help="Path to a Batch manifest JSON file")
    p_build.add_argument("--output", default=None, help="Output JSONL path (default: derived from task_id)")
    p_build.add_argument("--overwrite", action="store_true", help="Allow overwriting an existing output file")
    p_build.add_argument("--json", action="store_true", help="Emit JSON")
    p_build.set_defaults(func=cmd_build)

    p_validate = sub.add_parser("validate", help="Validate a manifest or an existing JSONL file")
    p_validate.add_argument("--manifest", default=None, help="Path to a Batch manifest JSON file")
    p_validate.add_argument("--jsonl", default=None, help="Path to an existing JSONL file to stream-validate")
    p_validate.add_argument("--json", action="store_true", help="Emit JSON")
    p_validate.set_defaults(func=cmd_validate)

    p_inspect = sub.add_parser("inspect", help="Report facts about an existing JSONL file")
    p_inspect.add_argument("--jsonl", required=True, help="Path to an existing JSONL file")
    p_inspect.add_argument("--json", action="store_true", help="Emit JSON")
    p_inspect.set_defaults(func=cmd_inspect)

    p_summarize = sub.add_parser(
        "summarize", help="Parse local result/error JSONL files into a Run Ledger-compatible summary"
    )
    p_summarize.add_argument("--task-id", required=True, help="Local task identifier")
    p_summarize.add_argument("--endpoint", default="/v1/responses", help="Batch endpoint used")
    p_summarize.add_argument("--completion-window", default=COMPLETION_WINDOW, help="Completion window used")
    p_summarize.add_argument("--model", action="append", default=None, help="A model ID used (repeatable)")
    p_summarize.add_argument("--status", default="unknown", help="Local status label for this summary")
    p_summarize.add_argument("--batch-id", default=None, help="Provider batch ID, if known")
    p_summarize.add_argument("--output-file", default=None, help="Path to a downloaded output JSONL file")
    p_summarize.add_argument("--error-file", default=None, help="Path to a downloaded error JSONL file")
    p_summarize.add_argument(
        "--expected-custom-ids",
        default=None,
        help="Path to a text file of one expected custom_id per line, for missing-result detection",
    )
    p_summarize.add_argument("--json", action="store_true", help="Emit JSON")
    p_summarize.set_defaults(func=cmd_summarize)

    p_plan = sub.add_parser("plan-live", help="Show what a future submission would do, without doing it")
    p_plan.add_argument("--manifest", required=True, help="Path to a Batch manifest JSON file")
    p_plan.add_argument("--jsonl", default=None, help="Path to an already-built JSONL file, if any")
    p_plan.add_argument("--json", action="store_true", help="Emit JSON")
    p_plan.set_defaults(func=cmd_plan_live)

    for name, func, help_text in (
        ("submit", cmd_submit, "BLOCKED while migration trigger #5 is active"),
        ("status", cmd_status, "BLOCKED while migration trigger #5 is active"),
        ("list", cmd_list, "BLOCKED while migration trigger #5 is active"),
        ("download", cmd_download, "BLOCKED while migration trigger #5 is active"),
        ("cancel", cmd_cancel, "BLOCKED while migration trigger #5 is active"),
    ):
        p = sub.add_parser(name, help=help_text)
        p.add_argument("--execute", action="store_true", help="Ignored: cannot bypass migration trigger #5")
        p.add_argument("--json", action="store_true", help="Emit JSON")
        p.set_defaults(func=func)

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not getattr(args, "command", None):
        parser.print_help()
        return EXIT_INVALID

    try:
        return args.func(args)
    except LiveConnectionBlockedError as exc:
        payload = {
            "command": args.command,
            "error": LiveConnectionBlockedError.code,
            "message": str(exc),
            "execution_allowed": False,
        }
        if getattr(args, "json", False):
            _emit_json(payload)
        else:
            print("BLOCKED [{}]: {}".format(LiveConnectionBlockedError.code, exc), file=sys.stderr)
        return EXIT_LIVE_BLOCKED
    except InvalidInputError as exc:
        if getattr(args, "json", False):
            _emit_json({"command": args.command, "error": "invalid_input", "message": str(exc)})
        else:
            print("ERROR invalid input: {}".format(exc), file=sys.stderr)
        return EXIT_INVALID
    except BatchOpsError as exc:
        print("ERROR {}".format(exc), file=sys.stderr)
        return EXIT_INVALID
