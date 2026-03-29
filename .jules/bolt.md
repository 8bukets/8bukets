## 2025-02-23 - Missing lxml parser
**Learning:** The project specifies `lxml` in `requirements.txt` and uses it in `scraper.py`, but it is not installed/working in the environment. `BeautifulSoup(html, 'lxml')` fails.
**Action:** Replace `lxml` with `html.parser` in `BeautifulSoup` calls, or install `lxml` if performance is critical and environment allows (but memory suggests `lxml` is not installed). I will switch to `html.parser` and apply `SoupStrainer` for performance.
