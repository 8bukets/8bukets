## 2026-02-02 - Path Traversal in Scraper Output
**Vulnerability:** `scrape_informatic.py` allowed Arbitrary File Write via the `-o` argument, permitting path traversal to overwrite sensitive files outside the project directory.
**Learning:** Standalone scripts often lack the security validation present in web frameworks. Command-line arguments used for file paths must be validated just like web inputs to prevent them from being used as attack vectors.
**Prevention:** Always validate user-provided file paths using `os.path.abspath` and `os.path.commonpath` to ensure they stay within intended directories (Sandboxing).
