---
title: "2026-09-04 - Elasticsearch - Learning Point 4"
tags:
  - learning
  - elasticsearch
created: 2026-09-04
---

# Near-Real-Time Indexing via Segmented Architecture

New documents go to an in-memory buffer, then flush to a Lucene segment (immutable). Segments become searchable within ~1 second (NRT = near-real-time). This segment-based design enables Elasticsearch to handle petabytes while maintaining search performance.

## Key Takeaway
Elasticsearch's near-real-time search capability comes from its immutable segment architecture — new documents are searchable within ~1 second.

## Related Concepts
- Segment Architecture
- Near Real-Time
- Index Refresh
