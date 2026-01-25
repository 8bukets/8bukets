## 2025-02-19 - SoupStrainer Optimization
**Learning:** `BeautifulSoup` parsing overhead can be significantly reduced (up to 24% in synthetic tests, ~9% in full extraction) by using `SoupStrainer` to parse only relevant `article` tags, especially on large pages like WordPress archives with many posts (350+ per page).
**Action:** Always consider `SoupStrainer` when extracting specific repeated elements from large documents.
