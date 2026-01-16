## 2025-05-22 - CSV Injection Pattern
**Vulnerability:** User-controlled data (titles, authors) was written directly to CSV without sanitization, allowing formula injection (e.g., `=1+1`).
**Learning:** Even internal scrapers dealing with "trusted" sites like Oracle should sanitize output, as the source content could be manipulated or accidentally contain control characters.
**Prevention:** Always use a sanitization helper (prepend `'` to `=+-@`) when writing to CSVs, regardless of the data source.
