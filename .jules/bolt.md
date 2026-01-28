## 2025-02-18 - BeautifulSoup Selector Performance
**Learning:** In this environment, `BeautifulSoup.select_one` (CSS selectors) proved to be ~13% slower than chained `find` calls for extracting data from large HTML documents.
**Action:** Default to `find()`/`find_all()` for high-frequency scraping paths; reserve CSS selectors for complex queries where `find` chains would be unreadable.
