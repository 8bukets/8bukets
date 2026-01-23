## 2026-01-23 - HTML Conversion Bottleneck
**Learning:** Using `markdownify(str(soup))` forces serialization and re-parsing, which is O(N) redundant work. In `scrape_informatic.py`, this was done per-post.
**Action:** Use `MarkdownConverter().convert_soup(soup)` to convert directly from the BeautifulSoup tree. Measured ~3.6x speedup.
