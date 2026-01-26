## 2026-01-26 - Path Traversal in File Output
**Vulnerability:** The scraper allowed arbitrary file paths for output files (JSON, CSV, TXT), enabling potential overwriting of sensitive files outside the project directory.
**Learning:** `open()` in Python accepts relative paths that can traverse up directories (`../`). Relying on user input for filenames without validation is dangerous.
**Prevention:** Always validate file paths against a whitelist or a base directory using `os.path.abspath` and `os.path.commonpath` before opening them for writing.
