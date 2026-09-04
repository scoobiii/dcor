from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import StrEnum
from math import isfinite
from typing import Any, Mapping


class Quality(StrEnum):
    GOOD = "GOOD"
    SUSPECT = "SUSPECT"
    BAD = "BAD"
    MISSING = "MISSING"
    STALE = "STALE"
    DUPLICATE = "DUPLICATE"


@dataclass(frozen=True, slots=True)
class Lineage:
    connector: str
    source_record_id: str | None = None
    schema_version: str = "1"
    original_timestamp: str | None = None


@dataclass(frozen=True, slots=True)
class Telemetry:
    facility_id: str
    timestamp: datetime
    metric: str
    value: float
    unit: str
    quality: Quality = Quality.GOOD
    confidence: float = 1.0
    source: str = "unknown"
    tenant_id: str | None = None
    asset_id: str | None = None
    lineage: Lineage | None = None

    def __post_init__(self) -> None:
        if not self.facility_id:
            raise ValueError("facility_id is required")
        if not self.metric:
            raise ValueError("metric is required")
        if not self.unit:
            raise ValueError("unit is required")
        if not isfinite(self.value):
            raise ValueError("value must be finite")
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        if self.timestamp.tzinfo is None:
            raise ValueError("timestamp must be timezone-aware")

    @property
    def timestamp_utc(self) -> datetime:
        return self.timestamp.astimezone(timezone.utc)

    def as_dict(self) -> dict[str, Any]:
        return {
            "tenant_id": self.tenant_id,
            "facility_id": self.facility_id,
            "asset_id": self.asset_id,
            "timestamp": self.timestamp_utc.isoformat().replace("+00:00", "Z"),
            "metric": self.metric,
            "value": self.value,
            "unit": self.unit,
            "quality": self.quality.value,
            "confidence": self.confidence,
            "source": self.source,
            "lineage": None if self.lineage is None else {
                "connector": self.lineage.connector,
                "source_record_id": self.lineage.source_record_id,
                "schema_version": self.lineage.schema_version,
                "original_timestamp": self.lineage.original_timestamp,
            },
        }

    @classmethod
    def from_mapping(cls, record: Mapping[str, Any]) -> "Telemetry":
        timestamp = record["timestamp"]
        if isinstance(timestamp, str):
            timestamp = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        quality = record.get("quality", Quality.GOOD)
        if not isinstance(quality, Quality):
            quality = Quality(str(quality).upper())
        lineage_value = record.get("lineage")
        lineage = None
        if lineage_value:
            lineage = Lineage(
                connector=str(lineage_value["connector"]),
                source_record_id=lineage_value.get("source_record_id"),
                schema_version=str(lineage_value.get("schema_version", "1")),
                original_timestamp=lineage_value.get("original_timestamp"),
            )
        return cls(
            tenant_id=record.get("tenant_id"),
            facility_id=str(record["facility_id"]),
            asset_id=record.get("asset_id"),
            timestamp=timestamp,
            metric=str(record["metric"]),
            value=float(record["value"]),
            unit=str(record["unit"]),
            quality=quality,
            confidence=float(record.get("confidence", 1.0)),
            source=str(record.get("source", "unknown")),
            lineage=lineage,
        )
