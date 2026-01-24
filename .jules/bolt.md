## 2024-05-23 - Database Connection Churn in Scraper
**Learning:** `BlogScraper.save_to_db` was opening and closing a SQLite connection for every single scraped item. While SQLite is lightweight, doing this inside a loop creates unnecessary file system overhead and locking operations.
**Action:** When working with scrapers or bulk data processors, always ensure database connections are reused across the batch operation (persistent connection) rather than established per-record.
