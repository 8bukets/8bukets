## 2024-10-24 - [Path Traversal & CSV Injection in Scraper]
**Vulnerability:** The scraper accepted arbitrary file paths for output, allowing potential file system overwrites (Path Traversal). It also wrote unsanitized user content to CSVs, allowing formula injection.
**Learning:** CLI tools that accept file paths as arguments must validate them against the expected directory scope, even if they aren't web servers. Data scraped from the web must be treated as untrusted user input when generating artifacts like CSVs.
**Prevention:** Use `os.path.abspath` and `os.path.commonpath` to lock file operations to a specific directory. Prepend `'` to CSV fields starting with `=`, `+`, `-`, `@` to neutralize formulas.
