# Validation Result

## Overview

A Validation Result is the Architectural Contract that records the outcome of a validation execution.

It is created by the Validation Worker upon completion of execution and published to the Operational Database as mutable Operational State.

The Validation Result provides the authoritative record of a completed validation execution.

---

# Purpose

A Validation Result enables the platform to:

* Record validation outcomes.
* Report execution status.
* Preserve execution metadata.
* Support operational visibility and historical analysis.

A Validation Result describes **what happened** during execution, not **how** the execution was performed.

---

# Architectural Role

A Validation Result provides:

* Execution outcome.
* Validation status.
* Execution metadata.
* References to execution artifacts (if applicable).

A Validation Result does not:

* Contain Artifact Packages.
* Contain the Execution Directory.
* Modify the Worker Manifest.
* Change the Validation Request.

Those responsibilities belong to other Architectural Contracts.

---

# Ownership

| Component            | Responsibility                               |
| -------------------- | -------------------------------------------- |
| Validation Worker    | Create Validation Result                     |
| Operational Database | Become authoritative owner after publication |
| Dashboard            | Consume Validation Result                    |
| Platform tooling     | Consume Validation Result                    |

Authoritative ownership transfers from the Validation Worker to the Operational Database upon publication.

---

# Lifecycle

```text id="8s7jpa"
Validation Worker
        │
Execute Validation
        │
Create Validation Result
        │
Publish
        ▼
Operational Database
        │
Query
        ▼
Dashboard / Platform Tooling
```

The Validation Result becomes part of the platform's Operational State after publication.

---

# Result Contents

A Validation Result should describe:

* Build Identity.
* Validation workload.
* Execution status.
* Completion metadata.
* Result metadata.
* References to execution artifacts (if applicable).

The exact serialization format is implementation-defined.

---

# Execution Outcome

A Validation Result should record:

* Successful completion.
* Failed execution.
* Aborted execution.
* Infrastructure failure.

Additional platform-specific outcome classifications may be introduced without changing the architectural role of the contract.

---

# Execution Artifacts

Execution logs, crash dumps, screenshots, and similar outputs are not embedded in the Validation Result.

Instead, the Validation Result may contain references to externally stored execution artifacts.

This keeps the contract lightweight while preserving access to detailed execution evidence.

---

# Mutability

Unlike the Build Manifest and Worker Manifest, the Validation Result becomes part of mutable Operational State after publication.

The Validation Worker publishes the completed result.

The Operational Database owns its lifecycle thereafter.

Historical retention and lifecycle policies are implementation-defined.

---

# Versioning

Validation Results should support versioning.

Versioning enables:

* Backward compatibility.
* Forward evolution.
* Independent platform upgrades.

Versioning strategy is implementation-defined.

---

# Design Principles

Validation Results should be:

* Complete.
* Deterministic.
* Versioned.
* Queryable.
* Independent of presentation.

The Validation Result is the authoritative architectural record of a completed validation execution.

---

# Relationship to Platform Services

The Validation Worker creates the Validation Result.

The Operational Database becomes the authoritative owner after publication.

The Dashboard and other platform tooling consume Validation Results through the Operational Query API.

Validation Results never modify previously published Architectural Contracts.

---

# Related Documentation

* `docs/architecture.md`
* `docs/glossary.md`
* `docs/developer/contracts/worker-manifest.md`
* `docs/developer/services/worker.md`
* `docs/developer/services/operational-database.md`
* `docs/developer/api/operational-query-api.md`

## Related ADRs

* ADR-0009 — Scheduler as Control Plane
* ADR-0010 — Operational Database
* ADR-0020 — Data Classification
* ADR-0022 — Dashboard as a Read-Only Platform Service
