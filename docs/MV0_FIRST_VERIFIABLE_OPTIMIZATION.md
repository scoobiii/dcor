# MV0 — First Verifiable Optimization

MV0 is the first product-level vertical slice. It exists to prove the DCOR thesis with reproducible evidence before the project expands into advanced optimization, RL, control or SaaS.

## Product promise

> **Observe → Measure → Simulate → Optimize → Verify**

The vertical slice must turn a real or public telemetry source into a measurable optimization opportunity and preserve enough evidence to reproduce the result.

## Pipeline

```text
Frontier telemetry
      ↓
Canonical model
      ↓
Quality + lineage
      ↓
Recorded replay
      ↓
Baseline
      ↓
Counterfactual
      ↓
Optimization candidate
      ↓
Safety / policy validation
      ↓
Prediction
      ↓
Verification
      ↓
Evidence artifact
```

## Minimum scope

MV0 is intentionally narrower than the full S0–S11 roadmap.

| Capability | Required for MV0 |
|---|---|
| Source | Frontier public telemetry |
| Contract | DCOR canonical telemetry |
| Quality | missing/duplicate/stale/sanity checks applicable to source |
| Lineage | source record + connector/schema version |
| Replay | deterministic recorded input |
| Baseline | explicit baseline definition and interval |
| Counterfactual | measurable alternative operating point |
| Optimization | at least one deterministic non-RL method |
| Safety | constraints evaluated before recommendation |
| Verification | actual vs baseline after normalization |
| Evidence | machine-readable Evidence Contract |

## Required output

A successful MV0 run must produce:

1. canonical telemetry records;
2. source and schema lineage;
3. quality report;
4. replay manifest;
5. baseline metrics;
6. counterfactual metrics;
7. optimization candidate and constraints;
8. predicted delta;
9. verification status;
10. evidence artifact linking all inputs and calculations.

Example presentation values are illustrative only; they must never be represented as measured Frontier results unless produced by the pipeline:

```text
IT Power             842.3 kW
Cooling Power        201.4 kW
Total Power        1,043.7 kW
PUE                   1.239
Baseline PUE          1.251
Optimized PUE         1.207
Predicted saving      3.52%
Verified saving       TBD
```

## Acceptance criteria

- [ ] Frontier source schema is documented.
- [ ] Adapter emits only canonical records.
- [ ] Every emitted record preserves lineage.
- [ ] Replay of the same fixture is deterministic.
- [ ] Quality failures are observable and counted.
- [ ] Baseline calculation is deterministic for a fixed input/version.
- [ ] Counterfactual calculation is reproducible.
- [ ] Optimization never bypasses the safety/policy boundary.
- [ ] Predicted and verified savings are separate states.
- [ ] Evidence can reconstruct the calculation without relying on an interactive notebook.
- [ ] CI validates the complete vertical slice.

## Non-goals

- No DQN/PPO/SAC requirement.
- No direct actuator control.
- No dashboard dependency.
- No uncontrolled external dataset copy into the repository.
- No claim of realized savings without verification.

## Definition of done

MV0 is `DONE` only when implementation, tests, CI validation and evidence are all present. The README may link to the resulting reproducible example once the CI gate has validated it.
