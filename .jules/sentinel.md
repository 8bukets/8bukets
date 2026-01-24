## 2024-05-22 - Path Traversal in Scraper Output
**Vulnerability:** `scraper.py` accepted arbitrary file paths for output files (e.g., `../evil.json`), allowing overwriting of files outside the working directory.
**Learning:** CLI tools accepting file paths must explicitly validate they are within the intended directory, as relative paths like `../` are interpreted by the OS.
**Prevention:** Use `os.path.abspath` and `os.path.commonpath` to enforce that output paths are contained within the current working directory.
