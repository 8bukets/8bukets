<<<<<<< sentinel/fix-csv-injection-2739836513252277633
## 2025-02-18 - CSV Injection in Scraper Output
**Vulnerability:** The scraper directly wrote unsanitized user content (titles, authors, categories) into a CSV file. Malicious content starting with `=`, `+`, `-`, or `@` could execute formulas when opened in spreadsheet software.
**Learning:** Data extracted from web pages, even if seemingly harmless text like "Category", can contain payloads targeting the *viewer* of the data (in this case, an analyst using Excel).
**Prevention:** Always sanitize data before writing to CSV. Prepend a single quote `'` to fields starting with dangerous characters (`=`, `+`, `-`, `@`) to force them to be treated as strings.
=======
## 2024-05-22 - [CLI Path Traversal]
**Vulnerability:** `scraper.py` and `analytics.py` allowed writing output files to arbitrary paths via CLI arguments (e.g., `../evil.json`).
**Learning:** Even local CLI tools can be vectors for path traversal if they accept file paths as arguments without validation, especially if wrapped by other systems.
**Prevention:** Implemented `validate_output_path` in `utils.py` to enforce that output paths are within the current working directory using `os.path.abspath` and `os.path.commonpath`.
>>>>>>> jules/scraper-markposition-17752547678215960211
