---
title: "2026-09-04 - NestJS - Learning Point 3"
tags:
  - learning
  - nestjs
created: 2026-09-04
---

# Dependency Injection Automates Wiring

NestJS's IoC container automatically resolves and injects dependencies. Declare what you need in a constructor, and Nest finds or creates it. You never write `new UserService()` — the framework handles instantiation and lifecycle management.

## Key Takeaway
NestJS's dependency injection container eliminates manual object wiring — the framework manages service lifecycles automatically.

## Related Concepts
- Inversion of Control
- Dependency Injection
- IoC Container

---

## 中文：依賴注入自動組裝元件

NestJS 的 IoC 容器自動解析並注入依賴。你只需在建構函式中宣告所需的服務，Nest 就會找到或建立它。你永遠不需要寫 `new UserService()`——框架會自動處理實例化和生命週期管理。

## 核心要點
NestJS 的依賴注入容器消除了手動組裝物件的繁瑣——框架自動管理服務的生命週期。

## 相關概念
- 控制反轉
- 依賴注入
- IoC 容器
