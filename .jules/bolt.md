## 2025-02-03 - Offloading BeautifulSoup to ProcessPoolExecutor
**Learning:** `BeautifulSoup` parsing is CPU-bound and blocks the `asyncio` event loop. Offloading it to a `ProcessPoolExecutor` allows the loop to continue processing network events, preventing bottlenecks during heavy parsing.
**Action:** When scraping large HTML pages in an async application, always offload the parsing logic to a separate process or thread (if GIL is not an issue, but for BS4 processes are safer).
