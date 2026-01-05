## 2024-05-23 - BeautifulSoup Selector Performance
**Learning:** `BeautifulSoup.find()` and `find_all()` are significantly faster (approx 40%) than `select()` and `select_one()` because they avoid the overhead of parsing CSS selectors.
**Action:** Prefer `find()` methods over CSS selectors in high-volume scraping loops where complex selectors are not strictly necessary.
