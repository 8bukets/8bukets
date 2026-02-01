from .base_agent import BaseAgent
import subprocess
import sys
import json
import os
import logging
import concurrent.futures
from typing import List, Dict

class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__("Researcher")

    def _scrape_blog(self, limit, output_file):
        """Helper to run blog scraping subprocess."""
        try:
            # We assume scrape_informatic.py is in the root directory
            cmd = [sys.executable, "scrape_informatic.py", "-n", str(limit), "-o", output_file]
            subprocess.run(cmd, check=True)

            if os.path.exists(output_file):
                with open(output_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return []
        except Exception as e:
            self.logger.error(f"Blog scraping failed: {e}")
            return []

    def _scrape_google(self):
        """Helper to run Google search scraping subprocess."""
        self.logger.info("Checking Google Listings...")
        try:
            search_output = "google_search_results.json"
            # We assume google_search_scraper.py is in the root directory
            cmd = [sys.executable, "google_search_scraper.py", "-o", search_output]
            subprocess.run(cmd, check=True)

            if os.path.exists(search_output):
                with open(search_output, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return []
        except Exception as e:
            self.logger.error(f"Google search scraping failed: {e}")
            return []

    def perform_task(self, data):
        # Data can specify limits or targets
        limit = data.get('limit', 1) if data else 1
        output_file = data.get('output_file', 'data.json') if data else 'data.json'

        self.logger.info(f"Scraping content (limit {limit} pages)...")

        results = {}

        # Run scraping tasks in parallel
        # ⚡ Bolt Optimization: Run I/O bound tasks concurrently
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            future_blog = executor.submit(self._scrape_blog, limit, output_file)
            future_google = executor.submit(self._scrape_google)

            results['blog_posts'] = future_blog.result()
            results['google_listings'] = future_google.result()

        return results
