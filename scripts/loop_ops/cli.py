"""Command-line interface for MellyCore loop operations.

Commands:
    validate        Validate the loop registry against Phase 1 policy.
    audit           Report each loop's real capability tier.
    guard           Run the deterministic circuit breaker over a run ledger.
    estimate-cost   Estimate token scenarios. Always labelled as an estimate.
    worktree-audit  Read-only git worktree report.
    redact-check    Report secret-shaped strings without printing any value.

Exit codes:
    0  success / CONTINUE
    1  invalid input or configuration / BLOCK_INVALID_STATE
    2  ESCALATE_HUMAN or PAUSE_BUDGET (guard only)

Every command is read-only. Nothing here writes to the repository, calls a
provider, or reaches the network.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Dict, List, Optional

from .cost import estimate_loop
from .guard import evaluate_or_block
from .models import (
    EXIT_INVALID,
    EXIT_OK,
    InvalidInputError,
    LoopOpsError,
)
from .readiness import audit_registry
from .redaction import scan_path
from .registry import load_budgets, load_ledger, load_registry
from .validators import ERROR, has_errors, validate
from .worktrees import audit_report, collect_worktrees

PROG = "py -3.9 -m scripts.loop_ops"


def _emit_json(payload: Any) -> None:
    print(json.dumps(payload, indent=2, sort_keys=False))


def _bullets(lines: List[str], prefix: str = "  - ") -> str:
    return "\n".join(prefix + line for line in lines)


# --- validate ----------------------------------------------------------------


def cmd_validate(args: argparse.Namespace) -> int:
    registry = load_registry(args.registry)
    findings = validate(registry)

    if args.json:
        _emit_json(
            {
                "command": "validate",
                "registry_id": registry.registry_id,
                "phase": registry.phase,
                "loops_checked": len(registry.loops),
                "valid": not has_errors(findings),
                "findings": [
                    {
                        "severity": f.severity,
                        "code": f.code,
                        "loop_id": f.loop_id,
                        "message": f.message,
                    }
                    for f in findings
                ],
            }
        )
        return EXIT_INVALID if has_errors(findings) else EXIT_OK

    print("MellyCore loop registry validation")
    print("  registry: {}".format(registry.registry_id))
    print("  phase:    {} ({})".format(registry.phase, "report-only" if registry.phase == 1 else "see registry"))
    print("  loops:    {}".format(len(registry.loops)))
    print("")

    if not findings:
        print("PASS no findings; registry is valid for Phase 1")
        return EXIT_OK

    for finding in findings:
        print(finding.render())
    print("")

    errors = sum(1 for f in findings if f.severity == ERROR)
    if errors:
        print("FAIL {} error(s), {} warning(s)".format(errors, len(findings) - errors))
        return EXIT_INVALID
    print("PASS 0 errors, {} warning(s)".format(len(findings)))
    return EXIT_OK


# --- audit -------------------------------------------------------------------


def cmd_audit(args: argparse.Namespace) -> int:
    registry = load_registry(args.registry)
    report = audit_registry(registry)

    if args.json:
        _emit_json({"command": "audit", **report})
        return EXIT_OK

    print("MellyCore loop capability audit")
    print("  registry: {}  phase: {}".format(report["registry_id"], report["phase"]))
    print("")
    print("Capability tiers are earned separately. A file existing proves configuration, not capability.")
    print("")

    for loop in report["loops"]:
        print("{} [{}]".format(loop["loop_id"], loop["status"]))
        print("  {}".format(loop["title"]))
        for tier, data in loop["capabilities"].items():
            mark = "yes" if data["value"] else "no "
            print("    {} {:<20} {}".format(mark, tier, data["evidence"]))
        print("")

    summary = report["summary"]
    print("Summary")
    print("  loops total:        {}".format(summary["loops_total"]))
    print("  enabled:            {}".format(summary["loops_enabled"]))
    print("  disabled:           {}".format(summary["loops_disabled"]))
    print("  validated:          {}".format(summary["validated"]))
    print("  exercised:          {}".format(summary["exercised"]))
    print("  human approved:     {}".format(summary["human_approved"]))
    print("  production enabled: {}".format(summary["production_enabled"]))
    print("")
    print("Assessment: {}".format(report["honest_assessment"]))
    return EXIT_OK


# --- guard -------------------------------------------------------------------


def cmd_guard(args: argparse.Namespace) -> int:
    registry = load_registry(args.registry)
    ledger = load_ledger(args.ledger)
    decision = evaluate_or_block(ledger, registry)

    if args.json:
        _emit_json(
            {
                "command": "guard",
                "loop_id": decision.loop_id,
                "run_id": decision.run_id,
                "decision": decision.decision,
                "reasons": decision.reasons,
                "checks": decision.checks,
                "exit_code": decision.exit_code,
                "deterministic": True,
            }
        )
        return decision.exit_code

    print("MellyCore loop guard")
    print("  loop: {}".format(decision.loop_id))
    print("  run:  {}".format(decision.run_id))
    print("")
    for name, result in decision.checks.items():
        print("  {:<22} {}".format(name, result))
    print("")
    print("DECISION {}".format(decision.decision))
    print(_bullets(decision.reasons))
    return decision.exit_code


# --- estimate-cost -----------------------------------------------------------


def cmd_estimate_cost(args: argparse.Namespace) -> int:
    registry = load_registry(args.registry)
    budgets = load_budgets(args.budgets)

    if args.loop:
        loop = registry.get(args.loop)
        if loop is None:
            raise InvalidInputError("unknown loop id {!r}".format(args.loop))
        loops = [loop]
    else:
        loops = registry.loops

    maker_checker: Optional[bool] = None
    if args.maker_checker:
        maker_checker = True
    elif args.no_maker_checker:
        maker_checker = False

    reports: List[Dict[str, Any]] = [
        estimate_loop(loop, budgets, parallel_agents=args.parallel_agents, apply_maker_checker=maker_checker)
        for loop in loops
    ]

    if args.json:
        _emit_json(
            {
                "command": "estimate-cost",
                "basis": "ESTIMATE_NOT_MEASURED",
                "basis_note": (
                    "These figures are estimates derived from planning inputs. They are not measured "
                    "token usage. No MellyCore loop has been run."
                ),
                "parallel_agents": args.parallel_agents,
                "estimates": reports,
            }
        )
        return EXIT_OK

    print("MellyCore loop cost estimate")
    print("  BASIS: ESTIMATE_NOT_MEASURED -- these are planning estimates, not measured usage.")
    print("  No MellyCore loop has been run, so no measured token spend exists.")
    print("  parallel agents: {}".format(args.parallel_agents))
    print("")

    for report in reports:
        print("{} [{}] verifier_required={}".format(report["loop_id"], report["status"], report["verifier_required"]))
        for scenario in report["scenarios"]:
            flag = "" if scenario["within_per_run_budget"] else "  OVER per-run budget"
            print(
                "    {:<16} ~{:>7} tokens  (maker/checker x{}){}".format(
                    scenario["scenario"],
                    scenario["estimated_tokens"],
                    scenario["multipliers"]["maker_checker"],
                    flag,
                )
            )
        realistic = report["realistic"]
        flag = "" if realistic["within_per_run_budget"] else "  OVER per-run budget"
        print(
            "    {:<16} ~{:>7} tokens  (weighted mix){}".format(
                "realistic", realistic["estimated_tokens"], flag
            )
        )
        print("")
    return EXIT_OK


# --- worktree-audit ----------------------------------------------------------


def cmd_worktree_audit(args: argparse.Namespace) -> int:
    worktrees = collect_worktrees(check_dirty=not args.no_dirty_check)
    report = audit_report(worktrees)

    if args.json:
        _emit_json({"command": "worktree-audit", **report})
        return EXIT_OK

    print("MellyCore worktree audit (read-only)")
    print("  This audit never removes, prunes, unlocks, resets, or cleans anything.")
    print("  worktrees: {}".format(report["worktree_count"]))
    print("")
    for wt in report["worktrees"]:
        if wt["dirty"] is None:
            dirty = "unknown"
        else:
            dirty = "dirty" if wt["dirty"] else "clean"
        print("  {}".format(wt["path"]))
        print("    branch: {}".format(wt["branch"] or "(detached)"))
        print("    head:   {}".format(wt["short_head"]))
        print("    state:  {}".format(dirty))
        if wt["risks"]:
            print("    risks:  {}".format(", ".join(wt["risks"])))
        print("")

    flagged = {k: v for k, v in report["risk_summary"].items() if v}
    if flagged:
        print("Risks found (operator decides; this tool does not act):")
        for risk, count in flagged.items():
            print("  {:<24} {}".format(risk, count))
    else:
        print("No collision or hygiene risks detected.")
    return EXIT_OK


# --- redact-check ------------------------------------------------------------


def cmd_redact_check(args: argparse.Namespace) -> int:
    findings = scan_path(args.path)

    if args.json:
        _emit_json(
            {
                "command": "redact-check",
                "path": args.path,
                "note": "Values are never reported. Only file, line, and category.",
                "read_only": True,
                "finding_count": len(findings),
                "findings": [f.to_dict() for f in findings],
            }
        )
        return EXIT_INVALID if findings else EXIT_OK

    print("MellyCore redaction check: {}".format(args.path))
    print("  Read-only. No file is modified. Detected values are never printed.")
    print("")
    if not findings:
        print("PASS no secret-shaped strings found")
        print("Note: detection is heuristic. A clean scan is not proof that no secret is present.")
        return EXIT_OK

    for finding in findings:
        print("  {}".format(finding.render()))
    print("")
    print("FAIL {} finding(s) need human review".format(len(findings)))
    return EXIT_INVALID


# --- parser ------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=PROG,
        description=(
            "MellyCore Loop Operations. Read-only tooling for defining, inspecting, validating, "
            "and estimating recurring agent workflows. Phase 1 is report-only: nothing here "
            "mutates the repository or calls a provider."
        ),
    )
    parser.add_argument(
        "--registry",
        default=None,
        help="Path to LOOP_REGISTRY.json (default: shared_context/loops/LOOP_REGISTRY.json)",
    )
    sub = parser.add_subparsers(dest="command")

    p_validate = sub.add_parser("validate", help="Validate the loop registry")
    p_validate.add_argument("--json", action="store_true", help="Emit JSON")
    p_validate.set_defaults(func=cmd_validate)

    p_audit = sub.add_parser("audit", help="Audit real loop capability")
    p_audit.add_argument("--json", action="store_true", help="Emit JSON")
    p_audit.set_defaults(func=cmd_audit)

    p_guard = sub.add_parser("guard", help="Run the deterministic circuit breaker over a run ledger")
    p_guard.add_argument("--ledger", required=True, help="Path to a run ledger JSON file")
    p_guard.add_argument("--json", action="store_true", help="Emit JSON")
    p_guard.set_defaults(func=cmd_guard)

    p_cost = sub.add_parser("estimate-cost", help="Estimate token scenarios (estimates only)")
    p_cost.add_argument("--loop", default=None, help="Estimate a single loop by id")
    p_cost.add_argument("--budgets", default=None, help="Path to LOOP_BUDGETS.json")
    p_cost.add_argument(
        "--parallel-agents",
        type=float,
        default=1.0,
        help="Hypothetical parallel-agent multiplier (default 1.0; Phase 1 runs one agent)",
    )
    p_cost.add_argument(
        "--maker-checker",
        action="store_true",
        help="Force the maker/checker multiplier on, regardless of the loop's verifier_required",
    )
    p_cost.add_argument(
        "--no-maker-checker",
        action="store_true",
        help="Force the maker/checker multiplier off",
    )
    p_cost.add_argument("--json", action="store_true", help="Emit JSON")
    p_cost.set_defaults(func=cmd_estimate_cost)

    p_wt = sub.add_parser("worktree-audit", help="Read-only git worktree report")
    p_wt.add_argument(
        "--no-dirty-check",
        action="store_true",
        help="Skip per-worktree git status; dirty state is then reported as unknown",
    )
    p_wt.add_argument("--json", action="store_true", help="Emit JSON")
    p_wt.set_defaults(func=cmd_worktree_audit)

    p_redact = sub.add_parser("redact-check", help="Report secret-shaped strings without printing values")
    p_redact.add_argument(
        "--path",
        default="shared_context/loops",
        help="File or directory to scan (default: shared_context/loops)",
    )
    p_redact.add_argument("--json", action="store_true", help="Emit JSON")
    p_redact.set_defaults(func=cmd_redact_check)

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not getattr(args, "command", None):
        parser.print_help()
        return EXIT_INVALID

    if getattr(args, "maker_checker", False) and getattr(args, "no_maker_checker", False):
        print("ERROR --maker-checker and --no-maker-checker are mutually exclusive", file=sys.stderr)
        return EXIT_INVALID

    try:
        return args.func(args)
    except InvalidInputError as exc:
        print("ERROR invalid input: {}".format(exc), file=sys.stderr)
        return EXIT_INVALID
    except LoopOpsError as exc:
        print("ERROR {}".format(exc), file=sys.stderr)
        return EXIT_INVALID
