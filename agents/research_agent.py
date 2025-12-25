from .base_agent import BaseAgent
import requests
from bs4 import BeautifulSoup

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("ResearchAgent")

    def run(self, context):
        query = context.get('search_query', 'site:malubeach.wordpress.com')
        self.log(f"Researching Google for: {query}")

        # Simulated Google Search (reusing logic from google_listings.py)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        url = f"https://www.google.com/search?q={query}&num=5"

        results_found = []
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                results = soup.find_all('div', class_='g')
                for res in results:
                    title_tag = res.find('h3')
                    if title_tag:
                        results_found.append(title_tag.get_text())
            else:
                self.log(f"Search failed with status {response.status_code}")
        except Exception as e:
            self.log(f"Search error: {e}")

        self.learn("search_results", results_found)
        return {"indexed_pages": results_found}
