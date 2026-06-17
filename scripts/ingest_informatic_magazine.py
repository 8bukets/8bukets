import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime, UTC

def scrape_informatic_magazine():
    base_url = "https://informaticmagazine.data.blog/"
    print(f"🚀 [Scraper] Starting comprehensive ingestion from {base_url}...")

    posts = []
    page = 1
    max_pages = 5 # Limit to 5 pages for a good balance of depth and performance

    while page <= max_pages:
        url = base_url if page == 1 else f"{base_url}page/{page}/"
        print(f" 📑 Scraping page {page}: {url}")

        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 404:
                print(f" ⏹️ Page {page} not found. Reached end of blog.")
                break
            response.raise_for_status()

            # Using html.parser for better portability as suggested in review
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

                content_tag = article.find('div', class_='entry-content')
                content = content_tag.get_text(separator='\n', strip=True) if content_tag else ""

                # Basic cleanup
                content = content.replace('IFRAME:', '').strip()

                # Deduplicate by link
                if not any(p['link'] == link for p in posts):
                    posts.append({
                        "title": title,
                        "link": link,
                        "content": content
                    })

            page += 1

        except Exception as e:
            print(f" ⚠️ Error scraping page {page}: {e}")
            break

    result = {
        "source": base_url,
        "title": "informatic online",
        "description": "Integrated market intelligence from informaticmagazine.data.blog",
        "analyzedAt": datetime.now(UTC).isoformat().replace('+00:00', 'Z'),
        "posts": posts,
        "signature": "All the best - https://informaticmagazine.data.blog/"
    }

    output_dir = os.path.join(os.getcwd(), 'data/knowledge')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'informatic_magazine.json')

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"✅ [Scraper] Successfully scraped {len(posts)} posts across {page-1} pages and saved to {output_path}")

if __name__ == "__main__":
    scrape_informatic_magazine()
