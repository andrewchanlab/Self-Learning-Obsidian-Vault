---
title: "2026-09-03 - Flutter - Learning Point 2"
tags:
  - learning
  - flutter
created: 2026-09-03
---

# Flutter's RenderObject — How Widgets Actually Paint

## English

Most Flutter widgets are **composed** (like Column, Row, Container) — they're thin wrappers that just configure child widgets. But the real painting work happens in **RenderObjectWidget**s, which create a **RenderObject** that knows how to paint itself on screen.

The key RenderObject is **RenderBox**, which uses a 2D Cartesian coordinate system. It implements `performLayout()` (how big am I?) and `paint()` (how do I draw myself?). When you create a custom `LeafRenderObjectWidget`, you're building the painting equivalent of `CustomPainter` — you have total control over the pixels.

The frame pipeline: **build → layout (size children) → paint (draw)**. Miss any of these and your widget breaks.

### Key Takeaway
RenderObject is Flutter's low-level rendering node. Compose-widgets configure them; LeafRenderObjectWidget creates custom ones — giving you pixel-level painting control beyond what built-in widgets offer.

### Related Concepts
- RenderObjectWidget
- RenderBox
- performLayout / paint
- LeafRenderObjectWidget
- CustomPainter

---

## 中文

大多數 Flutter widget 是**組合型**的（如 Column、Row、Container）——它們只是配置子 widget 的輕量包裝。但真正的繪製工作發生在 **RenderObjectWidget** 中，它創建一個知道如何在螢幕上繪製自己的 **RenderObject**。

關鍵的 RenderObject 是 **RenderBox**，它使用二維笛卡爾坐標系統。它實現 `performLayout()`（我有多大？）和 `paint()`（我怎麼畫自己？）。當你創建一個自定義 `LeafRenderObjectWidget` 時，你正在構建相當於 `CustomPainter` 的繪製控制——你完全掌控每個像素。

幀流程：**build → layout（調整子元件大小）→ paint（繪製）**。任何一步出錯你的 widget 都會出問題。

### 核心要點
RenderObject 是 Flutter 的低級渲染節點。組合 widgets 配置它們；LeafRenderObjectWidget 創建自定義 ones——給你超越內置 widget 的像素級繪製控制。

### 相關概念
- RenderObjectWidget
- RenderBox
- performLayout / paint
- LeafRenderObjectWidget
- CustomPainter
