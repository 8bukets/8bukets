## 2025-05-23 - [BeautifulSoup Performance: SoupStrainer]
**Learning:** `SoupStrainer` with `html.parser` is ~1.6x faster than standard parsing for extraction tasks.
**Action:** Use `SoupStrainer` when only extracting specific tags (like `<a>` or `<table>`) from large pages.
