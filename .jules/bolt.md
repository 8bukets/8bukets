## 2025-02-04 - DOM Traversal Bottleneck in Search
**Learning:** The synchronous DOM traversal (`getElementsByTagName` + `forEach`) in the search input event listener was blocking the main thread on every keystroke, causing potential UI jank.
**Action:** Applied debouncing (300ms) to the search input handler. Future UI interactions involving list filtering should always be debounced or throttled.
