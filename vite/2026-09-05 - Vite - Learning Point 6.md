---
title: "2026-09-05 - Vite - Learning Point 6"
tags:
  - learning
  - vite
created: 2026-09-05
---

# Vite 的生產建置：Rollup 打包而不是 ESM

Vite 在開發環境使用原生 ESM 讓瀏覽器分擔打包工作，但生產環境則完全不同——Vite 會呼叫 Rollup 將所有模組打包成少量靜態檔案。Rollup 支援 tree-shaking，會移除從未使用的程式碼（dead code elimination），所以最終 bundle 通常比開發版本小很多。Vite 的生產建置 also runs code splitting so each dynamic import() becomes its own chunk, enabling better caching. 你可以在 vite.config.ts 裡調整 rollupOptions 來控制輸出檔案名稱、code splitting 策略或 externals。

## 重要區分
- **開發環境**：原生 ESM，瀏覽器即時請求每個模組，no bundling
- **生產環境**：Rollup bundler + tree-shaking + code splitting，optimised static assets

## 為什麼這樣設計？
開發時要快速重載，生產時要最小化傳輸體積。兩種需求剛好相反，所以 Vite 採用不同的工具處理。

## Related Concepts
- Rollup bundler and its plugin ecosystem
- Tree-shaking（移除未使用程式碼）
- Code splitting（動態 import 分塊）
- Chunk splitting strategy
