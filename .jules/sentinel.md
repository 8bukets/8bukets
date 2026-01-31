## 2024-05-23 - CSV Injection Vulnerability in Scraper
**Vulnerability:** The scraper was exporting data directly to CSV without sanitizing fields that started with special characters (`=`, `+`, `-`, `@`). This allowed malicious content (Formula Injection) to potentially execute commands if the CSV was opened in a spreadsheet application.
**Learning:** Data extracted from external sources (even parsed HTML) must be treated as untrusted. When exporting to CSV, specific characters can trigger formula execution, regardless of the data's origin.
**Prevention:** Implement a sanitization layer for all CSV exports that detects fields starting with dangerous characters and neutralizes them (typically by prepending a single quote `'`).
