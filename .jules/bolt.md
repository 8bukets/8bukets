## 2026-01-23 - [Async Scraper Blocking Pattern]
**Learning:** This codebase uses `BeautifulSoup` with `html.parser` (blocking CPU operation) inside `async` functions without offloading to a thread. This negates the benefits of `aiohttp` by blocking the event loop. Also, `lxml` is missing despite documentation claims.
**Action:** Always verify dependencies and offload CPU-bound parsing to `asyncio.to_thread` when using `BeautifulSoup` in async scrapers.
