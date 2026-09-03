---
title: "2026-03-25 - Meilisearch - Learning Point 2"
tags:
  - learning
  - meilisearch
created: 2026-03-25
---

# Typo Tolerance and Search-as-you-Type

One of Meilisearch's defining features is its built-in typo tolerance. It uses a custom algorithm that allows 1 typo for words of 5+ characters and 2 typos for words of 9+ characters. More importantly, Meilisearch implements prefix search — searching "mach" matches "machine," "match," and "macho" because all these words start with the prefix "mach." Combined with its "search-as-you-type" experience (results update with each keystroke), this creates a Google-like instant search feel that's remarkably hard to build from scratch.

## Key Takeaway
Meilisearch handles the hard parts of search UX automatically — typo tolerance, prefix matching, and instant results without extra configuration.

## Related Concepts
- Typo tolerance algorithms (Damerau-Levenshtein distance)
- Prefix matching and n-gram tokenization
- Relevant sorting vs lexical sorting
