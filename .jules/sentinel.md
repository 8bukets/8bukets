## 2026-02-03 - CLI Output Path Vulnerability
**Vulnerability:** Scraper scripts accepted arbitrary output paths, allowing overwriting of source code or critical files via Path Traversal.
**Learning:** Automation tools intended for agents often lack basic I/O validation, assuming benign usage, which is dangerous in autonomous loops.
**Prevention:** Enforce strict output directories (e.g., `os.getcwd()`) and file extensions for all file-writing CLI tools.
