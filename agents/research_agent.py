from agents.base_agent import BaseAgent, Blackboard
from scraper import WordpressScraperAsync, DEFAULT_BASE_URL
import json
import os

class ResearchAgent(BaseAgent):
    """
    Advanced Research Agent that performs real asynchronous investigation
    of external domains identified during analysis.
    """
    def __init__(self):
        super().__init__("Research", dependencies=[], provides=["data_files", "raw_data"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.log("Starting research...")

        url = blackboard.get("url", DEFAULT_BASE_URL)
        limit = blackboard.get("limit", 5) # Default limit for testing
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

        # Apply compliance rules if available
        compliance = blackboard.get("compliance", {})
        disallowed = compliance.get("disallowed_paths", [])
        if disallowed:
            self.log(f"Applying {len(disallowed)} disallowed paths from compliance check.")
            scraper.set_disallowed_paths(disallowed)

        # Run the scrape
        await scraper.scrape()

        result = {
            "data_files": {
                "json": json_file,
                "csv": csv_file,
                "txt": txt_file
            }
        }

        # Load raw data into the result for other agents
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                result["raw_data"] = json.load(f)
            self.log(f"Scraped {len(result['raw_data'])} items.")
        except Exception as e:
            self.log(f"Failed to load scraped data: {e}")
            result["raw_data"] = []

        self.log("Research complete.")
        return result
