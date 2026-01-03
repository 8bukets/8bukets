from .base import Agent
import sqlite3

class MonetizationAgent(Agent):
    def __init__(self):
        super().__init__("MonetizationAgent")

    def perform_task(self):
        # DNA based IQ
        iq_level = self.dna.get('system_stats', {}).get('iq_level', 10)

        commercial_keywords = ['shop', 'buy', 'price', 'sale', 'deal', 'store']
        opportunities = []
        adsense_opportunities = []

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title, post_url FROM posts ORDER BY scraped_at DESC LIMIT 50")
            posts = cursor.fetchall()

            for title, url in posts:
                # Affiliate Check
                if any(kw in title.lower() for kw in commercial_keywords):
                    opportunities.append({'title': title, 'url': url})

                # AdSense Compliance Check (Simulated)
                # High IQ agents are better at spotting safe content
                if iq_level > 20:
                    if "gambling" not in title.lower() and "adult" not in title.lower():
                        adsense_opportunities.append({'title': title, 'url': url, 'type': 'AdSense Safe'})

        self.results['opportunities_count'] = len(opportunities)
        self.results['top_opportunities'] = opportunities[:3]
        self.results['adsense_candidates'] = adsense_opportunities[:3]

        if self.cookie_jar:
             self.cookie_jar.set_cookie("monetization.google", "adsense_status", "active", "3rd")
