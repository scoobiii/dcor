# Historical Cooling Cases

This document turns public historical cases into reproducible DCOR benchmark scenarios. Public facts are classified as `observed`, `reported`, `derived`, `simulated` or `unknown`.

## Case A — Facebook/Meta Prineville

Prineville is a benchmark for outside-air/economizer operation, direct evaporative cooling, water efficiency and control-induced psychrometric risk.

Historical OCP material reported PUE around **1.077 in Q2 2011** and approximately 1.06–1.10 during normal operation. Historical WUE reporting included **0.22 L/kWh for Q2 2012** after water metering was added. These are historical values, not 2026 operational claims.

The documented 2011 incident is particularly relevant: an erroneous control sequence closed outside-air dampers, recirculated hot air, and drove evaporative cooling toward maximum. Cold-aisle temperature and humidity rose sufficiently for condensation and equipment failures. DCOR models this as a control/psychrometric failure, not as proof that evaporative cooling is intrinsically inefficient.

### DCOR scenario

```text
weather → damper/control error → recirculation
        → evaporative response → RH/dew point rise
        → condensation exposure → equipment impact
```

Required metrics: outdoor T/RH, wet bulb, indoor T/RH, dew point, surface temperature, damper position, water flow, cooling power, IT load and failure state.

## Case B — Google / DeepMind cooling optimization

Google/DeepMind reported up to **40% reduction in cooling energy** from machine-learning optimization in 2016. The system used data from thousands of sensors and modeled variables including temperature, power, pump speeds and setpoints. The later safety-first architecture evaluated candidate actions, checked constraints and then allowed automated control under operator oversight. citeturn0search0turn0search3

DCOR reproduces the architectural lesson:

```text
sensor state → prediction → candidate actions
             → safety constraints → control → verification
```

The 40% figure must not be interpreted as 40% PUE reduction, nor as proof that simply raising a temperature setpoint produced the entire saving.

## Case C — Google London extreme-weather cooling failure

The July 2022 Google Cloud London incident is a resilience benchmark for extreme weather and correlated cooling-system failure. DCOR uses the case to test whether redundancy/capacity policies remain safe under common-mode environmental stress.

The benchmark must model:

- outdoor heat trajectory;
- available cooling capacity;
- redundant-unit failure combinations;
- thermal load;
- workload shedding;
- recovery time;
- SLA impact.

## Case D — Oracle thermal guidance

Oracle public guidance can be used as a vendor-specific reference case for environmental operating requirements. It must remain a source-specific policy, not a universal DCOR rule.

## Cross-case hypothesis

The cases converge on one engineering principle:

> **The optimum is a state-dependent operating point inside a safety envelope, not a universal temperature number.**

## Benchmark comparison

| Case | Main lesson | DCOR dimension |
|---|---|---|
| Prineville | efficient cooling can still fail under bad control/psychrometrics | dew point + control resilience |
| Google/DeepMind | predictive optimization can reduce cooling energy | dynamic optimization |
| Google London | redundancy can fail jointly under extreme weather | resilience/capacity |
| Oracle | vendor requirements vary by platform/equipment | policy-specific envelope |

## Evidence policy

Historical public data is never silently upgraded to current data. If the latest measured value cannot be established, DCOR records `unknown` and preserves the source date.
