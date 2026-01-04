## 2024-01-04 - [BeautifulSoup Performance: Find vs Select]
**Learning:** In this codebase's specific environment, `BeautifulSoup`'s `find()` method proved to be ~45% faster than `select_one()` (CSS selectors) for simple element lookups. This confirms the project's internal benchmarking notes.
**Action:** Prefer `find()`/`find_all()` over `select()`/`select_one()` for high-volume scraping loops where complex CSS selectors are not strictly necessary.
