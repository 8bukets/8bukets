## 2026-02-04 - Redundant Iterations in Data Processing
**Learning:** Multiple sequential passes over the same dataset for different metrics (domains, categories, dates, authors) significantly increases overhead, even if technically O(N).
**Action:** Always look for opportunities to fuse loops when processing list data for multiple aggregates. A single pass is cleaner and more cache-friendly.
