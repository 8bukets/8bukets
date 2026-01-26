## 2026-01-26 - SoupStrainer Optimization
**Learning:** Parsing full HTML documents with BeautifulSoup when only specific tags are needed is wasteful. `SoupStrainer` reduced parsing time by ~21% in benchmarks by only creating objects for the required tags.
**Action:** Always use `SoupStrainer` when scraping large pages if you only need a subset of the DOM.
