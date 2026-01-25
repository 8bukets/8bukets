## 2026-01-25 - Blocking Operations in Async Scrapers
**Learning:** The scraper was mixing `asyncio` for network I/O with blocking synchronous `BeautifulSoup` parsing in the main event loop. This negates the benefits of async I/O as the loop is blocked during parsing.
**Action:** Always identify CPU-bound tasks in async workflows and offload them to threads using `asyncio.to_thread` or `loop.run_in_executor`.
