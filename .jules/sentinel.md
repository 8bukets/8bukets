## 2024-03-24 - [CSV Injection Vulnerability]
**Vulnerability:** Scraped data was being written directly to CSV without sanitization. This allows malicious actors to inject spreadsheet formulas (starting with =, +, -, @) which could execute arbitrary code when opened in Excel/LibreOffice.
**Learning:** Even data from "trusted" sources should be sanitized before writing to formats like CSV that support active content. "Scraper" outputs are particularly risky as they process external data.
**Prevention:** Implemented `sanitize_for_csv` to prepend a single quote `'` to any field starting with risky characters, neutralizing the formula.
