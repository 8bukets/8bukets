## 2026-01-27 - Path Traversal in Scraper Output
**Vulnerability:** The scraper accepted arbitrary file paths for output files (JSON, CSV, TXT), allowing an attacker to potentially overwrite sensitive files on the system by providing paths like `../../etc/passwd`.
**Learning:** CLI tools that accept file paths as arguments are often overlooked for path traversal vulnerabilities. Relying on `open()` without validation assumes the user is benevolent or the environment is sandboxed, which may not be true.
**Prevention:** Implement a strict validation layer using `os.path.abspath` and `os.path.commonpath` to ensure all file operations occur within a designated safe directory (e.g., the current working directory).
