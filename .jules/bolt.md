## 2026-01-28 - BeautifulSoup Parsing Optimization
**Learning:** `SoupStrainer` significantly reduces parsing time by ignoring irrelevant HTML parts, and replacing `select_one` with `find` (avoiding CSS selector overhead) yields further improvements (~10% total boost) for large HTML documents.
**Action:** Prefer `SoupStrainer` for targeted scraping and use `find`/`find_all` over CSS selectors when performance is critical.
