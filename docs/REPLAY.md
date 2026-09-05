# DCOR Replay

Replay is the deterministic bridge between historical telemetry and optimization experiments.

## Replay contract

A replay manifest identifies:

- source/dataset identifier;
- content hash;
- time window/timezone;
- canonical schema version;
- quality policy;
- facility/equipment policy;
- workload/weather context;
- random seed when applicable;
- software/commit version.

## Thermal replay

Replay scenarios must be able to vary:

- outdoor temperature/RH;
- indoor temperature/RH;
- dew point and surface temperature;
- IT thermal load and density;
- cooling capacity and failed units;
- setpoint/control actions;
- workload/performance;
- SLA policy.

This enables counterfactual questions such as:

> Could the setpoint increase by 1 °C while retaining the required thermal margin and SLA risk?

## Determinism

For a fixed manifest/version, replay should produce equivalent canonical inputs within declared numerical tolerances. Any stochastic component records its seed and environment.

## Safety

Replay may simulate unsafe candidates to test the validator. Simulation of an unsafe state is not authorization to execute it.

## Verification

Replay results can establish prediction/regression evidence. Realized savings require measured execution data and baseline-adjusted verification.
