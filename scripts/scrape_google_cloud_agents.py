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

    # List of keywords/titles we expect to find as headers or important sections
    targets = [
        "What is an AI agent?",
        "Key features of an AI agent",
        "What is the difference between AI agents, AI assistants, and bots?",
        "Key differences",
        "How do AI agents work?",
        "What are the types of agents in AI?",
        "Based on interaction",
        "Based on number of agents",
        "Benefits of using AI agents",
        "Efficiency and productivity",
        "Improved decision-making",
        "Enhanced capabilities",
        "Social interaction and simulation",
        "Challenges with using AI agents",
        "Deploy AI agents for scale and efficiency with Cloud Run",
        "Use cases for AI agents",
        "Customer agents",
        "Employee agents",
        "Creative agents",
        "Data agents",
        "Code agents",
        "Security agents",
        "Google Cloud and AI agents"
    ]

    # Try finding headers
    headers = article.find_all(['h1', 'h2', 'h3', 'h4'])
    print(f"Found {len(headers)} headers.")

    for header in headers:
        title = clean_text(header.get_text())

        match_key = None
        for target in targets:
            if target.lower() in title.lower():
                match_key = target.lower().replace(" ", "-").replace("?", "").replace(",", "")
                target_title = target
                break

        if not match_key:
            continue

        content = []
        curr = header.find_next_sibling()

        count = 0
        while curr and count < 50 and curr.name not in ['h1', 'h2', 'h3', 'h4']:
            if curr.name == 'p':
                text = clean_text(curr.get_text())
                if text: content.append(text)
            elif curr.name in ['ul', 'ol']:
                for li in curr.find_all('li'):
                    text = clean_text(li.get_text())
                    if text: content.append(f"- {text}")
            elif curr.name == 'table':
                for tr in curr.find_all('tr'):
                    cells = [clean_text(td.get_text()) for td in tr.find_all(['th', 'td'])]
                    if cells:
                        content.append(" | ".join(cells))
            elif curr.name == 'div':
                # Sometimes content is wrapped in divs
                text = clean_text(curr.get_text(separator=' ', strip=True))
                if text and len(text) > 10 and not any(h in curr.name for h in ['h1', 'h2', 'h3']):
                    content.append(text)

            curr = curr.find_next_sibling()
            count += 1

        if content:
            if match_key in knowledge:
                knowledge[match_key]["content"] += "\n\n" + "\n\n".join(content)
            else:
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
    output_path = "data/knowledge/scraped_google_agents.json"
    os.makedirs("data/knowledge", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(knowledge, f, indent=4, ensure_ascii=False)

    print(f"Scraped {len(knowledge)} sections to {output_path}")

if __name__ == "__main__":
    scrape_google_cloud_agents()
