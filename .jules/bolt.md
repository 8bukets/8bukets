## 2026-01-08 - Parallel Subprocess Execution
**Learning:** Python's `subprocess.run` releases the GIL while waiting for the external process to complete. This means `ThreadPoolExecutor` is highly effective for parallelizing multiple subprocess calls, even in a single-threaded Python application.
**Action:** When orchestrating multiple independent CLI tools or scripts via `subprocess`, always wrap them in `ThreadPoolExecutor` (or `asyncio` if available) instead of running them sequentially. This is a low-risk, high-reward optimization for IO-bound orchestration tasks.
