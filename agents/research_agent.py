import asyncio
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse
from agents.base_agent import BaseAgent
from scraper import MarkPositionScraperAsync

class ResearchAgent(BaseAgent):
    def __init__(self, name: str = "Research"):
        super().__init__(name)
        self.robot_parser = RobotFileParser()

    def check_robots_txt(self, url: str) -> bool:
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        robots_url = f"{base_url}/robots.txt"

        self.log(f"Checking robots.txt at {robots_url}...")
        try:
            self.robot_parser.set_url(robots_url)
            self.robot_parser.read()
            can_fetch = self.robot_parser.can_fetch("*", url)
            self.log(f"Robots.txt permission for {url}: {can_fetch}")
            return can_fetch
        except Exception as e:
            self.log(f"Failed to check robots.txt: {e}", level="warning")
            # Fail open or closed? Usually fail open if robots.txt missing, but let's be safe.
            # If read() fails, it might be 404, which means allowed.
            return True

    async def process(self, data: dict) -> dict:
        """
        Expects data to contain 'target_url' and optionally 'limit' and 'concurrency'.
        """
        target_url = data.get("target_url", "https://markposition.wordpress.com/")
        limit = data.get("limit", 1) # Default to 1 page for quick autonomous run
        concurrency = data.get("concurrency", 5)

        self.log(f"Starting research on {target_url}")

        # Check robots.txt
        if not self.check_robots_txt(target_url):
            self.log(f"Access denied by robots.txt for {target_url}", level="error")
            return {"status": "blocked", "data": []}

        # Configure Scraper
        # Note: The original scraper writes to files. We might want to capture the data directly.
        # But for now, we'll let it write files and then read them, or modify scraper to return data.
        # Looking at scraper.py, it has `scrape()` which doesn't return data but saves it.
        # However, `scrape` populates `self.save_data`.
        # We can subclass or instantiate and modify.
        # To be cleaner, let's just run it and read the JSON.

        output_json = "agent_links.json"
        output_csv = "agent_links.csv"
        output_txt = "agent_unique_links.txt"

        scraper = MarkPositionScraperAsync(
            output_json=output_json,
            output_csv=output_csv,
            output_txt=output_txt,
            max_pages=limit,
            concurrency=concurrency
        )

        # We need to await the scrape
        await scraper.scrape()

        # Read the result
        import json
        try:
            with open(output_json, 'r', encoding='utf-8') as f:
                scraped_data = json.load(f)
            self.log(f"Successfully scraped {len(scraped_data)} items.")
            return {"status": "success", "data": scraped_data, "file": output_json}
        except Exception as e:
            self.log(f"Error reading scraped data: {e}", level="error")
            return {"status": "error", "error": str(e)}
