# Bolt's Journal

## 2026-01-28 - [Parallelized Researcher Agent]
**Learning:** `subprocess.run` blocks the main thread, making independent IO-bound tasks run sequentially unnecessarily. Using `ThreadPoolExecutor` allows these tasks (blog scraping and Google search) to run concurrently, effectively hiding the latency of the shorter task behind the longer one.
**Action:** When an agent needs to perform multiple independent external calls (subprocesses or API requests), use concurrency (threads or asyncio) to execute them in parallel.
