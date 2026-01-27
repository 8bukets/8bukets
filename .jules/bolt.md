## 2026-01-27 - BeautifulSoup Optimization
**Learning:** `html.parser` with `SoupStrainer('tag')` followed by `find()` is significantly faster (~3x in extraction) than parsing full DOM and using `select_one()` CSS selectors.
**Action:** Prefer `SoupStrainer` and `find()` over full parsing and CSS selectors for high-volume scraping tasks.
