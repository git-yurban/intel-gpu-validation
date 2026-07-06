# Service Discovery and Addressing

## Overview

Service Discovery and Addressing provide the platform capability that enables independent platform services to locate and communicate with one another.

The platform separates service identity from network location, allowing services to evolve, scale, and relocate without affecting other platform components.

Service Discovery is a shared platform capability rather than a platform service.

---

# Purpose

Service Discovery enables platform services to:

* Locate other platform services.
* Resolve service addresses.
* Communicate without implementation-specific knowledge.
* Support independent deployment and scaling.

This capability is foundational to the platform's service-oriented architecture.

---

# Architectural Role

Service Discovery provides:

* Service registration
* Service lookup
* Address resolution

It does not:

* Execute validation workloads.
* Schedule validation.
* Store platform data.
* Own Operational State.

Those responsibilities remain with individual platform services.

---

# Participants

Platform services participating in Service Discovery include:

* Builder
* Artifact Storage
* Artifact Manager
* Scheduler
* Validation Worker
* Operational Database
* Dashboard

Each service publishes its reachable endpoint using implementation-defined mechanisms.

---

# Discovery Model

```text id="d5l6es"
Platform Service
        │
Register
        │
        ▼
Service Discovery
        │
Resolve
        │
        ▼
Platform Service
```

The implementation of registration and resolution is intentionally outside the scope of the platform architecture.

---

# Design Principles

Service Discovery should be:

* Independent
* Reliable
* Scalable
* Implementation-agnostic
* Transparent to platform services

Platform services communicate using logical service identities rather than fixed network addresses.

---

# Failure Handling

If Service Discovery is unavailable:

* Existing service communications may continue according to implementation-specific behavior.
* New service discovery requests may fail.
* Platform recovery behavior is implementation-specific.

The architecture does not mandate a particular discovery technology or recovery mechanism.

---

# Scalability

Service Discovery should scale independently of individual platform services.

Platform growth should not require architectural changes to service addressing or discovery.

---

# Observability

Service Discovery should publish telemetry describing:

* Service registrations
* Service resolution requests
* Resolution latency
* Discovery failures
* Service health

Telemetry supports observability but is not Operational State.

---

# Relationship to Platform Services

Platform services depend on Service Discovery for locating one another.

Service Discovery does not change the responsibilities or ownership boundaries of individual platform services.

It provides the communication capability that allows independently deployed services to cooperate.

---

# Related Documentation

* `docs/architecture.md`
* `docs/principles.md`
* `docs/glossary.md`

## Related ADRs

* ADR-0015 — Service Discovery and Addressing
* ADR-0019 — Engineering Guidelines
* ADR-0021 — Telemetry and Observability
