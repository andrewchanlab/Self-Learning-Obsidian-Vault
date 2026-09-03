---
title: "2026-09-03 - Flutter - Learning Point 5"
tags:
  - learning
  - flutter
created: 2026-09-03
---

# Flutter Testing — Unit, Widget, and Integration Tests

## English

Flutter supports **three testing layers**:

**Unit tests** (`.test` files in `test/`) test pure Dart logic — business rules, repositories, providers. No widget rendering, no async delays from the framework. Use `unittest` or Riverpod's `ProviderScope` overrides to isolate.

**Widget tests** (`flutter_test`) render a single widget in a test environment: `tester.pumpWidget(MyWidget())`. You can tap, scroll, and assert on the rendered output. Good for testing UI logic and widget state changes. `pumpAndSettle()` waits for animations to finish.

**Integration tests** (`integration_test/`) run the full app on a real device or emulator — the entire Flutter engine, platform channels, everything. Use for critical user flows (login, checkout). Slowest to run, highest confidence.

Golden tests compare screenshots against stored reference images — catches unintended UI regressions. Run them in CI to ensure design consistency.

### Key Takeaway
Match the test layer to the confidence you need: unit tests for logic, widget tests for component behavior, integration tests for complete user flows. Golden tests catch visual regressions automatically.

### Related Concepts
- flutter_test
- ProviderScope overrides
- pumpWidget / pumpAndSettle
- integration_test
- Golden tests / screenshot testing

---

## 中文

Flutter 支持**三個測試層次**：

**單元測試**（`test/` 目錄中的 `.test` 文件）測試純 Dart 邏輯——業務規則、repository、provider。沒有 widget 渲染，沒有框架帶來的異步延遲。使用 `unittest` 或 Riverpod 的 `ProviderScope` overrides 來隔離。

**Widget 測試**（`flutter_test`）在測試環境中渲染單個 widget：`tester.pumpWidget(MyWidget())`。你可以點擊、滾動並對渲染輸出進行斷言。適合測試 UI 邏輯和 widget 狀態變化。`pumpAndSettle()` 等待動畫完成。

**集成測試**（`integration_test/`）在真實設備或模擬器上運行完整應用——整個 Flutter 引擎、Platform Channels、所有東西。用於關鍵用戶流程（登錄、結帳）。運行最慢，信心最高。

Golden tests 將截圖與存儲的參考圖像進行比較——捕捉意外的 UI 回歸。在 CI 中運行它們以確保設計一致性。

### 核心要點
根據你需要的信心程度選擇測試層次：單元測試用於邏輯，widget 測試用於組件行為，集成測試用於完整的用戶流程。Golden tests 自動捕捉視覺回歸。

### 相關概念
- flutter_test
- ProviderScope overrides
- pumpWidget / pumpAndSettle
- integration_test
- Golden tests / 截圖測試
