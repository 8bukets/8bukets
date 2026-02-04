## 2025-02-18 - CPU-bound Parsing in Async Scrapers
**Learning:** `BeautifulSoup` parsing is a synchronous, CPU-bound operation. When running in an `asyncio` event loop (like in `scraper.py`), it blocks the loop, preventing other concurrent network requests from progressing, effectively nullifying the benefits of `aiohttp`.
**Action:** Offload heavy parsing logic to a `ProcessPoolExecutor` using `loop.run_in_executor`. Ensure parsing functions are top-level or static (picklable) to work with the executor.
