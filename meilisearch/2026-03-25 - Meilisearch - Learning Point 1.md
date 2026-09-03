---
title: "2026-03-25 - Meilisearch - Learning Point 1"
tags:
  - learning
  - meilisearch
created: 2026-03-25
---

# Instant Search Through Inverted Indices

Meilisearch is built on top of LMDB (an extremely fast key-value store) and uses an inverted index as its core data structure. An inverted index maps every searchable term to the document IDs that contain it — imagine a book's index at the back that tells you which pages contain each word. When you search "machine learning," the engine looks up "machine" and "learning" in the index, finds the intersecting document IDs, and returns results in milliseconds. This is fundamentally faster than scanning every document (full-text search) because the lookup is O(1) rather than O(n).

## Key Takeaway
Meilisearch's inverted index makes search O(1) per query — no matter how many documents you have, search speed stays constant.

## Related Concepts
- Inverted index data structure
- Term frequency and relevance scoring
- BM25 ranking algorithm
