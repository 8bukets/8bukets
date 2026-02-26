## 2024-05-22 - Data Reuse in Analytics
**Learning:** `analytics.py` was redundantly parsing URLs to extract domains, even though `scraper.py` already pre-calculated and stored this information. This caused a significant performance overhead (~40% of user CPU time).
**Action:** Always check if upstream data sources (like scraper output) already contain the derived data needed for analysis before re-calculating it.
## 2026-02-26 - urlparse behavior for invalid URLs
**Learning:** `urllib.parse.urlparse` can return an empty string for `netloc` if the input is not a proper URL (e.g., 'not a url').
**Action:** Always check if the extracted domain is truthy before returning it, or return `None` explicitly if an empty string is not desired.
