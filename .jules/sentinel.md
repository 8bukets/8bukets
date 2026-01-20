## 2024-05-22 - CSV Injection Vulnerability in Scraper
**Vulnerability:** The scraper was writing user-controlled content (titles, authors, categories) directly to a CSV file without sanitization. This allows malicious actors to inject spreadsheet formulas (starting with =, +, -, @) that execute when the CSV is opened in Excel/LibreOffice.
**Learning:** Even when scraping "trusted" sites, content can be user-generated (comments, authors) or the site could be compromised. Data destined for spreadsheets must always be sanitized against formula injection.
**Prevention:** Implemented a `sanitize_for_csv` method that prepends a single quote `'` to fields starting with risky characters. This forces the spreadsheet to treat the cell as text.
