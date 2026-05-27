## 2024-05-22 - [CLI Path Traversal]
**Vulnerability:** `scraper.py` and `analytics.py` allowed writing output files to arbitrary paths via CLI arguments (e.g., `../evil.json`).
**Learning:** Even local CLI tools can be vectors for path traversal if they accept file paths as arguments without validation, especially if wrapped by other systems.
**Prevention:** Implemented `validate_output_path` in `utils.py` to enforce that output paths are within the current working directory using `os.path.abspath` and `os.path.commonpath`.
