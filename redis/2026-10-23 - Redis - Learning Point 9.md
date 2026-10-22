---
title: "2026-10-23 - Redis - Learning Point 9"
tags:
  - learning
  - redis
created: 2026-10-23
---

# Redis Cluster: Sharding the Keyspace with Hash Slots

### English

A single Redis process is limited by the RAM of one machine and by the network bandwidth of one NIC. **Redis Cluster** solves this by splitting the keyspace across several **master nodes**, each of which also keeps one or more **replicas** for failover. A cluster of six nodes (three masters, three replicas) is the smallest sensible production shape.

Cluster does **not** use consistent hashing in the classic library sense. Instead the keyspace is divided into a fixed number of **16384 hash slots**, and each master owns a contiguous range of them. The slot for a key is `CRC16(key) mod 16384`. Because the number of slots is fixed in advance, adding or removing a node means moving *slots* around, not rehashing every key in the universe — this is the key design decision that makes live resharding possible. Moving a slot literally means moving the keys that hash into it; Redis migrates them one by one with `MIGRATE` while continuing to serve traffic.

Nodes in a cluster do not proxy requests for other nodes. If you send `GET x` to a node that does not own the slot for `x`, it replies with a redirection error instead of forwarding the command:

```
127.0.0.1:7000> GET x
(error) MOVED 3999 127.0.0.1:6381
```

The **client** is responsible for following redirections and caching the slot-to-node map. `MOVED` means the slot has *permanently* moved, so the client updates its table and retries against the new node. `ASK` is a temporary redirection used during a migration in progress: the client sends `ASKING` followed by *only that one command* to the target node and does not update its table. Confusing the two is a classic source of bugs — treating an `ASK` as a permanent move corrupts the client's view of the cluster.

The most important consequence for application developers is that **multi-key commands must live in the same slot**. `MGET a b c` is fine only if `a`, `b` and `c` hash to one slot; otherwise the node returns `CROSSSLOT`. The escape hatch is the **hash tag**: if a key contains a substring in curly braces, only the part inside the braces is hashed. So `user:{1001}:profile` and `user:{1001}:settings` always land in the same slot, and a Lua script or `MGET` across them is legal. The rule of thumb is to tag on the *aggregate* identifier — the tenant, the account, the shopping cart — never on the specific record, otherwise you accidentally create a hot slot where every key of one customer piles onto a single node.

Note that cluster changes the atomicity model too: `MULTI/EXEC` and Lua scripts only guarantee atomicity *within a single node*. Cross-node atomicity does not exist in Redis Cluster, which is another reason to co-locate related keys with a hash tag.

### 中文

單一 Redis 程序受制於一台機器的記憶體與一張網絡卡的上限。**Redis Cluster** 的做法是把整個 keyspace（鍵空間）分佈到多個 **master 節點**，每個 master 再配上 **replica** 副本以便故障時自動接替。六個節點（三 master、三 replica）是最小的合理生產規模。

Cluster 並非採用傳統的 consistent hashing，而是把鍵空間切成固定數目的 **16384 個 hash slot（雜湊槽）**，每個 master 負責其中一段連續的槽。某個 key 的槽位由 `CRC16(key) mod 16384` 算出。槽位總數一開始就固定，之後加節點或減節點只是搬走某些槽，而唔需要為全世界重新雜湊 —— 呢個設計正係線上 resharding（重新分片）做得到嘅原因。所謂搬槽，實際上就係搬走雜湊到嗰啲槽嘅 key，Redis 會用 `MIGRATE` 逐個遷移，同時繼續服務查詢。

Cluster 節點之間**唔會代轉**（proxy）請求。如果你將 `GET x` 送到唔擁有 `x` 所在槽嘅節點，佢會直接回覆一個重定向錯誤：

```
127.0.0.1:7000> GET x
(error) MOVED 3999 127.0.0.1:6381
```

**客户端**要自己處理重定向，並且快取「槽 → 節點」嘅對照表。`MOVED` 代表槽位**永久**搬咗，客户端要更新對照表再重試；`ASK` 則係遷移進行中嘅**臨時**重定向，客户端只可以將嗰一次命令加上 `ASKING` 送到目標節點，並且**唔好**更新對照表。兩者搞混係好常見嘅 bug 來源 —— 將 `ASK` 當成永久搬遷，會令客户端對集群狀態嘅理解出錯。

對開發者最影響嘅一點係：**多 key 命令必須喺同一個槽**。`MGET a b c` 只有喺三個 key 都雜湊到同一槽先合法，否則節點會回 `CROSSSLOT`。逃生門係 **hash tag（雜湊標籤）**：如果 key 內含一對大括號，Redis 只會雜湊大括號入面嘅內容。所以 `user:{1001}:profile` 同 `user:{1001}:settings` 一定喺同一槽，可以用同一段 Lua 腳本或者 `MGET` 一次過處理。實務原則係用「聚合體」嘅識別碼做標籤 —— 例如租戶、戶口、購物車 —— 絕對唔好用單筆記錄嘅 ID，否則同一個客戶嘅所有 key 會全部撞去同一個節點，造成 hot slot。

另外要留意 cluster 改變咗原子性嘅保證：`MULTI/EXEC` 同 Lua 腳本只喺**單一節點**內保證原子性，跨節點嘅原子性喺 Redis Cluster 唔存在 —— 呢個亦係要用 hash tag 將相關 key 放埋一齊嘅原因。

## Key Takeaway
Redis Cluster splits keys across 16384 fixed hash slots so nodes can be added or removed without downtime, but it demands hash tags to keep related keys in one slot and one node.

## Related Concepts
- Hash Slots and CRC16
- MOVED and ASK Redirections
- Hash Tags and Cross-Slot Errors
- Cluster Resharding and MIGRATE

## Diagram
```mermaid
flowchart TD
    C[Client] -->|GET x| N1[Node A :7000]
    N1 -->|slot 3999 not owned| E[MOVED 3999 127.0.0.1:6381]
    E --> C
    C -->|retry| N2[Node B :6381 owns slot 3999]
    N2 --> V[Value]
    N1 -.->|reshard in progress| A[ASK 3999 node B + ASKING]
    A -.-> C
    K1[user:{1001}:profile] -->|CRC16 of 1001| S[Slot 8123]
    K2[user:{1001}:settings] -->|same slot| S
```
