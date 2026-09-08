from __future__ import annotations

import pytest

from dcor.benchmark_gate import (
    ExecutionEvidence,
    MetricDirection,
    MetricPolicy,
    MetricResult,
    compare_metric,
    evaluate_gate,
    validate_provenance,
)


def evidence() -> ExecutionEvidence:
    return ExecutionEvidence(
        commit_sha="abc123",
        ci_run_id="run-42",
        suite_version="benchmark-v1",
        environment={"runner": "ubuntu", "python": "3.11"},
        execution_proof={"proof_hash": "sha256:proof"},
        benchmark={"p95_ms": 10.0},
        baseline={"p95_ms": 10.0},
    )


def test_metric_policy_validation() -> None:
    with pytest.raises(ValueError, match="metric name"):
        MetricPolicy("", MetricDirection.HIGHER_IS_BETTER)
    with pytest.raises(ValueError, match="max_regression"):
        MetricPolicy("x", MetricDirection.HIGHER_IS_BETTER, max_regression=-1)
    with pytest.raises(ValueError, match="max_regression"):
        MetricPolicy("x", MetricDirection.HIGHER_IS_BETTER, max_regression=float("inf"))
    with pytest.raises(ValueError, match="absolute_threshold"):
        MetricPolicy("x", MetricDirection.HIGHER_IS_BETTER, absolute_threshold=float("nan"))
    with pytest.raises(ValueError, match="metric name"):
        MetricResult("", 1, 1)
    with pytest.raises(ValueError, match="finite"):
        MetricResult("x", float("inf"), 1)
    with pytest.raises(ValueError, match="finite"):
        MetricResult("x", 1, float("nan"))


def test_compare_higher_is_better_and_threshold() -> None:
    policy = MetricPolicy("throughput", MetricDirection.HIGHER_IS_BETTER, max_regression=0.05, absolute_threshold=90)
    assert compare_metric(policy, MetricResult("throughput", 100, 100)) is None
    assert compare_metric(policy, MetricResult("throughput", 100, 96)) is None
    assert "threshold" in compare_metric(policy, MetricResult("throughput", 100, 89))
    assert "regression" in compare_metric(policy, MetricResult("throughput", 100, 90))
    with pytest.raises(ValueError, match="names"):
        compare_metric(policy, MetricResult("latency", 100, 100))


def test_compare_lower_is_better_and_zero_baselines() -> None:
    policy = MetricPolicy("p95", MetricDirection.LOWER_IS_BETTER, max_regression=0.10, absolute_threshold=15)
    assert compare_metric(policy, MetricResult("p95", 10, 9)) is None
    assert compare_metric(policy, MetricResult("p95", 10, 11)) is None
    assert "threshold" in compare_metric(policy, MetricResult("p95", 10, 16))
    assert "regression" in compare_metric(policy, MetricResult("p95", 10, 12))
    assert compare_metric(MetricPolicy("x", MetricDirection.HIGHER_IS_BETTER), MetricResult("x", 0, 0)) is None
    assert "negative" in compare_metric(MetricPolicy("x", MetricDirection.HIGHER_IS_BETTER), MetricResult("x", 0, -1))
    assert compare_metric(MetricPolicy("x", MetricDirection.LOWER_IS_BETTER), MetricResult("x", 0, 0)) is None
    assert "above zero" in compare_metric(MetricPolicy("x", MetricDirection.LOWER_IS_BETTER), MetricResult("x", 0, 1))


def test_execution_evidence_is_deterministic_and_validates_required_fields() -> None:
    first = evidence()
    second = evidence()
    assert first.canonical() == second.canonical()
    assert first.evidence_hash == second.evidence_hash
    assert first.evidence_hash.startswith("sha256:")
    with pytest.raises(ValueError, match="commit_sha"):
        ExecutionEvidence("", "run", "v1", {"x": 1}, {"x": 1}, {"x": 1}, {"x": 1})
    with pytest.raises(ValueError, match="ci_run_id"):
        ExecutionEvidence("c", "", "v1", {"x": 1}, {"x": 1}, {"x": 1}, {"x": 1})
    with pytest.raises(ValueError, match="suite_version"):
        ExecutionEvidence("c", "r", "", {"x": 1}, {"x": 1}, {"x": 1}, {"x": 1})
    with pytest.raises(ValueError, match="environment"):
        ExecutionEvidence("c", "r", "v", {}, {"x": 1}, {"x": 1}, {"x": 1})
    with pytest.raises(ValueError, match="execution_proof"):
        ExecutionEvidence("c", "r", "v", {"x": 1}, {}, {"x": 1}, {"x": 1})
    with pytest.raises(ValueError, match="benchmark"):
        ExecutionEvidence("c", "r", "v", {"x": 1}, {"x": 1}, {}, {"x": 1})
    with pytest.raises(ValueError, match="baseline"):
        ExecutionEvidence("c", "r", "v", {"x": 1}, {"x": 1}, {"x": 1}, {})


def test_provenance_binding() -> None:
    e = evidence()
    assert validate_provenance(commit_sha="abc123", ci_commit_sha="abc123", ci_run_id="run-42", suite_version="benchmark-v1", evidence=e)
    assert not validate_provenance(commit_sha="wrong", ci_commit_sha="abc123", ci_run_id="run-42", suite_version="benchmark-v1", evidence=e)
    assert not validate_provenance(commit_sha="abc123", ci_commit_sha="wrong", ci_run_id="run-42", suite_version="benchmark-v1", evidence=e)
    assert not validate_provenance(commit_sha="abc123", ci_commit_sha="abc123", ci_run_id="wrong", suite_version="benchmark-v1", evidence=e)
    assert not validate_provenance(commit_sha="abc123", ci_commit_sha="abc123", ci_run_id="run-42", suite_version="wrong", evidence=e)
    assert not validate_provenance(commit_sha="", ci_commit_sha="abc123", ci_run_id="run-42", suite_version="benchmark-v1", evidence=e)


def test_gate_passes_only_when_all_contracts_and_metrics_pass() -> None:
    policies = (
        MetricPolicy("throughput", MetricDirection.HIGHER_IS_BETTER, max_regression=0.05),
        MetricPolicy("p95", MetricDirection.LOWER_IS_BETTER, max_regression=0.10),
    )
    results = (MetricResult("throughput", 100, 98), MetricResult("p95", 10, 10.5))
    decision = evaluate_gate(policies, results, coverage_percent=100, security_passed=True, functional_passed=True, real_execution=True, proof_valid=True, provenance_valid=True)
    assert decision.passed
    assert decision.failures == ()


def test_gate_collects_failures_and_missing_policy_results() -> None:
    policies = (
        MetricPolicy("throughput", MetricDirection.HIGHER_IS_BETTER),
        MetricPolicy("p95", MetricDirection.LOWER_IS_BETTER),
    )
    results = (MetricResult("throughput", 100, 90), MetricResult("unknown", 1, 1))
    decision = evaluate_gate(policies, results, coverage_percent=99.9, security_passed=False, functional_passed=False, real_execution=False, proof_valid=False, provenance_valid=False)
    assert not decision.passed
    assert any("coverage" in failure for failure in decision.failures)
    assert any("security" in failure for failure in decision.failures)
    assert any("functional" in failure for failure in decision.failures)
    assert any("real_execution" in failure for failure in decision.failures)
    assert any("proof" in failure for failure in decision.failures)
    assert any("provenance" in failure for failure in decision.failures)
    assert any("regression" in failure for failure in decision.failures)
    assert any("no policy" in failure for failure in decision.failures)
    assert any("p95" in failure and "missing" in failure for failure in decision.failures)
    nan_decision = evaluate_gate((), (), coverage_percent=float("nan"), security_passed=True, functional_passed=True, real_execution=True, proof_valid=True, provenance_valid=True)
    assert not nan_decision.passed
