## 2024-05-22 - [CSV Injection in Scraper]
**Vulnerability:** User-controlled content (titles, authors) scraped from the web was written directly to CSV, allowing for Formula Injection (CSV Injection).
**Learning:** Even "read-only" scrapers can introduce vulnerabilities if the output format (CSV) is consumed by vulnerable applications (Excel).
**Prevention:** Sanitize all fields starting with `=`, `+`, `-`, `@` by prepending `'` when writing to CSV.
