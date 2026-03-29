## 2024-05-22 - Regex Compilation Performance
**Learning:** Pre-compiling regex patterns (even simple ones like `\s+` and `^https?://`) resulted in ~14% speedup for `clean_text` and ~53% speedup for `is_url` checks in this environment.
**Action:** Always pre-compile regex patterns that are used in tight loops or frequently called helper methods.
