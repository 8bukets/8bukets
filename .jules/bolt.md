## 2025-01-18 - [Regex Extraction vs BeautifulSoup Parsing]
**Learning:** Parsing full HTML pages with BeautifulSoup just to extract a small section (like a comment) is inefficient (O(N) on document size). Using Regex to extract the target section first (O(N) but faster constant factor and no object creation) and then parsing only that snippet with BeautifulSoup significantly reduces CPU time and memory usage.
**Action:** When scraping large pages for small data snippets, consider extracting the snippet via Regex or string manipulation before invoking a full HTML parser.

## 2025-01-18 - [Offloading CPU-bound tasks in AsyncIO]
**Learning:** `BeautifulSoup` parsing is CPU-bound and blocks the AsyncIO event loop. Even for single pages, this interruption can affect responsiveness.
**Action:** Always offload parsing logic to a separate thread (using `asyncio.to_thread`) or process (using `concurrent.futures.ProcessPoolExecutor`) when running in an async context. For lightweight parsing (e.g. after Regex optimization), `asyncio.to_thread` is sufficient and avoids process overhead.
