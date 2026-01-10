## 2026-01-10 - CSV Injection (Formula Injection)

**Vulnerability:**
The `scraper.py` tool exports scraped data (like article titles and authors) to a CSV file. If a scraped website contained a malicious title starting with characters like `=`, `+`, `-`, or `@` (e.g., `=cmd|' /C calc'!A0`), opening the resulting CSV in Excel or LibreOffice could execute arbitrary commands on the user's machine. This is known as CSV Injection or Formula Injection.

**Learning:**
Even when scraping "trusted" sites, the data is external input and must be treated as untrusted. CSVs are not just simple text files; they are interpreted by spreadsheet software which has powerful features like formula execution. Standard CSV libraries (like Python's `csv`) handle delimiters but do not prevent formula injection by default.

**Prevention:**
Implemented a sanitization layer (`sanitize_for_csv` method) in `scraper.py`. Before writing any field to the CSV, we check if it starts with a dangerous character (`=`, `+`, `-`, `@`). If it does, we prepend a single quote (`'`), forcing the spreadsheet software to treat the cell as a string literal rather than a formula. This "tab escaping" is a standard mitigation for this vulnerability.
