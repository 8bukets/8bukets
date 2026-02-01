## 2026-02-01 - Prioritizing Pre-Parsed Fields in Analytics
**Learning:** The `links.json` dataset contains both raw (`external_link`) and processed (`domain`) data. Re-processing raw data (e.g., `urlparse`) in downstream analytics is redundant and inefficient, especially for large datasets.
**Action:** Always verify if a pre-processed field exists in the data schema before performing expensive parsing operations on raw inputs.
