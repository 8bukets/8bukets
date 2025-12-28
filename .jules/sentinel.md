## 2025-12-28 - [Path Traversal in CLI Tools]
**Vulnerability:** The scraper CLI tools allowed specifying output file paths outside the current directory (e.g., `../sensitive.file`), posing a path traversal risk if used with untrusted input or in automated pipelines.
**Learning:** Even client-side CLI tools should validate output paths to prevent accidental or malicious overwriting of system files, especially when part of a larger orchestration system.
**Prevention:** Implemented strict path validation using `pathlib.Path.is_relative_to(Path.cwd())` to ensure all output files remain within the execution directory.
