import json
from typing import Dict, Any
from .base_agent import BaseAgent

DNA_FILE = "dna.json"

class LearningAgent(BaseAgent):
    """
    Agent responsible for self-optimization of system parameters (DNA).
    """
    def __init__(self):
        super().__init__("Learning Agent")

    def process(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        self.log("Analyzing system performance and evolving DNA...")

        try:
            with open(DNA_FILE, 'r', encoding='utf-8') as f:
                dna = json.load(f)
        except FileNotFoundError:
            dna = {"concurrency": 2, "scrape_timeout": 30}

        total_duration = metrics.get('total_duration', 0)
        self.log(f"Total pipeline duration: {total_duration:.2f}s")

        # Evolutionary Logic:
        # If too slow (> 5s), try increasing concurrency (up to a limit).
        # If very fast (< 1s), maybe we can throttle to save resources (or just keep it).
        # For this 'Bolt' optimization, we always want speed, so let's ramp up concurrency if we are slow.

        changed = False
        if total_duration > 2.0:
            current_concurrency = dna.get('concurrency', 1)
            if current_concurrency < 5:
                dna['concurrency'] = current_concurrency + 1
                changed = True
                self.log(f"Evolving: Increasing concurrency to {dna['concurrency']}")

        if changed:
            with open(DNA_FILE, 'w', encoding='utf-8') as f:
                json.dump(dna, f, indent=4)

        return {"dna_updated": changed, "current_dna": dna}
