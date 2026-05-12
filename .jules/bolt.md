## 2025-10-27 - [Initial Performance Assessment]
**Learning:** `analytics.py` re-parses URLs for domain extraction despite `scraper.py` already providing a pre-computed `domain` field in `links.json`.
**Action:** Always check if upstream data sources (like scrapers or APIs) already provide processed fields before computing them again in downstream consumers.
