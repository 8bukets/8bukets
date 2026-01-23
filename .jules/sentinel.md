## 2026-01-23 - Path Traversal in CLI Tools
**Vulnerability:** `scraper.py` and `analytics.py` allowed arbitrary file paths via CLI arguments (e.g., `../file`), enabling potential overwriting of critical files or reading sensitive data outside the working directory.
**Learning:** CLI tools often assume trusted input, but when used in automated pipelines or containers, path traversal can lead to container escape or data corruption. Standard `open()` does not validate path boundaries.
**Prevention:** Always validate user-supplied file paths using `os.path.abspath` and `os.path.commonpath` to ensure they resolve within the intended directory (e.g., CWD) before file operations.
