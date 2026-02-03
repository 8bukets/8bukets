## 2025-02-23 - BeautifulSoup Performance Optimization
**Learning:** Parsing full HTML DOM is expensive when only specific tags are needed. Using `SoupStrainer` with `BeautifulSoup` significantly reduces parsing time (observed ~50% reduction) by only processing relevant tags.
**Action:** When scraping specific elements from large pages, always check if `SoupStrainer` can be used to filter tags at the parsing stage.
