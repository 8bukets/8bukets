from .base_agent import BaseAgent
from dataclasses import asdict

# Import scrapers directly
try:
    import scrape_informatic
    import google_search_scraper
except ImportError:
    # Handle cases where run from inside agents directory or package issues
    import sys
    import os
    sys.path.append(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))
    import scrape_informatic
    import google_search_scraper


class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__("Researcher")

    def perform_task(self, data):
        # Data can specify limits or targets
        limit = data.get('limit', 1) if data else 1
        # output_file is no longer strictly needed for data transfer, but we can still save it if desired
        # or we can remove it. For now, we will skip saving to file unless explicitly requested or for debugging
        # But to be safe and compatible with previous behavior if anything relies on the file existing:
        output_file = data.get(
            'output_file', 'data.json') if data else 'data.json'

        self.logger.info(f"Scraping content (limit {limit} pages)...")

        results = {}

        # 1. Scrape Blog Content
        try:
            # Direct call to scrape function
            # scrape returns List[Post] objects
            posts = scrape_informatic.scrape(
                output_file=output_file, max_pages=limit)
            results['blog_posts'] = [asdict(p) for p in posts]

        except Exception as e:
            self.logger.error(f"Blog scraping failed: {e}")
            results['blog_posts'] = []

        # 2. Check Google Listings
        self.logger.info("Checking Google Listings...")
        try:
            # Direct call to google search
            # We use the defaults from the script if not specified
            query = "site:informaticmagazine.data.blog"
            search_results = google_search_scraper.perform_google_search(
                query, num_results=10)
            results['google_listings'] = search_results

        except Exception as e:
            self.logger.error(f"Google search scraping failed: {e}")
            results['google_listings'] = []

        return results
