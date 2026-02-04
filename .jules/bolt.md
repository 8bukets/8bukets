# Bolt's Journal

## 2024-05-23 - Sequential Subprocesses
**Learning:** The `ResearcherAgent` runs two independent scraping scripts sequentially using `subprocess.run`. This blocks the main thread for the sum of both durations.
**Action:** Use `concurrent.futures.ThreadPoolExecutor` to run independent subprocesses in parallel.
