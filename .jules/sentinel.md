## 2026-01-20 - Implicit Trust in Agent Outputs
**Vulnerability:** The orchestration system wrote agent-generated content directly to Markdown reports without sanitization. This allowed potential Stored XSS and Markdown Injection if an agent ingested and propagated malicious content from the web (e.g., a blog post title containing `<script>`).
**Learning:** Autonomous agents act as proxies for external data. Even if they "process" data, they may preserve malicious payloads. Trusting agent output is equivalent to trusting the raw external data they consumed.
**Prevention:** Treat all agent outputs as untrusted input. Apply strict sanitization (e.g., `html.escape`) at the "sink" where data is persisted or displayed, regardless of which agent produced it.
