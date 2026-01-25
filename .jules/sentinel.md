## 2025-01-25 - Path Traversal in CLI Tools
**Vulnerability:** The `scraper.py` CLI tool accepted arbitrary output file paths, allowing file writes outside the working directory (Path Traversal) via arguments like `--txt ../file.txt`.
**Learning:** Even internal CLI tools need input validation if they deal with file paths, as they might be wrapped by other systems or run in shared environments. `os.path.commonpath` is a robust way to check directory containment.
**Prevention:** Always resolve paths to absolute values using `os.path.realpath` and verify they start with the expected root directory using `os.path.commonpath`.
