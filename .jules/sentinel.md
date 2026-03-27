## 2024-05-23 - CSV Formula Injection
**Vulnerability:** The scraper was writing user-controlled input (post titles, links) directly to CSV files without sanitization. This allows malicious actors to inject spreadsheet formulas (starting with `=`, `+`, `-`, `@`) that could execute code on a victim's machine when opening the CSV in Excel.
**Learning:** Even internal tools or scrapers need output encoding. Trusting external content (even from a blog) is risky when generating file formats like CSV that have executable features.
**Prevention:** Always sanitize CSV fields that start with trigger characters (`=`, `+`, `-`, `@`) by prepending a single quote `'` or otherwise escaping them. A `sanitize_for_csv` helper was added to `scraper.py`.
