## 2024-05-23 - [Frontend Search Performance]
**Learning:** The application performs synchronous DOM querying and text extraction on every `input` event in the search field. This is O(N) where N is the number of articles, and it triggers layout thrashing.
**Action:** Implement a standard debounce pattern (300ms) and cache the article text content on page load. This reduces the search complexity to O(N) on memory (fast) instead of DOM (slow) and reduces the frequency of execution drastically.
