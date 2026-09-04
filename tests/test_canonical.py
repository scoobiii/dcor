from datetime import datetime, timezone

import pytest

from dcor.canonical import Quality, Telemetry


def test_telemetry_normalizes_timestamp_to_utc() -> None:
    item = Telemetry(
        facility_id="dc-001",
        timestamp=datetime(2026, 9, 4, 12, 0, tzinfo=timezone.utc),
        metric="it_power_kw",
        value=842.3,
        unit="kW",
    )
    assert item.timestamp_utc.tzinfo == timezone.utc
    assert item.as_dict()["quality"] == "GOOD"


def test_mapping_round_trip() -> None:
    item = Telemetry.from_mapping(
        {
            "facility_id": "dc-001",
            "timestamp": "2026-09-04T15:00:00Z",
            "metric": "ambient_temp_c",
            "value": 29.4,
            "unit": "degC",
            "quality": "GOOD",
            "confidence": 0.95,
            "source": "fixture",
        }
    )
    assert item.quality is Quality.GOOD
    assert item.confidence == 0.95


def test_rejects_naive_timestamp() -> None:
    with pytest.raises(ValueError, match="timezone-aware"):
        Telemetry(
            facility_id="dc-001",
            timestamp=datetime(2026, 9, 4, 12, 0),
            metric="it_power_kw",
            value=1,
            unit="kW",
        )


def test_rejects_invalid_confidence() -> None:
    with pytest.raises(ValueError, match="between 0 and 1"):
        Telemetry(
            facility_id="dc-001",
            timestamp=datetime.now(timezone.utc),
            metric="it_power_kw",
            value=1,
            unit="kW",
            confidence=1.1,
        )
