## 2024-12-28 - Path Traversal Protection
**Vulnerability:** `scraper.py` allowed writing output files to arbitrary paths (e.g., `/tmp/file`, `../file`), enabling potential overwriting of critical system files or writing to unauthorized locations.
**Learning:** Even internal CLI tools can be dangerous if arguments aren't validated, especially if they might be run with privileges or automated inputs. `os.path.basename` is a simple way to enforce "current directory only" but doesn't handle all edge cases (like `..` as a filename on some systems, though `os.path.split` handles it). Strict validation is better than sanitization.
**Prevention:** Enforce that output filenames match their `os.path.basename` and reject any path components.
