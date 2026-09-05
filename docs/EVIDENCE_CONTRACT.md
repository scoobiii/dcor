# DCOR Evidence Contract

The Evidence Contract is the machine-readable boundary between an optimization claim and the evidence required to reproduce it.

## Principle

DCOR must distinguish:

```text
POTENTIAL → PREDICTED → EXECUTED → VERIFIED
```

An optimization result is not a verified saving merely because an optimizer predicted a reduction.

## Evidence envelope

```yaml
optimization_id: <stable identifier>
timestamp: <UTC timestamp>
facility_id: <canonical facility identifier>
baseline:
  definition: <baseline method/version>
  interval: <start/end>
  energy_kwh: <value>
prediction:
  method: <optimizer/version>
  energy_delta_kwh: <value>
  percent: <value>
action:
  type: <recommendation|setpoint|schedule|other>
  parameters: <canonical action parameters>
constraints:
  thermal: <pass/fail + values>
  equipment: <pass/fail + values>
  capacity: <pass/fail + values>
  sla: <pass/fail + values>
  policy: <pass/fail + values>
actual:
  interval: <start/end>
  energy_kwh: <value>
normalization:
  workload: <method/version>
  weather: <method/version>
  tariff: <method/version>
energy_delta:
  kwh: <value>
  percent: <value>
cost_delta:
  currency: <ISO-4217>
  amount: <value>
carbon_delta:
  kg_co2e: <value>
water_delta:
  liters: <value>
thermal_impact:
  max_delta_c: <value>
sla_impact:
  status: <pass/fail/unknown>
confidence: <0..1>
verification_status: <POTENTIAL|PREDICTED|EXECUTED|VERIFIED|REJECTED>
lineage:
  source: <source identifier>
  connector: <connector identifier>
  schema_version: <version>
  dataset_version: <version>
  replay_id: <replay identifier>
  code_version: <commit/package version>
```

## Required invariants

1. `optimization_id` is unique within the evidence namespace.
2. `timestamp` is timezone-aware and normalized to UTC.
3. `facility_id` resolves to the canonical facility identity.
4. Baseline, prediction and actual intervals are explicit.
5. Prediction cannot be labeled `VERIFIED`.
6. `VERIFIED` requires actual observations and declared normalization.
7. Constraint evaluation occurs before an action can be recommended for execution.
8. Lineage must identify the source, connector and calculation version.
9. Missing evidence fields must be represented as unknown/null according to the schema, never silently invented.
10. Numeric deltas must state their direction and unit unambiguously.

## Verification rule

For energy savings, the conceptual calculation is:

```text
verified_delta = normalized_baseline_energy - actual_energy
verified_percent = verified_delta / normalized_baseline_energy
```

The exact normalization method is part of the evidence and must be versioned. Workload, weather, tariff and other materially relevant conditions must not be silently ignored.

## Reproducibility

An evidence record must be sufficient to locate:

- the canonical input records;
- the replay manifest;
- the baseline implementation/version;
- the optimizer implementation/version;
- the constraint/policy version;
- the normalization method/version;
- the resulting calculation.

## Security and integrity

Evidence must not contain secrets, credentials or uncontrolled personal data. Production implementations should additionally support content hashes or immutable artifact identifiers so evidence can be integrity-checked after publication.
