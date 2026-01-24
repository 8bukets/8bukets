## 2024-05-22 - [Async Event Loop Blocking]
**Learning:** CPU-bound operations like `BeautifulSoup` parsing inside `async` functions block the asyncio event loop, defeating the purpose of concurrency.
**Action:** Offload CPU-bound tasks to a separate thread using `await asyncio.to_thread(sync_func, ...)` to keep the loop free for I/O tasks.
