# DCOR Standards & Reference Framework

DCOR uses standards as **constraints, interoperability references and evidence metadata**. It does not certify a facility, Uptime Tier or regulatory compliance.

## Thermal reference hierarchy

The thermal policy hierarchy is:

```text
OEM / equipment specification
        ↓
commissioning / facility operating policy
        ↓
applicable ASHRAE equipment class
        ↓
DCOR optimization envelope
```

A stricter facility/OEM limit wins. DCOR must never interpret a generic ASHRAE allowable range as permission to operate every device at that boundary.

### ASHRAE and setpoints

ASHRAE Thermal Guidelines are environmental guidance, not a single universal setpoint. The 2021 fifth edition introduced **H1** for high-density air-cooled servers. H1 uses a recommended **18–22 °C** range and an allowable **5–25 °C** dry-bulb range, with a maximum dew point of 17 °C and the applicable noncondensing humidity envelope. General A-class envelopes remain separate. citeturn0search1turn0search12

ASHRAE's current TC 9.9 Datacom Encyclopedia, evolved from the Datacom Series in 2024, is now the online repository for updated content; the fifth-edition thermal guidance remains the explicit source for the 2021 equipment table reproduced in the current Handbook Chapter 20. citeturn0search6turn0search1

DCOR therefore records separately:

- `recommended_min/max`;
- `allowable_min/max`;
- `max_dew_point`;
- `max_rh`;
- `max_temperature_rate_of_change`;
- `facility_setpoint`;
- `optimizer_candidate_setpoint`;
- `OEM_limit`;
- `commissioning_limit`;
- `policy_limit`.

**Never collapse these into one `setpoint` field.**

## Reference matrix

| Reference | DCOR use |
|---|---|
| ASHRAE TC 9.9 Thermal Guidelines | thermal/environmental envelopes, humidity/dew point and high-density equipment context |
| ASHRAE 2021 H1 | high-density air-cooled thermal reference |
| ASHRAE TC 9.9 Datacom Encyclopedia | current online TC 9.9 guidance and versioned reference metadata |
| ASHRAE 90.4 | data-center energy efficiency and facility-system requirements |
| Uptime Institute Tier | resilience context, never certification |
| ISO 50001 | energy management and continuous improvement concepts |
| The Green Grid PUE | facility-vs-IT efficiency KPI |
| The Green Grid WUE | water-efficiency KPI |
| CUE / carbon accounting | carbon-impact KPI |
| IEEE energy/data-center work | energy measurement, optimization, digital-twin and interconnection context |

## Thermal engineering rules

1. Temperature alone is insufficient; include humidity/dew point when condensation is relevant.
2. Use `DewPointMargin = T_surface - T_dewpoint` for condensation exposure.
3. Treat temperature and humidity as trajectories, not only instantaneous values.
4. Preserve applicable class-specific rate-of-change constraints; do not create a global ASHRAE dT/dt limit.
5. Use forecasted temperature and load to calculate `ThermalMargin` and `TTU`.
6. Model cooling capacity and redundancy explicitly.
7. A setpoint change is a control action, not merely a reporting field.
8. Validate fan/pump/compressor consequences; cooling savings can be offset by IT or auxiliary power.
9. Preserve uncertainty and data quality through every calculation.

## Recommended vs allowable vs optimum

```text
ASHRAE RECOMMENDED
        !=
ASHRAE ALLOWABLE
        !=
FACILITY POLICY
        !=
OEM LIMIT
        !=
OPTIMIZER CANDIDATE
        !=
ECONOMIC OPTIMUM
```

A candidate is admissible only when every applicable constraint is satisfied. Operation near an allowable boundary is a risk-managed operating decision, not evidence of optimality.

## Energy, water and carbon

PUE, WUE and carbon are derived KPIs with explicit boundaries, intervals and source lineage. They must never be inferred from incomplete measurements without an explicit quality state.

## Resilience

DCOR treats extreme weather, psychrometric excursions and correlated cooling failures as first-class scenarios. Redundancy does not imply zero common-mode risk.

## Data integrity

Canonical measurements carry timestamp, unit, quality, confidence and lineage. Processing must account for timezone, clock drift, duplicates, missing intervals, impossible values and sensor health.

## Source governance

Every production constraint must identify its source/reference and version. Standards change; hardcoded undocumented assumptions are prohibited.

## Current authoritative references

- ASHRAE TC 9.9 thermal guidance and data-center resources. citeturn0search6turn0search4
- ASHRAE Handbook—HVAC Applications, Chapter 20, current online thermal table. citeturn0search1
- ASHRAE 2021 Thermal Guidelines reference card. citeturn0search12
- Google DeepMind cooling optimization evidence. citeturn0search0turn0search3
