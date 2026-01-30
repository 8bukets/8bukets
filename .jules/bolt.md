## 2025-01-30 - [Blocking Async Event Loop]
**Learning:** CPU-bound operations like BeautifulSoup parsing in `async` functions block the asyncio event loop, defeating the purpose of asynchronous I/O.
**Action:** Offload CPU-heavy parsing to `loop.run_in_executor` to keep the event loop free for network tasks.
