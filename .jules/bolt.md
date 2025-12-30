## 2024-12-30 - SoupStrainer Optimization
**Learning:** Using `SoupStrainer` with `html.parser` allows BeautifulSoup to parse only a specific subset of the document tree (e.g., `<article>` tags), significantly reducing parsing time and memory usage (approx 3x faster in benchmarks).
**Action:** Always consider `SoupStrainer` when scraping large pages for specific elements, even if `lxml` is unavailable.
