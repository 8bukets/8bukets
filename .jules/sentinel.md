## 2026-01-07 - Path Traversal in File Output
**Vulnerability:** The scraper script `scrape_informatic.py` allowed users to specify arbitrary output paths via the `-o` argument without validation. This permitted writing files to sensitive locations (e.g., `/etc/passwd`) or overwriting critical system files (Path Traversal).
**Learning:** Initial validation using `startswith()` against `base_dir` is insufficient because it allows sibling directory bypasses (e.g., `/tmp/app_backup` matches prefix `/tmp/app`).
**Prevention:** Always use `os.path.commonpath()` or ensure the base directory path ends with a directory separator when validating paths to prevent prefix matching bypasses. Additionally, never use `sys.exit()` inside a reusable library function; let exceptions propagate.
