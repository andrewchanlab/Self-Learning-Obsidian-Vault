---
title: "2026-03-25 - Elasticsearch - Learning Point 1"
tags:
  - learning
  - elasticsearch
created: 2026-03-25
---

# Lucene: The Search Engine Underneath

Elasticsearch is built on Apache Lucene, a Java library that handles indexing and searching. Each Elasticsearch shard is a Lucene index — a directory of files containing an inverted index, stored field data, and a terms dictionary. When you index a document, Lucene tokenizes the text, lowercases it, removes stop words, applies stemming ("running" → "run"), and builds an inverted index mapping each term to the documents containing it. This is why Elasticsearch can search billions of documents: the inverted index makes lookups O(1) rather than O(n) document scans.

## Key Takeaway
Understanding Lucene is key to understanding Elasticsearch — every ES node, shard, and query ultimately runs Lucene code under the hood.

## Related Concepts
- Inverted indices and the terms dictionary
- Text analysis: tokenization, stemming, stop words
- Shards as Lucene indices
