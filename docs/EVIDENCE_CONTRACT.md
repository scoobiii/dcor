# DCOR Evidence Contract

Evidence makes optimization claims reproducible and auditable.

## Outcome states

```text
POTENTIAL → PREDICTED → EXECUTED → VERIFIED
```

States are not interchangeable. `PREDICTED` is not realized savings; `EXECUTED` only proves an action was applied; `VERIFIED` requires measured, normalized outcome evidence.

## Required provenance

Each optimization candidate records:

- source/replay identifier;
- canonical schema version;
- state timestamp and window;
- baseline version;
- policy/equipment-class version;
- candidate action/setpoint;
- model/optimizer version;
- predicted energy/water/carbon/performance/risk;
- constraint values and rejection reasons;
- uncertainty/confidence.

Executed candidates additionally record observed telemetry and verification calculations.

## Thermal evidence

For thermal optimization, evidence must preserve:

`ThermalMargin`, `DewPointMargin`, `CoolingCapacityMargin`, `TTU`, risk state, applicable limits, setpoint and equipment class.

A result must be traceable from the decision back to the raw/canonical measurements and policy that constrained it.

## Historical evidence

Historical public benchmarks must retain source date and provenance. Current operational values cannot be inferred from historical reports.

## Verification rule

A verified result requires a declared baseline and normalization methodology covering applicable workload, weather, tariff and operating conditions. Missing evidence downgrades the result to `UNKNOWN` or non-verified status; it is never silently estimated.
