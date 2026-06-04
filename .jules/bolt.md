## 2026-02-05 - URL Parsing in Scrapers
**Learning:** Repeatedly calling `urlparse()` inside tight loops (like checking external links for every scraped element) adds significant overhead. Pre-parsing constant base URLs can improve performance by ~50% in link-heavy checks.
**Action:** Pass pre-parsed `ParseResult` objects to helper functions instead of raw URL strings when the URL is constant or reused.
## 2026-01-27 - [Parallel Subprocess Execution]
**Learning:** Sequential execution of independent I/O-bound subprocesses (like web scraping) is a significant bottleneck. Python's `ThreadPoolExecutor` is effective for parallelizing `subprocess.run` calls without blocking the main thread.
**Action:** Identify independent agent tasks that spawn external processes and refactor them to run concurrently using `concurrent.futures`.
## 2026-02-06 - [Parallelizing IO-bound Agents]
**Learning:** The `ResearcherAgent` was sequentially shelling out to python scripts (`subprocess.run`) for independent IO-bound tasks (scraping and searching). This doubled the latency. Importing the modules and using `ThreadPoolExecutor` allowed them to run concurrently, effectively halving the wait time for the shorter task.
**Action:** Always check if agent tasks are independent and IO-bound; if so, parallelize them using threads or async. Prefer importing modules over `subprocess` for lower overhead and better integration.
