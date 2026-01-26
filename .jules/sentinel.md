## 2026-01-26 - Path Traversal in File Scraper
**Vulnerability:** The `scrape_informatic.py` script accepted an arbitrary file path for its output, allowing attackers to overwrite files outside the working directory (Path Traversal).
**Learning:** Scripts intended for CLI use are often overlooked for input validation, assuming user trust. However, when these scripts are orchestrated by agents (like `ResearcherAgent`), they become attack vectors if inputs are ever derived from untrusted sources.
**Prevention:** Always validate file paths using `os.path.abspath` and `os.path.commonpath` to ensure they remain within the intended directory sandbox.
