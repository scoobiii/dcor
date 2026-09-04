# DCOR Canonical Data Model

## Measurement envelope

A canonical measurement is source-neutral and carries enough context to be safely aggregated, validated and traced.

```json
{
  "tenant_id": "tenant-001",
  "facility_id": "dc-001",
  "asset_id": "rack-042",
  "timestamp": "2026-09-04T15:00:00Z",
  "metric": "it_power_kw",
  "value": 842.3,
  "unit": "kW",
  "quality": "GOOD",
  "confidence": 1.0,
  "source": "frontier",
  "lineage": {
    "connector": "frontier",
    "source_record_id": "r-001",
    "schema_version": "1"
  }
}
```

## Required fields

| Field | Type | Rule |
|---|---|---|
| `tenant_id` | string | required for SaaS persistence; optional for isolated lab mode |
| `facility_id` | string | stable facility identifier |
| `asset_id` | string/null | physical/logical asset when known |
| `timestamp` | RFC3339 UTC | source time normalized to UTC |
| `metric` | string | canonical metric name |
| `value` | number | finite numeric value |
| `unit` | string | canonical unit |
| `quality` | enum | GOOD, SUSPECT, BAD, MISSING, STALE, DUPLICATE |
| `confidence` | 0..1 | ingestion confidence |
| `source` | string | connector/source identity |
| `lineage` | object | source traceability |

## Initial canonical metrics

`it_power_kw`, `cooling_power_kw`, `total_power_kw`, `pue`, `ambient_temp_c`, `humidity_pct`, `supply_water_c`, `return_water_c`, `coolant_flow_lpm`, `cpu_utilization_pct`, `gpu_utilization_pct`.

Additional metrics are added through versioned schema changes, not ad-hoc connector fields.

## Quality rules

- timestamps are normalized to UTC while preserving original source timestamp in lineage when available;
- duplicates are detected by source identity plus timestamp/metric/asset semantics;
- impossible values become `BAD`, not silently clipped;
- stale values remain distinguishable from fresh values;
- unit conversion is explicit and tested;
- interpolation is a policy decision and cannot erase the original quality state;
- confidence is not a substitute for quality.

## Evolution

The model is versioned. Backward-compatible additions may remain in the same major version. Semantic changes require a new version and migration/test evidence.
