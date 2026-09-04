from collections.abc import Iterable, Mapping
from datetime import datetime, timezone

from dcor.canonical import Telemetry
from dcor.connectors.sdk import Connector, ConnectorHealth


class FixtureConnector(Connector):
    name = "fixture"

    def __init__(self) -> None:
        self.connected = False
        self.authenticated = False
        self.records = [
            {
                "facility_id": "dc-001",
                "timestamp": "2026-09-04T15:00:00Z",
                "metric": "it_power_kw",
                "value": 842.3,
                "unit": "kW",
            }
        ]

    def connect(self) -> None:
        self.connected = True

    def authenticate(self) -> None:
        self.authenticated = True

    def discover(self) -> Mapping[str, object]:
        return {"metrics": ["it_power_kw"]}

    def read(self) -> Iterable[Mapping[str, object]]:
        return self.records

    def normalize(self, record: Mapping[str, object]) -> Iterable[Telemetry]:
        yield Telemetry.from_mapping({**record, "source": self.name})

    def health(self) -> ConnectorHealth:
        return ConnectorHealth(self.name, self.connected, self.authenticated)

    def disconnect(self) -> None:
        self.connected = False
        self.authenticated = False


def test_connector_collects_through_canonical_boundary() -> None:
    connector = FixtureConnector()
    connector.connect()
    connector.authenticate()
    data = connector.collect()
    assert len(data) == 1
    assert data[0].source == "fixture"
    assert data[0].timestamp == datetime(2026, 9, 4, 15, tzinfo=timezone.utc)


def test_connector_health_reflects_lifecycle() -> None:
    connector = FixtureConnector()
    assert connector.health().connected is False
    connector.connect()
    connector.authenticate()
    assert connector.health().connected is True
    assert connector.health().authenticated is True
    connector.disconnect()
    assert connector.health().connected is False
