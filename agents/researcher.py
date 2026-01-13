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

        self.logger.info("Scraping content (limit %s pages)...", limit)

        results = {}

        # 1. Scrape Blog Content
        try:
            # Import dynamically to avoid top-level import issues if not in path
            import scrape_informatic

            # Use direct function call instead of subprocess
            # This avoids process startup overhead and disk I/O
            results['blog_posts'] = scrape_informatic.scrape(output_file=output_file, max_pages=limit)

        except ImportError:
            self.logger.error("Could not import scrape_informatic module. Ensure it is in the python path.")
            results['blog_posts'] = []
        except Exception as e:
            # pylint: disable=broad-except
            self.logger.error("Blog scraping failed: %s", e)
            results['blog_posts'] = []

        # 2. Check Google Listings
        self.logger.info("Checking Google Listings...")
        try:
            search_output = "google_search_results.json"
            # We assume google_search_scraper.py is in the root directory
            cmd = [sys.executable, "google_search_scraper.py", "-o", search_output]
            subprocess.run(cmd, check=True)

            if os.path.exists(search_output):
                with open(search_output, 'r', encoding='utf-8') as f:
                    results['google_listings'] = json.load(f)
            else:
                results['google_listings'] = []
        except Exception as e:
            # pylint: disable=broad-except
            self.logger.error("Google search scraping failed: %s", e)
            results['google_listings'] = []

        return results
