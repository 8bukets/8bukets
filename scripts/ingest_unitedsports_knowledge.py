import requests
from bs4 import BeautifulSoup
import json
import os
import time
from datetime import datetime, UTC

def scrape_unitedsports():
    base_url = "https://unitedsports.news.blog/"
    print(f"🚀 [Scraper] Starting comprehensive ingestion from {base_url}...")

    posts = []
    page = 1
    max_pages = 5

    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    })

    while page <= max_pages:
        url = base_url if page == 1 else f"{base_url}page/{page}/"
        print(f" 📑 Scraping page {page}: {url}")

        retries = 3
        success = False
        while retries > 0:
            try:
                response = session.get(url, timeout=15)
                if response.status_code == 429:
                    print(f" ⏳ Rate limited. Retrying in 10s... ({retries} retries left)")
                    time.sleep(10)
                    retries -= 1
                    continue

                if response.status_code == 404:
                    print(f" ⏹️ Page {page} not found. Reached end of blog.")
                    return posts

                response.raise_for_status()
                success = True
                break
            except Exception as e:
                print(f" ⚠️ Error scraping page {page}: {e}")
                retries -= 1
                time.sleep(2)

        if not success:
            print(f" ❌ Failed to scrape page {page} after retries.")
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article')
        if not articles:
            print(f" ⏹️ No articles found on page {page}. Stopping.")
            break

        for article in articles:
            title_tag = article.find(['h1', 'h2', 'h3'], class_='entry-title')
            if not title_tag:
                continue

            title = title_tag.get_text(strip=True)
            link = title_tag.find('a')['href'] if title_tag.find('a') else url

            # For this theme, content might be in entry-summary or entry-content
            content_tag = article.find('div', class_='entry-summary') or article.find('div', class_='entry-content')

            links = [a['href'] for a in content_tag.find_all('a', href=True)] if content_tag else []
            text_content = content_tag.get_text(separator='\n', strip=True) if content_tag else ""

            combined_content = text_content
            if links:
                # Deduplicate links and add them if they are not just the text content itself
                unique_links = list(dict.fromkeys(links))
                link_str = ", ".join(unique_links)
                if link_str not in combined_content:
                    combined_content += "\nLinks: " + link_str

            if not any(p['link'] == link for p in posts):
                posts.append({
                    "title": title,
                    "link": link,
                    "content": combined_content
                })

        page += 1
        time.sleep(2)

    return posts

if __name__ == "__main__":
    posts = scrape_unitedsports()

    if not posts:
        print("⚠️ [Scraper] No posts scraped. Aborting save to prevent data loss.")
        import sys
        sys.exit(0)

    sections = []
    for post in posts:
        sections.append({
            "header": post["title"],
            "content": post["content"]
        })

    result = {
        "source": "https://unitedsports.news.blog/",
        "title": "e&n - unitedsports",
        "description": "Integrated market intelligence from unitedsports.news.blog",
        "analyzedAt": datetime.now(UTC).isoformat().replace('+00:00', 'Z'),
        "sections": sections,
        "signature": "All the best - https://unitedsports.news.blog/"
    }

    output_dir = os.path.join(os.getcwd(), 'data/knowledge')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'unitedsports_knowledge.json')

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"✅ [Scraper] Successfully scraped {len(posts)} posts and saved to {output_path}")
