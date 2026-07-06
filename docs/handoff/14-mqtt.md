# MQTT

**Document:** 14-mqtt.md

---

# Purpose

MQTT provides lightweight telemetry and event distribution throughout the Intel GPU Validation Lab.

It enables real-time monitoring without participating in scheduling or test execution.

MQTT is strictly informational.

The platform must remain fully operational when MQTT is unavailable.

---

# Responsibilities

MQTT owns:

- Worker telemetry
- Health reporting
- Event publishing
- Performance metrics
- Operational notifications

MQTT does **not** own:

- Scheduling
- Queue management
- Worker registration
- Heartbeats
- Results
- Build publication

Those responsibilities belong to other services.

---

# High-Level Architecture

```
             Worker
                │
                ▼
             MQTT Broker
        ┌───────┼────────┐
        ▼       ▼        ▼
 Dashboard Monitoring Logging
```

MQTT distributes information to interested consumers.

---

# Why MQTT?

The validation lab contains hundreds of Workers.

Continuously polling every Worker would not scale well.

Instead:

```
Worker

↓

Publish

↓

Subscribers receive updates
```

This minimizes network traffic and simplifies monitoring.

---

# Broker

Recommended implementation:

```
Eclipse Mosquitto
```

Reasons:

- Lightweight
- Stable
- Well supported
- Easy to deploy
- Docker friendly

The broker remains independent of the Scheduler.

---

# Topics

Recommended topic hierarchy:

```
workers/

scheduler/

cache/

events/

system/
```

Hierarchical topics simplify subscriptions.

---

# Worker Topics

Each Worker publishes:

```
workers/<worker-id>/status

workers/<worker-id>/performance

workers/<worker-id>/cache

workers/<worker-id>/events
```

Consumers may subscribe selectively.

---

# Scheduler Topics

The Scheduler publishes:

```
scheduler/status

scheduler/campaigns

scheduler/events
```

These topics describe overall system activity.

---

# Cache Topics

Artifact Manager publishes:

```
cache/hits

cache/misses

cache/cleanup

cache/downloads
```

These metrics support optimization efforts.

---

# Event Topics

Examples:

```
events/build-published

events/campaign-created

events/worker-online

events/worker-offline

events/shard-completed

events/shard-failed
```

Events provide operational visibility.

---

# Message Format

Recommended payload:

```json
{
    "timestamp": "...",

    "worker_id": "...",

    "type": "...",

    "payload": {}
}
```

Messages should remain compact.

---

# Quality of Service

Recommended defaults:

Status

```
QoS 0
```

Events

```
QoS 1
```

Critical operational notifications

```
QoS 2
```

Higher QoS should be used sparingly.

---

# Retained Messages

Recommended retained topics:

```
workers/<id>/status

scheduler/status
```

Subscribers immediately receive current system state.

Transient events should never be retained.

---

# Worker Status

Workers periodically publish:

- State
- Current shard
- CPU usage
- Memory usage
- GPU utilization
- Disk usage
- Cache statistics

Publishing interval:

```
30 seconds
```

This interval is independent of Scheduler heartbeats.

---

# Performance Metrics

Workers publish:

- Shards completed
- Average execution time
- Cache hit rate
- Download throughput
- Extraction time
- Queue wait time

Metrics assist capacity planning.

---

# Cache Metrics

Artifact Manager publishes:

- Cache hits
- Cache misses
- Cache size
- Active references
- Cleanup events

These metrics help tune cache policies.

---

# Scheduler Metrics

Scheduler publishes:

- Active campaigns
- Pending shards
- Running shards
- Active Workers
- Retry count
- Queue depth

Operational dashboards consume these metrics.

---

# Failure Handling

MQTT failures are non-fatal.

```
Publish failure

↓

Log warning

↓

Continue execution
```

Workers never retry indefinitely.

Execution proceeds normally.

---

# Authentication

Recommended:

- TLS
- Username/password
- Client certificates (future)

Anonymous access should not be enabled.

---

# Configuration

Typical configuration:

```
Broker URL

Credentials

TLS

Client ID

Publish interval

QoS

Topic prefix
```

MQTT configuration is independent of Worker configuration.

---

# Design Principles

## MQTT is optional.

Execution never depends on telemetry.

---

## Publish only.

Workers should not require MQTT subscriptions for normal operation.

---

## Keep messages small.

Telemetry should not become a bandwidth bottleneck.

---

## Topics remain hierarchical.

Consumers subscribe only to what they need.

---

## Metrics complement persistent state.

Operational metrics are not a replacement for database records.

---

# Future Enhancements

Planned improvements include:

- Prometheus bridge
- Grafana integration
- OpenTelemetry exporter
- WebSocket gateway
- Fleet dashboards
- Alerting integration
- Historical telemetry aggregation
- Machine learning anomaly detection

---

# Summary

MQTT provides scalable, real-time telemetry for the Intel GPU Validation Lab.

By separating operational visibility from execution, the platform remains resilient while still offering rich monitoring and observability capabilities.

---

# Next Document

```
15-dashboard.md
```

This document describes the operational dashboard, campaign visualization, worker monitoring, and system health views.