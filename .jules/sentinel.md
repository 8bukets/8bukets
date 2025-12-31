## 2024-05-23 - Prevent Path Traversal in File Scraper
**Vulnerability:** The scraper accepted arbitrary file paths for output files (JSON, CSV, TXT), allowing a malicious user (or compromised script) to write files anywhere on the filesystem (e.g., `/tmp/hacked.json` or sensitive system directories if permissions allowed).
**Learning:** Even CLI tools running in controlled environments should validate output paths to prevent accidental or malicious overwriting of critical files outside the intended project directory. Relying on user input for file paths without validation is a common security oversight.
**Prevention:** Implemented `validate_output_path` using `os.path.abspath` and `os.path.commonpath` to ensure all output files are contained within the current working directory.
