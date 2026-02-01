## 2024-05-23 - [Initial Setup]
**Vulnerability:** N/A
**Learning:** Initial setup of sentinel journal.
**Prevention:** N/A

## 2024-05-23 - [CSV Injection in Scraper]
**Vulnerability:** User-controlled data (scraped titles/authors) was written directly to CSV files without sanitization, allowing for potential formula injection if opened in Excel.
**Learning:** When exporting data to CSV, simply escaping delimiters is not enough; fields starting with =, +, -, or @ must be treated as potential formulas.
**Prevention:** Implemented a sanitize_csv_field method that prepends a single quote to risky fields.
