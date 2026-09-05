# DCOR Use Cases

A use case is implementation-ready only when input data, constraints, objective, action space and verification path are explicit.

## UC01 — PUE optimization
Reduce facility overhead relative to IT load without violating thermal or operational constraints.

**Inputs:** IT/facility/cooling power and environmental telemetry.

**Output:** candidate operating point and predicted PUE/energy delta.

**Verification:** normalized measured energy against a versioned baseline.

## UC02 — Cooling optimization
Minimize cooling energy while maintaining the applicable thermal envelope, equipment limits and SLA.

**Inputs:** temperatures, humidity, dew point, cooling power/capacity, airflow/flow, IT load and weather.

**Output:** constrained cooling action and predicted consequences.

## UC03 — Water optimization
Reduce cooling-water consumption without creating thermal or equipment risk.

**Inputs:** metered water, cooling state, weather and workload.

**Output:** constrained water-saving action and verified WUE delta.

## UC04 — Energy-cost optimization
Minimize electricity cost under time-varying tariffs while maintaining SLA, capacity and thermal constraints.

## UC05 — Carbon optimization
Minimize carbon impact using declared emissions factors and workload-aware scheduling where applicable.

## UC06 — Workload-aware optimization
Optimize infrastructure against useful workload rather than facility efficiency alone.

**Primary KPI:** useful work per resource consumed.

## UC07 — Anomaly detection
Detect telemetry and operational behavior that invalidates optimization assumptions.

## UC08 — Baseline verification
Determine whether an observed result is better than a defensible, normalized baseline.

## UC09 — Data-quality monitoring
Prevent stale, missing, duplicated, impossible or low-confidence data from influencing optimization.

## UC10 — Multi-site optimization
Optimize a fleet while preserving tenant, facility, equipment and policy boundaries.

## UC11 — Thermal-risk prediction

**Problem:** detect movement toward an unsafe thermal state before a static limit is crossed.

**Inputs:** temperature, humidity/dew point, surface temperature, IT load, cooling capacity, setpoint, redundancy state, weather forecast and workload/performance.

**KPIs:**

- `ThermalMargin = T_limit - T_predicted`;
- `DewPointMargin = T_surface - T_dewpoint`;
- `CoolingCapacityMargin = Capacity_available - ThermalLoad`;
- `TTU = TimeToUnsafeState`;
- `SLA_Risk`.

**Output:** risk state `SAFE/WATCH/MARGINAL/CRITICAL/UNSAFE`, predicted transition time and evidence.

## UC12 — Economic setpoint optimization

**Problem:** find the highest-value admissible thermal operating point rather than hardcoding 22 °C or 27 °C.

**Objective:**

`maximize Useful_IT_Work / (Energy + Water + Carbon + Cost + Risk)`

**Constraints:** applicable OEM/facility/commissioning policy, thermal margin, dew-point margin, cooling capacity, SLA risk, performance floor, ramp/change-rate and resilience state.

**Method:** evaluate candidate setpoints/actions using a digital twin/counterfactual model; reject unsafe candidates; verify realized outcome against baseline.

### Important rule

A higher setpoint does not inherently increase server performance. It can improve net useful work by reducing cooling overhead or avoiding infrastructure bottlenecks, but can also increase IT fan power, component stress or throttling. DCOR measures the net effect.

## Product use-case rule

Use cases drive connector prioritization through the Connector ROI Matrix. A technically interesting adapter is not automatically a product priority.
