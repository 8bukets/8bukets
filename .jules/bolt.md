## 2026-01-27 - [Parallel Subprocess Execution]
**Learning:** Sequential execution of independent I/O-bound subprocesses (like web scraping) is a significant bottleneck. Python's `ThreadPoolExecutor` is effective for parallelizing `subprocess.run` calls without blocking the main thread.
**Action:** Identify independent agent tasks that spawn external processes and refactor them to run concurrently using `concurrent.futures`.
