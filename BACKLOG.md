# DCOR Backlog — S0 to S11 + MV0

## Delivery gate

Every sprint has four gates: **implementation → tests → CI validation → evidence/documentation**. A sprint cannot be marked DONE without all four.

## Product-value gate

**MV0 — First Verifiable Optimization** is a cross-cutting vertical slice between foundation/connectivity and advanced optimization. It does not replace S0–S11; it proves the product thesis before the project commits to RL, control or SaaS complexity.

| Milestone | Deliverable | Exit criteria | Status |
|---|---|---|---|
| S0 | Audit, baseline, repository contract, CI | clean repo baseline, CI runs on push | IN PROGRESS |
| S1 | Architecture + standards + canonical model | schemas, invariants and tests | IN PROGRESS |
| S2 | Connector SDK | lifecycle, errors, quality, lineage, contract tests | IN PROGRESS |
| S3 | Frontier | telemetry adapter + fixture/replay + validation | PLANNED |
| **MV0** | First Verifiable Optimization | Frontier → canonical → quality/lineage → replay → baseline → counterfactual → optimization → verification/evidence | **PLANNED** |
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
- Revalidate external-audit findings against current HEAD.

## S1 — Contracts

- Architecture and standards.
- Canonical telemetry envelope.
- Asset hierarchy and facility identity.
- Data-quality taxonomy.
- Lineage contract.
- Evidence Contract boundary for future optimization results.

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
- Produce the first real canonical telemetry path.

## MV0 — First Verifiable Optimization

- Execute the complete vertical slice using Frontier telemetry.
- Produce deterministic replay manifest.
- Calculate a versioned baseline and counterfactual.
- Run at least one deterministic non-RL optimization method.
- Evaluate safety/policy constraints before recommendation.
- Produce POTENTIAL/PREDICTED/EXECUTED/VERIFIED evidence without conflating states.
- Publish a reproducible machine-readable evidence artifact.
- Keep illustrative values separate from measured results.

Supporting contracts:

- `docs/MV0_FIRST_VERIFIABLE_OPTIMIZATION.md`
- `docs/EVIDENCE_CONTRACT.md`
- `docs/REPLAY.md`

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

- Add an explicit data-engineering/feature-store stage before RL experiments.
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

## Cross-cutting product artifacts

| Artifact | Purpose | Gate |
|---|---|---|
| `docs/USE_CASES.md` | Concrete user/business problems | Product planning |
| `docs/CONNECTOR_ROI.md` | Adapter prioritization and scope control | Before new connector |
| `docs/BENCHMARK.md` | Common scientific/performance evaluation | Before performance claims |
| `docs/EVIDENCE_CONTRACT.md` | Reproducible optimization evidence | MV0/S10 |
| `docs/REPLAY.md` | Deterministic data reproduction | S3/MV0/S7/S9 |
| `docs/AUDIT_REVALIDATION.md` | Snapshot finding lifecycle | Every external audit |
| `docs/OTTO_BRAND_SYSTEM.md` | Technical brand/operational states | Product/dev UX |

## Explicit non-goals

- No dashboard-first development.
- No vendor lock-in in the domain layer.
- No direct AI-to-actuator path.
- No unverified savings marketed as realized savings.
- No claim of Uptime Institute certification.
- No RL implementation before validated data/replay/non-RL baselines.
- No connector expansion without a documented ROI/use-case rationale.
