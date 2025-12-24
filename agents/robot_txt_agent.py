from .base_agent import BaseAgent
from typing import List, Dict, Any
import aiohttp
from urllib.parse import urlparse

class RobotTxtAgent(BaseAgent):
    def __init__(self):
        super().__init__("Robot.txt Agent")

    async def fetch_robots(self, session, url):
        try:
            parsed = urlparse(url)
            base = f"{parsed.scheme}://{parsed.netloc}"
            robots_url = f"{base}/robots.txt"

            async with session.get(robots_url, timeout=5) as response:
                if response.status == 200:
                    text = await response.text()
                    return robots_url, "Found", text[:100].replace('\n', ' ') + "..." # Preview
                else:
                    return robots_url, f"Status {response.status}", ""
        except Exception as e:
            return url, f"Error: {str(e)}", ""

    async def process(self, data: List[Dict], shared_context: Dict[str, Any], knowledge_base: Dict[str, Any]) -> Dict[str, Any]:
        # Identify the main domain from data
        if not data:
            return {"Status": "No data to check"}

        # Try to find the source domain. We assume the first post URL gives us the site.
        target_url = "https://markposition.wordpress.com/" # Default known target
        if data[0].get('post_url'):
            target_url = data[0]['post_url']

        results = {}

        async with aiohttp.ClientSession() as session:
            url, status, preview = await self.fetch_robots(session, target_url)
            results['Target'] = url
            results['Status'] = status
            results['Preview'] = preview

            # Share with other agents
            shared_context['robots_allowed'] = (status == "Found")
            shared_context['target_domain'] = urlparse(target_url).netloc

        return results
