## 2026-01-03 - [SoupStrainer Optimization]
**Learning:** Using `SoupStrainer` with `BeautifulSoup` provides significant performance improvements (approx 28% faster in this case) for scraping tasks where only a subset of the DOM is needed.
**Action:** Always check if full DOM parsing is necessary. If only specific tags are needed, use `SoupStrainer`. However, be careful to include all parent tags required for context or structure (e.g., `nav` for pagination) as `SoupStrainer` discards non-matching tags and their subtrees unless they are descendants of a matched tag.
