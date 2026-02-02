## 2026-02-02 - SoupStrainer for HTML Parsing
**Learning:** `BeautifulSoup` parsing overhead can be reduced by ~40% using `SoupStrainer('a')` when only specific tags are needed. This avoids parsing the full DOM tree while preserving the subtree of the matched tags.
**Action:** Use `SoupStrainer` in future scrapers when only a subset of the page is relevant.
