## 2026-02-04 - Single Pass Aggregation & Schema Mismatch
**Learning:** `analytics.py` was iterating over the dataset multiple times (O(N*M)) to extract different stats. This is inefficient. Additionally, a schema mismatch (`date` vs `datetime`) caused empty reports.
**Action:** When writing analytics scripts, use a single loop to aggregate all metrics at once. Always verify that input keys match expectations, handling aliases if necessary (e.g., `p.get('date') or p.get('datetime')`).
