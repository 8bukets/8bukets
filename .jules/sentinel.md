## 2025-05-23 - CSV Formula Injection in Scraper Data

**Vulnerability:** The `OracleNewsScraper` extracted data from web pages (titles, authors, categories) and wrote it directly to a CSV file without sanitization. If an attacker could inject a string starting with `=`, `+`, `-`, or `@` into the scraped content (e.g., via a comment section or by compromising the target site), opening the generated CSV in Excel could execute arbitrary formulas/commands on the analyst's machine.

**Learning:** Data extracted from "trusted" websites should still be treated as untrusted when converting to formats like CSV that have specific injection risks. Even simple text fields can be vectors for client-side attacks against the data consumer.

**Prevention:** Implemented a `sanitize_for_csv` method that prepends a single quote `'` to any field value starting with the dangerous characters (`=`, `+`, `-`, `@`). This forces Excel to treat the cell content as a string rather than a formula.
