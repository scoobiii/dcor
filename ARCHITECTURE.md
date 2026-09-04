# DCOR Architecture

## 1. Architectural principles

1. **Canonical contract first.** Every source is translated before entering domain services.
2. **Source independence.** Optimization, analytics and UI depend on canonical contracts, never on vendor APIs.
3. **Digital-twin parity.** Real telemetry and simulated/replayed telemetry use the same domain interfaces.
4. **Safety before actuation.** AI can propose an action; policy validation decides whether it can reach a controller.
5. **Evidence over claims.** Potential, predicted and verified savings are distinct states.
6. **Independent components.** DCOR is the platform/product identity; connectors, twin, optimizers and applications can version independently.
7. **Observable by default.** Every ingestion and optimization path exposes health, quality, latency and lineage.
8. **No dashboard-first development.** Presentation is downstream of the canonical model.

## 2. Logical architecture

```mermaid
flowchart TB
  subgraph SOURCES[External systems]
    F[Frontier telemetry]
    N[NLR/DOE]
    FILE[CSV/Parquet]
    MQTT[MQTT]
    REST[REST]
    BMS[BMS]
    DCIM[DCIM]
    SCADA[SCADA]
    EPMS[EPMS]
  end

  subgraph CONNECT[DCOR Connect]
    SDK[Connector SDK]
    DISC[Discovery]
    AUTH[Authentication]
    NORM[Normalize]
    VALID[Validate]
    HEALTH[Health + lineage]
  end

  subgraph DOMAIN[Canonical domain]
    MODEL[Canonical Data Model]
    QUALITY[Data Quality]
    STORE[Telemetry Store]
  end

  subgraph INTEL[Decision layer]
    TWIN[Digital Twin]
    BASE[Baseline / Counterfactual]
    ANA[Analytics]
    OPT[Optimizer]
    RL[DQN / RL]
  end

  subgraph CONTROL[Governed execution]
    POLICY[Policy + Safety Validator]
    REC[Recommendation]
    CTRL[Controller / Actuator]
    VERIFY[Savings Verification]
  end

  subgraph PRESENT[Consumers]
    API[API]
    DASH[Dashboard]
    FLEET[Fleet / SaaS]
  end

  SOURCES --> SDK --> DISC --> AUTH --> NORM --> VALID --> MODEL
  HEALTH -.-> SDK
  MODEL --> QUALITY --> STORE
  STORE --> TWIN
  STORE --> ANA
  TWIN --> BASE --> OPT
  ANA --> OPT
  OPT --> RL
  OPT --> POLICY
  RL --> POLICY
  POLICY --> REC --> VERIFY
  POLICY --> CTRL --> VERIFY
  STORE --> API --> DASH
  VERIFY --> API
  API --> FLEET
```

## 3. Dependency rule

```text
connectors -> canonical-model
canonical-model -> domain services
services -> packages
apps -> services/contracts
UI -> API/canonical DTOs

FORBIDDEN:
UI -> vendor connector
optimizer -> raw CSV column name
optimizer -> MQTT topic
optimizer -> BMS-specific register
```

## 4. Connector contract

Every connector implements the same lifecycle:

- `connect()`
- `authenticate()`
- `discover()`
- `read()`
- `normalize()`
- `validate()`
- `health()`
- `disconnect()`

The SDK owns orchestration and error semantics. Adapters own source-specific protocol details.

## 5. Canonical data path

`source record → adapter → canonical telemetry → quality gate → lineage → storage → analytics/twin → optimization → policy → recommendation/control → verification`

A failed quality gate does not silently become a trusted measurement. Missing, duplicated, stale, impossible or unit-inconsistent data carries explicit quality metadata.

## 6. Safety model

```mermaid
sequenceDiagram
  participant O as Optimizer
  participant P as Policy Validator
  participant C as Controller
  participant M as Measurement
  participant V as Verification

  O->>P: Proposed action + rationale + expected impact
  P->>P: Thermal / power / equipment / SLA / policy checks
  alt approved
    P->>C: Authorized action
    C->>M: System response
    M->>V: Actual telemetry
    V->>V: Baseline-adjusted verification
  else rejected
    P-->>O: Rejection + violated constraints
  end
```

## 7. Savings states

- `POTENTIAL`: theoretical opportunity from current baseline.
- `PREDICTED`: model-estimated result before execution.
- `EXECUTED`: action was accepted and applied.
- `VERIFIED`: measured outcome after normalization against baseline, workload, weather and tariff/operational conditions.

Only `VERIFIED` savings are presented as realized savings.

## 8. Multi-tenant boundary

`Tenant → Facility → Asset hierarchy → Telemetry → Analytics/Twin → Optimization → Policies → Users/Roles`.

Tenant identifiers must be present in persisted domain records and enforced at service boundaries. Cross-tenant reads are denied by default.

## 9. Deployment evolution

Phase 1: local Python packages + fixtures.

Phase 2: containerized connector/telemetry services.

Phase 3: event-driven ingestion + durable telemetry storage.

Phase 4: production SaaS, fleet orchestration and controlled actuation.

The domain contract remains stable across phases.
