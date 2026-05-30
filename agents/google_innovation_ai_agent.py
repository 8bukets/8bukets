import aiohttp
from bs4 import BeautifulSoup
from agents.base_agent import BaseAgent, Blackboard

class GoogleInnovationAIAgent(BaseAgent):
    """
    Scrapes https://blog.google/innovation-and-ai/
    and adds the latest innovation and AI knowledge to the Blackboard.
    """
    def __init__(self):
        super().__init__("GoogleInnovationAIAgent", dependencies=[], provides=["google_innovation_ai_knowledge"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        url = "https://blog.google/innovation-and-ai/"
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

                        links = soup.find_all('a', href=True)
                        seen_urls = set()

                        for link in links:
                            href = link['href']
                            # Filter for internal blog posts in innovation-and-ai
                            if '/innovation-and-ai/' in href and href != url and not href.endswith('/innovation-and-ai/'):
                                full_url = href if href.startswith('http') else f"https://blog.google{href}"
                                if full_url not in seen_urls:
                                    title = link.get_text(strip=True)
                                    # Basic heuristic to avoid menu links or short fragments
                                    if title and len(title) > 20:
                                        # Attempt to find a summary in a neighboring tag or parent
                                        snippet = ""
                                        parent = link.find_parent(['div', 'section', 'li', 'article'])
                                        if parent:
                                            summary_tag = parent.find(['p', 'span', 'div'], class_=lambda x: x and ('summary' in x.lower() or 'description' in x.lower() or 'snippet' in x.lower() or 'deck' in x.lower()))
                                            if summary_tag:
                                                snippet = summary_tag.get_text(strip=True)

                                        knowledge["articles"].append({
                                            "title": title,
                                            "url": full_url,
                                            "snippet": snippet
                                        })
                                        seen_urls.add(full_url)

                        self.logger.info(f"Successfully extracted {len(knowledge['articles'])} articles from Innovation & AI.")
                    else:
                        self.logger.warning(f"Failed to fetch {url}, status code: {response.status}")
        except Exception as e:
            self.logger.error(f"Error scraping {url}: {e}")

        return {"google_innovation_ai_knowledge": knowledge}
