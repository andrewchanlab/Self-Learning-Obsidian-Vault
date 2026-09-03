---
title: "2026-09-05 - Vite - Learning Point 7"
tags:
  - learning
  - vite
created: 2026-09-05
---

# Vite Config 中的路徑別名（Path Alias）設定

在大型專案裡不斷寫 `../../../../components/Button` 既冗長又容易出錯。Vite 讓你在 `vite.config.ts` 用 `resolve.alias` 設定路徑別名，例如把 `@` 指向 `src` 目錄。設定後，程式碼裡可以直接寫 `import Button from '@/components/Button'`，Vite 會在預覽和建置時都正確解析。TypeScript 專案還需要在 `tsconfig.json` 的 `paths` 欄位加入相同設定，讓 IDE 也能識別這些別名。

## 設定範例
```ts
// vite.config.ts
resolve: {
  alias: {
    '@': '/src',
    '@components': '/src/components',
  }
}
```

## 常見錯誤
如果只改了 `vite.config.ts` 但沒改 `tsconfig.json`，dev server 正常但 `tsc` 編譯會失敗。兩邊必須同步。

## Related Concepts
- TypeScript path mapping（tsconfig.json paths）
- Module resolution（模組解析機制）
- Absolute vs relative imports
