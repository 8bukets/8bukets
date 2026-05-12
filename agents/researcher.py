from .base_agent import BaseAgent
import sys
import json
import os
import logging
from typing import List, Dict
import concurrent.futures

# Import scraper modules
# We expect them to be in the python path (root directory)
try:
    import scrape_informatic
    import google_search_scraper
except ImportError as e:
    logging.warning(f"Scraper modules not found or dependencies missing: {e}")
    scrape_informatic = None
    google_search_scraper = None

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
    def _run_google_search_task(self, output_file: str):
        """
        Wraps google_search_scraper.perform_google_search to save results to file.
        """
        if not google_search_scraper:
            raise ImportError("google_search_scraper module not loaded")

        # Default query as per original script
        query = "site:informaticmagazine.data.blog"
        limit = 10 # Default limit

        # perform_google_search returns a list of dicts
        results = google_search_scraper.perform_google_search(query, num_results=limit)

        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=4, ensure_ascii=False)
            self.logger.info(f"Saved google search results to {output_file}")
        except IOError as e:
            self.logger.error(f"Failed to save google search output to {output_file}: {e}")
            raise

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
        search_output = "google_search_results.json"

        self.logger.info(f"Starting research (limit {limit} pages) with parallel execution...")

        results = {}
        results['blog_posts'] = []
        results['google_listings'] = []

        if not scrape_informatic or not google_search_scraper:
            self.logger.error("Scraper modules missing. Cannot perform research.")
            return results

        # Run scraping and google search in parallel using ThreadPoolExecutor
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            # Submit tasks
            future_blog = executor.submit(scrape_informatic.scrape, output_file, limit)
            future_google = executor.submit(self._run_google_search_task, search_output)

            # Wait for blog scraping
            try:
                # result() will raise any exception that occurred during execution
                future_blog.result()
                if os.path.exists(output_file):
                    with open(output_file, 'r', encoding='utf-8') as f:
                        results['blog_posts'] = json.load(f)
            except Exception as e:
                self.logger.error(f"Blog scraping failed: {e}")

            # Wait for google search
            try:
                future_google.result()
                if os.path.exists(search_output):
                    with open(search_output, 'r', encoding='utf-8') as f:
                        results['google_listings'] = json.load(f)
            except Exception as e:
                self.logger.error(f"Google search scraping failed: {e}")

        return results
