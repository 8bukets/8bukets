import requests
from bs4 import BeautifulSoup
import json
import os
import re

def clean_text(text):
    if not text: return ""
    return " ".join(text.split())

def scrape_google_cloud_agents():
    url = "https://cloud.google.com/discover/what-are-ai-agents"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    print(f"Fetching knowledge from {url}...")
    try:
        resp = requests.get(url, headers=headers, timeout=20)
        resp.raise_for_status()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return

    soup = BeautifulSoup(resp.content, "html.parser")

    # Target common content containers for Google Cloud docs
    article = soup.find('article') or soup.find('main') or soup.find('div', class_='cloud-content') or soup.body

    knowledge = {}

    # Improve scraping by looking for specific sections even if they are not direct siblings
    target_mapping = {
        "What is an AI agent?": ["what-is-an-ai-agent"],
        "Key features of an AI agent": ["key-features-of-an-ai-agent"],
        "What is the difference between AI agents, AI assistants, and bots?": ["ai-agents-vs-assistants-vs-bots"],
        "Key differences": ["key-differences"],
        "How do AI agents work?": ["how-ai-agents-work"],
        "What are the types of agents in AI?": ["types-of-ai-agents"],
        "Based on interaction": ["based-on-interaction"],
        "Based on number of agents": ["based-on-number-of-agents"],
        "Benefits of using AI agents": ["benefits-of-ai-agents"],
        "Efficiency and productivity": ["efficiency-and-productivity"],
        "Improved decision-making": ["improved-decision-making"],
        "Enhanced capabilities": ["enhanced-capabilities"],
        "Social interaction and simulation": ["social-interaction-and-simulation"],
        "Challenges with using AI agents": ["challenges-of-ai-agents"],
        "Deploy AI agents for scale and efficiency with Cloud Run": ["deploying-ai-agents-cloud-run"],
        "Use cases for AI agents": ["use-cases-for-ai-agents"],
        "Customer agents": ["customer-agents"],
        "Employee agents": ["employee-agents"],
        "Creative agents": ["creative-agents"],
        "Data agents": ["data-agents"],
        "Code agents": ["code-agents"],
        "Security agents": ["security-agents"],
        "Google Cloud and AI agents": ["google-cloud-ai-agent-portfolio", "google-cloud-and-ai-agents"]
    }

    # Try finding headers
    headers = article.find_all(['h1', 'h2', 'h3', 'h4'])
    print(f"Found {len(headers)} headers.")

    for header in headers:
        title = clean_text(header.get_text())

        target_keys = []
        target_title = ""
        for target, keys in target_mapping.items():
            if target.lower() in title.lower():
                target_keys = keys
                target_title = target
                break

        if not target_keys:
            continue

        content = []

        # Look ahead for content until the next header
        curr = header.next_element
        while curr:
            if curr == article: break
            if isinstance(curr, str):
                curr = curr.next_element
                continue
            if curr.name in ['h1', 'h2', 'h3', 'h4'] and curr != header:
                break

            if curr.name == 'p':
                text = clean_text(curr.get_text())
                if text and text not in content: content.append(text)
            elif curr.name in ['ul', 'ol']:
                items = []
                for li in curr.find_all('li'):
                    # Improved list item parsing to handle nested elements and preserve separators
                    item_parts = []
                    for child in li.children:
                        if child.name == 'a':
                            item_parts.append(clean_text(child.get_text()))
                        elif isinstance(child, str):
                            item_parts.append(child.strip())
                        else:
                            item_parts.append(clean_text(child.get_text()))

                    text = " ".join(filter(None, item_parts))
                    # Handle common "TitleDescription" joined cases by ensuring colon after known prefixes if missing
                    if "Gemini" in text and ":" not in text:
                        text = re.sub(r'(Gemini [^ ]+)', r'\1:', text, 1)

                    # Fix specific known joined words in the portfolio
                    text = text.replace("AppSecure", "App: Secure")
                    text = text.replace("PlatformCreate", "Platform: Create")
                    text = text.replace("StudioBuild", "Studio: Build")
                    text = text.replace("GardenCurated", "Garden: Curated")
                    text = text.replace("(ADK)Open-source", "(ADK): Open-source")
                    text = text.replace("ProtocolAn", "Protocol: An")
                    text = text.replace("RunA", "Run: A")

                    if text: items.append(f"- {text}")
                if items:
                    joined_items = "\n".join(items)
                    if joined_items not in content: content.append(joined_items)
            elif curr.name == 'table':
                rows = []
                for tr in curr.find_all('tr'):
                    cells = [clean_text(td.get_text()) for td in tr.find_all(['th', 'td'])]
                    if cells:
                        rows.append(" | " + " | ".join(cells) + " |")
                if rows:
                    if len(rows) > 0:
                        num_cols = len(rows[0].split(" | ")) - 2
                        separator = " | " + " | ".join(["---"] * num_cols) + " |"
                        rows.insert(1, separator)
                    table_str = "\n".join(rows)
                    if table_str not in content: content.append(table_str)

            curr = curr.next_element

        if content:
            for match_key in target_keys:
                # Always overwrite or cleanly merge to avoid duplicate bloat within the same run
                knowledge[match_key] = {
                    "title": target_title,
                    "content": "\n\n".join(content)
                }

    # If we found nothing, maybe the site uses different structure or is dynamic
    if not knowledge:
        print("Standard header-based scraping failed. Attempting deep text search...")
        text = article.get_text(separator='\n', strip=True)
        # This is a fallback to at least get some text if the structure is weird
        knowledge["full-text-fallback"] = {
            "title": "What are AI Agents? (Full Text)",
            "content": text[:5000] # Cap it
        }

    # Save to temporary file
    output_dir = "data/knowledge"
    output_path = os.path.join(output_dir, "scraped_google_agents.json")
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(knowledge, f, indent=4, ensure_ascii=False)

    print(f"Scraped {len(knowledge)} sections to {output_path}")

if __name__ == "__main__":
    scrape_google_cloud_agents()
