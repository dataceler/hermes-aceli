#!/usr/bin/env python3
"""Fail if the repository contains forbidden runtime data or secret-like values."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_NAMES = {".env", "auth.json", "state.db", "executions.db", "notepad.db"}
FORBIDDEN_DIRS = {"sessions", "logs", "cache", "output", ".git", "__pycache__"}
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\b(?:ghp|gho|ghu|ghs)_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
    re.compile(r"(?i)\b(?:api[_-]?key|secret|password|authorization)\s*[:=]\s*['\"]?[^\s'\"]{12,}"),
]


def main() -> int:
    findings: list[str] = []
    for path in ROOT.rglob("*"):
        if any(part in FORBIDDEN_DIRS for part in path.parts):
            continue
        if path.name in FORBIDDEN_NAMES or path.suffix.lower() in {".pem", ".key", ".p12", ".pfx"}:
            findings.append(f"forbidden-path: {path.relative_to(ROOT)}")
            continue
        if not path.is_file() or path.stat().st_size > 2_000_000:
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if any(pattern.search(content) for pattern in SECRET_PATTERNS):
            findings.append(f"secret-pattern: {path.relative_to(ROOT)}")
    if findings:
        print("SANITIZATION_FAILED")
        print("\n".join(findings))
        return 1
    print("SANITIZATION_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
