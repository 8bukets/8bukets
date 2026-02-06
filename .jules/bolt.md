## 2026-02-06 - [Parallelizing IO-bound Agents]
**Learning:** The `ResearcherAgent` was sequentially shelling out to python scripts (`subprocess.run`) for independent IO-bound tasks (scraping and searching). This doubled the latency. Importing the modules and using `ThreadPoolExecutor` allowed them to run concurrently, effectively halving the wait time for the shorter task.
**Action:** Always check if agent tasks are independent and IO-bound; if so, parallelize them using threads or async. Prefer importing modules over `subprocess` for lower overhead and better integration.
