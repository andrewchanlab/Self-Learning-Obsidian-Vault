---
title: "2026-09-04 - Vite - Learning Point 1"
tags:
  - learning
  - vite
created: 2026-09-04
---

# Vite Skips Bundling During Development for Instant Start

Traditional bundlers (Webpack, Rollup) must scan and bundle your entire dependency tree before serving the first page. Vite serves native ES modules directly to the browser — no bundling step needed. Dev server starts in ~100ms regardless of project size.

## Key Takeaway
Vite's esbuild-powered dependency pre-bundling eliminates the startup wait, making dev servers feel instantaneous even in large projects.

## Related Concepts
- ES Modules
- Build Tooling
- Dev Server

---

# Vite 跳過打包過程，實現即時啟動

傳統打包工具（Webpack、Rollup）在提供第一個頁面之前，必須掃描並打包整個依賴樹。Vite 直接將原生 ES 模塊提供給瀏覽器——無需打包步驟。無論項目多大，開發伺服器都能在約 100ms 內啟動。

## 核心要點
Vite 的 esbuild 驅動依賴預打包消除了啟動等待時間，讓大型項目的開發伺服器也能感覺瞬間響應。

## 相關概念
- ES 模塊（ES Modules）
- 構建工具（Build Tooling）
- 開發伺服器（Dev Server）
