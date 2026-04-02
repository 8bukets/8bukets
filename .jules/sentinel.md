## 2025-01-25 - Path Traversal in CLI Tools
**Vulnerability:** Scraper and Analytics scripts accepted arbitrary output paths, allowing writes outside the working directory.
**Learning:** CLI tools accepting file paths as arguments are often overlooked for path traversal vulnerabilities compared to web endpoints.
**Prevention:** Enforce strict path validation using `os.path.commonpath` to ensure output files remain within the intended directory.
