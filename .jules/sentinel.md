## 2026-01-14 - Path Traversal in Researcher Agent
**Vulnerability:** The `ResearcherAgent` accepted an `output_file` parameter from `data` and passed it directly to a subprocess command, allowing path traversal (e.g., `../../evil.json`).
**Learning:** Even internal data structures should be treated as untrusted if they define resources like file paths. The "Agent" abstraction often passes loose dictionaries (`data`) which can be polluted.
**Prevention:** Sanitized `output_file` using `os.path.basename()` to restrict file writing to the current directory (or intended directory).
