# Otto — DCOR Brand System

Otto is the DCOR engineering character. The brand must reinforce the product lifecycle without turning the technical product into a cartoon.

## Core identity

> **Otto observes before acting. Optimizes under constraints. Verifies the result.**

The operational sequence is:

```text
OBSERVE → MEASURE → SIMULATE → OPTIMIZE → VERIFY
```

## Asset roles

| Asset | Role | Primary use |
|---|---|---|
| Otto Hero | Full technical character | README hero, presentations, releases |
| Otto Mark | Circular/editorial emblem | Documentation, posters, community material |
| Otto Icon | Head + visor | Favicon, avatar, badges |
| Otto Minimal | Geometric silhouette | Small UI/loading states |

The existing technical Otto remains the canonical project mascot. New assets must preserve recognizability and avoid unrelated visual identities.

## Operational states

| State | Meaning | Suggested label |
|---|---|---|
| Observe | Telemetry/quality inspection | `OTTO / WATCHING` |
| Optimize | Candidate evaluation | `OTTO / OPTIMIZING` |
| Verify | Evidence accepted | `OTTO / VERIFIED` |
| Blocked | Constraint/policy rejection | `OTTO / BLOCKED` |
| Error | Pipeline failure | `OTTO / ERROR` |

States are semantic status indicators, not decorative animation requirements.

## Developer touchpoints

Preferred locations, in order of value:

1. README/product documentation;
2. CLI validation output;
3. CI/PR status language;
4. release notes;
5. dashboard only after the canonical product flow exists.

## CLI rule

Otto may appear in `scripts/test.sh` only as a compact status marker after the gate has succeeded or at a clearly defined failure boundary. The gate output remains machine-readable and must not depend on ANSI art, emoji or terminal width.

## Visual direction

Keep:

- technical posture;
- restrained HUD/telemetry motifs;
- ciano/teal and dark technical palette;
- subtle water/cooling references;
- engineering equipment rather than toy accessories.

Avoid:

- childish proportions;
- excessive facial comedy;
- visual noise in CI/log contexts;
- making Otto appear to authorize unsafe control actions.

## Product language

Otto should explain the architecture, not replace it. Examples:

```text
OTTO / WATCHING
Telemetry quality is being evaluated.

OTTO / OPTIMIZING
Candidate is within declared constraints.

OTTO / VERIFIED
Actual result reconciled against the normalized baseline.

OTTO / BLOCKED
Candidate rejected by policy or safety constraints.
```
