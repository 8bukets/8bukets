## 2024-05-22 - Optimizing BeautifulSoup Parsing
**Learning:** Parsing full HTML documents with BeautifulSoup is expensive. Using `SoupStrainer` to parse only relevant tags (e.g. `article` for blog posts) can reduce parsing time by over 60%. Additionally, replacing `select_one` (CSS selectors) with `find` (native tag lookup) improves extraction speed by ~40%.
**Action:** When scraping large pages where only a specific section is needed, always use `SoupStrainer` and prefer `find`/`find_all` over `select`/`select_one`.
