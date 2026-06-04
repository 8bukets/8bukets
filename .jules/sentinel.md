## 2026-01-27 - Path Traversal in Scraper Output
**Vulnerability:** `scraper.py` accepted paths outside the working directory (e.g. `../file.json`) for output arguments, allowing arbitrary file overwrite.
**Learning:** CLI tools taking file paths as arguments often overlook validation, assuming benign user intent.
**Prevention:** Enforce output paths to be within the current working directory using `os.path.abspath` and `os.path.commonpath`.
## 2025-02-18 - [CSV Injection Vulnerability in Scraper]
**Vulnerability:** The scraper writes user-controlled data (e.g., post titles) directly to a CSV file without sanitization. If a title begins with specific characters (`=`, `+`, `-`, `@`), spreadsheet software like Excel may interpret it as a formula, potentially leading to code execution (CSV Injection).
**Learning:** Even when scraping "trusted" sites, content can be manipulated or contain malicious data. Data destined for spreadsheet formats must always be treated as untrusted and sanitized to prevent formula injection.
**Prevention:** Sanitize all fields before writing to CSV. Prepend a single quote `'` to any field starting with dangerous characters (`=`, `+`, `-`, `@`) to force the spreadsheet to treat it as text.
