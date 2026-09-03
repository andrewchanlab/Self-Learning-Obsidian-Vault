---
title: "2026-09-03 - Streamlit - Learning Point 5"
tags:
  - learning
  - streamlit
created: 2026-09-03
---

# st.file_uploader and st.download_button Handle File I/O Natively

Streamlit has built-in widgets for file operations: `st.file_uploader` accepts file uploads with type/size constraints, returning a BytesIO object. `st.download_button` triggers a file download in the browser. Combined with `st.session_state`, these enable upload - process - download workflows entirely within Streamlit — no Flask routes or HTML forms needed.

## Key Takeaway
st.file_uploader and st.download_button enable complete file workflows without Flask or HTML.

## Related Concepts
- st.file_uploader
- st.download_button
- BytesIO

---

# st.file_uploader 和 st.download_button 原生處理文件 I/O

Streamlit 有內置的 widget 處理文件操作：`st.file_uploader` 接受文件上傳並支持類型/大小限制，返回 BytesIO 對象。`st.download_button` 在瀏覽器中觸發文件下載。配合 `st.session_state`，這些支持完全在 Streamlit 內完成上傳 → 處理 → 下載工作流程——無需 Flask 路由或 HTML 表單。

## 核心要點
st.file_uploader 和 st.download_button 無需 Flask 或 HTML 即可實現完整文件工作流程。

## 相關概念
- st.file_uploader
- st.download_button
- BytesIO
