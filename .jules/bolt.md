## 2024-05-23 - BeautifulSoup SoupStrainer Optimization
**Learning:** Parsing full HTML documents when only a subset of tags is needed is a major performance bottleneck in `bs4`. Using `SoupStrainer` to restrict parsing to specific tags (e.g., `article` with class `post`) reduced parsing time by ~56% in benchmarks.
**Action:** When scraping large pages for specific elements, always use `SoupStrainer` with the `parse_only` argument in `BeautifulSoup` constructor to avoid parsing unnecessary DOM nodes.
