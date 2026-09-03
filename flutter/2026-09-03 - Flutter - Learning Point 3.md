---
title: "2026-09-03 - Flutter - Learning Point 3"
tags:
  - learning
  - flutter
created: 2026-09-03
---

# InheritedWidget vs Context — Accessing Data Without Prop Drilling

## English

Flutter's `BuildContext` is your handle to the **widget tree** — when you call `Theme.of(context)` or `MediaQuery.of(context)`, you're really searching up the tree for the nearest ancestor of that type. `InheritedWidget` is the mechanism that makes this search efficient by caching the data at a known tree location.

When to use `InheritedWidget` directly: when you need to share **rarely-changing** data (themes, locales, auth state) across a large subtree without passing it through every constructor. For frequently-changing state, use Riverpod's `Provider` or `InheritedModel` instead — they rebuild only what listens to the specific data.

`context.watch<T>()` (Riverpod) and `InheritedWidget.updateShouldNotify()` both prevent unnecessary rebuilds by tracking who actually cares about the data.

### Key Takeaway
`BuildContext` walks the widget tree upward to find `InheritedWidget`s. Use `InheritedWidget` for stable shared state; prefer Riverpod Provider for reactive/frequently-changing state to avoid unnecessary widget rebuilds.

### Related Concepts
- BuildContext
- InheritedWidget
- InheritedModel
- Riverpod Provider
- context.watch / context.read

---

## 中文

Flutter 的 `BuildContext` 是你訪問** widget 樹**的 handle——當你調用 `Theme.of(context)` 或 `MediaQuery.of(context)` 時，你實際上是在樹中向上搜索該類型的最近祖先。`InheritedWidget` 是通過在已知樹位置緩存數據來使這種搜索高效的機制。

何時直接使用 `InheritedWidget`：當你需要在大子樹中共享**很少變化**的數據（主題、語言環境、認證狀態）而不通過每個構造函數傳遞時。對於經常變化的狀態，改用 Riverpod 的 `Provider` 或 `InheritedModel`——它們只重建實際關注特定數據的部分。

`context.watch<T>()`（Riverpod）和 `InheritedWidget.updateShouldNotify()` 都通過追蹤誰真正關心這個數據來防止不必要的重建。

### 核心要點
`BuildContext` 向上遍歷 widget 樹以找到 `InheritedWidget`s。對穩定的共享狀態使用 `InheritedWidget`；對於響應式/經常變化的狀態，首選 Riverpod Provider 以避免不必要的 widget 重建。

### 相關概念
- BuildContext
- InheritedWidget
- InheritedModel
- Riverpod Provider
- context.watch / context.read
