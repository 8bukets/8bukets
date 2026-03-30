## 2026-01-17 - Loop Fusion for Data Aggregation
**Learning:** Iterating over the same collection multiple times (loop splitting) to extract different attributes is less efficient than a single pass (loop fusion), especially in Python where iteration overhead is non-trivial.
**Action:** When aggregating multiple statistics from a list of dictionaries, combine the logic into a single loop to reduce complexity from O(k*N) to O(N).
