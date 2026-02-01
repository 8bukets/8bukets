## 2025-02-19 - Batching vs Pipelining for Scrapers
**Learning:** `asyncio.gather` on batches of tasks suffers from the "straggler problem" where the entire batch waits for the slowest request. A pipeline using `asyncio.wait(return_when=FIRST_COMPLETED)` with a controlled set of tasks significantly improves throughput for I/O bound scraping (~40% faster).
**Action:** Default to worker queues or dynamic task sets for scraping instead of batching.
