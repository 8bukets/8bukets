## 2025-02-18 - CSV Injection in Scraper Output
**Vulnerability:** The scraper directly wrote unsanitized user content (titles, authors, categories) into a CSV file. Malicious content starting with `=`, `+`, `-`, or `@` could execute formulas when opened in spreadsheet software.
**Learning:** Data extracted from web pages, even if seemingly harmless text like "Category", can contain payloads targeting the *viewer* of the data (in this case, an analyst using Excel).
**Prevention:** Always sanitize data before writing to CSV. Prepend a single quote `'` to fields starting with dangerous characters (`=`, `+`, `-`, `@`) to force them to be treated as strings.
