# Worker Manifest

## Overview

The Worker Manifest is the immutable Architectural Contract that defines a single validation execution.

It is created by the Scheduler after successful scheduling and consumed by a Validation Worker to execute the assigned validation workload.

The Worker Manifest contains all information required for execution and is the sole execution contract consumed by the Validation Worker.

---

# Purpose

The Worker Manifest enables the platform to:

* Describe a scheduled validation execution.
* Decouple scheduling from execution.
* Provide a complete, self-contained execution contract.
* Support deterministic and reproducible validation.

The Worker Manifest defines **what** the Validation Worker shall execute.

---

# Architectural Role

The Worker Manifest provides:

* Build Identity.
* Validation workload.
* Execution Directory Reference.
* Execution parameters.
* Validation metadata.

The Worker Manifest does not:

* Contain Artifact Packages.
* Describe Worker Capabilities.
* Record validation results.
* Contain mutable execution state.

Those responsibilities belong to other Architectural Contracts.

---

# Ownership

| Component         | Responsibility          |
| ----------------- | ----------------------- |
| Scheduler         | Create Worker Manifest  |
| Validation Worker | Consume Worker Manifest |

The Scheduler is the authoritative creator of the Worker Manifest.

The Validation Worker never modifies the Worker Manifest.

---

# Lifecycle

```text id="u4cb67"
Validation Request
        │
Capability Matching
        │
Prepare Execution Directory
        │
        ▼
Scheduler
        │
Create Worker Manifest
        │
Publish
        ▼
Transient Work Queue
        │
Receive
        ▼
Validation Worker
```

Publication of the Worker Manifest marks the completion of scheduling and the beginning of execution.

---

# Manifest Contents

A Worker Manifest should describe:

* Build Identity.
* Validation workload.
* Execution Directory Reference.
* Execution parameters.
* Validation metadata.

The exact serialization format is implementation-defined.

---

# Execution Directory Reference

The Worker Manifest contains an Execution Directory Reference.

The reference identifies a prepared Execution Directory.

The Execution Directory itself is not embedded in the Worker Manifest.

Resolution of the reference is performed by the Validation Worker.

---

# Self-Contained Execution Contract

The Worker Manifest is intentionally self-contained.

A Validation Worker should not require additional scheduling information to begin execution.

All information necessary to execute the validation workload is contained within the Worker Manifest or referenced through the Execution Directory Reference.

---

# Immutability

The Worker Manifest is immutable.

After publication:

* Build Identity never changes.
* Validation workload never changes.
* Execution Directory Reference never changes.
* Execution parameters never change.

A modified execution requires creation of a new Worker Manifest.

---

# Versioning

The Worker Manifest should support versioning.

Versioning enables:

* Backward compatibility.
* Forward evolution.
* Independent platform upgrades.

Versioning strategy is implementation-defined.

---

# Design Principles

The Worker Manifest should be:

* Immutable.
* Self-contained.
* Deterministic.
* Versioned.
* Reproducible.

The Worker Manifest is the complete execution contract between the Scheduler and the Validation Worker.

---

# Relationship to Platform Services

The Scheduler creates the Worker Manifest.

The Transient Work Queue delivers the Worker Manifest.

The Validation Worker consumes the Worker Manifest to execute the validation workload.

The Worker Manifest is never modified after publication.

---

# Related Documentation

* `docs/architecture.md`
* `docs/glossary.md`
* `docs/developer/contracts/validation-request.md`
* `docs/developer/contracts/execution-directory-reference.md`
* `docs/developer/services/scheduler.md`
* `docs/developer/services/worker.md`

## Related ADRs

* ADR-0003 — Build and Worker Manifest Model
* ADR-0004 — Single Self-Contained Worker Manifest
* ADR-0009 — Scheduler as Control Plane
* ADR-0014 — Transient Work Queue
* ADR-0020 — Data Classification


---

## This document crystallizes the platform's control-plane/execution-plane separation:

Control Plane
─────────────

Validation Request
        │
        ▼
Scheduler
        │
        ▼
Worker Manifest
══════════════════════════════
        Execution Boundary
══════════════════════════════

Execution Plane

Validation Worker
        │
Execution Environment
        │
Validation Result