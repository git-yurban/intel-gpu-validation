# Scheduler

**Document:** 07-scheduler.md

---

# Purpose

The Scheduler is the central control plane of the Intel GPU Validation Lab.

It owns every scheduling decision within the platform.

Workers never decide:

- what to execute
- when to execute
- retry policies
- prioritization
- campaign completion

The Scheduler is responsible for converting immutable build artifacts into executable work.

---

# Responsibilities

The Scheduler owns:

- Campaign creation
- Test sharding
- Worker registration
- Capability matching
- Queue management
- Retry policies
- Worker Manifest generation
- Campaign completion
- Campaign statistics

The Scheduler does **not**:

- Build software
- Publish artifacts
- Execute tests
- Download artifacts

---

# High-Level Architecture

```
              Build Manifest
                     │
                     ▼
                Scheduler
         ┌───────────┼────────────┐
         ▼           ▼            ▼
 Campaign DB     Redis Queue   Worker Registry
         │                        │
         └────────────┬───────────┘
                      ▼
              Worker Manifest
                      │
                      ▼
                  Worker
```

The Scheduler is the only component aware of the complete system state.

---

# Primary Workflow

```
Builder publishes build

↓

Scheduler discovers Build Manifest

↓

Create Campaign

↓

Generate Test Shards

↓

Create Worker Manifests

↓

Push work into Redis

↓

Workers execute shards

↓

Collect Results

↓

Campaign Complete
```

---

# Campaign

A Campaign represents one validation request.

Examples:

```
Mesa main

Mesa release/25.1

Mesa merge request

Nightly validation

Kernel upgrade validation
```

Each campaign references exactly one Build Manifest.

---

# Campaign Lifecycle

```
Created

↓

Queued

↓

Running

↓

Completed

↓

Archived
```

Campaign state is stored in PostgreSQL.

---

# Test Sharding

The Scheduler divides work into independent shards.

Example:

```
CTS

↓

1,200,000 tests

↓

12,000 shards

↓

Redis Queue
```

Workers pull shards continuously until completion.

---

# Shard Size

Recommended execution time:

```
2–10 minutes
```

Reasons:

- Better load balancing
- Faster retries
- Reduced idle time
- Higher throughput

Future versions may dynamically resize shards based on historical execution times.

---

# Worker Manifest Generation

Each shard receives its own Worker Manifest.

Example:

```json
{
    "manifest_version": 1,

    "campaign": {
        "id": "campaign-12345"
    },

    "build": {
        "name": "mesa-main-4f2c9b8d",
        "git_sha": "4f2c9b8d..."
    },

    "artifacts": [
        {
            "component": "mesa",
            "uri": "minio://artifacts/mesa/main/mesa-main-4f2c9b8d.tar.zst",
            "sha256": "..."
        }
    ],

    "shard": {
        "suite": "vulkancts",
        "tests": [
            "dEQP-VK.pipeline.*"
        ]
    }
}
```

The Worker never requires additional metadata.

---

# Worker Registration

Workers register when they start.

Registration includes:

- Worker ID
- Hostname
- Architecture
- GPU
- Driver
- Memory
- Software version
- Supported capabilities

Workers periodically refresh their registration.

---

# Capability Matching

Every shard may define requirements.

Examples:

```
Intel Xe

Intel DG2

Intel Battlemage

Kernel >= 6.10

Vulkan 1.4

Debug build
```

Only compatible workers receive the shard.

---

# Queue Management

Redis stores pending work.

Typical flow:

```
Create Worker Manifest

↓

Serialize

↓

Push to Redis

↓

Worker claims

↓

Execute

↓

Remove from queue
```

Redis never stores permanent state.

---

# Worker Heartbeats

Workers publish heartbeats periodically.

Typical interval:

```
30 seconds
```

Heartbeat includes:

- Status
- Active shard
- Progress
- Cache statistics
- Software version

---

# Failure Detection

Worker heartbeat expires.

```
Heartbeat timeout

↓

Shard marked abandoned

↓

Retry counter++

↓

Generate new Worker Manifest

↓

Requeue
```

No manual intervention required.

---

# Retry Policy

Retries occur automatically.

Recommended defaults:

Maximum retries:

```
3
```

Retry reasons:

- Worker failure
- Timeout
- GPU hang
- Infrastructure error

Functional test failures are **not retried** automatically.

---

# Worker States

Workers transition through:

```
Registering

↓

Idle

↓

Preparing

↓

Executing

↓

Uploading

↓

Idle
```

Workers remain stateless.

---

# Campaign Completion

A campaign completes when:

```
Pending shards == 0

AND

Running shards == 0

AND

Retry queue empty
```

Results are finalized and archived.

---

# Scheduling Strategy

The Scheduler favors:

1. Capability match
2. Worker locality (future)
3. Cache reuse (future)
4. FIFO campaign priority
5. Fair worker utilization

Scheduling algorithms should remain replaceable.

---

# Persistent State

PostgreSQL stores:

- Campaigns
- Workers
- Results
- History
- Statistics
- Retry counts

Redis stores only transient work items.

---

# Public REST API

Future endpoints:

```
POST /campaigns

GET /campaigns

GET /workers

GET /campaigns/{id}

DELETE /campaigns/{id}

POST /workers/register

POST /workers/heartbeat

POST /results
```

The REST API is the external interface to the Scheduler.

---

# Metrics

Useful Scheduler metrics include:

- Active campaigns
- Pending shards
- Running shards
- Completed shards
- Retry count
- Worker utilization
- Queue latency
- Average shard runtime
- Campaign duration

Metrics should be exported to Prometheus.

---

# Design Principles

## Scheduler owns policy.

Workers own execution.

---

## Shards remain small.

Smaller shards improve utilization and fault tolerance.

---

## Workers remain stateless.

No worker should be required for campaign completion.

---

## Redis remains transient.

Persistent state belongs in PostgreSQL.

---

## Build information is immutable.

Worker Manifests copy build information from the Build Manifest.

Workers never modify execution contracts.

---

# Future Enhancements

Planned improvements include:

- Historical runtime prediction
- Dynamic shard sizing
- Machine quarantine
- Campaign priorities
- Worker affinity
- Multi-site scheduling
- Predictive cache warming
- Maintenance windows
- Resource-aware scheduling
- Kubernetes-native scheduling

---

# Summary

The Scheduler is the control plane of the Intel GPU Validation Lab.

It transforms immutable builds into executable work while coordinating hundreds of workers through deterministic scheduling policies.

Its design ensures scalability, fault tolerance, and efficient hardware utilization without requiring workers to maintain global state.

---

# Next Document

```
08-worker.md
```

This document describes the Worker daemon, execution lifecycle, Artifact Manager integration, telemetry, and result publication.