import os
import json
import logging
import time
from .base_agent import BaseAgent, Blackboard

try:
    import psycopg2
    from psycopg2.extras import execute_values
    HAS_PSYCOPG2 = True
except ImportError:
    HAS_PSYCOPG2 = False

DEAD_LETTER_FILE = "data/failed_syncs.json"

class SyncAgent(BaseAgent):
    """Synchronizes scraped software and generated reviews with the database with retry logic."""
    def __init__(self):
        super().__init__("SyncAgent", 
                         dependencies=["analysis_stats", "generated_reviews"], 
                         provides=["sync_status"])
        self.db_url = os.environ.get("DATABASE_URL", "postgres://postgres:password@localhost:5432/software_reviews")
        self.max_retries = 3

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        if not HAS_PSYCOPG2:
            self.logger.warning("psycopg2-binary not installed. Skipping database sync.")
            return {"sync_status": "SKIPPED_NO_DRIVER"}

        self.logger.info("Synchronizing data and reviews with the web platform...")
        
        generated_reviews = blackboard.get("generated_reviews", {})
        
        # 1. Prepare software entries
        software_to_sync = []
        seen_slugs = set()
        for item in data:
            name = item.get("title")
            if not name: continue
            slug = name.lower().replace(" ", "-").replace("/", "-")[:50]
            if slug in seen_slugs: continue
            seen_slugs.add(slug)
            software_to_sync.append((
                name, slug, f"Automatically scraped from {item.get('post_url')}",
                ", ".join(item.get("categories", [])), item.get("external_link")
            ))

        # Retry logic
        conn = None
        for attempt in range(self.max_retries):
            try:
                conn = psycopg2.connect(self.db_url)
                break
            except Exception as e:
                self.logger.warning(f"Database connection attempt {attempt+1} failed: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt) # Exponential backoff
                else:
                    self.logger.error("Could not connect to database after all attempts. Caching failed sync.")
                    self._cache_failed_sync(software_to_sync, generated_reviews)
                    return {"sync_status": "FAILED_CACHED"}

        try:
            cur = conn.cursor()
            
            # 2. Ensure System User exists
            cur.execute("""
                INSERT INTO users (email, password_hash, role)
                VALUES ('system@8bukets.local', 'REDACTED', 'reviewer')
                ON CONFLICT (email) DO UPDATE SET role = 'reviewer'
                RETURNING id
            """)
            system_user_id = cur.fetchone()[0]

            # 3. Sync Software
            sw_query = """
                INSERT INTO software (name, slug, description, category, website_url)
                VALUES %s ON CONFLICT (slug) DO UPDATE SET website_url = EXCLUDED.website_url
                RETURNING id, slug
            """
            execute_values(cur, sw_query, software_to_sync)
            
            # Map slugs to IDs for review linking
            cur.execute("SELECT id, slug FROM software")
            slug_to_id = {slug: sid for sid, slug in cur.fetchall()}

            # 4. Sync Reviews
            reviews_to_sync = []
            for slug, review in generated_reviews.items():
                if slug in slug_to_id:
                    reviews_to_sync.append((
                        system_user_id, slug_to_id[slug], 
                        review['title'], review['content'], 
                        'approved', review['sentiment_score']
                    ))

            if reviews_to_sync:
                rev_query = """
                    INSERT INTO reviews (user_id, software_id, title, content, status, sentiment_score)
                    VALUES %s
                """
                execute_values(cur, rev_query, reviews_to_sync)

            conn.commit()
            self.logger.info(f"Sync complete. {len(software_to_sync)} software, {len(reviews_to_sync)} reviews.")
            cur.close()
            conn.close()
            
            # Clear cache if it was successful
            if os.path.exists(DEAD_LETTER_FILE):
                os.remove(DEAD_LETTER_FILE)
                
            return {"sync_status": f"SUCCESS_{len(software_to_sync)}_SW_{len(reviews_to_sync)}_REV"}
            
        except Exception as e:
            self.logger.error(f"Database sync failed during execution: {e}")
            if conn: conn.rollback()
            return {"sync_status": f"FAILED: {str(e)}"}

    def _cache_failed_sync(self, sw, rev):
        """Caches data that failed to sync locally."""
        cache = {
            "timestamp": time.time(),
            "software": sw,
            "reviews": rev
        }
        os.makedirs("data", exist_ok=True)
        with open(DEAD_LETTER_FILE, 'w') as f:
            json.dump(cache, f, indent=4)
        self.logger.info(f"Cached {len(sw)} entries to {DEAD_LETTER_FILE}")
