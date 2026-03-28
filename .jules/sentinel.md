## 2024-05-23 - CSV Injection in Scraper
**Vulnerability:** `scraper.py` exported unsanitized user inputs directly to CSV, allowing for Formula Injection (CSV Injection).
**Learning:** Data export tools must treat all external input as potentially malicious. The absence of a sanitization layer in `scraper.py` was a critical gap.
**Prevention:** Implemented `sanitize_for_csv` to prepend a single quote `'` to values starting with `=`, `+`, `-`, or `@`.
