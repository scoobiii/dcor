# DCOR Benchmark

The DCOR Benchmark provides a common evaluation surface for connectors, data quality, replay, baselines, optimization and safety. It is intended to prevent language choice or model novelty from becoming a substitute for measurable system performance.

## Benchmark stages

```text
ingestion
   ↓
normalization
   ↓
data quality
   ↓
replay
   ↓
baseline
   ↓
optimization
   ↓
safety
   ↓
verification
   ↓
performance
```

## Metrics

| Category | Primary KPI | Notes |
|---|---|---|
| Ingestion | records/s | State dataset and batch size |
| Latency | p50 / p95 / p99 | Separate ingestion and end-to-end latency |
| Memory | MB | Peak resident memory where measurable |
| CPU | % / CPU-seconds | Record environment |
| Normalization | records/s | Same canonical contract |
| Quality | invalid % | Include reason categories |
| Replay | deterministic match/tolerance | Fixed manifest + version |
| Baseline | MAE / RMSE | Dataset-specific validity rules |
| Optimization | energy/cost/carbon/water delta | Compare against declared baseline |
| Safety | rejected actions | Count and reason |
| Verification | confidence / verification rate | Prediction is not verification |
| Reproducibility | replay success rate | Same manifest across runs |

## Required benchmark metadata

Every benchmark result must identify:

- DCOR version/commit;
- connector and schema version;
- dataset/replay identifier and content hash;
- hardware/runtime environment;
- Python or other language/runtime version;
- configuration;
- seed when stochastic;
- warm-up policy;
- measurement interval;
- numerical tolerance where applicable.

## Fair comparison

Comparisons are valid only when inputs, canonical contract, measurement window and acceptance criteria are equivalent. A faster implementation that changes semantics is not a valid optimization.

Polyglot components must be benchmarked at the boundary they are intended to serve. The purpose is to establish a measurable reason for another language, not to maximize the language count.

## Optimization benchmark

Optimization results must include at least:

- baseline objective;
- candidate objective;
- constraint violations;
- rejected candidates/actions;
- predicted delta;
- actual delta when verification data exists;
- runtime and resource consumption.

No benchmark result may label predicted savings as verified savings.

## Regression policy

A benchmark becomes a regression gate only after its metric is stable enough to justify a threshold. Thresholds must be versioned with the benchmark and should distinguish deterministic failures from expected numerical variance.
