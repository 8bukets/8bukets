from .base import Agent
import sqlite3
import random
from google_checker import check_google_listings

class CuriosityAgent(Agent):
    def __init__(self):
        super().__init__("CuriosityAgent")

    def perform_task(self, context=None):
        """
        Explores adjacent topics to foster creativity.
        """
        # 1. Get a seed topic from DB
        topic = self.get_random_topic()
        if not topic:
            topic = "Design" # Fallback

        # 2. Apply "Antigravity" modifiers (unconventional combinations)
        modifiers = [
            "future of {} technology",
            "{} combined with AI",
            "autonomous {} systems",
            "coding for {}",
            "{} api integration",
            "impact of quantum computing on {}"
        ]
        modifier = random.choice(modifiers)
        query = modifier.format(topic)

        self.logger.info(f"Curiosity Triggered: Exploring '{query}'")

        # 3. Perform Exploration Search
        # We assume check_google_listings handles the search.
        # We limit to 5 results for exploration.
        search_results = check_google_listings(query, num_results=5)

        self.results['seed_topic'] = topic
        self.results['exploration_query'] = query
        self.results['findings'] = [r['title'] for r in search_results] if search_results else ["No external data found, internal simulation only."]

    def get_random_topic(self):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT title FROM posts ORDER BY RANDOM() LIMIT 1")
                row = cursor.fetchone()
                if row:
                    # Simple keyword extraction: take the longest word
                    words = row[0].split()
                    return max(words, key=len) if words else None
        except Exception as e:
            self.logger.error(f"DB Error: {e}")
        return None
