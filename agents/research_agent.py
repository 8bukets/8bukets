from agents.base_agent import BaseAgent
from scraper import WordpressScraperAsync, DEFAULT_BASE_URL
import os

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("Research")

    async def run(self, context: dict):
        self.log("Starting research...")

        url = context.get("url", DEFAULT_BASE_URL)
        limit = context.get("limit", 5) # Default limit for testing
        json_file = "links.json"
        csv_file = "links.csv"
        txt_file = "unique_links.txt"

        scraper = WordpressScraperAsync(
            base_url=url,
            output_json=json_file,
            output_csv=csv_file,
            output_txt=txt_file,
            max_pages=limit,
            concurrency=5
        )

        # Run the scrape
        await scraper.scrape()

        # Update context with file paths
        context["data_files"] = {
            "json": json_file,
            "csv": csv_file,
            "txt": txt_file
        }

        # Load raw data into context for other agents
        try:
            import json
            with open(json_file, 'r', encoding='utf-8') as f:
                context["raw_data"] = json.load(f)
            self.log(f"Scraped {len(context['raw_data'])} items.")
        except Exception as e:
            self.log(f"Failed to load scraped data: {e}")
            context["raw_data"] = []

        self.log("Research complete.")
