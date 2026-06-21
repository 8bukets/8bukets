from agents.base_agent import BaseAgent
import aiohttp
from urllib.parse import urlparse

class ComplianceAgent(BaseAgent):
    def __init__(self):
        super().__init__("Compliance")

    async def run(self, context: dict):
        self.log("Checking compliance and robots.txt...")
        url = context.get("url", "https://artmusicpage.wordpress.com/")
        parsed = urlparse(url)
        robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"

        disallowed = []
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(robots_url) as response:
                    if response.status == 200:
                        text = await response.text()
                        for line in text.splitlines():
                            if line.strip().lower().startswith("disallow:"):
                                path = line.split(":", 1)[1].strip()
                                if path:
                                    disallowed.append(path)
                        self.log(f"Found {len(disallowed)} disallow rules.")
                    else:
                        self.log(f"Could not fetch robots.txt (Status: {response.status})")
        except Exception as e:
            self.log(f"Error checking robots.txt: {e}")

        context["compliance"] = {
            "robots_txt_url": robots_url,
            "disallowed_paths": disallowed,
            "can_scrape": True # Default to true, scraper will filter specific paths
        }
