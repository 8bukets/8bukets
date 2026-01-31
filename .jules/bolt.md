## 2026-01-31 - Redundant URL Parsing in Loops
**Learning:** `urlparse` is relatively fast (~4µs) but when called inside nested loops (pages * posts * links), the cost accumulates. Pre-calculating constant components (like `netloc` of the base URL) prevents thousands of redundant calls.
**Action:** Identify loop invariants involving string parsing or regex and hoist them out of the hot path.
