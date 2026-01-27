## 2026-01-27 - CSV Injection and Path Traversal in Scraper
**Vulnerability:** The scraper accepted unsanitized input for CSV generation and unvalidated file paths for output.
**Learning:** Python's `csv` module does not automatically sanitize formula injection characters (`=`, `+`, `-`, `@`). CLI tools accepting paths must validate them against the CWD.
**Prevention:** Implement input sanitization for CSV fields and strict path validation using `os.path.abspath` and `os.path.commonpath`.
