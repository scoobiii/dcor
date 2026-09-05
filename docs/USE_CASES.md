# DCOR Use Cases

This catalog keeps the product boundary concrete. A use case is not complete until its input, constraints, algorithm and verification path are explicit.

## UC01 — PUE optimization

**Problem:** reduce facility overhead relative to IT load without violating thermal or operational constraints.

**Input:** IT power, cooling/HVAC/pump power, facility power and relevant environmental telemetry.

**Canonical metrics:** `it_power_kw`, `cooling_power_kw`, `facility_power_kw`, `pue`.

**Constraint:** thermal limits, equipment capacity, operational policy and SLA.

**Algorithm:** baseline → rules/PID/MPC/MILP → advanced optimization when justified.

**Output:** candidate operating point and predicted energy/PUE delta.

**Verification:** normalized baseline versus actual energy/PUE.

**Business KPI:** energy cost and PUE reduction.

## UC02 — Cooling optimization

**Problem:** minimize cooling energy while maintaining acceptable thermal conditions.

**Input:** temperatures, humidity, cooling power, airflow/flow where available, IT load and ambient conditions.

**Canonical metrics:** thermal and cooling power series plus quality/confidence.

**Constraint:** thermal envelope, equipment limits and control policy.

**Algorithm:** rules/PID/MPC; RL only after validated replay/twin baselines.

**Output:** recommendation with constraint evidence.

**Verification:** actual cooling energy and thermal impact.

**Business KPI:** cooling kWh, thermal excursions and operating cost.

## UC03 — Water optimization

**Problem:** reduce water consumption associated with cooling operations.

**Input:** water flow/consumption, cooling state, weather and workload.

**Canonical metrics:** water volume/flow, temperature, cooling power and workload proxies.

**Constraint:** thermal limits, equipment and water-system operating limits.

**Algorithm:** baseline and constrained optimization.

**Output:** predicted water delta and safe candidate action.

**Verification:** normalized water consumption and thermal impact.

**Business KPI:** WUE and water volume/cost.

## UC04 — Energy cost optimization

**Problem:** reduce electricity cost under time-varying tariffs without violating operational constraints.

**Input:** power/load series, tariff schedule, workload and operating constraints.

**Canonical metrics:** kW/kWh, tariff and workload features.

**Constraint:** SLA, capacity, thermal and policy limits.

**Algorithm:** constrained scheduling/optimization.

**Output:** predicted cost delta and recommendation.

**Verification:** normalized actual cost versus baseline.

**Business KPI:** currency saved per interval/month.

## UC05 — Carbon optimization

**Problem:** reduce carbon intensity associated with electricity consumption.

**Input:** energy consumption, grid carbon-intensity signal and workload.

**Canonical metrics:** kWh, carbon intensity and workload.

**Constraint:** SLA, capacity and operational policies.

**Algorithm:** constrained workload/energy scheduling where applicable.

**Output:** predicted carbon delta.

**Verification:** actual normalized energy × declared carbon-intensity methodology.

**Business KPI:** kgCO2e avoided.

## UC06 — Workload-aware optimization

**Problem:** avoid optimizing infrastructure against an incomplete view of IT demand.

**Input:** workload/compute telemetry plus facility telemetry.

**Canonical metrics:** workload, IT power, thermal and facility power.

**Constraint:** workload SLA and infrastructure capacity.

**Algorithm:** workload-aware baseline and constrained optimizer.

**Output:** infrastructure action tied to workload state.

**Verification:** energy/cost delta with workload normalization.

**Business KPI:** energy per unit of useful workload.

## UC07 — Anomaly detection

**Problem:** detect telemetry or operational behavior that invalidates optimization assumptions.

**Input:** canonical time series and quality metadata.

**Canonical metrics:** all relevant measurements plus quality/confidence.

**Constraint:** false-positive/false-negative policy and operational severity.

**Algorithm:** statistical/rule/model-based detection.

**Output:** anomaly with evidence and lineage.

**Verification:** replay/regression evaluation.

**Business KPI:** invalid data prevented from influencing decisions.

## UC08 — Baseline verification

**Problem:** determine whether an observed result is better than a defensible baseline.

**Input:** historical/reference telemetry, workload, weather and tariff context.

**Canonical metrics:** energy, workload, weather and relevant operating state.

**Constraint:** comparable operating conditions.

**Algorithm:** versioned baseline + normalization.

**Output:** baseline, normalized actual and delta.

**Verification:** Evidence Contract.

**Business KPI:** verified savings rather than predicted savings.

## UC09 — Data quality monitoring

**Problem:** prevent missing, stale, duplicate, impossible or low-confidence telemetry from contaminating downstream optimization.

**Input:** all connector outputs.

**Canonical metrics:** quality, confidence, timestamp and lineage fields.

**Constraint:** source-specific quality policy.

**Algorithm:** deterministic validation and quality classification.

**Output:** quality report and rejected/quarantined records.

**Verification:** contract and regression tests.

**Business KPI:** valid-record rate and optimization decisions protected from bad data.

## UC10 — Multi-site optimization

**Problem:** optimize a fleet while preserving tenant/site isolation and local operating constraints.

**Input:** canonical telemetry from multiple facilities plus site-specific policy.

**Canonical metrics:** common DCOR metrics and site metadata.

**Constraint:** tenant, site, equipment, thermal, SLA and policy boundaries.

**Algorithm:** site-local optimization with fleet-level analytics where justified.

**Output:** site-level recommendations and fleet roll-up.

**Verification:** evidence remains attributable to the site and tenant.

**Business KPI:** aggregate verified energy/cost/carbon/water improvement.

## Product rule

A use case should be promoted into implementation only when its data availability, business value, deployment reach and engineering effort justify the connector/algorithm investment. The use-case catalog is therefore an input to the Connector ROI Matrix and not a promise to implement every adapter.
