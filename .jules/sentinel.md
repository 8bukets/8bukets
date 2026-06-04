# Sentinel Security Journal

## 2025-10-15 - Path Traversal in File Output
**Vulnerability:** User-controlled output paths in `scraper.py` allowed writing files outside the working directory (Path Traversal).
**Learning:** CLI tools accepting file paths as arguments must validate that the resolved path is within the intended directory, even if they are just "scrapers".
**Prevention:** Use `os.path.abspath` and `os.path.commonpath` to validate paths against `os.getcwd()` before opening files.
