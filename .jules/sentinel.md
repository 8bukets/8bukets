## 2024-05-23 - [CSV Formula Injection in Scraper]
**Vulnerability:** The scraper was directly writing untrusted data (titles, authors, etc.) into CSV files. If a value started with `=`, `+`, `-`, or `@`, opening the CSV in Excel/Calc could execute it as a formula, leading to arbitrary code execution or data exfiltration on the analyst's machine.
**Learning:** Even internal data processing tools need strict input sanitization if the output is consumed by rich clients like Excel. "Trusted" websites can still contain malicious content in user-generated fields (comments, profile names).
**Prevention:** Implemented a `sanitize_for_csv` method that prepends `'` to any field starting with formula triggers. Applied this to all fields written to CSV.
