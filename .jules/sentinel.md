## 2025-05-25 - [CSV Injection Vulnerability]
**Vulnerability:** Untrusted user input from scraped websites was being written directly to CSV files without sanitization. If the input started with characters like `=`, `+`, `-`, or `@`, it could be interpreted as a formula by spreadsheet software, leading to arbitrary code execution on the analyst's machine.
**Learning:** Even in data processing or scraping tools that don't host a web server, "Client-Side Injection" (like CSV injection) is a critical risk if the output is consumed by humans using rich tools like Excel.
**Prevention:** Always sanitize data written to CSVs by prepending a single quote `'` to fields starting with dangerous characters (`=`, `+`, `-`, `@`).
