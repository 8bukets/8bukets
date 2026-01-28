## 2026-01-28 - SoupStrainer Optimization with html.parser
**Learning:** `BeautifulSoup(..., 'html.parser')` is CPU-heavy. Using `SoupStrainer` to limit parsing to specific tags (e.g., 'article') significantly reduces CPU usage (~28% in this case) even without `lxml`.
**Action:** When scraping specific elements with `html.parser`, always use `SoupStrainer` to restrict the parse tree.
