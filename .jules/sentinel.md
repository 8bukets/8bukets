## 2024-02-14 - Fix CSV Injection in Scraper
**Vulnerability:** The scraper was writing user-controlled input (titles, authors, etc.) directly to a CSV file without sanitization. If the input started with characters like `=`, `+`, `-`, or `@`, it could be interpreted as a formula by spreadsheet software, leading to arbitrary code execution (CSV Injection).
**Learning:** Even internal tools or scrapers need to sanitize data if the output is intended for consumption by other software (like Excel). CSV is not just a text format; it has executable capabilities in some contexts.
**Prevention:** Always sanitize fields before writing to CSV. A common technique is to prepend a single quote `'` to fields starting with dangerous characters.
