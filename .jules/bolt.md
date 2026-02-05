## 2024-05-22 - [Repeated Database Connection Anti-Pattern]
**Learning:** Establishing a new database connection for every single record insertion in a loop is a significant performance bottleneck due to connection overhead.
**Action:** Use a persistent connection for the lifetime of the scraper/worker, and manage transactions appropriately within that connection.
