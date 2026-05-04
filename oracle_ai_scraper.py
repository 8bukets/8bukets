import aiohttp
import asyncio
from bs4 import BeautifulSoup
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

URL = "https://www.oracle.com/artificial-intelligence/"

async def fetch_page(session, url):
    try:
        async with session.get(url, timeout=30) as response:
            if response.status == 200:
                return await response.text()
            else:
                logger.error(f"Failed to fetch {url}, status code: {response.status}")
                return None
    except Exception as e:
        logger.error(f"Error fetching {url}: {e}")
        return None

def clean_text(text):
    if not text:
        return ""
    return " ".join(text.split())

async def scrape_oracle_ai():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        html = await fetch_page(session, URL)

        if not html:
            logger.error("No HTML content fetched.")
            return

        soup = BeautifulSoup(html, 'html.parser')

        # Extract headings and paragraphs
        sections = []
        for element in soup.find_all(['h1', 'h2', 'h3', 'p']):
            text = clean_text(element.get_text())
            if text:
                sections.append({
                    "tag": element.name,
                    "content": text
                })

        # Extract key links
        links = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            text = clean_text(a.get_text())
            if text and ("ai" in href.lower() or "artificial-intelligence" in href.lower() or "machine-learning" in href.lower()):
                if href.startswith("/"):
                    href = "https://www.oracle.com" + href

                # Check if it's an Oracle link
                if "oracle.com" in href:
                    links.append({
                        "text": text,
                        "url": href
                    })

        # Deduplicate links
        unique_links = []
        seen_urls = set()
        for link in links:
            if link['url'] not in seen_urls:
                seen_urls.add(link['url'])
                unique_links.append(link)

        data = {
            "source_url": URL,
            "sections": sections,
            "key_links": unique_links
        }

        # Save as JSON
        with open('oracle_ai_docs.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        logger.info("Saved data to oracle_ai_docs.json")

        # Save as Markdown
        with open('oracle_ai_docs.md', 'w', encoding='utf-8') as f:
            f.write(f"# Oracle AI Documentation\n\n")
            f.write(f"Source: {URL}\n\n")

            f.write("## Sections\n\n")
            for section in sections:
                if section['tag'] in ['h1', 'h2', 'h3']:
                    f.write(f"\n### {section['content']}\n\n")
                else:
                    f.write(f"{section['content']}\n\n")

            f.write("## Key Links\n\n")
            for link in unique_links:
                f.write(f"- [{link['text']}]({link['url']})\n")

        logger.info("Saved data to oracle_ai_docs.md")

if __name__ == "__main__":
    asyncio.run(scrape_oracle_ai())
