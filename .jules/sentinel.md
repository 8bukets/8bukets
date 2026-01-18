## 2025-02-18 - CSV Injection (Formula Injection)
**Vulnerability:** `scraper.py` wrote unsanitized user input (titles, authors) directly to CSV cells. If these started with `=`, `+`, `-`, `@`, they would be interpreted as formulas in Excel, leading to potential RCE or data exfiltration.
**Learning:** Even in backend scripts, data destined for end-user applications (like Excel) must be treated as untrusted.
**Prevention:** Use a `sanitize_for_csv` helper to escape dangerous characters by prepending a single quote `'`.
