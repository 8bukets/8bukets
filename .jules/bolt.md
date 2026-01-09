## 2024-05-23 - [Frontend Search Debounce]
**Learning:** The search input listener fired on every keystroke (`input` event), causing immediate and redundant DOM traversals (`article.textContent`) and style updates. In a list of articles, this O(N) operation per character can lead to layout thrashing and poor responsiveness on lower-end devices.
**Action:** Implement a standard `debounce` utility to limit the execution frequency of the search handler. This groups rapid keystrokes into a single execution, significantly reducing main thread work.
