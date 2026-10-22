---
title: "2026-10-23 - Prisma - Learning Point 13"
tags:
  - learning
  - prisma
created: 2026-10-23
---

# Driver Adapters and the Rust-Free Client: Running Prisma Anywhere

### English

For most of Prisma's history, the client bundled a **query engine**: a small Rust binary that took your TypeScript query, translated it into SQL, sent it to the database, and returned typed results. That engine had consequences. It was platform-specific, so you had to declare which binaries to ship (`binaryTargets`), it was large, and it could not run in environments without a native binary — Cloudflare Workers, Vercel Edge Functions, Deno Deploy, or a browser.

**Driver adapters** remove that constraint. An adapter is a thin JavaScript object that knows how to talk to one specific database using a pure-JavaScript driver. The Prisma team maintains database adapters (`@prisma/adapter-pg` for PostgreSQL via `pg`, `@prisma/adapter-neon`, `@prisma/adapter-planetscale`, `@prisma/adapter-libsql`, `@prisma/adapter-better-sqlite3`, `@prisma/adapter-mssql`) and serverless adapters for HTTP/WebSocket-based providers (Neon, PlanetScale, Cloudflare D1). You hand the adapter to the client at construction time and Prisma uses it instead of the bundled engine:

```ts
import { PrismaClient } from './generated/prisma/client';
import { PrismaPg } from '@prisma/adapter-pg';

const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });
const prisma = new PrismaClient({ adapter });
```

The same code, the same type safety, the same generated API — but the transport underneath is now plain JavaScript.

Adapters also became the required companion of the **Rust-free client**. Prisma 6.16 marked the Rust-free ORM and driver adapters Generally Available, and the new `prisma-client` generator pairs them with `engineType = "client"`:

```prisma
generator client {
  provider   = "prisma-client"
  output     = "../src/generated/prisma"
  engineType = "client"
}
```

The `prisma-client` generator (GA in 6.16, and the default from Prisma 7) differs from the older `prisma-client-js` in ways that matter day to day. It requires an explicit `output` path — no more magic generation into `node_modules` — it outputs plain TypeScript that you own and can read, it is ESM-first with `moduleFormat` and `runtime` options for Bun, Deno, Cloudflare and React Native, and it no longer loads `.env` at runtime, so you must use `dotenv` or set environment variables yourself. `Prisma.validator` was removed; use TypeScript's native `satisfies` keyword instead.

Connection management deserves its own attention in serverless deployments. A traditional database connection is a long-lived TCP socket, and a serverless function that scales to hundreds of instances will happily exhaust the database's connection limit. The standard fix is a **connection pooler** such as PgBouncer in transaction mode, which lets many clients share a small number of real connections. Prisma's docs recommend keeping two URLs: a pooled one for the application runtime and a direct one for the CLI, because migrations need a direct connection:

```env
DATABASE_URL="postgres://user:pass@host-pooler:6543/db?pgbouncer=true"
DIRECT_URL="postgres://user:pass@host:5432/db"
```

Why does all of this matter? Because the deployment target is now a design input, not an afterthought. The choice of adapter, the presence or absence of a pooler, and whether the client is a Rust binary or pure TypeScript determine whether the same codebase can run in a container, in a Lambda, or at the edge.

### 中文

Prisma 大部分嘅歷史入面，client 都會附帶一個 **query engine**：一個細細嘅 Rust binary，負責將你嘅 TypeScript query 翻譯成 SQL送去資料庫，再將有型別嘅結果拎返嚟。呢個 engine 有幾個後果：佢係 platform-specific，所以你要聲明要打包邊啲 binary（`binaryTargets`）；佢體積唔細；而且佢根本無法喺冇 native binary 嘅環境運行 —— 例如 Cloudflare Workers、Vercel Edge Functions、Deno Deploy，或者瀏覽器。

**Driver adapter**（驅動適配器）就係為咗解決呢啲限制而存在。一個 adapter 係一個輕量嘅 JavaScript 物件，識得用純 JavaScript 嘅 driver 去同某一個特定資料庫溝通。Prisma 團隊維護住 database adapter（`@prisma/adapter-pg` 配 `pg` 連 PostgreSQL、`@prisma/adapter-neon`、`@prisma/adapter-planetscale`、`@prisma/adapter-libsql`、`@prisma/adapter-better-sqlite3`、`@prisma/adapter-mssql`），同埋針對以 HTTP/WebSocket 通訊嘅服務商嘅 serverless adapter（Neon、PlanetScale、Cloudflare D1）。你喺建立 client 嘅時候將 adapter 交畀佢，Prisma 就會用佢代替內置 engine：

```ts
import { PrismaClient } from './generated/prisma/client';
import { PrismaPg } from '@prisma/adapter-pg';

const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });
const prisma = new PrismaClient({ adapter });
```

同一份 code、同一種型別安全、同一個生成出嚟嘅 API —— 但底下嘅傳輸方式變成純 JavaScript。

Adapter 亦都成為 **Rust-free client** 嘅必須配搭。Prisma 6.16 將 Rust-free ORM 同 driver adapter 標記為 Generally Available，而新嘅 `prisma-client` generator 會同 `engineType = "client"` 配對使用：

```prisma
generator client {
  provider   = "prisma-client"
  output     = "../src/generated/prisma"
  engineType = "client"
}
```

新嘅 `prisma-client` generator（6.16 GA，由 Prisma 7 開始做預設）同舊嘅 `prisma-client-js` 有幾個分別係日常會撞到嘅：佢必須指定 `output` 路徑 —— 唔再「神奇地」生成入 `node_modules`；佢輸出純 TypeScript，屬於你自己、可以睇得明嘅 code；佢以 ESM 為先，用 `moduleFormat` 同 `runtime` 選項支援 Bun、Deno、Cloudflare 同 React Native；仲有佢唔會喺 runtime 自動讀 `.env`，所以你要自己用 `dotenv` 或者設定環境變數。`Prisma.validator` 已被移除，改用 TypeScript 原生嘅 `satisfies` 關鍵字就可以。

喺 serverless 部署，連線管理要特別留意。傳統資料庫連線係一條長命嘅 TCP socket，而一個可以擴展到幾百個 instance 嘅 serverless function，會好輕易就撞爆資料庫嘅連線上限。標準做法係用 **connection pooler**，例如 PgBouncer 嘅 transaction mode，令好多 client 共享少量真實連線。Prisma 官方建議保留兩個 URL：runtime 用 pooled 嘅，CLI 用 direct 嘅，因為 migration 需要直接連線：

```env
DATABASE_URL="postgres://user:pass@host-pooler:6543/db?pgbouncer=true"
DIRECT_URL="postgres://user:pass@host:5432/db"
```

點解呢啲咁重要？因為部署目標而家已經係一個「設計輸入」，唔係事後補救。你揀邊個 adapter、有冇 pooler、client 係 Rust binary 定純 TypeScript，呢啲決定咗同一份 code 到底可唔可以行喺 container、Lambda，定係 edge 上面。

## Key Takeaway
Driver adapters and the Rust-free TypeScript client decouple Prisma from native binaries, which is what makes the same schema-driven code runnable in containers, serverless functions and edge runtimes alike.

## Related Concepts
- Connection pooling and PgBouncer
- Prisma config file and environment variables
- Edge and serverless database providers
- Deploying Prisma migrations in CI

## Diagram
```mermaid
flowchart TD
    A[Your TypeScript code] --> B[PrismaClient]
    B --> C{Adapter supplied?}
    C -- No --> D[Rust query engine binary]
    D --> E[Database over TCP]
    C -- Yes --> F[Driver adapter in pure JS]
    F --> G[pg / Neon / PlanetScale driver]
    G --> H[Database over TCP or HTTP]
    F --> I[Edge runtime: Workers, Edge Functions, Deno]
```
