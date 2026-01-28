## 2026-01-28 - BeautifulSoup Performance: Find vs Select and Regex
**Learning:** `BeautifulSoup`'s `find()` and `find_all()` methods are faster than CSS selectors (`select()`, `select_one()`) because they avoid the overhead of the CSS selector compiler. Also, compiling regex patterns as class attributes avoids re-compilation in tight loops.
**Action:** Replace `select_one()` with `find()` where possible, and compile `re` patterns at the class level.
