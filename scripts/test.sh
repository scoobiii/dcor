#!/usr/bin/env sh
set -eu

VENV="${DCOR_VENV:-.venv}"

if [ -f "$VENV/bin/activate" ]; then
  # shellcheck disable=SC1090
  . "$VENV/bin/activate"
fi

if ! command -v python >/dev/null 2>&1; then
  echo 'ERROR: Python is required. Run ./scripts/bootstrap.sh first.' >&2
  exit 1
fi

printf '%s\n' 'DCOR local validation'
printf '%s\n' '====================='
printf '\n'

printf '%-22s' 'Python'
python --version

printf '%-22s' 'Dependencies'
python -m pip check >/dev/null
printf '%s\n' 'OK'

printf '%-22s' 'Canonical model'
python -m pytest tests/test_canonical.py -q
printf '%s\n' 'PASS'

printf '%-22s' 'Connector SDK'
python -m pytest tests/test_connector_sdk.py -q
printf '%s\n' 'PASS'

printf '%-22s' 'Architecture'
test -s README.md
test -s ARCHITECTURE.md
test -s STANDARDS.md
test -s BACKLOG.md
test -s docs/CANONICAL_DATA_MODEL.md
test -s docs/REUSE_MATRIX.md
test -s docs/DEVELOPMENT.md
test -s docs/COMPATIBILITY.md
test -s docs/DELIVERY_MANIFEST.md
test -s docs/MV0_FIRST_VERIFIABLE_OPTIMIZATION.md
test -s docs/EVIDENCE_CONTRACT.md
test -s docs/REPLAY.md
test -s docs/BENCHMARK.md
test -s docs/USE_CASES.md
test -s docs/CONNECTOR_ROI.md
test -s docs/AUDIT_REVALIDATION.md
test -s docs/OTTO_BRAND_SYSTEM.md
grep -q 'S0' README.md
grep -q 'S11' README.md
grep -q 'MV0' README.md
grep -q 'Connector SDK' BACKLOG.md
grep -q 'EVIDENCE_CONTRACT' BACKLOG.md
printf '%s\n' 'PASS'

printf '%-22s' 'Tests'
python -m pytest --cov=dcor --cov-report=term-missing --cov-report=xml --cov-fail-under=100
printf '%s\n' 'PASS'

printf '%-22s' 'Coverage'
python -m coverage report --fail-under=100 >/dev/null
printf '%s\n' 'PASS'

cat <<'EOF'

      .----.
   .-'  OTTO '-.
  /  VERIFIED  \\
  \  DCOR GATE /
   '----------'

EOF
printf '%s\n' 'DCOR LOCAL GATE: PASS'
