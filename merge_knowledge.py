import json
import os

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
            agents_data = json.load(f)

    # Prepare the unified structure
    # Memories suggest a flat key structure for distinct sections
    system_knowledge = {}
    if os.path.exists(system_path):
        try:
            with open(system_path, "r", encoding="utf-8") as f:
                system_knowledge = json.load(f)
        except Exception:
            pass

    # Merge innovation data
    existing_innovation = {item["url"]: item for item in system_knowledge.get("google_innovation_ai", [])}
    for item in innovation_data:
        existing_innovation[item["url"]] = item
    system_knowledge["google_innovation_ai"] = list(existing_innovation.values())

    # Merge agents data
    existing_agents = {item["url"]: item for item in system_knowledge.get("ai_agents_structured", [])}
    if isinstance(agents_data, dict):
        agents_data = [{"url": k, **v} for k, v in agents_data.items()]
    for item in agents_data:
        if item["url"] in existing_agents:
            # Smart merge definitions/tools
            existing = existing_agents[item["url"]]

            # Definitions
            existing_defs = {d["term"]: d["text"] for d in existing.get("definitions", [])}
            for d in item.get("definitions", []):
                existing_defs[d["term"]] = d["text"]
            existing["definitions"] = [{"term": k, "text": v} for k, v in existing_defs.items()]

            # Tools
            existing_tools = set(existing.get("google_cloud_tools", []))
            existing_tools.update(item.get("google_cloud_tools", []))
            existing["google_cloud_tools"] = sorted(list(existing_tools))

            # Benefits & Use Cases
            existing_ucs = {u["title"]: u["description"] for u in existing.get("use_cases", [])}
            for u in item.get("use_cases", []):
                existing_ucs[u["title"]] = u["description"]
            existing["use_cases"] = [{"title": k, "description": v} for k, v in existing_ucs.items()]

            existing_bens = {b["title"]: b["description"] for b in existing.get("benefits", [])}
            for b in item.get("benefits", []):
                existing_bens[b["title"]] = b["description"]
            existing["benefits"] = [{"title": k, "description": v} for k, v in existing_bens.items()]
        else:
            existing_agents[item["url"]] = item

    system_knowledge["ai_agents_structured"] = list(existing_agents.values())

    with open(system_path, "w", encoding="utf-8") as f:
        json.dump(system_knowledge, f, indent=4, ensure_ascii=False)

    with open("CONSOLIDATED_KNOWLEDGE.md", "a", encoding="utf-8") as f:
        f.write("\n---\nAll the best - https://markposition.wordpress.com\n")
    print(f"Merged knowledge into {system_path}")

if __name__ == "__main__":
    merge_knowledge()
