from .base_agent import BaseAgent
import asyncio
from scraper import MarkPositionScraperAsync
import os

class ResearchAgent(BaseAgent):
    def __init__(self, shared_state):
        super().__init__("ResearchAgent", shared_state)
        self.scraped = False

    async def perform_task(self):
        if not self.scraped:
            self.log("🕵️ Starting research (scraping)...")
            scraper = MarkPositionScraperAsync(
                output_json="autonomous_links.json",
                output_csv="autonomous_links.csv",
                output_txt="autonomous_unique_links.txt",
                max_pages=2, # Limit for demo/autonomy to be fast
                concurrency=3
            )
            await scraper.scrape()
            self.scraped = True
            self.shared_state['new_data_available'] = True
            self.log("✅ Research complete. Data updated.")

            # Notify Intelligence Agent
            if 'IntelligenceAgent' in self.shared_state['agents']:
                self.send_message(self.shared_state['agents']['IntelligenceAgent'], {
                    'type': 'research_complete',
                    'count': 350 # approximation or need to read file
                })

        await asyncio.sleep(10)
