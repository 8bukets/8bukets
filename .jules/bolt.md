## 2024-05-22 - Data Reuse in Analytics
**Learning:** `analytics.py` was redundantly parsing URLs to extract domains, even though `scraper.py` already pre-calculated and stored this information. This caused a significant performance overhead (~40% of user CPU time).
**Action:** Always check if upstream data sources (like scraper output) already contain the derived data needed for analysis before re-calculating it.
## 2026-02-26 - urlparse behavior for invalid URLs
**Learning:** `urllib.parse.urlparse` can return an empty string for `netloc` if the input is not a proper URL (e.g., 'not a url').
**Action:** Always check if the extracted domain is truthy before returning it, or return `None` explicitly if an empty string is not desired.
## 2026-02-26 - Asynchronous Agent Pipeline
**Learning:** For systems where individual components (like agents) perform network I/O, an asynchronous pipeline is significantly more efficient.
**Action:** Transitioned the agent ecosystem to fully async/await, standardizing on aiohttp for all network requests (including Robots.txt check) to reduce library bloat and improve concurrency.
## 2026-02-26 - Browser-Based Agent Verification
**Learning:** Pure HTTP scraping can miss UI elements or accessibility issues. Adding a Playwright-based agent allows for real-browser verification and visual regression testing.
**Action:** Integrated 'BrowserTestAgent' into the autonomous cycle to capture screenshots and verify site titles, enhancing the 'Google Antigravity' collaboration check.
## 2026-02-26 - Stage-Based Concurrent Agent Execution
**Learning:** Sequential execution of agents can be slow, especially when many agents perform I/O. Grouping agents by dependencies allows for safe parallelization within stages.
**Action:** Implemented a stage-based pipeline in 'run_system.py' using 'asyncio.gather', significantly improving the overall cycle performance while ensuring collaborative agents receive the necessary context.
## 2026-02-26 - Robust Persistence and Observability
**Learning:** File-based JSON memory is fragile for concurrent systems. SQLAlchemy with SQLite provides a robust, thread-safe persistence layer. Structured logging and rich CLI tools significantly enhance system observability.
**Action:** Migrated memory to SQLite, implemented dynamic agent loading, and added a rich dashboard to 'run_system.py' for better monitoring of the autonomous pipeline.
## 2026-02-26 - Production-Ready Autonomous Ecosystem
**Learning:** Hardcoding paths and interpreters (like 'python3') can cause failures in containers or virtualenvs. Using 'sys.executable' and standardizing project metadata (pyproject.toml) ensures cross-platform stability.
**Action:** Optimized the orchestrator for production, implemented containerization with 'Dockerfile' and 'docker-compose.yml', and added 'HEALTHCHECK' and '.dockerignore' for robust deployments.
## 2026-02-26 - Self-Autonomous Evolution and Meta-Coding
**Learning:** An autonomous system can be made self-evolving by implementing agents that write code for new agents based on data patterns. Dynamic loading ensures these new capabilities are integrated into the next cycle without human intervention.
**Action:** Implemented 'MetaCodingAgent' for autonomous agent generation, 'WebResearchAgent' for real-time external intelligence, and 'DocumentationAgent' for tracking system evolution in 'SYSTEM_EVOLUTION.md'.
