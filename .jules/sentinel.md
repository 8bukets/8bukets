## 2024-03-25 - [CSV Injection (Formula Injection) in Scraper]
**Vulnerability:** The `scraper.py` script was directly writing untrusted data (post titles, authors, etc.) into a CSV file. If these fields started with special characters like `=`, `+`, `-`, or `@`, spreadsheet software (like Excel) would interpret them as formulas, potentially leading to arbitrary code execution on the analyst's machine.
**Learning:** Even internal data collection tools need sanitization if their output is consumed by vulnerable software like Excel. Data "sanitized" for HTML display might still be dangerous in CSV format.
**Prevention:** Always sanitize data before writing to CSV. A common mitigation is to prepend a single quote `'` to any field starting with formula triggers (`=`, `+`, `-`, `@`).
