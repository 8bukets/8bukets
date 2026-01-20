## 2026-01-20 - Pre-calculation of Loop Invariants
**Learning:** In `scrape_informatic.py`, `urlparse(base_url)` was being called inside `is_external_link`, which is invoked for every link in every post. Pre-calculating `base_netloc` once and passing it down reduced execution time of the check by ~50%.
**Action:** Identify constant values used in tight loops (especially parsing or object creation) and compute them once outside the loop.
