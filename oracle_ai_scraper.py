import aiohttp
import asyncio
from bs4 import BeautifulSoup
import json
import logging
import argparse


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

URL = "https://www.oracle.com/artificial-intelligence/"

class OracleAIScraper:
    def __init__(self, output_json: str, output_md: str):
        self.output_json = output_json
        self.output_md = output_md
        self.url = URL

    def clean_text(self, text: str) -> str:
        """Normalize whitespace and remove non-breaking spaces."""
        if not text:
            return ""
        text = text.replace('\xa0', ' ')
        return " ".join(text.split()).strip()

    async def fetch_page(self, session: aiohttp.ClientSession, url: str) -> str:
        try:
            timeout = aiohttp.ClientTimeout(total=30)
            async with session.get(url, timeout=timeout) as response:
                response.raise_for_status()
                return await response.text()
        except Exception as e:
            logger.error(f"Error fetching {url}: {e}")
            return None

    async def parse_page(self, html: str) -> dict:
        soup = BeautifulSoup(html, 'html.parser')

        # We will extract structure based on headers, paragraphs, and list items.
        data = {
            "title": "Oracle Artificial Intelligence",
            "sections": []
        }

        # Try extracting main content body to avoid nav bars, footers
        # Typical Oracle structure might have a main container
        main_content = soup.find('main') or soup.find(id='maincontent') or soup

        # Extract headings and following paragraphs/lists
        headings = main_content.find_all(['h1', 'h2', 'h3'])

        for heading in headings:
            section_title = self.clean_text(heading.get_text())
            if not section_title:
                continue

            section_content = []

            # Get next siblings until next heading
            nxt = heading.next_sibling
            while nxt:
                if nxt.name in ['h1', 'h2', 'h3']:
                    break

                if nxt.name in ['p', 'div']:
                    text = self.clean_text(nxt.get_text())
                    if text:
                        section_content.append(text)
                elif nxt.name in ['ul', 'ol']:
                    items = [self.clean_text(li.get_text()) for li in nxt.find_all('li')]
                    if items:
                        section_content.append({"list": items})

                nxt = nxt.next_sibling

            if section_content:
                data["sections"].append({
                    "heading": section_title,
                    "content": section_content
                })

        return data

    async def scrape(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            logger.info(f"Fetching {self.url}...")
            html = await self.fetch_page(session, self.url)
            if html:
                data = await self.parse_page(html)
                logger.info(f"Extracted {len(data['sections'])} sections.")
                self.save_data(data)
            else:
                logger.error("Failed to fetch page.")

    def save_data(self, data: dict):
        # Save JSON
        try:
            with open(self.output_json, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            logger.info(f"Saved data to {self.output_json}")
        except IOError as e:
            logger.error(f"Failed to save JSON: {e}")

        # Save MD
        try:
            with open(self.output_md, 'w', encoding='utf-8') as f:
                f.write(f"# {data['title']}\n\n")
                f.write(f"Source: {self.url}\n\n")

                for section in data['sections']:
                    f.write(f"## {section['heading']}\n\n")
                    for item in section['content']:
                        if isinstance(item, str):
                            f.write(f"{item}\n\n")
                        elif isinstance(item, dict) and "list" in item:
                            for li in item["list"]:
                                f.write(f"- {li}\n")
                            f.write("\n")
            logger.info(f"Saved data to {self.output_md}")
        except IOError as e:
            logger.error(f"Failed to save Markdown: {e}")

def main():
    parser = argparse.ArgumentParser(description="Scraper for Oracle AI Knowledge")
    parser.add_argument("--json", default="oracle_ai_docs.json", help="Output JSON filename")
    parser.add_argument("--md", default="oracle_ai_docs.md", help="Output Markdown filename")

    args = parser.parse_args()

    scraper = OracleAIScraper(
        output_json=args.json,
        output_md=args.md
    )

    asyncio.run(scraper.scrape())

if __name__ == "__main__":
    main()
