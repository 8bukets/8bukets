## 2026-01-27 - CLI Path Traversal
**Vulnerability:** `scraper.py` and `analytics.py` allowed arbitrary file paths via CLI arguments, enabling path traversal (reading/writing files outside CWD).
**Learning:** CLI tools often trust user input for file paths implicitly. `os.path.commonpath` is a robust way to validate paths against a safe root (like CWD).
**Prevention:** Always validate file paths provided by users or external sources. Use a dedicated `validate_path` function that resolves absolute paths and checks containment.
## 2026-02-06 - SSRF in RobotTxtAgent
**Vulnerability:** The `RobotTxtAgent` was vulnerable to Server-Side Request Forgery (SSRF). It dynamically determined the base URL for fetching `robots.txt` from the input data (`post_url`). If the input data contained a malicious URL (e.g., pointing to `localhost`), the agent would attempt to fetch `robots.txt` from that internal service.
**Learning:** trusting input data to construct network requests without validation is dangerous, especially when the data source is external or can be manipulated. Even in "internal" agents, defense in depth is crucial.
**Prevention:** Validate all URLs against an allowlist of trusted domains before making requests. For specific scrapers, hardcode the target domain or strictly validate that the dynamic URL belongs to the expected target.
# Sentinel's Journal

## 2025-02-20 - CSV Injection Vulnerability
**Vulnerability:** The scraper was writing untrusted data (post titles, authors, etc.) directly to a CSV file without sanitization. If the data started with characters like `=`, `+`, `-`, or `@`, it could be interpreted as a formula by spreadsheet software (Excel, Google Sheets), potentially executing arbitrary commands or exfiltrating data.
**Learning:** Even "internal" tools that generate reports can be vectors for attack if the output is consumed by vulnerable software like Excel. Data from the web is always untrusted.
**Prevention:** Always sanitize data before writing to CSV. Prepend a single quote `'` to fields starting with dangerous characters (`=`, `+`, `-`, `@`) to force them to be treated as strings.
