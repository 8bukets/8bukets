import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_google_blog(url, category_path):
    print(f"Fetching {url}...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return []

    soup = BeautifulSoup(resp.content, "html.parser")

    articles = []
    links = soup.find_all('a', href=True)
    seen_urls = set()

    for link in links:
        href = link['href']
        if category_path in href and href != url and not href.endswith(category_path):
            full_url = href if href.startswith('http') else f"https://blog.google{href}"
            if full_url not in seen_urls:
                title = link.get_text(strip=True)
                if title and len(title) > 20:
                    snippet = ""
                    parent = link.find_parent(['div', 'section', 'li', 'article'])
                    if parent:
                        summary_tag = parent.find(['p', 'span', 'div'], class_=lambda x: x and ('summary' in x.lower() or 'description' in x.lower() or 'snippet' in x.lower() or 'deck' in x.lower()))
                        if summary_tag:
                            snippet = summary_tag.get_text(strip=True)

                    articles.append({
                        "title": title,
                        "url": full_url,
                        "snippet": snippet
                    })
                    seen_urls.add(full_url)
    return articles

def run_scrapers():
    # 1. Models & Research
    research_url = "https://blog.google/innovation-and-ai/models-and-research/"
    research_articles = scrape_google_blog(research_url, "/innovation-and-ai/models-and-research/")

    # 2. Innovation & AI
    innovation_url = "https://blog.google/innovation-and-ai/"
    innovation_articles = scrape_google_blog(innovation_url, "/innovation-and-ai/")

    all_articles = research_articles + innovation_articles

    # Load existing data to merge
    json_path = "data/google_innovation_ai.json"
    existing_articles = []
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                existing_articles = json.load(f)
        except Exception as e:
            print(f"Error reading existing JSON: {e}")

    # Deduplicate by URL
    combined_articles = existing_articles + all_articles
    unique_articles = []
    seen_urls = set()
    for art in combined_articles:
        if art['url'] not in seen_urls:
            unique_articles.append(art)
            seen_urls.add(art['url'])

    # Save to JSON
    os.makedirs("data", exist_ok=True)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(unique_articles, f, indent=4, ensure_ascii=False)
    print(f"Saved JSON data to {json_path}")

    # Save to Markdown
    md_path = "google_innovation_ai_report.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Google Innovation & AI Blog Updates\n\n")
        f.write(f"Scraped from [{innovation_url}]({innovation_url}) and [{research_url}]({research_url})\n\n")
        if not unique_articles:
            f.write("No recent articles found.\n")
        else:
            for article in unique_articles:
                f.write(f"### {article['title']}\n")
                f.write(f"- URL: {article['url']}\n")
                if article.get('snippet'):
                    f.write(f"- Summary: {article['snippet']}\n")
                f.write("\n")
    print(f"Saved Markdown report to {md_path}")

if __name__ == "__main__":
    run_scrapers()
