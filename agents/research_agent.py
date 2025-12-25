import asyncio
import urllib.robotparser
from urllib.parse import urlparse
from .base_agent import BaseAgent, AgentContext
from scraper import MarkPositionScraperAsync, BASE_URL

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("ResearchAgent 🔍")

    def check_robots_txt(self, url: str) -> bool:
        parsed = urlparse(url)
        robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(robots_url)
        try:
            rp.read()
            return rp.can_fetch("*", url)
        except Exception as e:
            # If we can't read robots.txt, we assume it's okay or fail safe.
            # Standard practice usually allows if no robots.txt, but let's be safe.
            print(f"Warning: Could not check robots.txt: {e}")
            return True

    def run(self, context: AgentContext):
        self.log(context, "Checking robots.txt compliance...")
        if not self.check_robots_txt(BASE_URL):
            self.log(context, f"🛑 Access to {BASE_URL} forbidden by robots.txt.")
            return

        self.log(context, f"Starting scraping of {BASE_URL}...")

        # Configure scraper
        json_out = "links.json"
        csv_out = "links.csv"
        txt_out = "unique_links.txt"

        scraper = MarkPositionScraperAsync(
            output_json=json_out,
            output_csv=csv_out,
            output_txt=txt_out,
            max_pages=1, # Limit for demo/autonomy speed
            concurrency=3
        )

        # Run async scraper in sync context
        asyncio.run(scraper.scrape())

        context.set("scraped_json", json_out)
        self.log(context, "Scraping complete. Data saved.")
