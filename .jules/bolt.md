## 2024-05-23 - BeautifulSoup SoupStrainer Performance
**Learning:** `SoupStrainer` with `html.parser` yields a 3x speedup over standard parsing by avoiding full tree construction. While `lxml` is even faster (6x), `html.parser` + `SoupStrainer` is a significant optimization that requires no extra dependencies.
**Action:** Always use `SoupStrainer` when scraping specific tags from large documents, even if stuck with `html.parser`.
