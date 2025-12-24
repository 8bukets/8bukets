from .base import Agent
import os
import json

class IntelligenceAgent(Agent):
    def __init__(self):
        super().__init__("IntelligenceAgent")
        self.memory_file = "agent_memory.json"

    def perform_task(self, context=None):
        # Load memory (simulated learning)
        memory = self.load_memory()
        run_count = memory.get('run_count', 0) + 1
        memory['run_count'] = run_count
        self.save_memory(memory)

        # "Evolving" Strategy based on experience (runs)
        if run_count < 5:
            strategy = "Phase 1: Data Accumulation. Focus on high-volume keywords."
        elif run_count < 10:
            strategy = "Phase 2: Optimization. Refine ad targeting based on initial data."
        else:
            strategy = "Phase 3: Scaling. Expand to adjacent niches and increase ad spend."

        # Analyze context (Collaboration)
        keywords = context.get('keywords', []) if context else []
        if keywords:
            top_kw = keywords[0][0]
            trend_alert = f"Detected high interest in '{top_kw}'. Adjusting priorities."
        else:
            trend_alert = "Steady state. No immediate trend spikes."

        self.results['strategy'] = strategy
        self.results['trend_alert'] = trend_alert
        self.results['experience_level'] = f"Level {run_count}"

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
            json.dump(memory, f)
