## 2026-02-03 - CSV Injection Vulnerability
**Vulnerability:** User-controlled input (titles, authors, etc.) was written directly to CSV files without sanitization, allowing for Formula Injection (CSV Injection) if the data contained special characters (`=`, `+`, `-`, `@`).
**Learning:** Python's `csv` module does not automatically sanitize fields against formula injection; it only handles CSV formatting (quoting, escaping delimiters).
**Prevention:** Always sanitize untrusted input before writing to CSV by prepending a single quote (`'`) to fields starting with dangerous characters (`=`, `+`, `-`, `@`).
