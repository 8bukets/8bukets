import requests
from bs4 import BeautifulSoup
import json
import logging

logger = logging.getLogger("AIKnowledgeScraper")

def scrape_ai_agents_knowledge():
    url = "https://cloud.google.com/discover/what-are-ai-agents"
    logger.info(f"Fetching AI Agent knowledge from {url}...")
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Error fetching AI Agent knowledge: {e}")
        return False

    soup = BeautifulSoup(resp.content, "html.parser")
    headings = soup.find_all("h2")
    data = {}

    for header in headings:
        section_id = header.get("id")
        if not section_id:
            section_id = header.get_text(strip=True).lower().replace(" ", "-").replace("?", "")

        section_title = header.get_text(strip=True)
        content = []
        curr = header.find_next_sibling()

        while curr:
            if curr.name == "h2":
                break

            if curr.name == "pre":
                code = curr.get_text(strip=True)
                content.append(f"```\n{code}\n```")
            elif curr.name in ["h3", "h4"]:
                title = curr.get_text(strip=True)
                content.append(f"### {title}")
            elif curr.name == "ul":
                for li in curr.find_all("li", recursive=False):
                    content.append(f"- {li.get_text(strip=True)}")
            elif curr.name == "ol":
                for idx, li in enumerate(curr.find_all("li", recursive=False)):
                    content.append(f"{idx + 1}. {li.get_text(strip=True)}")
            elif curr.name == "table":
                rows = []
                for tr in curr.find_all("tr"):
                    cells = [th_td.get_text(strip=True) for th_td in tr.find_all(["th", "td"])]
                    rows.append(" | ".join(cells))
                content.append("\n".join(rows))
            else:
                text = curr.get_text(separator=' ', strip=True)
                if text:
                    content.append(text)

            curr = curr.find_next_sibling()

        data[section_id] = {
            "title": section_title,
            "content": "\n\n".join(content)
        }

    # Save to JSON
    json_path = "ai_agents_knowledge.json"
    try:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        logger.info(f"Saved AI Agent knowledge to {json_path}")

        # Save to Markdown for documentation reference
        md_path = "ai_agents_knowledge.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write("# What are AI Agents?\n\n")
            f.write(f"Scraped from [{url}]({url})\n\n")
            for section_id, section_data in data.items():
                f.write(f"## {section_data['title']}\n\n")
                f.write(f"{section_data['content']}\n\n")
        return True
    except Exception as e:
        logger.error(f"Failed to save AI Agent knowledge files: {e}")
        return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    scrape_ai_agents_knowledge()
