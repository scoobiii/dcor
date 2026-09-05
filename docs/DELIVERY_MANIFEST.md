# DCOR — Delivery Manifest

This is the machine-auditable inventory behind the README delivery monitor.

## Completion rule

A milestone is DONE only when required artifacts exist, tests pass, package coverage meets the project gate, CI validates the commit, and evidence/documentation is current.

LOC is telemetry, never proof of completion.

## Inventory

| Milestone | Required artifacts | Status |
|---|---|---|
| S0 | README, backlog, CI, bootstrap/test, audit revalidation | IN PROGRESS |
| S1 | architecture, standards, canonical model, reuse matrix | IN PROGRESS |
| S2 | Connector SDK + contract tests | IN PROGRESS |
| S3 | Frontier connector + fixture/replay | PLANNED |
| MV0 | verifiable optimization + thermal risk + evidence | PLANNED |
| S4 | NLR/DOE connector | PLANNED |
| S5 | CSV/Parquet | PLANNED |
| S6 | MQTT/REST | PLANNED |
| S7 | Twin + baseline/counterfactual | PLANNED |
| S8 | Rule/PID/MPC/MILP + thermal optimizer | PLANNED |
| S9 | DQN/RL | PLANNED |
| S10 | verification + policy/control | PLANNED |
| S11 | SaaS/fleet/production | PLANNED |

## New documentation contract

| Artifact | Purpose |
|---|---|
| `docs/THERMAL_OPTIMIZATION.md` | thermal state, risk, TTU, psychrometrics and setpoint optimization |
| `docs/HISTORICAL_COOLING_CASES.md` | Prineville, Google/DeepMind, Google London and Oracle benchmark context |
| `docs/BENCHMARK.md` | Benchmark 001 and common evaluation protocol |
| `docs/STANDARDS.md` | standards hierarchy and H1 policy semantics |
| `docs/USE_CASES.md` | thermal-risk and economic-setpoint use cases |

## Evidence rule

Historical public values retain their source date. A historical PUE/WUE value cannot be presented as a current measurement. Unknown remains `unknown`.

## Evolution protocol

1. define required paths;
2. implement complete vertical slice;
3. add tests;
4. update documentation;
5. run local gate;
6. require CI;
7. update status only with exit evidence.
