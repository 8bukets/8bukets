# Sentinel 🛡️ Journal

## 2026-01-25 - Prevent Path Traversal in Scrapers

**Vulnerability:** Scraper scripts (`scrape_informatic.py`) accepted user-provided output paths without validation, allowing arbitrary file writes (Path Traversal, CWE-22).
**Learning:** Utilities that accept file paths as arguments must validate them against a safe root directory (like CWD) before writing. `os.path.commonpath` is a reliable way to check directory containment.
**Prevention:** Always use a canonical path validation helper (like `validate_path`) for any file path inputs.
