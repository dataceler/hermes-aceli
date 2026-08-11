#!/usr/bin/env python3
"""Export a strict, sanitized allowlist from a Hermes home into this repository."""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {".md", ".py", ".sh", ".bash", ".json", ".yaml", ".yml", ".toml", ".txt"}
FORBIDDEN_PARTS = {".env", "auth.json", "state.db", "sessions", "logs", "cache", "output", "executions.db", "notepad.db", ".git"}
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\b(?:ghp|gho|ghu|ghs)_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
    re.compile(r"(?i)\b(?:api[_-]?key|secret|password|authorization)\s*[:=]\s*['\"]?[^\s'\"]{12,}"),
]


def is_allowed_file(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS and not any(part in FORBIDDEN_PARTS for part in path.parts)


def secret_reason(path: Path) -> str | None:
    if not is_allowed_file(path):
        return "not-allowlisted"
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except OSError as exc:
        return f"unreadable: {exc.__class__.__name__}"
    for pattern in SECRET_PATTERNS:
        if pattern.search(content):
            return "secret-pattern"
    return None


def copy_file(source: Path, destination: Path, copied: list[str], skipped: list[dict[str, str]]) -> None:
    reason = secret_reason(source)
    relative = str(destination.relative_to(REPO))
    if reason:
        skipped.append({"source": str(source), "destination": relative, "reason": reason})
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    copied.append(relative)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes")))
    args = parser.parse_args()
    source = args.source.expanduser().resolve()
    if not source.is_dir():
        raise SystemExit(f"Hermes source does not exist: {source}")

    runtime = REPO / "runtime"
    copied: list[str] = []
    skipped: list[dict[str, str]] = []
    for directory in (runtime / "memories", runtime / "skills"):
        if directory.exists():
            shutil.rmtree(directory)
    jobs = runtime / "cron" / "jobs.json"
    if jobs.exists():
        jobs.unlink()

    for name in ("MEMORY.md", "USER.md"):
        copy_file(source / "memories" / name, runtime / "memories" / name, copied, skipped)
    copy_file(source / "cron" / "jobs.json", runtime / "cron" / "jobs.json", copied, skipped)

    skills = source / "skills"
    if skills.is_dir():
        for file in sorted(skills.rglob("*")):
            if file.is_file() and not any(part.startswith(".") for part in file.relative_to(skills).parts):
                copy_file(file, runtime / "skills" / file.relative_to(skills), copied, skipped)

    manifest = {
        "schema_version": 1,
        "exported_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": str(source),
        "copied": copied,
        "skipped": skipped,
    }
    (runtime / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"exported={len(copied)} skipped={len(skipped)} manifest=runtime/manifest.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
