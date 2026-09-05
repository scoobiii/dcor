# DCOR Canonical Data Model

The canonical model is the interoperability boundary between connectors and domain services.

## Measurement envelope

Every measurement must preserve:

- `tenant_id` / facility / asset identity;
- metric name and value;
- unit and timestamp/timezone;
- quality state;
- confidence/uncertainty where available;
- source connector and source identifier;
- schema/version lineage.

## Thermal domain vocabulary

Where supported, canonical telemetry may include:

```text
ambient_temperature
supply_temperature
return_temperature
inlet_temperature
surface_temperature
relative_humidity
wet_bulb_temperature
dew_point_temperature
it_thermal_load
rack_density
cooling_capacity
cooling_power
fan_power
pump_power
compressor_power
setpoint
workload
performance
sla_state
redundancy_state
```

## Derived indicators

Derived values must identify their inputs and calculation version.

- `ThermalMargin = T_limit - T_predicted`
- `DewPointMargin = T_surface - T_dewpoint`
- `CoolingCapacityMargin = Capacity_available - ThermalLoad`
- `TTU = TimeToUnsafeState`
- `PUE = FacilityPower / ITPower` when boundaries are valid
- `WUE = WaterConsumption / ITEnergy` when boundaries are valid

## Setpoint semantics

Do not overload `setpoint` to mean a standard recommendation. Store policy/reference ranges separately from the active facility setpoint and optimizer candidates.

```text
reference_range
allowable_range
facility_limit
OEM_limit
commissioning_limit
current_setpoint
candidate_setpoint
```

## Quality states

At minimum:

`VALID | MISSING | STALE | DUPLICATE | INVALID | ESTIMATED | SIMULATED | UNKNOWN`

A derived metric built from invalid inputs cannot become a trusted measurement merely because its arithmetic succeeds.

## Contract rule

Connectors normalize source semantics into this vocabulary. Optimizers, analytics and UI must consume canonical fields rather than source-specific names.
