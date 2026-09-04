# DCOR — Data Center Optimization & Reduction

**Connect. Measure. Simulate. Optimize. Verify.**

DCOR is a vendor-neutral platform for data-center energy, cooling, cost, carbon and operational optimization. **DCOR is the product/platform name; connectors, services and optimization engines are independently evolvable components.**

> **SCADA shows. DCIM organizes. BMS controls. DCOR explains, simulates, optimizes and verifies.**

## Product boundary

DCOR does not replace SCADA, BMS, DCIM or EPMS. It consumes their telemetry through connectors, converts heterogeneous data into a canonical contract, builds a digital-twin/counterfactual view, evaluates baselines, optimizes within safety and operational policies, and verifies realized savings.

The optimization layer is deliberately downstream of the data contract. **The dashboard is not the starting point.** UI components consume canonical data and must not encode vendor-specific telemetry assumptions.

## Architecture

```mermaid
flowchart LR
  S[SCADA / BMS / DCIM / EPMS / Sensors] --> C[DCOR Connect]
  C --> N[Canonical Data Model]
  N --> Q[Data Quality + Lineage]
  Q --> O[DCOR Observe]
  Q --> T[DCOR Twin]
  T --> A[DCOR Analytics]
  A --> B[Baseline / Counterfactual]
  B --> Z[DCOR Optimize]
  Z --> V[Safety / Policy Validator]
  V --> R[Recommendation / Control]
  R --> X[DCOR Verify]
  X --> D[API / Dashboard / Fleet]
```

## Delivery monitor

The table below is the **living delivery contract**. Every sprint is advanced only after its implementation, tests and validation are committed and pushed. The CI workflow runs on every push and records the state of the repository. GitHub Actions supports push-triggered workflows, matrix jobs and status badges. citeturn0search5turn0search2turn0search0

| Sprint | Scope | Status | Exit evidence |
|---|---|---|---|
| S0 | Baseline, audit, reproducibility, CI skeleton | **IN PROGRESS** | audit + CI + tests |
| S1 | Clean Architecture + canonical contracts | **PLANNED** | architecture + schema tests |
| S2 | Universal Connector SDK | **IN PROGRESS** | SDK + contract tests |
| S3 | Frontier connector | **PLANNED** | adapter + fixture + validation |
| S4 | NLR/DOE connector | **PLANNED** | adapter + fixture + validation |
| S5 | CSV/Parquet connector | **PLANNED** | ingestion + normalization tests |
| S6 | MQTT + REST connectors | **PLANNED** | protocol contract tests |
| S7 | Digital Twin + baseline | **PLANNED** | replay/counterfactual benchmark |
| S8 | Optimization engines | **PLANNED** | Rule/PID/MPC/MILP benchmarks |
| S9 | DQN / modern RL | **PLANNED** | reproducible RL benchmark |
| S10 | Savings verification + safety/control | **PLANNED** | verified savings + policy gates |
| S11 | SaaS, fleet, observability, production hardening | **PLANNED** | release gate + production checklist |

**Rule:** a sprint is not marked complete because code exists. It requires implementation + automated tests + CI validation + documented exit evidence.

### Commit/push protocol

- `feat(s0): establish dcor baseline and delivery contract`
- `feat(s1): define architecture and canonical model`
- `feat(s2): implement connector sdk`
- `feat(s3): add frontier connector`
- …
- `feat(s11): production hardening and release gate`

Each push to `main` executes the CI gate. Test/build outputs may be retained as workflow artifacts for diagnosis and auditing. citeturn0search1

## First canonical telemetry contract

The platform normalizes source-specific records into a stable envelope. Source lineage is preserved; the optimization domain does not depend on the source protocol.

```json
{
  "timestamp": "2026-09-04T15:00:00Z",
  "facility_id": "dc-001",
  "metric": "it_power_kw",
  "value": 842.3,
  "unit": "kW",
  "source": "example",
  "quality": "GOOD",
  "confidence": 1.0,
  "lineage": {"connector": "example", "record_id": "r-001"}
}
```

See [Canonical Data Model](docs/CANONICAL_DATA_MODEL.md).

## Connector roadmap

Priority implementation order:

1. Frontier telemetry
2. NLR/DOE PUE telemetry
3. CSV / Parquet
4. MQTT
5. REST
6. Additional BMS/DCIM/SCADA/EPMS adapters

The first five are adapters over the same Connector SDK and canonical contract.

## Research and optimization

The original Deep Q-Learning work is retained as research input rather than as the platform architecture. Optimization will be benchmarked in this order:

**baseline → rules → PID/MPC/MILP → DQN → Double/Dueling DQN → PPO/SAC**, with workload, thermal, equipment, SLA, cost, carbon and water constraints represented explicitly.

## Standards and governance

See [ARCHITECTURE.md](ARCHITECTURE.md), [STANDARDS.md](STANDARDS.md) and [BACKLOG.md](BACKLOG.md).

## Repository layout

```text
apps/                 deployable applications
services/             domain services
packages/             stable contracts and reusable libraries
connectors/           source/protocol adapters
digital-twin/         simulation and replay
datasets/             manifests/fixtures, not uncontrolled data dumps
research/              research adapters and experiments
hardware-lab/          physical/edge experiments
docs/                  architecture, standards and runbooks
benchmarks/            scientific comparisons
tests/                 cross-component tests
infra/                  deployment and operations
.github/workflows/     CI gates
```

## Status

This repository intentionally starts with the contract and ingestion layer. **Do not build the dashboard ahead of the canonical data model.**
