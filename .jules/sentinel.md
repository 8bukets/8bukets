## 2025-02-19 - Path Traversal in CLI Arguments
**Vulnerability:** `scraper.py` accepted output file paths via CLI arguments without validation, allowing arbitrary file overwrite via path traversal (e.g., `../file`).
**Learning:** CLI tools that write files based on user input are susceptible to Arbitrary File Write if not sandboxed or validated.
**Prevention:** Validate all file paths using `os.path.abspath` and `os.path.commonpath` to ensure they stay within the intended directory (e.g., CWD).
