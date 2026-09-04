# DCOR Standards & Reference Framework

DCOR uses standards as engineering constraints and interoperability references. It does **not** claim to certify a facility, an Uptime Tier, or regulatory compliance.

| Reference | DCOR use |
|---|---|
| Uptime Institute Tier I–IV | operational context and resilience constraints; not certification |
| Uptime Institute TCOS / M&O | operational discipline and maintainability context |
| ASHRAE TC 9.9 | IT thermal envelope and environmental constraints |
| ISO 50001 | energy-management concepts, measurement and continuous improvement |
| The Green Grid PUE | facility-vs-IT efficiency KPI |
| The Green Grid WUE | water-efficiency KPI |
| CUE / carbon accounting concepts | carbon-impact KPI |
| IEEE P5002 | trusted digital energy-usage recording concepts |
| IEEE P4200 | data-center/grid interconnection context |
| IEEE P3793 | data collection and efficiency optimization context |
| IEEE P7100 | environmental impact considerations for AI |
| IEEE P3973 | digital-twin-enabled modular data-center context |
| IEEE 1927.1 | energy-efficient orchestration/management context |

## Engineering rules

### Thermal

Thermal policies must encode inlet/return/supply temperatures, humidity where relevant, ramp limits and equipment operating envelopes. ASHRAE guidance is treated as a reference for allowable operating conditions; facility-specific OEM and commissioning limits take precedence where stricter.

### Energy

Energy measurements preserve raw units and timestamps. Derived KPIs must identify the source interval and aggregation method. PUE is never inferred from incomplete power boundaries without an explicit quality state.

### Carbon

Carbon calculations require an explicit emissions-factor source, effective interval and unit. A missing or stale factor cannot silently produce a verified carbon saving.

### Water

WUE calculations require water-consumption telemetry and matching IT-energy boundaries. Cooling-water estimates must be distinguished from metered consumption.

### Resilience

Uptime Tier is a facility resilience classification/context, not a DCOR optimization score. DCOR must never optimize through a constraint that compromises a customer-defined resilience policy.

### Data integrity

Each canonical measurement carries quality, confidence and lineage. Time-series processing must account for timezone, clock drift, duplicates, missing intervals, outliers and sensor health.

## Source governance

The implementation should link each production rule to the applicable standard/reference version in a machine-readable policy registry. Standards evolve; the code must therefore avoid hard-coding undocumented assumptions.

## Primary external references

- Uptime Institute Tier Certification overview and Tier standards.
- ISO 50001 Energy Management Systems.
- ASHRAE TC 9.9 thermal/environmental guidance.
- The Green Grid PUE/WUE guidance.
- IEEE data-center energy, interconnection, optimization and digital-twin working-group standards.

See the project research notes for exact source versions and applicability decisions before a production release.
