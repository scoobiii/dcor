# DCOR Benchmark

The benchmark evaluates ingestion, canonicalization, replay, baselines, thermal risk, optimization, safety and verification under a common contract.

## Benchmark pipeline

```text
ingestion → normalization → quality → replay
→ baseline → counterfactual → risk → optimization
→ safety → verification → performance
```

## Benchmark 001 — Cooling Envelope & Failure Resilience

### Objective

Determine whether DCOR can identify a safe and economically superior operating point while detecting approach to thermal/psychrometric failure.

### Scenarios

1. **Prineville control excursion:** outside-air/damper error + evaporative cooling + humidity/condensation.
2. **Google/DeepMind optimization:** predictive cooling optimization under constraints.
3. **Google London:** extreme outdoor heat + correlated cooling failures.
4. **High-density H1:** candidate setpoints constrained by the applicable H1 envelope.

### Candidate setpoint experiment

A facility may start from a 22 °C baseline and test candidate values upward/downward **only within the applicable policy envelope**. For H1, the 2021 ASHRAE reference is 18–22 °C recommended and 15–25 °C allowable. A 26–27 °C candidate is therefore rejected when H1 is the governing policy. citeturn0search1turn0search19

## Metrics

| Category | KPI |
|---|---|
| Energy | IT kWh, cooling kWh, facility kWh, PUE |
| Water | water volume, WUE |
| Carbon | kgCO2e with declared factor |
| Performance | useful work, throughput, latency, throttling |
| Thermal | inlet/return/supply T, ThermalMargin |
| Psychrometric | RH, dew point, DewPointMargin |
| Capacity | CoolingCapacityMargin |
| Risk | thermal risk probability/state, TTU |
| Resilience | available capacity, failed units, recovery time |
| SLA | violation probability/actual violations |
| Optimization | objective delta, rejected candidates |
| Verification | baseline-normalized actual delta |

## Required result record

Every result includes:

- commit/version;
- dataset/replay hash;
- policy version;
- equipment class;
- baseline definition;
- candidate action;
- predicted energy/water/carbon/performance/risk;
- constraints and rejection reasons;
- actual measurements when executed;
- verification state.

## Fair comparison

Same canonical semantics, time window, workload normalization, policy, acceptance criteria and hardware/runtime class are required for valid comparisons. Changing semantics to obtain a faster benchmark is not an optimization.

## Safety assertions

- unsafe candidates must be rejected;
- H1 26 °C must be rejected when H1 is active;
- decreasing `DewPointMargin` must increase condensation exposure;
- decreasing `CoolingCapacityMargin` must restrict feasible actions;
- forecasted boundary crossing must be detected before the static limit;
- predicted savings must never be labeled verified.

## Regression policy

Stable benchmark thresholds become CI gates only after repeatability is demonstrated. Every threshold is versioned and tied to the benchmark definition.
