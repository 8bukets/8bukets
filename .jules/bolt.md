## 2024-05-22 - Pre-compiled Regex Overhead
**Learning:** In `scraper.py`, `re.sub` and `re.match` were called for every scraped item. Moving these to class-level pre-compiled patterns (`re.compile`) and removing redundant string `replace` calls (since regex `\s` handles `\xa0`) improved `clean_text` performance by ~26% and `is_url` by ~50%.
**Action:** When auditing scrapers or tight loops, look for repeated `re` module calls and redundant string normalization steps that regex can handle.
