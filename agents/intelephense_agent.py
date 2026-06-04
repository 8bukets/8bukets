import json
import os
from .base_agent import BaseAgent, Blackboard

class IntelephenseAgent(BaseAgent):
    """
    Agent that provides Intelephense documentation knowledge.
    """
    def __init__(self):
        super().__init__("IntelephenseAgent",
                         dependencies=[],
                         provides=["intelephense_docs"])
        self.knowledge_file = "intelephense_docs.json"

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Loading Intelephense Documentation...")

        if not os.path.exists(self.knowledge_file):
            self.logger.error(f"Knowledge file {self.knowledge_file} not found.")
            return {"intelephense_docs": {}}

        try:
            with open(self.knowledge_file, "r", encoding="utf-8") as f:
                intelephense_docs = json.load(f)

            self.logger.info("Intelephense Documentation loaded successfully.")
            return {"intelephense_docs": intelephense_docs}
        except Exception as e:
            self.logger.error(f"Failed to load Intelephense knowledge: {e}")
            return {"intelephense_docs": {}}
