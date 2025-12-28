## 2024-12-28 - Missing Path Traversal Validation
**Vulnerability:** The scraper accepts output file paths without validation, allowing path traversal (e.g., `../outside.json`). While OS permissions might mitigate this in some environments, the application logic itself failed to enforce directory confinement.
**Learning:** A memory or documentation stating that a vulnerability is fixed (e.g., "strictly validated using `os.path.commonpath`") does not guarantee it is implemented in the actual code. Always verify code over documentation.
**Prevention:** Implement `os.path.commonpath` checks for all user-provided file paths before file operations.
