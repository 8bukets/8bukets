## 2024-01-07 - CSV Injection & SSRF Prevention
**Vulnerability:** The scraper accepted any URL scheme (potentially allowing `file://` access) and saved unsanitized input to the database, which could lead to CSV Formula Injection if the data were later exported to Excel.
**Learning:** Even if a tool doesn't export to CSV directly, it's safer to sanitize data at the point of ingestion if the data is likely to be used in analyst reports or spreadsheets later. Always validate URL schemes for external requests.
**Prevention:** Added `sanitize_for_csv` to prefix dangerous characters (`=`, `+`, `-`, `@`) with a single quote. Added a check in `fetch_page` to ensure the URL starts with `http://` or `https://`.
