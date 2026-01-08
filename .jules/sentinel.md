## Sentinel Journal

## 2026-01-08 - CSV Injection Vulnerability
**Vulnerability:** Scraped data was written directly to CSV without sanitization, allowing malicious titles to execute spreadsheet formulas.
**Learning:** Even internal data processing tools need input sanitization if the output (CSV) is consumed by vulnerable software (Excel).
**Prevention:** Always prepend a single quote to fields starting with , , , or  when exporting to CSV.

## 2025-02-18 - CSV Injection Vulnerability
**Vulnerability:** Scraped data was written directly to CSV without sanitization, allowing malicious titles to execute spreadsheet formulas.
**Learning:** Even internal data processing tools need input sanitization if the output (CSV) is consumed by vulnerable software (Excel).
**Prevention:** Always prepend a single quote to fields starting with `=`, `+`, `-`, or `@` when exporting to CSV.
