## 2026-01-23 - Prevent Path Traversal in CLI Tools
**Vulnerability:** CLI tools accepting output file paths without validation allow writing to arbitrary locations (Path Traversal).
**Learning:** Python's `open()` does not validate paths. Scripts intended for automation can be misused if they accept file paths as arguments.
**Prevention:** Use `os.path.abspath` and `os.path.commonpath` to enforce that output files are within the intended directory (e.g., CWD).
