---
title: "2026-09-04 - Vite - Learning Point 3"
tags:
  - learning
  - vite
created: 2026-09-04
---

# Native ES Modules Enable On-Demand Loading

Vite uses native ES module syntax in the browser. Instead of bundling everything upfront, the browser only downloads the modules it actually needs for the current page. Each module is a separate HTTP request — lazy loaded on demand. Think of it like ordering one dish at a time instead of a full buffet at once.

## Key Takeaway
ESM's fine-grained loading means faster initial page loads and automatic code splitting without manual configuration.

## Related Concepts
- ES Modules (ESM)
- Lazy Loading
- Code Splitting

---

# 原生 ES 模塊實現按需加載

Vite 在瀏覽器中使用原生 ES 模塊語法。不是預先打包所有內容，而是瀏覽器只下載當前頁面實際需要的模塊。每個模塊都是一個獨立的 HTTP 請求——按需懶加載。可以把它想象成一次點一道菜，而不是一次過拿到全部自助餐。

## 核心要點
ESM 的細粒度加載意味著更快的初始頁面加載和自動代碼分割，無需手動配置。

## 相關概念
- ES 模塊（ES Modules / ESM）
- 懶加載（Lazy Loading）
- 代碼分割（Code Splitting）
