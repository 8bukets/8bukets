## 2026-02-05 - URL Parsing in Scrapers
**Learning:** Repeatedly calling `urlparse()` inside tight loops (like checking external links for every scraped element) adds significant overhead. Pre-parsing constant base URLs can improve performance by ~50% in link-heavy checks.
**Action:** Pass pre-parsed `ParseResult` objects to helper functions instead of raw URL strings when the URL is constant or reused.
