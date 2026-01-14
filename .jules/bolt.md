## 2025-02-12 - BeautifulSoup Performance in Async Context
**Learning:** `BeautifulSoup` parsing is synchronous and CPU-intensive, which blocks the `asyncio` event loop. Using `SoupStrainer` significantly reduces this overhead (~2.5x faster) by parsing only relevant tags, which is critical when offloading to threads isn't implemented.
**Action:** Always check if `SoupStrainer` can be applied when using `BeautifulSoup` in scraping logic, especially within async functions.
