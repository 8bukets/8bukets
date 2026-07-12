import requests
from bs4 import BeautifulSoup
import json
import os
import re

URL = "https://cloud.google.com/discover/what-are-ai-agents"

def clean_text(text):
    if not text: return ""
    return " ".join(text.split())

def scrape_discovery():
    print(f"Fetching AI Agent knowledge from {URL}...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        resp = requests.get(URL, headers=headers, timeout=15)
        resp.raise_for_status()
    except Exception as e:
        print(f"Error fetching {URL}: {e}")
        return

    soup = BeautifulSoup(resp.content, "lxml")

    data = {}
    ordered_keys = []

    stop_markers = [
        "Additional resources", "Take the next step", "Continue browsing",
        "Why Google", "Products and pricing", "Solutions", "Resources", "Engage"
    ]

    skip_titles = [
        "Stay informed", "Topics", "Page Contents",
        "arrow_forward", "Key benefits", "Reports and insights",
        "Industry Solutions", "Featured Products", "Business Intelligence",
        "Compute", "Containers", "Data Analytics", "Databases",
        "Developer Tools", "Distributed Cloud", "Hybrid and Multicloud",
        "Industry Specific", "Integration Services", "Management Tools",
        "Maps and Geospatial", "Media Services", "Migration",
        "Networking", "Operations", "Productivity and Collaboration",
        "Security and Identity", "Serverless", "Storage", "Web3",
        "Save money with our transparent approach to pricing",
        "Pricing overview and tools", "Product-specific Pricing",
        "Learn & build", "Connect", "Consulting and Partners",
        "Overview", "Products", "Pricing", "Docs", "Support", "Console",
        "Contact us", "Start free", "Sign in", "Language"
    ]

    main = soup.find(['main', 'article', 'div'], {'role': 'main'})
    if not main:
        main = soup.body

    current_id = ""
    current_title = ""
    current_content = []
    stop_scraping = False

    def finalize_section():
        nonlocal current_id, current_title, current_content
        if current_id and current_content:
            # Filter noise and stop markers
            filtered = []
            for line in current_content:
                line = line.strip()
                if not line: continue
                if any(skip in line for skip in skip_titles): continue
                if any(stop in line for stop in stop_markers): continue
                # Filter out obvious SEO/Social noise
                if "all the best" in line.lower() or "wordpress.com" in line.lower(): continue
                filtered.append(line)

            if filtered:
                unique = []
                seen = set()
                for line in filtered:
                    if line.lower() not in seen:
                        unique.append(line)
                        seen.add(line.lower())

                # Use \n for joining to preserve table and list structures
                content_str = "\n".join(unique)
                data[current_id] = {"title": current_title, "content": content_str}
                if current_id not in ordered_keys:
                    ordered_keys.append(current_id)

    for el in main.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'table', 'pre']):
        if stop_scraping: break

        if el.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            title = clean_text(el.get_text())
            if not title: continue

            if any(stop in title for stop in stop_markers):
                finalize_section()
                stop_scraping = True
                continue

            finalize_section()

            if any(skip == title for skip in skip_titles):
                current_id = ""
                current_title = ""
                current_content = []
                continue

            current_title = title
            current_id = el.get('id') or re.sub(r'\s+', '-', title.lower()).replace('?', '').replace(',', '')

            # Map new IDs to existing ones to avoid duplication
            id_map = {
                "challenges-with-using-ai-agents": "challenges-of-ai-agents",
                "benefits-of-using-ai-agents": "benefits-of-ai-agents",
                "what-are-the-types-of-agents-in-ai": "types-of-ai-agents",
                "how-do-ai-agents-work": "how-ai-agents-work",
                "what-is-the-difference-between-ai-agents-ai-assistants-and-bots": "ai-agents-vs-assistants-vs-bots",
                "deploy-ai-agents-for-scale-and-efficiency-with-cloud-run": "deploying-ai-agents-cloud-run"
            }
            if current_id in id_map:
                current_id = id_map[current_id]

            current_content = []
        elif current_id:
            if el.name == 'p':
                text = clean_text(el.get_text())
                if text: current_content.append(text)
            elif el.name in ['ul', 'ol']:
                items = []
                for li in el.find_all('li', recursive=False):
                    li_text = clean_text(li.get_text())
                    if li_text:
                        items.append(f"- {li_text}")
                if items: current_content.append("\n".join(items))
            elif el.name == 'table':
                rows = []
                headers = el.find_all(['th', 'td']) # More robust header detection
                # Try to find a reasonable header count
                first_tr = el.find('tr')
                if first_tr:
                    header_count = len(first_tr.find_all(['td', 'th']))
                else:
                    header_count = 0

                for tr in el.find_all('tr'):
                    cells = [clean_text(td.get_text()) for td in tr.find_all(['td', 'th'])]
                    if cells:
                        rows.append(" | " + " | ".join(cells) + " |")

                if rows:
                    if header_count > 1:
                        sep = " | " + " | ".join(["---"] * header_count) + " |"
                        rows.insert(1, sep)
                    current_content.append("\n".join(rows))
            elif el.name == 'pre':
                text = el.get_text().strip()
                if text: current_content.append(f"```\n{text}\n```")

    finalize_section()

    target_dir = "data/knowledge"
    os.makedirs(target_dir, exist_ok=True)
    json_path = os.path.join(target_dir, "ai_agents_knowledge.json")

    existing = {}
    if os.path.exists(json_path):
        try:
            with open(json_path, 'r') as f:
                existing = json.load(f)
        except: pass

    # Smart merge: update existing, add new
    for k, v in data.items():
        existing[k] = v

    with open(json_path, 'w') as f:
        json.dump(existing, f, indent=4)

    # Rebuild MD file preserving manual sections
    md_path = os.path.join(target_dir, "ai_agents_knowledge.md")

    manual_sections = {k: v for k, v in existing.items() if k not in data and k not in ordered_keys}

    with open(md_path, 'w') as f:
        f.write(f"# AI Agents Knowledge base\n\nLatest Update from: {URL}\n\n")

        # Write manual/legacy sections first (like Compile, Jules Tools)
        for k, v in manual_sections.items():
            f.write(f"## {v['title']}\n\n{v['content']}\n\n---\n\n")

        # Write newly scraped sections
        for key in ordered_keys:
            if key in existing:
                f.write(f"## {existing[key]['title']}\n\n{existing[key]['content']}\n\n---\n\n")

    # Update system_knowledge.json
    sk_path = os.path.join(target_dir, "system_knowledge.json")
    if os.path.exists(sk_path):
        try:
            with open(sk_path, 'r') as f:
                sk = json.load(f)

            if 'ai_agents_structured' not in sk:
                sk['ai_agents_structured'] = []

            sk['ai_agents_structured'] = [item for item in sk['ai_agents_structured'] if item.get('url') != URL]

            new_entry = {
                "url": URL,
                "title": "What are AI agents? (GCP Discovery)",
                "sections": []
            }
            for key in ordered_keys:
                new_entry['sections'].append({
                    "header": data[key]['title'],
                    "content": data[key]['content'].split('\n\n')
                })
            sk['ai_agents_structured'].append(new_entry)

            # Also merge top-level if needed but mostly used in MD generation
            for key in data:
                sk[key] = data[key]

            with open(sk_path, 'w') as f:
                json.dump(sk, f, indent=2)
            print("Integrated into system_knowledge.json")
        except Exception as e:
            print(f"Error updating system_knowledge.json: {e}")

if __name__ == "__main__":
    scrape_discovery()
