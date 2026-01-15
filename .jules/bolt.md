## 2026-01-15 - Loop Consolidation in Analytics
**Learning:** Python `Counter` and list comprehensions can hide multiple passes over data. Consolidating into a single loop with explicit `counter[key] += 1` is O(N) vs O(kN) and saves intermediate list memory, which is significant for scalability.
**Action:** Check for multiple iterations over the same large dataset in `analytics` or `processing` scripts and combine them using single-pass accumulation.
