## 2026-02-06 - Redundant URL Parsing
**Learning:** The analytics pipeline was performing redundant `urlparse` operations on every record to extract domains, ignoring the existing `domain` field provided by the scraper. This highlighted the importance of verifying input data schema before implementing extraction logic.
**Action:** When optimizing data processing scripts, first inspect the full schema of the input data to identify pre-calculated fields that can replace runtime computations.
