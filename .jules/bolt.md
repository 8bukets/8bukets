## 2025-12-25 - [Regex Parsing vs BeautifulSoup]
**Learning:** For large HTML documents where only a specific commented section is needed, using Regex to extract that section is significantly faster than parsing the full document with BeautifulSoup (observed ~3.4x speedup).
**Action:** When targeting specific fragments within comments or clearly delimited blocks, consider Regex extraction first before full DOM parsing.
