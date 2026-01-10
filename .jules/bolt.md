## 2024-01-20 - [Efficient HTML Parsing with SoupStrainer]
**Learning:** `BeautifulSoup` by default builds the entire DOM tree even if we only need to verify the existence of a few tags. Using `SoupStrainer` with `parse_only` allows `BeautifulSoup` to skip parsing irrelevant parts of the document, resulting in a ~30% speedup for structure verification tasks.
**Action:** When using `BeautifulSoup` for read-only tasks where only specific tags are needed, always use `SoupStrainer` to minimize parsing overhead.
