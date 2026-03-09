from markposition.agents.base_agent import BaseAgent
from markposition.agents.vector_memory import VectorMemory
import json

class LearningAgent(BaseAgent):
    """
    Autonomous agent that learns from system execution history and proposes
    architectural or strategic optimizations.
    """
    execution_stage = 10 # Post-analysis and post-reasoning

    def __init__(self):
        super().__init__("LearningAgent")
        self.vm = VectorMemory()

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Executing Autonomous Learning & Optimization...")

        # 1. Retrieve historical patterns
        historical_patterns = self.vm.search("Market Pattern", top_k=10)

        # 2. Analyze evolution of findings
        dominant_themes = {}
        for p in historical_patterns:
            text = p['metadata'].get('text', '')
            # Simple theme extraction
            if "Category" in text:
                theme = text.split("Category:")[1].split("(")[0].strip()
                dominant_themes[theme] = dominant_themes.get(theme, 0) + 1

        # 3. Propose Optimizations
        optimizations = []
        if len(dominant_themes) > 0:
            top_theme = max(dominant_themes, key=dominant_themes.get)
            optimizations.append(f"Learning: Dominant theme '{top_theme}' identified across multiple cycles. Priority assigned.")

        # 4. Meta-Feedback for Orchestrator
        cycle_status = context.get("autonomous_status", "STABLE")
        if cycle_status == "STABLE" and len(historical_patterns) > 5:
            optimizations.append("System Optimization: Increasing agent concurrency for Stage 5 based on stable performance.")

        # 5. Persist Learnings
        for opt in optimizations:
             self.vm.add_entry(opt, {"type": "system_optimization", "agent": self.name})

        return {
            "system_optimizations": optimizations,
            "learned_themes": dominant_themes
        }
