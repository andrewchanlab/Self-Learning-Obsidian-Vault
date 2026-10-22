---
title: "2026-10-23 - Redis - Learning Point 11"
tags:
  - learning
  - redis
created: 2026-10-23
---

# Hash Field Expiration: Giving Individual Fields Their Own TTL

### English

Until Redis 7.4, expiration existed at exactly one level: the **key**. `SETEX session:abc 3600 "..."` sets a deadline for the entire value, and when it fires, the whole key disappears. That granularity is awkward for a very common data shape — a **session or cart hash** where different fields logically expire at different times. A session hash typically holds `user_id`, `created_at`, `last_seen`, a list of `perm:*` flags, and a `refresh_token`. Some of those should live for hours, some for minutes, and some (like `created_at`) should live forever as an audit field. With key-level TTL only, you have two bad options: use a separate key per field (which destroys atomicity — updating two fields becomes two commands, so a crash between them leaves the hash inconsistent), or pick one TTL for everything (which either expires your audit data early or keeps stale flags around too long).

Redis 7.4 added **hash field expiration**, which gives each *field* inside a hash its own TTL. The commands are `HEXPIRE`, `HPEXPIRE`, `HEXPIREAT`, `HPEXPIREAT`, `HPTTL`, `HPERSIST`, and `HPEXPIRETIME`:

```
> HSET session:abc user_id u_42 created_at 1729600000 perm:read 1 perm:write 1
> HEXPIRE session:abc 300 FIELDS 2 perm:read perm:write
1
1
> HPTTL session:abc user_id
-1
> HPTTL session:abc perm:read
300
```

The reply is a list, one integer per field: `1` means the TTL was set, `0` means it was not set because a condition failed, `-2` means the field does not exist, and `-1` (from `HPTTL`) means the field exists but has no expiration. The `FIELDS numfields` argument is mandatory in the 7.4 syntax — you must state how many fields follow, which lets the server validate the argument list without ambiguity.

Conditional updates are supported with `NX`, `XX`, `GT` and `LT`. `NX` sets the TTL only if the field currently has none, `XX` only if it already has one, `GT` only if the new expiry is later, `LT` only if it is sooner. A field with no TTL is treated as infinite for the purposes of `GT` and `LT`, so `GT` on a persistent field will always succeed and `LT` on a persistent field will always fail. This makes the commands safe to use in a "refresh the deadline only if it is close to expiring" pattern without a read-modify-write race.

Two behaviours surprise people. First, TTLs are cleared only by commands that *overwrite or delete* the field — `HSET` on an existing field resets it to no-TTL, and `HDEL` removes it entirely; commands that conceptually change a value without replacing it leave the TTL alone. Second, when the last field with a TTL expires and no non-expiring fields remain, the key itself is removed automatically, so you do not leak empty hashes.

Why does this matter beyond tidiness? Memory. A Redis deployment that stores a million session hashes with a uniform 24-hour TTL holds every byte of those hashes for a full day, even the fields nobody reads. Field-level expiry lets the hot fields (the token, the last-seen timestamp) die quickly while the cold audit fields survive, which directly reduces `maxmemory` pressure and therefore eviction churn. It also removes a whole category of application bug: the "expired permission flag that was never cleaned up" problem, now handled by the data store rather than by a sweeper cron job.

Finally, note that field expiration is a Redis 7.4+ feature. On older servers the command simply does not exist, so feature-detect with `COMMAND INFO HEXPIRE` at startup, or gate your code on the server version, before relying on it.

### 中文

喺 Redis 7.4 之前，到期功能（expiration）只有一個層次：**key**。`SETEX session:abc 3600 "..."` 設定咗成個 value 嘅死線，時間一到，個 key 就整個消失。呢種粒度對一個好常見嘅資料形狀頗為尷尬 —— **session 或者購物車 hash**，入面唔同欄位嘅邏輯生命週期其實唔同。一個 session hash 通常裝住 `user_id`、`created_at`、`last_seen`、一串 `perm:*` 權限旗標同一個 `refresh_token`。其中一啲應該存活幾個鐘，一啲只需幾分鐘，而 `created_at` 呢類審計欄位應該永遠保留。如果只有 key 級 TTL，你只有兩個都唔理想嘅選擇：用每個欄位一個 key（會破壞原子性 —— 更新兩個欄位變成兩條指令，中途當機就會令 hash 狀態不一致），或者全部欄位用同一個 TTL（於是要麼提早刪咗審計資料，要麼令過期嘅權限旗標殘留太耐）。

Redis 7.4 加入咗 **hash field expiration（雜湊欄位級過期）**，令 hash 入面每個 *field* 都擁有自己嘅 TTL。相關指令包括 `HEXPIRE`、`HPEXPIRE`、`HEXPIREAT`、`HPEXPIREAT`、`HPTTL`、`HPERSIST` 同 `HPEXPIRETIME`：

```
> HSET session:abc user_id u_42 created_at 1729600000 perm:read 1 perm:write 1
> HEXPIRE session:abc 300 FIELDS 2 perm:read perm:write
1
1
> HPTTL session:abc user_id
-1
> HPTTL session:abc perm:read
300
```

回覆係一個列表，每個欄位一個整數：`1` 代表成功設定 TTL，`0` 代表因為條件不符而未設定，`-2` 代表欄位唔存在，而 `HPTTL` 回 `-1` 代表欄位存在但冇到期設定。7.4 語法入面 `FIELDS numfields` 係必須嘅 —— 你要聲明跟住有幾多個欄位，令伺服器可以無歧義噉驗證參數列表。

條件更新方面支援 `NX`、`XX`、`GT` 同 `LT`。`NX` 只喺欄位目前冇 TTL 時設定；`XX` 只喺已經有 TTL 時設定；`GT` 只喺新到期時間更遲時設定；`LT` 只喺更早時設定。冇 TTL 嘅欄位喺 `GT` / `LT` 比較時當作無限大，所以對持久欄位行 `GT` 一定成功，行 `LT` 就一定失敗。呢個特性令你可以安全咁寫「只有當死線快到期時先刷新」嘅邏輯，完全唔需要先讀後寫嘅競態處理。

有兩個行為容易令人意外。第一，TTL 只會被「覆寫或者刪除」欄位嘅指令清除 —— 對已存在欄位執行 `HSET` 會令佢變成冇 TTL，而 `HDEL` 會直接刪走；至於概念上改變咗內容但冇真正取代嘅指令，會保留原本嘅 TTL。第二，當所有有 TTL 嘅欄位都過期、而冇任何永久欄位留下時，個 key 會自動被移除，所以唔會殘留一堆空 hash。

除咗整潔，呢件事仲有實際意義 —— 記憶體。一個儲存過百萬個 session hash、全部用 24 小時統一 TTL 嘅 Redis 部署，即使冇人讀嘅欄位，都要喺記憶體裏面擺足一日。欄位級過期令熱欄位（token、last-seen）可以好快消失，冷欄位（審計資料）則留低，直接減低 `maxmemory` 壓力，亦即減少淘汰震盪。同時佢仲消走了一整類應用層 bug：「過期咗但冇人清理嘅權限旗標」，而家交畀資料庫層處理，唔使再寫定時清理嘅 cron job。

最後提提你，欄位級過期係 Redis 7.4+ 先有嘅功能。喺舊伺服器上呢條指令根本唔存在，所以啟動時可以用 `COMMAND INFO HEXPIRE` 做特性偵測，或者按伺服器版本做 gating，先好依賴佢。

## Key Takeaway
Hash field expiration (Redis 7.4+) gives individual fields their own TTL, so one session hash can hold short-lived tokens and permanent audit fields without duplicating data into separate keys.

## Related Concepts
- Key Expiration and TTL
- Session Storage Patterns
- Memory Pressure and maxmemory
- Conditional Command Options

## Diagram
```mermaid
flowchart TD
    A[HSET session:abc user_id created_at perm:read perm:write] --> B[HEXPIRE session:abc 300 FIELDS 2 perm:read perm:write]
    B --> C{Per-field TTL stored}
    C --> D[HPTTL perm:read = 300]
    C --> E[HPTTL user_id = -1 (no TTL)]
    C --> F{Time passes}
    F --> G[perm:read and perm:write deleted automatically]
    F --> H[user_id and created_at survive]
    G --> I{Any non-expiring field left?}
    I -->|Yes| H
    I -->|No| J[Key removed automatically]
```
