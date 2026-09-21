#!/usr/bin/env python3
"""Reject invisible Unicode characters in Git-tracked text files.

Agents read tracked files as instructions or context. Invisible characters
(zero-width, bidirectional controls, tag characters, variation selectors)
can hide text from human reviewers while still reaching the model.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import unicodedata
from pathlib import Path


# Invisible characters outside Unicode category Cf.
EXTRA_INVISIBLE_RANGES = (
    (0xFE00, 0xFE0F),    # variation selectors
    (0xE0100, 0xE01EF),  # variation selectors supplement
    (0x115F, 0x1160),    # Hangul choseong/jungseong fillers
    (0x3164, 0x3164),    # Hangul filler
    (0xFFA0, 0xFFA0),    # halfwidth Hangul filler
)


def is_invisible(char: str) -> bool:
    if unicodedata.category(char) == "Cf":
        return True
    code = ord(char)
    return any(low <= code <= high for low, high in EXTRA_INVISIBLE_RANGES)


def describe(char: str) -> str:
    return f"U+{ord(char):04X} {unicodedata.name(char, 'UNNAMED')}"


def tracked_files(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=root, capture_output=True, text=True, check=True
    )
    return [root / name for name in result.stdout.split("\0") if name]


def read_text(path: Path) -> str | None:
    """Return file text, or None for binary, non-UTF-8, or missing files."""
    try:
        data = path.read_bytes()
    except (FileNotFoundError, IsADirectoryError):
        return None
    if b"\0" in data:
        return None
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return None


def find_invisible(text: str) -> list[tuple[int, int, str]]:
    """Return (line, column, description) for each invisible character."""
    findings = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        for column, char in enumerate(line, start=1):
            if is_invisible(char):
                findings.append((line_number, column, describe(char)))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    checked = 0
    for path in tracked_files(root):
        text = read_text(path)
        if text is None:
            continue
        checked += 1
        for line, column, description in find_invisible(text):
            errors.append(f"{path.relative_to(root)}:{line}:{column}: {description}")
    if errors:
        print("Invisible Unicode check failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Invisible Unicode check passed ({checked} text file(s)).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
