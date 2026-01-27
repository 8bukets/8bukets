## 2026-01-27 - Path Traversal in Scraper Outputs
**Vulnerability:** CLI scrapers (`scrape_informatic.py`, `google_search_scraper.py`) blindly trusted user-provided output paths, allowing writes to arbitrary locations (e.g., `/tmp/`, potentially system files).
**Learning:** Even internal CLI tools can be entry points for attacks if they run with elevated privileges or in shared environments. `os.path.abspath` alone resolves paths but doesn't validate boundaries.
**Prevention:** Enforce a sandbox by checking `os.path.commonpath([cwd, abs_path]) == cwd`. Centralize this validation in a `utils.py` module.
