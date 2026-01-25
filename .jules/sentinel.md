# Sentinel Journal

## 2026-01-25 - Path Traversal in File Output
**Vulnerability:** `BlogScraper` allowed arbitrary file paths for `output_json` and `db_name` arguments, enabling writing files outside the intended directory via `..` traversal.
**Learning:** CLI tools accepting file paths as arguments must validate them against a trusted root directory to prevent overwriting sensitive files or writing to unauthorized locations.
**Prevention:** Use `os.path.abspath` and `os.path.commonpath` to enforce that user-supplied paths resolve within the current working directory or a specific safe directory.
