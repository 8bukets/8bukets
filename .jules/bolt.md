## 2024-01-04 - [Python/BeautifulSoup Performance]
**Learning:** `BeautifulSoup`'s `select_one` (CSS selector) is significantly slower (approx 33%) than using native `find` methods, especially when called repeatedly in a loop. Also, pre-compiling regex in Python gives a noticeable speedup (~25%) for frequently called text cleaning functions.
**Action:** Prefer `find`/`find_all` over `select`/`select_one` in tight loops for BeautifulSoup. Always pre-compile regexes used in hot paths.
