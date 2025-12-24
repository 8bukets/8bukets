from .base import BaseAgent
from typing import Any, Dict
import sys
import os
import asyncio

# Ensure root directory is in path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scraper import MarkPositionScraperAsync

class ResearchAgent(BaseAgent):
    def __init__(self, limit: int = 5):
        super().__init__("ResearchAgent")
        self.limit = limit
        self.output_json = "data.json" # Internal data file for agents
        self.output_csv = "data.csv"
        self.output_txt = "data.txt"

    async def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        self.log(f"Starting research (scraping max {self.limit} pages)...")

        scraper = MarkPositionScraperAsync(
            output_json=self.output_json,
            output_csv=self.output_csv,
            output_txt=self.output_txt,
            max_pages=self.limit,
            concurrency=3
        )

        await scraper.scrape()
        self.log("Scraping complete.")

        # Load the data to pass to context
        import json
        try:
            with open(self.output_json, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return {"scraped_data": data}
        except Exception as e:
            self.log(f"Failed to load scraped data: {e}")
            return {"scraped_data": []}
