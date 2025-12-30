## 2024-05-23 - Path Traversal in File Outputs
**Vulnerability:** User-controlled output paths in `scraper.py` and `analytics.py` allowed writing files outside the current working directory via path traversal (e.g., `../file`).
**Learning:** Python's `open()` does not validate if the path is within the intended directory. Accepting file paths from CLI arguments without validation is risky.
**Prevention:** Use `os.path.abspath` and `os.path.commonpath` to enforce that all file write operations are contained within the current working directory.
