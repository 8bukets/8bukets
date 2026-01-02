## 2024-05-23 - Scraper Input/Output Vulnerabilities
**Vulnerability:** The scraper accepted arbitrary output paths (leading to Path Traversal) and wrote unsanitized data to CSV (leading to CSV Injection).
**Learning:** Utilities that accept file paths as arguments from users (CLI) or configuration must validate that the paths are contained within expected directories, especially when running in environments where file system access is broad.
**Prevention:** Implemented `validate_output_path` using `os.path.commonpath` to enforce sandbox boundaries and `sanitize_for_csv` to neutralize active content triggers (`=`, `+`, `-`, `@`).
