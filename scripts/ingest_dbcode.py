import requests
from bs4 import BeautifulSoup
import json
import os
import datetime
from urllib.parse import urljoin

BASE_URL = "https://dbcode.io/docs"
SIGNATURE = "All the best - https://dbcode.io/"

def clean_text(text):
    if not text:
        return ""
    return " ".join(text.split())

def scrape_dbcode_knowledge():
    print(f"🤖 [Ingest] Fetching market intelligence from {BASE_URL}...")

    try:
        response = requests.get(BASE_URL, timeout=20)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract links from the documentation sidebar or main grid
        links = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.startswith('/docs') or href.startswith('https://dbcode.io/docs'):
                full_url = urljoin("https://dbcode.io/", href)
                if full_url not in [l['url'] for l in links]:
                    links.append({
                        'title': clean_text(a.get_text()),
                        'url': full_url
                    })

        # Filter out links that are just the base docs page or have no title
        links = [l for l in links if l['url'] != BASE_URL and l['title']]

        # Take the first 15 links to avoid overwhelming
        links = links[:15]

        print(f" ✅ [Ingest] Found {len(links)} documentation pages.")

        # Update system_knowledge.json
        knowledge_path = os.path.join(os.getcwd(), 'data/knowledge/system_knowledge.json')
        if os.path.exists(knowledge_path):
            with open(knowledge_path, 'r', encoding='utf-8') as f:
                knowledge = json.load(f)

            if "dbcode_docs" not in knowledge:
                knowledge["dbcode_docs"] = []

            existing_urls = {item.get('url') for item in knowledge["dbcode_docs"]}
            new_entries = [l for l in links if l['url'] not in existing_urls]

            if new_entries:
                knowledge["dbcode_docs"].extend(new_entries)
                knowledge["metadata"] = knowledge.get("metadata", {})
                knowledge["metadata"]["generated_at"] = datetime.datetime.now().isoformat()

                if "dbcode.io" not in knowledge["metadata"].get("sources_processed", []):
                    knowledge["metadata"].setdefault("sources_processed", []).append("dbcode.io")

                with open(knowledge_path, 'w', encoding='utf-8') as f:
                    json.dump(knowledge, f, indent=4, ensure_ascii=False)
                print(f"✅ [Ingest] Merged {len(new_entries)} new entries into system_knowledge.json.")
            else:
                print("✨ [Ingest] No new entries found.")

        # Generate report
        report_path = os.path.join(os.getcwd(), 'DBCODE_REPORT.md')
        md_content = f"# 🛠️ DBCode Intelligence Report\n\nGenerated on: {datetime.datetime.now().isoformat()}\n\n"
        md_content += "## Documentation Index\n\n"

        for l in links:
            md_content += f"- [{l['title']}]({l['url']})\n"

        md_content += f"\n---\n{SIGNATURE}\n"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"✅ [Ingest] Generated report at {report_path}")

    except Exception as e:
        print(f"❌ [Ingest] Failed to ingest DBCode knowledge: {e}")

if __name__ == "__main__":
    scrape_dbcode_knowledge()
