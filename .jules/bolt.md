## 2026-01-27 - SoupStrainer Attribute Filtering Gotcha
**Learning:** `SoupStrainer('tag', class_='value')` with `html.parser` may fail to match elements where 'value' is just one of multiple classes (exact match vs contains). It's safer to strain by tag name only and filter attributes later.
**Action:** Use `SoupStrainer('tag')` and then `soup.find_all('tag', class_='value')` for reliable partial parsing.
## 2024-05-22 - Data Reuse in Analytics
**Learning:** `analytics.py` was redundantly parsing URLs to extract domains, even though `scraper.py` already pre-calculated and stored this information. This caused a significant performance overhead (~40% of user CPU time).
**Action:** Always check if upstream data sources (like scraper output) already contain the derived data needed for analysis before re-calculating it.
