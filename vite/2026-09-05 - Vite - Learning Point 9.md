---
title: "2026-09-05 - Vite - Learning Point 9"
tags:
  - learning
  - vite
created: 2026-09-05
---

# Vite 與 TypeScript：esbuild 加速類型檢查

Vite 使用 esbuild 來轉譯 TypeScript，esbuild 比 tsc 快 10-100 倍，所以 Vite 的 TS 編譯幾乎是即時的。但這裡有個重要的陷阱：esbuild 只做語法轉譯（transpile），不 做型別檢查（type checking）。也就是說 `const x: number = "hello"` 這種錯誤在 Vite dev server 裡不會被發現，只有執行 `tsc --noEmit` 才會報錯。對於大型專案，這是個值得注意的限制——很多人以為 `vite build` 會catch所有 TS 錯誤，實際上它不會。

## 解決方案
- 小型專案：`vite-plugin-checker` 在 dev 時執行 `tsc --noEmit`
- 大型專案：CI pipeline 裡单独跑 `tsc --noEmit`
- 注意：`vue-tsc`（Vue 官方）是用於 `.vue` 檔案的 type checking

## Vite 的編譯流程（簡化）
1. `*.ts/*.vue` → esbuild transpile → JS（快速，無類型檢查）
2. 輸出結果送到瀏覽器
3. 型別檢查需要单独运行 tsc

## Related Concepts
- esbuild 與 tsc 的差異
- TypeScript type checking vs transpiling
- vite-plugin-checker
- vue-tsc
