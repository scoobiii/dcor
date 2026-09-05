# DCOR — Delivery Manifest

This file is the machine-auditable delivery inventory behind the README sprint monitor.

## Rules

A deliverable is considered complete only when its required repository paths exist, its tests pass, its production package meets the 100% coverage gate, and CI validates the commit.

LOC is tracked as an engineering telemetry signal, **not** as a completion criterion: a smaller implementation is not better if it omits required behavior, and extra LOC is not evidence of delivery.

## Inventory

| Milestone | Required artifacts | Planned LOC | Status | Exit evidence |
|---|---|---:|---|---|
| S0 | `README.md`, `BACKLOG.md`, `.github/workflows/ci.yml`, `scripts/bootstrap.sh`, `scripts/test.sh` | TBD | IN PROGRESS | reproducible local/CI gate + audit revalidation |
| S1 | `ARCHITECTURE.md`, `STANDARDS.md`, `docs/CANONICAL_DATA_MODEL.md`, `docs/REUSE_MATRIX.md`, `src/dcor/canonical.py` | TBD | IN PROGRESS | contract + architecture tests |
| S2 | `src/dcor/connectors/`, connector tests | TBD | IN PROGRESS | SDK contract tests + 100% coverage |
| S3 | Frontier connector + fixtures + validation | TBD | PLANNED | source replay + normalization evidence |
| MV0 | `docs/MV0_FIRST_VERIFIABLE_OPTIMIZATION.md`, `docs/EVIDENCE_CONTRACT.md`, `docs/REPLAY.md`, Frontier vertical slice | TBD | PLANNED | baseline + counterfactual + verified evidence |
| **MV1** | `docs/POWER_THERMAL_800VDC.md`, coupled power/thermal topology model, replay/counterfactual scenarios, deterministic optimizer evidence | TBD | **PLANNED** | comparable topology scenarios + constraints + evidence/verification |
| S4 | NLR/DOE connector + fixtures + validation | TBD | PLANNED | source replay + normalization evidence |
| S5 | CSV/Parquet connectors + fixtures + validation | TBD | PLANNED | ingestion + normalization evidence |
| S6 | MQTT + REST connectors + protocol fixtures | TBD | PLANNED | protocol contract evidence |
| S7 | Digital Twin + baseline/replay components | TBD | PLANNED | counterfactual benchmark |
| S8 | Rule/PID/MPC/MILP optimization components | TBD | PLANNED | optimizer benchmark |
| S9 | DQN/modern RL components + reproducible benchmark | TBD | PLANNED | RL benchmark |
| S10 | Savings verification + safety/policy/control components | TBD | PLANNED | verified savings + safety gates |
| S11 | SaaS/fleet/observability/production release artifacts | TBD | PLANNED | production release gate |

## Cross-cutting evidence

| Artifact | Purpose |
|---|---|
| `docs/USE_CASES.md` | Product/use-case definition |
| `docs/CONNECTOR_ROI.md` | Connector scope and priority control |
| `docs/BENCHMARK.md` | Performance/scientific comparison protocol |
| `docs/EVIDENCE_CONTRACT.md` | Reproducible optimization evidence |
| `docs/REPLAY.md` | Deterministic data reproduction |
| `docs/POWER_THERMAL_800VDC.md` | 800 VDC + liquid cooling power-thermal architecture and MV1 exit criteria |
| `docs/AUDIT_REVALIDATION.md` | External-audit snapshot revalidation |
| `docs/OTTO_BRAND_SYSTEM.md` | Technical mascot and operational-state system |

## Evolution protocol

For each sprint or milestone:

1. define required paths before implementation;
2. implement the minimum complete vertical slice;
3. add tests with the implementation;
4. update the manifest with actual LOC after implementation;
5. run `./scripts/test.sh`;
6. push and require CI to pass;
7. change the sprint/milestone status only after exit evidence exists.

The manifest intentionally uses `TBD` for future LOC until the implementation is designed. This avoids turning an arbitrary line-count estimate into a false delivery promise.

## Final delivery condition

The project is **not fully delivered** until S0–S11 are `DONE`, every required artifact is present, all required tests pass, and the final CI gate reports 100% package coverage. MV0 and MV1 are product-value milestones, not replacements for S0–S11. The README remains the human-facing monitor; this manifest is the detailed inventory.
