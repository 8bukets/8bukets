## 2026-02-03 - Avoid Full DOM Parsing for Simple Extraction
**Learning:** Parsing an entire HTML document with BeautifulSoup just to extract a single comment or script tag is extremely inefficient (O(N) for DOM construction). Using Regex to find the target string first can speed up the process by orders of magnitude (observed ~390x speedup).
**Action:** When targeting specific embedded data (JSON blobs, comments), always try to extract the substring via Regex or string search before passing it to a parser.
