import json
import os
from datetime import datetime

def merge_knowledge():
    innovation_path = "data/google_innovation_ai.json"
    agents_path = "data/ai_agents_knowledge.json"
    system_path = "data/knowledge/system_knowledge.json"

    innovation_data = []
    if os.path.exists(innovation_path):
        with open(innovation_path, "r", encoding="utf-8") as f:
            innovation_data = json.load(f)

    agents_data = []
    if os.path.exists(agents_path):
        with open(agents_path, "r", encoding="utf-8") as f:
            content = json.load(f)
            if isinstance(content, list):
                agents_data = content
            elif isinstance(content, dict):
                # For dict-style knowledge, we treat the values as content items if they have url
                # or just use innovation-style list for ai_agents_structured
                # However, merge logic below expects a list of items with 'url'
                agents_data = []
                for k, v in content.items():
                    if isinstance(v, dict) and "url" in v:
                        agents_data.append(v)
                    elif isinstance(v, dict) and "content" in v:
                        # Fallback for dict without url
                        agents_data.append({"url": k, "title": k, "content": v["content"]})

    # Prepare the unified structure
    system_knowledge = {
        "metadata": {
            "generated_at": datetime.now().isoformat(),
            "version": 1.0,
            "sources_processed": []
        },
        "typescript_sections": {}
    }

    if os.path.exists(system_path):
        try:
            with open(system_path, "r", encoding="utf-8") as f:
                existing = json.load(f)
                if isinstance(existing, dict):
                    # Preserve existing structure and migrate sections if needed
                    for k, v in existing.items():
                        if k == "sections":
                            system_knowledge.update(v)
                        else:
                            system_knowledge[k] = v
        except Exception as e:
            print(f"Warning: Failed to load existing knowledge: {e}")

    # Merge innovation data
    existing_innovation = {item["url"]: item for item in system_knowledge.get("google_innovation_ai", []) if isinstance(item, dict) and "url" in item}
    for item in innovation_data:
        if isinstance(item, dict) and "url" in item:
            existing_innovation[item["url"]] = item
    system_knowledge["google_innovation_ai"] = list(existing_innovation.values())

    # Merge agents data
    existing_agents = {item["url"]: item for item in system_knowledge.get("ai_agents_structured", []) if isinstance(item, dict) and "url" in item}
    for item in agents_data:
        if not isinstance(item, dict) or "url" not in item: continue

        url = item["url"]
        if url in existing_agents:
            # Smart merge definitions/tools
            existing = existing_agents[url]

            # Definitions
            existing_defs = {d["term"]: d["text"] for d in existing.get("definitions", []) if isinstance(d, dict)}
            for d in item.get("definitions", []):
                if isinstance(d, dict):
                    existing_defs[d["term"]] = d["text"]
            existing["definitions"] = [{"term": k, "text": v} for k, v in existing_defs.items()]

            # Tools
            existing_tools = set(existing.get("google_cloud_tools", []))
            existing_tools.update(item.get("google_cloud_tools", []))
            existing["google_cloud_tools"] = sorted(list(existing_tools))

            # Benefits & Use Cases
            existing_ucs = {u["title"]: u["description"] for u in existing.get("use_cases", []) if isinstance(u, dict)}
            for u in item.get("use_cases", []):
                if isinstance(u, dict):
                    existing_ucs[u["title"]] = u["description"]
            existing["use_cases"] = [{"title": k, "description": v} for k, v in existing_ucs.items()]

            existing_bens = {b["title"]: b["description"] for b in existing.get("benefits", []) if isinstance(b, dict)}
            for b in item.get("benefits", []):
                if isinstance(b, dict):
                    existing_bens[b["title"]] = b["description"]
            existing["benefits"] = [{"title": k, "description": v} for k, v in existing_bens.items()]
        else:
            existing_agents[url] = item

    system_knowledge["ai_agents_structured"] = list(existing_agents.values())

    # Update metadata
    system_knowledge["metadata"]["generated_at"] = datetime.now().isoformat()

    with open(system_path, "w", encoding="utf-8") as f:
        json.dump(system_knowledge, f, indent=2, ensure_ascii=False)

    print(f"Successfully merged knowledge into {system_path}")

if __name__ == "__main__":
    merge_knowledge()
