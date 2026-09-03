---
title: "2026-09-04 - NestJS - Learning Point 2"
tags:
  - learning
  - nestjs
created: 2026-09-04
---

# Controllers Direct Traffic, Services Do the Work

Controllers receive HTTP requests, extract parameters, and call the right service methods. They never contain business logic — they delegate to services which know HOW to do things. This separation makes business logic reusable across different entry points (HTTP, WebSockets, gRPC).

## Key Takeaway
NestJS enforces a clean separation between routing (controllers) and business logic (services) — making logic reusable and testable.

## Related Concepts
- MVC Pattern
- Business Logic
- REST API

---

## 中文：控制器指揮流量，服務執行業務

控制器接收 HTTP 請求、提取參數，然後調用正確的服務方法。控制器本身不含業務邏輯——它們將工作委託給服務，由服務來處理「如何做」。這種分離使業務邏輯可以在不同入口點（HTTP、WebSockets、gRPC）復用。

## 核心要點
NestJS 強制將路由（控制器）和業務邏輯（服務）分離，使邏輯可復用且易於測試。

## 相關概念
- MVC 模式
- 業務邏輯
- REST API
