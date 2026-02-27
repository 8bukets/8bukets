from .base_agent import BaseAgent
from urllib.parse import urlparse
import logging

class RobotTxtAgent(BaseAgent):
    def __init__(self):
        super().__init__("RobotTxtAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Checking robots.txt compliance and secrets...")

        # Determine base URL from data or default
        base_url = "https://markposition.wordpress.com"
        if data:
            # Try to infer from first post
            link = data[0].get('post_url')
            if link:
                parsed = urlparse(link)
                base_url = f"{parsed.scheme}://{parsed.netloc}"

        robots_url = f"{base_url}/robots.txt"
        self.logger.info(f"Fetching {robots_url}")

        robots_content = self.fetch_robots_sync(robots_url)

        disallowed = []
        sitemaps = []

        if robots_content:
            for line in robots_content.splitlines():
                line = line.strip()
                if line.lower().startswith("disallow:"):
                    path = line.split(":", 1)[1].strip()
                    disallowed.append(path)
                elif line.lower().startswith("sitemap:"):
                    sitemaps.append(line.split(":", 1)[1].strip())

        # Save findings to memory for evolution (e.g. noticing changes over time)
        previous_disallowed = self.get_agent_memory("disallowed_paths", [])
        new_paths = set(disallowed) - set(previous_disallowed)
        if new_paths:
            self.logger.info(f"EVOLUTION: New disallowed paths detected: {new_paths}")

        self.update_agent_memory("disallowed_paths", disallowed)

        return {
            "robots_txt": {
                "url": robots_url,
                "status": "Found" if robots_content else "Not Found",
                "disallowed_paths": disallowed,
                "sitemaps": sitemaps
            }
        }

    def fetch_robots_sync(self, url):
        # Using requests for synchronous fetching within the pipeline
        try:
            import requests
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                return resp.text
            return None
        except ImportError:
            self.logger.error("Request module not found. Skipping robots.txt fetch.")
            return None
        except Exception as e:
            self.logger.error(f"Failed to fetch robots.txt: {e}")
            return None
