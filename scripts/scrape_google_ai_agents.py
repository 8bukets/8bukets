import requests
from bs4 import BeautifulSoup
import json
import os
import datetime

def scrape():
    url = "https://cloud.google.com/discover/what-are-ai-agents"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.content, 'lxml')

    title = soup.find('h1').get_text(strip=True) if soup.find('h1') else "What is an AI agent?"

    sections = []
    for header_tag in soup.find_all(['h2', 'h3']):
        header_text = header_tag.get_text(strip=True)
        if not header_text or len(header_text) < 3: continue

        content = []
        curr = header_tag.find_next_sibling()
        while curr and curr.name not in ['h1', 'h2', 'h3']:
            txt = curr.get_text(separator=' ', strip=True)
            if txt:
                content.append(txt)
            curr = curr.find_next_sibling()

        if content:
            sections.append({
                "header": header_text,
                "content": "\n\n".join(content)
            })

    result = {
        "title": title,
        "source": url,
        "sections": sections,
        "analyzedAt": datetime.datetime.now().isoformat()
    }

    os.makedirs('scratch', exist_ok=True)
    with open('scratch/scraped_ai_agents.json', 'w') as f:
        json.dump(result, f, indent=4)
    print(f"Scraped {len(sections)} sections successfully to scratch/scraped_ai_agents.json")

if __name__ == "__main__":
    scrape()
