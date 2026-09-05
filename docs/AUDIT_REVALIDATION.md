# DCOR Audit Revalidation

External audits are snapshots. Findings must be revalidated against the current `main` before they are treated as active defects.

## Finding lifecycle

```text
External audit
     ↓
Finding
     ↓
HEAD revalidation
     ↓
OPEN / FIXED / SUPERSEDED
     ↓
Evidence
```

## Status definitions

| Status | Meaning |
|---|---|
| OPEN | The finding still applies to the current repository state and has no accepted remediation yet. |
| FIXED | The finding no longer applies because the required remediation is present and validated. |
| SUPERSEDED | The original finding is obsolete because the architecture, requirement or repository path changed; a replacement finding may be required. |

## Revalidation record

For each material finding record:

```yaml
finding_id: AUD-<number>
source: <audit/report identifier>
observed_at: <timestamp>
validated_against: <commit SHA>
status: OPEN|FIXED|SUPERSEDED
evidence:
  repository_paths: []
  tests: []
  ci_run: <run identifier|null>
notes: <concise rationale>
```

## Current external-audit snapshot

The supplied audit identified these principal findings:

- S0/S1/S2 foundation was still described as in progress.
- No real connector or minimum vertical slice was identified in the audit snapshot.
- The S8→S9 transition was considered at risk of underestimating data engineering and compute complexity.
- Scope creep was identified as a risk for additional adapters.
- Otto was recommended as a technical engineering character rather than a childish mascot, with multiple usage states.
- The audit also reported documentation/path issues that must be treated as snapshot findings and rechecked against current `main`.

This document does **not** assert that those findings remain true. It defines how they are revalidated.

## Current revalidation notes

As of the current repository inspection:

- `README.md`, `BACKLOG.md`, `ARCHITECTURE.md`, `STANDARDS.md`, `docs/DEVELOPMENT.md`, `docs/COMPATIBILITY.md`, `docs/DELIVERY_MANIFEST.md` and the canonical/connector implementation paths exist on `main`.
- The README language selector points to the multilingual files under `docs/project/`.
- The new MV0, Evidence, Replay, Benchmark, Use Case and Connector ROI contracts are now documented.
- S3 Frontier remains a planned implementation until its adapter, fixture, tests and CI evidence exist.

The repository must not mark S0–S2, S3 or MV0 as `DONE` based on documentation alone.
