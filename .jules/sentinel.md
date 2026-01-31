# Sentinel Journal

## 2026-01-31 - CSV Formula Injection
**Vulnerability:** User-controlled input (titles, authors, etc.) starting with `=`, `+`, `-`, or `@` was written directly to CSV files, allowing for Formula Injection (CSV Injection) if opened in spreadsheet software.
**Learning:** Text-based data formats like CSV are not purely passive; spreadsheet software often interprets specific characters as executable formulas, creating a bridge from data to code execution.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending a single quote `'` to any field starting with formula triggers (`=`, `+`, `-`, `@`).
