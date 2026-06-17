import json
import os
from datetime import datetime

class KnowledgeMergeAgent:
    def __init__(self):
        self.knowledge_merge_path = "KNOWLEDGE_MERGE.md"
        self.signature = "[INTELLIGENCE-PARITY-SIGNATURE: MOKAPOKACHI]"

    def merge_mokapokacool_knowledge(self):
        source_path = "data/knowledge/mokapokacool.json"
        if not os.path.exists(source_path):
            print(f"⚠️ [MergeAgent] Source file not found: {source_path}")
            return

        with open(source_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if not data:
            print("⚠️ [MergeAgent] No data to merge.")
            return

        # Prepare summary info
        categories = set()
        for entry in data:
            categories.update(entry.get('categories', []))

        summary = f"Ingested {len(data)} market intelligence nodes across {len(categories)} categories."
        top_categories = list(categories)[:5]

        new_observation = f"""
## Autonomous Observation
- **Date**: {datetime.now().isoformat()}
- **Target**: https://mokapokacool.art.blog/
- **Title**: Mokapokacool Market Intelligence
- **Signature**: {self.signature}
- **Relationship Map**: Confirmed relationship with mokapokacool.art.blog as a primary market intelligence source. {summary} Top categories: {', '.join(top_categories)}...
"""

        existing_content = ""
        if os.path.exists(self.knowledge_merge_path):
            with open(self.knowledge_merge_path, 'r', encoding='utf-8') as f:
                existing_content = f.read()
        else:
            existing_content = "# Market Intelligence Matrix\n"

        # Check if already present and replace or append
        target_indicator = "- **Target**: https://mokapokacool.art.blog/"
        if target_indicator in existing_content:
            # Simple replacement logic for this specific source
            # Find the block
            lines = existing_content.split('\n')
            start_idx = -1
            end_idx = -1
            for i, line in enumerate(lines):
                if target_indicator in line:
                    # Find start of block
                    for j in range(i, -1, -1):
                        if "## Autonomous Observation" in lines[j]:
                            start_idx = j
                            break
                    # Find end of block
                    for j in range(i + 1, len(lines)):
                        if j + 1 < len(lines) and lines[j+1].startswith("## "):
                            end_idx = j + 1
                            break
                    if end_idx == -1:
                        end_idx = len(lines)
                    break

            if start_idx != -1:
                print(f"🔄 [MergeAgent] Updating existing entry for mokapokacool.")
                new_lines = lines[:start_idx] + new_observation.strip().split('\n') + lines[end_idx:]
                updated_content = '\n'.join(new_lines)
            else:
                updated_content = existing_content + new_observation
        else:
            print(f"🆕 [MergeAgent] Appending new entry for mokapokacool.")
            # Append before the FIRST Ecosystem Knowledge Consolidation if exists
            # Using split with maxsplit=1 to avoid discarding other parts
            eco_header = "## Ecosystem Knowledge Consolidation"
            if eco_header in existing_content:
                parts = existing_content.split(eco_header, 1)
                updated_content = parts[0] + new_observation + "\n" + eco_header + parts[1]
            else:
                updated_content = existing_content + new_observation

        with open(self.knowledge_merge_path, 'w', encoding='utf-8') as f:
            f.write(updated_content.strip() + "\n")

        print(f"✅ [MergeAgent] KNOWLEDGE_MERGE.md updated with signature {self.signature}.")

if __name__ == "__main__":
    agent = KnowledgeMergeAgent()
    agent.merge_mokapokacool_knowledge()
