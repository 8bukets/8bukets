## 2026-01-24 - Path Traversal in CLI Arguments
**Vulnerability:** The `scraper.py` script accepted user-provided paths for output files without validation, allowing writing files outside the intended directory (Path Traversal).
**Learning:** Python `argparse` arguments passed directly to file operations are a common attack vector in CLI tools, as they lack the implicit sanitization often found in web frameworks.
**Prevention:** Implement a `_validate_path` method using `os.path.commonpath` to enforce that all output paths resolve to a location within the current working directory (CWD) before opening files.
