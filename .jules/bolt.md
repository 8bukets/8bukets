## 2025-02-18 - Regex Compilation in Loops
**Learning:** In `OracleNewsScraper`, regexes for text cleaning and date extraction were being compiled repeatedly inside tight loops (`clean_text` called per article, date regex per link).
**Action:** Pre-compiled regexes as class attributes (`WHITESPACE_PATTERN`, `DATE_PATTERN`) to avoid recompilation overhead.
