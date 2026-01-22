## 2025-02-14 - CSV Injection in Data Scrapers
**Vulnerability:** Unsanitized user input (titles, authors) starting with `=`, `+`, `-`, `@` was written directly to CSV files, enabling Formula Injection attacks.
**Learning:** Scrapers acting as data bridges between untrusted web content and local analyst tools (Excel) are high-risk vectors for client-side attacks.
**Prevention:** Always sanitize CSV output by prepending `'` to fields starting with trigger characters, even if the data source seems "benign" (like a blog title).
