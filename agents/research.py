import asyncio
from agents.base import BaseAgent
from scraper import WebshopScraperAsync
import logging

logger = logging.getLogger(__name__)

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("ResearchAgent")

    def run(self, output_json, output_csv, output_txt, max_pages=None, concurrency=5):
        logger.info(f"[{self.name}] Starting scraping task...")
        scraper = WebshopScraperAsync(
            output_json=output_json,
            output_csv=output_csv,
            output_txt=output_txt,
            max_pages=max_pages,
            concurrency=concurrency
        )
        try:
            asyncio.run(scraper.scrape())
            return True
        except Exception as e:
            logger.error(f"[{self.name}] Scraping failed: {e}")
            return False
