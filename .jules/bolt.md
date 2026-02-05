## 2024-01-16 - [Analytics Optimization]
**Learning:** Combining multiple optimized list comprehensions into a single Python `for` loop increased execution time from ~1.06s to ~1.26s. Python's interpreter overhead for manual looping and dictionary updates outweighs the cost of iterating the list multiple times with C-optimized list comprehensions and `Counter(list)`.
**Action:** Prefer list comprehensions and built-in functions over manual loops for data aggregation in Python, unless memory pressure is high.

## 2024-01-16 - [LRU Cache]
**Learning:** Adding `@lru_cache` to a function processing unique inputs (e.g., unique URLs) increases execution time due to cache management overhead with a 0% hit rate.
**Action:** Only use `lru_cache` when repeated inputs are expected.
