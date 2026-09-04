# Reuse / Adapt / Rewrite / Discard Matrix

Decision rule: reuse behavior and proven hardware/protocol code where it is safe; adapt domain-specific pieces behind DCOR contracts; rewrite architecture-critical components that would leak old assumptions; discard unrelated/UI-first material.

| Source | Decision | Target | Rationale |
|---|---|---|---|
| `Minimize-Energy-consumption-with-Deep-Learning-model` | **ADAPT** | `research/minimize-energy` | Preserve research, notebook, reward ideas and experiments; do not make it the production architecture. |
| `ThermoFlex-Dashboard` | **ADAPT** | `apps/web` / dashboard references | Reuse UI structure/components selectively after canonical API exists; rewrite domain assumptions. |
| `SmartMeters` | **ADAPT** | `hardware-lab/smartmeters` | Useful real electrical telemetry/IoT fixture; wrap measurements in canonical model. |
| `kit-iot` | **REUSE + ADAPT** | `hardware-lab/edge` | Raspberry Pi/I2C/Node.js edge patterns can seed connector/edge experiments. |
| `cpu-info` | **ADAPT** | `packages/telemetry` | Useful host CPU telemetry, but expose only canonical workload/resource metrics. |
| `BME680` / sensor examples | **ADAPT** | `hardware-lab/bme680` | Environmental sensor fixture; not a DCOR domain dependency. |
| `SensorDashboard` | **DISCARD** | — | Historical visualization reference only; too coupled to old UI assumptions. |
| generic unrelated repos | **DISCARD** | — | Avoid repository-frankenstein and preserve bounded contexts. |

## Rules

- No copied code enters `packages/canonical-model` without contract tests.
- Research code remains isolated from production services.
- Hardware drivers remain below the connector/edge boundary.
- UI code cannot become the source of truth for telemetry schemas.
- Every adapted component gets provenance documented before release.
