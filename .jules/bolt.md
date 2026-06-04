## 2024-05-23 - BeautifulSoup SoupStrainer Optimization
**Learning:** Parsing the entire HTML document with `BeautifulSoup` when only a specific subset of tags is needed is wasteful. Using `SoupStrainer('a', href=True)` to filter tags *before* creating the full parse tree resulted in a ~40% performance improvement (1.5s vs 2.5s in benchmarks) for extracting links.
**Action:** Always consider `SoupStrainer` when scraping specific elements from large HTML pages, especially if using the default `html.parser` which is slower than `lxml`.
## 2026-02-06 - Redundant URL Parsing
**Learning:** The analytics pipeline was performing redundant `urlparse` operations on every record to extract domains, ignoring the existing `domain` field provided by the scraper. This highlighted the importance of verifying input data schema before implementing extraction logic.
**Action:** When optimizing data processing scripts, first inspect the full schema of the input data to identify pre-calculated fields that can replace runtime computations.
