---
title: "2026-10-23 - Vite - Learning Point 16"
tags:
  - learning
  - vite
created: 2026-10-23
---

# Vite Library Mode: Building a Package Other People Install

### English

Almost everything Vite is famous for is about serving *your* application to *your* browser. But a large part of the JavaScript ecosystem is different: a **library** — a Vue component, a React hook, a design-system package, a CLI — that other developers install from npm and import into *their* applications. Vite can build that too, through **library mode**, enabled by setting `build.lib`.

The switch is small but changes the semantics of the build completely:

```js
import { defineConfig } from 'vite'
import { resolve } from 'node:path'

export default defineConfig({
  build: {
    lib: {
      entry: resolve(__dirname, 'src/index.ts'),
      name: 'MyLib',              // global variable name, required for umd/iife
      formats: ['es', 'cjs'],
      fileName: (format) => `index.${format === 'es' ? 'js' : 'cjs'}`,
      cssFileName: 'style',
    },
    rollupOptions: {
      external: [/^react($|\/)/, /^react-dom($|\/)/],
    },
  },
})
```

With `build.lib.entry` set, Vite stops doing an HTML-driven build and instead treats your entry (or entries) as the Rollup `input`. The default formats are `['es', 'umd']` for a single entry and `['es', 'cjs']` for multiple entries, and you can select from `es`, `cjs`, `umd` and `iife` explicitly. `umd` and `iife` require `name`, because those formats must collapse everything into one self-executing closure that assigns a value to a global — structurally they cannot represent multiple entry chunks or code splitting. If you configure `formats: ['es', 'umd']` together with multiple entries, Vite errors. The workaround is to run two separate builds with different `lib` configurations.

The single most important decision is **what to externalise**. `external` lists dependencies that should stay as bare `import` statements in the output rather than being inlined. For a React component library, React itself must be external — otherwise your package ships a second copy of React, which breaks hooks and context because React's internal state lives in module-level variables, and two copies means two separate states.

A trap lurks here: Rollup matches `external` string entries by **exact specifier equality**, not by prefix. `external: ['react']` keeps `import 'react'` out of the bundle but does nothing for `import 'react/jsx-runtime'`, which the automatic JSX transform emits in every file. Rollup resolves `react/jsx-runtime` from `node_modules` and inlines it — silently shipping a second copy of the runtime, with no build error at all. The fix is to use a regular expression:

```js
external: [/^react($|\/)/, /^react-dom($|\/)/]
```

Another subtlety is `output.globals`, a separate map from `external`. Only `umd` and `iife` read it, because those formats have no `import`/`require` — an external becomes a property lookup on a global object, and `globals` says which property. An external listed in `external` but missing from `globals` produces a UMD file that references an undefined variable and throws at load time. The `es` and `cjs` formats ignore `globals` entirely, which is why the same misconfiguration passes every ESM test and only explodes when someone drops the UMD file onto a page via a `<script>` tag.

The second big decision is **how granular the output should be**. By default the `es` output is one file with the whole reachable module graph concatenated in. That is ideal for a single cohesive utility but wrong for a component set where consumers import three of forty components. Setting `output.preserveModules: true` mirrors your source tree into `dist/`, one file per source module, which maximises downstream tree-shaking. The costs are real: many more files in the tarball, no cross-module inlining, and the need to pair it with `output.preserveModulesRoot: 'src'` so the `dist` tree does not carry a redundant `src/` prefix. `preserveModules` is also incompatible with `umd` and `iife`. And because preserved modules keep their top-level side effects, you should declare `sideEffects` in `package.json` (for example `"sideEffects": ["**/*.css"]`) so a consumer's tree-shaker does not drop your stylesheet import.

Finally, `package.json` is part of the build. The `exports` map is the authoritative resolver in modern Node and bundlers; `main` and `module` are legacy fallbacks. Note that the `types` condition must come **first** inside each `exports` block, because Node and TypeScript match conditions top-to-bottom and a `types` entry placed after `import`/`require` is silently skipped:

```json
{
  "name": "my-lib",
  "type": "module",
  "files": ["dist"],
  "main": "./dist/index.cjs",
  "module": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js",
      "require": "./dist/index.cjs"
    },
    "./style.css": "./dist/style.css"
  },
  "peerDependencies": { "react": ">=18" }
}
```

Vite also has a legacy `vite.config.js` field for library builds, but the `build.lib` approach is current. TypeScript declaration files are not generated by Vite itself — the community plugin `vite-plugin-dts` is the usual answer.

### 中文

Vite 最出名嘅用途基本上都係「服務你自己嘅應用畀你自己嘅瀏覽器」。但 JavaScript 生態入面有相當大一部分唔同：**library** —— 一個 Vue 元件、一個 React hook、一套 design system、一個 CLI —— 由其他開發者由 npm 安裝，再 import 落**佢哋**嘅應用入面。Vite 同樣可以打包呢啲，只要設定 `build.lib` 啟動 **library mode**。

改動非常細，但會徹底改變 build 嘅語意：

```js
import { defineConfig } from 'vite'
import { resolve } from 'node:path'

export default defineConfig({
  build: {
    lib: {
      entry: resolve(__dirname, 'src/index.ts'),
      name: 'MyLib',              // 全域變數名，umd/iife 必須
      formats: ['es', 'cjs'],
      fileName: (format) => `index.${format === 'es' ? 'js' : 'cjs'}`,
      cssFileName: 'style',
    },
    rollupOptions: {
      external: [/^react($|\/)/, /^react-dom($|\/)/],
    },
  },
})
```

一旦設定咗 `build.lib.entry`，Vite 就唔再做以 HTML 為入口嘅 build，而係將你嘅 entry（或多個 entry）當作 Rollup 嘅 `input`。預設格式喺單一 entry 係 `['es', 'umd']`，多個 entry 係 `['es', 'cjs']`；你亦可以明確指定 `es`、`cjs`、`umd`、`iife`。`umd` 同 `iife` 必須要有 `name`，因為呢兩種格式要把所有嘢壓縮成一個自我執行嘅 closure，再賦值俾一個全域變數 —— 結構上佢哋根本表達唔到多個 entry chunk 或者 code splitting。如果你同時用多個 entry 又寫 `formats: ['es', 'umd']`，Vite 會直接報錯。 workaround 就係分兩次 build，用唔同嘅 `lib` 設定。

最重要嘅決定係**邊啲嘢要 externalise（外置）**。`external` 列出嘅依賴會喺輸出入面保留為裸嘅 `import` 語句，而唔會被內聯。React 元件庫就必須將 React 本身 external —— 否則你個套件會打包多一份 React，因為 React 嘅內部狀態存喺模組層級變數，兩份就係兩份獨立狀態，hooks 同 context 全部壞掉。

呢度有個陷阱：Rollup 對 `external` 嘅字串項目係用**完全相等**嚟匹配 specifier，唔係前綴匹配。`external: ['react']` 會令 `import 'react'` 唔入包，但對 `import 'react/jsx-runtime'` 毫無作用 —— 而自動 JSX 轉換喺每個檔案都會產生後者。Rollup 會由 `node_modules` 解析 `react/jsx-runtime` 並將其內聯 —— 靜靜哋送咗多一份 runtime 出嚟，build 過程完全冇報錯。修正方法係用正則表達式：

```js
external: [/^react($|\/)/, /^react-dom($|\/)/]
```

另一個細節係 `output.globals`，同 `external` 係兩份唔同嘅清單。只有 `umd` 同 `iife` 會讀佢，因為呢兩種格式冇 `import`/`require` —— external 會變成對某個全域物件嘅屬性存取，而 `globals` 就係話明係邊個屬性。如果某個 external 喺 `external` 有、`globals` 冇，產生嘅 UMD 檔會引用一個未定義變數，一載入就拋錯。`es` 同 `cjs` 完全唔理會 `globals`，所以同一個設定錯誤可以通過所有 ESM 測試，直到有人用 `<script>` 標籤將 UMD 檔放上頁面先爆炸。

第二個大決定係**輸出要幾粒度**。預設情況下 `es` 輸出係一個檔案，整個可達模組圖被拼接入去。對單一完整嘅工具函數嚟講呢係最理想，但對元件集合就錯 —— 因為消費者通常只會 import 四十個入面嘅三個。設定 `output.preserveModules: true` 會將原始碼樹鏡射到 `dist/`，每個源模組一個檔案，令下游 tree-shaking 效果最大化。代價亦係實實在在：套件入面檔案數量大增、冇咗跨模組內聯，而且要配 `output.preserveModulesRoot: 'src'`，令 `dist` 唔會多咗一層冇必要嘅 `src/` 前綴。`preserveModules` 亦同 `umd`、`iife` 唔相容。而且因為保留咗模組嘅頂層副作用，你應該喺 `package.json` 宣告 `sideEffects`（例如 `"sideEffects": ["**/*.css"]`），以免消費者嘅 tree-shaker 把你個樣式表 import 咗去。

最後，`package.json` 本身都係 build 嘅一部分。`exports` map 係現代 Node 同 bundler 權威嘅解析方式；`main` 同 `module` 係舊式後備。注意 `types` 條件必須放喺每個 `exports` 區塊嘅**最前面**，因為 Node 同 TypeScript 由上至下匹配條件，`types` 放喺 `import`/`require` 之後會被無聲無息咁略過：

```json
{
  "name": "my-lib",
  "type": "module",
  "files": ["dist"],
  "main": "./dist/index.cjs",
  "module": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js",
      "require": "./dist/index.cjs"
    },
    "./style.css": "./dist/style.css"
  },
  "peerDependencies": { "react": ">=18" }
}
```

Vite 仲有一個舊式嘅 `vite.config.js` 欄位用嚟做 library build，但 `build.lib` 先係現行做法。而 TypeScript 嘅 `.d.ts` 宣告檔唔係由 Vite 自動生成 —— 社群插件 `vite-plugin-dts` 係最常見嘅答案。

## Key Takeaway
Library mode turns Vite into a package builder where the two decisive choices — what stays external and how granular the output is — determine whether consumers get a working, tree-shakable package.

## Related Concepts
- External Dependencies and Peer Dependencies
- Tree Shaking and sideEffects
- Package exports Maps
- Rollup Output Formats

## Diagram
```mermaid
flowchart TD
    SRC[src/index.ts + src/components/*] --> LIB[build.lib.entry]
    LIB --> EXT{external regex}
    EXT -->|react, react-dom| OUT[Kept as bare import]
    EXT -->|everything else| INL[Inlined into bundle]
    INL --> ES[dist/index.js (es)]
    INL --> CJS[dist/index.cjs (cjs)]
    INL --> UMD[dist/index.umd.js (umd, needs globals map)]
    OUT --> ES
    OUT --> CJS
    OUT --> UMD
    PM[output.preserveModules] -.->|optional| ES
    PKG[package.json exports map] --> RESOLVER[Consumer bundler]
    ES --> RESOLVER
    CJS --> RESOLVER
```
