# Execution Directory Reference

## Overview

An Execution Directory Reference is the Architectural Contract that identifies a prepared Execution Directory.

It is created by the Artifact Manager, embedded in a Worker Manifest by the Scheduler, and consumed by a Validation Worker to locate the prepared execution resources.

The Execution Directory Reference identifies a transient execution resource rather than containing the execution resources themselves.

---

# Purpose

An Execution Directory Reference enables the platform to:

* Identify a prepared Execution Directory.
* Decouple execution resources from scheduling.
* Reference transient execution resources without embedding them in Architectural Contracts.

The reference identifies **where** execution resources are available, not **what** those resources contain.

---

# Architectural Role

An Execution Directory Reference provides:

* Identification of a prepared Execution Directory.
* Access information required by the Validation Worker.
* Metadata required to resolve the Execution Directory.

An Execution Directory Reference does not:

* Contain build outputs.
* Contain Artifact Packages.
* Contain validation results.
* Define execution behavior.

Those responsibilities belong to other Architectural Contracts.

---

# Ownership

| Component         | Responsibility                       |
| ----------------- | ------------------------------------ |
| Artifact Manager  | Create Execution Directory Reference |
| Scheduler         | Embed reference in Worker Manifest   |
| Validation Worker | Resolve and consume the reference    |

The Artifact Manager is the authoritative creator of the Execution Directory Reference.

The reference is never modified after creation.

---

# Lifecycle

```text id="9s6p1e"
Artifact Manager
        │
Prepare Execution Directory
        │
Create Execution Directory Reference
        │
        ▼
Scheduler
        │
Embed in Worker Manifest
        │
        ▼
Validation Worker
        │
Resolve Reference
        │
Execute Validation
```

The Execution Directory itself exists only for the duration of validation execution.

---

# Reference Contents

An Execution Directory Reference should describe:

* Execution Directory identifier.
* Resolution metadata.
* Lifetime information.

The exact serialization format is implementation-defined.

---

# Resolution

The Validation Worker resolves the Execution Directory Reference before beginning validation execution.

Resolution retrieves access to the prepared Execution Directory.

The resolution mechanism is implementation-defined.

---

# Transient Resource

The Execution Directory Reference identifies a transient execution resource.

The referenced Execution Directory:

* Exists only for validation execution.
* Is not a published artifact.
* Is removed after execution completes.

The reference itself is immutable even though the referenced resource is transient.

---

# Immutability

An Execution Directory Reference is immutable.

After creation:

* The identifier never changes.
* Resolution metadata never changes.
* Lifetime information never changes.

A different Execution Directory requires creation of a new reference.

---

# Design Principles

Execution Directory References should be:

* Immutable.
* Lightweight.
* Self-contained.
* Deterministic.
* Versioned.

The reference should identify execution resources without embedding them.

---

# Relationship to Platform Services

The Artifact Manager creates the Execution Directory Reference.

The Scheduler includes the reference in the Worker Manifest.

The Validation Worker resolves the reference to obtain the prepared Execution Directory.

The Execution Directory Reference is never used to describe published artifacts or Operational State.

---

# Related Documentation

* `docs/architecture.md`
* `docs/glossary.md`
* `docs/developer/contracts/worker-manifest.md`
* `docs/developer/platform/execution-environment.md`
* `docs/developer/services/artifact-manager.md`

## Related ADRs

* ADR-0005 — Artifact Storage
* ADR-0011 — Execution Environment Isolation
* ADR-0020 — Data Classification
