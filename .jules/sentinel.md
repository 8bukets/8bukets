## 2025-12-31 - [Path Traversal in File Outputs]
**Vulnerability:** The scraper accepted user-controlled paths (`output_json` and `db_name`) without validation, allowing attackers to overwrite files outside the working directory (e.g., `../../etc/passwd`).
**Learning:** `os.path.abspath` alone is insufficient; `os.path.commonpath` is essential to verify that the resolved target path is strictly within the intended base directory (jail).
**Prevention:** Always validate file paths from user input using a strict allow-list or directory containment check (like `os.path.commonpath([cwd, abs_path]) == cwd`) before opening files.
