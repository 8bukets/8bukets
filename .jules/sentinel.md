## 2025-02-18 - Path Traversal Risk in CLI Arguments
**Vulnerability:** `scraper.py` accepts file paths via CLI arguments (`--json`, `--db`) without validation, allowing users to overwrite arbitrary files if the script runs with sufficient privileges.
**Learning:** CLI tools often trust user input implicitly, but when automated or exposed, they become attack vectors.
**Prevention:** Always validate file paths using `os.path.commonpath` to ensure they remain within the expected directory (sandbox).
