
## 2026-02-01 - [Accessible CLI Reports]
**Learning:** ASCII visual bars in Markdown tables create significant noise for screen readers. Standard Markdown has no accessibility attributes.
**Action:** Wrap decorative ASCII elements in <span aria-hidden="true">...</span> tags to hide them from assistive technology while maintaining visual utility.
