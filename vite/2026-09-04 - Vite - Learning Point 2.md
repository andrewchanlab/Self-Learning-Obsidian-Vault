---
title: "2026-09-04 - Vite - Learning Point 2"
tags:
  - learning
  - vite
created: 2026-09-04
---

# Hot Module Replacement Updates Only What Changed

When you edit a file, Vite doesn't reload the whole page — it swaps just that module in the browser. Your app state (form inputs, scroll position) survives. This is like replacing one Lego block without dismantling the entire structure.

## Key Takeaway
Vite's HMR preserves application state while instantly updating changed modules — the fastest possible feedback loop during development.

## Related Concepts
- Hot Module Replacement
- State Preservation
- Fast Refresh

---

# 熱模塊替換只更新變更的部分

當你編輯文件時，Vite 不會重新載入整個頁面——它只會在瀏覽器中替換那個模塊。你的應用狀態（表單輸入、滾動位置）得以保留。這就像更換一塊樂高積木，而不需要拆掉整個結構。

## 核心要點
Vite 的 HMR 在即時更新變更模塊的同時保留應用狀態——這是開發過程中最快的反饋循環。

## 相關概念
- 熱模塊替換（Hot Module Replacement）
- 狀態保留（State Preservation）
- 快速刷新（Fast Refresh）
