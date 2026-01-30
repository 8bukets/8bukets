## 2025-01-30 - [Blocking Parsing in Async Loop]
**Learning:** `BeautifulSoup` parsing is a CPU-bound operation that blocks the asyncio event loop even when inside an `async def`.
**Action:** Offload heavy parsing logic to a thread executor using `loop.run_in_executor` to maintain concurrency for network tasks.
