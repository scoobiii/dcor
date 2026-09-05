# DCOR Backlog — S0 to S11 + MV0 + MV1

## Delivery gate

Every sprint has four gates: **implementation → tests → CI validation → evidence/documentation**. A sprint cannot be marked DONE without all four.

## Product-value gates

**MV0 — First Verifiable Optimization** proves the core telemetry-to-evidence vertical slice before advanced optimization.

**MV1 — 800 VDC + Liquid Cooling Power-Thermal Optimization** extends that proof into the AI-era high-density infrastructure boundary, where electrical distribution and thermal management are evaluated as one coupled system.

| Milestone | Deliverable | Exit criteria | Status |
|---|---|---|---|
| S0 | Audit, baseline, repository contract, CI | clean repo baseline, CI runs on push | IN PROGRESS |
| S1 | Architecture + standards + canonical model | schemas, invariants and tests | IN PROGRESS |
| S2 | Connector SDK | lifecycle, errors, quality, lineage, contract tests | IN PROGRESS |
| S3 | Frontier | telemetry adapter + fixture/replay + validation | PLANNED |
| **MV0** | First Verifiable Optimization + thermal risk | Frontier → canonical → replay → baseline → counterfactual → risk → optimization → verification/evidence | **PLANNED** |
| **MV1** | 800 VDC + liquid cooling co-optimization | coupled power/thermal topology → replay → counterfactual → deterministic optimization → evidence | **PLANNED** |
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
- Keep electrical and thermal telemetry addressable by common asset/time/lineage identifiers.
- Keep recommended, allowable, facility, OEM and optimizer setpoint semantics distinct.

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
- Calculate thermal/capacity/SLA risk from current state and forecast where data supports it.
- Evaluate candidate dynamic setpoints rather than treating a fixed temperature as universally optimal.
- Run at least one deterministic non-RL optimization method.
- Evaluate safety/policy constraints before recommendation.
- Produce POTENTIAL/PREDICTED/EXECUTED/VERIFIED evidence without conflating states.
- Publish a reproducible machine-readable evidence artifact.
- Keep illustrative values separate from measured results.

Supporting contracts:

- `docs/MV0_FIRST_VERIFIABLE_OPTIMIZATION.md`
- `docs/THERMAL_OPTIMIZATION.md`
- `docs/THERMAL_PATTERNS_ASHRAE.md`
- `docs/EVIDENCE_CONTRACT.md`
- `docs/REPLAY.md`

## MV1 — 800 VDC + Liquid Cooling Power-Thermal Optimization

- Define power regimes: `AC_LEGACY`, `AC_HYBRID_800VDC`, `NATIVE_800VDC`, `MV_TO_800VDC`.
- Define thermal regimes: `AIR_LEGACY`, `EVAP_AIR_LEGACY`, `LIQUID_D2C`, `LIQUID_CLOSED_LOOP_DRY`, `LIQUID_HYBRID_EVAP`, `LIQUID_CHILLED`.
- Model 800 VDC distribution, conversion, DC/DC and sidecar losses.
- Model direct-to-chip liquid cooling, TCS/CDU and facility cooling loop.
- Model dry cooler, chiller and optional external evaporative-assist heat rejection.
- Keep internal evaporative air cooling out of the high-density AI reference path; retain it for legacy/historical cases.
- Couple workload, electrical and thermal telemetry in replay/counterfactual scenarios.
- Compare at least two complete power/thermal topologies under identical workload/environment inputs.
- Benchmark conversion loss, cooling energy, water, thermal headroom, electrical risk, SLA risk and useful compute per facility kWh.
- Extend Evidence with topology, power-regime and thermal-regime provenance.
- Keep electrical protection, grounding, thermal interlock and leak/flow constraints behind the safety/policy boundary.

Supporting contract:

- `docs/POWER_THERMAL_800VDC.md`

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
- Power-thermal topology scenarios required by MV1.
- Historical cooling benchmark scenarios for Prineville, Google/DeepMind, Google London and Oracle context.

## S8 — Optimization

- Formal objective: energy cost + carbon + water + thermal risk + electrical risk + SLA risk + wear.
- Constraint registry.
- Rule, PID, MPC and MILP baselines.
- Dynamic setpoint candidate evaluation.
- Safety validator before recommendation/control.
- Power-thermal co-optimization benchmark before RL.

## S9 — DQN / RL

- Add an explicit data-engineering/feature-store stage before RL experiments.
- Port original DQN research into an isolated experiment package.
- Double/Dueling/target-network/Huber improvements as applicable.
- Compare against non-RL baselines including MV1 deterministic optimization.
- Reproducibility: seed, dataset version, environment version, metrics.

## S10 — Verification + Control

- POTENTIAL/PREDICTED/EXECUTED/VERIFIED savings lifecycle.
- Workload/weather/tariff normalization.
- Recommendation audit trail.
- Policy-gated actuation interface.
- Electrical and thermal safety verification.

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
| `docs/POWER_THERMAL_800VDC.md` | 800 VDC + liquid cooling power-thermal boundary | MV1 |
| `docs/THERMAL_OPTIMIZATION.md` | Thermal state, risk, TTU and dynamic setpoint optimization | MV0/S8 |
| `docs/THERMAL_PATTERNS_ASHRAE.md` | ASHRAE envelope and thermal-pattern semantics | MV0/S1 |
| `docs/HISTORICAL_COOLING_CASES.md` | Historical cooling/resilience benchmark context | MV0/S7 |
| `docs/AUDIT_REVALIDATION.md` | Snapshot finding lifecycle | Every external audit |
| `docs/OTTO_BRAND_SYSTEM.md` | Technical brand/operational states | Product/dev UX |

## Explicit non-goals

- No universal fixed setpoint.
- No vendor lock-in in the domain layer.
- No direct AI-to-actuator path.
- No unverified savings marketed as realized.
- No claim of Uptime Institute certification.
- No RL implementation before validated data/replay/non-RL baselines.
- No assumption that 800 VDC is universally optimal; it must be demonstrated by scenario evidence.
- No assumption that all data centers require liquid cooling; regime selection is explicit and workload/density dependent.
- No connector expansion without a documented ROI/use-case rationale.
