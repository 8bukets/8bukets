from .base import Agent
import sqlite3

class MonetizationAgent(Agent):
    def __init__(self):
        super().__init__("MonetizationAgent")

    def perform_task(self):
        commercial_keywords = ['shop', 'buy', 'price', 'sale', 'deal', 'store']
        opportunities = []

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title, post_url FROM posts ORDER BY scraped_at DESC LIMIT 50")
            posts = cursor.fetchall()

            for title, url in posts:
                if any(kw in title.lower() for kw in commercial_keywords):
                    opportunities.append({'title': title, 'url': url})

        self.results['opportunities_count'] = len(opportunities)
        self.results['top_opportunities'] = opportunities[:3]
