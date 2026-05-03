import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_google_research():
    url = "https://blog.google/innovation-and-ai/models-and-research/"
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

    articles = []
    links = soup.find_all('a', href=True)
    seen_urls = set()

    for link in links:
        href = link['href']
        if '/innovation-and-ai/models-and-research/' in href and href != url:
            full_url = href if href.startswith('http') else f"https://blog.google{href}"
            if full_url not in seen_urls:
                title = link.get_text(strip=True)
                if title and len(title) > 10:
                    articles.append({
                        "title": title,
                        "url": full_url
                    })
                    seen_urls.add(full_url)

    # Save to JSON
    os.makedirs("data", exist_ok=True)
    json_path = "data/google_research.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=4, ensure_ascii=False)
    print(f"Saved JSON data to {json_path}")

    # Save to Markdown
    md_path = "google_research_report.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Google Models & Research Blog Updates\n\n")
        f.write(f"Scraped from [{url}]({url})\n\n")
        if not articles:
            f.write("No recent articles found.\n")
        else:
            for article in articles:
                f.write(f"### {article['title']}\n")
                f.write(f"- URL: {article['url']}\n\n")
    print(f"Saved Markdown report to {md_path}")

if __name__ == "__main__":
    scrape_google_research()
