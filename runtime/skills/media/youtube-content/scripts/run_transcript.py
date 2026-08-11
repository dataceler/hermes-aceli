#!/usr/bin/env python3
"""Run fetch_transcript.py inside a dedicated, reusable virtual environment.

This launcher is safe on PEP 668 / EXTERNALLY-MANAGED Python installations:
it never installs into the current or system interpreter. The virtual environment
lives outside the skill directory so skill updates do not delete it.
"""

from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys

PACKAGE_SPEC = "youtube-transcript-api>=1,<2"
SKILL_DIR = Path(__file__).resolve().parents[1]
FETCH_SCRIPT = SKILL_DIR / "scripts" / "fetch_transcript.py"
HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes")).expanduser()
VENV_DIR = Path(
    os.environ.get(
        "YOUTUBE_CONTENT_VENV",
        HERMES_HOME / "cache" / "venvs" / "youtube-content",
    )
).expanduser().resolve()


def venv_python(venv_dir: Path) -> Path:
    """Return the platform-specific Python executable inside a venv."""
    if os.name == "nt":
        return venv_dir / "Scripts" / "python.exe"
    return venv_dir / "bin" / "python"


def module_available(python: Path, module: str) -> bool:
    """Check a module with the target interpreter, never the outer interpreter."""
    if not python.is_file():
        return False
    result = subprocess.run(
        [str(python), "-c", f"import {module}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0


def dependency_available(python: Path) -> bool:
    return module_available(python, "youtube_transcript_api")


def pip_available(python: Path) -> bool:
    return module_available(python, "pip")


def create_or_repair_venv() -> Path:
    """Create/repair the dedicated venv and install the pinned dependency range."""
    python = venv_python(VENV_DIR)
    has_python = python.is_file()
    has_pip = pip_available(python)
    if not has_python or not has_pip:
        VENV_DIR.parent.mkdir(parents=True, exist_ok=True)
        command = [sys.executable, "-m", "venv"]
        if has_python and not has_pip:
            # This path belongs exclusively to this skill. A partial venv can retain
            # a broken interpreter symlink unless it is explicitly cleared.
            command.append("--clear")
        command.append(str(VENV_DIR))
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as exc:
            raise SystemExit(
                "Unable to create or repair the YouTube transcript virtual environment. "
                "Install your OS Python venv package (for example python3-venv) "
                "and retry. The system Python was not modified."
            ) from exc

    python = venv_python(VENV_DIR)
    if not pip_available(python):
        try:
            subprocess.run(
                [str(python), "-m", "ensurepip", "--upgrade"],
                check=True,
            )
        except subprocess.CalledProcessError as exc:
            raise SystemExit(
                f"Virtual environment at {VENV_DIR} has no working pip/ensurepip. "
                "Install the matching OS venv package and retry."
            ) from exc

    if not dependency_available(python):
        try:
            subprocess.run(
                [
                    str(python),
                    "-m",
                    "pip",
                    "install",
                    "--disable-pip-version-check",
                    PACKAGE_SPEC,
                ],
                check=True,
            )
        except subprocess.CalledProcessError as exc:
            raise SystemExit(
                f"Unable to install {PACKAGE_SPEC!r} in {VENV_DIR}. "
                "Check network/package-index access and retry. "
                "The system Python was not modified."
            ) from exc

    if not dependency_available(python):
        raise SystemExit(
            f"Virtual environment exists but youtube_transcript_api is unavailable: {VENV_DIR}"
        )
    return python


def main() -> None:
    if not FETCH_SCRIPT.is_file():
        raise SystemExit(f"Transcript helper not found: {FETCH_SCRIPT}")

    python = venv_python(VENV_DIR)
    if not dependency_available(python):
        python = create_or_repair_venv()

    argv = [str(python), str(FETCH_SCRIPT), *sys.argv[1:]]
    if os.name == "nt":
        completed = subprocess.run(argv, check=False)
        raise SystemExit(completed.returncode)
    os.execv(str(python), argv)


if __name__ == "__main__":
    main()
