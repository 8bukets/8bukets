## 2024-05-23 - Path Traversal in File Output
**Vulnerability:** The scraper accepted output filenames via CLI arguments and wrote to them without validation. This allowed writing files outside the intended directory (Path Traversal), potentially overwriting sensitive files if run with sufficient permissions.
**Learning:** CLI tools that write files should validate paths if they are expected to run in restricted environments or handle untrusted input, even if the user provides the arguments.
**Prevention:** Use `os.path.realpath` and `os.path.commonpath` to ensure the output path is contained within the current working directory (or a specific allowed directory).
