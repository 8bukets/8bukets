## 2026-02-01 - CSV Injection in Scraper Output
**Vulnerability:** The scraper was writing untrusted user input directly to a CSV file without sanitization. Malicious content starting with characters like `=`, `+`, `-`, or `@` could be executed as formulas when opened in spreadsheet software, leading to potential command execution.
**Learning:** Output formats like CSV are not just text; they can carry executable payloads when interpreted by applications like Excel. Trusting external data sources (web scraping) to be free of such payloads is unsafe.
**Prevention:** Implement a sanitization layer for all CSV outputs. Prepend a single quote `'` to any field starting with active characters (`=`, `+`, `-`, `@`) to ensure they are treated as literal strings.
