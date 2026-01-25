## 2026-01-25 - Path Traversal in File Output
**Vulnerability:** The scraper accepted user-defined output paths without validation, allowing arbitrary file overwrites via path traversal (e.g., `../file`).
**Learning:** CLI tools that accept file paths as arguments must treat them as untrusted input, just like web inputs.
**Prevention:** Always resolve paths to absolute paths and verify they are contained within an intended directory (using `os.path.commonpath`) before writing.
