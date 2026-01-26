## 2024-05-22 - SoupStrainer vs Markdownify
**Learning:** `SoupStrainer` improves parsing time by ~17% by filtering extraneous tags (`article` and `nav` only). However, `markdownify` conversion remains a significant bottleneck in `scrape_informatic.py`, consuming ~18% of execution time.
**Action:** When optimizing scrapers using `markdownify`, consider that parsing optimizations have diminished returns unless `markdownify` itself is optimized or avoided.
