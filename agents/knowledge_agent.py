from .base_agent import BaseAgent, Blackboard
import json
import os

class KnowledgeAgent(BaseAgent):
    """
    Agent that provides foundational AI Agent knowledge scraped from Google Cloud.
    """
    def __init__(self):
        super().__init__("KnowledgeAgent",
                         dependencies=[],
                         provides=["ai_agents_definitions", "agent_best_practices"])
        self.knowledge_file = "ai_agents_knowledge.json"

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Loading AI Agent Knowledge from Google Cloud Discover...")

        if not os.path.exists(self.knowledge_file):
            self.logger.error(f"Knowledge file {self.knowledge_file} not found.")
            return {
                "ai_agents_definitions": {},
                "agent_best_practices": []
            }

        try:
            with open(self.knowledge_file, "r", encoding="utf-8") as f:
                knowledge = json.load(f)

            # Extract specific definitions and best practices
            definitions = {
                "ai_agent": knowledge.get("key-features-of-an-ai-agent", {}).get("content", ""),
                "differences": knowledge.get("what-is-the-difference-between-ai-agents,-ai-assistants,-and-bots", {}).get("content", ""),
                "types": knowledge.get("what-are-the-types-of-agents-in-ai", {}).get("content", "")
            }

            best_practices = [
                "Focus on reasoning, acting, observing, and planning.",
                "Implement self-refining capabilities for continuous improvement.",
                "Ensure robust memory management (short-term, long-term, episodic, consensus).",
                "Utilize appropriate tools for environment interaction."
            ]

            return {
                "ai_agents_definitions": definitions,
                "agent_best_practices": best_practices
            }
        except Exception as e:
            self.logger.error(f"Failed to load knowledge: {e}")
            return {
                "ai_agents_definitions": {},
                "agent_best_practices": []
            }
