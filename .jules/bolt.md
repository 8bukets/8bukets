# Bolt's Journal

## 2024-05-22 - BeautifulSoup Performance
**Learning:** `BeautifulSoup.find()` is significantly faster (~50%) than `select_one()` for simple tag/class lookups in this codebase's environment. `select_one` uses `soupsieve` which adds overhead.
**Action:** Prefer `find()` and `find_all()` over CSS selectors when specificity is low (e.g., just tag and class).
