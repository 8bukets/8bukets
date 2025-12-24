from .base_agent import BaseAgent
from typing import List, Dict, Any
import aiohttp
import asyncio
from urllib.parse import urlparse

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("Research Agent")

    async def fetch_headers(self, session, url):
        try:
            async with session.head(url, timeout=5, allow_redirects=True) as response:
                server = response.headers.get('Server', 'Unknown')
                return server
        except:
            return "Error"

    async def process(self, data: List[Dict]) -> Dict[str, Any]:
        # Get unique domains
        unique_links = list(set([p.get('external_link') for p in data if p.get('external_link')]))
        # Limit to top 5 unique links for "daily research" to avoid spamming
        targets = unique_links[:5]

        results = {}
        tech_stack = []

        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_headers(session, url) for url in targets]
            headers = await asyncio.gather(*tasks)

            for url, server in zip(targets, headers):
                domain = urlparse(url).netloc
                tech_stack.append(f"{domain}: {server}")

        results['Server Technologies (Sample)'] = "; ".join(tech_stack)
        return results
