## 2025-10-26 - [Blocking Event Loop in Async Scraper]
**Learning:** `BeautifulSoup` parsing is synchronous and blocks the asyncio event loop. Even if declared in an `async` function, CPU-bound tasks halt all other async operations (like network requests).
**Action:** Offload CPU-bound tasks like parsing to a thread pool using `loop.run_in_executor` to keep the event loop responsive.
