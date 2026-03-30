## 2025-10-26 - [BeautifulSoup Overhead for Simple Extraction]
**Learning:** Initializing `BeautifulSoup(html, 'html.parser')` parses the entire DOM tree, which is O(N) and expensive for large documents (e.g., 0.35s for 500KB).
**Action:** When extracting a specific substring (like a comment or JSON blob) from a large HTML file, use Regex (`re.finditer` with `re.DOTALL`) instead of full DOM parsing. Benchmarks showed a ~300x speedup (0.001s vs 0.35s).
