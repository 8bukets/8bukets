## 2026-01-21 - [CSV Injection in Scraper]
**Vulnerability:** `scraper.py` was saving scraped data directly to CSV without sanitization, allowing formula injection.
**Learning:** Data scraped from "trusted" domains (like a specific WordPress site) can still contain malicious payloads if the site is compromised or accepts user input.
**Prevention:** Use `security_utils.sanitize_for_csv` to escape fields starting with `=`, `+`, `-`, `@`.
