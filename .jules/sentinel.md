## 2024-05-23 - Markdown Injection in Report Generation
**Vulnerability:** The `MonetizationAgent` included raw blog post titles in the generated Markdown report. Scraped titles containing Markdown syntax (e.g., links, images) were rendered, creating a risk of phishing or XSS in vulnerable viewers.
**Learning:** External inputs must be sanitized before inclusion in rich text formats like Markdown. Trusting scraped content to be plain text is risky.
**Prevention:** Use context-aware escaping functions (e.g., `sanitize_markdown`) when embedding untrusted data into structured documents. Treat all external data as potentially malicious.
