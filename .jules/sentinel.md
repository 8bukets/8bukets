## 2024-05-23 - CSV Injection Vulnerability
**Vulnerability:** User-controlled input (titles, authors, categories) was being written directly to a CSV file without sanitization. This could allow malicious formulas to be executed if the CSV file is opened in a spreadsheet application like Excel.
**Learning:** Even when scraping data, one must treat the content as untrusted. CSVs are not just simple text files when opened in spreadsheet software; they interpret formulas.
**Prevention:** Implemented a `sanitize_for_csv` method that prepends a single quote (`'`) to any field starting with `=`, `+`, `-`, or `@`. This forces the spreadsheet software to treat the cell as text.
