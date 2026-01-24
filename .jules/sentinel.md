## 2025-02-18 - Path Traversal in Local CLI Tools
**Vulnerability:** `scraper.py` allowed writing files to arbitrary paths via command line arguments (e.g., `--json ../system_file`).
**Learning:** Even local automation scripts can be vulnerable to path traversal if they accept file paths as input. This can be exploited if the script is run with elevated privileges or as part of a pipeline where inputs are controlled by an attacker.
**Prevention:** Always validate output file paths are within the intended directory using `os.path.abspath` and `os.path.commonpath` before writing.
