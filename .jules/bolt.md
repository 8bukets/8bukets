## 2025-01-08 - [Single Pass Aggregation in Analytics]
**Learning:** Iterating over a dataset multiple times (once for each metric) is a common anti-pattern that looks clean but scales poorly (O(MN) where M is metrics). In `analytics.py`, consolidating 4 loops into 1 reduced complexity to O(N).
**Action:** When calculating multiple aggregates from a list of dicts, always use a single loop with multiple counters/accumulators.
