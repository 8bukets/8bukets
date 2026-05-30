import requests
from bs4 import BeautifulSoup
import json
import logging
import os

logger = logging.getLogger("AIKnowledgeScraper")

def scrape_ai_agents_knowledge():
    url = "https://cloud.google.com/discover/what-are-ai-agents"
    logger.info(f"Fetching AI Agent knowledge from {url}...")
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Error fetching AI Agent knowledge: {e}")
        return False

    soup = BeautifulSoup(resp.content, "html.parser")

    # Capture all relevant headings as section markers
    headings = soup.find_all(["h1", "h2", "h3", "h4"])
    all_tags = soup.find_all(True)
    data = {}
    ordered_scraped_keys = []

    for i, header in enumerate(headings):
        section_title = header.get_text(strip=True)
        # Skip UI and navigation sections
        if section_title in ["Additional resources", "Take the next step", "Accelerate your digital transformation", "Why Google", "Products and pricing", "Solutions", "Resources", "Engage", "Stay informed", "Topics"]:
            continue

        section_id = header.get("id")
        if not section_id:
            section_id = section_title.lower().replace(" ", "-").replace("?", "").replace(",", "")

        next_header = headings[i+1] if i+1 < len(headings) else None

        try:
            start_idx = all_tags.index(header)
            end_idx = all_tags.index(next_header) if next_header else len(all_tags)
        except ValueError:
            continue

        section_content = []
        processed_tags = set()

        for j in range(start_idx + 1, end_idx):
            tag = all_tags[j]
            if tag in processed_tags:
                continue

            if tag.name == "h4":
                section_content.append(f"### {tag.get_text(strip=True)}")
            elif tag.name in ["p", "table", "pre", "h5", "h6"]:
                if tag.name == "table":
                    rows = []
                    header_count = 0
                    for k, tr in enumerate(tag.find_all("tr")):
                        cells = [th_td.get_text(separator=" ", strip=True) for th_td in tr.find_all(["th", "td"])]
                        if not any(cells): continue
                        rows.append(" | ".join(cells))
                        if k == 0 or header_count == 0:
                            header_count = len(cells)

                    if rows and header_count > 1:
                        separator = " | ".join(["---"] * header_count)
                        rows.insert(1, separator)
                    section_content.append("\n".join(rows))
                elif tag.name == "pre":
                    section_content.append(f"```\n{tag.get_text(strip=True)}\n```")
                else:
                    text = tag.get_text(separator=' ', strip=True)
                    if text:
                        section_content.append(text)

                # Mark all descendants as processed
                for descendant in tag.find_all(True):
                    processed_tags.add(descendant)

            elif tag.name in ["ul", "ol"]:
                list_items = []
                for li in tag.find_all("li", recursive=False):
                    li_text = li.get_text(separator=" ", strip=True)
                    if li_text:
                        list_items.append(f"- {li_text}")
                    processed_tags.add(li)
                    for d in li.find_all(True):
                        processed_tags.add(d)
                if list_items:
                    section_content.append("\n".join(list_items))

        if section_content:
            data[section_id] = {
                "title": section_title,
                "content": "\n\n".join(section_content)
            }
            ordered_scraped_keys.append(section_id)

    # Save to JSON
    json_path = "ai_agents_knowledge.json"
    try:
        final_data = {}
        manual_keys = ["compile-definition", "compile", "jules-tools", "knowledge-merge", "gemini-cli-remote-subagents", "gemini-cli-subagents", "ide-integration"]
        if os.path.exists(json_path):
            with open(json_path, "r", encoding="utf-8") as f:
                old_data = json.load(f)
            # Keep manual entries
            for key in manual_keys:
                if key in old_data:
                    final_data[key] = old_data[key]

        final_data.update(data)

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(final_data, f, indent=4, ensure_ascii=False)
        logger.info(f"Saved AI Agent knowledge to {json_path}")

        md_path = "ai_agents_knowledge.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write("# What are AI Agents?\n\n")
            f.write(f"Scraped from [{url}]({url})\n\n")

            # Re-order: Scraped content first (preserving page order), then manual entries at the end
            for k in ordered_scraped_keys:
                if k in final_data:
                    f.write(f"## {final_data[k]['title']}\n\n")
                    f.write(f"{final_data[k]['content']}\n\n")

            f.write("---\n\n# Manual Knowledge Additions\n\n")
            for mk in manual_keys:
                if mk in final_data and mk not in ordered_scraped_keys:
                    f.write(f"## {final_data[mk]['title']}\n\n")
                    f.write(f"{final_data[mk]['content']}\n\n")



        return True
    except Exception as e:
        logger.error(f"Failed to save AI Agent knowledge files: {e}")
        return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    scrape_ai_agents_knowledge()
