import requests
from bs4 import BeautifulSoup
import json
import os
import datetime
from urllib.parse import urlparse

BASE_URL = "https://markposition.wordpress.com/"

def clean_text(text):
    if not text:
        return ""
    return " ".join(text.split())

def scrape_markposition_knowledge(max_pages=5):
    print(f"🤖 [Ingest] Fetching market intelligence from {BASE_URL} (max {max_pages} pages)...")
    all_entries = []

    try:
        for page in range(1, max_pages + 1):
            url = BASE_URL if page == 1 else f"{BASE_URL}page/{page}/"
            print(f" - Scraping page {page}: {url}")

            try:
                response = requests.get(url, timeout=20)
                if response.status_code == 404:
                    print(f" ✨ [Ingest] Page {page} not found. Ending pagination.")
                    break
                response.raise_for_status()
            except Exception as e:
                print(f" ❌ [Ingest] Error fetching page {page}: {e}")
                break

            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.find_all('article', class_='post')

            page_entries = []
            for article in articles:
                title_tag = article.select_one('h1.entry-title a')
                if not title_tag:
                    continue

                title = clean_text(title_tag.get_text())
                post_url = title_tag.get('href')

                date_tag = article.select_one('time.entry-date')
                date = clean_text(date_tag.get_text()) if date_tag else ""
                datetime_str = date_tag.get('datetime') if date_tag else ""

                author_tag = article.select_one('.author .fn')
                author = clean_text(author_tag.get_text()) if author_tag else "Filip Keser"

                categories = []
                classes = article.get('class', [])
                for cls in classes:
                    if cls.startswith('category-'):
                        cat = cls.replace('category-', '').replace('-', ' ').title()
                        categories.append(cat)

                external_link = None
                content_div = article.select_one('.entry-content')
                if content_div:
                    link_tag = content_div.find('a')
                    if link_tag:
                        external_link = link_tag.get('href')

                    if not external_link:
                        iframe_tag = content_div.find('iframe')
                        if iframe_tag:
                            external_link = iframe_tag.get('src')

                domain = None
                if external_link:
                    try:
                        domain = urlparse(external_link).hostname.replace('www.', '')
                    except:
                        pass

                page_entries.append({
                    "title": title,
                    "date": date,
                    "datetime": datetime_str,
                    "author": author,
                    "categories": categories,
                    "external_link": external_link,
                    "domain": domain,
                    "post_url": post_url
                })

            if not page_entries:
                print(f" ✨ [Ingest] No entries found on page {page}. Ending pagination.")
                break

            all_entries.extend(page_entries)
            print(f" ✅ [Ingest] Parsed {len(page_entries)} entries from page {page}.")

        print(f"✅ [Ingest] Total entries parsed: {len(all_entries)}")

        # Update system_knowledge.json
        knowledge_path = os.path.join(os.getcwd(), 'data/knowledge/system_knowledge.json')
        if os.path.exists(knowledge_path):
            with open(knowledge_path, 'r', encoding='utf-8') as f:
                knowledge = json.load(f)

            if "market_data" not in knowledge:
                knowledge["market_data"] = {"total_entries": 0, "recent_entries": [], "all_entries": []}

            # Merge logic
            existing_urls = {e.get('post_url') for e in knowledge["market_data"].get("all_entries", [])}
            new_entries = [e for e in all_entries if e.get('post_url') not in existing_urls]

            if new_entries:
                # Migration check
                if "sections" in knowledge and "market_data" in knowledge["sections"]:
                    print("📦 [Ingest] Migrating nested market_data to flat structure...")
                    knowledge["market_data"] = knowledge["sections"]["market_data"]
                    del knowledge["sections"]["market_data"]
                    if not knowledge["sections"]:
                        del knowledge["sections"]

                combined = new_entries + knowledge["market_data"].get("all_entries", [])
                knowledge["market_data"]["all_entries"] = combined
                knowledge["market_data"]["recent_entries"] = combined[:20]
                knowledge["market_data"]["total_entries"] = len(combined)

                if "metadata" not in knowledge:
                    knowledge["metadata"] = {"sources_processed": [], "generated_at": ""}

                if "markposition.wordpress.com" not in knowledge["metadata"].get("sources_processed", []):
                    knowledge["metadata"].setdefault("sources_processed", []).append("markposition.wordpress.com")

                knowledge["metadata"]["generated_at"] = datetime.datetime.now().isoformat()

                with open(knowledge_path, 'w', encoding='utf-8') as f:
                    json.dump(knowledge, f, indent=4, ensure_ascii=False)
                print(f"✅ [Ingest] Merged {len(new_entries)} new entries into system_knowledge.json.")
            else:
                print("✨ [Ingest] No new entries found.")

        # Generate report
        report_path = os.path.join(os.getcwd(), 'MARKPOSITION_REPORT.md')
        md_content = f"# 📈 Markposition Intelligence Report\n\nGenerated on: {datetime.datetime.now().isoformat()}\n\n"
        md_content += "## Recent Market Intelligence\n\n"

        for e in all_entries[:20]:
            md_content += f"### {e['title']}\n"
            md_content += f"- **Date**: {e['date']}\n"
            md_content += f"- **Domain**: {e['domain'] or 'N/A'}\n"
            md_content += f"- **Link**: [{e['external_link'] or 'Post Link'}]({e['external_link'] or e['post_url']})\n\n"

        md_content += "\n---\nAll the best - https://markposition.wordpress.com\n"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"✅ [Ingest] Generated report at {report_path}")

    except Exception as e:
        print(f"❌ [Ingest] Failed to ingest Markposition knowledge: {e}")

if __name__ == "__main__":
    scrape_markposition_knowledge()
