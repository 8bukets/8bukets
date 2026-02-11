## 2026-02-06 - Redundant URL Parsing in Analytics pipeline
**Learning:** The scraping pipeline pre-computes derived fields (like `domain`) which are often ignored by downstream consumers (`analytics.py`) in favor of re-computing them. This leads to wasted CPU cycles (~3.5x slower in this case).
**Action:** Always check if upstream data sources already provide the parsed/derived data before implementing parsing logic in consumers.
