import requests
from bs4 import BeautifulSoup
import json
import os
import re

def extract_structured_knowledge(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

    soup = BeautifulSoup(resp.content, "html.parser")

    knowledge = {
        "url": url,
        "title": soup.title.string if soup.title else "N/A",
        "definitions": [],
        "use_cases": [],
        "benefits": [],
        "google_cloud_tools": []
    }

    # Heuristic: look for sections
    text_content = soup.get_text(separator=' ', strip=True).lower()

    # Common patterns for AI Agents
    if any(kw in text_content for kw in ["agent", "autonomous", "generative ai", "gemini", "gemma", "research"]):
        # Extract headers and following content
        for header in soup.find_all(['h1', 'h2', 'h3']):
            header_text = header.get_text(strip=True)
            content = []
            curr = header.find_next_sibling()
            while curr and curr.name not in ['h1', 'h2', 'h3']:
                if curr.name in ['p', 'li']:
                    content.append(curr.get_text(strip=True))
                curr = curr.find_next_sibling()

            combined_content = " ".join(content)
            low_header = header_text.lower()

            if any(kw in low_header for kw in ["what is", "definition", "introducing", "about"]):
                knowledge["definitions"].append({"term": header_text, "text": combined_content})
            elif any(kw in low_header for kw in ["use case", "how to use", "applications", "example"]):
                knowledge["use_cases"].append({"title": header_text, "description": combined_content})
            elif any(kw in low_header for kw in ["benefit", "why", "advantage", "impact", "value"]):
                knowledge["benefits"].append({"title": header_text, "description": combined_content})
            elif any(kw in low_header for kw in ["cloud", "vertex", "platform", "infrastructure"]):
                knowledge["google_cloud_tools"].append(header_text)

    # If no sections found, try to extract from paragraphs based on keywords
    if not any([knowledge["definitions"], knowledge["use_cases"], knowledge["benefits"]]):
        # Also check for lead content
        lead_content = soup.find('div', class_='article-lead')
        if lead_content:
            text = lead_content.get_text(strip=True)
            if "agent" in text.lower():
                knowledge["definitions"].append({"term": "AI Agent (Lead Insight)", "text": text})

        paragraphs = soup.find_all('p')
        for p in paragraphs:
            text = p.get_text(strip=True)
            if len(text) < 50: continue

            if "agent" in text.lower() and ("is a" in text.lower() or "defined as" in text.lower()):
                knowledge["definitions"].append({"term": "AI Agent", "text": text})
            elif "can use" in text.lower() or "allows users to" in text.lower():
                knowledge["use_cases"].append({"title": "General Use Case", "description": text})
            elif "improve" in text.lower() or "efficiency" in text.lower() or "faster" in text.lower():
                knowledge["benefits"].append({"title": "General Benefit", "description": text})

    return knowledge

def run_knowledge_scraper():
    base_url = "https://blog.google/innovation-and-ai/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    print(f"Scanning {base_url} for AI Agent articles...")
    try:
        resp = requests.get(base_url, headers=headers)
        resp.raise_for_status()
    except Exception as e:
        print(f"Failed to scan base URL: {e}")
        return

    soup = BeautifulSoup(resp.content, "html.parser")
    links = soup.find_all('a', href=True)

    article_urls = set()
    keywords = ["agent", "gemini", "research", "autonomous", "vibe", "coding"]

    for link in links:
        href = link['href']
        text = link.get_text(strip=True).lower()
        if any(kw in text or kw in href.lower() for kw in keywords):
            if '/innovation-and-ai/' in href and href != base_url:
                full_url = href if href.startswith('http') else f"https://blog.google{href}"
                article_urls.add(full_url)

    print(f"Found {len(article_urls)} potential articles. Diving in...")

    # Load existing knowledge to merge
    json_path = "data/ai_agents_knowledge.json"
    existing_knowledge = []
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                existing_knowledge = json.load(f)
        except Exception as e:
            print(f"Error reading existing knowledge: {e}")

    new_knowledge = []
    seen_titles = {item["title"] for item in existing_knowledge}

    for url in list(article_urls)[:15]: # Limit to 15 for better coverage
        print(f"Scraping {url}...")
        k = extract_structured_knowledge(url)
        if k and (k["definitions"] or k["use_cases"] or k["benefits"]):
            if k["title"] not in seen_titles:
                new_knowledge.append(k)
                seen_titles.add(k["title"])

    all_knowledge = existing_knowledge + new_knowledge

    # Save to JSON
    os.makedirs("data", exist_ok=True)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_knowledge, f, indent=4, ensure_ascii=False)

    # Save to Markdown
    with open("ai_agents_knowledge.md", "w", encoding="utf-8") as f:
        f.write("# AI Agents Knowledge Repository\n\n")
        f.write(f"Synthesized from Google Innovation & AI Blog\n\n")

        for item in all_knowledge:
            f.write(f"## [{item['title']}]({item['url']})\n\n")

            if item["definitions"]:
                f.write("### Definitions\n")
                for d in item["definitions"]:
                    f.write(f"- **{d['term']}**: {d['text']}\n")
                f.write("\n")

            if item["use_cases"]:
                f.write("### Use Cases\n")
                for u in item["use_cases"]:
                    f.write(f"- **{u['title']}**: {u['description']}\n")
                f.write("\n")

            if item["benefits"]:
                f.write("### Benefits\n")
                for b in item["benefits"]:
                    f.write(f"- **{b['title']}**: {b['description']}\n")
                f.write("\n")

            if item["google_cloud_tools"]:
                f.write("### Google Cloud Tools\n")
                for tool in item["google_cloud_tools"]:
                    f.write(f"- {tool}\n")
                f.write("\n")

            f.write("---\n\n")

    print(f"Successfully synthesized knowledge from {len(all_knowledge)} articles.")

if __name__ == "__main__":
    run_knowledge_scraper()
