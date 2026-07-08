import json
import os
import re

def update_knowledge():
    scraped_json_path = "data/knowledge/scraped_google_agents.json"
    ai_agents_json_path = "data/knowledge/ai_agents_knowledge.json"
    ai_agents_md_path = "data/knowledge/ai_agents_knowledge.md"
    system_json_path = "data/knowledge/system_knowledge.json"

    if not os.path.exists(scraped_json_path):
        print(f"Error: {scraped_json_path} not found. Run scraper first.")
        return

    with open(scraped_json_path, "r", encoding="utf-8") as f:
        gcp_knowledge = json.load(f)

    # Load existing AI agents knowledge
    ai_agents_knowledge = {}
    if os.path.exists(ai_agents_json_path):
        with open(ai_agents_json_path, "r", encoding="utf-8") as f:
            try:
                ai_agents_knowledge = json.load(f)
            except:
                ai_agents_knowledge = {}

    # Update/Add to AI agents knowledge
    for slug, data in gcp_knowledge.items():
        # Deduplicate content if it's already there
        if slug in ai_agents_knowledge:
            if ai_agents_knowledge[slug]["content"] != data["content"]:
                ai_agents_knowledge[slug] = data
        else:
            ai_agents_knowledge[slug] = data

    os.makedirs(os.path.dirname(ai_agents_json_path), exist_ok=True)
    with open(ai_agents_json_path, "w", encoding="utf-8") as f:
        json.dump(ai_agents_knowledge, f, indent=4, ensure_ascii=False)

    # Sync to Markdown (Non-destructive merge by header)
    url = "https://cloud.google.com/discover/what-are-ai-agents"
    existing_sections = {}

    if os.path.exists(ai_agents_md_path):
        with open(ai_agents_md_path, "r", encoding="utf-8") as f:
            md_content = f.read()
            # Split by '---' separator
            blocks = md_content.split('---')
            for block in blocks:
                # Find header '### Title'
                header_match = re.search(r'### (.*?)\n', block)
                if header_match:
                    header_title = header_match.group(1).strip()
                    # Content is everything after the header line
                    content = block.split(header_match.group(0), 1)[1].strip()
                    if content:
                        existing_sections[header_title] = content

    # ONLY update or add sections from the newly scraped GCP knowledge
    for slug, data in gcp_knowledge.items():
        title = data.get('title', slug)
        content = data.get('content', '')
        # Ensure we don't accidentally add Gemini CLI docs if they weren't in gcp_knowledge
        # (they shouldn't be, but let's be safe)
        if title:
            existing_sections[title] = content

    # Re-build the full Markdown with ALL sections (preserved + updated)
    with open(ai_agents_md_path, "w", encoding="utf-8") as f:
        f.write(f"# AI Agents Knowledge base\n\nLatest Update from: {url}\n\n")

        for title in sorted(existing_sections.keys()):
            f.write(f"### {title}\n\n")
            f.write(f"{existing_sections[title]}\n\n")
            f.write("---\n\n")

        f.write(f"All the best - {url}\n")

    # Update system_knowledge.json
    if os.path.exists(system_json_path):
        with open(system_json_path, "r", encoding="utf-8") as f:
            system_knowledge = json.load(f)

        if "ai_agents_structured" not in system_knowledge:
            system_knowledge["ai_agents_structured"] = []

        # Remove old entry for the specific URL if exists
        system_knowledge["ai_agents_structured"] = [e for e in system_knowledge["ai_agents_structured"] if e.get("url") != url]

        new_entry = {
            "url": url,
            "title": "What are AI agents? (GCP Discovery)",
            "sections": [
                {"header": data["title"], "content": data["content"].split("\n\n")} for slug, data in gcp_knowledge.items()
            ]
        }
        system_knowledge["ai_agents_structured"].append(new_entry)

        with open(system_json_path, "w", encoding="utf-8") as f:
            # Reverting to 4-space indentation to minimize diff noise as per review
            json.dump(system_knowledge, f, indent=4, ensure_ascii=False)

    print(f"Successfully updated knowledge bases with comprehensive GCP AI Agents intelligence from {scraped_json_path}.")

if __name__ == "__main__":
    update_knowledge()
