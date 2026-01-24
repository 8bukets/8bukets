## 2024-05-23 - [Blocking Event Loop in Scraper]
**Learning:** `BeautifulSoup` parsing is a synchronous CPU-bound operation. When executed directly within an `async def` method, it blocks the entire `asyncio` event loop, preventing concurrent network requests from being processed effectively.
**Action:** Always wrap CPU-intensive parsing logic (like `BeautifulSoup` or heavy regex) in `asyncio.to_thread()` (or `loop.run_in_executor`) when working with `asyncio`. This ensures the event loop remains free to handle I/O operations.
