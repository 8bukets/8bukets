## 2026-01-24 - CLI Output Path Traversal
**Vulnerability:** CLI tools `scrape_informatic.py` and `google_search_scraper.py` accepted an output file path argument without validation, allowing arbitrary file writes via path traversal (e.g., `../../file.txt`).
**Learning:** Developers often assume CLI tools are run by trusted users or in trusted environments, neglecting input validation for file system operations.
**Prevention:** Always validate file paths provided as input using `os.path.abspath` and `os.path.commonpath` to ensure they reside within the intended directory sandbox.
