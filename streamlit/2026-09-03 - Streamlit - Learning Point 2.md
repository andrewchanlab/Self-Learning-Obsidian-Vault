---
title: "2026-09-03 - Streamlit - Learning Point 2"
tags:
  - learning
  - streamlit
created: 2026-09-03
---

# st.session_state Is the Built-In State Management Primitive

`st.session_state` is a dict-like object that persists variables across Streamlit reruns. Initialize with `if 'key' not in st.session_state: st.session_state['key'] = value`. Widgets can be bound to session state keys using the `key` parameter, making widget values directly accessible. This is the foundation for building interactive, stateful Streamlit applications.

## Key Takeaway
st.session_state persists variables and widget values across reruns.

## Related Concepts
- State Persistence
- Widget key Parameter
- Callback Functions

---

# st.session_state 是內置的狀態管理原語

`st.session_state` 是一個類似字典的對象，在 Streamlit 重新運行期間持久保存變量。用 `if 'key' not in st.session_state: st.session_state['key'] = value` 初始化。Widget 可以使用 `key` 參數綁定到 session state 鍵，使 widget 值可直接訪問。這是構建交互式、有狀態 Streamlit 應用的基礎。

## 核心要點
st.session_state 在多次運行間持久保存變量和 widget 值。

## 相關概念
- 狀態持久化
- Widget key 參數
- 回調函數
