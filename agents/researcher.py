from .base_agent import BaseAgent
import sys
import json
import os
import logging
from typing import List, Dict

# Import scrapers directly to avoid subprocess overhead
import scrape_informatic
import google_search_scraper

class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__("Researcher")

    def perform_task(self, data):
        # Data can specify limits or targets
        limit = data.get('limit', 1) if data else 1
        output_file = data.get('output_file', 'data.json') if data else 'data.json'

        self.logger.info(f"Scraping content (limit {limit} pages)...")

        results = {}

        # 1. Scrape Blog Content
        try:
            # Optimization: Direct function call instead of subprocess
            results['blog_posts'] = scrape_informatic.scrape(output_file, max_pages=limit)
        except Exception as e:
            self.logger.error(f"Blog scraping failed: {e}")
            results['blog_posts'] = []

        # 2. Check Google Listings
        self.logger.info("Checking Google Listings...")
        try:
            search_output = "google_search_results.json"

            # Optimization: Direct function call instead of subprocess
            results['google_listings'] = google_search_scraper.perform_google_search(
                query="site:informaticmagazine.data.blog",
                num_results=10
            )
            # Persist to file to maintain behavior
            with open(search_output, 'w', encoding='utf-8') as f:
                json.dump(results['google_listings'], f, indent=4, ensure_ascii=False)

        except Exception as e:
            self.logger.error(f"Google search scraping failed: {e}")
            results['google_listings'] = []

        return results
