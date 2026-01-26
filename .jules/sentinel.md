## 2025-02-18 - Path Traversal in CLI Tools
**Vulnerability:** `scraper.py` and `analytics.py` accepted output file paths via CLI arguments without validation, allowing arbitrary file writes (Path Traversal) outside the project directory.
**Learning:** Python's `argparse` does not validate paths by default. CLI tools that write files must explicitly check that the target path is within allowed boundaries to prevent overwriting system files or malicious payload placement.
**Prevention:** Use `os.path.abspath` and `os.path.commonpath` to ensure the resolved output path starts with the expected root directory (e.g., `os.getcwd()`) before opening files for writing.
