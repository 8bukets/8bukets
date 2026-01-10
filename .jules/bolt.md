## 2024-05-22 - [Optimizing BeautifulSoup in AsyncIO]
**Learning:** Even if a function is defined as `async`, `BeautifulSoup` parsing is synchronous and CPU-bound, blocking the event loop. In high-concurrency scraping, this serialization becomes a major bottleneck.
**Action:** Always offload `BeautifulSoup` parsing to `loop.run_in_executor`. Additionally, `SoupStrainer` significantly reduces parsing time by ignoring irrelevant parts of the DOM, especially effective when `lxml` is used as the parser.
