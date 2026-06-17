import os
import json
import logging
from datetime import datetime
from .base_agent import BaseAgent, Blackboard

class KnowledgeMergeAgent(BaseAgent):
    """
    KnowledgeMergeAgent

    This agent is responsible for consolidating market intelligence from various
    scraped sources into the unified system knowledge base.
    """
    def __init__(self):
        super().__init__("KnowledgeMergeAgent",
                         dependencies=["scraped_data"],
                         provides=["consolidated_knowledge"])
        self.knowledge_dir = os.path.join(os.getcwd(), 'data/knowledge')
        self.system_knowledge_path = os.path.join(self.knowledge_dir, 'system_knowledge.json')
        self.knowledge_merge_md_path = os.path.join(os.getcwd(), 'KNOWLEDGE_MERGE.md')

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("🚀 [KnowledgeMergeAgent] Starting knowledge consolidation pulse...")

        if not os.path.exists(self.knowledge_dir):
            os.makedirs(self.knowledge_dir, exist_ok=True)

        # 1. Load existing system knowledge
        system_knowledge = {"typescript_sections": []}
        if os.path.exists(self.system_knowledge_path):
            try:
                with open(self.system_knowledge_path, 'r', encoding='utf-8') as f:
                    system_knowledge = json.load(f)
            except Exception as e:
                self.logger.error(f"❌ Failed to load existing system knowledge: {e}")

        # 2. Identify all knowledge sources in the directory
        source_files = [f for f in os.listdir(self.knowledge_dir) if f.endswith('_knowledge.json') and f != 'system_knowledge.json']

        consolidated_count = 0
        new_observations = []

        for source_file in source_files:
            source_path = os.path.join(self.knowledge_dir, source_file)
            try:
                with open(source_path, 'r', encoding='utf-8') as f:
                    source_data = json.load(f)

                title = source_data.get('title', 'Unknown Source')
                url = source_data.get('source', '')

                # Check if this source already exists in system_knowledge
                existing_idx = -1
                for i, section in enumerate(system_knowledge.get('typescript_sections', [])):
                    if section.get('title') == title or (section.get('metadata') and section.get('metadata').get('source') == url):
                        existing_idx = i
                        break

                new_section = {
                    "title": title,
                    "metadata": {
                        "source": url,
                        "analyzedAt": source_data.get('analyzedAt', datetime.utcnow().isoformat() + "Z"),
                        "description": source_data.get('description', '')
                    },
                    "sections": source_data.get('sections', [])
                }

                if existing_idx != -1:
                    system_knowledge['typescript_sections'][existing_idx] = new_section
                    self.logger.info(f"🔄 Updated knowledge from: {title}")
                else:
                    system_knowledge.setdefault('typescript_sections', []).append(new_section)
                    self.logger.info(f"➕ Added new knowledge from: {title}")

                consolidated_count += 1

                # Prepare observation entry for KNOWLEDGE_MERGE.md
                sections = source_data.get('sections', [])
                top_headers = [s.get('header') for s in sections[:3]]
                summary_info = f" Extracted key topics: {', '.join(top_headers)}..." if top_headers else ""

                observation = f"""
## Autonomous Observation
- **Date**: {datetime.utcnow().isoformat() + "Z"}
- **Target**: {url}
- **Title**: {title}
- **Relationship Map**: Confirmed relationship with {url} (Title: {title}) as an intelligence source.{summary_info} (Content Length: {len(str(sections))} chars)
"""
                new_observations.append(observation)

            except Exception as e:
                self.logger.error(f"❌ Failed to process source file {source_file}: {e}")

        # 3. Save updated system knowledge
        with open(self.system_knowledge_path, 'w', encoding='utf-8') as f:
            json.dump(system_knowledge, f, indent=2, ensure_ascii=False)

        # 4. Update KNOWLEDGE_MERGE.md
        if new_observations:
            self._update_knowledge_merge_md(new_observations)

        self.logger.info(f"✅ [KnowledgeMergeAgent] Consolidation complete. Processed {consolidated_count} sources.")
        return {"consolidated_count": consolidated_count, "status": "SUCCESS"}

    def _update_knowledge_merge_md(self, new_observations):
        content = ""
        if os.path.exists(self.knowledge_merge_md_path):
            with open(self.knowledge_merge_md_path, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            content = "# Market Intelligence Matrix\n"

        for obs in new_observations:
            # Check if this target is already observed to avoid duplicate sections
            # Extract target URL from observation
            target_line = [line for line in obs.split('\n') if '- **Target**:' in line]
            if target_line:
                target_url = target_line[0].split(': ')[1].strip()
                target_indicator = f"- **Target**: {target_url}"

                if target_indicator in content:
                    # Basic replacement of existing block for that target
                    # In a production scenario, we'd use more robust parsing
                    self.logger.info(f"ℹ️ Knowledge for {target_url} already exists in KNOWLEDGE_MERGE.md. Skipping append to prevent spam.")
                    continue

            # Prepend new observations after the main header
            if "# Market Intelligence Matrix" in content:
                content = content.replace("# Market Intelligence Matrix", "# Market Intelligence Matrix\n" + obs)
            else:
                content = obs + "\n" + content

        with open(self.knowledge_merge_md_path, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == "__main__":
    # For testing
    import asyncio
    logging.basicConfig(level=logging.INFO)
    agent = KnowledgeMergeAgent()
    asyncio.run(agent.run([], {}))
