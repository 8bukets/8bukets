import aiohttp
import asyncio
from .base_agent import BaseAgent

class HealthCheckAgent(BaseAgent):
    def __init__(self):
        super().__init__("Health Check Agent")

    async def check_url(self, session, url):
        try:
            async with session.head(url, allow_redirects=True, timeout=5) as response:
                return url, response.status
        except Exception:
            return url, "Error"

    async def check_links(self, links):
        async with aiohttp.ClientSession() as session:
            tasks = [self.check_url(session, link) for link in links]
            return await asyncio.gather(*tasks)

    def run(self):
        self.log("Starting health check on recent links...")
        if not self.data:
            return

        # Check only top 10 recent links to save time/resources
        recent_links = [p.get('external_link') for p in self.data if p.get('external_link')][:10]

        # Async run wrapper
        loop = asyncio.get_event_loop()
        if loop.is_running():
            # Should not happen in standard script execution but safe handling
            results = asyncio.run(self.check_links(recent_links))
        else:
            results = loop.run_until_complete(self.check_links(recent_links))

        self.results = {
            "checked_count": len(results),
            "statuses": {str(link): status for link, status in results}
        }
        self.log("Health check complete.")
