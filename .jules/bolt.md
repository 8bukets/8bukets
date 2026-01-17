# Bolt's Journal

## 2026-01-17 - Subprocess Overhead in Agents
**Learning:** The agent architecture (`ResearcherAgent`, `AnalyzerAgent`) relied on `subprocess.run` to call sibling scripts (`scrape_informatic.py`, `textblob`). This introduces significant overhead (process startup, file I/O for data passing) and prevents concurrency.
**Action:** Refactor agents to import and call functions directly. Use `ThreadPoolExecutor` for IO-bound tasks like scraping. Ensure scripts are importable (guard `main` with `if __name__ == "__main__":`).
