# DCOR Backlog — S0 to S11 + MV0

## Delivery gate

Every milestone requires **implementation → tests → CI validation → evidence/documentation**.

## Product-value gate

**MV0 — First Verifiable Optimization** proves the thesis before advanced RL/control/SaaS.

| Milestone | Deliverable | Status |
|---|---|---|
| S0 | Audit, baseline, repository contract, CI | IN PROGRESS |
| S1 | Architecture, standards, canonical contracts | IN PROGRESS |
| S2 | Universal Connector SDK | IN PROGRESS |
| S3 | Frontier connector | PLANNED |
| **MV0** | Verifiable optimization + thermal risk | PLANNED |
| S4 | NLR/DOE | PLANNED |
| S5 | CSV/Parquet | PLANNED |
| S6 | MQTT + REST | PLANNED |
| S7 | Twin + baseline | PLANNED |
| S8 | Rules/PID/MPC/MILP | PLANNED |
| S9 | DQN/RL | PLANNED |
| S10 | Verification + governed control | PLANNED |
| S11 | SaaS/fleet/production | PLANNED |

## New cross-cutting work — Thermal Intelligence

### T1 — Thermal state contract

Add temperature, RH, dew point, wet bulb, surface temperature, IT load, cooling capacity, redundancy, setpoint, workload and performance fields where available.

### T2 — Risk envelope

Implement `ThermalMargin`, `DewPointMargin`, `CoolingCapacityMargin`, `SLA_Risk` and `TTU` with versioned policies.

### T3 — Economic setpoint optimizer

Evaluate candidate control actions rather than treating 22 °C or 27 °C as universal constants. Objective: useful work per combined resource/risk cost.

### T4 — Historical benchmark

Implement Benchmark 001 with Prineville, Google/DeepMind, Google London and high-density H1 scenarios.

### T5 — Safety gate

Reject actions outside OEM/commissioning/facility policy or applicable equipment-class envelope. No AI-to-actuator bypass.

## Existing S8 optimization requirement

The optimizer objective must include energy, water, carbon, monetary cost, thermal risk, SLA risk and equipment wear where data supports them. PUE remains a KPI, not the sole objective.

## Research order

`baseline → rules → PID/MPC/MILP → DQN → Double/Dueling DQN → PPO/SAC`.

RL remains downstream of validated data, replay, baseline and safety gates.

## Explicit non-goals

- universal fixed setpoint;
- dashboard-first development;
- vendor lock-in in domain contracts;
- direct AI-to-actuator path;
- unverified savings marketed as realized;
- Uptime certification claim;
- RL before validated foundations.
