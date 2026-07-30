"""Command-line interface for the MellyCore OpenAI Batch API foundation.

Commands:
    build       Validate a manifest and write its deterministic JSONL input file.
    validate    Validate a manifest, or stream-validate an existing JSONL file.
    inspect     Report facts about an existing JSONL file (count, size, sha256).
    summarize   Parse downloaded result/error files into a Run Ledger-compatible summary.
    plan-live   Show what a future submission would do, without doing it.
    activation-preflight
                Stage B local activation preflight (pricing evidence, exact-model/
                envelope/cost checks, optional authorization-artifact validation).
                Always reports execution_authorized=false. See activation.py.
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

``build``, ``validate``, ``inspect``, ``summarize``, ``plan-live``, and
``activation-preflight`` are the only commands that do anything; none of them
constructs a provider client, imports the OpenAI SDK, or reaches the
network. ``submit``, ``status``, ``list``, ``download``, and ``cancel``
always fail with exit code 78 right now -- see
:mod:`scripts.mellycore_batch.policy`.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from .activation import (
    DEFAULT_PRICING_MANIFEST_PATH,
    build_preflight_record,
    enforce_cost_cap,
    enforce_request_envelope,
    estimate_cost,
    load_authorization_artifact,
    load_pricing_manifest,
    parse_canonical_utc_timestamp,
    validate_authorization_artifact,
    validate_pricing_evidence,
)
from .jsonl import (
    build_jsonl,
    iter_validate_jsonl_file,
    render_jsonl_bytes,
    sha256_of_file,
)
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
from .policy import (
    credential_material_present,
    enforce_live_connection_allowed,
    get_active_policy,
)
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
            print(
                "  line {}: {} - {}".format(
                    finding["line"], finding["code"], finding["message"]
                )
            )
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
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


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
    print(
        "  credentials_detected:  {} (value never shown)".format(
            plan["credentials_detected"]
        )
    )
    print("  blocking_trigger:      {}".format(policy.blocking_trigger))
    print("  execution_allowed:     {}".format(plan["execution_allowed"]))
    return EXIT_OK


# --- activation-preflight (Stage B, local only, no network) -------------------


def _parse_now_arg(raw: Optional[str]) -> datetime:
    if not raw:
        return datetime.now(timezone.utc)
    try:
        return parse_canonical_utc_timestamp(raw, field_name="--now")
    except BatchOpsError as exc:
        raise InvalidInputError(
            "--now must use canonical UTC format YYYY-MM-DDTHH:MM:SSZ"
        ) from exc


def cmd_activation_preflight(args: argparse.Namespace) -> int:
    """Stage B activation preflight: local validation only, never a live connection.

    Imports no provider client and no OpenAI SDK. Loads and cross-checks the
    pricing-evidence manifest, enforces the exact-model/request/input/output
    envelope, computes a Decimal cost estimate against the hard cap, and (if
    an authorization artifact path is given) validates -- but never consumes
    -- it. ``execution_authorized`` and ``migration_trigger_5_crossed`` are
    always ``False`` in the emitted record; this command cannot report
    otherwise regardless of any flag or file it is given.
    """
    manifest = load_manifest_file(Path(args.manifest))
    validate_manifest(manifest)

    payload_bytes = render_jsonl_bytes(manifest.requests)
    input_byte_count = len(payload_bytes)
    input_jsonl_sha256 = hashlib.sha256(payload_bytes).hexdigest()

    now = _parse_now_arg(args.now)

    pricing_manifest_path = (
        Path(args.pricing_manifest)
        if args.pricing_manifest
        else DEFAULT_PRICING_MANIFEST_PATH
    )
    pricing_manifest = load_pricing_manifest(pricing_manifest_path)
    validate_pricing_evidence(pricing_manifest, now)

    envelope = enforce_request_envelope(manifest.requests, input_byte_count)
    cost_estimate = estimate_cost(
        envelope.input_byte_count, envelope.total_max_output_tokens
    )
    enforce_cost_cap(cost_estimate)

    canonical_commit_sha = args.canonical_commit_sha or "unknown"
    activation_commit_sha = args.activation_commit_sha or "unknown"

    authorization_id: Optional[str] = None
    if args.authorization:
        if not args.canonical_commit_sha or not args.activation_commit_sha:
            raise InvalidInputError(
                "--authorization requires both --canonical-commit-sha and --activation-commit-sha"
            )
        artifact = load_authorization_artifact(Path(args.authorization))
        validate_authorization_artifact(
            artifact,
            now=now,
            expected_canonical_base_sha=canonical_commit_sha,
            expected_activation_commit_sha=activation_commit_sha,
            expected_task_id=manifest.task_id,
        )
        # Preflight validates only -- it never calls
        # scripts.mellycore_batch.activation.consume_authorization. Only a
        # hypothetical, separately authorized Stage C execution attempt would
        # ever consume an authorization artifact, and that code path does not
        # exist in this package.
        authorization_id = artifact.authorization_id

    record = build_preflight_record(
        task_id=manifest.task_id,
        authorization_id=authorization_id,
        canonical_commit_sha=canonical_commit_sha,
        activation_commit_sha=activation_commit_sha,
        endpoint=manifest.endpoint,
        completion_window=manifest.completion_window,
        envelope=envelope,
        pricing_manifest=pricing_manifest,
        cost_estimate=cost_estimate,
        input_jsonl_sha256=input_jsonl_sha256,
        credential_present=credential_material_present(),
    )
    payload = record.to_dict()

    if args.json:
        _emit_json({"command": "activation-preflight", **payload})
        return EXIT_OK

    print(
        "MellyCore Batch activation-preflight -- Stage B PLANNING ONLY, no network, nothing submitted"
    )
    print("  task_id:                          {}".format(payload["task_id"]))
    print("  authorization_id:                 {}".format(payload["authorization_id"]))
    print(
        "  provider / endpoint / model:       {} / {} / {}".format(
            payload["provider"], payload["endpoint"], payload["model"]
        )
    )
    print("  request_count:                    {}".format(payload["request_count"]))
    print(
        "  input_jsonl_size / sha256:         {} / {}".format(
            payload["input_jsonl_size"], payload["input_jsonl_sha256"]
        )
    )
    print(
        "  maximum_total_output_tokens:       {}".format(
            payload["maximum_total_output_tokens"]
        )
    )
    print(
        "  pricing_verified_at / valid_until: {} / {}".format(
            payload["pricing_verified_at"], payload["pricing_valid_until"]
        )
    )
    print(
        "  estimated_maximum_cost / cap:      {} / {}".format(
            payload["estimated_maximum_cost"], payload["authorized_hard_cost_cap"]
        )
    )
    print(
        "  credential_present:                {} (value never shown)".format(
            payload["credential_present"]
        )
    )
    print(
        "  execution_authorized:              {}".format(
            payload["execution_authorized"]
        )
    )
    print(
        "  migration_trigger_5_crossed:       {}".format(
            payload["migration_trigger_5_crossed"]
        )
    )
    return EXIT_OK


# --- provider-backed commands (always blocked right now) ----------------------


#: The submit/status/list/download/cancel command bodies below call
#: ``enforce_live_connection_allowed`` as their first and only action. That
#: call always raises :class:`LiveConnectionBlockedError` while migration
#: trigger #5 is active, so nothing after it in any of these functions can
#: currently execute. The actual provider-calling logic is deliberately not
#: written yet: it belongs to the separately authorized
#: ``MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`` task (Stage C),
#: after its own separate authorization -- Stage B (this module's
#: ``activation-preflight`` command and :mod:`scripts.mellycore_batch.activation`)
#: only plans and validates; it does not authorize or implement Stage C.


def cmd_submit(args: argparse.Namespace) -> int:
    enforce_live_connection_allowed("submit")
    raise NotImplementedError(
        "live submission is out of scope for this foundation task"
    )


def cmd_status(args: argparse.Namespace) -> int:
    enforce_live_connection_allowed("status")
    raise NotImplementedError(
        "live status polling is out of scope for this foundation task"
    )


def cmd_list(args: argparse.Namespace) -> int:
    enforce_live_connection_allowed("list")
    raise NotImplementedError("live listing is out of scope for this foundation task")


def cmd_download(args: argparse.Namespace) -> int:
    enforce_live_connection_allowed("download")
    raise NotImplementedError("live download is out of scope for this foundation task")


def cmd_cancel(args: argparse.Namespace) -> int:
    enforce_live_connection_allowed("cancel")
    raise NotImplementedError(
        "live cancellation is out of scope for this foundation task"
    )


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

    p_build = sub.add_parser(
        "build", help="Validate a manifest and write its deterministic JSONL file"
    )
    p_build.add_argument(
        "--manifest", required=True, help="Path to a Batch manifest JSON file"
    )
    p_build.add_argument(
        "--output",
        default=None,
        help="Output JSONL path (default: derived from task_id)",
    )
    p_build.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow overwriting an existing output file",
    )
    p_build.add_argument("--json", action="store_true", help="Emit JSON")
    p_build.set_defaults(func=cmd_build)

    p_validate = sub.add_parser(
        "validate", help="Validate a manifest or an existing JSONL file"
    )
    p_validate.add_argument(
        "--manifest", default=None, help="Path to a Batch manifest JSON file"
    )
    p_validate.add_argument(
        "--jsonl",
        default=None,
        help="Path to an existing JSONL file to stream-validate",
    )
    p_validate.add_argument("--json", action="store_true", help="Emit JSON")
    p_validate.set_defaults(func=cmd_validate)

    p_inspect = sub.add_parser(
        "inspect", help="Report facts about an existing JSONL file"
    )
    p_inspect.add_argument(
        "--jsonl", required=True, help="Path to an existing JSONL file"
    )
    p_inspect.add_argument("--json", action="store_true", help="Emit JSON")
    p_inspect.set_defaults(func=cmd_inspect)

    p_summarize = sub.add_parser(
        "summarize",
        help="Parse local result/error JSONL files into a Run Ledger-compatible summary",
    )
    p_summarize.add_argument("--task-id", required=True, help="Local task identifier")
    p_summarize.add_argument(
        "--endpoint", default="/v1/responses", help="Batch endpoint used"
    )
    p_summarize.add_argument(
        "--completion-window", default=COMPLETION_WINDOW, help="Completion window used"
    )
    p_summarize.add_argument(
        "--model", action="append", default=None, help="A model ID used (repeatable)"
    )
    p_summarize.add_argument(
        "--status", default="unknown", help="Local status label for this summary"
    )
    p_summarize.add_argument(
        "--batch-id", default=None, help="Provider batch ID, if known"
    )
    p_summarize.add_argument(
        "--output-file", default=None, help="Path to a downloaded output JSONL file"
    )
    p_summarize.add_argument(
        "--error-file", default=None, help="Path to a downloaded error JSONL file"
    )
    p_summarize.add_argument(
        "--expected-custom-ids",
        default=None,
        help="Path to a text file of one expected custom_id per line, for missing-result detection",
    )
    p_summarize.add_argument("--json", action="store_true", help="Emit JSON")
    p_summarize.set_defaults(func=cmd_summarize)

    p_plan = sub.add_parser(
        "plan-live", help="Show what a future submission would do, without doing it"
    )
    p_plan.add_argument(
        "--manifest", required=True, help="Path to a Batch manifest JSON file"
    )
    p_plan.add_argument(
        "--jsonl", default=None, help="Path to an already-built JSONL file, if any"
    )
    p_plan.add_argument("--json", action="store_true", help="Emit JSON")
    p_plan.set_defaults(func=cmd_plan_live)

    p_preflight = sub.add_parser(
        "activation-preflight",
        help=(
            "Stage B local activation preflight: pricing evidence, exact-model/envelope/cost checks, "
            "optional authorization-artifact validation. Local only, no network, never authorizes execution."
        ),
    )
    p_preflight.add_argument(
        "--manifest", required=True, help="Path to a Batch manifest JSON file"
    )
    p_preflight.add_argument(
        "--pricing-manifest",
        default=None,
        help="Path to the pricing-evidence manifest (default: the package's openai_batch_pricing.json)",
    )
    p_preflight.add_argument(
        "--authorization",
        default=None,
        help="Path to a one-time authorization-artifact JSON file to validate (never consumed by this command)",
    )
    p_preflight.add_argument(
        "--canonical-commit-sha",
        default=None,
        help="Expected canonical base commit SHA an authorization artifact must bind to",
    )
    p_preflight.add_argument(
        "--activation-commit-sha",
        default=None,
        help="Expected activation commit SHA an authorization artifact must bind to",
    )
    p_preflight.add_argument(
        "--now",
        default=None,
        help="ISO-8601 timestamp to evaluate freshness/expiry against (default: current UTC time)",
    )
    p_preflight.add_argument("--json", action="store_true", help="Emit JSON")
    p_preflight.set_defaults(func=cmd_activation_preflight)

    for name, func, help_text in (
        ("submit", cmd_submit, "BLOCKED while migration trigger #5 is active"),
        ("status", cmd_status, "BLOCKED while migration trigger #5 is active"),
        ("list", cmd_list, "BLOCKED while migration trigger #5 is active"),
        ("download", cmd_download, "BLOCKED while migration trigger #5 is active"),
        ("cancel", cmd_cancel, "BLOCKED while migration trigger #5 is active"),
    ):
        p = sub.add_parser(name, help=help_text)
        p.add_argument(
            "--execute",
            action="store_true",
            help="Ignored: cannot bypass migration trigger #5",
        )
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
            print(
                "BLOCKED [{}]: {}".format(LiveConnectionBlockedError.code, exc),
                file=sys.stderr,
            )
        return EXIT_LIVE_BLOCKED
    except InvalidInputError as exc:
        if getattr(args, "json", False):
            _emit_json(
                {"command": args.command, "error": "invalid_input", "message": str(exc)}
            )
        else:
            print("ERROR invalid input: {}".format(exc), file=sys.stderr)
        return EXIT_INVALID
    except BatchOpsError as exc:
        print("ERROR {}".format(exc), file=sys.stderr)
        return EXIT_INVALID
