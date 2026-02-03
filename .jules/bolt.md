# BOLT'S JOURNAL - CRITICAL LEARNINGS ONLY

## 2026-02-03 - [Sequential Subprocesses Bottleneck]
**Learning:** The `ResearcherAgent` was executing independent scraping tasks (Blog Scraping and Google Search) sequentially using `subprocess.run`, adding unnecessary latency. These tasks are IO-bound and independent, making them perfect candidates for parallel execution.
**Action:** When identifying multiple `subprocess.run` calls or heavy IO tasks in a sequence, always check if they share dependencies. If not, parallelize them using `concurrent.futures.ThreadPoolExecutor` to reduce total execution time to roughly the duration of the longest task.
