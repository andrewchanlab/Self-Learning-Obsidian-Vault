---
title: "2026-09-05 - Meilisearch - Learning Point 7"
tags:
  - learning
  - meilisearch
created: 2026-09-05
---

# Meilisearch 的同義詞（Synonyms）與詞形還原（Stemming）

除了錯字容忍，Meilisearch 還支援同義詞設定——你可以在 index 設定裡定義 "movie" 和 "film" 為同義詞，搜尋其中一個就會同時匹配另一個。Meilisearch 也內建 stemming，會將 "running"、"runs"、"ran" 還原為詞根 "run"，所以搜尋 "running" 能找到包含 "run" 的文件。These features work together to make search more intuitive for end users.

## 同義詞配置
```json
{
  "synonyms": {
    "movie": ["film", "cinema", "movie"],
    "program": ["programme", "software", "app"]
  }
}
```

## Stemming 的語言限制
Meilisearch 的 stemming 演算法支援主要歐洲語言（English, French, Spanish, German 等）。對於亞洲語言（中文、日文、韓文），由於這些語言不是以空格分詞，Meilisearch 的預設 stemming 效果有限，通常需要配合自訂分詞器。

## Related Concepts
- Stemming and lemmatization
- Synonym mapping
- Language-specific analyzers
- CJK tokenization challenges
