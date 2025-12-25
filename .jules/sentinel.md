## 2025-02-19 - Path Traversal in Scraper Output
**Vulnerability:** The scraper scripts (`scrape_informatic.py`, `google_search_scraper.py`) accept user-defined output paths without validation, allowing arbitrary file writes (Path Traversal).
**Learning:** CLI tools often overlook input validation for file paths, assuming they will be run by trusted users. However, if these tools are part of a larger automated system or exposed via an interface, this becomes a critical vulnerability.
**Prevention:** Always sanitize file paths. Use `os.path.basename` to strip directories or validate that the resolved path is within an allowed directory.
