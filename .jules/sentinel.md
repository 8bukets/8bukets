## 2024-05-22 - CSV Injection Prevention
**Vulnerability:** User-controlled content from scraped websites could contain CSV formula injection payloads (starting with =, @, +, -) which would be executed when the CSV file is opened in Excel.
**Learning:** Even data from 'public' websites can be malicious if not properly sanitized before being consumed by other tools (like spreadsheet software).
**Prevention:** Sanitize all fields starting with dangerous characters by prepending a single quote before writing to CSV.
