---
title: "2026-09-05 - Vite - Learning Point 10"
tags:
  - learning
  - vite
created: 2026-09-05
---

# Vite Plugin 生態系：官方、社群與如何選擇

Vite 的插件系統與 Rollup 插件相容，但有些只適用於 Vite 的特殊鉤子（hooks）。官方維護的插件包括 `@vitejs/plugin-vue`（Vue SFC 支援）、`@vitejs/plugin-react`（React Fast Refresh）、`@vitejs/plugin-legacy`（向後相容）。社群插件則涵蓋 SSR、圖片優化、PWA 等場景。選擇插件時要注意：有些是為 Rollup 設計的，有些是專為 Vite 設計（用 `vite-plugin-` 前綴），混用可能導致問題。

## 常用插件分類
| 類別 | 範例 |
|------|------|
| Framework | `@vitejs/plugin-vue`, `@vitejs/plugin-react` |
| SSR | `vite-plugin-ssr`, `vike` |
| 圖片優化 | `vite-plugin-imagemin`, `vite-image` |
| PWA | `vite-plugin-pwa` |
| 環境變數 | `dotenv`（內建支援） |

## 寫 Plugin 的基本概念
Vite 插件是一個物件，有 `name`、`apply`（套用到哪個階段）和一組 hook 函數。每個 hook 接收 `VirtualModule` 或 `TransformResult`，可以在 transform 階段修改模組內容。

## Related Concepts
- Rollup plugin compatibility
- Vite specific hooks (configureServer, transformIndexHtml)
- Official vs community plugins
- Plugin ordering and enforcement
