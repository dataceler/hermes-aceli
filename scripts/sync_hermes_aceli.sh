#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_HOME="${HERMES_HOME_SOURCE:-$HOME/.hermes}"
cd "$ROOT"

python3 scripts/export_hermes_state.py --source "$SOURCE_HOME"
python3 scripts/verify_sanitized_export.py

git add --all
if git diff --cached --quiet; then
  exit 0
fi

git commit -m "backup: sanitized Hermes state"
GIT_TERMINAL_PROMPT=0 git push origin main
printf 'hermes-aceli sync: published %s\n' "$(git rev-parse --short HEAD)"
