## 2025-02-18 - SSRF Prevention in Scraper
**Vulnerability:** The scraper blindly followed URLs found in "older posts" links, which could lead to SSRF or Open Redirect if the target site is compromised or contains malicious links (e.g., to internal metadata services).
**Learning:** Always validate URLs extracted from external content before making HTTP requests.
**Prevention:** Implemented strict URL validation ensuring scheme is http/s and domain matches the intended target.
