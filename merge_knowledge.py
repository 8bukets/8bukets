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

    system_knowledge["google_innovation_ai"] = innovation_data
    system_knowledge["ai_agents_structured"] = agents_data

    with open(system_path, "w", encoding="utf-8") as f:
        json.dump(system_knowledge, f, indent=4, ensure_ascii=False)

    print(f"Merged knowledge into {system_path}")

if __name__ == "__main__":
    merge_knowledge()
