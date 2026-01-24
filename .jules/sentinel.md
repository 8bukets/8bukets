## 2026-01-24 - Path Traversal in File Output
**Vulnerability:** Arbitrary file write via directory traversal (`../`) in CLI output arguments (`--json`, `--csv`, etc.).
**Learning:** Python's `open()` does not validate paths against the CWD. Accepting user-supplied paths for output files allows writing outside the intended directory if not validated.
**Prevention:** Always validate output paths using `os.path.abspath` and `os.path.commonpath` to ensure they stay within the intended directory (Jail).
