## 2026-01-27 - Path Traversal in Scraper Output
**Vulnerability:** `scraper.py` accepted paths outside the working directory (e.g. `../file.json`) for output arguments, allowing arbitrary file overwrite.
**Learning:** CLI tools taking file paths as arguments often overlook validation, assuming benign user intent.
**Prevention:** Enforce output paths to be within the current working directory using `os.path.abspath` and `os.path.commonpath`.
