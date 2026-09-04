from collections.abc import Iterable, Mapping

import pytest

from dcor.canonical import Telemetry
from dcor.connectors.sdk import Connector, ConnectorHealth, NormalizationError


class BrokenConnector(Connector):
    name = "broken"

    def connect(self) -> None:
        pass

    def authenticate(self) -> None:
        pass

    def discover(self) -> Mapping[str, object]:
        return {}

    def read(self) -> Iterable[Mapping[str, object]]:
        return [{"raw": "record"}]

    def normalize(self, record: Mapping[str, object]) -> Iterable[Telemetry]:
        raise ValueError("bad source record")

    def health(self) -> ConnectorHealth:
        return ConnectorHealth(self.name, False, False, details={"reason": "fixture"})

    def disconnect(self) -> None:
        pass


def test_collect_wraps_normalization_failures() -> None:
    with pytest.raises(NormalizationError, match="broken: bad source record"):
        BrokenConnector().collect()


def test_connector_health_preserves_optional_metadata() -> None:
    health = BrokenConnector().health()
    assert health.last_error is None
    assert health.details == {"reason": "fixture"}
