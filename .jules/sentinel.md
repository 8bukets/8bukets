## 2024-02-14 - Prevent CSV Formula Injection
**Vulnerability:** User-controlled data (e.g., titles, authors, categories) was written directly to CSV files without sanitization. If these fields started with specific characters (`=`, `+`, `-`, `@`), spreadsheet software (like Excel) could execute them as formulas (CSV Injection), leading to potential code execution on the analyst's machine.
**Learning:** CSV files are not just text files; they are interpreted by spreadsheet applications. Trusting scraped data to be safe for CSV format is a common oversight.
**Prevention:** Sanitize all fields written to CSVs by prepending a single quote (`'`) if they start with dangerous characters. This forces the spreadsheet to treat the content as a string.
