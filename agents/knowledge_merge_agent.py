import os
import json
from datetime import datetime, UTC
from .base_agent import BaseAgent, Blackboard

class KnowledgeMergeAgent(BaseAgent):
    """
    KnowledgeMergeAgent (Python Implementation)
    Responsible for merging market intelligence from various scrapers
    into the consolidated system knowledge base.
    """
    def __init__(self):
        super().__init__("KnowledgeMergeAgent",
                         dependencies=["informatic_magazine_scraped"],
                         provides=["knowledge_consolidation_status"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("🚀 [KnowledgeMergeAgent] Starting knowledge consolidation cycle...")

        knowledge_dir = os.path.join(os.getcwd(), 'data/knowledge')
        informatic_json_path = os.path.join(knowledge_dir, 'informatic_magazine.json')
        system_knowledge_path = os.path.join(knowledge_dir, 'system_knowledge.json')
        knowledge_merge_md_path = os.path.join(os.getcwd(), 'KNOWLEDGE_MERGE.md')

        if not os.path.exists(informatic_json_path):
            self.logger.warning(f"⚠️ [KnowledgeMergeAgent] Scraped data not found at {informatic_json_path}")
            return {"status": "skipped", "reason": "No data to merge"}

        try:
            # 1. Load scraped data
            with open(informatic_json_path, 'r', encoding='utf-8') as f:
                scraped_data = json.load(f)

            # 2. Update system_knowledge.json (TypeScript-compatible structure)
            system_knowledge = {"typescript_sections": []}
            if os.path.exists(system_knowledge_path):
                with open(system_knowledge_path, 'r', encoding='utf-8') as f:
                    system_knowledge = json.load(f)

            # Use top 50 posts for a better balance between breadth and performance
            max_posts = 50
            new_section = {
                "title": scraped_data["title"],
                "metadata": {
                    "source": scraped_data["source"],
                    "analyzedAt": scraped_data["analyzedAt"],
                    "description": scraped_data["description"],
                    "signature": scraped_data["signature"]
                },
                "sections": [
                    {
                        "header": post["title"],
                        "content": post["content"]
                    } for post in scraped_data["posts"][:max_posts]
                ]
            }

            # Deduplicate by title
            system_knowledge["typescript_sections"] = [
                s for s in system_knowledge.get("typescript_sections", [])
                if s["title"] != scraped_data["title"]
            ]
            system_knowledge["typescript_sections"].append(new_section)

            with open(system_knowledge_path, 'w', encoding='utf-8') as f:
                json.dump(system_knowledge, f, indent=2, ensure_ascii=False)

            # 3. Update KNOWLEDGE_MERGE.md
            with open(knowledge_merge_md_path, 'r', encoding='utf-8') as f:
                md_content = f.read()

            now = datetime.now(UTC).isoformat().replace('+00:00', 'Z')
            relationship_text = f"Confirmed relationship with {scraped_data['source']} as an intelligence source. Scraped {len(scraped_data['posts'])} posts across multiple pages."

            observation_block = f"""
## Autonomous Observation
- **Date**: {now}
- **Target**: {scraped_data['source']}
- **Title**: {scraped_data['title']}
- **Relationship Map**: {relationship_text}
- **Signature**: {scraped_data['signature']}
"""

            # Remove previous observation of the same target to avoid duplication
            target_str = f"- **Target**: {scraped_data['source']}"
            if target_str in md_content:
                # Naive implementation: remove all blocks containing the target
                lines = md_content.split('\n')
                new_lines = []
                in_target_block = False

                # First pass: identify start of blocks
                blocks = []
                current_block = []
                for line in lines:
                    if line.startswith("## Autonomous Observation"):
                        if current_block: blocks.append(current_block)
                        current_block = [line]
                    else:
                        current_block.append(line)
                if current_block: blocks.append(current_block)

                # Second pass: filter out blocks with our target
                filtered_blocks = [b for b in blocks if target_str not in "\n".join(b)]
                md_content = "\n".join(["\n".join(b) for b in filtered_blocks])

            # Insert the new observation at the top of the observation list
            insert_point = "## Autonomous Observation"
            if insert_point in md_content:
                md_content = md_content.replace(insert_point, observation_block + "\n" + insert_point, 1)
            else:
                md_content += "\n" + observation_block

            # Clean up potential multiple signatures and ensure it's at the end
            sig = scraped_data["signature"]
            md_content = md_content.replace(sig, "").strip()
            md_content = md_content + "\n\n" + sig + "\n"

            with open(knowledge_merge_md_path, 'w', encoding='utf-8') as f:
                f.write(md_content)

            self.logger.info("✅ [KnowledgeMergeAgent] Successfully merged intelligence and updated system matrix.")
            return {"status": "success", "merged_items": len(scraped_data["posts"])}

        except Exception as e:
            self.logger.error(f"❌ [KnowledgeMergeAgent] Consolidation failed: {e}")
            raise e

if __name__ == "__main__":
    import asyncio
    import logging
    logging.basicConfig(level=logging.INFO)
    agent = KnowledgeMergeAgent()
    blackboard = Blackboard()
    asyncio.run(agent.run([], blackboard))
