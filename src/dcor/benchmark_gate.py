from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from enum import StrEnum
from math import isfinite
from typing import Any, Mapping


class MetricDirection(StrEnum):
    HIGHER_IS_BETTER = "higher_is_better"
    LOWER_IS_BETTER = "lower_is_better"


@dataclass(frozen=True, slots=True)
class MetricPolicy:
    name: str
    direction: MetricDirection
    max_regression: float = 0.0
    absolute_threshold: float | None = None

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("metric name is required")
        if self.max_regression < 0 or not isfinite(self.max_regression):
            raise ValueError("max_regression must be finite and non-negative")
        if self.absolute_threshold is not None and not isfinite(self.absolute_threshold):
            raise ValueError("absolute_threshold must be finite")


@dataclass(frozen=True, slots=True)
class MetricResult:
    name: str
    baseline: float
    candidate: float

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("metric name is required")
        if not isfinite(self.baseline) or not isfinite(self.candidate):
            raise ValueError("metric values must be finite")


@dataclass(frozen=True, slots=True)
class GateDecision:
    passed: bool
    failures: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ExecutionEvidence:
    commit_sha: str
    ci_run_id: str
    suite_version: str
    environment: Mapping[str, Any]
    execution_proof: Mapping[str, Any]
    benchmark: Mapping[str, Any]
    baseline: Mapping[str, Any]

    def __post_init__(self) -> None:
        for field_name in ("commit_sha", "ci_run_id", "suite_version"):
            if not getattr(self, field_name):
                raise ValueError(f"{field_name} is required")
        for field_name in ("environment", "execution_proof", "benchmark", "baseline"):
            if not getattr(self, field_name):
                raise ValueError(f"{field_name} is required")

    def canonical(self) -> str:
        payload = {
            "baseline": self.baseline,
            "benchmark": self.benchmark,
            "ci_run_id": self.ci_run_id,
            "commit_sha": self.commit_sha,
            "environment": self.environment,
            "execution_proof": self.execution_proof,
            "suite_version": self.suite_version,
        }
        return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)

    @property
    def evidence_hash(self) -> str:
        digest = hashlib.sha256(self.canonical().encode("utf-8")).hexdigest()
        return f"sha256:{digest}"


def compare_metric(policy: MetricPolicy, result: MetricResult) -> str | None:
    if policy.name != result.name:
        raise ValueError("policy and result metric names must match")

    if policy.direction is MetricDirection.HIGHER_IS_BETTER:
        if policy.absolute_threshold is not None and result.candidate < policy.absolute_threshold:
            return f"{result.name}: candidate {result.candidate} is below threshold {policy.absolute_threshold}"
        if result.baseline == 0:
            return None if result.candidate >= 0 else f"{result.name}: candidate is negative"
        regression = (result.baseline - result.candidate) / abs(result.baseline)
    else:
        if policy.absolute_threshold is not None and result.candidate > policy.absolute_threshold:
            return f"{result.name}: candidate {result.candidate} exceeds threshold {policy.absolute_threshold}"
        if result.baseline == 0:
            return None if result.candidate <= 0 else f"{result.name}: candidate is above zero baseline"
        regression = (result.candidate - result.baseline) / abs(result.baseline)

    if regression > policy.max_regression:
        return f"{result.name}: regression {regression:.6f} exceeds allowed {policy.max_regression:.6f}"
    return None


def evaluate_gate(
    policies: tuple[MetricPolicy, ...],
    results: tuple[MetricResult, ...],
    *,
    coverage_percent: float,
    security_passed: bool,
    functional_passed: bool,
    real_execution: bool,
    proof_valid: bool,
    provenance_valid: bool,
) -> GateDecision:
    failures: list[str] = []
    if not isfinite(coverage_percent) or coverage_percent < 100.0:
        failures.append(f"coverage: {coverage_percent} is below required 100.0")
    if not security_passed:
        failures.append("security: failed")
    if not functional_passed:
        failures.append("functional: failed")
    if not real_execution:
        failures.append("real_execution: not proven")
    if not proof_valid:
        failures.append("proof: invalid")
    if not provenance_valid:
        failures.append("provenance: invalid")

    policy_by_name = {policy.name: policy for policy in policies}
    for result in results:
        policy = policy_by_name.get(result.name)
        if policy is None:
            failures.append(f"{result.name}: no policy defined")
            continue
        failure = compare_metric(policy, result)
        if failure:
            failures.append(failure)

    expected_metrics = set(policy_by_name)
    actual_metrics = {result.name for result in results}
    for missing in sorted(expected_metrics - actual_metrics):
        failures.append(f"{missing}: benchmark result missing")

    return GateDecision(passed=not failures, failures=tuple(failures))


def validate_provenance(
    *,
    commit_sha: str,
    ci_commit_sha: str,
    ci_run_id: str,
    suite_version: str,
    evidence: ExecutionEvidence,
) -> bool:
    return bool(
        commit_sha
        and ci_commit_sha
        and commit_sha == ci_commit_sha
        and ci_run_id == evidence.ci_run_id
        and commit_sha == evidence.commit_sha
        and suite_version == evidence.suite_version
    )
