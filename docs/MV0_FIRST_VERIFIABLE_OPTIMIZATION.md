# MV0 — First Verifiable Optimization

MV0 proves the DCOR product thesis before advanced RL/control/SaaS complexity.

## Product promise

> **Observe → Measure → Simulate → Predict Risk → Optimize → Verify**

## Pipeline

```text
source → canonical → quality/lineage → replay
→ baseline → counterfactual → thermal/performance risk
→ candidate actions → safety/policy → prediction
→ execution/replay → verification → evidence
```

## Minimum scope

| Capability | Required |
|---|---|
| Source | Frontier public telemetry |
| Contract | canonical telemetry |
| Quality | applicable missing/duplicate/stale/sanity checks |
| Lineage | source + connector/schema/version |
| Replay | deterministic |
| Baseline | explicit/versioned |
| Counterfactual | measurable alternative operating point |
| Risk | thermal + capacity + SLA margins |
| Optimization | deterministic non-RL baseline |
| Safety | policy validation before action |
| Verification | normalized actual vs baseline |
| Evidence | machine-readable provenance |

## Thermal acceptance criteria

- [ ] `ThermalMargin` is computed from predicted state, not only current temperature.
- [ ] `DewPointMargin` is evaluated whenever condensation is relevant.
- [ ] `CoolingCapacityMargin` is evaluated before candidate approval.
- [ ] `TTU` identifies forecasted safe-set crossing where possible.
- [ ] equipment class/policy is explicit; generic ASHRAE values are not universalized.
- [ ] candidate setpoint is represented as a control action.
- [ ] performance floor is enforced.
- [ ] rejected candidates include machine-readable reasons.

## Setpoint experiment

A baseline may use 22 °C, but MV0 must not assume it is optimal. Candidate evaluation is policy-bounded and includes energy, water, carbon, performance, risk and cost.

For H1 high-density air-cooled equipment, the 2021 ASHRAE reference is 18–22 °C recommended and 15–25 °C allowable. Therefore 26–27 °C is outside the H1 allowable range and must be rejected if H1 is the active policy. citeturn0search1turn0search19

## Required outputs

1. canonical records;
2. quality and lineage report;
3. replay manifest;
4. baseline;
5. counterfactual;
6. thermal/performance risk report;
7. candidate actions and policy decisions;
8. predicted delta;
9. verification status;
10. evidence artifact.

## Non-goals

- no DQN/PPO/SAC requirement;
- no direct actuator control;
- no dashboard dependency;
- no uncontrolled dataset copy;
- no realized-savings claim without verification.

## Definition of done

MV0 is DONE only when implementation, tests, CI and reproducible evidence all exist.
