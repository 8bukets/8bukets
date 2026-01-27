## 2026-01-27 - Optimizing BeautifulSoup with SoupStrainer
**Learning:** Parsing large HTML documents with `BeautifulSoup` is significantly faster when using `SoupStrainer` to limit the parse tree to only relevant tags (e.g., 'article'), especially when combined with replacing CSS selectors (`select_one`) with direct tag lookups (`find`).
**Action:** When scraping specific elements from large pages, always check if `SoupStrainer` can be used to discard unnecessary HTML structure before full parsing.
