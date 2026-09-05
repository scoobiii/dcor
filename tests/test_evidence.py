from datetime import datetime, timezone

import pytest

from dcor.evidence import Evidence, EvidenceStatus


def test_evidence_round_trip_and_verified_delta() -> None:
    item = Evidence(
        optimization_id="opt-001",
        timestamp=datetime(2026, 9, 4, 15, 0, tzinfo=timezone.utc),
        facility_id="dc-001",
        baseline={"energy_kwh": 100.0, "method": "baseline-v1"},
        prediction={"energy_delta_kwh": 4.0},
        action={"type": "recommendation"},
        constraints={"thermal": "PASS"},
        actual={"energy_kwh": 94.0},
        normalization={"workload": "v1"},
        energy_delta_kwh=6.0,
        cost_delta={"currency": "BRL", "amount": 12.0},
        carbon_delta_kg_co2e=2.5,
        water_delta_liters=10.0,
        thermal_impact={"max_delta_c": 0.2},
        sla_impact={"status": "PASS"},
        confidence=0.98,
        verification_status=EvidenceStatus.VERIFIED,
        lineage={"replay_id": "replay-001", "code_version": "abc"},
    )

    assert item.is_verified
    assert item.timestamp_utc.tzinfo == timezone.utc
    assert item.verified_energy_delta_kwh == 6.0
    payload = item.as_dict()
    assert payload["verification_status"] == "VERIFIED"
    assert payload["cost_delta"]["currency"] == "BRL"

    restored = Evidence.from_mapping(payload)
    assert restored == item


def test_minimal_evidence_uses_defaults_and_none_fields() -> None:
    item = Evidence.from_mapping(
        {
            "optimization_id": "opt-002",
            "timestamp": "2026-09-04T15:00:00Z",
            "facility_id": "dc-001",
            "baseline": {"energy_kwh": 50},
        }
    )
    assert item.verification_status is EvidenceStatus.POTENTIAL
    assert not item.is_verified
    payload = item.as_dict()
    assert payload["prediction"] is None
    assert payload["lineage"] is None


def test_from_mapping_accepts_enum_status() -> None:
    item = Evidence.from_mapping(
        {
            "optimization_id": "opt-003",
            "timestamp": datetime(2026, 9, 4, tzinfo=timezone.utc),
            "facility_id": "dc-001",
            "baseline": {"energy_kwh": 20},
            "verification_status": EvidenceStatus.EXECUTED,
        }
    )
    assert item.verification_status is EvidenceStatus.EXECUTED


def test_verified_requires_actual_results() -> None:
    with pytest.raises(ValueError, match="actual results"):
        Evidence(
            optimization_id="opt-004",
            timestamp=datetime.now(timezone.utc),
            facility_id="dc-001",
            baseline={"energy_kwh": 20},
            verification_status=EvidenceStatus.VERIFIED,
        )


def test_verified_delta_requires_actual() -> None:
    item = Evidence(
        optimization_id="opt-005",
        timestamp=datetime.now(timezone.utc),
        facility_id="dc-001",
        baseline={"energy_kwh": 20},
    )
    with pytest.raises(ValueError, match="actual results"):
        _ = item.verified_energy_delta_kwh


def test_verified_delta_requires_energy_fields() -> None:
    item = Evidence(
        optimization_id="opt-006",
        timestamp=datetime.now(timezone.utc),
        facility_id="dc-001",
        baseline={"energy_kwh": 20},
        actual={"other": 19},
    )
    with pytest.raises(ValueError, match="energy_kwh"):
        _ = item.verified_energy_delta_kwh


def test_evidence_rejects_invalid_identity_timestamp_confidence_and_numbers() -> None:
    now = datetime.now(timezone.utc)
    with pytest.raises(ValueError, match="optimization_id"):
        Evidence("", now, "dc", {"energy_kwh": 1})
    with pytest.raises(ValueError, match="facility_id"):
        Evidence("id", now, "", {"energy_kwh": 1})
    with pytest.raises(ValueError, match="timezone-aware"):
        Evidence("id", datetime(2026, 1, 1), "dc", {"energy_kwh": 1})
    with pytest.raises(ValueError, match="baseline"):
        Evidence("id", now, "dc", {})
    with pytest.raises(ValueError, match="between 0 and 1"):
        Evidence("id", now, "dc", {"energy_kwh": 1}, confidence=1.1)
    with pytest.raises(ValueError, match="energy_delta_kwh"):
        Evidence("id", now, "dc", {"energy_kwh": 1}, energy_delta_kwh=float("inf"))
    with pytest.raises(ValueError, match="carbon_delta_kg_co2e"):
        Evidence("id", now, "dc", {"energy_kwh": 1}, carbon_delta_kg_co2e=float("nan"))
    with pytest.raises(ValueError, match="water_delta_liters"):
        Evidence("id", now, "dc", {"energy_kwh": 1}, water_delta_liters=float("inf"))


def test_negative_and_zero_deltas_are_valid_finite_values() -> None:
    item = Evidence(
        "opt-007",
        datetime.now(timezone.utc),
        "dc-001",
        {"energy_kwh": 10},
        energy_delta_kwh=-1.0,
        carbon_delta_kg_co2e=0.0,
        water_delta_liters=-2.0,
    )
    assert item.energy_delta_kwh == -1.0
