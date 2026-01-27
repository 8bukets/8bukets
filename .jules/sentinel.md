## 2025-02-18 - Path Traversal in Scraper Output
**Vulnerability:** The `scraper.py` script accepted file paths for output (`--json`, `--csv`, `--txt`) without validation, allowing a user to write files to arbitrary locations on the filesystem (Path Traversal).
**Learning:** Command-line tools that accept file paths are often overlooked for security compared to web apps, but they can be just as dangerous if used in automated pipelines or setuid contexts. Standard libraries like `argparse` do not sanitize paths by default.
**Prevention:** Always validate user-provided file paths using a strict allow-list or by ensuring they resolve within a specific safe directory using `os.path.abspath` and `os.path.commonpath`.
