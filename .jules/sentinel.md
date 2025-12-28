## 2024-12-25 - Path Traversal in File Output
**Vulnerability:** The scraper accepted arbitrary file paths for output files (JSON, CSV, TXT) without validation. This allowed an attacker to overwrite sensitive files outside the application directory (e.g., `../../etc/passwd` or system config files) by supplying a path like `../hacked.json`.
**Learning:** Python's `open()` function happily accepts relative paths that traverse directories. Trusting user input (or CLI arguments) for file paths directly is dangerous.
**Prevention:** Always validate output paths. Use `os.path.abspath()` to resolve the target path and `os.path.commonpath()` (or strict prefix checking) to ensure the resolved path resides within the intended directory (e.g., the current working directory).
