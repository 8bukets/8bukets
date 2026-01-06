## 2024-05-23 - [SSRF Risk in Scraper Pagination]
**Vulnerability:** The scraper blindly follows the "Previous" link found in the HTML of the scraped page (`nav_previous`). A compromised or malicious server could redirect the scraper to internal resources (SSRF) or malicious protocols (though `requests` is limited to http/https by default).
**Learning:** Scrapers must treat all content from the target site, including navigation links, as untrusted user input. Validating the URL scheme and domain scope is crucial.
**Prevention:** Implement strict URL validation before fetching any new URL found in the wild. Ensure the scheme is http/s and the domain matches the expected target.
