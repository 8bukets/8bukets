## 2026-02-01 - Agent Subprocess Parallelization
**Learning:** The `ResearcherAgent` invoked multiple independent subprocesses sequentially, which was a clear bottleneck for I/O bound tasks. Since the agent architecture relies on standalone scripts, `concurrent.futures.ThreadPoolExecutor` is effective for parallelizing these subprocess calls without modifying the scripts themselves.
**Action:** When working with agent-based architectures where tasks are delegated to subprocesses, always check for opportunities to run independent tasks concurrently.
