## 2024-02-14 - Prevent CSV Injection in Scraper
**Vulnerability:** Scraper data was being written to CSV files without sanitization. User-controlled input starting with `=`, `+`, `-`, or `@` could be interpreted as formulas by spreadsheet software (Excel, LibreOffice), leading to Arbitrary Command Execution (ACE) on the victim's machine.
**Learning:** Python's `csv` module does not automatically sanitize input for spreadsheet formulas. It handles CSV formatting (quotes/commas) but not "active content" injection.
**Prevention:** Always prepend a single quote `'` to fields starting with dangerous characters (`=`, `+`, `-`, `@`) when generating CSVs that might be opened in spreadsheet software.
