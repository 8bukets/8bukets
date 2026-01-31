## 2026-01-31 - [Offloading CPU-bound parsing to ThreadPool]
**Learning:** `BeautifulSoup` parsing is a synchronous, CPU-intensive operation that blocks the asyncio event loop. Even with `aiohttp`, parsing in the main loop limits concurrency because the loop cannot schedule new network tasks while parsing.
**Action:** Always offload blocking CPU operations (like HTML parsing with BS4) to `loop.run_in_executor` to keep the event loop free for I/O.
