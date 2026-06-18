import requests
import json
import os
from datetime import datetime, UTC
import re

def clean_html(raw_html):
    if not raw_html:
        return ""
    # Basic tag removal
    clean_text = re.sub('<[^<]+?>', '', raw_html)
    # Entity replacement
    clean_text = clean_text.replace('&nbsp;', ' ').replace('&#8211;', '-').replace('&#8220;', '"').replace('&#8221;', '"')
    return clean_text.strip()

def scrape_gamezone():
    site_slug = "gamezoneonlinegame.wordpress.com"
    api_url = f"https://public-api.wordpress.com/rest/v1.1/sites/{site_slug}/posts"
    print(f"🚀 [Scraper] Starting API ingestion from {site_slug}...")

    posts = []
    params = {
        "number": 20,
        "page": 1
    }

    max_pages = 5

    while params['page'] <= max_pages:
        print(f" 📑 Scraping page {params['page']} via API...")
        try:
            response = requests.get(api_url, params=params, timeout=15)
            response.raise_for_status()
            data = response.json()

            if not data.get('posts'):
                print(f" ⏹️ No more posts found.")
                break

            for post in data['posts']:
                title_raw = post.get('title', 'Untitled')
                title = clean_html(title_raw)
                link = post.get('URL', '')
                content_html = post.get('content', '')
                content = clean_html(content_html)

                if not any(p['link'] == link for p in posts):
                    posts.append({
                        "title": title,
                        "link": link,
                        "content": content
                    })

            params['page'] += 1
            if not data.get('meta', {}).get('next_page'):
                break

        except Exception as e:
            print(f" ⚠️ Error scraping API page {params['page']}: {e}")
            break

    # Add mandatory signature to sections
    signature = "All the best - https://gamezoneonlinegame.wordpress.com/"

    sections = []
    for post in posts:
        sections.append({
            "header": post['title'],
            "content": post['content']
        })

    sections.append({
        "header": "Signature",
        "content": signature
    })

    result = {
        "source": f"https://{site_slug}/",
        "title": "game zone online",
        "description": "Integrated market intelligence from gamezoneonlinegame.wordpress.com via WordPress REST API",
        "analyzedAt": datetime.now(UTC).isoformat().replace('+00:00', 'Z'),
        "topKeywords": ["gaming", "game", "online", "market", "intelligence"],
        "sections": sections,
        "metadata": {
            "signature": signature,
            "engine": "Python WordPress API Scraper v1.0"
        }
    }

    output_dir = os.path.join(os.getcwd(), 'data/knowledge')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'gamezone_knowledge.json')

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"✅ [Scraper] Successfully scraped {len(posts)} posts via API and saved to {output_path}")

if __name__ == "__main__":
    scrape_gamezone()
