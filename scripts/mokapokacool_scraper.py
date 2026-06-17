import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

def scrape_moka_poka():
    url = "https://mokapokacool.art.blog/"
    print(f"🚀 [Scraper] Starting ingestion from {url}...")

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ [Scraper] Failed to fetch {url}: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('article')
    knowledge_data = []
    md_output = "# Mokapokacool Market Intelligence\n\n"

    for article in articles:
        title_tag = article.find('h1', class_='entry-title') or article.find('h2', class_='entry-title')
        if not title_tag:
            continue

        title = title_tag.get_text().strip()
        link = title_tag.find('a')['href'] if title_tag.find('a') else "N/A"

        date_tag = article.find('time', class_='entry-date')
        date = date_tag.get_text().strip() if date_tag else "Unknown Date"

        categories = [cat.get_text().strip() for cat in article.find_all('a', rel='category tag')]

        # Extract external links from the content
        content_div = article.find('div', class_='entry-content')
        external_links = []
        if content_div:
            external_links = [a['href'] for a in content_div.find_all('a') if a.get('href') and not a['href'].startswith(url)]

        entry = {
            "title": title,
            "date": date,
            "url": link,
            "categories": categories,
            "external_links": external_links
        }
        knowledge_data.append(entry)

        md_output += f"## {title}\n"
        md_output += f"- **Date**: {date}\n"
        md_output += f"- **Categories**: {', '.join(categories)}\n"
        md_output += f"- **Primary Link**: {link}\n"
        if external_links:
            md_output += "- **External References**:\n"
            for ext in external_links:
                md_output += f"  - {ext}\n"
        md_output += "\n"

    # Ensure data directory exists
    os.makedirs('data/knowledge', exist_ok=True)

    # Save JSON
    with open('data/knowledge/mokapokacool.json', 'w', encoding='utf-8') as f:
        json.dump(knowledge_data, f, indent=2, ensure_ascii=False)

    # Save MD
    with open('data/knowledge/mokapokacool.md', 'w', encoding='utf-8') as f:
        f.write(md_output)

    print(f"✅ [Scraper] Ingested {len(knowledge_data)} articles.")
    return knowledge_data

if __name__ == "__main__":
    scrape_moka_poka()
