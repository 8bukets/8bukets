import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime, UTC

def scrape_infogadgettech():
    url = "https://infogadgettech.wordpress.com/"
    print(f"🚀 [Scraper] Scraping {url}...")

    try:
        # Using a browser-like User-Agent to avoid blocks
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"macOS"',
            'Upgrade-Insecure-Requests': '1'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.title.string.strip() if soup.title else "gadget"

        sections = []

        # WordPress blogs often have articles
        articles = soup.find_all('article')

        if not articles:
            articles = soup.find_all(class_='post') or soup.find_all(class_='entry-content')

        if articles:
            for article in articles:
                header_elem = article.find(['h1', 'h2', 'h3', 'h4'], class_='entry-title') or article.find(['h1', 'h2', 'h3', 'h4'])
                header_text = header_elem.get_text(strip=True) if header_elem else "Blog Post"

                content_elem = article.find(class_='entry-content') or article
                content_text = content_elem.get_text(separator='\n', strip=True)

                if header_text and content_text:
                    # Clean up some noise
                    content_text = content_text.replace('IFRAME:', '').strip()

                    sections.append({
                        "header": header_text,
                        "content": content_text
                    })
        else:
            content_div = soup.find('main') or soup.find(id='content') or soup.find('body')
            if content_div:
                sections.append({
                    "header": "Main Content",
                    "content": content_div.get_text(separator='\n', strip=True)
                })

        # Add the specific signature as required
        signature = "All the best - https://infogadgettech.wordpress.com/"
        sections.append({
            "header": "Signature",
            "content": signature
        })

        data = {
            "source": url,
            "title": title,
            "description": f"Market intelligence and gadget tech updates extracted from {url}.",
            "analyzedAt": datetime.now(UTC).isoformat().replace('+00:00', 'Z'),
            "sections": sections,
            "metadata": {
                "signature": signature,
                "engine": "Python BeautifulSoup Scraper v1.0"
            }
        }

        output_dir = "data/knowledge"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "infogadgettech_knowledge.json")

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"✅ [Scraper] Successfully saved {len(sections)} sections of knowledge to {output_path}")
        return data

    except Exception as e:
        print(f"❌ [Scraper] Failed to scrape {url}: {e}")
        return None

if __name__ == "__main__":
    scrape_infogadgettech()
