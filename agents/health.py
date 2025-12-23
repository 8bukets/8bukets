from .base import Agent
import os
import sqlite3

class HealthAgent(Agent):
    def __init__(self):
        super().__init__("HealthAgent")

    def perform_task(self):
        # Check DB
        if os.path.exists(self.db_name):
            self.results['db_status'] = "OK"
            self.results['db_size'] = os.path.getsize(self.db_name)
        else:
            self.results['db_status'] = "Missing"

        # Check Scraper output
        if os.path.exists("wishlist_data.json"):
            self.results['json_status'] = "OK"
        else:
            self.results['json_status'] = "Missing"
