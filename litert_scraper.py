import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_litert_docs():
    url = "https://ai.google.dev/edge/litert/overview"
    print(f"Fetching {url}...")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return

    soup = BeautifulSoup(resp.content, "html.parser")

    # Since the structure might vary, let's look for headings and associate content under them.
    # In Google Dev site, main content is usually inside a <div class="devsite-article-body"> or <article>

    main_article = soup.find('article', class_='devsite-article') or soup.find('div', class_='devsite-article-body') or soup.find('main')

    if not main_article:
        print("Warning: Could not find main article container. Using full body.")
        main_article = soup.body

    data = {}

    # We want to find the Hardware Acceleration section and others
    # Headers are typically h2, h3

    current_section = "Overview"
    data[current_section] = {"title": current_section, "content": []}

    for element in main_article.find_all(['h2', 'h3', 'h4', 'p', 'ul', 'ol', 'pre']):
        if element.name in ['h2', 'h3']:
            # New section
            current_section = element.get_text(strip=True)
            # Remove any trailing anchor link text like "bookmark"
            if current_section.endswith('bookmark'):
                current_section = current_section[:-8].strip()

            data[current_section] = {
                "title": current_section,
                "content": []
            }
        elif element.name == 'h4':
            title = element.get_text(strip=True)
            if title.endswith('bookmark'):
                title = title[:-8].strip()
            data[current_section]["content"].append(f"### {title}")
        elif element.name == 'pre':
            code = element.get_text(strip=True)
            data[current_section]["content"].append(f"```\n{code}\n```")
        elif element.name in ['ul', 'ol']:
            for li in element.find_all('li', recursive=False):
                text = li.get_text(separator=' ', strip=True)
                data[current_section]["content"].append(f"- {text}")
        elif element.name == 'p':
            text = element.get_text(separator=' ', strip=True)
            if text:
                data[current_section]["content"].append(text)

    # Clean up empty sections
    cleaned_data = {}
    for k, v in data.items():
        if v["content"]:
            cleaned_data[k] = {
                "title": v["title"],
                "content": "\n\n".join(v["content"])
            }

    # Save to JSON
    json_path = "litert_docs.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(cleaned_data, f, indent=4, ensure_ascii=False)
    print(f"Saved JSON data to {json_path}")

    # Save to Markdown
    md_path = "litert_docs.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# LiteRT Overview Documentation\n\n")
        f.write(f"Scraped from [{url}]({url})\n\n")
        for section_id, section_data in cleaned_data.items():
            f.write(f"## {section_data['title']}\n\n")
            f.write(f"{section_data['content']}\n\n")
    print(f"Saved Markdown data to {md_path}")

if __name__ == "__main__":
    scrape_litert_docs()
