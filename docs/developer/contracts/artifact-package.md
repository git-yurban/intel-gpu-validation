# Artifact Package

## Overview

An Artifact Package is the immutable Architectural Contract that encapsulates one or more build outputs produced by the Builder.

Artifact Packages are the units of publication, storage, and retrieval within the platform. They are referenced by the Build Manifest and retrieved through the Artifact Access API.

Artifact Packages become immutable after publication.

---

# Purpose

Artifact Packages enable the platform to:

* Package build outputs.
* Publish build outputs.
* Store immutable build artifacts.
* Retrieve build outputs for validation execution.

Artifact Packages are the authoritative representation of published build outputs.

---

# Architectural Role

An Artifact Package provides:

* Immutable build outputs.
* Artifact metadata.
* Integrity information.

An Artifact Package does not:

* Describe the Build.
* Describe validation execution.
* Record validation results.
* Define scheduling behavior.

Those responsibilities belong to other Architectural Contracts.

---

# Ownership

| Component         | Responsibility                                                               |
| ----------------- | ---------------------------------------------------------------------------- |
| Builder           | Create Artifact Package                                                      |
| Artifact Storage  | Become authoritative owner after publication                                 |
| Artifact Manager  | Retrieve Artifact Package                                                    |
| Validation Worker | Indirectly consume Artifact Package through the prepared Execution Directory |

Ownership transfers from the Builder to Artifact Storage upon successful publication.

---

# Lifecycle

```text id="8w3n6d"
Builder
      │
Create Artifact Package
      │
Publish
      ▼
Artifact Storage
      │
Retrieve
      ▼
Artifact Manager
      │
Prepare Execution Directory
```

Artifact Packages remain immutable throughout their lifecycle.

---

# Package Contents

An Artifact Package should contain:

* Build outputs.
* Artifact metadata.
* Integrity information.

The internal organization and serialization format are implementation-defined.

---

# Publication

Artifact Packages are published by the Builder.

Successful publication transfers authoritative ownership to Artifact Storage.

Partial publication is not permitted.

---

# Immutability

Artifact Packages are immutable.

After publication:

* Contents never change.
* Metadata never changes.
* Integrity information never changes.

A modified build output requires creation of a new Artifact Package.

---

# Integrity

Each Artifact Package should support integrity verification.

Integrity information enables the platform to verify:

* Package completeness.
* Package authenticity (if applicable).
* Package integrity.

Integrity verification occurs before Execution Directory preparation.

---

# Versioning

Artifact Packages should support versioning.

Versioning enables:

* Backward compatibility.
* Forward evolution.
* Independent platform upgrades.

Versioning strategy is implementation-defined.

---

# Design Principles

Artifact Packages should be:

* Immutable.
* Self-contained.
* Portable.
* Versioned.
* Deterministic.

Artifact Packages should be suitable for long-term storage and reproducible retrieval.

---

# Relationship to Platform Services

The Builder creates Artifact Packages.

Artifact Storage becomes the authoritative owner after publication.

The Artifact Access API provides read-only retrieval.

The Artifact Manager retrieves Artifact Packages to prepare an Execution Directory.

Validation Workers consume the prepared Execution Directory rather than Artifact Packages directly.

---

# Related Documentation

* `docs/architecture.md`
* `docs/glossary.md`
* `docs/developer/contracts/build-manifest.md`
* `docs/developer/services/builder.md`
* `docs/developer/services/artifact-storage.md`
* `docs/developer/api/artifact-access-api.md`

## Related ADRs

* ADR-0002 — Immutable Build Artifacts
* ADR-0005 — Artifact Storage
* ADR-0006 — Compressed Artifact Format
* ADR-0020 — Data Classification
