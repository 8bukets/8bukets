## 2024-01-24 - Async Scraper Blocking
**Learning:** `BeautifulSoup` parsing is CPU-intensive and blocks the `asyncio` event loop, negating the benefits of concurrent fetching.
**Action:** Offload parsing to a separate thread using `asyncio.to_thread` to maintain event loop responsiveness during heavy parsing.
