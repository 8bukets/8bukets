## 2024-02-14 - Fix CSV Formula Injection
**Vulnerability:** The scraper was writing untrusted input (scraped content) directly to a CSV file. If the content started with special characters like `=`, `+`, `-`, or `@`, it could be interpreted as a formula by spreadsheet software (like Excel), potentially executing arbitrary code.
**Learning:** Even when scraping "trusted" sites, the content should be treated as untrusted. CSVs are not just text files; they are executable by some readers.
**Prevention:** Sanitized all fields written to CSV by prepending a single quote `'` if they start with dangerous characters. This forces the spreadsheet to treat the cell as text.
