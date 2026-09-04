# DCOR — Local Development

## One-command contract

DCOR uses the same bootstrap and validation entry points across supported POSIX environments:

```sh
./scripts/bootstrap.sh
./scripts/test.sh
```

The intended developer flow is:

```sh
git clone <repository>
cd dcor
./scripts/bootstrap.sh
./scripts/test.sh
```

`bootstrap.sh` creates `.venv` and installs the package with the test extras. `test.sh` activates the local environment when present and executes the same validation gate used by CI.

## Validation output

A successful local gate is expected to report:

```text
DCOR local validation
=====================

Python ............... 3.x
Dependencies ......... OK
Canonical model ...... PASS
Connector SDK ........ PASS
Architecture ......... PASS
Tests ................ PASS
Coverage ............. PASS

DCOR LOCAL GATE: PASS
```

The exact Python patch version and pytest summary may vary by environment.

## Coverage policy

The project gate is **100% statement coverage for the `dcor` package**. A lower result is a gate failure, not a warning. New production code must arrive with tests that exercise all executable paths required by the coverage tool.

This is deliberately stricter than a conventional minimum threshold because DCOR is a telemetry, optimization and eventually control platform: untested contract behavior must not silently enter downstream stages.

## Local/CI parity

The CI workflow must invoke `scripts/test.sh` rather than maintain a second, divergent test recipe. CI may add matrix-specific setup and artifact publication around that gate, but the core validation command remains the same.

Coverage reports are generated in XML form so CI can preserve them as workflow artifacts for diagnosis and audit. GitHub Actions supports retaining test and coverage output as artifacts after a run. citeturn0search0turn0search1

## Environment rules

- Core runtime remains dependency-light.
- Do not add a system service, database, broker, GPU stack or browser dependency to the foundation sprint without a concrete feature requiring it.
- Prefer Python standard library and POSIX shell for the bootstrap/gate layer.
- Connector-specific dependencies belong to the connector that needs them and should not contaminate the canonical model.
- A new dependency requires tests and documentation of its portability impact.

## Development commands

```sh
# bootstrap isolated environment
./scripts/bootstrap.sh

# run the complete local gate
./scripts/test.sh

# direct test execution, when debugging
python -m pytest
```

If executable permissions were not preserved by a copy mechanism, use:

```sh
sh scripts/bootstrap.sh
sh scripts/test.sh
```

## Sprint completion rule

A sprint is not complete because its code exists. The delivery monitor must have:

1. all planned files present;
2. all required tests present and passing;
3. the coverage gate passing at 100%;
4. architecture/documentation checks passing;
5. CI green for the commit;
6. exit evidence identified in `BACKLOG.md`.

The repository's delivery manifest is the source of truth for planned implementation paths and their status.
