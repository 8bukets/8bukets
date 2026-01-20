## 2025-02-19 - Regex Compilation Pattern
**Learning:** `clean_text` is a hot path called for multiple fields per scraped item. Pre-compiling `re.sub` patterns yields ~14-16% performance improvement in this specific function.
**Action:** Always pre-compile regex patterns used in data cleaning methods that run in loops.
