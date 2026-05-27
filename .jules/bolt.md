## 2026-01-27 - Optimizing BeautifulSoup with SoupStrainer
**Learning:** Parsing large HTML documents with `BeautifulSoup` is significantly faster when using `SoupStrainer` to limit the parse tree to only relevant tags (e.g., 'article'), especially when combined with replacing CSS selectors (`select_one`) with direct tag lookups (`find`).
**Action:** When scraping specific elements from large pages, always check if `SoupStrainer` can be used to discard unnecessary HTML structure before full parsing.
## 2025-01-26 - SoupStrainer with html.parser
**Learning:** SoupStrainer does not improve parsing performance significantly when used with 'html.parser' because the parser still tokenizes the entire document. It may save memory but can be CPU neutral or even slower due to overhead. Measurable gains require 'lxml'.
**Action:** Only use SoupStrainer for performance if 'lxml' is available. Otherwise, consider regex splitting for massive documents if strict correctness is not required.
## 2024-05-22 - Data Reuse in Analytics
**Learning:** `analytics.py` was redundantly parsing URLs to extract domains, even though `scraper.py` already pre-calculated and stored this information. This caused a significant performance overhead (~40% of user CPU time).
**Action:** Always check if upstream data sources (like scraper output) already contain the derived data needed for analysis before re-calculating it.
