# Sentinel Journal

## 2025-02-19 - Initial Setup
**Vulnerability:** Missing security documentation.
**Learning:** Security context was not persisted.
**Prevention:** Created journal to track learnings.

## 2025-02-19 - CSV Injection in Scraper
**Vulnerability:** `scraper.py` wrote untrusted input (title, author, categories) directly to CSV files without sanitization. If these fields started with `=`, `+`, `-`, or `@`, they could be executed as formulas in spreadsheet software.
**Learning:** Always assume external data is malicious, even from "trusted" sites like WordPress blogs. CSVs are not just text files; they are executable in the context of spreadsheet applications.
**Prevention:** Implemented `sanitize_for_csv` helper function to prepend a single quote `'` to any field starting with dangerous characters. This forces the spreadsheet to treat the content as a string.
