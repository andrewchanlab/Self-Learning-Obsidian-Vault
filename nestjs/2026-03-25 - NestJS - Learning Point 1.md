---
title: "2026-03-25 - NestJS - Learning Point 1"
tags:
  - learning
  - nestjs
created: 2026-03-25
---

# NestJS Architecture: Modules, Controllers, and Providers

NestJS is built on three core building blocks. Modules (`@Module()`) are organizational units that group related functionality — each feature (users, auth, products) typically has its own module. Controllers (`@Controller()`) handle incoming HTTP requests and route them to the right handler methods, returning responses. Providers (services, repositories, factories — anything with `@Injectable()`) contain the business logic and can be injected into controllers or other providers via dependency injection. This layered architecture makes code testable and maintainable because each piece has a single, clear responsibility.

## Key Takeaway
NestJS enforces a clean architecture through modules as namespaces, controllers as HTTP handlers, and providers as injectable business logic — making large codebases organized by design.

## Related Concepts
- Dependency injection container
- Request/response lifecycle
- Feature-based module organization
