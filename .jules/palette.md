## 2026-01-28 - Markdown Report Navigation
**Learning:** For CLI tools that generate static reports (like Markdown), treating the report as a "user interface" is crucial. Users often navigate these reports like web pages. Adding explicit HTML anchors `<a name='...'></a>` is more reliable than implicit slug generation for internal linking, especially when headers contain emojis, which can break standard slugifiers.
**Action:** When improving generated reports, always implement a Table of Contents, use explicit HTML anchors for sections, and include "Back to Top" links to improve navigability.
