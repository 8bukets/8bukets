## 2024-02-14 - BeautifulSoup Performance: Find vs Select
**Learning:** `find()`/`find_all()` is significantly faster (~44%) than `select_one()`/`select()` (CSS selectors) for simple attribute lookups in BeautifulSoup 4.
**Action:** Use `find()` for direct tag/class lookups in tight loops. Use `select()` only when complex nested selectors are strictly necessary for readability.
