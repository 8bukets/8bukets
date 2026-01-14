## 2025-10-15 - CSV Formula Injection
**Vulnerability:** User-controlled input (article titles) was written directly to CSV files without sanitization. If a title started with characters like `=`, `+`, `-`, or `@`, it could execute formulas in spreadsheet software (CSV Injection).
**Learning:** Even when scraping "trusted" sites, content can be manipulated or malicious, and data formats like CSV have hidden execution capabilities.
**Prevention:** Sanitize all fields exported to CSV by prepending a single quote `'` if they start with dangerous characters.
