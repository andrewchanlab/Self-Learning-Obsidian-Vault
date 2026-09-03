---
title: "2026-09-03 - Streamlit - Learning Point 3"
tags:
  - learning
  - streamlit
created: 2026-09-03
---

# st.cache Decorators Prevent Repeated Expensive Computations

Streamlit's `@st.cache_data` and `@st.cache_resource` decorators memoize function results. `@st.cache_data` caches return values — ideal for expensive data transformations or API calls. `@st.cache_resource` caches global resources like database connections. Cache invalidation is controlled via `ttl` (time-to-live) or `max_entries`. Without caching, every rerun recomputes everything from scratch.

## Key Takeaway
@st.cache_data and @st.cache_resource memoize results to avoid recomputation on every rerun.

## Related Concepts
- @st.cache_data
- @st.cache_resource
- Memoization

---

# st.cache 裝飾器防止重複昂貴計算

Streamlit 的 `@st.cache_data` 和 `@st.cache_resource` 裝飾器會緩存函數結果。`@st.cache_data` 緩存返回值——適合昂貴的數據轉換或 API 調用。`@st.cache_resource` 緩存全局資源如數據庫連接。緩存失效可通過 `ttl`（生存時間）或 `max_entries` 控制。沒有緩存，每次重新運行都會從頭開始重算所有內容。

## 核心要點
@st.cache_data 和 @st.cache_resource 緩存結果以避免每次運行重新計算。

## 相關概念
- @st.cache_data
- @st.cache_resource
- 記憶化
