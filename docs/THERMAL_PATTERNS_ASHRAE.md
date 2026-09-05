# DCOR — ASHRAE Thermal Patterns & Environmental Envelope

## Purpose

This document translates the current public ASHRAE TC 9.9 thermal guidance into an explicit DCOR documentation contract for **temperature, humidity, dew point and rate-of-change patterns**.

It is intentionally separate from `docs/THERMAL_OPTIMIZATION.md`: that document defines optimization and risk logic; this document defines the **reference envelope and temporal-pattern semantics** used as constraints and evidence metadata.

## 1. Authoritative baseline

The current public baseline for the thermal equipment envelope is **ASHRAE Thermal Guidelines for Data Processing Environments, Fifth Edition (ASHRAE 2021)**, with the revised reference card published by ASHRAE. ASHRAE's current TC 9.9 Datacom Encyclopedia, evolved from the Datacom Series in 2024, is the online home for updated and frequently maintained content. The 5th-edition guidance remains the version explicitly identified in the current ASHRAE Handbook Chapter 20 as the source of the 2021 thermal table.

References:

- ASHRAE TC 9.9, *Thermal Guidelines for Data Processing Environments*, Fifth Edition, 2021.
- ASHRAE TC 9.9 Reference Card, Fifth Edition, revised/expanded.
- ASHRAE Handbook—HVAC Applications, Chapter 20, *Data Centers and Telecommunication Facilities*.
- ASHRAE TC 9.9 Datacom Encyclopedia for subsequently updated online content.

DCOR must store the **reference name, edition/version, publication date and retrieval date** with any constraint derived from ASHRAE.

## 2. Temperature envelope is class-specific

ASHRAE does not define one universal data-center temperature setpoint.

For the 2021 equipment guidance:

| Class | Recommended dry-bulb | Allowable dry-bulb | Max dew point | Max RH at upper dew-point boundary |
|---|---:|---:|---:|---:|
| A1–A4 | 18–27 °C | class-dependent | A1 17 °C; A2 21 °C; A3/A4 24 °C | A1/A2 80%; A3 85%; A4 90% |
| H1 | 18–22 °C | 5–25 °C | 17 °C | 80% |

The table is an **equipment environmental envelope**, not a prescription that a facility should operate at the midpoint or at the maximum allowable boundary.

H1 is specifically for high-density air-cooled equipment. High-powered CPUs, GPUs and dense memory can require increased cooling and may justify separate environmental controls.

Source: ASHRAE Handbook Chapter 20, Table 1, which reproduces the 2021 Thermal Guidelines equipment specifications. citeturn0search1turn0search12

## 3. Relative humidity is not sufficient by itself

DCOR must not use a rule such as:

```text
RH < X% => safe
RH >= X% => unsafe
```

Humidity constraints are coupled to temperature and dew point. The relevant state is psychrometric.

Minimum derived variables when inputs permit:

```text
T_dry_bulb
RH
T_dewpoint
T_wetbulb
T_surface
DewPointMargin
```

For condensation exposure:

```text
DewPointMargin = T_surface - T_dewpoint
```

and:

```text
T_surface <= T_dewpoint  => condensation boundary crossed
```

DCOR should maintain a positive policy-defined margin rather than treating the mathematical boundary as an operating target.

## 4. The 90% RH issue

The ASHRAE A4 allowable envelope permits up to **90% RH at a maximum 24 °C dew point**, subject to the complete environmental envelope and noncondensing condition. This does **not** mean that 90% RH is universally safe, nor that 90% RH implies condensation.

At high RH, the distance between air temperature and dew point becomes small. A colder surface, cooling transient, airflow change or control excursion can therefore consume the remaining margin quickly.

For DCOR, a condition such as:

```text
RH = 90%
DewPointMargin ≈ small
```

must be represented as **low psychrometric margin**, not automatically as a failure.

The 5th edition also incorporated ASHRAE-funded research on corrosion under high relative humidity and gaseous pollutants. ASHRAE recommends environmental corrosion monitoring using silver/copper coupons in applicable datacom environments. citeturn0search1turn0search0

## 5. Temperature pattern / rate of change

A thermal state is not only a point `(T, RH)`; it is a trajectory.

For the 2021 allowable equipment table, the maximum temperature rate of change is **5 K/h or 20 K/h**, depending on the applicable product/class condition and interpretation of the table's limits. DCOR must not collapse these into a single global threshold.

Canonical fields:

```text
T_rate_K_per_h
RH_rate_percent_per_h
T_acceleration_K_per_h2
pattern_window
excursion_duration
peak_excursion
recovery_rate
```

A rate limit is a **constraint on the trajectory**, not merely on the absolute temperature.

Example:

```text
22 °C → 24 °C
```

can be acceptable as an endpoint while still requiring investigation if the transition is too rapid for the applicable equipment policy.

## 6. Pattern classes for DCOR

DCOR should classify observed thermal trajectories into reusable patterns:

| Pattern | Description | Primary risk |
|---|---|---|
| `STEADY` | stable T/RH/load | low dynamic risk |
| `WARMING` | sustained positive dT/dt | thermal margin erosion |
| `COOLING` | sustained negative dT/dt | condensation/transient risk if dew point is approached |
| `HUMIDITY_RISE` | positive dRH/dt or dew-point rise | psychrometric margin erosion |
| `DRYING` | falling RH/dew point | usually lower condensation risk; may affect other policies |
| `EXCURSION` | threshold crossing with recovery | equipment/SLA exposure |
| `OSCILLATION` | repeated control cycling | control instability / auxiliary-energy penalty |
| `RAMP` | monotonic controlled transition | rate-limit compliance |
| `STEP` | abrupt setpoint/environment change | transient thermal/condensation risk |
| `COMMON_MODE` | simultaneous thermal/cooling degradation across redundant paths | resilience risk |

Pattern classification is descriptive. The safety gate still evaluates the actual policy and equipment constraints.

## 7. Rate-of-change and dew-point interaction

The dangerous case is not necessarily the highest temperature. A fast thermal or humidity transition can create a short-lived state in which a surface crosses the dew point.

DCOR therefore evaluates:

```text
T(t)
RH(t)
T_dewpoint(t)
T_surface(t)
DewPointMargin(t)
ΔT/Δt
ΔRH/Δt
ΔT_dewpoint/Δt
```

and forecasts the minimum margin over the control horizon:

```text
min_tau DewPointMargin(t + tau)
```

A candidate control action must not be accepted solely because its endpoint is inside the static ASHRAE envelope.

## 8. Recommended vs allowable

DCOR must preserve this distinction:

```text
RECOMMENDED
    !=
ALLOWABLE
    !=
FACILITY POLICY
    !=
OEM LIMIT
    !=
OPTIMIZER CANDIDATE
    !=
ECONOMIC OPTIMUM
```

The applicable equipment/OEM/facility restriction wins when stricter than the generic ASHRAE envelope.

Operating near an allowable boundary is a controlled risk decision, not evidence of optimality.

## 9. Evidence schema implications

Thermal evidence should include at minimum:

```text
reference_id
reference_version
reference_retrieved_at
equipment_class
T_dry_bulb
RH
T_dewpoint
T_wetbulb
T_surface
DewPointMargin
T_rate_K_per_h
RH_rate_percent_per_h
ThermalMargin
CoolingCapacityMargin
TTU
policy_version
quality_state
lineage
```

A missing sensor must remain explicit as `unknown` or equivalent quality state. Derived values must identify their calculation method and source inputs.

## 10. Benchmark requirements

Benchmark 001 should include at least these temporal cases:

1. **Stable:** state remains inside recommended range.
2. **Recommended-to-allowable:** controlled excursion without violating the applicable class.
3. **Rate violation:** endpoint is acceptable but transition rate is outside policy.
4. **Dew-point approach:** RH/dew point rises while a surface remains relatively cold.
5. **Condensation boundary:** `DewPointMargin <= 0` in the simulated or measured state.
6. **Oscillation:** repeated setpoint corrections increase auxiliary power without improving useful work.
7. **Correlated failure:** extreme weather plus simultaneous cooling degradation.
8. **H1 rejection:** a 26 °C candidate is rejected when H1 policy is active because it exceeds the H1 25 °C allowable upper bound.

## 11. DCOR design rule

The optimizer must reason about **state + trajectory + forecast + policy**, not temperature alone:

```text
measure
  ↓
quality / lineage
  ↓
psychrometric state
  ↓
trajectory / pattern
  ↓
forecast
  ↓
constraints
  ↓
candidate action
  ↓
safety gate
  ↓
execute
  ↓
verify
```

This is the thermal counterpart of DCOR's general evidence loop:

```text
measure → experiment → compare → optimize → verify → replicate
```
