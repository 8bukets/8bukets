## 2025-01-26 - SoupStrainer with html.parser
**Learning:** SoupStrainer does not improve parsing performance significantly when used with 'html.parser' because the parser still tokenizes the entire document. It may save memory but can be CPU neutral or even slower due to overhead. Measurable gains require 'lxml'.
**Action:** Only use SoupStrainer for performance if 'lxml' is available. Otherwise, consider regex splitting for massive documents if strict correctness is not required.
