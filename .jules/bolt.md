## 2024-05-22 - [Asyncio Blocking Bottleneck]
**Learning:** CPU-bound operations like `BeautifulSoup` parsing block the asyncio event loop, negating concurrency benefits.
**Action:** Offload heavy parsing to `concurrent.futures.ProcessPoolExecutor` using `loop.run_in_executor` to keep the loop free for I/O.
