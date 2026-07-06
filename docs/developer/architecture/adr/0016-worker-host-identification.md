# ADR-0016: Worker Host Identification

**Status:** Accepted

**Date:** 2026-07-02

## Context

The validation platform executes workloads on a fleet of Worker Hosts.

A Worker Host provides the compute resources required by a single Validation Worker.

To support scheduling, operational monitoring, diagnostics, auditing, and historical reporting, every Worker Host must be uniquely identifiable throughout its operational lifetime.

The platform therefore requires a stable Worker Host Identity.

---

## Decision

Every Worker Host shall have exactly one immutable Worker Host Identity.

The Worker Host Identity uniquely identifies the execution resource hosting a Validation Worker.

Worker Host Identities are assigned when a Worker Host is registered with the platform and remain unchanged throughout the lifetime of the host.

---

## Scope

The Worker Host Identity is used by platform services including:

* Scheduler
* Operational Database
* Dashboard

Validation Workers report the Worker Host Identity as part of their operational state.

The representation of the Worker Host Identity is an implementation decision.

---

## Identity Rules

A Worker Host Identity:

* Is globally unique.
* Is immutable.
* Identifies exactly one Worker Host.
* Is never reused.
* Remains valid until the Worker Host is permanently removed from the platform.

Worker replacement or software upgrades do not change the Worker Host Identity.

---

## Worker Host Lifecycle

```text id="kbl8sl"
Provision Worker Host
          │
Assign Worker Host Identity
          │
          ▼
Register with Platform
          │
          ▼
Execute Validation Workloads
          │
          ▼
Retire Worker Host
```

The Worker Host Identity remains constant throughout the operational lifetime of the Worker Host.

---

## Consequences

### Advantages

* Enables reliable Worker Host identification.
* Supports scheduling and diagnostics.
* Simplifies operational reporting.
* Preserves historical execution records.
* Improves auditability.

### Disadvantages

* Requires unique identity assignment.
* Requires Worker Host registration.
* Identity lifecycle must be managed.

---

## Alternatives Considered

### Identify Worker Hosts by hostname

Rejected.

Hostnames may change over time and should not be treated as architectural identities.

### Identify Worker Hosts by network address

Rejected.

Network addresses are deployment details and are not stable architectural identifiers.

### Reassign Worker Host Identities

Rejected.

Historical execution records require stable, immutable Worker Host identities.

---

## Related ADRs

* ADR-0009 — Scheduler as Control Plane
* ADR-0010 — Operational Database
* ADR-0012 — Stateless Workers
* ADR-0017 — Worker Capability Model
* ADR-0018 — Capability-Based Scheduling
