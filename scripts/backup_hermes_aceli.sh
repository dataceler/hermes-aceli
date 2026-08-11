#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_HOME="${HERMES_HOME_SOURCE:-$HOME/.hermes}"
MODE="${1:-export}"

cd "$ROOT"
python3 scripts/export_hermes_state.py --source "$SOURCE_HOME"
python3 scripts/verify_sanitized_export.py

git status --short

if [[ "$MODE" == "commit" ]]; then
  git add --all
  if git diff --cached --quiet; then
    echo "No changes to commit."
  else
    git commit -m "backup: sanitized Hermes state"
  fi
elif [[ "$MODE" != "export" ]]; then
  echo "Usage: $0 [export|commit]" >&2
  exit 2
fi

# Deliberately no automatic push. Publishing remains an explicit reviewed action.
