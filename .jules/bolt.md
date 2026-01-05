## 2024-05-23 - BeautifulSoup Selectors vs Find
**Learning:** `BeautifulSoup`'s `select` and `select_one` methods (CSS selectors) are significantly slower (~45%) than direct `find` and `find_all` methods for simple lookups. This is because CSS selectors require parsing and traversing the tree in a more complex way.
**Action:** Prefer `find` / `find_all` for hot paths in scrapers where performance matters, especially when extracting simple attributes or classes.
