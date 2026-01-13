## 2024-03-25 - [Missing Dependency Verification in Patches]
**Vulnerability:** A security patch for `scraper.py` introduced `urlparse` usage without explicit verification of imports, potentially crashing the application (DoS risk).
**Learning:** Even when a module seems to import a library (e.g., `urljoin`), one must verify that the specific function being used (`urlparse`) is also imported or available in the scope.
**Prevention:** Always grep or read the import section of the file before using a standard library function, and run a test that specifically exercises the new code path to catch `NameError` or `ImportError` immediately.
