---
title: "2026-03-25 - StreamLit - Learning Point 3"
tags:
  - learning
  - streamlit
created: 2026-03-25
---

# Caching: Avoiding Expensive Recomputation

Streamlit's `@st.cache_data` decorator solves the performance problem caused by its re-run model. When a function is decorated with `@st.cache_data`, Streamlit stores its return values keyed by the function's input arguments. On subsequent calls with the same inputs, it returns the cached result instantly without re-executing the function. This is critical for expensive operations like loading ML models, querying databases, or downloading large datasets — without caching, every slider change would re-trigger a 30-second data load, making the app unusable.

## Key Takeaway
Use `@st.cache_data` for any function that takes more than ~100ms to run — it's the difference between a snappy app and a sluggish one.

## Related Concepts
- st.cache_data vs st.cache_resource
- TTL-based cache expiration
- Cache invalidation strategies
