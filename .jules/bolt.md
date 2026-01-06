## 2025-02-14 - BeautifulSoup SoupStrainer Optimization
**Learning:** `SoupStrainer` significantly speeds up parsing (2.5x in this case) by instructing BeautifulSoup to only build the DOM tree for specific tags. Crucially, when using `html.parser`, it preserves the full subtree of the matched tags, allowing for safe extraction of child elements.
**Action:** Use `SoupStrainer` for scraping tasks where the target data is confined to specific container elements (like `<article>` or `<div class="content">`), especially when parsing large pages with irrelevant headers/footers.
