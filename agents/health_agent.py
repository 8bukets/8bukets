from .base_agent import BaseAgent
from typing import List, Dict, Any
import aiohttp
import asyncio
import random

class HealthCheckAgent(BaseAgent):
    def __init__(self):
        super().__init__("Health Check Agent")

    async def check_link(self, session, url):
        try:
            async with session.head(url, timeout=5, allow_redirects=True) as response:
                return response.status
        except:
            return 0

    async def process(self, data: List[Dict], shared_context: Dict[str, Any], knowledge_base: Dict[str, Any]) -> Dict[str, Any]:
        links = [p.get('external_link') for p in data if p.get('external_link')]
        if not links:
            return {"Health Status": "No links to check"}

        # Check sample
        sample = random.sample(links, min(len(links), 5))

        results = {}
        # Use shared session if available, else create local
        session = shared_context.get('session')
        local_session = None
        if not session:
            local_session = aiohttp.ClientSession()
            session = local_session

        try:
            tasks = [self.check_link(session, url) for url in sample]
            statuses = await asyncio.gather(*tasks)

            success_count = len([s for s in statuses if 200 <= s < 400])
            results['Sample Size'] = len(sample)
            results['Healthy Links'] = success_count
            results['Broken/Error Links'] = len(sample) - success_count
        finally:
            if local_session:
                await local_session.close()

        return results
