#!/usr/bin/env python3
"""Offline deterministic checks for the Caramel Digital Studio repository."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "AGENT_HANDOFF_LOG.md",
    "AGENT_HANDOFF_TEMPLATE.md",
    "AGENT_LANGUAGE_PROTOCOL.md",
    "GOOGLE_CALENDAR_05A_MANUAL_PAYMENT_TEMPLATES_2026-11-24.md",
    "GOOGLE_CALENDAR_05A_BOOKING_FLOW_TEST_CHECKLIST_2026-11-24.md",
)
TEXT_SUFFIXES = {
    ".css", ".html", ".js", ".json", ".md", ".mjs", ".py", ".sh",
    ".toml", ".ts", ".tsx", ".txt", ".yml", ".yaml",
}


def run_git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, capture_output=True, check=False
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result.stdout.strip()


def tracked_text_files() -> list[Path]:
    paths = []
    for item in run_git("ls-files").splitlines():
        path = ROOT / item
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            paths.append(path)
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    failures: list[str] = []
    warnings: list[str] = []
    files = tracked_text_files()

    # Build the retired provider name without placing the literal in this checker.
    retired_provider = "Str" + "ipe"
    matches = []
    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        if retired_provider.casefold() in text.casefold():
            matches.append(str(path.relative_to(ROOT)))
    if matches:
        failures.append("Retired provider reference found in: " + ", ".join(matches))

    for required in REQUIRED_FILES:
        if not (ROOT / required).is_file():
            failures.append(f"Required agent file missing: {required}")

    status = run_git("status", "--porcelain")
    branch = run_git("branch", "--show-current")
    head = run_git("rev-parse", "HEAD")
    ci_mode = bool(os.environ.get("CI"))
    try:
        upstream = run_git("rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}")
        remote_head = run_git("rev-parse", upstream)
    except RuntimeError:
        if not ci_mode:
            failures.append("No upstream branch is available for local remote-alignment verification")
        upstream = "detached-ci-checkout"
        remote_head = head
    if status:
        failures.append("Working tree has uncommitted changes")
    if branch and branch != "main" and not ci_mode:
        warnings.append(f"Current branch is {branch}, expected main for release verification")
    if head != remote_head:
        failures.append(f"Local HEAD {head[:12]} differs from {upstream} {remote_head[:12]}")

    result = {
        "repository": str(ROOT),
        "tracked_text_files_checked": len(files),
        "retired_provider_matches": matches,
        "required_agent_files_missing": [
            item for item in REQUIRED_FILES if not (ROOT / item).is_file()
        ],
        "branch": branch,
        "upstream": upstream,
        "head": head,
        "remote_head": remote_head,
        "working_tree_clean": not bool(status),
        "failures": failures,
        "warnings": warnings,
        "passed": not failures,
    }

    if args.as_json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Checked {len(files)} tracked text files")
        print(f"Branch: {branch}")
        print(f"Remote alignment: {'aligned' if head == remote_head else 'different'}")
        print(f"Working tree: {'clean' if not status else 'changes present'}")
        print(f"Retired-provider matches: {len(matches)}")
        print(f"Result: {'PASS' if not failures else 'FAIL'}")
        for warning in warnings:
            print(f"WARNING: {warning}")
        for failure in failures:
            print(f"ERROR: {failure}")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
