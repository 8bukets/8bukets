from .base import Agent
import sqlite3
from datetime import datetime, timedelta
from collections import Counter
import re

class AnalystAgent(Agent):
    def __init__(self):
        super().__init__("AnalystAgent")

    def perform_task(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()

            # Stats
            cursor.execute("SELECT COUNT(*) FROM posts")
            total_posts = cursor.fetchone()[0]

            two_weeks_ago = datetime.now() - timedelta(weeks=2)
            cursor.execute("SELECT title FROM posts WHERE scraped_at >= ?", (two_weeks_ago,))
            new_titles = [row[0] for row in cursor.fetchall()]

            self.results['total_posts'] = total_posts
            self.results['new_posts_count'] = len(new_titles)
            self.results['keywords'] = self.analyze_keywords(new_titles)

    def analyze_keywords(self, titles):
        text = " ".join(titles).lower()
        text = re.sub(r'[^\w\s]', '', text)
        words = text.split()
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'this', 'that', 'it', 'as', 'from', 'de', 'la', 'official', 'online'}
        filtered_words = [w for w in words if w not in stop_words and len(w) > 2]
        return Counter(filtered_words).most_common(5)
