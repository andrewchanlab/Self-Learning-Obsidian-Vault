---
title: "2026-09-05 - Vite - Learning Point 8"
tags:
  - learning
  - vite
created: 2026-09-05
---

# Vite 的 CSS 處理：CSS Modules 與 PostCSS 支援

Vite 對 CSS 的支援開箱即用。你可以直接 import CSS 檔案，Vite 會自動處理，而且支援 CSS Modules——只要檔名是 `*.module.css`，Vite 會把類名自動加上 hash 避免衝突。這對於 component-level styling 非常重要，因為不同 component 的 `.button` 類名不會互相覆蓋。Vite also supports PostCSS out of the box，只要專案根目錄有 `postcss.config.js` 或 `postcss.config.cjs`，Vite 就會自動應用 PostCSS 插件（如 Autoprefixer、CSS Nano）。

## CSS Modules 範例
```css
/* Button.module.css */
.button { color: blue; }
```
```js
// Component.jsx
import styles from './Button.module.css'
// styles.button === "Button_button_1x2y3"
```

## PostCSS 的角色
PostCSS 是一個 CSS-to-CSS 編譯器，允許你用 JavaScript 插件轉換 CSS。Vite 整合它之後，你可以用 Autoprefixer 自動加瀏覽器前綴，或用 CSS Nano 壓縮 CSS。

## Related Concepts
- CSS Modules and scoped class names
- PostCSS plugins ecosystem
- Autoprefixer, CSS Nano
- Scoped CSS in component libraries
