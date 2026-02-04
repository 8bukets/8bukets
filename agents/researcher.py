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

    def _scrape_blog(self, limit, output_file):
        """Helper to run the blog scraper."""
        try:
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

    def _scrape_google(self, search_output):
        """Helper to run the google scraper."""
        try:
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
        search_output = "google_search_results.json"

        self.logger.info(f"Starting research tasks (limit {limit} pages)...")

        results = {}

        # Parallel execution using ThreadPoolExecutor
        # Optimization: Run independent scraping tasks in parallel to reduce total wait time.
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            future_blog = executor.submit(self._scrape_blog, limit, output_file)
            future_google = executor.submit(self._scrape_google, search_output)

            # Wait for results
            results['blog_posts'] = future_blog.result()
            results['google_listings'] = future_google.result()

        self.logger.info(f"Research tasks completed. Found {len(results.get('blog_posts', []))} posts and {len(results.get('google_listings', []))} listings.")
        return results
