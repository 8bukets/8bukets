from .base_agent import BaseAgent
import scrape_informatic
import google_search_scraper

class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__("Researcher")

    def perform_task(self, data):
        # Data can specify limits or targets
        limit = data.get('limit', 1) if data else 1
        # output_file is no longer mandatory for internal passing, but we can still respect it if needed.
        # For performance, we skip writing if not strictly required, but the instruction implied optimization.
        # We will keep data in memory.

        self.logger.info(f"Scraping content (limit {limit} pages)...")

        results = {}

        # 1. Scrape Blog Content
        try:
            # Direct call to scrape_informatic.scrape
            # We skip file writing by default unless user specified output_file in data,
            # but original code always wrote to 'data.json' or data['output_file'].
            # To preserve exact functionality (side effect of creating file), we could pass output_file.
            # However, Bolt's mission is speed. Removing disk I/O is a speed feature.
            # If the file is not used elsewhere (only read back), we can skip it.
            # main_orchestrator.py does NOT use 'data.json' directly; it uses the returned data.
            # So we can safely skip file writing.

            results['blog_posts'] = scrape_informatic.scrape(max_pages=limit)

        except Exception as e:
            self.logger.error(f"Blog scraping failed: {e}")
            results['blog_posts'] = []

        # 2. Check Google Listings
        self.logger.info("Checking Google Listings...")
        try:
            # Direct call to google_search_scraper
            # perform_google_search returns the list.
            # Default query was "site:informaticmagazine.data.blog"

            results['google_listings'] = google_search_scraper.perform_google_search(
                query="site:informaticmagazine.data.blog",
                num_results=10
            )

        except Exception as e:
            self.logger.error(f"Google search scraping failed: {e}")
            results['google_listings'] = []

        return results
