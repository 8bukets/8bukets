from markposition.agents.base_agent import BaseAgent
from markposition.agents.vector_memory import VectorMemory

class KnowledgeAgent(BaseAgent):
    """
    Agent that synthesizes internal patterns and external research into
    long-term structural knowledge.
    """
    execution_stage = 4 # Runs after Research but before high-level strategy

    def __init__(self):
        super().__init__("KnowledgeAgent")
        self.vm = VectorMemory()

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Synthesizing System Knowledge...")

        research = context.get("research_notes", [])
        patterns = context.get("market_patterns", [])

        knowledge_base_entries = []

        # 1. Correlate Research with Market Patterns
        for pattern in patterns:
            # Semantic search for relevant research
            related_research = self.vm.search(pattern, top_k=2)
            for res in related_research:
                entry = f"Knowledge Synthesis: '{pattern}' is supported by external intelligence: {res['metadata'].get('text')}"
                knowledge_base_entries.append(entry)

        # 2. Persist Synthesis
        for entry in knowledge_base_entries:
            self.vm.add_entry(entry, {"type": "knowledge_synthesis", "agent": self.name})

        return {"knowledge_synthesis": knowledge_base_entries}
