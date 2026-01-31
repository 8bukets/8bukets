## 2026-01-31 - [Optimization: Single Pass Analytics]
**Learning:** Iterating over a dataset multiple times (O(k*N)) for simple aggregations is a common anti-pattern. Consolidating into a single pass (O(N)) reduces overhead and improves scalability, especially when parsing or expensive operations are involved in the loop.
**Action:** Always look for opportunities to aggregate multiple metrics in a single loop over the data.
