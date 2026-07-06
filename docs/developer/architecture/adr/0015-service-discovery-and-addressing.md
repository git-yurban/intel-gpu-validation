# ADR-0015: Service Discovery and Addressing

**Status:** Accepted

**Date:** 2026-07-02

## Context

The validation platform consists of multiple independent platform services that communicate over the network.

As services are deployed, upgraded, replaced, or scaled, network endpoints may change.

Platform services therefore require a stable mechanism for locating and communicating with one another without depending on fixed network addresses.

---

## Decision

The platform adopts **Service Discovery and Addressing** as the architectural mechanism for locating platform services.

Services communicate using logical service identities rather than fixed network addresses.

The implementation of service discovery is not defined by the platform architecture.

---

## Responsibilities

Service Discovery and Addressing is responsible for:

* Resolving logical service identities.
* Providing stable service endpoints.
* Supporting independent service deployment.
* Enabling service replacement.

Service Discovery and Addressing is not responsible for:

* Service communication protocols.
* Authentication or authorization.
* Load balancing policy.
* Service health monitoring.
* Operational state management.

---

## Service Model

Every platform service has a stable logical identity.

Platform services discover one another through the service discovery mechanism rather than using implementation-specific addresses.

Examples of platform services include:

* Builder
* Artifact Storage
* Artifact Manager
* Scheduler
* Operational Database
* Dashboard

Validation Workers participate as clients of platform services and do not require inbound service discovery.

---

## Resolution Flow

```text
Platform Service
        │
Resolve Logical Service Identity
        │
        ▼
Service Discovery
        │
Return Service Endpoint
        │
        ▼
Communicate with Platform Service
```

Resolved endpoints are implementation details and may change without affecting the platform architecture.

---

## Design Principles

Service Discovery and Addressing should be:

* Stable
* Independent of deployment topology
* Replaceable
* Scalable
* Transparent to platform services

The platform architecture intentionally does not prescribe the discovery technology.

---

## Consequences

### Advantages

* Decouples services from physical deployment.
* Simplifies scaling and replacement.
* Supports flexible deployment models.
* Enables infrastructure evolution without architectural change.

### Disadvantages

* Introduces a service discovery dependency.
* Requires endpoint resolution before communication.
* Adds operational infrastructure.

---

## Alternatives Considered

### Fixed network addresses

Rejected.

Static addressing tightly couples the architecture to deployment topology and complicates service replacement.

### Hardcoded service endpoints

Rejected.

Hardcoded endpoints reduce deployment flexibility and increase operational complexity.

### Service-specific discovery mechanisms

Rejected.

A common discovery mechanism provides a consistent architectural model across all platform services.

---

## Related ADRs

* ADR-0009 — Scheduler as Control Plane
* ADR-0010 — Operational Database
* ADR-0013 — Builder as an Independent Service
