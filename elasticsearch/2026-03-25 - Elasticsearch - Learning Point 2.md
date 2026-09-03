---
title: "2026-03-25 - Elasticsearch - Learning Point 2"
tags:
  - learning
  - elasticsearch
created: 2026-03-25
---

# Distributed Architecture: Shards, Replicas, and Recovery

Elasticsearch scales horizontally by distributing indices across nodes as shards. Each index is split into primary shards (the authoritative copy) and replica shards (copies for read scaling and fault tolerance). When a node fails, Elasticsearch automatically reassigns its shards to healthy nodes using the cluster state. The coordinator node that receives a search request fans out the query to all relevant shards (primary or replica), collects results, merges them using the `track_total_hits` parameter, and returns a unified response. This distributed model enables near-linear scalability — double the nodes, roughly double the throughput.

## Key Takeaway
Elasticsearch's masterless cluster design means any node can coordinate searches, and automatic shard rebalancing handles failures without manual intervention.

## Related Concepts
- Primary and replica shard roles
- Cluster state and the elected master node
- Query fan-out and result merging
