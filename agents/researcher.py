from .base_agent import BaseAgent
import sys
import json
import os
import logging

# Import scrapers directly
sys.path.append(os.getcwd()) # Ensure root is in path
try:
    import scrape_informatic
    import google_search_scraper
except ImportError:
    logging.getLogger("Researcher").warning("Could not import scrapers. Make sure they are in the python path.")

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
            # Direct call to scrape_informatic
            self.logger.info("Calling scrape_informatic.scrape() directly.")
            blog_posts = scrape_informatic.scrape(output_file, max_pages=limit)
            results['blog_posts'] = blog_posts
        except Exception as e:
            self.logger.error("Blog scraping failed: %s", e)
            # Fallback to file reading if scrape failed but maybe wrote file?
            # Or just empty list
            results['blog_posts'] = []

        # 2. Check Google Listings
        self.logger.info("Checking Google Listings...")
        try:
            search_output = "google_search_results.json"
            query = "site:informaticmagazine.data.blog"
            limit_search = 10 # Default from original script

            # Direct call to google_search_scraper
            self.logger.info("Calling google_search_scraper.perform_google_search() directly.")
            search_results = google_search_scraper.perform_google_search(query, num_results=limit_search)

            # Save artifacts as expected by other components or for history
            with open(search_output, 'w', encoding='utf-8') as f:
                json.dump(search_results, f, indent=4, ensure_ascii=False)

            results['google_listings'] = search_results

        except Exception as e:
            self.logger.error("Google search scraping failed: %s", e)
            results['google_listings'] = []

        return results
