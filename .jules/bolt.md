## 2024-05-23 - BeautifulSoup Selectors vs Find
**Learning:** `BeautifulSoup`'s CSS selectors (`select`, `select_one`) are significantly slower (~37%) than the native `find` and `find_all` methods for this specific HTML structure and usage. This is likely due to the overhead of parsing the CSS selector string and the additional abstraction layer.
**Action:** Prefer `find()` and `find_all()` over `select()`/`select_one()` in hot loops, especially when the selector is simple (e.g., just a tag and class).
