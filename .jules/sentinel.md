## 2026-01-22 - [Path Traversal in Output Files]
**Vulnerability:** Scraper scripts (`scrape_informatic.py` and `google_search_scraper.py`) accepted an output file path via CLI argument without validation, allowing writing to arbitrary files (Path Traversal). Initial fix using `startswith` was vulnerable to partial path traversal (e.g. `/path/to/dir_suffix`).
**Learning:** CLI tools that accept file paths for output must validate that the path is within the intended directory. Using `startswith` is insufficient.
**Prevention:** Use `os.path.commonpath([abs_cwd, abs_output]) == abs_cwd` to strictly ensure the path is within the directory, or verify the path prefix ends with the system separator.
