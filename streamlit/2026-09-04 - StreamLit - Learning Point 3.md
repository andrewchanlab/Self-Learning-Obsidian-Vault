---
title: "2026-09-04 - StreamLit - Learning Point 3"
tags:
  - learning
  - streamlit
created: 2026-09-04
---

# Widgets Are Just Function Calls

Interactive elements in Streamlit are one-liners: `st.slider()`, `st.checkbox()`, `st.selectbox()`, `st.file_uploader()`. Each returns a value you use in your code directly. No HTML forms, no JavaScript event handlers — just Python variables bound to UI elements.

## Key Takeaway
Streamlit widgets abstract away all JavaScript/DOM complexity — UI interactivity becomes plain Python function calls.

## Related Concepts
- UI Components
- Python Decorators
- Form Handling

---

# 組件只是函數調用

Streamlit 的互動元素只需一行代碼：`st.slider()`、`st.checkbox()`、`st.selectbox()`、`st.file_uploader()`。每個都會直接返回一個值供你使用。不用 HTML 表單，不用 JavaScript 事件處理器——只有綁定到 UI 元素的 Python 變數。

## 核心要點
Streamlit 組件將所有 JavaScript/DOM 複雜性封裝隱藏——UI 互動變成了簡單的 Python 函數調用。

## 相關概念
- UI 組件
- Python 裝飾器
- 表單處理
