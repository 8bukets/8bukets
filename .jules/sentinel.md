## 2025-01-26 - Path Traversal in File Outputs
**Vulnerability:** Scraper and analytics scripts accepted arbitrary file paths for output, allowing writing to files outside the working directory (e.g., `../file.txt`).
**Learning:** The codebase uses `argparse` to take file paths but assumes users will provide safe paths. `open()` in Python accepts relative paths that can traverse directories.
**Prevention:** Always validate file paths provided by users. Use `os.path.abspath` and `os.path.commonpath` to ensure the resolved path is within the intended directory (CWD or specific output folder).
