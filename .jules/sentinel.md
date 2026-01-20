## 2024-05-23 - CSV Injection in Scraper Outputs
**Vulnerability:** User-controlled content (titles, authors) starting with `=`, `@`, `+`, or `-` can trigger formula execution in Excel when exported to CSV.
**Learning:** Scraped data is untrusted input. Even if it comes from a public blog, it can contain malicious formatting.
**Prevention:** Sanitize all fields written to CSV by prepending `'` to sensitive leading characters.
