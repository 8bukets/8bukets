# Bolt's Journal

## 2026-01-16 - Analytics Performance Optimization
**Learning:** For large datasets where only simple date extraction is needed (e.g., Year or YYYY-MM-DD), avoiding `datetime` object instantiation and using string slicing on ISO 8601 strings is significantly faster and more memory efficient. Also, prefer generators and `itertools.chain` over building large intermediate lists for aggregation tasks.
**Action:** When optimizing aggregation scripts, check if full object parsing is necessary or if lightweight string operations suffice. Use generators for `Counter` inputs.
