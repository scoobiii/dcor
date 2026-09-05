# DCOR Thermal Optimization

## Purpose

This document defines the thermal-risk and setpoint optimization model used by DCOR. It replaces the simplistic rule `if temperature > X then alarm` with a state-space and forecast-based approach.

## 1. Thermal state

Minimum state vector:

```text
T_inlet, T_supply, T_return,
RH_inlet, RH_supply,
T_dewpoint, T_wetbulb,
T_surface,
IT_load, rack_density,
fan_power, pump_power, compressor_power,
cooling_capacity, redundancy_state,
setpoint,
workload, performance,
outdoor_temperature, outdoor_RH,
weather_forecast,
SLA_state
```

Not every facility exposes every field. Missing fields are explicit; they are not silently estimated into verified evidence.

## 2. Thermal risk

`R_thermal = P(state(t+τ) ∉ SafeSet | state(t), forecast, action)`.

Risk can be deterministic or probabilistic. A production implementation must expose its model version, horizon, confidence and assumptions.

### Margins

`ThermalMargin = T_limit - T_predicted`

`DewPointMargin = T_surface - T_dewpoint`

`CoolingCapacityMargin = Capacity_available - ThermalLoad`

`SLA_Margin = SLA_limit - predicted_SLA_risk`

### Time-to-unsafe

`TTU = min { τ ≥ 0 : state(t+τ) ∉ SafeSet }`

TTU is more operationally useful than a static alarm because it answers whether an apparently safe state is moving rapidly toward an unsafe boundary.

## 3. Risk states

```text
SAFE
  ↓ margin erosion
WATCH
  ↓ insufficient forecast margin
MARGINAL
  ↓ boundary likely/near
CRITICAL
  ↓ constraint violated
UNSAFE
```

The exact thresholds are facility/equipment policies and must be versioned.

## 4. Psychrometric risk

Evaporative cooling depends on evaporative potential, which is strongly affected by dry-bulb temperature and humidity. DCOR therefore derives wet-bulb/dew-point quantities where the necessary inputs exist.

Condensation risk is governed by surface temperature relative to dew point:

`T_surface <= T_dewpoint` → condensation boundary.

A positive safety margin is required:

`T_surface >= T_dewpoint + Δsafe`.

This captures a class of failures where ambient temperature can look acceptable while moisture/condensation creates equipment risk.

## 5. Setpoint is a control variable

DCOR stores the current setpoint and evaluates candidate setpoints as actions. It does not treat a standard's recommended temperature as the optimizer's answer.

```text
reference envelope
      ↓
facility constraints
      ↓
current state + forecast
      ↓
candidate setpoints
      ↓
predicted energy/water/performance/risk
      ↓
safety gate
      ↓
optimal admissible action
```

## 6. Performance-aware optimization

A candidate `T` is evaluated by:

`J(T,u) = Useful_IT_Work(T,u) / ResourceCost(T,u)`

where `ResourceCost` may include:

- facility energy;
- IT energy;
- cooling energy;
- water;
- carbon;
- monetary cost;
- equipment wear/risk.

Subject to:

```text
ThermalMargin >= ΔT_min
DewPointMargin >= ΔDP_min
CoolingCapacityMargin >= ΔC_min
SLA_Risk <= SLA_max
Performance >= Performance_baseline
Policy == compliant
```

### Important interpretation

Raising a setpoint does **not** inherently increase server performance. It may improve useful work indirectly by reducing cooling overhead, avoiding power/cooling bottlenecks or preventing thermal throttling. It can also increase fan power, component stress or throttling. DCOR must measure/predict the net effect.

## 7. Candidate sweep

For a baseline at 22 °C, a benchmark may evaluate:

```text
22 → 23 → 24 → 25 → 26 → 27 °C
```

but only within the applicable equipment/facility policy. For high-density H1 air-cooled equipment, the 2021 ASHRAE reference is 18–22 °C recommended and 15–25 °C allowable, so 26–27 °C would be outside that H1 allowable envelope unless a different applicable policy/class governs the equipment. citeturn0search1turn0search19

The sweep is therefore a **benchmark method**, not a recommendation to operate at every tested point.

## 8. Control safety

The AI/optimizer may propose an action but cannot authorize it. The safety validator checks the candidate against thermal, dew-point, capacity, equipment, SLA, resilience and change-rate constraints.

## 9. Evidence

For every candidate, persist:

`state_hash + forecast_hash + policy_version + candidate + predicted_metrics + risk + rejected_constraints`.

For executed actions also persist observed telemetry and baseline-adjusted verification.

## 10. Engineering test cases

1. Temperature rising with constant load → TTU decreases.
2. Dew point rising toward surface temperature → DewPointMargin decreases.
3. Cooling capacity loss → CoolingCapacityMargin decreases and candidate actions become restricted.
4. Setpoint increase lowers cooling power but increases IT fan power → optimizer selects net minimum only if constraints hold.
5. H1 equipment at 26 °C → candidate rejected when H1 policy is active.
6. Extreme weather + simultaneous cooling failures → resilience policy triggers load-shed/recovery strategy.
