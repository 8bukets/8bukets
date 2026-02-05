## 2026-02-05 - CSV Injection in Scraper
**Vulnerability:** Unsanitized scraped data (titles, dates, etc.) being written directly to CSV files allowed for Formula Injection (CSV Injection). Strings starting with =, +, -, or @ could execute formulas in spreadsheet software.
**Learning:** Data from external sources, even public websites, must be treated as untrusted. When exporting to CSV, special characters at the beginning of fields can trigger formula execution in spreadsheet applications, posing a security risk to the user.
**Prevention:** Sanitize all fields before writing to CSV by prepending a single quote (') to any string starting with =, +, -, or @. This ensures the spreadsheet software interprets the value as literal text.
