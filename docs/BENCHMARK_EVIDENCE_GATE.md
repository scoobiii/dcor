# Benchmark Evidence Gate v1

This deliverable establishes the deterministic policy/evidence layer for benchmark-based merge decisions. It does not claim that every benchmark stage is already wired into CI; it provides the executable contract that CI can consume.

## Contract

```text
BUILD
  ↓
FUNCTIONAL + INTEGRATION
  ↓
SECURITY
  ↓
100% COVERAGE
  ↓
PERFORMANCE / FAILURE TESTS
  ↓
REAL EXECUTION
  ↓
EXECUTION PROOF
  ↓
CI PROVENANCE
  ↓
BASELINE COMPARISON
  ↓
MERGE ALLOWED | BLOCKED
```

## Implementation

`src/dcor/benchmark_gate.py` provides:

- `MetricPolicy` with explicit metric direction, regression tolerance and optional absolute threshold;
- `MetricResult` with finite baseline/candidate values;
- `compare_metric()` with direction-aware regression calculation;
- `ExecutionEvidence` with deterministic RFC-8785-style JSON ordering using Python's canonical JSON settings and a SHA-256 evidence hash;
- `validate_provenance()` binding commit SHA, CI run ID and benchmark suite version;
- `evaluate_gate()` which fails closed when required functional/security/provenance evidence is absent, coverage is below 100%, metrics are missing, or regressions exceed policy.

The hash is calculated from the canonical evidence payload containing commit, CI run, suite version, environment, execution proof, benchmark result and baseline comparison inputs. Generated timestamps are deliberately not part of the canonical payload unless they are explicitly part of one of those evidence objects.

## Regression semantics

Policies are metric-specific:

- higher-is-better metrics regress when the candidate falls below baseline;
- lower-is-better metrics regress when the candidate rises above baseline;
- absolute thresholds are evaluated in the metric's natural direction;
- zero baselines use explicit zero-boundary rules rather than division by zero;
- missing policy or missing benchmark result blocks the gate.

This prevents a single generic `candidate >= baseline` rule from incorrectly evaluating latency, error rate or memory.

## Provenance rule

Evidence is valid only when all of the following agree:

1. the tested commit SHA;
2. the CI commit SHA;
3. the CI run ID;
4. the benchmark suite version;
5. the corresponding values embedded in `ExecutionEvidence`.

`ExecutionEvidence.evidence_hash` provides deterministic integrity for that bound payload. It is tamper-evident, not a cryptographic signature and not an identity/authentication mechanism.

## Validation

The executable tests are in `tests/test_benchmark_gate.py`. They cover validation failures, both metric directions, thresholds, zero baselines, deterministic hashing, provenance mismatches, complete gate success, and fail-closed gate behavior.

The repository's existing CI already runs the complete `tests/` suite on Python 3.11, 3.12 and 3.13. This deliverable therefore enters the existing CI test matrix without introducing a second incompatible test recipe.
