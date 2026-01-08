## 2024-02-14 - Blocking Event Loop with BeautifulSoup
**Learning:** `BeautifulSoup` parsing is a CPU-bound operation. When running inside an `asyncio` loop (like in `scraper.py`), calling it directly blocks the entire event loop, preventing other concurrent tasks (like network requests) from progressing. This negates the benefits of concurrency for heavy scraping tasks.
**Action:** Always offload CPU-intensive parsing to a separate thread using `asyncio.to_thread` (or `loop.run_in_executor`) to keep the event loop responsive.
