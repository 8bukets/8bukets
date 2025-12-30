## 2024-02-14 - Prevent CSV Formula Injection
**Vulnerability:** User-controlled data (like article titles or authors) being written directly to a CSV file could contain spreadsheet formulas (starting with `=`, `+`, `-`, `@`). If opened in Excel, these could execute malicious commands.
**Learning:** Python's standard `csv` module does not automatically sanitize fields for Excel formula injection. It only handles CSV formatting (quoting delimiters), not content sanitization.
**Prevention:** Explicitly sanitize any untrusted input before writing to CSV by prepending a single quote (`'`) if the content starts with dangerous characters.
