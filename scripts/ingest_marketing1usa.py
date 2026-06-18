import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime, timezone

def scrape_marketing1usa():
    url = "https://marketing1usa.wordpress.com/"
    print(f"🚀 [Scraper] Scraping {url}...")

    try:
        # Using a browser-like User-Agent to avoid blocks
        session = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
        }
        response = session.get(url, headers=headers, timeout=15)

        if response.status_code == 429:
             print("⚠️ 429 detected, attempting fallback with simple headers...")
             response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)

        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.title.string.strip() if soup.title else "marketing"

        sections = []

        # In WordPress blogs, posts are often in articles, entry-content divs, or post-content
        # Based on the text view, it might be a list of posts
        articles = soup.find_all(['article', 'div'], class_=['post', 'type-post', 'entry', 'entry-content'])

        if not articles:
            # Try finding any div that might contain post headers
            articles = soup.select('.post, .entry, article')

        if articles:
            for article in articles:
                header_elem = article.find(['h1', 'h2', 'h3', 'h4', 'a'], class_=['entry-title', 'post-title'])
                if not header_elem and article.name != 'article':
                     # If we are looking at divs, try harder to find a title
                     header_elem = article.find(['h1', 'h2', 'h3', 'h4'])

                header_text = header_elem.get_text(strip=True) if header_elem else ""

                # Try to get the actual content part
                content_elem = article.find(class_=['entry-content', 'post-content', 'content']) or article

                # Cleanup
                for junk in content_elem.find_all(class_=['sharedaddy', 'wpcnt', 'jp-relatedposts', 'post-meta', 'entry-meta']):
                    junk.decompose()

                content_text = content_elem.get_text(separator='\n', strip=True)

                if header_text and content_text and content_text != header_text:
                    # Deduplicate
                    if not any(s['header'] == header_text for s in sections):
                        sections.append({
                            "header": header_text,
                            "content": content_text
                        })

        if not sections:
            # Fallback to looking for links that might be posts
            for link in soup.find_all('a', href=True):
                href = link['href']
                if '/2022/' in href or '/2023/' in href:
                    text = link.get_text(strip=True)
                    if text and len(text) > 3:
                        sections.append({
                            "header": text,
                            "content": f"Reference: {href}"
                        })

        if not sections:
            # Extreme fallback
            content_div = soup.find('main') or soup.find(id='content') or soup.find('body')
            if content_div:
                text = content_div.get_text(separator='\n', strip=True)
                if text:
                    sections.append({
                        "header": "Main Content",
                        "content": text[:2000] # Limit size
                    })

        # Add the specific signature as required
        signature = "All the best - https://marketing1usa.wordpress.com/"
        sections.append({
            "header": "Signature",
            "content": signature
        })

        data = {
            "source": url,
            "title": title,
            "description": "Market intelligence and company news updates extracted from marketing1usa.wordpress.com.",
            "topKeywords": ["marketing", "online", "branding", "usa"],
            "analyzedAt": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            "sections": sections,
            "metadata": {
                "signature": signature,
                "engine": "Python BeautifulSoup Scraper v1.0"
            }
        }

        output_dir = "data/knowledge"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "marketing1usa_knowledge.json")

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"✅ [Scraper] Successfully saved {len(sections)} sections of knowledge to {output_path}")
        return data

    except Exception as e:
        print(f"❌ [Scraper] Failed to scrape {url}: {e}")
        # Ensure we still have a file for the next step even if it's minimal or error state
        return None

if __name__ == "__main__":
    scrape_marketing1usa()
