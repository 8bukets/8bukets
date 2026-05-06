import os
import json
from .base_agent import BaseAgent, Blackboard

class KnowledgeAgent(BaseAgent):
    """
    KnowledgeAgent: Provides structured AI agent knowledge (definitions, use cases, benefits)
    from the synthesized data to the Blackboard.
    """
    def __init__(self):
        super().__init__("KnowledgeAgent", dependencies=[], provides=["ai_agent_knowledge"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Providing structured AI agent knowledge to the ecosystem...")

        knowledge_file = "data/ai_agents_knowledge.json"
        knowledge_data = []

        if os.path.exists(knowledge_file):
            try:
                with open(knowledge_file, "r", encoding="utf-8") as f:
                    knowledge_data = json.load(f)
                self.logger.info(f"Loaded {len(knowledge_data)} knowledge entries from {knowledge_file}")
            except Exception as e:
                self.logger.error(f"Error reading knowledge file: {e}")
        else:
            self.logger.warning(f"Knowledge file {knowledge_file} not found. Running with empty knowledge base.")

        # Synthesize a more compact summary for other agents to consume easily
        synthesized = {
            "entries": knowledge_data,
            "all_definitions": [d for entry in knowledge_data for d in entry.get("definitions", [])],
            "all_use_cases": [u for entry in knowledge_data for u in entry.get("use_cases", [])],
            "all_benefits": [b for entry in knowledge_data for b in entry.get("benefits", [])],
            "all_tools": list(set([t for entry in knowledge_data for t in entry.get("google_cloud_tools", [])]))
        }

        return {"ai_agent_knowledge": synthesized}
