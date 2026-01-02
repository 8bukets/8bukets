## 2024-05-23 - [Secure File Output & CSV Sanitization]
**Vulnerability:** The scraper allowed writing files to arbitrary paths via CLI arguments (Path Traversal) and writing unsanitized user content to CSVs (CSV Injection), which could lead to arbitrary code execution if opened in spreadsheet software.
**Learning:** Libraries like `csv` do not automatically sanitize content for formula injection. Also, accepting file paths from user input without validation is a common oversight in CLI tools.
**Prevention:** Always validate file paths using `os.path.abspath` and `os.path.commonpath` to ensure they are contained within the intended directory. Explicitly sanitize any string starting with `=`, `+`, `-`, `@` before writing to CSV.
