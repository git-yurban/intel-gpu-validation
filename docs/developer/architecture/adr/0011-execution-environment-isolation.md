# ADR-0011: Execution Environment Isolation

**Status:** Accepted

**Date:** 2026-07-02

## Context

Validation workloads execute complex graphics software, drivers, runtime libraries, and test suites that may modify temporary files, caches, environment variables, or process state.

Residual state from previous executions can compromise validation reproducibility and make failures difficult to diagnose.

The platform therefore requires every validation workload to execute within an isolated execution environment.

---

## Decision

Every validation workload shall execute within an isolated **Execution Environment**.

An Execution Environment is created specifically for a validation workload and is discarded after execution completes.

The mechanism used to provide isolation is an implementation decision.

---

## Isolation Requirements

An Execution Environment shall provide isolation for:

* Runtime files
* Temporary files
* Process execution
* Environment variables
* Working directories
* Runtime configuration

The architecture does not prescribe how isolation is implemented.

---

## Execution Lifecycle

```text id="g4rjqe"
Worker Manifest
        │
        ▼
Prepare Execution Environment
        │
        ▼
Execute Validation
        │
        ▼
Collect Validation Results
        │
        ▼
Destroy Execution Environment
```

Each validation workload receives a newly prepared Execution Environment.

Execution Environments are never reused between validation workloads.

---

## Design Principles

Execution Environments should be:

* Isolated
* Deterministic
* Disposable
* Reproducible
* Independent of scheduling decisions

The lifecycle of an Execution Environment is limited to a single validation workload.

---

## Consequences

### Advantages

* Improves validation reproducibility.
* Prevents residual runtime state.
* Simplifies troubleshooting.
* Supports deterministic execution.
* Reduces cross-workload interference.

### Disadvantages

* Requires environment preparation.
* Introduces cleanup overhead.
* May increase execution startup time.

---

## Alternatives Considered

### Shared execution environments

Rejected.

Reusing execution environments allows residual state to influence future validation workloads.

### Persistent execution environments

Rejected.

Persistent environments complicate reproducibility and increase long-term maintenance.

### Prescribe a specific isolation technology

Rejected.

Isolation technology is an implementation decision that may evolve independently of the platform architecture.

---

## Related ADRs

* ADR-0004 — Single Self-Contained Worker Manifest
* ADR-0009 — Scheduler as Control Plane
* ADR-0012 — Stateless Workers
