## 2025-02-18 - Switch to lxml for Parsing Speed
**Learning:** Switching from Python's standard `html.parser` to `lxml` for BeautifulSoup parsing resulted in a ~23% performance improvement in scraping tasks.
**Action:** Use `lxml` as the default parser for BeautifulSoup when scraping large or multiple pages, provided the external dependency is acceptable.
