## 2026-02-06 - Avoid Redundant URL Parsing
**Learning:** URL parsing using `urllib.parse` adds up when processing thousands of records. Using a pre-computed `domain` field from the dataset reduced execution time by ~63% (from 10.6ms to 3.9ms per 1000 runs) in `analytics.py`.
**Action:** Always verify if required metadata (like domains) is already present in the source data before implementing parsing logic.
