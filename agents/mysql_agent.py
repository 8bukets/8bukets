import os
import asyncio
import json
from .base_agent import BaseAgent, Blackboard

try:
    import aiomysql
    AIOMYSQL_AVAILABLE = True
except ImportError:
    AIOMYSQL_AVAILABLE = False

class MySQLAgent(BaseAgent):
    """
    Agent responsible for synchronizing system state and scraped data
    with a MySQL database instance.
    """
    def __init__(self):
        super().__init__("MySQLAgent",
                         dependencies=["analysis_stats", "research_data", "system_evolution"],
                         provides=["mysql_sync_status"])
        self.host = os.environ.get("MYSQL_HOST", "localhost")
        self.port = int(os.environ.get("MYSQL_PORT", 3306))
        self.user = os.environ.get("MYSQL_USER", "root")
        self.password = os.environ.get("MYSQL_PASSWORD", "")
        self.db_name = os.environ.get("MYSQL_DB", "markposition_db")

    async def _init_db(self, pool):
        """Creates tables if they don't exist."""
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                # Create posts table
                await cur.execute("""
                    CREATE TABLE IF NOT EXISTS posts (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        post_url VARCHAR(512) UNIQUE,
                        title TEXT,
                        date VARCHAR(255),
                        author VARCHAR(255),
                        categories TEXT,
                        external_link TEXT,
                        domain VARCHAR(255),
                        full_data JSON
                    )
                """)
                # Create system snapshots table
                await cur.execute("""
                    CREATE TABLE IF NOT EXISTS system_snapshots (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        timestamp FLOAT,
                        evolution JSON,
                        sigma_status JSON,
                        analysis JSON
                    )
                """)
            await conn.commit()

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        if not AIOMYSQL_AVAILABLE:
            self.logger.warning("aiomysql not installed. Skipping sync.")
            return {"mysql_sync_status": "DRIVER_MISSING"}

        if not os.environ.get("MYSQL_HOST"):
            self.logger.warning("MYSQL_HOST not found in environment. Using default 'localhost' or skipping sync if connection fails.")
            # We don't strictly return here since we have a default "localhost", but it's good to log.

        self.logger.info(f"Synchronizing data to MySQL database: {self.db_name} at {self.host}:{self.port}")

        try:
            pool = await aiomysql.create_pool(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                db=self.db_name,
                autocommit=True
            )

            # Initialize tables
            await self._init_db(pool)

            async with pool.acquire() as conn:
                async with conn.cursor() as cur:
                    # 1. Sync Scraped Data (Batch Upsert)
                    if data:
                        for post in data:
                            if "post_url" in post:
                                post_url = post["post_url"]
                                title = post.get("title", "")
                                date_str = post.get("date", "")
                                author = post.get("author", "")
                                categories = json.dumps(post.get("categories", []))
                                external_link = post.get("external_link", "")
                                domain = post.get("domain", "")
                                full_data = json.dumps(post)

                                # Use INSERT ... ON DUPLICATE KEY UPDATE for upsert functionality
                                await cur.execute("""
                                    INSERT INTO posts (post_url, title, date, author, categories, external_link, domain, full_data)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                    ON DUPLICATE KEY UPDATE
                                        title=VALUES(title),
                                        date=VALUES(date),
                                        author=VALUES(author),
                                        categories=VALUES(categories),
                                        external_link=VALUES(external_link),
                                        domain=VALUES(domain),
                                        full_data=VALUES(full_data)
                                """, (post_url, title, date_str, author, categories, external_link, domain, full_data))

                        self.logger.info(f"Synced {len(data)} posts to MySQL.")

                    # 2. Sync System Snapshot
                    snapshot_timestamp = asyncio.get_event_loop().time()
                    evolution = json.dumps(blackboard.get("system_evolution") or {})
                    sigma_status = json.dumps(blackboard.get("sigma_performance_report") or {})
                    analysis = json.dumps(blackboard.get("analysis_stats") or {})

                    await cur.execute("""
                        INSERT INTO system_snapshots (timestamp, evolution, sigma_status, analysis)
                        VALUES (%s, %s, %s, %s)
                    """, (snapshot_timestamp, evolution, sigma_status, analysis))

            pool.close()
            await pool.wait_closed()
            return {"mysql_sync_status": "SUCCESS"}

        except Exception as e:
            self.logger.error(f"Failed to sync with MySQL: {e}")
            return {"mysql_sync_status": f"FAILED: {str(e)}"}
