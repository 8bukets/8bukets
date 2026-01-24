## 2024-05-23 - Path Traversal in CLI Output Arguments
**Vulnerability:** The scraper accepted output file paths via command line arguments without validation, allowing users to write files to arbitrary locations on the file system (Path Traversal).
**Learning:** Even CLI tools can be vulnerable to path traversal if they are used in automated pipelines or shared environments. `os.path.commonpath` can raise `ValueError` on Windows if paths are on different drives, which must be handled securely (fail closed, not open).
**Prevention:** Always validate user-supplied file paths using `os.path.realpath` and `os.path.commonpath`. Explicitly catch `ValueError` from `commonpath` and treat it as a security violation (different drives cannot be nested).
