## 2026-02-05 - [Async Event Loop Blocking by BeautifulSoup]
**Learning:** `BeautifulSoup` parsing is CPU-intensive and blocks the `asyncio` event loop even when called within an `async` function. In `scraper.py`, parsing 500 pages caused up to 115ms lag per tick, degrading concurrency.
**Action:** Offload CPU-bound parsing tasks to `ProcessPoolExecutor` using `loop.run_in_executor`. Ensure parsing functions are picklable (top-level module functions) to work with multiprocessing.
