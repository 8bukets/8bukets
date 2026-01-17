## 2024-05-22 - Asyncio Blocking Operations
**Learning:** CPU-bound tasks like BeautifulSoup parsing inside an async function block the event loop, reducing concurrency throughput.
**Action:** Offload such tasks to a thread pool using `loop.run_in_executor`.
