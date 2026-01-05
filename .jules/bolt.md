## 2026-01-05 - [BeautifulSoup Performance: Find vs Select]
**Learning:** `BeautifulSoup`'s `find`/`find_all` methods are significantly faster (~45%) than CSS selectors (`select`/`select_one`) for this project's scraping tasks. The overhead of compiling and evaluating CSS selectors adds up in tight loops or large documents.
**Action:** Prefer `find` methods for scraping logic, especially in high-frequency loops. Use variables to store intermediate elements (like header/meta containers) to avoid redundant traversals.
