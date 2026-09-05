# DCOR — Delivery Manifest

This file is the machine-auditable delivery inventory behind the README sprint monitor.

## Rules

A deliverable is considered complete only when its required repository paths exist, its tests pass, its production package meets the 100% coverage gate, and CI validates the commit.

LOC is tracked as engineering telemetry, **not** as a completion criterion.

## Inventory

| Milestone | Required artifacts | Planned LOC | Status | Exit evidence |
|---|---|---:|---|---|
| S0 | `README.md`, `BACKLOG.md`, `.github/workflows/ci.yml`, `scripts/bootstrap.sh`, `scripts/test.sh` | TBD | IN PROGRESS | reproducible local/CI gate + audit revalidation |
| S1 | `ARCHITECTURE.md`, `STANDARDS.md`, `docs/CANONICAL_DATA_MODEL.md`, `docs/REUSE_MATRIX.md`, `src/dcor/canonical.py` | TBD | IN PROGRESS | contract + architecture tests |
| S2 | `src/dcor/connectors/`, connector tests | TBD | IN PROGRESS | SDK contract tests + 100% coverage |
| S3 | Frontier connector + fixtures + validation | TBD | PLANNED | source replay + normalization evidence |
| MV0 | `docs/MV0_FIRST_VERIFIABLE_OPTIMIZATION.md`, thermal-risk contracts, `docs/EVIDENCE_CONTRACT.md`, `docs/REPLAY.md`, Frontier vertical slice | TBD | PLANNED | baseline + counterfactual + risk + verified evidence |
| **MV1** | `docs/POWER_THERMAL_800VDC.md`, coupled power/thermal topology model, replay/counterfactual scenarios, deterministic optimizer evidence | TBD | **PLANNED** | comparable topology scenarios + constraints + evidence/verification |
| S4 | NLR/DOE connector + fixtures + validation | TBD | PLANNED | source replay + normalization evidence |
| S5 | CSV/Parquet connectors + fixtures + validation | TBD | PLANNED | ingestion + normalization tests |
| S6 | MQTT + REST connectors + protocol fixtures | TBD | PLANNED | protocol contract evidence |
| S7 | Digital Twin + baseline/replay components + historical cooling cases | TBD | PLANNED | counterfactual benchmark |
| S8 | Rule/PID/MPC/MILP + dynamic-setpoint/thermal optimizer components | TBD | PLANNED | optimizer benchmark + safety constraints |
| S9 | DQN/modern RL components + reproducible benchmark | TBD | PLANNED | RL benchmark |
| S10 | Savings verification + safety/policy/control components | TBD | PLANNED | verified savings + safety gates |
| S11 | SaaS/fleet/observability/production release artifacts | TBD | PLANNED | production release gate |

## Cross-cutting evidence

| Artifact | Purpose | Gate |
|---|---|---|
| `docs/USE_CASES.md` | Product/use-case definition | Product planning |
| `docs/CONNECTOR_ROI.md` | Connector scope and priority control | Before new connector |
| `docs/BENCHMARK.md` | Performance/scientific comparison protocol | Before performance claims |
| `docs/EVIDENCE_CONTRACT.md` | Reproducible optimization evidence | MV0/S10 |
| `docs/REPLAY.md` | Deterministic data reproduction | S3/MV0/S7/S9 |
| `docs/POWER_THERMAL_800VDC.md` | 800 VDC + liquid cooling power-thermal architecture and MV1 exit criteria | MV1 |
| `docs/THERMAL_OPTIMIZATION.md` | Thermal state, risk, TTU and dynamic setpoint optimization | MV0/S8 |
| `docs/THERMAL_PATTERNS_ASHRAE.md` | ASHRAE envelope and thermal-pattern semantics | MV0/S1 |
| `docs/HISTORICAL_COOLING_CASES.md` | Prineville, Google/DeepMind, Google London and Oracle benchmark context | MV0/S7 |
| `docs/AUDIT_REVALIDATION.md` | External-audit snapshot revalidation | Every external audit |
| `docs/OTTO_BRAND_SYSTEM.md` | Technical mascot and operational-state system | Product/dev UX |

## Evidence rules

Historical public values retain their source date. A historical PUE/WUE value cannot be presented as a current measurement. Unknown remains `unknown`.

Thermal and power-thermal documentation does not constitute implementation or operational validation. A milestone remains PLANNED until its implementation, tests, CI and evidence exit criteria exist.

## Evolution protocol

For each sprint or milestone:

1. define required paths before implementation;
2. implement the minimum complete vertical slice;
3. add tests with the implementation;
4. update the manifest with actual LOC after implementation;
5. run `./scripts/test.sh`;
6. push and require CI to pass;
7. change the sprint/milestone status only after exit evidence exists.

The manifest intentionally uses `TBD` for future LOC until implementation is designed.

## Final delivery condition

The project is **not fully delivered** until S0–S11 are `DONE`, every required artifact is present, all required tests pass, and the final CI gate reports 100% package coverage. MV0 and MV1 are product-value milestones, not replacements for S0–S11. The README remains the human-facing monitor; this manifest is the detailed inventory.
