## 2026-02-01 - CSV Injection Vulnerability
**Vulnerability:** The scraper was writing scraped data (titles, authors, etc.) directly to CSV files without sanitization. If these fields started with `=`, `+`, `-`, or `@`, they could be executed as formulas in spreadsheet software (CSV Injection).
**Learning:** Even when scraping "trusted" sites, content can be manipulated or formatted in ways that exploit local tools (like Excel) when exported.
**Prevention:** Implemented a sanitization layer (`sanitize_for_csv`) that prepends a single quote `'` to any field starting with risky characters before writing to CSV.
