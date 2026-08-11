#!/usr/bin/env python3
"""Verify structural invariants in the ecosystem qualification evidence."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_DOCUMENTS = {
    "CROSS_PROJECT_RECONCILIATION.md",
    "INTEGRATION_STATE.md",
    "DEPENDENCY_PUBLICATION.md",
    "EXPERIMENTAL_ASSIGNMENT_REGISTRY.md",
    "QUALIFICATION_MATRIX.md",
    "REFERENCE_COMMITS.md",
    "REMAINING_GAPS.md",
    "SOURCE_AUDIT.md",
    "WALLET_MARKETPLACE_AUDIT.md",
    "WALLET_MARKETPLACE_IMPLEMENTATION.md",
    "docs/REPOSITORY-MAP.md",
}
WORKING_REPOSITORIES = {
    "work/handshake-rs-profile",
    "work/hns-dane-bootstrap-generator",
    "work/hns-dane-browser-extension",
    "work/hns-dane-browser-mobile",
    "work/hns-dane-crawler",
    "work/hns-dane-engine",
    "work/hns-node-rs",
    "work/hns-rs",
    "work/hns-wallet-rs",
    "work/MeshMine",
}
QUALIFICATION_ROW = re.compile(
    r"^\|\s*(\d+)\s*\|.*\|\s*(PASS|PARTIAL|NOT RUN)(?::.*?)?\s*\|\s*$"
)
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
PENDING_FINAL_REVISIONS = "PENDING FINAL RECONCILIATION"
FINAL_REPORT_HEADINGS = {
    "## Repository and crate delivery",
    "## Canonical protocols and Denuo registry",
    "## `hns-node-rs`",
    "## Provider API and browser authority",
    "## Wallet, names, Shakedex, and market board",
    "## Database migrations and restart boundary",
    "## Bitcoin, Ethereum, and bilateral settlement",
    "## Qualification results",
    "## Security, trust, and release blockers",
    "## Exact revisions and commands",
}
FINAL_CODE_REPOSITORIES = {
    "hns-rs",
    "hns-node-rs",
    "hns-dane-engine",
    "hns-wallet-rs",
    "hns-dane-browser-mobile",
    "hns-dane-browser-extension",
}
FINAL_REFERENCE_REPOSITORIES = {
    "hns-rs": "work/hns-rs",
    "hns-node-rs": "work/hns-node-rs",
    "hns-dane-engine": "work/hns-dane-engine",
    "hns-wallet-rs": "work/hns-wallet-rs",
    "hns-dane-browser-mobile": "work/hns-dane-browser-mobile",
    "hns-dane-browser-extension": "work/hns-dane-browser-extension",
}
CURRENT_CHECKPOINT_HEADING = (
    "## 2026-08-02 local wallet and marketplace checkpoint"
)


def verify_required_documents(errors: list[str]) -> None:
    for relative in sorted(REQUIRED_DOCUMENTS):
        if not (ROOT / relative).is_file():
            errors.append(f"missing required evidence document: {relative}")


def verify_qualification_matrix(errors: list[str]) -> None:
    matrix = (ROOT / "QUALIFICATION_MATRIX.md").read_text(encoding="utf-8")
    rows: dict[int, str] = {}
    for line in matrix.splitlines():
        match = QUALIFICATION_ROW.match(line)
        if match:
            number = int(match.group(1))
            if number in rows:
                errors.append(f"duplicate qualification row: {number}")
            rows[number] = match.group(2)
    expected = set(range(1, 39))
    if set(rows) != expected:
        errors.append(
            "qualification rows differ from 1..38: "
            f"missing={sorted(expected - set(rows))}, extra={sorted(set(rows) - expected)}"
        )


def verify_checkpoint_inventory(errors: list[str]) -> None:
    checkpoints = (ROOT / "REFERENCE_COMMITS.md").read_text(encoding="utf-8")
    for repository in sorted(WORKING_REPOSITORIES):
        if f"`{repository}`" not in checkpoints:
            errors.append(f"reference checkpoint table omits {repository}")


def table_rows_with_label(text: str, label: str) -> list[str]:
    marker = f"`{label}`"
    return [
        line
        for line in text.splitlines()
        if line.startswith("|") and marker in line
    ]


def final_row(
    text: str,
    label: str,
    location: str,
    errors: list[str],
) -> str | None:
    rows = table_rows_with_label(text, label)
    if len(rows) != 1:
        errors.append(
            f"{location} must contain exactly one table row for {label}; "
            f"found {len(rows)}"
        )
        return None
    return rows[0]


def verify_final_row_fields(
    row: str,
    label: str,
    location: str,
    require_hash: bool,
    errors: list[str],
) -> str | None:
    cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
    if len(cells) != 4:
        errors.append(
            f"{location} row for {label} must have exactly four columns"
        )
        return None

    _, branch, revision_cell, qualification = cells
    if branch != "`main`":
        errors.append(f"{location} row for {label} does not record branch main")
    if "./scripts/check.sh" not in qualification:
        errors.append(
            f"{location} row for {label} lacks its scripts/check.sh command"
        )
    if not re.match(r"^(?:STAGED )?PASS\b", qualification):
        errors.append(f"{location} row for {label} lacks an explicit PASS result")

    match = re.fullmatch(r"`([0-9a-f]{40})`", revision_cell)
    if require_hash and match is None:
        errors.append(
            f"{location} row for {label} lacks an exact revision in its revision cell"
        )
    return match.group(1) if match else None


def verify_current_checkpoint(errors: list[str]) -> dict[str, str]:
    checkpoints = (ROOT / "REFERENCE_COMMITS.md").read_text(encoding="utf-8")
    if CURRENT_CHECKPOINT_HEADING not in checkpoints:
        errors.append(
            "reference checkpoints omit the dated 2026-08-02 wallet checkpoint"
        )
        return {}

    current = checkpoints.split(CURRENT_CHECKPOINT_HEADING, maxsplit=1)[1]
    current = current.split("\n## ", maxsplit=1)[0]
    revisions: dict[str, str] = {}
    for report_name, reference_name in sorted(FINAL_REFERENCE_REPOSITORIES.items()):
        row = final_row(
            current,
            reference_name,
            "current reference checkpoint",
            errors,
        )
        if row is None:
            continue
        revision = verify_final_row_fields(
            row,
            reference_name,
            "current reference checkpoint",
            True,
            errors,
        )
        if revision is not None:
            revisions[report_name] = revision

    ecosystem = final_row(
        current,
        "integration",
        "current reference checkpoint",
        errors,
    )
    if ecosystem is not None:
        verify_final_row_fields(
            ecosystem,
            "integration",
            "current reference checkpoint",
            False,
            errors,
        )
        if "containing commit" not in ecosystem:
            errors.append(
                "current reference checkpoint lacks ecosystem containing-commit policy"
            )
    return revisions


def verify_wallet_report(
    errors: list[str],
    allow_pending: bool,
    checkpoint_revisions: dict[str, str],
) -> None:
    report = (ROOT / "WALLET_MARKETPLACE_IMPLEMENTATION.md").read_text(
        encoding="utf-8"
    )
    headings = {line for line in report.splitlines() if line.startswith("## ")}
    for heading in sorted(FINAL_REPORT_HEADINGS - headings):
        errors.append(f"wallet implementation report omits section: {heading}")

    status_terms = (
        "implemented",
        "tested",
        "experimental",
        "disabled",
        "unavailable",
        "deferred",
    )
    for term in status_terms:
        if f"**{term}**" not in report:
            errors.append(f"wallet implementation report omits status definition: {term}")

    if PENDING_FINAL_REVISIONS in report:
        if not allow_pending:
            errors.append(
                "wallet implementation report still has pending final revisions"
            )
        return

    exact_section = report.split("## Exact revisions and commands", maxsplit=1)[-1]
    if (
        "| Repository | Branch | Revision | Last non-redundant qualification |"
        not in exact_section
    ):
        errors.append("wallet implementation report lacks the final ledger schema")
    qualification_ledger = exact_section.split(
        "Source-only production-continuation revisions",
        maxsplit=1,
    )[0]
    for repository in sorted(FINAL_CODE_REPOSITORIES):
        row = final_row(
            qualification_ledger,
            repository,
            "final report ledger",
            errors,
        )
        if row is None:
            continue
        revision = verify_final_row_fields(
            row,
            repository,
            "final report ledger",
            True,
            errors,
        )
        checkpoint = checkpoint_revisions.get(repository)
        if revision is not None and checkpoint is not None and revision != checkpoint:
            errors.append(
                f"final report revision for {repository} differs from current "
                "reference checkpoint"
            )

    ecosystem = final_row(
        qualification_ledger,
        "ecosystem",
        "final report ledger",
        errors,
    )
    if ecosystem is not None:
        verify_final_row_fields(
            ecosystem,
            "ecosystem",
            "final report ledger",
            False,
            errors,
        )
        if "containing commit" not in ecosystem:
            errors.append("final report lacks ecosystem containing-commit policy")


def link_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")]
    return target.split(maxsplit=1)[0]


def verify_relative_links(errors: list[str]) -> None:
    for document in sorted(ROOT.rglob("*.md")):
        if ".git" in document.parts:
            continue
        text = document.read_text(encoding="utf-8")
        for raw in MARKDOWN_LINK.findall(text):
            target = link_target(raw)
            if (
                not target
                or target.startswith(("#", "http://", "https://", "mailto:"))
            ):
                continue
            relative = unquote(target.split("#", 1)[0])
            resolved = (document.parent / relative).resolve()
            if not resolved.exists():
                errors.append(
                    f"{document.relative_to(ROOT)}: broken relative link {target!r}"
                )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--allow-pending-wallet-revisions",
        action="store_true",
        help="permit the final revision ledger to remain pending during pre-commit reconciliation",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    verify_required_documents(errors)
    verify_qualification_matrix(errors)
    verify_checkpoint_inventory(errors)
    checkpoint_revisions = verify_current_checkpoint(errors)
    verify_wallet_report(
        errors,
        args.allow_pending_wallet_revisions,
        checkpoint_revisions,
    )
    verify_relative_links(errors)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    suffix = (
        " (final wallet revisions pending)"
        if args.allow_pending_wallet_revisions
        else ""
    )
    print(
        "ecosystem evidence structure, 38-row matrix, checkpoints, wallet report, and links verified"
        f"{suffix}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
