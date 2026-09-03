---
title: "2026-09-04 - NestJS - Learning Point 6"
tags:
  - learning
  - nestjs
created: 2026-09-04
---

# NestJS Dependency Injection — Let the Container Do the Wiring

NestJS's IoC (Inversion of Control) container automatically resolves dependencies. Mark a constructor parameter with `@Injectable()` and Nest injects the instance — no manual `new Class()` calls. This makes services testable: swap a real repository for a mock just by configuring the testing module.

## Key Takeaway
Dependency injection in NestJS decouples your code: services declare what they need, the framework provides it, and you never write `new Service()` in application code.

## Related Concepts
- Inversion of Control
- Dependency Injection
- Unit Testing

---

## 中文：NestJS 依賴注入 — 讓容器完成連線

NestJS 的 IoC（控制反轉）容器自動解析依賴。用 `@Injectable()` 標記構造函數參數，Nest 就會注入實例 — 無需手動調用 `new Class()`。這使得服務可測試：只需配置測試模塊，就可以用模擬對象替換真實的倉庫。

## 核心要點
NestJS 中的依賴注入將你的代碼解耦：服務聲明它們需要什麼，框架提供它，而你在應用程序代碼中永遠不需要寫 `new Service()`。

## 相關概念
- 控制反轉
- 依賴注入
- 單元測試
