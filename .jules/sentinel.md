## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2024-05-24 - Improper Input Validation in Scraper
**Vulnerability:** The scraper accepted any text in `href` attributes as a URL, including `javascript:`, `file:`, and malformed URLs with newlines. This could lead to XSS or File Inclusion if the output is processed by a vulnerable tool, and Line Injection in the output TXT file.
**Learning:** `BeautifulSoup` extracts attributes raw. URL validation must go beyond regex matching for the start of the string (`^http`) and should fully clean and validate the scheme and content.
**Prevention:** Implemented a strict `validate_url` method that removes all whitespace and enforces `http://` or `https://` schemes before accepting any link.
