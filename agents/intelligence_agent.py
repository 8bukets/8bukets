import json
import os
from .base_agent import BaseAgent
from typing import Dict, Any

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("Intelligence Agent")
        self.memory_file = "agent_memory.json"
        self.iq = 25

    def load_memory(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save_memory(self, memory):
        with open(self.memory_file, 'w') as f:
            json.dump(memory, f, indent=4)

    def process(self, analysis_result: Dict) -> Dict:
        self.log("Extracting intelligence...")

        memory = self.load_memory()
        run_count = memory.get('run_count', 0) + 1
        self.iq = min(200, 25 + (run_count * 0.1))  # IQ grows with experience
        memory['run_count'] = run_count
        memory['current_iq'] = self.iq
        self.save_memory(memory)

        keywords = [w[0] for w in analysis_result.get('common_keywords', [])]

        insight = "Neutral"
        if "available" in keywords or "new" in keywords:
            insight = "Growth/Expansion Phase"

        self.log(f"Current IQ: {self.iq:.1f}")

        return {
            "strategic_insight": insight,
            "focus_areas": keywords[:3],
            "iq_score": self.iq,
            "learning_iteration": run_count
        }
