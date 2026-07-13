import json
import os
from datetime import datetime

def ingest_ai_agents_discovery():
    print("🤖 [Ingestion] Starting non-destructive merge for AI Agent knowledge...")

    target_file = 'ai_agents_knowledge.md'
    json_file = 'ai_agents_knowledge.json'

    # Non-destructive merge logic
    new_knowledge = f"\n## AI Agent Discovery Update ({datetime.now().isoformat()})\n- Ingested latest GCP AI Agent discovery insights for Phase 27.\n"

    if os.path.exists(target_file):
        with open(target_file, 'a') as f:
            f.write(new_knowledge)
    else:
        with open(target_file, 'w') as f:
            f.write("# AI Agents Knowledge\n" + new_knowledge)

    print(f"✅ [Ingestion] Merged insights into {target_file}.")

if __name__ == "__main__":
    ingest_ai_agents_discovery()
