# Redis

**Document:** 13-redis.md

---

# Purpose

Redis provides transient work distribution between the Scheduler and Workers.

It is responsible for efficiently delivering work while maintaining high throughput and low latency.

Redis is **not** a persistent datastore.

All authoritative scheduling state remains in PostgreSQL.

---

# Responsibilities

Redis owns:

- Pending work queues
- Atomic shard claiming
- Temporary work leases
- Fast queue operations

Redis does **not** own:

- Campaign state
- Worker registration
- Build metadata
- Results
- Retry history

Those are persisted in PostgreSQL.

---

# High-Level Architecture

```
              Scheduler
                   │
                   ▼
             PostgreSQL
                   │
           Rebuild Queue
                   │
                   ▼
                Redis
                   │
                   ▼
                Workers
```

Redis accelerates scheduling but is never the source of truth.

---

# Queue Model

The Scheduler generates Worker Manifests.

Each Worker Manifest represents one executable shard.

```
Campaign

↓

Shard

↓

Worker Manifest

↓

Redis Queue

↓

Worker
```

Workers always consume complete Worker Manifests.

---

# Queue Organization

Initially, a single queue is sufficient.

```
queue:pending
```

Future versions may introduce:

```
queue:high

queue:normal

queue:low

queue:gpu:xe

queue:gpu:bmg
```

Queue organization should remain configurable.

---

# Worker Claim

Workers request work using an atomic claim operation.

```
Pending Queue

↓

Atomic Pop

↓

Worker receives Worker Manifest
```

A shard cannot be assigned twice.

---

# Lease Model

Each claimed shard receives a lease.

```
Claim

↓

Lease Active

↓

Heartbeat

↓

Lease Renewed

↓

Complete

↓

Lease Released
```

If the lease expires, the Scheduler may reassign the shard.

---

# Heartbeats

Workers periodically renew their lease.

Typical interval:

```
30 seconds
```

Failure to renew indicates a lost Worker.

---

# Failure Recovery

```
Worker crashes

↓

Lease expires

↓

Scheduler detects expiration

↓

Generate new Worker Manifest

↓

Push back into Redis
```

Recovery is automatic.

---

# Queue Recovery

Redis is considered disposable.

If Redis is lost:

```
Redis restart

↓

Scheduler scans PostgreSQL

↓

Identify queued shards

↓

Regenerate Worker Manifests

↓

Repopulate queues
```

No execution state is lost.

---

# Worker Polling

Workers continuously request work.

```
GET WORK

↓

Work available?

↓

Yes

↓

Execute

↓

No

↓

Sleep

↓

Retry
```

Polling intervals should use exponential backoff when idle.

---

# Atomic Operations

All queue operations should be atomic.

Examples:

- Claim shard
- Acknowledge completion
- Renew lease

Atomicity prevents duplicate execution.

---

# Worker Manifest Storage

Redis stores serialized Worker Manifests.

The Scheduler is responsible for generating them.

Workers never modify manifests.

---

# Throughput

Redis should support:

- Thousands of queued shards
- Hundreds of Workers
- Millisecond claim latency

Scheduling throughput should not become a bottleneck.

---

# Failure Handling

Recoverable failures:

- Temporary connection loss
- Redis restart

Fatal failures:

- Invalid Worker Manifest
- Corrupted queue entry

Invalid work items should be discarded and regenerated.

---

# Monitoring

Useful Redis metrics include:

- Queue length
- Claims per second
- Average wait time
- Lease expirations
- Requeued shards
- Worker polling rate

These metrics support capacity planning.

---

# Security

Access should be restricted.

Recommended:

- Authentication
- TLS
- Private network
- Least privilege

Workers require only queue access.

---

# Configuration

Typical configuration:

```
Redis endpoint

Authentication

TLS

Queue prefix

Lease timeout

Maximum queue size

Worker polling interval
```

Configuration remains independent of Scheduler logic.

---

# Design Principles

## Redis is transient.

All persistent state belongs elsewhere.

---

## Queue operations are atomic.

Duplicate execution must be prevented.

---

## Workers consume immutable Worker Manifests.

Execution contracts are never modified.

---

## Scheduler owns recovery.

Workers remain unaware of queue failures.

---

## Redis is replaceable.

The platform should tolerate Redis loss without losing scheduling state.

---

# Future Enhancements

Planned improvements include:

- Priority queues
- GPU-specific queues
- Delayed retry queues
- Dead-letter queues
- Queue statistics
- Multi-region Redis
- Redis Cluster
- Stream-based transport
- Adaptive polling

---

# Summary

Redis provides fast, transient work distribution between the Scheduler and Workers.

By treating Redis as a disposable transport layer rather than a persistent datastore, the platform remains resilient, recoverable, and horizontally scalable.

---

# Next Document

```
14-mqtt.md
```

This document describes telemetry, health reporting, event publishing, and monitoring integration using MQTT.