---
title: "2026-09-03 - Flutter - Learning Point 4"
tags:
  - learning
  - flutter
created: 2026-09-03
---

# Flutter Animations — Implicit, Explicit, and Custom Controllers

## English

Flutter gives you **three animation layers**:

1. **Implicit animations** (`AnimatedContainer`, `AnimatedOpacity`, `AnimatedPadding`) — Flutter manages the controller for you. Just change the target value and it animates to it. Simplest, best for UI state transitions.

2. **Explicit animations** (`RotationTransition`, `ScaleTransition`, `AnimationController`) — You control the controller. Use when you need to trigger the animation programmatically, repeat it, or chain multiple tweens. More code, more control.

3. **Custom painters** (`CustomPainter` + `AnimationController`) — You control every pixel per frame. For visualizations, games, or canvas drawing that needs to animate. Most powerful, most complex.

The `Tween` defines the interpolation from start to end value. `Curve` modifies the timing (ease-in, bounce, etc.). Combine them: `controller.drive(Tween(begin: 0, end: 1).chain(CurveTween(curve: Curves.bounceOut)))`.

### Key Takeaway
Use implicit animations for simple state transitions. Reach for explicit AnimationControllers when you need programmatic control, repeats, or chained tweens. CustomPainter is for canvas-level pixel control with animations.

### Related Concepts
- AnimationController
- Tween / CurveTween
- AnimatedBuilder
- CustomPainter
- Curves (bounceOut, easeInOut, etc.)

---

## 中文

Flutter 提供**三個動畫層次**：

1. **隱式動畫**（`AnimatedContainer`、`AnimatedOpacity`、`AnimatedPadding`）——Flutter 為你管理控制器。只需更改目標值，它就會動畫到該值。最簡單，最適合 UI 狀態轉換。

2. **顯式動畫**（`RotationTransition`、`ScaleTransition`、`AnimationController`）——你控制控制器。在需要以編程方式觸發動畫、重複或鏈接多個補間動畫時使用。代碼更多，控制更多。

3. **自定義繪製**（`CustomPainter` + `AnimationController`）——你控制每一幀的每個像素。用於可視化、遊戲或需要動畫的畫布繪圖。最強大，也最複雜。

`Tween` 定義從起始值到結束值的插值。`Curve` 修改時序（緩入、彈跳等）。組合它們：`controller.drive(Tween(begin: 0, end: 1).chain(CurveTween(curve: Curves.bounceOut)))`。

### 核心要點
對簡單的狀態轉換使用隱式動畫。在需要編程控制、重複或鏈接補間動畫時使用顯式 AnimationControllers。自定義 Painter 用於帶動畫的畫布級像素控制。

### 相關概念
- AnimationController
- Tween / CurveTween
- AnimatedBuilder
- CustomPainter
- Curves（bounceOut、easeInOut 等）
