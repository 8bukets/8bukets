from .base_agent import BaseAgent
import subprocess
import sys
import json
import os
import logging
from typing import List, Dict

class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__("Researcher")

    def perform_task(self, data):
        # Data can specify limits or targets
        limit = data.get('limit', 1) if data else 1
        output_file = data.get('output_file', 'data.json') if data else 'data.json'
        # Security: Sanitize output_file to prevent path traversal
        output_file = os.path.basename(output_file)

        self.logger.info(f"Scraping content (limit {limit} pages)...")

        results = {}

        # 1. Scrape Blog Content
        try:
            # We assume scrape_informatic.py is in the root directory
            cmd = [sys.executable, "scrape_informatic.py", "-n", str(limit), "-o", output_file]
            subprocess.run(cmd, check=True)

            if os.path.exists(output_file):
                with open(output_file, 'r', encoding='utf-8') as f:
                    results['blog_posts'] = json.load(f)
            else:
                results['blog_posts'] = []
        except Exception as e:
            self.logger.error(f"Blog scraping failed: {e}")
            results['blog_posts'] = []

        # 2. Check Google Listings
        self.logger.info("Checking Google Listings...")
        try:
            search_output = "google_search_results.json"
            # We assume google_search_scraper.py is in the root directory
            # We need to create google_search_scraper.py if it doesn't exist or is not importable
            # Since we are using subprocess, we can call it.
            # Wait, I need to restore google_search_scraper.py first.
            cmd = [sys.executable, "google_search_scraper.py", "-o", search_output]
            subprocess.run(cmd, check=True)

            if os.path.exists(search_output):
                with open(search_output, 'r', encoding='utf-8') as f:
                    results['google_listings'] = json.load(f)
            else:
                results['google_listings'] = []
        except Exception as e:
            self.logger.error(f"Google search scraping failed: {e}")
            results['google_listings'] = []

        return results
