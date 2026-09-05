# DCOR MV1 — 800 VDC + Liquid Cooling Power-Thermal Architecture

## Purpose

`MV1` defines the next product-value frontier after MV0: **verifiable co-optimization of electrical distribution and thermal infrastructure for high-density AI data centers**.

The architectural premise is that power and cooling cannot be optimized independently at extreme rack density. 800 VDC changes the electrical distribution topology while direct-to-chip liquid cooling changes the thermal path; both affect losses, capacity, reliability, operating envelope and optimization opportunities.

This document is an architecture boundary, not a claim that every deployment must use 800 VDC or liquid cooling.

## External industry context

The industry is actively standardizing 800 VDC for next-generation AI data centers. OCP reports that Google, Microsoft and NVIDIA are working through OCP toward common 800 VDC requirements, interfaces, power quality and safety frameworks. NVIDIA describes 800 VDC as a path to fewer conversion stages and lower distribution losses. Schneider and Eaton describe the associated transition toward higher-density racks and liquid cooling, including cooling implications for power infrastructure itself.

DCOR therefore treats 800 VDC as a **reference optimization regime**, not as a vendor-specific implementation.

## Reference thermal/electrical topology

```text
                         GRID / MV
                            |
                    MV -> 800 VDC
                 SST / rectifier / UPS
                            |
                       800 VDC BUS
                            |
             +--------------+--------------+
             |                             |
        IT POWER RACK                 POWER SIDEcar
             |                             |
          DC/DC                         losses
             |                             |
       GPU / CPU / NIC              optional cooling
             |
      DIRECT-TO-CHIP LIQUID
             |
          TCS / CDU
             |
      FACILITY COOLING LOOP
             |
       HEAT REJECTION
        /      |       \
   DRY COOLER CHILLER  EVAP-ASSIST
```

The initial reference architecture assumes **liquid as the primary thermal path for high-density AI compute**. It does not assume internal evaporative air cooling as the primary GPU thermal path.

External evaporative assistance remains an optional heat-rejection strategy where climate, water availability, operating cost and reliability make it Pareto-optimal.

## Thermal regimes

| Regime | Primary IT thermal path | Heat rejection | DCOR role |
|---|---|---|---|
| `AIR_LEGACY` | air | air-side / chilled air | compatibility / historical |
| `EVAP_AIR_LEGACY` | air + evaporative | evaporative air-side | historical/legacy benchmark |
| `LIQUID_D2C` | direct-to-chip liquid | dry cooler / chiller / hybrid | primary AI reference |
| `LIQUID_CLOSED_LOOP_DRY` | closed liquid loop | dry cooler | preferred low-water reference |
| `LIQUID_HYBRID_EVAP` | closed liquid loop | dry cooler + evaporative assist | conditional optimization |
| `LIQUID_CHILLED` | closed liquid loop | chiller plant | constrained climate/temperature regime |

The regime must be explicit in the canonical facility/asset model. Optimizers must never infer it from a vendor name or an undocumented convention.

## Power regimes

| Regime | Distribution | Optimization concern |
|---|---|---|
| `AC_LEGACY` | facility AC + rack conversion | conversion/distribution losses |
| `AC_HYBRID_800VDC` | AC upstream + 800 VDC sidecar | retrofit efficiency and sidecar heat |
| `NATIVE_800VDC` | centralized 800 VDC | conversion, protection, storage, bus utilization |
| `MV_TO_800VDC` | MV direct conversion to 800 VDC | conversion efficiency, protection, fault response |

DCOR must model the actual topology rather than assuming a single 800 VDC implementation.

## Coupled optimization problem

The objective is not simply `PUE ↓` or `cooling power ↓`.

```text
minimize

  energy_cost
+ carbon_cost
+ water_cost
+ conversion_loss
+ cooling_energy
+ thermal_risk
+ electrical_risk
+ SLA_risk
+ equipment_wear

subject to

  800 VDC voltage/current limits
  protection and grounding constraints
  DC/DC operating envelope
  rack power limit
  GPU/CPU thermal limits
  coolant supply/return limits
  CDU/TCS flow and capacity
  heat-rejection capacity
  weather envelope
  water availability
  redundancy / resilience requirements
  workload/SLA constraints
```

## Canonical measurements

MV1 extends the canonical telemetry vocabulary conceptually with:

### Electrical

- bus voltage;
- bus current;
- rack power;
- conversion efficiency;
- DC/DC input/output voltage;
- DC/DC temperature;
- sidecar power and losses;
- protection state;
- energy storage state where applicable.

### Thermal

- chip/package temperature;
- coolant supply temperature;
- coolant return temperature;
- flow rate;
- pressure;
- CDU load;
- TCS load;
- facility loop temperature;
- dry-cooler fan/pump power;
- chiller power;
- evaporative-assist state;
- ambient dry-bulb/wet-bulb conditions.

### Workload

- accelerator utilization;
- compute throughput;
- workload class;
- batch/inference state;
- power cap;
- tokens/s or equivalent useful-work metric where applicable.

All measurements remain subject to the canonical quality and lineage contract.

## Agents

MV1 adds a coupled agent topology to the existing DCOR Agent Fabric:

```text
Supervisor Agent
      |
 +----+----+---------+---------+---------+
 |         |         |         |         |
Power   Thermal   Workload  Weather   Safety
Agent    Agent     Agent     Agent     Agent
 |         |         |         |         |
 +---------+---------+---------+---------+
                    |
             Optimization Agent
                    |
             Verification Agent
```

Agents reason and coordinate; they are **not the source of truth**. Canonical telemetry, configuration, policy and Evidence remain authoritative.

No direct agent-to-actuator path is introduced by MV1.

## Counterfactual scenarios

The replay/twin layer must be able to compare at least:

1. current AC + current cooling;
2. AC + liquid cooling;
3. hybrid AC/800 VDC + liquid cooling;
4. 800 VDC + liquid cooling + dry cooler;
5. 800 VDC + liquid cooling + evaporative-assisted heat rejection;
6. alternative setpoints and workload power caps.

The scenario engine must preserve identical workload and environmental inputs when comparing alternatives.

## Evidence

MV1 uses the existing Evidence contract and adds the requirement that optimization evidence identify both electrical and thermal configuration.

Minimum evidence dimensions:

```text
optimization_id
topology_id
power_regime
thermal_regime
baseline
prediction
action
constraints
actual
normalization
energy_delta
conversion_loss_delta
cooling_energy_delta
cost_delta
carbon_delta
water_delta
thermal_impact
electrical_impact
sla_impact
confidence
verification_status
lineage
```

A predicted improvement in conversion loss is not a verified facility saving. Verification requires measured telemetry and appropriate normalization.

## Benchmark

MV1 benchmarks:

- electrical conversion efficiency;
- distribution loss;
- cooling energy;
- water consumption;
- thermal headroom;
- power-quality events;
- constraint violations;
- useful compute per facility kWh;
- tokens per facility kWh where a token metric is meaningful;
- CAPEX/OPEX/TCO where scenario data supports it;
- optimization latency and reproducibility.

PUE remains useful, but it is insufficient as the sole optimization KPI for high-density AI infrastructure.

## Safety boundaries

800 VDC is a high-energy electrical domain. DCOR must not autonomously modify protection, grounding, isolation, fault-clearing or energization settings.

Liquid cooling is also a safety-critical physical system. DCOR must not autonomously bypass leak detection, flow protection, temperature limits, pressure limits or equipment interlocks.

All recommendations affecting physical infrastructure pass through the existing policy/safety validator.

## Implementation sequence

```text
S3 Frontier
   ↓
MV0 First Verifiable Optimization
   ↓
MV1 Power-Thermal Model
   ↓
800 VDC topology model
   ↓
Liquid cooling topology model
   ↓
Coupled replay/counterfactual
   ↓
Deterministic optimization
   ↓
Evidence + verification
   ↓
RL only after validated baseline
```

## Non-goals

- No assumption that 800 VDC is universally superior without scenario evidence.
- No vendor-specific 800 VDC lock-in in the domain model.
- No claim that all existing data centers should replace air cooling.
- No direct electrical or thermal actuation from an AI agent.
- No RL-first implementation.
- No unverified energy, water or cost savings.

## Exit criteria for MV1

MV1 can become `DONE` only when DCOR can replay a representative high-density workload and produce a deterministic, machine-readable comparison of at least two power/thermal topologies, with constraints, lineage, predicted impact and post-execution verification represented by the Evidence contract.
