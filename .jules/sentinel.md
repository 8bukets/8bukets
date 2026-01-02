## 2025-05-23 - [Path Traversal in Output Filenames]
**Vulnerability:** The scraper allowed arbitrary file overwrite via user-controlled command-line arguments (output filenames) without validation.
**Learning:** Argument parser inputs are untrusted and must be validated, especially when used in file operations like open().
**Prevention:** Always resolve paths using os.path.abspath and verify they are contained within the intended directory using os.path.commonpath.
