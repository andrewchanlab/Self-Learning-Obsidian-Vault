---
title: "2026-09-03 - Streamlit - Learning Point 1"
tags:
  - learning
  - streamlit
created: 2026-09-03
---

# Streamlit Uses a Script Model — Every Script Run Is a Full Re-Render

Streamlit apps are single-page Python scripts that re-run top-to-bottom on every user interaction. There is no request/response cycle — the framework re-executes your script when a widget changes, and Streamlit intelligently updates only the affected widgets. This makes state management different from traditional web frameworks; you use `st.session_state` to persist data across reruns.

## Key Takeaway
Streamlit re-runs the entire script on every interaction; use st.session_state for persistence.

## Related Concepts
- Script Model
- st.session_state
- Widget Re-render

---

# Streamlit 使用腳本模型——每次運行都是完整重新渲染

Streamlit 應用是單頁 Python 腳本，每次用戶交互都會從頭到尾重新運行。沒有請求/響應週期——當 widget 發生變化時，框架會重新執行你的腳本，Streamlit 會智能地只更新受影響的 widget。這使得狀態管理與傳統 Web 框架不同；你需要使用 `st.session_state` 來在多次運行間持久化數據。

## 核心要點
Streamlit 每次交互都重新運行整個腳本；用 st.session_state 實現持久化。

## 相關概念
- 腳本模型
- st.session_state
- Widget 重新渲染
