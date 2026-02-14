# Sentinel Journal

## 2025-12-25 - [Fix Path Traversal in Scraper]
**Vulnerability:** The scraper accepted output filenames directly from command-line arguments without validation, allowing for path traversal (e.g., `../file.json`). This could potentially allow overwriting critical files if the scraper is run with elevated privileges or user-supplied input.
**Learning:** Even CLI tools should validate file paths when they accept them as arguments, especially if they might be part of a larger automated system. Trusting user input for file operations is a common source of vulnerabilities.
**Prevention:** Validate that output paths are within the intended directory (e.g., current working directory) using `os.path.abspath` and `os.path.commonpath`.
