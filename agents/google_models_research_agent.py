import aiohttp
from bs4 import BeautifulSoup
from agents.base_agent import BaseAgent, Blackboard

class GoogleModelsResearchAgent(BaseAgent):
    """
    Scrapes https://blog.google/innovation-and-ai/models-and-research/
    and adds the latest research knowledge to the Blackboard.
    """
    def __init__(self):
        super().__init__("GoogleModelsResearchAgent", dependencies=[], provides=["google_models_research_knowledge"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        url = "https://blog.google/innovation-and-ai/models-and-research/"
        self.logger.info(f"Scraping knowledge from {url}...")

        knowledge = {
            "source": url,
            "articles": []
        }

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            async with aiohttp.ClientSession(headers=headers, timeout=aiohttp.ClientTimeout(total=15)) as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        html = await response.text()
                        soup = BeautifulSoup(html, "html.parser")

                        # Find all article links - they often have a specific class or are within a specific structure
                        # Based on typical Google Blog structure, they use <a> tags with titles
                        # We'll look for links that look like blog posts
                        links = soup.find_all('a', href=True)
                        seen_urls = set()

                        for link in links:
                            href = link['href']
                            # Filter for internal blog posts in models-and-research
                            if '/innovation-and-ai/models-and-research/' in href and href != url:
                                full_url = href if href.startswith('http') else f"https://blog.google{href}"
                                if full_url not in seen_urls:
                                    title = link.get_text(strip=True)
                                    if title and len(title) > 10:
                                        # Attempt to find a summary in a neighboring tag or parent
                                        snippet = ""
                                        parent = link.find_parent(['div', 'section', 'li'])
                                        if parent:
                                            summary_tag = parent.find(['p', 'span', 'div'], class_=lambda x: x and ('summary' in x or 'description' in x or 'snippet' in x or 'deck' in x))
                                            if summary_tag:
                                                snippet = summary_tag.get_text(strip=True)

                                        knowledge["articles"].append({
                                            "title": title,
                                            "url": full_url,
                                            "snippet": snippet
                                        })
                                        seen_urls.add(full_url)

                        self.logger.info(f"Successfully extracted {len(knowledge['articles'])} articles.")
                    else:
                        self.logger.warning(f"Failed to fetch {url}, status code: {response.status}")
        except Exception as e:
            self.logger.error(f"Error scraping {url}: {e}")

        return {"google_models_research_knowledge": knowledge}
