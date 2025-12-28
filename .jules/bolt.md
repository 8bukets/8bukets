## 2024-12-27 - [lxml Parser Optimization]
**Learning:** Switching from `html.parser` to `lxml` in BeautifulSoup provides a significant performance boost (~18%) for parsing large HTML documents, even with simple structure.
**Action:** Default to `lxml` for scraping tasks where performance is critical and C-extensions are permitted.
