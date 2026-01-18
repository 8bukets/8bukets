from .base import BaseAgent
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import urllib.robotparser
import re

class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__("Researcher")
        self.base_url = "https://software-online-review.com/"
        self.rp = urllib.robotparser.RobotFileParser()
        self.rp.set_url(f"{self.base_url}robots.txt")
        self.read_robots_txt()

    def read_robots_txt(self):
        try:
            self.rp.read()
            self.log_activity("Robots.txt read successfully.")
        except Exception as e:
            self.logger.error(f"Could not read robots.txt: {e}")

    def can_fetch(self, url):
        return self.rp.can_fetch("*", url)

    async def fetch_page(self, session, url):
        if not self.can_fetch(url):
            self.log_activity(f"Blocked by robots.txt: {url}")
            return None

        try:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    self.logger.warning(f"Failed to fetch {url}: {response.status}")
        except Exception as e:
            self.logger.error(f"Error fetching {url}: {e}")
        return None

    async def scrape(self, limit=1):
        self.log_activity(f"Starting research scrape on {self.base_url}")
        async with aiohttp.ClientSession() as session:
            html = await self.fetch_page(session, self.base_url)
            if html:
                soup = BeautifulSoup(html, 'html.parser')
                articles = soup.select('article')
                posts = []
                for article in articles[:limit]:
                    title_tag = article.select_one('.entry-title a')
                    if title_tag:
                        posts.append({
                            'title': title_tag.get_text().strip(),
                            'url': title_tag['href']
                        })
                return posts
        return []

    def run(self, context):
        self.log_activity("Running research task...")
        loop = asyncio.get_event_loop()
        if loop.is_closed():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        # In a real environment, we'd manage the loop better or reuse existing
        posts = loop.run_until_complete(self.scrape(limit=3))
        context['scraped_data'] = posts
        self.learn(f"Found {len(posts)} articles.")
