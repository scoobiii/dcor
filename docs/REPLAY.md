# DCOR Replay

DCOR Replay turns recorded telemetry into a deterministic input for testing, simulation, benchmarking and audit.

## Pipeline

```text
Source telemetry
      ↓
Canonical records
      ↓
Recorded fixture
      ↓
Replay manifest
      ↓
Twin / baseline / optimizer
```

The same canonical recording must be usable whether its original source was a public dataset, a connector, a lab sensor or a production export.

## Replay manifest

A replay manifest should declare at minimum:

```yaml
replay_id: <stable identifier>
source:
  name: <source>
  connector: <connector>
  schema_version: <version>
dataset:
  version: <version>
  content_hash: <hash>
window:
  start: <UTC timestamp>
  end: <UTC timestamp>
canonical_contract: <version>
quality_policy: <version>
normalization_policy: <version>
execution:
  code_version: <commit/package version>
  seed: <integer|null>
  timezone: UTC
```

## Determinism requirements

For a fixed manifest, input fixture and implementation version:

- record ordering is stable;
- timestamps are normalized consistently;
- normalization produces the same canonical values;
- quality classification is repeatable;
- baseline calculations are repeatable;
- optimizer experiments declare randomness and seed it where applicable;
- replay identifies the exact source/data/code versions used.

Floating-point algorithms may have platform-dependent last-bit differences; benchmark acceptance must therefore define the numerical tolerance rather than pretending all runtimes are bit-identical.

## Uses

Replay is a first-class capability for:

- incident reproduction;
- regression tests;
- connector validation;
- algorithm comparison;
- benchmark execution;
- RL training/evaluation;
- counterfactual experiments;
- evidence reconstruction.

## Data policy

Large or externally licensed datasets should not be copied into the repository merely to make a demo convenient. Prefer manifests, checksums, documented acquisition instructions and small redistributable fixtures. Licensing terms remain authoritative for each source.

## Acceptance criteria

- [ ] A replay has a stable identifier and content hash.
- [ ] Replay input is canonical or deterministically canonicalized.
- [ ] Source lineage is preserved.
- [ ] Replay is independent of dashboard/UI state.
- [ ] The same replay can feed baseline and optimization components.
- [ ] Regression tests detect changes in replay output.
- [ ] Evidence records can reference the replay identifier.
