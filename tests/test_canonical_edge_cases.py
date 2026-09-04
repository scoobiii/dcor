from datetime import datetime, timedelta, timezone

import pytest

from dcor.canonical import Lineage, Quality, Telemetry


def valid_record() -> dict[str, object]:
    return {
        "tenant_id": "tenant-1",
        "facility_id": "dc-001",
        "asset_id": "rack-01",
        "timestamp": "2026-09-04T15:00:00Z",
        "metric": "it_power_kw",
        "value": 842.3,
        "unit": "kW",
        "quality": "suspect",
        "confidence": 0.75,
        "source": "fixture",
        "lineage": {
            "connector": "fixture",
            "source_record_id": "r-001",
            "schema_version": "2",
            "original_timestamp": "2026-09-04T14:59:00Z",
        },
    }


def test_mapping_supports_optional_fields_and_lineage() -> None:
    item = Telemetry.from_mapping(valid_record())
    assert item.quality is Quality.SUSPECT
    assert item.lineage == Lineage(
        connector="fixture",
        source_record_id="r-001",
        schema_version="2",
        original_timestamp="2026-09-04T14:59:00Z",
    )
    assert item.as_dict()["tenant_id"] == "tenant-1"
    assert item.as_dict()["asset_id"] == "rack-01"
    assert item.as_dict()["lineage"]["connector"] == "fixture"


def test_mapping_accepts_quality_enum_and_datetime() -> None:
    timestamp = datetime(2026, 9, 4, 12, tzinfo=timezone(timedelta(hours=-3)))
    item = Telemetry.from_mapping(
        {
            "facility_id": "dc-001",
            "timestamp": timestamp,
            "metric": "it_power_kw",
            "value": 1,
            "unit": "kW",
            "quality": Quality.GOOD,
        }
    )
    assert item.quality is Quality.GOOD
    assert item.timestamp_utc == datetime(2026, 9, 4, 15, tzinfo=timezone.utc)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("facility_id", "", "facility_id is required"),
        ("metric", "", "metric is required"),
        ("unit", "", "unit is required"),
        ("value", float("inf"), "value must be finite"),
        ("value", float("nan"), "value must be finite"),
    ],
)
def test_rejects_invalid_required_values(field: str, value: object, message: str) -> None:
    record = {
        "facility_id": "dc-001",
        "timestamp": datetime.now(timezone.utc),
        "metric": "it_power_kw",
        "value": 1.0,
        "unit": "kW",
    }
    record[field] = value
    with pytest.raises(ValueError, match=message):
        Telemetry(**record)  # type: ignore[arg-type]


@pytest.mark.parametrize("confidence", [-0.01, 1.01])
def test_rejects_out_of_range_confidence(confidence: float) -> None:
    with pytest.raises(ValueError, match="between 0 and 1"):
        Telemetry(
            facility_id="dc-001",
            timestamp=datetime.now(timezone.utc),
            metric="it_power_kw",
            value=1,
            unit="kW",
            confidence=confidence,
        )


def test_as_dict_without_lineage() -> None:
    item = Telemetry(
        facility_id="dc-001",
        timestamp=datetime(2026, 9, 4, 15, tzinfo=timezone.utc),
        metric="it_power_kw",
        value=1,
        unit="kW",
    )
    assert item.as_dict()["lineage"] is None


def test_mapping_uses_defaults() -> None:
    item = Telemetry.from_mapping(
        {
            "facility_id": "dc-001",
            "timestamp": "2026-09-04T15:00:00Z",
            "metric": "it_power_kw",
            "value": 1,
            "unit": "kW",
        }
    )
    assert item.quality is Quality.GOOD
    assert item.confidence == 1.0
    assert item.source == "unknown"
    assert item.tenant_id is None
    assert item.asset_id is None
