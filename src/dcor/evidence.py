from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import StrEnum
from math import isfinite
from typing import Any, Mapping


class EvidenceStatus(StrEnum):
    POTENTIAL = "POTENTIAL"
    PREDICTED = "PREDICTED"
    EXECUTED = "EXECUTED"
    VERIFIED = "VERIFIED"
    REJECTED = "REJECTED"


@dataclass(frozen=True, slots=True)
class Evidence:
    optimization_id: str
    timestamp: datetime
    facility_id: str
    baseline: Mapping[str, Any]
    prediction: Mapping[str, Any] | None = None
    action: Mapping[str, Any] | None = None
    constraints: Mapping[str, Any] | None = None
    actual: Mapping[str, Any] | None = None
    normalization: Mapping[str, Any] | None = None
    energy_delta_kwh: float | None = None
    cost_delta: Mapping[str, Any] | None = None
    carbon_delta_kg_co2e: float | None = None
    water_delta_liters: float | None = None
    thermal_impact: Mapping[str, Any] | None = None
    sla_impact: Mapping[str, Any] | None = None
    confidence: float = 1.0
    verification_status: EvidenceStatus = EvidenceStatus.POTENTIAL
    lineage: Mapping[str, Any] | None = None

    def __post_init__(self) -> None:
        if not self.optimization_id:
            raise ValueError("optimization_id is required")
        if not self.facility_id:
            raise ValueError("facility_id is required")
        if self.timestamp.tzinfo is None:
            raise ValueError("timestamp must be timezone-aware")
        if not self.baseline:
            raise ValueError("baseline is required")
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        if self.energy_delta_kwh is not None and not isfinite(self.energy_delta_kwh):
            raise ValueError("energy_delta_kwh must be finite")
        if self.carbon_delta_kg_co2e is not None and not isfinite(self.carbon_delta_kg_co2e):
            raise ValueError("carbon_delta_kg_co2e must be finite")
        if self.water_delta_liters is not None and not isfinite(self.water_delta_liters):
            raise ValueError("water_delta_liters must be finite")
        if self.verification_status is EvidenceStatus.VERIFIED and self.actual is None:
            raise ValueError("VERIFIED evidence requires actual results")

    @property
    def timestamp_utc(self) -> datetime:
        return self.timestamp.astimezone(timezone.utc)

    @property
    def is_verified(self) -> bool:
        return self.verification_status is EvidenceStatus.VERIFIED

    @property
    def verified_energy_delta_kwh(self) -> float:
        if self.actual is None:
            raise ValueError("actual results are required to calculate verified energy delta")
        try:
            baseline_energy = float(self.baseline["energy_kwh"])
            actual_energy = float(self.actual["energy_kwh"])
        except KeyError as exc:
            raise ValueError("baseline and actual require energy_kwh") from exc
        return baseline_energy - actual_energy

    def as_dict(self) -> dict[str, Any]:
        return {
            "optimization_id": self.optimization_id,
            "timestamp": self.timestamp_utc.isoformat().replace("+00:00", "Z"),
            "facility_id": self.facility_id,
            "baseline": dict(self.baseline),
            "prediction": None if self.prediction is None else dict(self.prediction),
            "action": None if self.action is None else dict(self.action),
            "constraints": None if self.constraints is None else dict(self.constraints),
            "actual": None if self.actual is None else dict(self.actual),
            "normalization": None if self.normalization is None else dict(self.normalization),
            "energy_delta_kwh": self.energy_delta_kwh,
            "cost_delta": None if self.cost_delta is None else dict(self.cost_delta),
            "carbon_delta_kg_co2e": self.carbon_delta_kg_co2e,
            "water_delta_liters": self.water_delta_liters,
            "thermal_impact": None if self.thermal_impact is None else dict(self.thermal_impact),
            "sla_impact": None if self.sla_impact is None else dict(self.sla_impact),
            "confidence": self.confidence,
            "verification_status": self.verification_status.value,
            "lineage": None if self.lineage is None else dict(self.lineage),
        }

    @classmethod
    def from_mapping(cls, record: Mapping[str, Any]) -> "Evidence":
        timestamp = record["timestamp"]
        if isinstance(timestamp, str):
            timestamp = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        status = record.get("verification_status", EvidenceStatus.POTENTIAL)
        if not isinstance(status, EvidenceStatus):
            status = EvidenceStatus(str(status).upper())
        return cls(
            optimization_id=str(record["optimization_id"]),
            timestamp=timestamp,
            facility_id=str(record["facility_id"]),
            baseline=record["baseline"],
            prediction=record.get("prediction"),
            action=record.get("action"),
            constraints=record.get("constraints"),
            actual=record.get("actual"),
            normalization=record.get("normalization"),
            energy_delta_kwh=record.get("energy_delta_kwh"),
            cost_delta=record.get("cost_delta"),
            carbon_delta_kg_co2e=record.get("carbon_delta_kg_co2e"),
            water_delta_liters=record.get("water_delta_liters"),
            thermal_impact=record.get("thermal_impact"),
            sla_impact=record.get("sla_impact"),
            confidence=float(record.get("confidence", 1.0)),
            verification_status=status,
            lineage=record.get("lineage"),
        )
