---
title: "2026-09-04 - StreamLit - Learning Point 5"
tags:
  - learning
  - streamlit
created: 2026-09-04
---

# Session State Persists Data Across Widget Interactions

Streamlit normally reruns the entire script on every interaction, which would reset all variables. `st.session_state` solves this by storing values that persist across reruns. It's the key to building multi-step forms, counters, and stateful UIs — without session state, your app would forget everything between clicks.

## Key Takeaway
`st.session_state` is Streamlit's answer to statelessness — it preserves data across script reruns, enabling truly interactive applications.

## Related Concepts
- State Management
- Web Sessions
- Callback Functions

---

# Session State 在組件互動中保持數據持久

Streamlit 通常在每次互動時重新執行整個腳本，這會重置所有變數。`st.session_state` 解決了這個問題——它儲存的值能在多次執行之間保持。這是構建多步驟表單、計數器和有狀態 UI 的關鍵。沒有 session state，你的應用在每次點擊後都會忘記所有東西。

## 核心要點
`st.session_state` 是 Streamlit 應對無狀態問題的方案——它能在腳本重新執行之間保留數據，實現真正的互動應用。

## 相關概念
- 狀態管理
- Web 會話
- 回調函數
