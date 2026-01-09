## 2024-01-09 - CSV Injection Vulnerability
**Vulnerability:** The scraper was exporting data directly to CSV without sanitizing fields that started with special characters (`=`, `+`, `-`, `@`), enabling CSV Injection (Formula Injection) attacks.
**Learning:** Even simple data export features like CSV generation require strict input sanitization to prevent downstream attacks in spreadsheet software.
**Prevention:** Always sanitize user-controlled input before writing to CSV files by escaping dangerous starting characters. Added `sanitize_for_csv` method to `scraper.py`.
