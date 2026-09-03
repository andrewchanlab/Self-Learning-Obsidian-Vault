---
title: "2026-09-04 - Vite - Learning Point 5"
tags:
  - learning
  - vite
created: 2026-09-04
---

# Production Builds Use Rollup for Optimized Output

While Vite uses esbuild for lightning-fast dev builds, production builds switch to Rollup — a mature, purpose-built bundler. Rollup produces highly optimized, tree-shaken output with smaller bundle sizes and better chunk splitting. It's the best of both worlds: fast dev and lean prod.

## Key Takeaway
Vite intelligently picks the right tool for each environment: esbuild for dev speed, Rollup for production optimization.

## Related Concepts
- Rollup
- Tree Shaking
- Bundle Optimization

---

# 生產構建使用 Rollup 輸出優化結果

Vite 在快速開發構建中使用 esbuild，但在生產構建時切換到 Rollup——一個成熟的、專門構建的打包器。Rollup 產生高度優化、去除了未使用代碼的輸出，擁有更小的包體積和更好的分塊分割。這是兩全其美的方案：開發快速，生產精簡。

## 核心要點
Vite 智能地為每個環境選擇合適的工具：開發用 esbuild 加速，生產用 Rollup 優化。

## 相關概念
- Rollup
-  Tree Shaking（去除死代碼）
-  包體積優化（Bundle Optimization）
