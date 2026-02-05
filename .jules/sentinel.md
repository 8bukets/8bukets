# Sentinel Journal

## 2025-02-18 - [Path Traversal in Output Filenames]
**Vulnerability:** The scraper accepted user-controlled output filenames without validation, allowing path traversal (`../../sensitive_file`) and arbitrary file overwrites.
**Learning:** Even CLI tools need strict input validation for file paths if they accept arguments that determine where to write data.
**Prevention:** Implemented `validate_output_path` using `os.path.abspath` and `os.path.commonpath` to ensure all output files are contained within the current working directory.
