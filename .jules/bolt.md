## 2025-01-19 - Memory-Efficient Data Aggregation
**Learning:** Concatenating strings in a loop (e.g., `text_corpus += item['title']`) to build a large corpus for processing is O(N²) and memory-inefficient.
**Action:** Use generators to yield data chunks (e.g., words from individual titles) and consume them directly with `collections.Counter` or `itertools.chain`. This avoids creating massive intermediate strings and lists.
