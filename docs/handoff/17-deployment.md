# Deployment

**Document:** 17-deployment.md

---

# Purpose

This document describes the deployment architecture of the Intel GPU Validation Lab.

The platform is designed to be simple to deploy, easy to operate, and straightforward to scale.

Docker Compose is the primary deployment method.

Future deployments may use Kubernetes without requiring architectural changes.

---

# Deployment Goals

The deployment should provide:

- Reproducible environments
- Minimal configuration
- Stateless services
- Simple upgrades
- Easy debugging
- Horizontal scalability

---

# Deployment Topology

```
                +----------------------+
                |      Scheduler       |
                +----------+-----------+
                           |
        +------------------+------------------+
        |        |          |        |        |
        ▼        ▼          ▼        ▼        ▼
   PostgreSQL  Redis      MinIO   Dashboard  Builder
                                         (served by Scheduler)

                           |
                    Worker Fleet
        +---------+---------+---------+---------+
        |         |         |         |         |
      tgl-01    tgl-02    lnl-01    bmg-01   ...
```

The Scheduler coordinates the entire platform.

---

# Core Services

The platform consists of:

- Scheduler
- PostgreSQL
- Redis
- MinIO
- Builder(s)
- Worker(s)

The Dashboard is served directly by the Scheduler.

---

# Docker Images

Recommended images:

```
intel-gpu-scheduler

intel-gpu-worker

intel-gpu-builder
```

Supporting infrastructure uses upstream images:

```
postgres

redis

minio/minio
```

---

# Docker Compose

Infrastructure services are deployed using a common Compose file.

Example services:

```
scheduler

postgres

redis

minio
```

Workers are deployed independently on validation machines.

---

# Worker Deployment

Every Worker machine runs the same Docker Compose configuration.

Example:

```yaml
services:
  worker:
    image: intel-gpu-worker:latest

    restart: unless-stopped

    network_mode: host

    uts: host

    devices:
      - /dev/dri

    volumes:
      - /var/cache/intel-gpu-validation:/cache
      - /var/log/intel-gpu-validation:/logs
```

The Worker image is identical across the fleet.

---

# Worker Identity

Workers derive their identity from the host operating system.

```
socket.gethostname()
```

Because the container shares the host UTS namespace:

```yaml
uts: host
```

The Worker automatically registers using the machine hostname.

Examples:

```
tgl-01

lnl-02

bmg-04
```

No worker-specific container configuration is required.

---

# Builder Deployment

Builders run independently from Workers.

Typical deployment:

```
builder-01

builder-02
```

Builders execute Buildbot jobs and publish artifacts.

Builders are horizontally scalable.

---

# Storage

Persistent storage includes:

```
PostgreSQL

MinIO

Worker Cache
```

Redis remains transient.

---

# Persistent Volumes

Recommended volume layout:

```
postgres-data/

minio-data/

worker-cache/

worker-logs/
```

Persistent data survives container upgrades.

---

# Networking

Recommended:

```
network_mode: host
```

for Workers.

Infrastructure services communicate over a private network.

External access is limited to the Scheduler.

---

# Service Discovery

Infrastructure services use stable DNS names.

Examples:

```
scheduler

postgres

redis

minio
```

Workers identify themselves using the host hostname.

---

# Configuration

Configuration should be supplied through:

- Environment variables
- Configuration files
- Docker secrets

Container images remain immutable.

---

# Logging

Logs should be written to:

```
/var/log/intel-gpu-validation/
```

Host-mounted log directories simplify troubleshooting.

---

# Upgrades

Rolling Worker upgrade:

```
Drain Worker

↓

Finish active shard

↓

Replace container

↓

Register

↓

Resume work
```

Scheduler upgrades should preserve PostgreSQL state.

---

# Scaling

Scale Builders by adding additional build machines.

Scale Workers by adding additional validation machines.

The Scheduler remains the central control plane.

---

# Monitoring

Operational monitoring includes:

- Scheduler health
- Worker health
- Queue depth
- Cache utilization
- Database health
- Storage utilization

The Dashboard provides a unified view.

---

# Backup

Recommended backups:

- PostgreSQL
- MinIO

Worker caches do not require backup.

They are disposable.

---

# Design Principles

## Containers are immutable.

Runtime configuration is external.

---

## Worker images are identical.

Identity comes from the host hostname.

---

## Scheduler is the control plane.

Workers remain stateless.

---

## Persistent data is centralized.

Worker caches are expendable.

---

## Docker Compose is the reference deployment.

Alternative orchestrators should preserve the same architecture.

---

# Future Enhancements

Planned improvements include:

- Kubernetes deployment
- Helm charts
- High-availability Scheduler
- PostgreSQL replication
- Redis Sentinel
- MinIO distributed mode
- Automated upgrades
- Fleet management

---

# Summary

The Intel GPU Validation Lab is designed for simple, reproducible deployment using Docker Compose.

By keeping Worker images identical and deriving Worker identity from the host through the shared UTS namespace, the platform minimizes configuration while remaining easy to operate and scale.

---

# Next Document

```
18-roadmap.md
```

This document outlines the implementation phases, milestones, future enhancements, and long-term vision for the platform.