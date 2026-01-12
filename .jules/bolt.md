## 2025-02-19 - BeautifulSoup SoupStrainer Optimization
**Learning:** Using `SoupStrainer('a', href=True)` to parse only relevant tags improved parsing performance by ~45% (from 4.2s to 2.3s in benchmark).
**Action:** Always check if we need the full DOM tree when scraping; use `SoupStrainer` if we only target specific elements.
