---
title: "2026-09-04 - Elasticsearch - Learning Point 2"
tags:
  - learning
  - elasticsearch
created: 2026-09-04
---

# Distributed by Design — Shards and Replicas

An Elasticsearch index is split into shards (default 5) distributed across nodes. Each shard is a full-text search engine running Lucene. Replicas provide fault tolerance — if a node dies, its shards are served by replicas on other nodes. You scale by adding nodes; Elasticsearch rebalances automatically.

## Key Takeaway
Elasticsearch's sharding architecture enables horizontal scale and fault tolerance — data is distributed across the cluster with automatic failover.

## Related Concepts
- Sharding
- Data Replication
- Distributed Systems
