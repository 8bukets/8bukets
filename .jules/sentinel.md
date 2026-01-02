## 2024-05-23 - Prevent CSV Injection and Path Traversal in Scraper
**Vulnerability:** The scraper was vulnerable to CSV Injection (allowing malicious formulas to be executed if the CSV is opened in Excel) and Path Traversal (allowing files to be written outside the intended directory).
**Learning:** User-controlled data scraped from the web should never be trusted, even if it looks like "just text". Output paths must always be validated against the current working directory.
**Prevention:** Implement `sanitize_for_csv` to prepend `'` to risky characters (`=`, `+`, `-`, `@`) and `validate_output_path` using `os.path.commonpath` to enforce directory confinement.
