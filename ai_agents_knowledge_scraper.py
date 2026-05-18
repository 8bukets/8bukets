import requests
from bs4 import BeautifulSoup
import json
import os
import re

def clean_text(text):
    if not text: return ""
    return " ".join(text.split())

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

    h1 = soup.find('h1')
    title = clean_text(h1.get_text()) if h1 else (soup.title.string.split(" - ")[0] if soup.title else "N/A")

    knowledge = {
        "url": url,
        "title": title,
        "definitions": [],
        "use_cases": [],
        "benefits": [],
        "google_cloud_tools": []
    }

    text_content = soup.get_text(separator=' ', strip=True).lower()

    if any(kw in text_content for kw in ["agent", "autonomous", "generative ai", "gemini", "gemma", "research", "vibe", "mtp", "speculative", "innovation", "ai", "intelligence"]):

        summary_sections = {
            "General summary": "definitions",
            "Bullet points": "benefits",
            "Basic explainer": "definitions"
        }
        for section_title, target_key in summary_sections.items():
            section_header = soup.find(['h2', 'h3', 'div', 'button'], string=re.compile(f"^{section_title}$", re.I))
            if section_header:
                content = []
                curr = section_header.find_next_sibling()
                count = 0
                while curr and count < 15 and curr.name not in ['h1', 'h2', 'h3'] and not (curr.name == 'div' and curr.get_text(strip=True) in summary_sections):
                    if curr.name in ['p', 'li', 'span']:
                        text = clean_text(curr.get_text(separator=' ', strip=True))
                        if text: content.append(text)
                    elif curr.name == 'ul':
                        content.extend([clean_text(li.get_text(separator=' ', strip=True)) for li in curr.find_all('li') if li.get_text(strip=True)])
                    curr = curr.find_next_sibling()
                    count += 1

                if content:
                    combined_content = " ".join(content)
                    if target_key == "definitions":
                        knowledge["definitions"].append({"term": section_title, "text": combined_content})
                    else:
                        knowledge["benefits"].append({"title": section_title, "description": combined_content})

        for header in soup.find_all(['h2', 'h3']):
            header_text = clean_text(header.get_text())
            if header_text in summary_sections or header_text == title: continue

            content = []
            curr = header.find_next_sibling()

            # Skip noise
            while curr and (curr.name in ['div', 'span', 'figure', 'button', 'header', 'footer', 'script', 'style'] or not curr.get_text(strip=True)):
                if curr.name in ['p', 'li', 'ul']: break
                if curr.name in ['h1', 'h2', 'h3']: break
                curr = curr.find_next_sibling()

            count = 0
            while curr and count < 20 and curr.name not in ['h1', 'h2', 'h3']:
                if curr.name in ['p', 'li', 'span']:
                    text = clean_text(curr.get_text(separator=' ', strip=True))
                    if text: content.append(text)
                elif curr.name == 'ul':
                    content.extend([clean_text(li.get_text(separator=' ', strip=True)) for li in curr.find_all('li') if li.get_text(strip=True)])
                curr = curr.find_next_sibling()
                count += 1

            combined_content = " ".join(content)
            low_header = header_text.lower()

            if any(kw in low_header for kw in ["what is", "definition", "introducing", "about", "how it works", "speculative decoding", "choose a research", "accelerating gemma 4"]):
                if combined_content:
                    knowledge["definitions"].append({"term": header_text, "text": combined_content})
            elif any(kw in low_header for kw in ["use case", "how to use", "applications", "example", "unlocking", "drive real-world"]):
                if combined_content:
                    knowledge["use_cases"].append({"title": header_text, "description": combined_content})
            elif any(kw in low_header for kw in ["benefit", "why", "advantage", "impact", "value", "accelerating", "unlock proprietary"]):
                if combined_content:
                    knowledge["benefits"].append({"title": header_text, "description": combined_content})
            elif any(kw in low_header for kw in ["cloud", "vertex", "platform", "infrastructure", "tools", "where you can dive", "where to dive", "get started"]):
                if len(header_text) < 50:
                    knowledge["google_cloud_tools"].append(header_text)

                ul = header.find_next('ul')
                if ul:
                    prev_h = ul.find_previous(['h2', 'h3'])
                    if prev_h == header:
                        tools = [clean_text(li.get_text()) for li in ul.find_all('li') if len(li.get_text(strip=True)) < 60]
                        knowledge["google_cloud_tools"].extend(tools)

    # Extract tools by keywords
    tool_keywords = ["Gemini", "Gemma", "Vertex AI", "Model Context Protocol", "MCP", "LiteRT", "Interactions API", "Hugging Face", "Kaggle", "vLLM", "MLX"]
    for kw in tool_keywords:
        if kw.lower() in text_content:
            knowledge["google_cloud_tools"].append(kw)

    # Clean up tools list
    forbidden_tools = ["Developer tools", "How to get started", "Where you can dive deeper", "Explore other styles", "Bullet points", "General summary", "Basic explainer", "Get started", "Where you can dive", "Take advantage"]
    cleaned_tools = []
    seen_tools = set()
    for t in knowledge["google_cloud_tools"]:
        t_clean = t.strip().rstrip('.')
        if len(t_clean) > 2 and len(t_clean) < 60:
            if not any(f.lower() in t_clean.lower() for f in forbidden_tools):
                if t_clean.lower() not in seen_tools:
                    cleaned_tools.append(t_clean)
                    seen_tools.add(t_clean.lower())

    knowledge["google_cloud_tools"] = cleaned_tools

    return knowledge

def run_knowledge_scraper():
    scan_urls = [
        "https://blog.google/innovation-and-ai/",
        "https://blog.google/innovation-and-ai/models-and-research/gemini-models/"
    ]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    article_urls = set()
    keywords = ["agent", "gemini", "research", "autonomous", "vibe", "coding", "gemma", "mtp", "deep research", "ai", "innovation", "intelligence", "recap"]

    for base_url in scan_urls:
        print(f"Scanning {base_url}...")
        try:
            resp = requests.get(base_url, headers=headers)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.content, "html.parser")
            links = soup.find_all('a', href=True)
            for link in links:
                href = link['href']
                text = link.get_text(strip=True).lower()
                if any(kw in text or kw in href.lower() for kw in keywords):
                    if '/innovation-and-ai/' in href and href != base_url:
                        full_url = href if href.startswith('http') else f"https://blog.google{href}"
                        article_urls.add(full_url)
        except Exception as e:
            print(f"Failed to scan {base_url}: {e}")

    # Manually ensure the Deep Research article is included if missed by scan
    article_urls.add("https://blog.google/innovation-and-ai/models-and-research/gemini-models/next-generation-gemini-deep-research/")

    print(f"Found {len(article_urls)} potential articles. Diving in...")

    json_path = "data/ai_agents_knowledge.json"
    existing_knowledge = []
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                existing_knowledge = json.load(f)
        except Exception as e:
            print(f"Error reading existing knowledge: {e}")

    new_knowledge = []
    for url in sorted(list(article_urls)):
        print(f"Scraping {url}...")
        k = extract_structured_knowledge(url)
        if k and (k["definitions"] or k["use_cases"] or k["benefits"] or k["google_cloud_tools"]):
            new_knowledge.append(k)

    # Merge logic
    merged_knowledge = {item["url"]: item for item in existing_knowledge}
    for item in new_knowledge:
        merged_knowledge[item["url"]] = item

    all_knowledge = list(merged_knowledge.values())

    os.makedirs("data", exist_ok=True)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_knowledge, f, indent=4, ensure_ascii=False)

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
        f.write("\nAll the best - https://markposition.wordpress.com\n")

    print(f"Successfully synthesized knowledge from {len(all_knowledge)} articles.")

if __name__ == "__main__":
    run_knowledge_scraper()
