"""Command-line interface for Context Gate implementation Phase I1.

Commands:
    preview          Evaluate a candidate batch with R1-R9 and write nothing.
    validate-record  Validate one draft, decided, preview, or canonical record.

Exit codes:
    0  command completed and no record/item was invalid or refused
    1  malformed command/input or invalid ContextSource record
    2  preview completed deterministically with one or more REFUSE outcomes

This phase contains no apply command, no store writer, no migration, no refusal
log writer, no index, and no audit command. Both commands are read-only by
construction and perform no network or provider calls.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, List, Mapping, Optional

from .checks import OUTCOME_ORDER, REFUSE, load_default_records, preview_batch
from .models import (
    EXIT_INVALID,
    EXIT_OK,
    EXIT_REFUSED,
    ContextGateError,
    InvalidInputError,
    validate_record_shape,
)

PROG = "py -3.9 -m scripts.context_gate"


class SafeArgumentParser(argparse.ArgumentParser):
    """Turn parser failures into the CLI's documented aggregate-safe exit 1."""

    def error(self, message: str) -> None:
        raise InvalidInputError("command arguments are invalid: {}".format(message))


def _emit_json(payload: Any) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False))


def _load_json_object(path_text: str, label: str) -> Mapping[str, Any]:
    path = Path(path_text)
    try:
        raw = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise InvalidInputError("{} file is unreadable".format(label)) from exc
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise InvalidInputError("{} file is not valid JSON".format(label)) from exc
    if not isinstance(data, Mapping):
        raise InvalidInputError("{} must be a JSON object".format(label))
    return data


def cmd_preview(args: argparse.Namespace) -> int:
    manifest = _load_json_object(args.batch, "batch manifest")
    records = load_default_records()
    report = preview_batch(manifest, existing_records=records)
    payload = report.to_dict()

    if args.json:
        _emit_json(payload)
    else:
        print("MellyCore Context Gate preview")
        print("  batch:             {}".format(report.batch_id))
        print("  validated_at:      {}".format(report.validated_at))
        print("  writes_performed:  0")
        print("")
        for item in report.items:
            if item.outcome == REFUSE:
                print(
                    "item {}: REFUSE reason_codes={}".format(
                        item.item_index, ",".join(item.reason_codes)
                    )
                )
                continue
            print(
                "item {}: {} source_id={} computed_trust={}".format(
                    item.item_index, item.outcome, item.source_id, item.computed_trust
                )
            )
            if item.warnings:
                print("  warnings: {}".format(",".join(item.warnings)))
            if item.parking_codes:
                print("  parking_codes: {}".format(",".join(item.parking_codes)))
            for question in item.parked_questions:
                print("  question: {}".format(question))
            if item.stale_implicated:
                print("  stale_implicated: {}".format(",".join(item.stale_implicated)))
            if item.draft_contradictions:
                print("  draft_contradictions:")
                print(
                    json.dumps(
                        [dict(entry) for entry in item.draft_contradictions],
                        indent=2,
                        sort_keys=True,
                        ensure_ascii=False,
                    )
                )
            if item.canonical_record_bytes is not None:
                print("  canonical_record_bytes:")
                print(item.canonical_record_bytes, end="")
        print("")
        print(
            "outcomes: {}".format(
                " ".join("{}={}".format(name, report.counts[name]) for name in OUTCOME_ORDER)
            )
        )

    return EXIT_REFUSED if report.has_refusals else EXIT_OK


def cmd_validate_record(args: argparse.Namespace) -> int:
    path = Path(args.file)
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise InvalidInputError("record file is unreadable") from exc
    try:
        data = json.loads(raw.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise InvalidInputError("record file is not valid UTF-8 JSON") from exc

    findings = validate_record_shape(data, raw_bytes=raw)
    payload = {
        "command": "validate-record",
        "valid": not findings,
        "findings": [finding.to_dict() for finding in findings],
        "writes_performed": 0,
    }
    if args.json:
        _emit_json(payload)
    else:
        print("MellyCore ContextSource validation")
        print("  writes_performed: 0")
        if not findings:
            print("PASS record is valid")
        else:
            for finding in findings:
                where = " [{}]".format(finding.field) if finding.field else ""
                print("ERROR {}{}: {}".format(finding.code, where, finding.message))
            print("FAIL {} finding(s)".format(len(findings)))
    return EXIT_INVALID if findings else EXIT_OK


def build_parser() -> argparse.ArgumentParser:
    parser = SafeArgumentParser(
        prog=PROG,
        description=(
            "MellyCore Context Gate Phase I1. Read-only ContextSource validation and "
            "R1-R9 batch preview. No apply mode or repository write path exists."
        ),
    )
    sub = parser.add_subparsers(dest="command", parser_class=SafeArgumentParser)

    p_preview = sub.add_parser("preview", help="Evaluate a candidate batch; write nothing")
    p_preview.add_argument("--batch", required=True, help="Path to a candidate batch manifest JSON file")
    p_preview.add_argument("--json", action="store_true", help="Emit deterministic JSON")
    p_preview.set_defaults(func=cmd_preview)

    p_validate = sub.add_parser("validate-record", help="Validate one ContextSource record")
    p_validate.add_argument("--file", required=True, help="Path to a ContextSource JSON file")
    p_validate.add_argument("--json", action="store_true", help="Emit deterministic JSON")
    p_validate.set_defaults(func=cmd_validate_record)
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    try:
        args = parser.parse_args(argv)
        if not getattr(args, "command", None):
            parser.print_help()
            return EXIT_INVALID
        return args.func(args)
    except InvalidInputError as exc:
        print("ERROR invalid input: {}".format(exc), file=sys.stderr)
        return EXIT_INVALID
    except ContextGateError as exc:
        print("ERROR {}".format(exc), file=sys.stderr)
        return EXIT_INVALID
