## 2026-02-02 - CSV Injection in Scraper Output
**Vulnerability:** `scraper.py` wrote unsanitized user content (titles, authors, etc.) directly to CSV. Malicious content starting with `=`, `+`, `-`, or `@` could trigger formula execution in spreadsheet software.
**Learning:** Even "read-only" scrapers can introduce vulnerabilities if they output to formats like CSV that have executable features. Data from the web should always be treated as untrusted.
**Prevention:** Always sanitize data before writing to CSV. Prepend a single quote `'` to fields starting with trigger characters.
