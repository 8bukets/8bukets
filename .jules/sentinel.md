## 2025-02-18 - CSV Injection in Scraper
**Vulnerability:** `scraper.py` was writing untrusted data directly to CSV without sanitization, allowing CSV injection payloads (starting with `=`, `+`, `-`, `@`) to be executed by spreadsheet software.
**Learning:** Even when using standard libraries like `csv`, application-level sanitization is required for specific attack vectors like CSV Injection (Formula Injection).
**Prevention:** Always sanitize user-controlled input before writing to CSV. Prepend a single quote `'` to fields starting with dangerous characters.
