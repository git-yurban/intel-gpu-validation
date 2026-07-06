# ADR-0023: Configuration over Customization

**Status:** Accepted

**Date:** 2026-07-02

## Context

The validation platform must support different environments, hardware configurations, deployment models, scheduling policies, retention policies, and operational requirements.

Allowing platform behavior to diverge through service-specific customization increases complexity, reduces reproducibility, and makes long-term maintenance more difficult.

The platform therefore requires a consistent approach to platform configuration.

---

## Decision

The platform adopts **Configuration over Customization** as an architectural principle.

Platform behavior should be controlled through configuration rather than service-specific customization or source code modifications.

Configuration adjusts platform behavior without changing architectural responsibilities.

---

## Configuration Principles

Configuration should be used for:

* Deployment settings
* Scheduling policies
* Artifact retention policies
* Platform limits
* Operational thresholds
* Environment-specific values

Configuration should not be used to:

* Change service responsibilities.
* Modify architectural boundaries.
* Introduce platform-specific behavior.
* Replace architectural decisions.

Architectural changes require new or updated Architecture Decision Records.

---

## Design Principles

Configuration should be:

* Declarative
* Versioned
* Observable
* Reproducible
* Consistent across platform services

Configuration should be external to platform services whenever practical.

---

## Architectural Boundaries

Configuration influences **how** platform services operate.

Architecture defines **what** platform services are responsible for.

Configuration must not redefine architectural ownership or service boundaries.

Changes to architecture require architectural decisions, not configuration changes.

---

## Consequences

### Advantages

* Simplifies deployments.
* Supports multiple environments.
* Improves reproducibility.
* Reduces implementation divergence.
* Preserves architectural consistency.

### Disadvantages

* Requires configuration management.
* Excessive configuration can become difficult to maintain.
* Configuration changes still require operational discipline.

---

## Alternatives Considered

### Service-specific customization

Rejected.

Customization increases long-term maintenance costs and encourages architectural divergence.

### Source code modifications for deployments

Rejected.

Deployment-specific behavior should be expressed through configuration whenever practical.

### Environment-specific architectures

Rejected.

A single architectural model simplifies long-term evolution and operational consistency.

---

## Related ADRs

* ADR-0019 — Engineering Guidelines
