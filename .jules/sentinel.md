## 2026-01-25 - Path Traversal in CLI Arguments
**Vulnerability:** The `scraper.py` script accepted file paths for output (`--json`, `--csv`, `--txt`) directly from command-line arguments and passed them to `open()` without validation. This allowed writing files to arbitrary locations (Path Traversal / Arbitrary File Write).
**Learning:** Even CLI tools used internally or via automation can be vulnerable to path traversal if they process user-controlled input (arguments) that determine file operations.
**Prevention:** Always validate file paths against a whitelist of allowed directories (e.g., using `os.path.abspath` and `os.path.commonpath`) before performing file I/O.
