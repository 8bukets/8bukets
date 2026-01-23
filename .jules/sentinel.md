## 2026-01-23 - Path Traversal in Scraper Output
**Vulnerability:** The scraper accepted arbitrary file paths for JSON and SQLite output via CLI arguments, allowing writing files to arbitrary locations (e.g., `/tmp`, `../`).
**Learning:** `open()` and `sqlite3.connect()` do not validate that paths are within the intended directory. CLI arguments defaulting to current directory filenames gave a false sense of security.
**Prevention:** Always validate user-provided file paths using `os.path.abspath` and `os.path.commonpath` to ensure they are within the expected directory (sandbox).
