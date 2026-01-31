## 2026-01-31 - Single-Pass Aggregation
**Learning:** Consolidating multiple O(N) loops into a single pass significantly improved execution time (~50% reduction) for analytics processing. Additionally, using pre-calculated fields (like `domain`) avoids expensive repeated parsing operations.
**Action:** Always look for opportunities to compute multiple aggregates in a single iteration over large datasets. Prefer raw data access over expensive re-computation when possible.
