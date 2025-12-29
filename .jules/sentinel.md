## 2025-01-01 - [Path Traversal & CSV Injection Fixes]
**Vulnerability:**
1. **Path Traversal:** The `scraper.py` allowed users to specify arbitrary file paths for output (e.g., `../../etc/passwd`), potentially leading to file overwrites outside the intended directory.
2. **CSV Injection:** The scraper exported data to CSV without sanitizing fields. Malicious input (e.g., titles starting with `=`) could execute formulas in spreadsheet software (Excel, LibreOffice) when opened by an admin.

**Learning:**
1. **Path Validation:** Python's `open()` does not inherently restrict paths. Explicit validation against the current working directory (`os.getcwd()`) or a specific output folder is required.
2. **CSV Trust:** CSVs are often treated as simple text files, but spreadsheet software parses them as active documents. Any user-controlled input in a CSV must be sanitized (typically by prepending `'`).

**Prevention:**
1. **Validation Wrapper:** I implemented a `validate_path` method that checks if the resolved absolute path starts with the CWD.
2. **Sanitization Wrapper:** I implemented a `sanitize_for_csv` method that prepends `'` to dangerous characters (`=`, `+`, `-`, `@`).
