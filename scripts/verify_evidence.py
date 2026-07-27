#!/usr/bin/env python3
"""Verify structural invariants in the ecosystem qualification evidence."""

from __future__ import annotations

from pathlib import Path
import re
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_DOCUMENTS = {
    "INTEGRATION_STATE.md",
    "QUALIFICATION_MATRIX.md",
    "REFERENCE_COMMITS.md",
    "REMAINING_GAPS.md",
    "SOURCE_AUDIT.md",
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
    "work/MeshMine",
}
QUALIFICATION_ROW = re.compile(
    r"^\|\s*(\d+)\s*\|.*\|\s*(PASS|PARTIAL|NOT RUN)(?::.*?)?\s*\|\s*$"
)
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


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
    expected = set(range(1, 27))
    if set(rows) != expected:
        errors.append(
            "qualification rows differ from 1..26: "
            f"missing={sorted(expected - set(rows))}, extra={sorted(set(rows) - expected)}"
        )


def verify_checkpoint_inventory(errors: list[str]) -> None:
    checkpoints = (ROOT / "REFERENCE_COMMITS.md").read_text(encoding="utf-8")
    for repository in sorted(WORKING_REPOSITORIES):
        if f"`{repository}`" not in checkpoints:
            errors.append(f"reference checkpoint table omits {repository}")


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


def main() -> int:
    errors: list[str] = []
    verify_required_documents(errors)
    verify_qualification_matrix(errors)
    verify_checkpoint_inventory(errors)
    verify_relative_links(errors)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("ecosystem evidence structure, 26-row matrix, checkpoints, and links verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
