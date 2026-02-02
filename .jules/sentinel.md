## 2026-02-02 - Path Traversal in Scraper Output
**Vulnerability:** The `scraper.py` script accepted output file paths from command-line arguments without validation, allowing users to write files to arbitrary locations on the filesystem (Path Traversal).
**Learning:** CLI tools often trust user input too much. Even internal tools can be misused or exploited if they handle file paths insecurely. Using `os.path.abspath` alone is insufficient if symlinks are involved; `os.path.realpath` is safer.
**Prevention:** Always validate output paths against a safe directory (whitelist approach) using `os.path.commonpath` with resolved paths (`os.path.realpath`).
