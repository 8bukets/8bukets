## 2025-02-18 - CSV Injection in Scraper
**Vulnerability:** User-controlled data (e.g., post titles, authors) was written directly to CSV files without sanitization. If a field started with =, +, -, or @, it could be interpreted as a malicious formula by spreadsheet software (CSV Injection / Formula Injection).
**Learning:** Even when scraping "trusted" sites, the content (titles, author names) can be manipulated or contain characters that trigger client-side vulnerabilities in the tools used to view the data. Trust nothing.
**Prevention:** Sanitize all fields written to CSV by prepending a single quote (') if they start with potentially dangerous characters (=, +, -, @).
