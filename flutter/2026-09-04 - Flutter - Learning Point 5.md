---
title: "2026-09-04 - Flutter - Learning Point 5"
tags:
  - learning
  - flutter
created: 2026-09-04
---

# Flutter's Layered Architecture — From Dart to Native Pixels

## English

Flutter apps run on a **layered architecture**. At the top, you write Dart code — widgets, business logic, state. Below that, the Flutter engine (written in C++) takes your widget tree and translates it into platform-specific drawing commands. For iOS it uses Metal; for Android it uses Vulkan or Skia. The result is truly native performance — no webviews, no bridges, just pixels on screen.

The key insight: **Flutter owns the entire rendering pipeline**. Unlike React Native, which delegates UI rendering to native components, Flutter paints every pixel itself. This gives you pixel-perfect control and consistent look across platforms, but means Flutter doesn't automatically adopt native UI updates (like iOS design changes).

### Key Takeaway
Flutter's layered architecture — Dart → Engine (C++) → GPU — delivers native performance while giving you full control over every pixel. The tradeoff is caring about platform-specific rendering details yourself.

### Related Concepts
- Rendering Pipeline
- Skia / Vulkan / Metal
- Native Performance
- Cross-Platform Rendering

---

## 中文

Flutter 應用運行在**分層架構**上。最上層是你寫的 Dart 代碼 — widgets、邏輯、狀態。在它下面，Flutter 引擎（用 C++ 編寫）把你的 widget 樹翻譯成平台專屬的繪圖指令。對於 iOS 它使用 Metal；對於 Android 它使用 Vulkan 或 Skia。结果是真正的原生效能——不是 webview，沒有橋接層，只有螢幕上的像素。

關鍵洞察：**Flutter 完全掌控整個渲染管線**。不同於 React Native（把 UI 渲染委託給原生元件），Flutter 自己繪製每個像素。這給你像素級的控制和跨平台一致的外觀，但代價是 Flutter 不會自動採用原生 UI 更新（如 iOS 設計變化）。

### 關鍵要點
Flutter 的分層架構 — Dart → 引擎（C++）→ GPU — 在讓你完全控制每個像素的同時，提供原生效能。代價是你需要自己關注平台特定的渲染細節。

### 相關概念
- 渲染管線
- Skia / Vulkan / Metal
- 原生效能
- 跨平台渲染
