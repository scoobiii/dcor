# DCOR — Compatibility Matrix

## Current foundation

The S0/S1/S2 foundation is intentionally pure Python with no runtime dependencies outside the standard library. Test tooling is supplied through the `test` optional dependency in `pyproject.toml`.

This makes the foundation suitable for validation in lightweight Linux environments, subject to the availability of a supported Python interpreter and virtual-environment tooling.

| Environment | Target | Validation status | Gate |
|---|---|---|---|
| Ubuntu x86_64 | Required | CI + local target | `scripts/test.sh` |
| Ubuntu ARM64 | Required | Local target | `scripts/test.sh` |
| Ubuntu PRoot | Target | Local validation required | `scripts/test.sh` |
| Alpine x86_64 | Required | Local validation required | `scripts/test.sh` |
| Alpine ARM64 | Required | Local validation required | `scripts/test.sh` |
| Alpine PRoot | Target | Local validation required | `scripts/test.sh` |
| Termux | Target | Local validation required | `scripts/test.sh` |

"Target" means the code is deliberately kept compatible where practical; it does **not** mean the environment is certified until the gate has actually been executed there.

## Foundation dependency policy

Current runtime dependencies:

- Python `>=3.11`
- no third-party runtime package

Current test dependencies:

- `pytest>=8.0`
- `pytest-cov>=5.0`

Do not install future connector stacks globally. When a connector introduces a dependency, document it at the connector boundary and add an explicit compatibility test.

## Validation protocol

For each environment:

```sh
./scripts/bootstrap.sh
./scripts/test.sh
```

Record at minimum:

- OS/distribution and architecture;
- Python version;
- bootstrap result;
- dependency installation result;
- complete test result;
- measured coverage;
- final `DCOR LOCAL GATE` result.

A compatibility row may move to **validated** only after the command has actually passed in that environment.

## Known portability boundary

The foundation does not currently require Docker, systemd, PostgreSQL, Redis, Kafka, Node.js, a browser, CUDA or a GPU. Those are intentionally outside the S0/S1/S2 portability contract.

Future stages may introduce optional dependencies for Parquet, MQTT, REST, optimization and ML. Those additions must update this matrix rather than silently changing the foundation requirements.
