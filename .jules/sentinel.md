## 2026-01-27 - Path Traversal in CLI Output Arguments
**Vulnerability:** CLI tools (`scraper.py`) accepted output file paths directly from arguments without validation, allowing arbitrary file writes via path traversal (e.g., `../file.json`).
**Learning:** Python's `open()` does not sandbox file access; CLI tools accepting paths must explicitly validate them against a root directory.
**Prevention:** Use `os.path.abspath` and `os.path.commonpath` to enforce that resolved paths remain within the intended working directory.
