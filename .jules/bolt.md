## 2024-02-14 - HTML Parsing Bottleneck in Async Loop
**Learning:** Even when using `asyncio` for I/O bound tasks, CPU-bound tasks like `BeautifulSoup` parsing can block the event loop, degrading performance.
**Action:** Offload CPU-intensive parsing to `ProcessPoolExecutor` using `loop.run_in_executor` to keep the event loop free for network operations.
