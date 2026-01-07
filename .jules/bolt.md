## 2024-05-23 - [BeautifulSoup Performance]
**Learning:** `html.parser` is significantly slower than `lxml` for large documents, and parsing the entire DOM is wasteful when extracting specific tags.
**Action:** Use `SoupStrainer` with `lxml` to parse only relevant tags (e.g., `<a>`), reducing parsing time by ~48% and memory usage.
