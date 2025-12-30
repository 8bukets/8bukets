## 2024-05-23 - [Optimization: SoupStrainer for Partial Parsing]
**Learning:** `BeautifulSoup` parses the entire HTML document by default. Using `SoupStrainer` with `html.parser` (when `lxml` is unavailable) to filter for specific tags (e.g., `article`) before parsing significantly reduces parsing time (~1.6x faster in benchmarks).
**Action:** Always check if full document parsing is necessary. If only specific sections are needed, use `SoupStrainer` to limit the scope of the parser, especially for large HTML documents.
