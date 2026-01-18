from .base_agent import BaseAgent
from typing import Dict, Any
import json
import os

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("Intelligence Agent")
        self.memory_file = "intelligence_memory.json"

    def load_memory(self) -> Dict:
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save_memory(self, memory: Dict):
        with open(self.memory_file, 'w') as f:
            json.dump(memory, f, indent=4)

    def process(self, analysis_result: Dict) -> Dict:
        self.log("Extracting intelligence...")
        memory = self.load_memory()

        keywords = [w[0] for w in analysis_result.get('common_keywords', [])]

        # Learning: Track keyword frequency over time
        keyword_history = memory.get('keyword_history', {})
        for k in keywords:
            keyword_history[k] = keyword_history.get(k, 0) + 1
        memory['keyword_history'] = keyword_history
        self.save_memory(memory)

        insight = "Neutral"
        if "available" in keywords or "new" in keywords:
            insight = "Growth/Expansion Phase"

        # Evolving insight based on history
        top_historical = sorted(keyword_history.items(), key=lambda x: x[1], reverse=True)[:3]
        historical_context = f"Consistent focus on: {', '.join([k[0] for k in top_historical])}"

        return {
            "strategic_insight": insight,
            "historical_context": historical_context,
            "focus_areas": keywords[:3]
        }
