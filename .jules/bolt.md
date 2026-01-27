## 2024-05-22 - BeautifulSoup Selector Performance
**Learning:** In this codebase, replacing CSS selectors (`select_one`) with direct tag searches (`find`) yielded a ~46% performance improvement for element extraction. `SoupStrainer` provided a smaller (~6%) but additive gain.
**Action:** Prefer `find/find_all` over `select/select_one` in tight loops or high-volume scraping tasks.
