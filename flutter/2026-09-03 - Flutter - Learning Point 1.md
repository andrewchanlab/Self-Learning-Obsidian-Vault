---
title: "2026-09-03 - Flutter - Learning Point 1"
tags:
  - learning
  - flutter
created: 2026-09-03
---

# Flutter Platform Channels — Bridging Dart and Native Code

## English

Flutter Platform Channels provide a **bi-directional communication bridge** between your Dart code and native platform code (Swift/Kotlin). When you need a native API that Flutter doesn't expose — like iOS ARKit or Android NFC — you write a MethodChannel: Dart sends a method name + arguments, the native side receives it, executes, and returns a result. This is how packages like `camera` or `battery` work under the hood.

The flow: Dart (invokeMethod) → BinaryMessenger → iOS (FlutterMethodChannel) → Swift → result back the same way.

**When to use:** Native APIs, device sensors, platform-specific UI tweaks, or performance-critical code you want in native language.

### Key Takeaway
Platform Channels let Dart call native code and vice versa — enabling access to any native API Flutter doesn't natively expose, with full async response handling.

### Related Concepts
- BinaryMessenger
- MethodChannel / EventChannel
- Platform-specific implementation
- Native plugin architecture

---

## 中文

Flutter Platform Channels 在你的 Dart 代碼和原生平台代碼（Swift/Kotlin）之間提供了**雙向通信橋樑**。當你需要一個 Flutter 沒有暴露的原生 API 時——比如 iOS ARKit 或 Android NFC——你編寫一個 MethodChannel：Dart 發送方法名 + 參數，原生端接收它、執行、並返回結果。這就是 `camera`、`battery` 等插件的底層原理。

流程：Dart（invokeMethod）→ BinaryMessenger → iOS（FlutterMethodChannel）→ Swift → 結果原路返回。

**使用時機：** 原生 API、設備傳感器、平台特定的 UI 調整，或你希望以原生語言運行的效能關鍵代碼。

### 核心要點
Platform Channels 讓 Dart 調用原生代碼，反之亦然——實現對任何 Flutter 沒有原生暴露的原生 API 的訪問，具有完整的異步響應處理。

### 相關概念
- BinaryMessenger
- MethodChannel / EventChannel
- 平台特定實現
- 原生插件架構
