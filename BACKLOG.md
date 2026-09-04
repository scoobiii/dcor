# DCOR Backlog — S0 to S11

## Delivery gate

Every sprint has four gates: **implementation → tests → CI validation → evidence/documentation**. A sprint cannot be marked DONE without all four.

| Sprint | Deliverable | Exit criteria | Status |
|---|---|---|---|
| S0 | Audit, baseline, repository contract, CI | clean repo baseline, CI runs on push | IN PROGRESS |
| S1 | Architecture + standards + canonical model | schemas, invariants and tests | IN PROGRESS |
| S2 | Connector SDK | lifecycle, errors, quality, lineage, contract tests | IN PROGRESS |
| S3 | Frontier | telemetry adapter + fixture/replay + validation | PLANNED |
| S4 | NLR/DOE | PUE/power/weather adapter + validation | PLANNED |
| S5 | CSV/Parquet | deterministic batch ingestion + normalization | PLANNED |
| S6 | MQTT + REST | protocol adapters + retry/idempotency tests | PLANNED |
| S7 | Twin + baseline | replay, counterfactual and baseline benchmark | PLANNED |
| S8 | Optimization | rules/PID/MPC/MILP benchmark and safety gates | PLANNED |
| S9 | DQN/RL | modernized DQN + RL benchmark, reproducible runs | PLANNED |
| S10 | Verify + Control | verified savings + governed actuation path | PLANNED |
| S11 | SaaS + production | multi-tenant, observability, security, release gate | PLANNED |

## S0 — Baseline

- Audit empty/new repository state.
- Establish product definition and non-goals.
- Establish CI-on-push gate.
- Establish delivery monitor in README.

## S1 — Contracts

- Architecture and standards.
- Canonical telemetry envelope.
- Asset hierarchy and facility identity.
- Data-quality taxonomy.
- Lineage contract.

## S2 — Connector SDK

- Source-independent connector interface.
- Connector configuration and lifecycle.
- Discovery/read/normalize/validate pipeline.
- Health and metrics contract.
- Contract-test harness.

## S3 — Frontier

- Implement adapter for the public Frontier telemetry schema.
- Preserve 10-minute timestamps and source lineage.
- Add replay fixture and quality tests.

## S4 — NLR/DOE

- Map PUE, IT power, cooling, HVAC, pump and weather fields.
- Validate energy boundaries and missing intervals.

## S5 — CSV/Parquet

- Streaming/chunked ingestion where appropriate.
- Schema mapping configuration.
- Deterministic normalization and timestamp policy.

## S6 — MQTT + REST

- MQTT topic mapping, QoS/reconnect behavior.
- REST polling, pagination, rate-limit and retry behavior.
- Idempotent ingestion.

## S7 — Digital Twin + Baseline

- Real-data replay through the same canonical contract.
- Counterfactual baseline.
- Rule/PID benchmark.
- Thermal/energy sanity constraints.

## S8 — Optimization

- Formal objective: energy cost + carbon + water + thermal risk + SLA risk + wear.
- Constraint registry.
- Rule, PID, MPC and MILP baselines.
- Safety validator before recommendation/control.

## S9 — DQN / RL

- Port original DQN research into an isolated experiment package.
- Double/Dueling/target-network/Huber improvements as applicable.
- Compare against non-RL baselines.
- Reproducibility: seed, dataset version, environment version, metrics.

## S10 — Verification + Control

- POTENTIAL/PREDICTED/EXECUTED/VERIFIED savings lifecycle.
- Workload/weather/tariff normalization.
- Recommendation audit trail.
- Policy-gated actuation interface.

## S11 — Production SaaS

- Tenant isolation.
- RBAC and secrets management.
- Connector observability.
- SLOs and incident runbooks.
- Deployment/rollback.
- Security and dependency gates.
- Release checklist.

## Explicit non-goals

- No dashboard-first development.
- No vendor lock-in in the domain layer.
- No direct AI-to-actuator path.
- No unverified savings marketed as realized savings.
- No claim of Uptime Institute certification.
