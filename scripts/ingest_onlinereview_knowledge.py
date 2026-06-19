import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime, UTC

def scrape_onlinereview():
    url = "https://onlinereview.news.blog/"
    print(f"🚀 [Scraper] Scraping {url}...")

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string.strip() if soup.title else "Online Review News"

        sections = []
        articles = soup.find_all('article')

        if not articles:
            articles = soup.find_all(class_='post') or soup.find_all(class_='entry-content')

        if articles:
            for article in articles:
                header_elem = article.find(['h1', 'h2', 'h3', 'h4'], class_='entry-title')
                if not header_elem:
                    header_elem = article.find(['h1', 'h2', 'h3', 'h4'])

                header_text = header_elem.get_text(strip=True) if header_elem else "Blog Post"

                content_elem = article.find(class_='entry-content') or article
                content_text = content_elem.get_text(separator='\n', strip=True)

                if header_text and content_text:
                    sections.append({
                        "header": header_text,
                        "content": content_text
                    })
        else:
            # Fallback
            content_div = soup.find('main') or soup.find(id='content') or soup.find('body')
            if content_div:
                sections.append({
                    "header": "Main Content",
                    "content": content_div.get_text(separator='\n', strip=True)
                })

        # Add the specific signature as required
        signature = "All the best - https://onlinereview.news.blog/"
        sections.append({
            "header": "Signature",
            "content": signature
        })

        data = {
            "source": url,
            "title": title,
            "description": "Market intelligence and news reviews extracted from onlinereview.news.blog.",
            "topKeywords": ["news", "review", "online", "market", "intelligence"],
            "analyzedAt": datetime.now(UTC).isoformat().replace('+00:00', 'Z'),
            "sections": sections,
            "metadata": {
                "signature": signature,
                "engine": "Python BeautifulSoup Scraper v1.0"
            }
        }

        output_dir = "data/knowledge"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "onlinereview_knowledge.json")

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"✅ [Scraper] Successfully saved {len(sections)} sections of knowledge to {output_path}")
        return data

    except Exception as e:
        print(f"❌ [Scraper] Failed to scrape {url}: {e}")
        return None

if __name__ == "__main__":
    scrape_onlinereview()
