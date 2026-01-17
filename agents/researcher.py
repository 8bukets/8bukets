from .base_agent import BaseAgent
import json
import os
import logging
from typing import List, Dict
import concurrent.futures
import sys

# Import scrapers (assuming running from root)
try:
    import scrape_informatic
    import google_search_scraper
except ImportError:
    # If running from agents dir or elsewhere, try to adjust path
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    import scrape_informatic
    import google_search_scraper

class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__("Researcher")

    def perform_task(self, data):
        # Data can specify limits or targets
        limit = data.get('limit', 1) if data else 1
        output_file = data.get('output_file', 'data.json') if data else 'data.json'
        search_output = "google_search_results.json"

        self.logger.info(f"Scraping content (limit {limit} pages) and checking Google listings...")

        results = {}

        # Use ThreadPoolExecutor to run scraping tasks in parallel
        # This significantly speeds up the process by not waiting for one to finish before starting the other
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            future_blog = executor.submit(self._scrape_blog, limit, output_file)
            future_google = executor.submit(self._search_google, search_output)

            results['blog_posts'] = future_blog.result()
            results['google_listings'] = future_google.result()

        return results

    def _scrape_blog(self, limit, output_file):
        try:
            self.logger.info("Starting blog scraping...")
            # Call the scraper directly instead of using subprocess
            return scrape_informatic.scrape(output_file=output_file, max_pages=limit)
        except Exception as e:
            self.logger.error(f"Blog scraping failed: {e}")
            return []

    def _search_google(self, output_file):
        try:
            self.logger.info("Starting Google search...")
            query = "site:informaticmagazine.data.blog"
            # Call the scraper directly
            results = google_search_scraper.perform_google_search(query, num_results=10)

            # Save to file to maintain existing behavior (artifacts for inspection)
            try:
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(results, f, indent=4, ensure_ascii=False)
                # Use logger from BaseAgent if available, but here we are in a method.
                # self.logger is available.
                self.logger.info(f"Saved results to {output_file}")
            except IOError as e:
                self.logger.error(f"Failed to save output to {output_file}: {e}")

            return results
        except Exception as e:
            self.logger.error(f"Google search scraping failed: {e}")
            return []
