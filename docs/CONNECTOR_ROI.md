# DCOR Connector ROI Matrix

DCOR does not implement connectors merely because an integration is technically possible. Connector priority is a product decision.

## Prioritization model

Use a qualitative score first, then replace it with measured values as implementation evidence becomes available:

```text
ROI priority ≈
(business value × data availability × deployment reach × optimization potential)
÷ engineering cost
```

Scores use a 1–5 scale. Higher is better for the numerator; engineering cost is also 1–5, where 5 means expensive.

## Initial matrix

| Connector / source | Business value | Data availability | Deployment reach | Optimization potential | Engineering cost | Priority |
|---|---:|---:|---:|---:|---:|---|
| Frontier | 5 | 5 | 4 | 5 | 2 | P0 |
| CSV | 5 | 5 | 5 | 4 | 1 | P0 |
| NLR/DOE | 4 | 5 | 4 | 4 | 2 | P0 |
| REST | 5 | 4 | 5 | 4 | 2 | P1 |
| MQTT | 5 | 4 | 5 | 5 | 3 | P1 |
| OPC-UA | 5 | 4 | 5 | 5 | 4 | P1 |
| Modbus | 4 | 4 | 5 | 4 | 4 | P2 |
| Direct BMS/DCIM/SCADA/EPMS adapters | 5 | 3 | 4 | 5 | 5 | P2 |

These are planning scores, not measured market or implementation benchmarks. They must be revised when real deployment evidence exists.

## Decision rules

A connector should move from PLANNED to implementation only if:

1. a concrete use case consumes its data;
2. the source fields map cleanly to the canonical contract or expose a documented mapping gap;
3. source licensing/terms permit the intended use;
4. quality and lineage behavior are testable;
5. the connector does not leak vendor-specific assumptions into the domain core;
6. expected value justifies maintenance cost.

## Priority gates

**P0** — required to prove the first product value or provide broadly reusable data.

**P1** — high-value protocol/integration path after the first vertical slice.

**P2** — valuable but expensive or deployment-specific; implement when a validated use case requires it.

## Scope-control rule

Adding a new adapter requires a short decision record containing:

- consumer use case;
- source/protocol;
- canonical fields affected;
- expected deployment reach;
- data-quality risks;
- security/operational risks;
- engineering estimate;
- ROI score;
- explicit reason to implement now rather than later.

This is the principal defense against scope creep and against turning vendor neutrality into reverse vendor lock-in through an unbounded adapter catalog.
