from .base_agent import BaseAgent
import subprocess
import sys
import json
import os
import logging
from typing import List, Dict
import concurrent.futures

class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__("Researcher")

    def _scrape_blog_task(self, limit, output_file):
        """Task to scrape blog content."""
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

    def _check_google_listings_task(self):
        """Task to check google listings."""
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

        self.logger.info(f"Scraping content (limit {limit} pages) and checking Google listings in parallel...")

        results = {}

        # Use ThreadPoolExecutor to run independent I/O bound tasks in parallel
        # Bolt Optimization: Parallelize independent scraping tasks
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            future_blog = executor.submit(self._scrape_blog_task, limit, output_file)
            future_google = executor.submit(self._check_google_listings_task)

            # Retrieve results
            results['blog_posts'] = future_blog.result()
            results['google_listings'] = future_google.result()

        return results
