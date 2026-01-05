## 2024-05-22 - BeautifulSoup `find` vs `select`
**Learning:** `find()`/`find_all()` is significantly faster (~44%) than `select_one()`/`select()` for simple tag/class lookups in BeautifulSoup. `select` involves parsing CSS selectors which adds overhead.
**Action:** Prefer `find` for direct tag/class lookups. Reserve `select` for complex nested selectors where readability outweighs the performance cost.
