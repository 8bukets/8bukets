import json
import os

def merge_knowledge():
    # Only merge from the intended path
    agents_path = "data/knowledge/ai_agents_knowledge.json"
    system_path = "data/knowledge/system_knowledge.json"
    consolidated_path = "CONSOLIDATED_KNOWLEDGE.md"

    if not os.path.exists(agents_path):
        print(f"Source file {agents_path} not found.")
        return

    with open(agents_path, "r", encoding="utf-8") as f:
        agents_data = json.load(f)

    system_knowledge = {}
    if os.path.exists(system_path):
        try:
            with open(system_path, "r", encoding="utf-8") as f:
                system_knowledge = json.load(f)
        except Exception:
            pass

    # Ensure sections exist
    if "ai_agents_structured" not in system_knowledge:
        system_knowledge["ai_agents_structured"] = []

    # Map existing by URL or Title for merging
    # For this specific source, we are merging by sections from the single page
    # The script in ingest_ai_agents_knowledge.ts outputs sections as keys

    # We will clear old scraped data from this URL to avoid duplication/pollution
    source_url = "https://cloud.google.com/discover/what-are-ai-agents"
    system_knowledge["ai_agents_structured"] = [
        item for item in system_knowledge["ai_agents_structured"]
        if item.get("url") != source_url
    ]

    # Add the new unified entry
    new_entry = {
        "url": source_url,
        "title": "What are AI agents?",
        "sections": [
            {"header": v["title"], "content": v["content"].split("\n\n")}
            for k, v in agents_data.items()
        ]
    }
    system_knowledge["ai_agents_structured"].append(new_entry)

    with open(system_path, "w", encoding="utf-8") as f:
        json.dump(system_knowledge, f, indent=4, ensure_ascii=False)
    print(f"Merged knowledge into {system_path}")

    # Handle CONSOLIDATED_KNOWLEDGE.md carefully
    if os.path.exists(consolidated_path):
        with open(consolidated_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Check if signature already exists at the end
        signature = "All the best - https://markposition.wordpress.com"
        has_signature = any(signature in line for line in lines[-5:])

        if not has_signature:
            with open(consolidated_path, "a", encoding="utf-8") as f:
                f.write(f"\n---\n{signature}\n")
            print(f"Signed {consolidated_path}")

if __name__ == "__main__":
    merge_knowledge()
