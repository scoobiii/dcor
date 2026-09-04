#!/usr/bin/env sh
set -eu

PYTHON="${PYTHON:-python3}"
VENV="${DCOR_VENV:-.venv}"

printf '%s\n' 'DCOR bootstrap'
printf '%s\n' '==============='

if ! command -v "$PYTHON" >/dev/null 2>&1; then
  echo "ERROR: Python interpreter '$PYTHON' was not found." >&2
  exit 1
fi

"$PYTHON" --version

if [ ! -d "$VENV" ]; then
  "$PYTHON" -m venv "$VENV"
fi

# shellcheck disable=SC1090
. "$VENV/bin/activate"

python -m pip install --upgrade pip
python -m pip install -e '.[test]'

printf '\n%s\n' 'DCOR bootstrap: PASS'
