from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Iterable, Mapping

from dcor.canonical import Telemetry


class ConnectorError(RuntimeError):
    """Base exception for connector failures."""


class AuthenticationError(ConnectorError):
    pass


class NormalizationError(ConnectorError):
    pass


@dataclass(frozen=True, slots=True)
class ConnectorHealth:
    connector: str
    connected: bool
    authenticated: bool
    last_error: str | None = None
    details: Mapping[str, Any] = field(default_factory=dict)


class Connector(ABC):
    """Source-independent connector lifecycle."""

    name: str

    @abstractmethod
    def connect(self) -> None: ...

    @abstractmethod
    def authenticate(self) -> None: ...

    @abstractmethod
    def discover(self) -> Mapping[str, Any]: ...

    @abstractmethod
    def read(self) -> Iterable[Mapping[str, Any]]: ...

    @abstractmethod
    def normalize(self, record: Mapping[str, Any]) -> Iterable[Telemetry]: ...

    def validate(self, telemetry: Telemetry) -> Telemetry:
        # Canonical model performs structural validation. Connectors may override
        # this method for source-specific ranges without changing the contract.
        return telemetry

    @abstractmethod
    def health(self) -> ConnectorHealth: ...

    @abstractmethod
    def disconnect(self) -> None: ...

    def collect(self) -> list[Telemetry]:
        """Read, normalize and validate records through the canonical boundary."""
        output: list[Telemetry] = []
        for record in self.read():
            try:
                normalized = self.normalize(record)
            except Exception as exc:  # normalize failures become connector errors
                raise NormalizationError(f"{self.name}: {exc}") from exc
            for item in normalized:
                output.append(self.validate(item))
        return output
