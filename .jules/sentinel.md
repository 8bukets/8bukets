## 2024-05-22 - [CSV Injection in Scraper]
**Vulnerability:** Scraper was writing unsanitized external data (titles, dates, etc.) directly to CSV, allowing Formula Injection.
**Learning:** Data scraped from the web must be treated as untrusted, especially when exporting to formats like CSV that have executable capabilities in some viewers (Excel).
**Prevention:** Sanitize fields starting with `=`, `+`, `-`, `@` by prepending `'` before writing to CSV.
