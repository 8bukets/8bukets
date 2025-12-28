## 2025-12-28 - Path Traversal in File Output
**Vulnerability:** The `save_json` method in `scraper.py` accepted an arbitrary file path from user arguments without validation. This allowed writing the output JSON to any location on the file system writable by the user (Path Traversal / Arbitrary File Write).
**Learning:** Even simple scripts that take output file paths as arguments must validate that the path is within the intended directory (usually CWD) to prevent overwriting critical system or application files.
**Prevention:** Use `os.path.abspath` to resolve the target path and `os.getcwd()` (or a configured root) to check that the target path starts with the allowed root directory using `os.path.commonpath`.
