## 2024-05-22 - [Regex Compilation in Hot Paths]
**Learning:** Re-compiling regex patterns inside frequently called methods (like `clean_text` called for every field of every article) creates significant overhead.
**Action:** Pre-compile regex patterns as class attributes. In `scraper.py`, pre-compiling `\s+` and removing redundant string replacement improved performance by ~3x (from ~1.27s to ~0.41s for 100k iterations).
