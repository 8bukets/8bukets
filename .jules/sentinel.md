## 2025-12-26 - Path Traversal in Researcher Agent
**Vulnerability:** The `ResearcherAgent` accepted an `output_file` parameter from user input and passed it directly to a subprocess (`scrape_informatic.py`). This allowed an attacker to overwrite arbitrary files on the system (e.g., `../../etc/passwd`) via path traversal.
**Learning:** Even internal agents can be vectors for attack if their inputs can be controlled by a user or an untrusted source. Subprocesses that perform file I/O are particularly sensitive.
**Prevention:** Always sanitize file paths from untrusted sources. Use `os.path.basename()` to restrict files to a single directory, or resolve the path with `os.path.abspath()` and verify it starts with the intended directory prefix.
