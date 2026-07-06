# Build Manifest

## Overview

The Build Manifest is the immutable Architectural Contract describing a published Build.

It defines the Build Identity, the published Artifact Packages that comprise the Build, and the information required by the platform to prepare an Execution Directory.

The Build Manifest is created by the Builder and never changes after publication.

---

# Purpose

The Build Manifest enables the platform to:

* Identify a published Build.
* Describe the Artifact Packages that comprise the Build.
* Provide a deterministic description of build outputs.
* Support reproducible validation execution.

The Build Manifest is the authoritative description of a published Build.

---

# Architectural Role

The Build Manifest provides:

* Build Identity.
* Artifact Package references.
* Build metadata.
* Build composition.

The Build Manifest does not:

* Contain Artifact Package contents.
* Describe validation requests.
* Describe Worker Capabilities.
* Record validation results.

Those responsibilities belong to other Architectural Contracts.

---

# Ownership

| Component         | Responsibility                                                             |
| ----------------- | -------------------------------------------------------------------------- |
| Builder           | Create Build Manifest                                                      |
| Artifact Storage  | Store referenced Artifact Packages                                         |
| Artifact Manager  | Consume Build Manifest                                                     |
| Scheduler         | Reference Build Identity                                                   |
| Validation Worker | Indirectly consume Build Manifest through the prepared Execution Directory |

The Builder is the authoritative creator of the Build Manifest.

---

# Lifecycle

```text id="5mq1m5"
Builder
      │
Create Build Manifest
      │
Publish
      ▼
Artifact Storage
      │
Immutable Contract
      │
      ▼
Artifact Manager
      │
Prepare Execution Directory
```

The Build Manifest never changes after publication.

---

# Manifest Contents

A Build Manifest should describe:

* Build Identity
* Build metadata
* Build version
* Build timestamp
* Published Artifact Packages
* Artifact integrity information
* Platform metadata required to prepare execution

The exact serialization format is implementation-defined.

---

# Artifact References

The Build Manifest references Artifact Packages.

It does not embed them.

Artifact references should uniquely identify immutable published Artifact Packages.

Artifact retrieval is performed through the Artifact Access API.

---

# Immutability

A Build Manifest is immutable.

After publication:

* Fields are never modified.
* Artifact references never change.
* Build Identity never changes.

A modified Build requires creation of a new Build Manifest.

---

# Versioning

The Build Manifest should support versioning.

Versioning enables:

* Backward compatibility.
* Forward evolution.
* Independent platform upgrades.

Versioning strategy is implementation-defined.

---

# Integrity

The Build Manifest should enable verification that:

* Referenced Artifact Packages exist.
* Artifact integrity can be validated.
* Artifact references resolve unambiguously.

Integrity verification occurs before Execution Directory preparation.

---

# Design Principles

The Build Manifest should be:

* Immutable.
* Self-contained.
* Deterministic.
* Versioned.
* Reproducible.

The Build Manifest is the authoritative description of a published Build.

---

# Relationship to Platform Services

The Builder creates the Build Manifest.

Artifact Storage stores the referenced Artifact Packages.

The Artifact Manager consumes the Build Manifest to prepare an Execution Directory.

The Scheduler references the Build Identity contained within the Build Manifest.

Validation Workers consume the prepared Execution Directory rather than the Build Manifest directly.

---

# Related Documentation

* `docs/architecture.md`
* `docs/glossary.md`
* `docs/developer/services/builder.md`
* `docs/developer/services/artifact-manager.md`
* `docs/developer/contracts/artifact-package.md`

## Related ADRs

* ADR-0002 — Immutable Build Artifacts
* ADR-0003 — Build and Worker Manifest Model
* ADR-0005 — Artifact Storage
* ADR-0007 — Build Identity
* ADR-0020 — Data Classification
