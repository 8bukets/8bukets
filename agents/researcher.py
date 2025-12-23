from .base import Agent
from google_checker import check_google_listings, save_rankings_to_db

class ResearcherAgent(Agent):
    def __init__(self):
        super().__init__("ResearcherAgent")

    def perform_task(self):
        query = "site:wishlist.design.blog"
        # We can also add dynamic queries based on analysis later
        results = check_google_listings(query)
        save_rankings_to_db(results, query)

        self.results['seo_checked'] = True
        self.results['rankings_found'] = len(results)
        self.results['top_rank'] = results[0]['title'] if results else "None"
