## 2024-05-22 - CSV Injection in Scraper
**Vulnerability:** User input scraped from websites was written directly to CSV files, allowing formula injection if the content started with `=`, `+`, `-`, or `@`.
**Learning:** `csv.writer` does not sanitize against formula injection; raw input must be manually sanitized.
**Prevention:** Always use a helper function like `sanitize_for_csv` to prepend a single quote `'` to risky strings, ensuring they are treated as text by spreadsheet software.
