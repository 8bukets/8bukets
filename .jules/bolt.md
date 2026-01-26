## 2025-01-26 - SoupStrainer for Partial Parsing
**Learning:** Parsing full HTML pages with `BeautifulSoup` is CPU-intensive. When only specific tags (e.g., `<article>`) are needed, `SoupStrainer` reduces parsing time by ~25% by ignoring the rest of the document (headers, sidebars, scripts).
**Action:** Use `SoupStrainer` in `BeautifulSoup` constructor whenever extracting data from specific sections of large HTML documents.
