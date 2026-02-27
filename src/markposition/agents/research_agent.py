from .base_agent import BaseAgent
from bs4 import BeautifulSoup
import asyncio

class WebResearchAgent(BaseAgent):
    execution_stage = 2
    def __init__(self):
        super().__init__("WebResearchAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Running Web Research...")

        analysis = context.get("analysis_stats", {})
        top_domains = list(analysis.get("top_domains", {}).keys())

        research_notes = []

        # Limit to top 3 domains to avoid excessive I/O
        for domain in top_domains[:3]:
            url = f"https://{domain}"
            try:
                self.logger.info(f"Researching domain: {url}")
                if self.session:
                    async with self.session.get(url, timeout=10) as resp:
                        if resp.status == 200:
                            html = await resp.text()
                            soup = BeautifulSoup(html, 'html.parser')

                            title = soup.title.string if soup.title else "No title"
                            description = ""
                            desc_tag = soup.find("meta", attrs={"name": "description"})
                            if desc_tag:
                                description = desc_tag.get("content", "")

                            research_notes.append(f"Domain: {domain} | Title: {title} | Description: {description[:100]}...")
                        else:
                            research_notes.append(f"Domain: {domain} | Failed to fetch (Status: {resp.status})")
                else:
                    research_notes.append(f"Domain: {domain} | No session available for real-time research.")
            except Exception as e:
                self.logger.warning(f"Failed to research {domain}: {e}")
                research_notes.append(f"Domain: {domain} | Research error: {str(e)[:50]}")

        return {"research_notes": research_notes}
