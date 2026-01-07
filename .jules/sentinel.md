## 2025-02-18 - CSV Injection in Scraper Output
**Vulnerability:** The scraper was writing user-controlled data (scraped from an external website) directly into a CSV file without sanitization. Fields starting with characters like `=`, `+`, `-`, or `@` could be interpreted as formulas by spreadsheet software (e.g., Excel), leading to potential arbitrary command execution (CSV Injection).
**Learning:** Even data scraped from "trusted" sites should be treated as untrusted when exporting to formats like CSV that have executable capabilities. Output encoding/sanitization is context-dependent (HTML vs CSV vs SQL).
**Prevention:** Always sanitize data before writing to CSV. Prepend a single quote `'` to fields starting with dangerous characters to force them to be treated as text strings.
