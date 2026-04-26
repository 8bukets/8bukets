import aiohttp
from bs4 import BeautifulSoup
from agents.base_agent import BaseAgent, Blackboard

class GoogleEdgeAgent(BaseAgent):
    """
    Scrapes https://ai.google.dev/edge and adds its findings to the Blackboard.
    """
    def __init__(self):
        super().__init__("GoogleEdgeAgent", dependencies=[], provides=["google_edge_knowledge"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Scraping knowledge from https://ai.google.dev/edge...")
<<<<<<< HEAD

=======

>>>>>>> origin/add-google-edge-agent-9371392929328195231
        url = "https://ai.google.dev/edge"
        knowledge = {
            "source": url,
            "title": "",
            "sections": []
        }
<<<<<<< HEAD

=======

>>>>>>> origin/add-google-edge-agent-9371392929328195231
        try:
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=15)) as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        html = await response.text()
                        soup = BeautifulSoup(html, "html.parser")
<<<<<<< HEAD

                        title_tag = soup.find("title")
                        if title_tag:
                            knowledge["title"] = title_tag.get_text(strip=True)

=======

                        title_tag = soup.find("title")
                        if title_tag:
                            knowledge["title"] = title_tag.get_text(strip=True)

>>>>>>> origin/add-google-edge-agent-9371392929328195231
                        # Extract main headings and paragraphs
                        for header in soup.find_all(['h1', 'h2', 'h3']):
                            section_title = header.get_text(strip=True)
                            if not section_title:
                                continue
<<<<<<< HEAD

=======

>>>>>>> origin/add-google-edge-agent-9371392929328195231
                            section_content = []
                            curr = header.find_next_sibling()
                            while curr and curr.name not in ['h1', 'h2', 'h3']:
                                if curr.name in ['p', 'li', 'span', 'div'] and curr.get_text(strip=True):
                                    text = curr.get_text(separator=' ', strip=True)
                                    if len(text) > 20:  # Skip very short fragments
                                        section_content.append(text)
                                curr = curr.find_next_sibling()
<<<<<<< HEAD

=======

>>>>>>> origin/add-google-edge-agent-9371392929328195231
                            if section_content:
                                knowledge["sections"].append({
                                    "heading": section_title,
                                    "content": " ".join(section_content)
                                })
<<<<<<< HEAD

=======

>>>>>>> origin/add-google-edge-agent-9371392929328195231
                        self.logger.info(f"Successfully extracted {len(knowledge['sections'])} sections of knowledge.")
                    else:
                        self.logger.warning(f"Failed to fetch {url}, status code: {response.status}")
        except Exception as e:
            self.logger.error(f"Error scraping {url}: {e}")
<<<<<<< HEAD

=======

>>>>>>> origin/add-google-edge-agent-9371392929328195231
        return {"google_edge_knowledge": knowledge}
