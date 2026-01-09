## 2025-05-18 - [Optimized HTML Parsing with SoupStrainer]
**Learning:** `BeautifulSoup` parsing can be significantly accelerated (over 60% faster) by using `SoupStrainer` to parse only relevant tags (e.g., `<a>`) and using the `lxml` parser.
**Action:** Use `SoupStrainer` and `lxml` for large HTML documents when only specific tags are needed, but always implement a fallback to `html.parser` if `lxml` is not guaranteed to be present.
