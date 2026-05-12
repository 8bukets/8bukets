<<<<<<< bolt-optimize-scraper-12240886470808254228
## 2026-01-27 - BeautifulSoup Optimization
**Learning:** `html.parser` with `SoupStrainer('tag')` followed by `find()` is significantly faster (~3x in extraction) than parsing full DOM and using `select_one()` CSS selectors.
**Action:** Prefer `SoupStrainer` and `find()` over full parsing and CSS selectors for high-volume scraping tasks.
=======
## 2026-02-05 - [Async Event Loop Blocking by BeautifulSoup]
**Learning:** `BeautifulSoup` parsing is CPU-intensive and blocks the `asyncio` event loop even when called within an `async` function. In `scraper.py`, parsing 500 pages caused up to 115ms lag per tick, degrading concurrency.
**Action:** Offload CPU-bound parsing tasks to `ProcessPoolExecutor` using `loop.run_in_executor`. Ensure parsing functions are picklable (top-level module functions) to work with multiprocessing.
>>>>>>> sentinel-csv-injection-fix-6855106868508477486
