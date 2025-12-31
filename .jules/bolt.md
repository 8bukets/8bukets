## 2024-05-23 - BeautifulSoup Performance and Blocking I/O
**Learning:**
1. `lxml` is significantly faster than `html.parser` but requires an external dependency, which must be managed carefully.
2. `SoupStrainer` is an effective optimization but depends on the underlying parser's capabilities.
3. For asyncio-based scrapers, running CPU-bound tasks like `BeautifulSoup` parsing in the main thread blocks the event loop, negating concurrency benefits. Offloading these tasks to `loop.run_in_executor` (thread pool) is a critical optimization to maintain high throughput.
**Action:** Always wrap CPU-intensive parsing logic in a synchronous function and call it via `await loop.run_in_executor(None, sync_func, ...)` in async applications.
